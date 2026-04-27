---
openspp:
  doc_status: draft
  products: [core]
---

# Configuration vs customization

OpenSPP, built on the Odoo framework, supports two distinct ways to adapt the system to a country's needs:

- **Configuration** — adapting OpenSPP to a country's needs using OpenSPP Studio, a no-code interface for building registry fields, event types, change request workflows, eligibility rules, and business logic
- **Customization** — extending OpenSPP by writing Odoo modules (Python, XML, JavaScript) for requirements that exceed what Studio can express

These are not mutually exclusive. Most deployments use OpenSPP Studio for the majority of their needs and customization only where Studio cannot achieve the desired outcome.

---

## At a glance

| Dimension | Configuration (OpenSPP Studio) | Customization |
|---|---|---|
| **What it is** | Building registry fields, event types, eligibility rules, change workflows, and business logic through OpenSPP Studio | Writing new Odoo modules or modifying existing code |
| **Who does it** | Implementers, M&E officers, program managers, country coordinators | Python/Odoo developers |
| **Technical skill required** | No programming — comparable to building forms in KoBoToolbox or ODK | Advanced — Python, Odoo ORM, XML views, JavaScript |
| **Typical timeframe** | Hours to days | Days to weeks (or longer for complex features) |
| **Cost** | Low — primarily staff time for setup and testing | Higher — requires developer resources, code review, and QA |
| **Maintenance burden** | Low — configurations are stored as data and persist across upgrades with minimal effort | Higher — custom code must be tested and potentially updated with each OpenSPP or Odoo upgrade |
| **Risk of breaking changes** | Low — Studio configurations are part of the supported interface | Moderate to high — custom code may depend on internal APIs that change between versions |
| **Reversibility** | Easy — deactivate a configuration or revert to a previous version | Harder — removing custom modules may require data migration |

---

## Configuration in detail

Configuration in OpenSPP is done through **OpenSPP Studio**, a no-code interface designed for implementers who are familiar with form builders like KoBoToolbox or ODK but do not have programming knowledge. Studio handles approximately 80% of common adaptation needs through visual tools.

### What can be configured

| Area | What OpenSPP Studio provides |
|---|---|
| **Registry fields** | Add custom fields to individual and group records (disability type, national IDs, vulnerability scores) using the Registry Field Builder |
| **Event types** | Design data collection forms for assessments, surveys, and field visits using the Event Type Designer |
| **Change request workflows** | Build approval workflows for updating registrant information (phone number changes, address updates, ID document updates) using the Change Request Builder |
| **Eligibility rules** | Define who qualifies for programs using CEL expressions, with pre-built logic packs for common patterns (PMT targeting, child benefits, social pensions, vulnerability assessment) |
| **Business logic** | Build scoring algorithms, benefit calculations, and exclusion criteria using the CEL expression editor with variable discovery and test personas |
| **User roles and permissions** | Assign security groups and Studio permission levels (Viewer, Editor, Manager) to control access |
| **Reports and dashboards** | Built-in pivot tables, graphs, and exportable reports for program monitoring |
| **Localization** | Language, currency, date formats, and translations |

### Configuration lifecycle

All Studio configurations follow a managed lifecycle:

- **Draft** — configuration is being prepared; editors and managers can modify freely
- **Active** — configuration is live and in use; only managers can modify
- **Inactive** — configuration was active but is now disabled; can be reactivated

Changes are logged with user and timestamp, and deactivation shows impact warnings (e.g., "This field is used by 1,247 records").

### Functional implications

- **Faster time to deployment** — a program can be set up and running in days rather than weeks
- **Lower cost** — no developer involvement needed; implementers and program staff can do the work
- **Easier training** — Studio's interface is comparable to form builders that many M&E teams already know
- **Safer upgrades** — configuration is stored as data (database records), not code, so it generally survives version upgrades intact
- **Built-in governance** — approval workflows, versioning, and audit trails are part of Studio

### What requires a developer

Studio cannot:

- Create entirely new registry tabs or pages (view architecture changes)
- Handle complex change requests involving multi-record operations (add member, split household, merge records)
- Add custom CEL functions not in the standard library
- Build external system connectors (OpenSPP modules that connect to national ID platforms, civil registration systems, or mobile money providers through their published APIs)
- Create custom computed fields that require Python
- Optimize performance-critical batch operations for large-scale deployments
- Build custom reports beyond what built-in reporting tools can express

When you hit these limits, customization is the path forward.

---

## Customization in detail

Customization means writing Odoo modules — Python classes, XML view definitions, and optionally JavaScript — that extend or override OpenSPP's behavior.

