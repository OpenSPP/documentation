# Part of OpenSPP. See LICENSE file for full copyright and licensing details.
import logging
from datetime import date

from dateutil.relativedelta import relativedelta

from odoo import _, fields, models

_logger = logging.getLogger(__name__)


class CCTEligibilityManager(models.Model):
    """Eligibility manager for conditional cash transfer programs.

    Filters households based on two criteria:
    1. Household income is at or below a configurable threshold
    2. Household has at least one child under a configurable age
    """

    _name = "spp.program.membership.manager.cct"
    _inherit = ["spp.program.membership.manager", "spp.manager.source.mixin"]
    _description = "CCT Eligibility Manager"

    max_income = fields.Float(
        string="Maximum Household Income",
        default=10000.0,
        help="Households with income above this amount are not eligible.",
    )

    child_max_age = fields.Integer(
        string="Maximum Child Age",
        default=18,
        help="Children must be under this age (in years) for the household to qualify.",
    )

    def _get_child_birthdate_cutoff(self):
        """Return the earliest birthdate for a child to be considered eligible."""
        return date.today() - relativedelta(years=self.child_max_age)

    def _get_eligible_group_ids(self):
        """Return IDs of groups that meet income and child-age criteria."""
        cutoff_date = self._get_child_birthdate_cutoff()

        # Find groups with income at or below the threshold
        groups = self.env["res.partner"].search([
            ("is_registrant", "=", True),
            ("is_group", "=", True),
            ("income", "<=", self.max_income),
        ])

        eligible_ids = []
        for group in groups:
            # Check if any member is a child under the age threshold
            for membership in group.group_membership_ids:
                individual = membership.individual
                if (
                    individual.birthdate
                    and individual.birthdate >= cutoff_date
                ):
                    eligible_ids.append(group.id)
                    break

        return eligible_ids

    def enroll_eligible_registrants(self, program_memberships):
        """Validate which program members meet the CCT criteria."""
        eligible_ids = self._get_eligible_group_ids()
        return program_memberships.filtered(
            lambda m: m.partner_id.id in eligible_ids
        )

    def verify_cycle_eligibility(self, cycle, membership):
        """Re-check CCT eligibility for cycle members."""
        eligible_ids = self._get_eligible_group_ids()
        return membership.filtered(
            lambda m: m.partner_id.id in eligible_ids
        )

    def import_eligible_registrants(self, state=None):
        """Import households matching CCT criteria into the program."""
        eligible_ids = self._get_eligible_group_ids()

        # Exclude already-enrolled households
        existing = self.env["spp.program.membership"].search([
            ("program_id", "=", self.program_id.id),
            ("partner_id", "in", eligible_ids),
        ]).mapped("partner_id.id")

        new_ids = [pid for pid in eligible_ids if pid not in existing]

        vals_list = [
            {
                "program_id": self.program_id.id,
                "partner_id": pid,
                "state": state or "draft",
            }
            for pid in new_ids
        ]

        if vals_list:
            self.env["spp.program.membership"].create(vals_list)

        return len(vals_list)
