---
openspp:
  doc_status: draft
  products: [core]
---

# Configuration guide

**For: implementers** (M&E teams, technical staff comfortable with Kobo/CommCare level configuration)

This guide covers configuring OpenSPP without code — setting up eligibility rules, formulas, workflows, and system behavior through the OpenSPP Studio interface and configuration screens.

## Overview

The Configuration Guide is designed for implementers who need to customize OpenSPP for their specific program requirements. No programming knowledge is required — configuration uses visual tools and simple expression languages.

## Topics covered

- **[Alerts](alerts/index.md)** — Rule-based monitoring and notifications
- **[Approval workflows](approval_workflows/index.md)** — Multi-tier approval routing for change requests and programs
- **[Area management](area_management/index.md)** — Administrative hierarchy and geographic boundaries
- **[Audit configuration](audit/index.md)** — Tracking and logging system changes
- **[Banking](banking/index.md)** — Bank codes and payment account configuration
- **[Case management](case_management/index.md)** — Case types, stages, and team assignments
- **[CEL expressions](cel/index.md)** — Common Expression Language for rules and formulas
- **[Change request types](change_request_types/index.md)** — Configuring change request workflows (NEW V2)
- **[Consent configuration](consent/index.md)** — Managing data sharing consent (NEW V2)
- **[Custom fields](custom_fields/index.md)** — Registrant field groups
- **[Document management](document_management/index.md)** — Document directories, categories, and retention
- **[DRIMS configuration](drims/index.md)** — Disaster-responsive and shock-responsive settings
- **[Eligibility rules](eligibility/index.md)** — Configuring who qualifies for programs
- **[Entitlement formulas](entitlement_formulas/index.md)** — Calculating benefit amounts
- **[Event data](event_data/index.md)** — Capturing external data from surveys and forms (V2 enhanced)
- **[Farmer registry](farmer_registry/index.md)** — Farm entity configuration
- **[GIS configuration](gis/index.md)** — Spatial data layers, color schemes, and map reports
- **[Graduation](graduation/index.md)** — Exit pathways and criteria for program beneficiaries
- **[Grievance redress](grievance_redress/index.md)** — Ticket categories, service-level rules, teams, and tags
- **[Hazard management](hazard_management/index.md)** — Hazard categories, incidents, and program linking
- **[Import matching](import_matching/index.md)** — Deduplication during import
- **[OpenSPP Studio](studio/index.md)** — No-code configuration tool (NEW V2)
- **[Role configuration](role_configuration/index.md)** — Configuring users, roles, and role-based access (global and local roles)
- **[Scoring & assessment](scoring/index.md)** — Scoring models and dimensions for targeting
- **[Service points](service_points/index.md)** — Service delivery location configuration
- **[Session tracking](session_tracking/index.md)** — Session types and attendance tracking
- **[Simulation](simulation/index.md)** — Scenario modeling for program planning
- **[Storage backend](storage_backend/index.md)** — File storage backends (local disk, cloud object stores)
- **[Variables and indicators](variables/index.md)** — Unified variable system (NEW V2)
- **[Vocabulary system](vocabulary/index.md)** — Standardized codes and terminologies (NEW V2)

```{toctree}
:maxdepth: 2
:hidden:

alerts/index
approval_workflows/index
area_management/index
audit/index
banking/index
case_management/index
cel/index
change_request_types/index
consent/index
custom_fields/index
document_management/index
drims/index
eligibility/index
entitlement_formulas/index
event_data/index
farmer_registry/index
gis/index
graduation/index
grievance_redress/index
hazard_management/index
import_matching/index
studio/index
role_configuration/index
scoring/index
service_points/index
session_tracking/index
simulation/index
storage_backend/index
variables/index
vocabulary/index
```
