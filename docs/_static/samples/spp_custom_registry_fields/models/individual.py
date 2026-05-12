# Part of OpenSPP. See LICENSE file for full copyright and licensing details.
import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class ResPartnerCustomFields(models.Model):
    """Add custom fields to the individual registry.

    Extends res.partner to add education level and head of household
    tracking for individual registrants.
    """

    _inherit = "res.partner"

    education_level_id = fields.Many2one(
        "spp.vocabulary.code",
        string="Education Level",
        domain="[('vocabulary_id.name', '=', 'Education Level')]",
        help="Highest level of education completed.",
    )

    is_head_of_household = fields.Boolean(
        string="Head of Household",
        default=False,
        help="Whether this individual is the head of their household.",
    )
