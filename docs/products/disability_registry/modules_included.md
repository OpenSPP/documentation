---
openspp:
  doc_status: draft
---

# Modules included

The OpenSPP Disability Registry product is built on the following module and its dependencies.

## Core module

- **{doc}`OpenSPP Disability Registry </reference/modules/spp_disability_registry>`** (`spp_disability_registry`) — Disability assessment and registry management implementing WG-SS and CFM standards with assistive device tracking and CEL eligibility functions.

## Dependencies

The disability registry module requires the following OpenSPP modules, which are automatically installed as dependencies:

- **{doc}`OpenSPP Registry </reference/modules/spp_registry>`** (`spp_registry`) — Consolidated registry management for individuals and groups.
- **{doc}`OpenSPP Vocabulary </reference/modules/spp_vocabulary>`** (`spp_vocabulary`) — Standardized code list management for impairment types, causes, severity levels, and device types.
- **{doc}`OpenSPP Approval </reference/modules/spp_approval>`** (`spp_approval`) — Multi-tier approval workflows for assessment review before results become active.
- **{doc}`OpenSPP CEL Domain Query Builder </reference/modules/spp_cel_domain>`** (`spp_cel_domain`) — CEL expression support for disability-based eligibility targeting in programs.

## Expanding the Disability Registry

Additional OpenSPP modules can be installed alongside the Disability Registry to extend functionality — for example, adding program management, GIS-based targeting, or change request workflows. Read more about {doc}`module installation </get_started/modules/index>`.
