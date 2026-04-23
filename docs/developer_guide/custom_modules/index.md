---
openspp:
  doc_status: draft
  products: [core]
---

# Custom modules

**For: developers**

This section walks you through creating a custom Odoo module for OpenSPP. OpenSPP modules follow standard Odoo module conventions with additional naming rules, security patterns, and mixins specific to the platform.

## Before you start

Make sure you have:

- A working {doc}`development environment <../setup/index>`
- Basic understanding of the {doc}`architecture <../architecture/index>` (especially the {doc}`module organization <../architecture/module_organization>` and {doc}`data model <../architecture/data_model>`)

## Quick start checklist

Creating a new OpenSPP module involves these steps:

1. **Scaffold** — Create the directory structure, manifest, and init files
2. **Models** — Define your models using the `spp.*` namespace with correct field naming
3. **Security** — Set up the three-tier group hierarchy, ACLs, and record rules
4. **Views** — Create form, list, and search views with the correct XML ID naming
5. **Mixins** — Integrate OpenSPP mixins for approval workflows, source tracking, etc.
6. **Tests** — Write tests using `TransactionCase` with role-based access testing

## Topics covered

- **[Module scaffold](scaffold.md)**: Directory structure, manifest, and initial files
- **[Models](models.md)**: The `spp.*` namespace, field naming rules, and model patterns
- **[Security](security.md)**: Three-tier group architecture, ACLs, and record rules
- **[Views and menus](views.md)**: XML ID conventions, view patterns, and menu structure
- **[Mixins](mixins.md)**: Available OpenSPP mixins and when to use them
- **[Testing](testing.md)**: Test patterns, helpers, and role-based testing
- **[Example: custom registry fields](example.md)**: Complete walkthrough building a module that adds fields to the individual registry

```{toctree}
:maxdepth: 2
:hidden:

scaffold
models
security
views
mixins
testing
example
```
