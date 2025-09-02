---
review-status: needs-review
review-date: 2025-06-04
reviewer: migration-script
migration-notes: "Added during 2025 documentation reorganization"
myst:
  html_meta:
    "title": "OpenSPP Overview"
    "description": "High-level overview of OpenSPP social protection platform products, features, and concepts for decision makers"
    "keywords": "OpenSPP, overview, social protection, SP-MIS, Social Registry, Farmer Registry"
---

# Overview

OpenSPP is a modular platform for delivering social protection programs. This section explains what it does, how it works, and whether it fits your needs.

## Choose your product configuration

OpenSPP offers three specialized configurations designed for different social protection scenarios:

:::::{grid} 3
:gutter: 2

::::{grid-item-card} [SP-MIS](products/sp_mis.md)
:link: products/sp_mis.md
:link-type: doc

Social Protection Management Information System for comprehensive program delivery including cash transfers, conditional assistance, and humanitarian interventions.
::::

::::{grid-item-card} [Social Registry](products/social_registry.md)  
:link: products/social_registry.md
:link-type: doc

Centralized beneficiary database that serves as a single source of truth across multiple programs, reducing duplication and enabling better coordination.
::::

::::{grid-item-card} [Farmer Registry](products/farmer_registry.md)
:link: products/farmer_registry.md
:link-type: doc

Agricultural-focused platform combining farm data, land management, and social protection for rural development and climate resilience programs.
::::
:::::

[Explore all products →](products/index.md)

## Understand core capabilities

OpenSPP delivers comprehensive social protection through modular features that work together seamlessly:

**Data Foundation**
- [Unified registry](features/unified_registry.md) for consolidated beneficiary data
- [GIS and land management](features/gis_land_management.md) for location-based targeting

**Program Delivery**  
- [Program management](features/program_management.md) across the complete lifecycle
- [Eligibility and targeting](features/eligibility_targeting.md) with flexible rules
- [Payment and disbursement](features/payment_disbursement.md) through multiple channels

**System Infrastructure**
- [Data integration and APIs](features/data_integration_apis.md) for interoperability
- [Change management](features/change_management.md) with audit trails
- [Grievance redress](features/grievance_redress.md) for accountability

[View all features →](features/index.md)

## Learn fundamental concepts

Understanding OpenSPP's design principles and theoretical foundations:

- [Digital public infrastructure](concepts/digital_public_infrastructure.md) - How OpenSPP aligns with DPI principles
- [Integrated beneficiary registry](concepts/integrated_beneficiary_registry.md) - Registry architecture and design  
- [Data protection](concepts/data_protection.md) - Privacy and security framework
- [Extensibility](concepts/extensibility.md) - Platform customization capabilities

[Explore all concepts →](concepts/index.md)

## Plan your implementation

Ready to explore OpenSPP for your organization? Our structured approach helps you validate fit and plan successful deployments:

**[From proof of concept to pilot](poc_and_pilot.md)** - Comprehensive guide covering:
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