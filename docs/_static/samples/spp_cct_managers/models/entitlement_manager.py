# Part of OpenSPP. See LICENSE file for full copyright and licensing details.
from odoo import api, models


class EntitlementManagerRegistration(models.Model):
    """Register the CCT entitlement manager in the selection dropdown."""

    _inherit = "spp.program.entitlement.manager"

    @api.model
    def _selection_manager_ref_id(self):
        selection = super()._selection_manager_ref_id()
        new_manager = (
            "spp.program.entitlement.manager.cct",
            "CCT Entitlement (Base + Per-Child)",
        )
        if new_manager not in selection:
            selection.append(new_manager)
        return selection
