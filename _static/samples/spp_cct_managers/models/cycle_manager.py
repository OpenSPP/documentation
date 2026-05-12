# Part of OpenSPP. See LICENSE file for full copyright and licensing details.
from odoo import api, models


class CycleManagerRegistration(models.Model):
    """Register the CCT cycle manager in the selection dropdown."""

    _inherit = "spp.cycle.manager"

    @api.model
    def _selection_manager_ref_id(self):
        selection = super()._selection_manager_ref_id()
        new_manager = (
            "spp.cycle.manager.cct",
            "CCT Quarterly Cycle",
        )
        if new_manager not in selection:
            selection.append(new_manager)
        return selection
