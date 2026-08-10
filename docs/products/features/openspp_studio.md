---
myst:
  html_meta:
    "title": "OpenSPP Studio: No-Code Configuration"
    "description": "OpenSPP Studio no-code interface for custom fields, eligibility logic, change request types, and data collection forms"
    "keywords": "OpenSPP, Studio, no-code, low-code, CEL, custom fields, configuration, social protection"
---

# OpenSPP Studio: no-code configuration

OpenSPP Studio provides a no-code interface for configuring platform behavior without writing code: adding custom fields to registrant profiles, defining eligibility and entitlement logic using the Common Expression Language (CEL), building new change request types, and designing custom data-collection forms.

## Configuration without code

Social protection programs constantly need to adapt: a new field to capture a specific vulnerability, a revised eligibility formula, an additional data point for a follow-up survey. On many platforms, each of these changes requires developer involvement — writing code, deploying it, and testing it — which slows down program design and creates dependency on technical teams that may not be available where they're needed most.

OpenSPP Studio addresses this by exposing platform configuration through guided, wizard-driven interfaces backed by real Odoo models rather than one-off scripts. Program staff can add fields, write eligibility rules, and design new workflows themselves, while built-in governance — draft and published states, approval routing, versioning, and persona-based testing — ensures changes are reviewed and validated before they affect real beneficiaries. For the vast majority of configuration needs — new fields, new eligibility rules, new change request types, new data collection forms — no code is required. Rules are written in the Common Expression Language (CEL), a simple, readable syntax that non-technical staff can learn quickly, backed by variable discovery, built-in testing, and validation. For the rare cases that call for deeply custom logic, OpenSPP's underlying modules remain fully extensible by developers, so Studio's no-code layer never becomes a ceiling.

## Studio capabilities

* **No-code custom fields**: Add new fields to registrant forms through a guided wizard — each field is a genuine Odoo model field with its own persisted view, not a workaround
* **Logic and expression engine**: Define eligibility criteria, entitlement formulas, and other business rules using the Common Expression Language (CEL), with variable discovery from registry fields, vocabularies, and scoring models
* **Governance, versioning, and testing**: Require approval before publishing new logic, maintain full version history, and validate rules against reusable test personas before they go live
* **Pre-built logic packs**: Install ready-made rule libraries for common program types such as poverty targeting, child benefits, social pensions, and disaster response
* **No-code change request types**: Define new change request document types — with their own fields, form, and approval routing — for straightforward field updates
* **No-code event and survey types**: Design custom data-collection forms for field visits, health screenings, and other structured data capture, with field-level validation and conditional visibility
* **Program-scoped configuration**: Restrict Studio-built fields, logic, change request types, and event types to specific programs
* **API exposure**: Expose Studio-defined custom fields and variables through OpenSPP's REST API for external system integration

## Technical implementation

OpenSPP Studio is delivered through the following modules:

* **[spp_studio](/reference/modules/spp_studio.md)**: Core no-code configuration framework — custom field builder, logic and expression governance, versioning, testing, and pre-built packs
* **[spp_studio_change_requests](/reference/modules/spp_studio_change_requests.md)**: No-code builder for new change request types
* **[spp_studio_events](/reference/modules/spp_studio_events.md)**: No-code builder for custom data-collection and survey types
* **`spp_studio_programs`**: Scopes Studio-built customizations to specific programs
* **[spp_studio_api_v2](/reference/modules/spp_studio_api_v2.md)**: Exposes Studio-defined custom fields and variables through OpenSPP's REST API
* **[spp_cel_domain](/reference/modules/spp_cel_domain.md)**: Common Expression Language engine underlying Studio's logic and variable system
