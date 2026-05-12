# Part of OpenSPP. See LICENSE file for full copyright and licensing details.
{
    "name": "OpenSPP Custom Registry Fields",
    "summary": "Adds education level and head of household fields to the individual registry.",
    "category": "OpenSPP/Configuration",
    "version": "19.0.2.0.0",
    "sequence": 1,
    "author": "OpenSPP.org",
    "website": "https://github.com/OpenSPP/OpenSPP2",
    "license": "LGPL-3",
    "development_status": "Alpha",
    "maintainers": [],
    "depends": [
        "spp_registry",
        "spp_security",
        "spp_vocabulary",
    ],
    "data": [
        # Security (must be first)
        "security/groups.xml",
        "security/ir.model.access.csv",
        # Views
        "views/individual_views.xml",
    ],
    "application": False,
    "installable": True,
    "auto_install": False,
}
