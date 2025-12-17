# OpenSPP V2 (Odoo 19) Documentation Backlog

This file tracks the work needed to update `documentation/` for **OpenSPP V2**.

## Scope + decisions (locked)

- **Odoo version:** V2 docs target **Odoo 19 only**
- **Deployment path:** **Docker** (primary install/deploy docs)
- **Public API:** **API V2 only** (no v1, no “deprecated”)
- **Studio:** Document as **implemented / near-ready** (not “future concept”)
- **Auto-generated module docs:** ignore `documentation/docs/modules/` (not part of this rewrite)
- **Overview page:** keep a single **Overview** page (no separate “v2_overview.md”)

## How to use this backlog

- Use checkboxes as the source of truth:
  - `[ ]` = not started
  - `[~]` = in progress
  - `[x]` = done
  - `[!]` = blocked / needs decision
- Prefer creating or updating pages under `documentation/docs/`.
- When you finish an item, add a short note and (optionally) PR/commit link.

---

## P0 — Must-fix before publishing V2 docs

### Accuracy + broken placeholders

- [x] Update `documentation/docs/index.md` (remove stale “Q2 2024 Disability Registry” claim; align messaging)
- [x] Update `documentation/docs/getting_started/index.md` (Odoo 19 baseline; remove/replace absolute `https://docs.openspp.org/...` internal links)
- [x] Update `documentation/docs/getting_started/installation_guide.md` (Docker-based dev + production guidance; `openspp-docker` as recommended path)
- [ ] Replace TODO/empty pages with real content or remove them from navigation:
  - [x] `documentation/docs/technical_reference/apis.md` (was empty; now documents API v2 at a high level)
  - [x] `documentation/docs/technical_reference/g2p-connect.md` (removed)
  - [x] `documentation/docs/technical_reference/openg2p.md` (removed)
  - [ ] `documentation/docs/tutorial/programs/export_beneficiaries.md` (empty)
  - [ ] `documentation/docs/getting_started/creating_a_program.md` (empty)
- [ ] Remove TODO stubs that currently publish:
  - [x] `documentation/docs/tutorial/event_data.md`
  - [ ] `documentation/docs/tutorial/vouchers.md` (Implementation section)
  - [x] `documentation/docs/tutorial/proxy_means_test.md` (rewritten using `spp_scoring`)
  - [x] `documentation/docs/tutorial/access_management.md` (rewritten for role/privilege-based access)
  - [ ] `documentation/docs/community_and_support/i18n_l10n.md` (“General procedure” TODO + references “OpenSPP 6”)

### Navigation / toctree correctness

- [~] Fix `documentation/docs/technical_reference/index.md` toctree references (added missing stubs: `oidc`, `dci`, `module`; needs full content pass)
- [ ] Ensure every published section index includes all intended pages (or explicitly removes them):
  - [~] `documentation/docs/tutorial/index.md` (deduplicated “Programs and Cycles”; still needs a full coverage pass, including `access_management.md`)
  - [ ] `documentation/docs/howto/index.md` (remove duplicate `developer_guides/troubleshooting`)

### Legacy references that conflict with V2

- [x] Update `documentation/docs/technical_reference/audit_logs.md` (document `spp_audit` and remove Odoo 15 “Smile Audit” guidance)
- [ ] Update `documentation/docs/technical_reference/external_api.rst` examples/claims to reflect Odoo 19, and position XML-RPC as “internal/advanced” vs the official API v2 (REST)

---

## P1 — Core V2 content alignment (highest user value)

### Information architecture (what users install / where they start)

- [ ] Add a single “Overview” page and link it from `documentation/docs/index.md`
  - [!] Decide location (recommended: `documentation/docs/getting_started/overview.md` or `documentation/docs/explanation/overview.md`)
- [ ] Add “Module selection / what to install” page based on V2 consolidation targets
  - Source: `openspp-modules-v2/docs/architecture/V2_MODULE_ARCHITECTURE.md`
  - Output: `documentation/docs/getting_started/module_selection.md` (recommended)

### Access rights & roles (Odoo 19 privileges)

Sources:
- `openspp-modules-v2/docs/specs/access-rights/*`
- `openspp-modules-v2/docs/architecture/decisions/ADR-004-access-rights-management.md`

