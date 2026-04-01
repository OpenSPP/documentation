# Part of OpenSPP. See LICENSE file for full copyright and licensing details.
from odoo import api, models


class EligibilityManagerRegistration(models.Model):
    """Register the CCT eligibility manager in the selection dropdown."""

    _inherit = "spp.eligibility.manager"

    @api.model
    def _selection_manager_ref_id(self):
        selection = super()._selection_manager_ref_id()
        new_manager = (
            "spp.program.membership.manager.cct",
            "CCT Eligibility (Income + Children)",
        )
        if new_manager not in selection:
            selection.append(new_manager)
        return selection
