# Part of OpenSPP. See LICENSE file for full copyright and licensing details.
import logging
from datetime import date

from dateutil.relativedelta import relativedelta

from odoo import _, fields, models

_logger = logging.getLogger(__name__)


class CCTEntitlementManager(models.Model):
    """Entitlement manager for conditional cash transfer programs.

    Calculates entitlements as:
        amount = base_amount + (per_child_amount * eligible_children)

    Where eligible_children is capped at max_children.
    """

    _name = "spp.program.entitlement.manager.cct"
    _inherit = [
        "spp.base.program.entitlement.manager",
        "spp.manager.source.mixin",
    ]
    _description = "CCT Entitlement Manager"

    IS_CASH_ENTITLEMENT = True

    base_amount = fields.Monetary(
        string="Base Amount per Household",
        default=1000.0,
        currency_field="currency_id",
        help="Fixed amount every eligible household receives.",
    )

    per_child_amount = fields.Monetary(
        string="Per-Child Top-Up",
        default=500.0,
        currency_field="currency_id",
        help="Additional amount per eligible child.",
    )

    max_children = fields.Integer(
        string="Maximum Children for Top-Up",
        default=5,
        help="Cap on the number of children counted for the top-up. "
        "Set to 0 for no cap.",
    )

    child_max_age = fields.Integer(
        string="Maximum Child Age",
        default=18,
        help="Children must be under this age to count for the top-up.",
    )

    currency_id = fields.Many2one(
        "res.currency",
        related="program_id.journal_id.currency_id",
        readonly=True,
    )

    def _count_eligible_children(self, group):
        """Count children under the age threshold in a household."""
        cutoff_date = date.today() - relativedelta(years=self.child_max_age)
        count = 0
        for membership in group.group_membership_ids:
            individual = membership.individual
            if (
                individual.birthdate
                and individual.birthdate >= cutoff_date
            ):
                count += 1
        return count

    def _calculate_amount(self, group):
        """Calculate entitlement amount for a household."""
        eligible_children = self._count_eligible_children(group)

        if self.max_children > 0:
            eligible_children = min(eligible_children, self.max_children)

        return self.base_amount + (self.per_child_amount * eligible_children)

    def prepare_entitlements(self, cycle, beneficiaries):
        """Create entitlement records for each beneficiary household."""
        # Avoid duplicates: check for existing entitlements in this cycle
        existing_partner_ids = self.env["spp.entitlement"].search([
            ("cycle_id", "=", cycle.id),
        ]).mapped("partner_id.id")

        entitlement_vals = []
        for membership in beneficiaries:
            partner = membership.partner_id
            if partner.id in existing_partner_ids:
                continue

            amount = self._calculate_amount(partner)

            entitlement_vals.append({
                "cycle_id": cycle.id,
                "partner_id": partner.id,
                "initial_amount": amount,
                "state": "draft",
                "is_cash_entitlement": True,
            })

        entitlements = self.env["spp.entitlement"]
        if entitlement_vals:
            entitlements = self.env["spp.entitlement"].create(entitlement_vals)

        return entitlements

    def set_pending_validation_entitlements(self, cycle):
        """Move draft entitlements to pending validation."""
        entitlements = self.env["spp.entitlement"].search([
            ("cycle_id", "=", cycle.id),
            ("state", "=", "draft"),
        ])
        if entitlements:
            entitlements.write({"state": "pending_validation"})

    def validate_entitlements(self, cycle):
        """Approve pending entitlements."""
        entitlements = self.env["spp.entitlement"].search([
            ("cycle_id", "=", cycle.id),
            ("state", "in", ["draft", "pending_validation"]),
        ])
        if entitlements:
            return self.approve_entitlements(entitlements)

    def approve_entitlements(self, entitlements):
        """Approve entitlements and mark them ready for payment."""
        err_count = 0
        error_messages = []

        for entitlement in entitlements:
            try:
                entitlement.write({"state": "approved"})
            except Exception as e:
                err_count += 1
                error_messages.append(str(e))

        error_message = "\n".join(error_messages) if error_messages else ""
        return (err_count, error_message)

    def cancel_entitlements(self, cycle):
        """Cancel all non-final entitlements in the cycle."""
        entitlements = self.env["spp.entitlement"].search([
            ("cycle_id", "=", cycle.id),
            ("state", "in", ["draft", "pending_validation", "approved"]),
        ])
        if entitlements:
            entitlements.write({"state": "cancelled"})
