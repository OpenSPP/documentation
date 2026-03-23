---
openspp:
  doc_status: draft
  products: [core]
---

# Modules Reference

This section provides comprehensive documentation for all OpenSPP V2 modules.

## Module Categories

### Core Modules

Foundation modules that provide essential platform functionality.

| Module | Summary |
| --- | --- |
| [Area Management](spp_area) | Establishes associations between registrants and geographical administrative areas with validation and hierarchy support. |
| [Base (Common)](spp_base_common) | Main menu, generic configuration, user role management base, area management base, and non-OpenSPP menu hiding. |
| [Base Settings](spp_base_setting) | Fundamental configurations for country implementations, Country Offices, and user management. |
| [GIS](spp_gis) | GIS core with area geo fields, importer extensions, layers, and spatial queries. |
| [Programs](spp_programs) | Manage cash and in-kind entitlements, integrate with inventory, and program management for social protection. |
| [Registry](spp_registry) | Consolidated registry management for individuals, groups, and membership. |
| [Security](spp_security) | Central security definitions for OpenSPP modules. |
| [Storage Backend](spp_storage_backend) | Pluggable storage backend configuration (Odoo, S3, Azure, Filesystem). |

### API V2 Modules

RESTful API modules built on FastAPI for external system integration.

| Module | Summary |
| --- | --- |
| [API V2](spp_api_v2) | Core API V2 module providing FastAPI-based RESTful endpoints. |
| [API V2 - Change Request](spp_api_v2_change_request) | REST API endpoints for Change Request V2. |
| [API V2 - Cycles](spp_api_v2_cycles) | API endpoints for program cycle management. |
| [API V2 - Data](spp_api_v2_data) | API endpoints for variable data push/pull. |
| [API V2 - Entitlements](spp_api_v2_entitlements) | API endpoints for entitlement management. |
| [API V2 - GIS](spp_api_v2_gis) | OGC API - Features compliant GIS endpoints for QGIS and GovStack. |
| [API V2 - Products](spp_api_v2_products) | API endpoints for product catalog management. |
| [API V2 - Service Points](spp_api_v2_service_points) | API endpoints for service point management. |
| [API V2 - Simulation](spp_api_v2_simulation) | REST API for simulation scenario management. |
| [API V2 - Vocabulary](spp_api_v2_vocabulary) | API endpoints for vocabulary/lookup data. |
| [OAuth](spp_oauth) | OAuth 2.0 authentication framework for API security. |

### Case Management Modules

Modules for individual case tracking and management.

| Module | Summary |
| --- | --- |
| [Case Management Base](spp_case_base) | Core case management with configurable workflow stages and intervention plans. |
| [Case: CEL Rules](spp_case_cel) | CEL-based triage and assignment rules for case management. |
| [Case: Demo Data](spp_case_demo) | Demo data generator for Case Management. |
| [Case: Entitlements](spp_case_entitlements) | Links cases to program entitlements for relationship tracking. |
| [Case: Graduation](spp_case_graduation) | Link graduation assessments to cases for exit management. |
| [Case: Programs](spp_case_programs) | Links cases to programs with compliance tracking. |
| [Case: Registry](spp_case_registry) | Links cases to registrants with area auto-population. |
| [Case: Sessions](spp_case_session) | Link sessions and training attendance to cases. |

### CEL Modules

Common Expression Language modules for rule-based logic.

| Module | Summary |
| --- | --- |
| [CEL Domain Query Builder](spp_cel_domain) | Write simple CEL-like expressions to filter records. |
| [CEL Event Data](spp_cel_event) | Integrate event data with CEL expressions for eligibility rules. |
| [CEL Expression Widget](spp_cel_widget) | Reusable CEL expression editor with syntax highlighting and autocomplete. |
| [CEL Registry Search](spp_cel_registry_search) | Search the registry using CEL expressions. |
| [CEL Vocabulary](spp_cel_vocabulary) | Vocabulary-aware CEL functions for eligibility rules. |

### Change Request Modules

Workflow modules for managing data change requests.

| Module | Summary |
| --- | --- |
| [Change Request V2](spp_change_request_v2) | Configuration-driven change request system with conflict detection and duplicate prevention. |
| [CR Types - Advanced](spp_cr_types_advanced) | Advanced change request types with custom Python strategies. |
| [CR Types - Base](spp_cr_types_base) | Basic change request types with field mapping strategy. |

### DRIMS Modules

Disaster Response Inventory Management System.

| Module | Summary |
| --- | --- |
| [DRIMS](spp_drims) | Disaster relief inventory management for donations, requests, and distribution tracking. |
| [DRIMS - Sri Lanka](spp_drims_sl) | Sri Lanka-specific configuration for DRIMS with geographic hierarchy and approval thresholds. |
| [DRIMS - Sri Lanka Demo](spp_drims_sl_demo) | Demo data generator for DRIMS Sri Lanka implementation. |

### Farmer Registry Modules

Modules for agricultural beneficiary management.