Deliverables:
- [x] Rewrite `documentation/docs/tutorial/access_management.md` (user/admin actions aligned to Odoo 19)
- [ ] Rewrite `documentation/docs/howto/user_guides/administrating_role_based_access.md` (if kept as separate from tutorial)
- [x] Add `documentation/docs/technical_reference/access_rights.md` (concepts, roles, privileges, local roles/areas, troubleshooting)
- [ ] Sweep all prerequisites in tutorials/howtos for old role names and update them consistently

### API V2 (official API)

Sources:
- `openspp-modules-v2/docs/specs/api-v2/SPEC.md`
- `openspp-modules-v2/docs/architecture/decisions/ADR-010-api-v2-architecture.md`

Deliverables:
- [x] Create `documentation/docs/technical_reference/api_v2/index.md` (entrypoint)
- [x] Create `documentation/docs/technical_reference/api_v2/authentication.md` (OAuth2 client credentials, JWT)
- [x] Create `documentation/docs/technical_reference/api_v2/clients_and_scopes.md` (client configuration and scopes)
- [x] Create `documentation/docs/technical_reference/api_v2/resources.md` (resources + endpoint summary)
- [x] Create `documentation/docs/technical_reference/api_v2/search.md` (simple + advanced search, filter discovery)
- [x] Create `documentation/docs/technical_reference/api_v2/batch.md` (batch/transaction bundles)
- [x] Create `documentation/docs/technical_reference/api_v2/extensions.md` (capability statement + `_extensions`)
- [x] Create `documentation/docs/technical_reference/api_v2/errors.md` (error model and common responses)
- [x] Create `documentation/docs/technical_reference/api_v2/consent_model.md` (consent-aware behavior)
- [x] Update `documentation/docs/howto/developer_guides/rest_api.md` to be API v2-oriented (extensions guide)

### Change Requests V2

Sources:
- `openspp-modules-v2/docs/architecture/V2_MODULE_ARCHITECTURE.md` (CR consolidation)
- `openspp-modules-v2/docs/architecture/decisions/ADR-002-change-request-event-integration.md`
- `openspp-modules-v2/docs/specs/CHANGE_REQUEST_V2_IMPLEMENTATION_PLAN.md` (if used)

Deliverables:
- [ ] Rewrite `documentation/docs/tutorial/change_requests.md` for `spp_change_request_v2` (configuration-driven CR types, approvals, lifecycle)
- [ ] Create `documentation/docs/technical_reference/change_requests_v2.md` (CR types, apply strategies, audit/event trail)

### Programs / cycles / entitlements (ensure names + flows match V2)

- [ ] Review + update `documentation/docs/tutorial/programs_and_cycles.md`
- [ ] Review + update program user guides under `documentation/docs/tutorial/user_guides/`:
  - `create_social_protection_program.md`
  - `create_program_cycle_prepare_entitlements.md`
  - `configure_cash_entitlements.md`
  - `allocate_funds.md`
  - `enroll_beneficiaries.md`
- [ ] Update `documentation/docs/technical_reference/programs/*` references away from `g2p_programs` (Odoo module docs currently look legacy)

### Event data / CEL / indicators

- [x] Implement `documentation/docs/tutorial/event_data.md`
- [x] Remove legacy `documentation/docs/tutorial/indicators.md` and replace with `documentation/docs/tutorial/variables_and_expressions.md`
- [x] Add CEL technical reference section under `documentation/docs/technical_reference/cel/` and link it from Technical Reference
- [x] Document Programs eligibility/compliance CEL: `documentation/docs/tutorial/programs/eligibility_and_compliance.md`
- [x] Document entitlement amount formulas (runtime CEL): `documentation/docs/tutorial/programs/entitlement_amount_formulas.md`

### Workflow rules (spp_workflow)

- [ ] Document workflow concepts and where rules are used (triggers, states, conditions, assignments)
- [ ] Document CEL usage in workflow rules (runtime context, available variables, examples)
- [ ] Add screenshot placeholders for workflow builder screens (Studio/Workflow UI)

### Vocabulary / code URIs (interoperability)

Sources:
- `openspp-modules-v2/docs/architecture/decisions/ADR-009-terminology-system.md`
- `openspp-modules-v2/docs/architecture/decisions/ADR-016-vocabulary-profiles-and-code-uris.md`

