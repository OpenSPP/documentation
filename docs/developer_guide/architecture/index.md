---
openspp:
  doc_status: draft
  products: [core]
---

# Architecture

**For: developers**

This section covers the technical architecture of OpenSPP V2. Understanding these concepts will help you navigate the codebase, extend the platform, and make informed design decisions.

## OpenSPP at a glance

OpenSPP is built on top of **Odoo 19** (OCA/OCB Community Edition) and follows Odoo's module-based architecture. The platform adds ~110 modules that provide social protection functionality on top of Odoo's ERP foundation.

### Key architectural choices

| Aspect              | Approach                                                                              |
| ------------------- | ------------------------------------------------------------------------------------- |
| **Foundation**      | Odoo 19 (OCA/OCB) — inherits ORM, views, security, workflow engine                    |
| **Registrants**     | Extend `res.partner` (Odoo's contact model) with `is_registrant` / `is_group` flags   |
| **Program logic**   | Strategy pattern via pluggable managers (eligibility, entitlements, cycles, payments) |
| **Expressions**     | CEL (Common Expression Language) for dynamic rules, scoring, and eligibility          |
| **API**             | REST API V2 with OAuth2, external IDs only, consent-based filtering                   |
| **No-code config**  | Studio modules for field builders, logic packs, and change request types              |
| **Background jobs** | `odoo-job-worker` for async processing (imports, bulk operations)                     |
| **Data protection** | Field-level classification, PII encryption (AES-256-GCM), audit logging               |

### Design principles

1. **Registry abstraction** — All beneficiary types (individuals, households, farmers, disaster-affected populations) are represented as registrants in a unified registry, differentiated by group types and custom fields rather than separate models.

2. **Extensible core** — The manager pattern lets deployments customize program behavior without modifying core modules. Need a different eligibility check? Write a new eligibility manager, not a fork.

3. **Dual customization** — Simple configuration through Studio (no-code), complex logic through custom modules (code). Studio handles 80% of customization needs.

4. **API-first interoperability** — External systems interact through the API V2, which exposes only external identifiers (never database IDs) and respects consent-based data access rules.

5. **Performance at scale** — Designed for millions of registrants with CEL-to-SQL compilation, variable caching, batch processing, and async job queues.

## Odoo concepts for OpenSPP developers

If you're new to Odoo, here are the key concepts you'll encounter when working with OpenSPP:

- **ORM** — Odoo uses its own ORM. Models are Python classes with `_name` (new model) or `_inherit` (extend existing model). Fields are declared as class attributes using `fields.Char()`, `fields.Many2one()`, etc. Data lives in PostgreSQL tables auto-managed by the ORM.
- **Views** — UI is defined in XML files using Odoo's view system (form, list/tree, kanban, search views). Views can be extended with XPath expressions without modifying the original.
- **Security** — Access control has three layers: user groups (`res.groups`), ACL rules (`ir.model.access.csv` files), and record rules (`ir.rule` for row-level filtering).
- **Data files** — XML and CSV files in a module's `data/` and `security/` directories are loaded on install/upgrade. They create records (views, menus, actions, ACLs, default data).
- **Inheritance** — Odoo supports class inheritance (`_inherit` to extend a model), prototype inheritance (`_inherit` + `_name` to copy), and view inheritance (XPath-based).

For comprehensive Odoo developer documentation, refer to the [Odoo 19 Developer Documentation](https://www.odoo.com/documentation/19.0/developer.html).

## Topics covered

- **[Module organization](module_organization.md)**: How modules are named, categorized, and depend on each other
- **[Data model](data_model.md)**: Core entities — registrants, programs, cycles, entitlements — and their relationships

```{toctree}
:maxdepth: 2
:hidden:

module_organization
data_model
```