| Module | Summary |
| --- | --- |
| [Farmer Registry](spp_farmer_registry) | Farm details, agricultural activities, seasons, and CEL variable integration. |
| [Farmer Registry: Change Requests](spp_farmer_registry_cr) | Farmer-specific change request types for farm details and activities. |
| [Farmer Registry: Dashboard](spp_farmer_registry_dashboard) | Dashboard with CEL-based metrics and trends for farmer data. |
| [Farmer Registry: Demo](spp_farmer_registry_demo) | Demo generator with fixed stories and volume generation. |
| [Farmer Registry: Vocabularies](spp_farmer_registry_vocabularies) | FAO-aligned vocabularies for crops, livestock, and aquaculture. |

### GIS Modules

Geographic Information System modules for spatial data and mapping.

| Module | Summary |
| --- | --- |
| [GIS Indicators](spp_gis_indicators) | Choropleth visualization with color scales and classification methods. |
| [GIS Reports](spp_gis_report) | Geographic visualization and reporting for social protection data. |
| [GIS Reports - Programs](spp_gis_report_programs) | Add program context filtering to GIS reports. |
| [Registrant GIS](spp_registrant_gis) | Adds GPS coordinates to registrants for spatial queries. |

### GRM Modules

Grievance Redress Mechanism modules.

| Module | Summary |
| --- | --- |
| [GRM](spp_grm) | Centralized grievance receiving, tracking, and resolution with multi-channel submission. |
| [GRM: Case Link](spp_grm_case_link) | Links GRM tickets with Case Management for escalation. |
| [GRM: CEL Rules](spp_grm_cel) | CEL-based routing and escalation rules for GRM tickets. |
| [GRM: Demo Data](spp_grm_demo) | Demo data generator for GRM with story-based tickets. |
| [GRM: Programs](spp_grm_programs) | Link GRM tickets to programs, entitlements, and payments. |
| [GRM: Registry](spp_grm_registry) | Link GRM tickets to registrants with repeat ticket detection. |

### Hazard & Emergency Modules

Modules for disaster and emergency management.

| Module | Summary |
| --- | --- |
| [Hazard & Emergency Management](spp_hazard) | Hazard classification, incident recording, and impact assessment for emergency response. |
| [Hazard: Programs](spp_hazard_programs) | Links hazard impacts to program eligibility and emergency entitlements. |

### Indicators & Metrics Modules

Modules for data analytics, indicators, and scoring.

| Module | Summary |
| --- | --- |
| [Analytics](spp_analytics) | Query engine for indicators, simulations, and GIS analytics. |
| [Indicator](spp_indicator) | Publishable indicators based on CEL variables for dashboards, GIS, and APIs. |
| [Indicator Studio](spp_indicator_studio) | Studio UI for managing publishable indicators. |
| [Metric](spp_metric) | Unified metric foundation for indicators and simulations. |
| [Metric Service](spp_metric_service) | Computation services for fairness, distribution, breakdown, and privacy. |

### Integration Modules

Modules for external system integration and data exchange.

| Module | Summary |
| --- | --- |
| [Banking](spp_banking) | Bank account details for registrants and payment processing. |
| [DCI Core](spp_dci) | Core DCI (Digital Convergence Initiative) API components and schemas. |
| [DCI Client](spp_dci_client) | Base DCI client infrastructure with OAuth2 and data source management. |
| [DCI Client - CRVS](spp_dci_client_crvs) | Connect to Civil Registration and Vital Statistics registries via DCI API. |
| [DCI Client - Disability](spp_dci_client_dr) | Connect to Disability Registries via DCI API. |
| [DCI Client - IBR](spp_dci_client_ibr) | Connect to Identity Bureau for duplication checks via DCI API. |
| [DCI Server](spp_dci_server) | DCI API server infrastructure with FastAPI routers. |
| [Document Management System](spp_dms) | Centralized document management with directory trees and indexed storage. |
| [Event Data](spp_event_data) | Records events from surveys, field visits, and external systems (ODK, KoBoToolbox). |
| [HXL Integration](spp_hxl) | Humanitarian Exchange Language support for data interoperability. |
| [HXL Area Integration](spp_hxl_area) | HXL import with area-level aggregation for humanitarian indicators. |
| [Import Match](spp_import_match) | Intelligent import matching to prevent duplication during bulk data onboarding. |
| [Service Points](spp_service_points) | Manage physical or virtual service delivery locations with area linking. |
| [Source Tracking](spp_source_tracking) | Track data provenance and source information for registrants. |
| [Vocabulary](spp_vocabulary) | Centralized vocabulary and lookup value management. |

### Monitoring Modules

Modules for audit, compliance, and approval workflows.

| Module | Summary |
| --- | --- |
| [Alerts](spp_alerts) | Generic alert engine for threshold monitoring, expiry tracking, and deadlines. |
| [Approval](spp_approval) | Standardized approval workflows with multi-tier sequencing and CEL rules. |
| [Audit](spp_audit) | Immutable change history with multiple backends (database, file, syslog, HTTP). |

### Registry Extensions

Modules extending core registry functionality.

