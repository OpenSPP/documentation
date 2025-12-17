---
myst:
  html_meta:
    "description": "How OpenSPP is structured as Odoo modules"
    "property=og:title": "Modules"
    "keywords": "OpenSPP, modules, Odoo addons, Odoo 19"
---

# Modules

OpenSPP is delivered as a set of **Odoo 19 addons** (modules). Implementations install only the modules needed for a
given country, program, or deployment.

## Naming and versioning

- OpenSPP modules follow the `spp_*` naming convention.
- Module versions follow the Odoo 19 series (for example `19.0.x.y.z`).

## Where module choices show up in the product

- Modules are installed via **Odoo Apps**.
- Installed modules control which OpenSPP menus, models, and capabilities are available.

This page will be expanded with V2-specific “what to install” guidance based on the implemented module architecture and
consolidation work.
