---
openspp:
  doc_status: draft
myst:
  html_meta:
    "title": "Choosing Your Configuration - OpenSPP"
    "description": "Decision framework for selecting the right OpenSPP modules and configuration for your social protection program"
    "keywords": "OpenSPP, module selection, configuration, custom combinations, social protection"
---

# Choosing your configuration

**For:** Implementers and technical teams designing an OpenSPP deployment

This guide helps you decide between using a standard OpenSPP product and building a custom module combination — and walks you through the selection process if you choose the custom route.

## Step 1: Review OpenSPP standard products

Before considering a custom combination, check whether one of the five standard products covers your use case:

| Product | Best for |
|---------|----------|
| {doc}`SP-MIS </products/spmis/index>` | Cash transfers, social assistance, full program lifecycle management |
| {doc}`Social Registry </products/social_registry/index>` | Centralized beneficiary database serving multiple programs |
| {doc}`Farmer Registry </products/farmer_registry/index>` | Agricultural household registration and targeted input distribution |
| {doc}`DRIMS </products/drims/index>` | Disaster response inventory, donations, and dispatch management |
| {doc}`Disability Registry </products/disability_registry/index>` | Standardized disability assessment and targeting |

Standard products offer:
- Proven configurations that have been tested together
- Comprehensive documentation and demo data
- Faster setup — one starter module installs everything
- Community support and known upgrade paths

**Use a standard product when** your program matches its core scope. You can still extend a standard product with additional modules — for example, adding GIS, case management, or scoring to SP-MIS.

## Step 2: Decide if you need a custom combination

A custom combination is worth considering when:

- Your program spans multiple sectors and no single product covers all requirements
- You need only a subset of a product's features and want a leaner installation
- You are combining capabilities from two different products (e.g., Farmer Registry + DRIMS)
- You have a specialized workflow that requires modules not bundled in any standard product

:::{important}
The SP-MIS (`spp_starter_sp_mis`), Social Registry (`spp_starter_social_registry`), and Farmer Registry (`spp_starter_farmer_registry`) starter modules are **mutually exclusive** — only one can be installed in a single Odoo database. DRIMS and the Disability Registry can be installed alongside any of them.
:::

## Step 3: Use case examples

These combinations are validated starting points for common cross-sector programs.

### Inclusive social protection

**Use case:** Social Registry + Disability Registry + GIS

Combine the Social Registry as the beneficiary data foundation with the Disability Registry for WG-SS/CFM assessments and GIS for geographic targeting. Use built-in CEL functions from the Disability Registry to write eligibility rules that automatically flag households with persons with disabilities.

| Module | Purpose |
|--------|---------|
| `spp_starter_social_registry` | Beneficiary registration and data management |
| `spp_disability_registry` | Standardized disability assessment (WG-SS/CFM) |
| `spp_gis` | Geographic visualization and spatial targeting |
| `spp_area` | Administrative area hierarchy for geographic filtering |
| `spp_programs` | Program enrollment and entitlement management |

---

### Agricultural disaster response

**Use case:** Farmer Registry + DRIMS

Link agricultural household data with disaster response inventory management. When a hazard incident is declared, match affected farm households against DRIMS warehouses and dispatch agricultural inputs or relief items to affected areas.

| Module | Purpose |
|--------|---------|
| `spp_starter_farmer_registry` | Farmer and farm household registration |
| `spp_drims` | Disaster response inventory, donations, and dispatches |
| `spp_hazard` | Hazard incident recording and area linkage |
| `spp_gis` | Geographic overlap between farm areas and incident zones |
| `spp_area` | Administrative area hierarchy shared across both systems |

---

### Social work case management

**Use case:** Social Registry + Case Management + Grievance Redress

Build a social work program where case workers manage individual cases, record home visits and intervention plans, track beneficiary progress, and handle complaints — all linked to a unified beneficiary registry.

| Module | Purpose |
|--------|---------|
| `spp_starter_social_registry` | Centralized beneficiary database |
| `spp_case_base` | Case creation, stage workflows, intervention plans, visit logs |
| `spp_case_registry` | Links cases to registrant records |
| `spp_case_programs` | Connects cases to program enrollment |
| `spp_grm` | Grievance and complaint management |
| `spp_grm_registry` | Links grievances to registered beneficiaries |

---

### Integrated SP-MIS with disability targeting

**Use case:** SP-MIS + Disability Registry

Extend the standard SP-MIS with disability-aware targeting. Use the Disability Registry's CEL functions (`has_disability()`, `household_has_pwd()`) as eligibility criteria to automatically identify and enroll persons with disabilities or households with disabled members.