Deliverables:
- [ ] Create `documentation/docs/explanation/vocabulary.md` (why vocabularies exist, code URIs, mappings)
- [ ] Create `documentation/docs/howto/admin_guides/vocabulary_management.md` (manage vocabularies, profiles)
- [ ] Add API v2 section referencing vocabulary endpoints (if relevant)

### Data governance / security (make it concrete to V2)

Sources:
- `openspp-modules-v2/docs/architecture/decisions/ADR-011-data-classification-system.md`
- `openspp-modules-v2/docs/architecture/decisions/ADR-012-pii-encryption-strategy.md`

Deliverables:
- [ ] Refactor `documentation/docs/technical_reference/security.md` into actionable subpages:
  - [ ] `documentation/docs/technical_reference/security/data_classification.md`
  - [ ] `documentation/docs/technical_reference/security/pii_encryption.md`
  - [ ] `documentation/docs/technical_reference/security/key_management.md`
  - [ ] `documentation/docs/technical_reference/security/audit.md` (OpenSPP audit approach)
  - [ ] `documentation/docs/technical_reference/security/source_tracking.md`
- [ ] Update `documentation/docs/explanation/data_protection.md` to link to these controls

### Verifiable Credentials / OIDC4VCI

Sources:
- `openspp-modules-v2/docs/specs/oidc4vci-compliance.md`
- `openspp-modules-v2/docs/architecture/decisions/ADR-006-verifiable-credentials-system.md`

Deliverables:
- [ ] Create `documentation/docs/technical_reference/verifiable_credentials.md`
- [ ] Update `documentation/docs/howto/developer_guides/oidc.md` to match V2 implementation

### Studio (document as implemented)

Sources:
- `openspp-modules-v2/docs/specs/OPENSPP_STUDIO_SPECIFICATION.md`

Deliverables:
- [ ] Create `documentation/docs/tutorial/studio/index.md` (what Studio is, roles, lifecycle)
- [ ] Create “how-to” pages (minimal, practical):
  - [ ] `documentation/docs/tutorial/studio/registry_fields.md`
  - [ ] `documentation/docs/tutorial/studio/event_types.md`
  - [ ] `documentation/docs/tutorial/studio/change_requests.md`
  - [ ] `documentation/docs/tutorial/studio/eligibility_rules.md`

---

## P2 — Cleanup, consistency, and “docs feel”

### Remove legacy naming + broken references

- [ ] Sweep `documentation/docs/` (excluding `modules/`) for `g2p_*`, `g2p.` and update to V2 (`spp_*`, `spp.`) where applicable
- [ ] Sweep for Odoo 15/17 references and update to Odoo 19
- [ ] Replace internal absolute links (`https://docs.openspp.org/...`) with relative doc links

### Duplications and structure

- [ ] Decide canonical location for “User guides” (currently duplicated under `tutorial/user_guides/` and `howto/user_guides/`)
- [ ] Ensure all section landing pages reflect the final structure:
  - `documentation/docs/tutorial/index.md`
  - `documentation/docs/howto/index.md`
  - `documentation/docs/technical_reference/index.md`
  - `documentation/docs/explanation/index.md`

### Operational guidance improvements (Docker + production readiness)

- [ ] Expand `documentation/docs/technical_reference/backup.md` for V2 deployment realities
- [ ] Expand `documentation/docs/technical_reference/monitoring.md` (logs/metrics, what to watch in production)
- [ ] Expand `documentation/docs/technical_reference/performance_optimization.md` (high-scale patterns mentioned in V2 architecture)
- [ ] Validate `documentation/docs/technical_reference/architecture.md` against V2 narrative (remove “Open G2P core functions” framing if no longer accurate)

---

## Notes / references (V2 sources used)

- Architecture + consolidation: `openspp-modules-v2/docs/architecture/V2_ARCHITECTURE.md`, `openspp-modules-v2/docs/architecture/V2_MODULE_ARCHITECTURE.md`
- ADRs: `openspp-modules-v2/docs/architecture/decisions/ADR-001*` through `ADR-018*`
- Specs: `openspp-modules-v2/docs/specs/*` (API v2, access-rights, Studio, security)
