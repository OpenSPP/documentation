---
review-status: needs-review
review-date: 2025-06-04
reviewer: migration-script
migration-notes: "Added during 2025 documentation reorganization"
---

# Features

OpenSPP delivers comprehensive social protection capabilities through modular, interoperable components that adapt to diverse program requirements and implementation contexts. Each feature area integrates seamlessly with others, creating a unified platform for managing complex social protection interventions.

## Data Foundation

### [Unified Registry](unified_registry.md)
Central repository for all beneficiary data, supporting both individuals and hierarchical groups. Eliminates data fragmentation by providing a single source of truth that multiple programs can share, reducing duplication and ensuring consistency across interventions.

### [Geospatial (GIS) and Land Management](gis_land_management.md)
Location-based intelligence for precise geographic targeting and land record management. Enables spatial analysis for disaster response, agricultural programs, and service delivery optimization through interactive mapping and area-based calculations.

## Program Delivery

### [Program Management](program_management.md)
Complete lifecycle management from program design through beneficiary graduation. Supports diverse intervention types including emergency cash transfers, social pensions, conditional programs, and mixed benefit distributions with configurable cycles and workflows.

### [Eligibility & Targeting](eligibility_targeting.md)
Flexible rules engine for identifying and enrolling beneficiaries using multiple methodologies. Combines manual selection, geographic targeting, demographic filters, proxy means testing, and custom SQL rules to ensure programs reach their intended populations.

### [Payment & Disbursement](payment_disbursement.md)
Pluggable architecture for multi-channel benefit delivery through banks, mobile money, vouchers, and cash. Integrates with existing financial infrastructure using standards like G2P Connect while maintaining fallback options for areas with limited services.

### [In-Kind Benefits](in_kind_benefits.md)
Comprehensive management of non-cash assistance including food rations, agricultural inputs, and medical supplies. Features integrated inventory tracking, distribution planning, voucher systems, and vendor management for accountable in-kind delivery.

## System Infrastructure

### [Data Integration & APIs](data_integration_apis.md)
RESTful APIs and integration connectors for seamless data exchange with external systems. Enables interoperability with civil registries, national ID systems, mobile data collection tools, and other government databases through standardized interfaces.

### [Change Management](change_management.md)
Formal workflows and audit trails for data modifications ensuring integrity and accountability. Tracks every change with complete before/after snapshots, approval chains, and justification documentation for regulatory compliance and fraud prevention.

## Accountability

### [Grievance Redress Mechanism](grievance_redress.md)
Multi-channel feedback system for managing beneficiary complaints and appeals transparently. Provides accessible pathways for issue resolution while generating insights for program improvement through pattern analysis of grievance data.

```{toctree}
:maxdepth: 2
:caption: Contents
:hidden:

Unified Registry <unified_registry>
Program Management <program_management>
Eligibility & Targeting <eligibility_targeting>
Payment & Disbursement <payment_disbursement>
In-Kind Benefits <in_kind_benefits>
Data Integration & APIs <data_integration_apis>
Change Management <change_management>
GIS & Land Management <gis_land_management>
Grievance Redress <grievance_redress>
```
