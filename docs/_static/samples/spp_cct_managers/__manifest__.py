# Part of OpenSPP. See LICENSE file for full copyright and licensing details.
{
    "name": "OpenSPP CCT Program Managers",
    "summary": "Custom managers for conditional cash transfer programs: "
    "income-based eligibility, per-child entitlements, and quarterly cycles.",
    "category": "OpenSPP/Core",
    "version": "19.0.2.0.0",
    "sequence": 1,
    "author": "OpenSPP.org",
    "website": "https://github.com/OpenSPP/OpenSPP2",
    "license": "LGPL-3",
    "development_status": "Alpha",
    "maintainers": [],
    "depends": [
        "spp_programs",
        "spp_security",
    ],
    "data": [
        # Security
        "security/ir.model.access.csv",
        # Views
        "views/eligibility_views.xml",
        "views/entitlement_views.xml",
        "views/cycle_views.xml",
    ],
    "application": False,
    "installable": True,
    "auto_install": False,
}