| Module | Purpose |
|--------|---------|
| `spp_starter_sp_mis` | Full SP-MIS foundation |
| `spp_disability_registry` | Assessment, device tracking, and CEL eligibility functions |

---

### Scoring and simulation for targeting

**Use case:** Social Registry or SP-MIS + Scoring + Simulation

Apply proxy means testing (PMT) or vulnerability scoring to rank beneficiaries, then use the simulation engine to model different targeting thresholds before committing to enrollment.

| Module | Purpose |
|--------|---------|
| `spp_starter_social_registry` or `spp_starter_sp_mis` | Registry foundation |
| `spp_scoring` | PMT and vulnerability scoring with configurable formulas |
| `spp_scoring_programs` | Applies scoring thresholds in program eligibility |
| `spp_simulation` | Simulate enrollment outcomes before committing |

## Step 4: Assess module compatibility

Most OpenSPP modules are additive — they extend core models without conflicting. Use this reference when assembling your module list.

**Always compatible with any base:**

| Module | Notes |
|--------|-------|
| `spp_disability_registry` | Extends `res.partner` non-destructively |
| `spp_drims` | Operates independently on its own models |
| `spp_gis` / `spp_area` | Geographic layer shared by all modules |
| `spp_audit` | Transparent audit logging, no functional conflicts; program/cycle audit rules add automatically via `spp_audit_programs` when `spp_programs` is installed |
| `spp_grm` | Standalone grievance system, linkable to registry |
| `spp_case_base` | Case management layer independent of program modules |
| `spp_scoring` | Scoring engine usable alongside any registry base |
| `spp_approval` | Approval workflow mixin used across multiple modules |
| `spp_vocabulary` | Shared code list system, no conflicts |
| `spp_encryption` | Field-level encryption applicable to any base |
| `spp_studio` | No-code customization layer, no functional conflicts; program scoping adds automatically via `spp_studio_programs` when `spp_programs` is installed |
| `spp_api_v2` | REST API layer compatible with all configurations; Program/ProgramMembership endpoints add automatically via `spp_api_v2_programs` when `spp_programs` is installed |

**Mutually exclusive — install only one:**
- `spp_starter_sp_mis`
- `spp_starter_social_registry`
- `spp_starter_farmer_registry`

**Require a specific base:**

| Module | Requires |
|--------|----------|
| `spp_case_programs` | `spp_programs` (included in SP-MIS and Social Registry) |
| `spp_grm_programs` | `spp_programs` |
| `spp_farmer_registry_cr` | `spp_starter_farmer_registry` |
| `spp_hazard_programs` | `spp_programs` and `spp_hazard` |
| `spp_drims_sl` | `spp_drims` (country-specific configuration) |

**Auto-installing program companions:**

Several base modules ship a thin companion that carries their program-specific surface so the base can be installed without the Programs stack. You never add these to your module list manually — each installs (and uninstalls) automatically with its base + `spp_programs` pairing.

| Companion | Auto-installs when present |
|-----------|---------------------------|
| `spp_api_v2_programs` | `spp_api_v2` + `spp_programs` |
| `spp_audit_programs` | `spp_audit` + `spp_programs` |
| `spp_source_tracking_programs` | `spp_source_tracking` + `spp_programs` |
| `spp_studio_programs` | `spp_studio` + `spp_programs` |
| `spp_studio_change_requests_programs` | `spp_studio_change_requests` + `spp_studio_programs` |
| `spp_studio_events_programs` | `spp_studio_events` + `spp_studio_programs` |

## Step 5: Assemble your module list

Follow this order when selecting modules for a custom build:

1. **Start with a registry base** — Choose one starter module (`spp_starter_sp_mis`, `spp_starter_social_registry`, or `spp_starter_farmer_registry`) or use `spp_registry` directly for a minimal installation.

2. **Add program delivery** — Install `spp_programs` if you need enrollment, cycles, entitlements, or payment management. This is included in SP-MIS and Social Registry starters.

3. **Layer specialized modules** — Add modules for your specific needs: disability assessments, case management, disaster response, GIS, scoring, grievances, and so on.

4. **Add data quality tools** — Consider `spp_change_request_v2` for structured data update workflows, `spp_audit` for compliance logging, and `spp_deduplication` for duplicate management.

5. **Configure integrations** — Add `spp_api_v2` for external system connectivity, `spp_dci` for government interoperability, or `spp_oauth` for SSO.

## Reference

- {doc}`Full module reference </reference/modules/index>` — All 60+ modules with dependency information
- {doc}`Technical architecture </developer_guide/architecture/index>` — Module dependency patterns for developers
- {doc}`Custom Module Combinations </products/custom_solutions>` — Overview of the custom combinations approach