### What requires customization

| Area | Examples |
|---|---|
| **New data models** | Adding a grievance redress module with its own models and workflows |
| **Complex business logic** | Logic that cannot be expressed in CEL, such as algorithms requiring external data lookups or multi-step computations across systems |
| **External system connectors** | Building OpenSPP modules that connect to external systems through their published APIs — for example, national ID platforms (MOSIP), civil registration (CRVS), or mobile money providers. The external integration uses standard APIs, but the OpenSPP side requires custom module development to handle data exchange and processing. |
| **Complex change requests** | Multi-record operations such as adding household members, splitting households, or merging records |
| **UI modifications** | New registry tabs, specialized form layouts, or new widget types |
| **Data migration** | Scripts to import beneficiary data from legacy systems |
| **Custom reports** | Reports with logic that exceeds what built-in reporting can express |
| **Performance optimization** | Batch processing, queue jobs, and tuning for large-scale deployments |

### Functional implications

- **Longer timelines** — custom modules require design, development, testing, and deployment cycles
- **Higher cost** — developers must be engaged, whether in-house or contracted
- **Ongoing maintenance** — every custom module is code that must be kept compatible with future OpenSPP and Odoo releases
- **Testing requirements** — custom code needs unit tests, integration tests, and user acceptance testing before deployment
- **Upgrade risk** — Odoo's internal APIs can change between major versions; custom modules may need adaptation

### Technical implications

- **Module structure** — custom code follows Odoo's module conventions (`__manifest__.py`, `models/`, `views/`, `security/`, `data/`)
- **Model inheritance** — use `_inherit` to extend existing models rather than modifying them directly, preserving upgradeability
- **View inheritance** — use `xpath` expressions to modify existing views instead of replacing them wholesale
- **API stability** — prefer Odoo's public ORM methods over internal helpers; internal methods may change without notice
- **Data migrations** — include migration scripts (`migrations/` directory) for schema changes so existing deployments can upgrade safely

---

## Decision framework

Use this flowchart to decide between configuration and customization:

1. **Can it be done in OpenSPP Studio?** (registry fields, event types, change requests, CEL expressions, logic packs) → Configure it in Studio.
2. **Is there an existing OCA or community module that provides the feature?** → Evaluate and install it (this is installation, not customization).
3. **Does it require new data models, logic beyond CEL, external system connectors, or custom UI?** → Customize it, but scope the module narrowly and follow Odoo's inheritance patterns.

### Cost-benefit considerations

| Factor | Favor configuration | Favor customization |
|---|---|---|
| Budget | Limited budget, no developer resources | Development budget available |
| Timeline | Need it running this week | Can plan a development sprint |
| Team skills | Implementers and program staff familiar with form builders | Access to Odoo/Python developers |
| Longevity | Feature needed for one program cycle | Core capability needed long-term |
| Upgrade path | Must stay on supported upgrade path | Willing to maintain custom code |
| Uniqueness | Standard social protection workflow expressible in CEL | Country-specific regulation requiring custom logic or external integration |

---

## Available OpenSPP documentation

OpenSPP provides two guides that correspond to the approaches described here:

- **{doc}`Configuration guide <../../config_guide/index>`** — covers what can be achieved through OpenSPP Studio: registry field building, event type design, change request workflows, CEL expressions, eligibility rules, and system settings. Aimed at **implementers**, **M&E officers**, and **program managers**.
- **{doc}`Developer guide <../../developer_guide/index>`** — covers writing custom modules: model development, view inheritance, API integration, testing, and deployment. Aimed at **developers**.

When a task can be accomplished through OpenSPP Studio, refer to the configuration guide. When it requires code, refer to the developer guide.

---

## Additional resources

- [Odoo developer documentation](https://www.odoo.com/documentation/17.0/developer.html)
- [Odoo functional documentation](https://www.odoo.com/documentation/17.0/)
- [Odoo module development tutorial](https://www.odoo.com/documentation/17.0/developer/tutorials/server_framework_101.html)
- [Odoo model inheritance reference](https://www.odoo.com/documentation/17.0/developer/reference/backend/orm.html#inheritance)
- [Odoo view inheritance reference](https://www.odoo.com/documentation/17.0/developer/reference/backend/views.html#inheritance-specs)
- [Odoo Community Association (OCA)](https://odoo-community.org)
- [OCA module repositories on GitHub](https://github.com/OCA)
- [Odoo upgrade documentation](https://www.odoo.com/documentation/17.0/administration/upgrade.html)
- [OpenSPP website](https://openspp.org)
