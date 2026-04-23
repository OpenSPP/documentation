# Part of OpenSPP. See LICENSE file for full copyright and licensing details.
import logging
from datetime import date

from dateutil.relativedelta import relativedelta

from odoo import _, fields, models

_logger = logging.getLogger(__name__)


QUARTER_START_MONTHS = {
    1: (1, 3),    # Q1: Jan-Mar
    2: (4, 6),    # Q2: Apr-Jun
    3: (7, 9),    # Q3: Jul-Sep
    4: (10, 12),  # Q4: Oct-Dec
}


class CCTCycleManager(models.Model):
    """Cycle manager for conditional cash transfer programs.

    Creates quarterly cycles aligned to calendar quarters (Q1-Q4).
    Automatically copies beneficiaries from the program when a new
    cycle is created.
    """

    _name = "spp.cycle.manager.cct"
    _inherit = ["spp.base.cycle.manager", "spp.manager.source.mixin"]
    _description = "CCT Cycle Manager (Quarterly)"

    is_auto_copy_beneficiaries = fields.Boolean(
        string="Auto-Copy Beneficiaries",
        default=True,
        help="Automatically copy enrolled beneficiaries from the program "
        "when a new cycle is created.",
    )

    def _get_quarter(self, d):
        """Return the quarter number (1-4) for a date."""
        return (d.month - 1) // 3 + 1

    def _get_quarter_dates(self, year, quarter):
        """Return (start_date, end_date) for a given quarter."""
        start_month, end_month = QUARTER_START_MONTHS[quarter]
        start_date = date(year, start_month, 1)
        # End date is the last day of the end month
        end_date = date(year, end_month, 1) + relativedelta(
            months=1, days=-1
        )
        return start_date, end_date

    def new_cycle(self, name, new_start_date, sequence):
        """Create a new quarterly cycle aligned to calendar quarters."""
        quarter = self._get_quarter(new_start_date)
        year = new_start_date.year

        start_date, end_date = self._get_quarter_dates(year, quarter)

        cycle_name = name or f"Q{quarter} {year}"

        cycle = self.env["spp.cycle"].create({
            "name": cycle_name,
            "program_id": self.program_id.id,
            "start_date": start_date,
            "end_date": end_date,
            "sequence": sequence,
        })

        # Auto-copy beneficiaries if enabled
        if self.is_auto_copy_beneficiaries:
            self.copy_beneficiaries_from_program(cycle)

        return cycle

    def check_eligibility(self, cycle, beneficiaries=None):
        """Delegate eligibility checking to the program's eligibility managers."""
        for manager in self.program_id.eligibility_manager_ids:
            mgr_impl = manager.manager_ref_id
            if mgr_impl:
                mgr_impl.verify_cycle_eligibility(cycle, beneficiaries)

        return {
            "type": "ir.actions.client",
            "tag": "display_notification",
            "params": {
                "title": _("Eligibility Check"),
                "message": _("Eligibility check completed."),
                "type": "info",
            },
        }

    def prepare_entitlements(self, cycle):
        """Delegate entitlement preparation to entitlement managers."""
        beneficiaries = self.env["spp.cycle.membership"].search([
            ("cycle_id", "=", cycle.id),
            ("state", "=", "enrolled"),
        ])

        for manager in self.program_id.entitlement_manager_ids:
            mgr_impl = manager.manager_ref_id
            if mgr_impl:
                mgr_impl.prepare_entitlements(cycle, beneficiaries)

    def validate_entitlements(self, cycle, cycle_memberships):
        """Delegate entitlement validation to entitlement managers."""
        for manager in self.program_id.entitlement_manager_ids:
            mgr_impl = manager.manager_ref_id
            if mgr_impl:
                mgr_impl.validate_entitlements(cycle)

    def approve_cycle(self, cycle, auto_approve=False, entitlement_manager=None):
        """Approve the cycle and optionally auto-approve entitlements."""
        if cycle.state != "to_approve":
            return

        cycle.write({"state": "approved"})

        if auto_approve and entitlement_manager:
            entitlement_manager.validate_entitlements(cycle)

    def copy_beneficiaries_from_program(self, cycle, state="enrolled"):
        """Copy enrolled program members into the cycle."""
        memberships = self.env["spp.program.membership"].search([
            ("program_id", "=", self.program_id.id),
            ("state", "=", "enrolled"),
        ])

        existing = self.env["spp.cycle.membership"].search([
            ("cycle_id", "=", cycle.id),
        ]).mapped("partner_id.id")

        vals_list = [
            {
                "cycle_id": cycle.id,
                "partner_id": m.partner_id.id,
                "state": state,
            }
            for m in memberships
            if m.partner_id.id not in existing
        ]

        if vals_list:
            self.env["spp.cycle.membership"].create(vals_list)

    def add_beneficiaries(self, cycle, beneficiaries, state="draft"):
        """Add specific beneficiaries to the cycle."""
        existing = self.env["spp.cycle.membership"].search([
            ("cycle_id", "=", cycle.id),
        ]).mapped("partner_id.id")

        vals_list = [
            {
                "cycle_id": cycle.id,
                "partner_id": pid,
                "state": state,
            }
            for pid in beneficiaries
            if pid not in existing
        ]

        if vals_list:
            self.env["spp.cycle.membership"].create(vals_list)

    def issue_payments(self, cycle):
        """Delegate payment processing to payment managers."""
        for manager in self.program_id.payment_manager_ids:
            mgr_impl = manager.manager_ref_id
            if mgr_impl:
                mgr_impl.prepare_payments(cycle)

    def mark_distributed(self, cycle):
        """Set the cycle state to distributed."""
        cycle.write({"state": "distributed"})

    def mark_ended(self, cycle):
        """Set the cycle state to ended."""
        cycle.write({"state": "ended"})

    def mark_cancelled(self, cycle):
        """Set the cycle state to cancelled."""
        cycle.write({"state": "cancelled"})

    def on_start_date_change(self, cycle):
        """Recalculate quarter dates when start date changes."""
        quarter = self._get_quarter(cycle.start_date)
        year = cycle.start_date.year
        start_date, end_date = self._get_quarter_dates(year, quarter)

        cycle.write({
            "name": f"Q{quarter} {year}",
            "start_date": start_date,
            "end_date": end_date,
        })

    def on_state_change(self, cycle):
        """No additional logic on state change."""
        pass
