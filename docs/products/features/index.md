---
myst:
  html_meta:
    "title": "OpenSPP Features"
    "description": "Comprehensive features of OpenSPP social protection platform including registry, program management, and payment systems"
    "keywords": "OpenSPP, features, social protection, registry, eligibility, payments, GIS"
---

# Features in OpenSPP

OpenSPP's features work together to deliver end-to-end social protection programs. Each component can be configured independently while maintaining seamless integration with others.

## Data foundation

**{doc}`Unified Registry <unified_registry>`**: Central repository for all beneficiary data, supporting both individuals and hierarchical groups.
Eliminates data fragmentation by providing a single source of truth that multiple programs can share, reducing duplication and ensuring consistency across interventions.

**{doc}`Geospatial (GIS) and land management <gis_land_management>`**: Location-based intelligence for precise geographic targeting and land record management.
Enables spatial analysis for disaster response, agricultural programs, and service delivery optimization through interactive mapping and area-based calculations.

## Program delivery

**{doc}`Program management <program_management>`**: Complete lifecycle management from program design through benefit calculation and disbursement.
Supports diverse intervention types including emergency cash transfers, social pensions, and conditional programs with configurable cycles and workflows.

**{doc}`Eligibility & targeting <eligibility_targeting>`**: Flexible rules engine for identifying and enrolling beneficiaries using multiple methodologies.
Combines manual selection, geographic targeting, demographic filters, proxy means testing, and CEL-based custom rules to ensure programs reach their intended populations.

**{doc}`Payment & disbursement <payment_disbursement>`**: Payment processing system for bank and cash-based benefit disbursement.
Manages the payment lifecycle with configurable batching, asynchronous processing, and per-program currency configuration.

**{doc}`In-kind benefits <in_kind_benefits>`**: Comprehensive management of non-cash assistance including food rations, agricultural inputs, and medical supplies.
Features integrated inventory tracking and vendor/supplier management for accountable in-kind delivery.

## System infrastructure

**{doc}`Data integration & APIs <data_integration_apis>`**: RESTful APIs and integration connectors for seamless data exchange with external systems.
Enables interoperability with civil registries, national ID systems, and other government databases through standardized interfaces.

**{doc}`Change management <change_management>`**: Formal workflows and audit trails for data modifications ensuring integrity and accountability.
Tracks every change with complete before/after snapshots, approval chains, and justification documentation for regulatory compliance and fraud prevention.

## Accountability

**{doc}`Grievance redress mechanism <grievance_redress>`**: Feedback system for managing beneficiary complaints and appeals transparently.
Provides accessible pathways for issue resolution and links grievances to specific programs, payments, and eligibility decisions for context-aware resolution.

## Configuration and extensibility

**{doc}`Standardized vocabularies <vocabularies>`**: Configurable, hierarchical classification codes for genders, relationships, disability categories, and more.
Ships with 19 pre-built vocabularies while remaining fully extensible, with cross-standard mapping and multi-language labels.

**{doc}`Common Expression Language (CEL) <cel_expressions>`**: A lightweight, secure rules engine for eligibility criteria, entitlement formulas, and compliance checks.
Compiles expressions to SQL for performance at scale, with built-in safeguards against unsafe or runaway expressions.

**{doc}`OpenSPP Studio <openspp_studio>`**: No-code interface for adding custom fields, eligibility logic, change request types, and data collection forms.
Lets program staff configure the platform themselves through guided wizards, without developer involvement for most changes.

```{toctree}
:maxdepth: 2
:caption: Contents
:hidden:

Unified registry <unified_registry>
GIS & land management <gis_land_management>
Program management <program_management>
Eligibility & targeting <eligibility_targeting>
Payment & disbursement <payment_disbursement>
In-Kind benefits <in_kind_benefits>
Data integration & APIs <data_integration_apis>
Change management <change_management>
Grievance redress <grievance_redress>
Standardized vocabularies <vocabularies>
Common Expression Language (CEL) <cel_expressions>
OpenSPP Studio <openspp_studio>
```