| Module | Summary |
| --- | --- |
| [Disability Registry](spp_disability_registry) | WG-SS/CFM disability assessments, assistive device tracking, and CEL functions. |
| [Graduation](spp_graduation) | Manage graduation and exit from time-bound social protection programs. |
| [Group Hierarchy](spp_registry_group_hierarchy) | Hierarchical group relationships with nested group structures. |
| [Registry Search Portal](spp_registry_search) | Search-first registry interface for privacy protection. |
| [Session Tracking](spp_session_tracking) | Track attendance at required sessions and trainings. |

### Scoring & Targeting Modules

Modules for beneficiary assessment and targeting.

| Module | Summary |
| --- | --- |
| [Scoring](spp_scoring) | Configurable scoring and assessment framework for beneficiary targeting. |
| [Scoring: Programs](spp_scoring_programs) | Integrates scoring with program eligibility and entitlements. |
| [Simulation](spp_simulation) | Simulate targeting scenarios and analyze fairness before committing. |

### Security & Identity Modules

Modules for access control, encryption, privacy, and security features.

| Module | Summary |
| --- | --- |
| [Attachment Antivirus Scan](spp_attachment_av_scan) | ClamAV-based antivirus scanning with quarantine workflow. |
| [Consent](spp_consent) | DPV-aligned consent management implementing ISO/IEC TS 27560:2023. |
| [Encryption](spp_encryption) | JWE encryption, JWT signing, and Linked Data Proof signing. |
| [Key Management](spp_key_management) | Centralized cryptographic key management with pluggable providers. |
| [QR Credentials](spp_claim_169) | MOSIP Claim 169 QR code identity credentials for registrants. |
| [User Roles](spp_user_roles) | Area-based access control with global and local role definitions. |

### Studio Modules

No-code configuration tools for implementers.

| Module | Summary |
| --- | --- |
| [Custom Fields](spp_custom_field) | Define and add custom data fields to registrant profiles. |
| [Studio](spp_studio) | No-code customization interface for OpenSPP. |
| [Studio - API V2](spp_studio_api_v2) | Bridge Studio custom fields and variables with API v2. |
| [Studio - Change Requests](spp_studio_change_requests) | No-code change request type builder. |
| [Studio - Events](spp_studio_events) | No-code event type designer for data collection. |

### Utility Modules

Helper modules providing common utilities and tools.

| Module | Summary |
| --- | --- |
| [Area HDX Integration](spp_area_hdx) | HDX Common Operational Datasets integration for admin boundaries. |
| [Hide Menus: Base](spp_hide_menus_base) | Manage visibility of navigation menus for specific user groups. |
| [Irrigation](spp_irrigation) | Irrigation asset management with GIS and water distribution networks. |
| [Land Record](spp_land_record) | Land parcel records with ownership, lease tracking, and GIS fields. |
| [Versioning](spp_versioning) | Artifact versioning with scheduled activation. |

### Starter & Demo Modules

Pre-configured bundles and demonstration data.

| Module | Summary |
| --- | --- |
| [Demo](spp_demo) | Core demo module with data generator and sample data. |
| [MIS Demo V2](spp_mis_demo_v2) | Demo Generator V2 for SP-MIS programs with fixed stories and volume generation. |
| [Starter: Farmer Registry](spp_starter_farmer_registry) | Complete Farmer Registry bundle with API, DCI, and Program support. |
| [Starter: Social Registry](spp_starter_social_registry) | Complete Social Registry bundle with API, DCI, and Change Request support. |
| [Starter: SP-MIS](spp_starter_sp_mis) | Complete SP-MIS bundle with Social Registry, Programs, and Service Points. |

### Theme & Branding

| Module | Summary |
| --- | --- |
| [Branding Kit](spp_branding_kit) | Branding customization, URL routing (`/openspp`), and telemetry management. |
| [Theme](theme_openspp_muk) | OpenSPP visual theme and branding. |

```{toctree}
:maxdepth: 1
:hidden:

spp_alerts
spp_analytics
spp_api_v2
spp_approval
spp_area
spp_area_hdx
spp_attachment_av_scan
spp_audit
spp_banking
spp_base_common
spp_base_setting
spp_branding_kit
spp_case_base
spp_cel_domain
spp_change_request_v2
spp_claim_169
spp_consent
spp_custom_field
spp_dci
spp_demo
spp_disability_registry
spp_dms
spp_drims
spp_encryption
spp_event_data
spp_farmer_registry
spp_gis
spp_graduation
spp_grm
spp_hazard
spp_hide_menus_base
spp_hxl
spp_import_match
spp_indicator
spp_indicator_studio
spp_irrigation
spp_key_management
spp_land_record
spp_metric
spp_metric_service
spp_mis_demo_v2
spp_oauth
spp_programs
spp_registrant_gis
spp_registry
spp_registry_group_hierarchy
spp_registry_search
spp_scoring
spp_security
spp_service_points
spp_session_tracking
spp_simulation
spp_source_tracking
spp_starter_farmer_registry
spp_starter_social_registry
spp_starter_sp_mis
spp_storage_backend
spp_studio
spp_user_roles
spp_versioning
spp_vocabulary
theme_openspp_muk
```
