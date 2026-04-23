---
openspp:
  doc_status: draft
  products: [core]
---

# Module organization

**For: developers**

OpenSPP is built as a collection of Odoo modules that extend the base Odoo platform. Understanding how modules are organized and how they depend on each other is essential for navigating the codebase and building extensions.

## Naming conventions

All OpenSPP modules use the `spp_` prefix:

| Pattern | Meaning | Examples |
|---------|---------|----------|
| `spp_base_*` | Core foundation modules | `spp_base_common`, `spp_base_setting` |
| `spp_registry*` | Registrant management | `spp_registry`, `spp_registry_group_hierarchy` |
| `spp_programs*` | Program management | `spp_programs`, `spp_programs_sp`, `spp_programs_approval` |
| `spp_api_v2*` | REST API v2 endpoints | `spp_api_v2`, `spp_api_v2_data`, `spp_api_v2_cycles` |
| `spp_cel_*` | CEL expression modules | `spp_cel_domain`, `spp_cel_widget`, `spp_cel_event` |
| `spp_studio*` | No-code configuration | `spp_studio`, `spp_studio_events`, `spp_studio_change_requests` |
| `spp_dci*` | DCI protocol modules | `spp_dci`, `spp_dci_client`, `spp_dci_server_social` |
| `spp_gis*` | Geographic information | `spp_gis`, `spp_gis_indicators`, `spp_gis_report` |
| `spp_grm*` | Grievance redress | `spp_grm`, `spp_grm_programs`, `spp_grm_registry` |
| `spp_drims*` | Disaster relief | `spp_drims`, `spp_drims_sl`, `spp_drims_sl_demo` |
| `spp_*_demo*` | Demo data modules | `spp_mis_demo_v2`, `spp_drims_sl_demo`, `spp_grm_demo` |

## Module categories

Each module declares a `category` in its `__manifest__.py`. These categories group modules in the Odoo Apps interface:

| Category | Purpose | Examples |
|----------|---------|----------|
| `OpenSPP/Core` | Foundation modules required by most deployments | `spp_registry`, `spp_programs`, `spp_security` |
| `OpenSPP/Configuration` | Admin tools and no-code configuration | `spp_studio`, `spp_custom_field`, `spp_branding_kit` |
| `OpenSPP/Integration` | APIs, DCI, banking, external connectivity | `spp_api_v2`, `spp_dci`, `spp_banking` |
| `OpenSPP/GIS` | Geographic and spatial modules | `spp_gis`, `spp_area`, `spp_gis_indicators` |
| `OpenSPP/Identity` | Identification and key management | `spp_idpass`, `spp_key_management` |
| `OpenSPP/Infrastructure` | System-level modules | `spp_alerts`, `spp_audit` |
| `OpenSPP` | General-purpose modules | Various |

## Core dependency chain

The core modules form a clear dependency hierarchy:

```
spp_security          (access control primitives)
    |
    +-- spp_vocabulary    (code systems and controlled lists)
    |       |
    |       +-- spp_registry    (registrant/group management)
    |               |
    |               +-- spp_base_common    (common foundation, UI branding)
    |               |
    |               +-- spp_programs       (programs, cycles, entitlements, payments)
    |                       |
    |                       +-- spp_cel_domain    (CEL expressions)
    |                       +-- spp_approval      (approval workflows)
    |                       +-- spp_banking       (bank details)
    |                       +-- spp_area          (geographic areas)
    |                       +-- spp_service_points (service delivery points)
```

### Key dependencies explained

- **`spp_security`** is the lowest-level OpenSPP module. It provides access control groups and security primitives that all other modules depend on.
- **`spp_vocabulary`** provides controlled vocabulary lists (code systems). The registry uses vocabularies for ID types, relationship types, and other coded values.
- **`spp_registry`** extends Odoo's `res.partner` model to represent individuals and groups. It depends on `spp_vocabulary` for coded fields.
- **`spp_base_common`** is the typical entry point for installations. It pulls in `spp_registry` and adds UI branding and common settings.
- **`spp_programs`** is the largest core module. It provides the program management framework including the manager pattern for eligibility, entitlements, cycles, and payments.

## Module manifest structure

Every module has an `__manifest__.py` file following this pattern:

```python
{
    "name": "OpenSPP Programs",
    "version": "19.0.2.0.0",
    "category": "OpenSPP/Core",
    "license": "LGPL-3",
    "author": "OpenSPP.org",
    "website": "https://github.com/OpenSPP/OpenSPP2",
    "depends": [
        "spp_registry",
        "spp_banking",
        "spp_cel_domain",
        # ... other dependencies
    ],
    "data": [
        "security/groups.xml",
        "security/ir.model.access.csv",
        "views/program_views.xml",
        # ... data files
    ],
    "installable": True,
    "auto_install": False,
}
```

### Version format

Versions follow the pattern `{odoo_version}.{major}.{minor}.{patch}`:

- `19.0` — Odoo version
- `2.0.0` — OpenSPP module version (major.minor.patch)

## Third-party dependencies

OpenSPP includes several OCA (Odoo Community Association) and third-party module sets:

| Module set | Purpose |
|------------|---------|
| `server-ux` | OCA server UX improvements |
| `server-tools` | OCA server utilities |
| `server-backend` | OCA backend tools |
| `rest-framework` | OCA REST framework foundation |
| `odoo-job-worker` | Async job queue processing |
| `theme_openspp_muk` | OpenSPP UI theme (MUK-based) |
| `fastapi` | FastAPI integration for API V2 |
| `extendable` / `extendable_fastapi` | Pydantic model extension support |

These are installed automatically by the Docker build and available in the addons path.
