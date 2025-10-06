---
myst:
  html_meta:
    "title": "OpenSPP Overview"
    "description": "High-level overview of OpenSPP social protection platform products, features, and concepts for decision makers"
    "keywords": "OpenSPP, overview, social protection, SP-MIS, Social Registry, Farmer Registry"
---

# Overview

OpenSPP is a modular platform for delivering social protection programs. This section explains what it does, how it works, and guides you forward in your understanding of OpenSPP.

## Choose your product configuration

OpenSPP offers three specialized configurations designed for different social protection scenarios:

:::::{grid} 3
:gutter: 2

::::{grid-item-card} [SP-MIS](products/sp_mis.md)
:link: products/sp_mis
:link-type: doc

Social Protection Management Information System for comprehensive program delivery including cash transfers, conditional assistance, and humanitarian interventions.
::::

::::{grid-item-card} [Social Registry](products/social_registry.md)  
:link: products/social_registry
:link-type: doc

Centralized beneficiary database that serves as a single source of truth across multiple programs, reducing duplication and enabling better coordination.
::::

::::{grid-item-card} [Farmer Registry](products/farmer_registry.md)
:link: products/farmer_registry
:link-type: doc

Agricultural-focused platform combining farm data, land management, and social protection for rural development and climate resilience programs.
::::
:::::

## Understand core capabilities

OpenSPP delivers comprehensive social protection through modular features that work together seamlessly:

**Data foundation**
- {doc}`Unified registry <features/unified_registry>` for consolidated beneficiary data
- {doc}`GIS and land management <features/gis_land_management>` for location-based targeting

**Program delivery**  
- {doc}`Program management <features/program_management>` across the complete lifecycle
- {doc}`Eligibility and targeting <features/eligibility_targeting>` with flexible rules
- {doc}`Payment and disbursement <features/payment_disbursement>` through multiple channels

**System infrastructure**
- {doc}`Data integration and APIs <features/data_integration_apis>` for interoperability
- {doc}`Change management <features/change_management>` with audit trails
- {doc}`Grievance redress <features/grievance_redress>` for accountability

{doc}`View all features → <features/index>`

## Learn fundamental concepts

Understanding OpenSPP's design principles and theoretical foundations:

- {doc}`Digital public infrastructure <concepts/digital_public_infrastructure>` - How OpenSPP aligns with DPI principles
- {doc}`Integrated beneficiary registry <concepts/integrated_beneficiary_registry>` - Registry architecture and design  
- {doc}`Data protection <concepts/data_protection>` - Privacy and security framework
- {doc}`Extensibility <concepts/extensibility>` - Platform customization capabilities

{doc}`Explore all concepts → <concepts/index>`

## Plan your implementation

Ready to explore OpenSPP for your organization? Our structured approach helps you validate fit and plan successful deployments:

**{doc}`From proof of concept to pilot <poc_and_pilot>`** - Comprehensive guide covering:
- Proof of concept (4-8 weeks) for initial validation
- Pilot implementation (3-6 months) for real-world testing  
- Resource planning and success criteria
- Prerequisites and decision frameworks

```{toctree}
:maxdepth: 2
:caption: Contents
:hidden:

products/index
features/index
concepts/index
poc_and_pilot
```