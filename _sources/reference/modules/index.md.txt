---
openspp:
  doc_status: draft
  products: [core]
---

# Modules Reference

This section provides comprehensive documentation for all OpenSPP V2 modules in **Stable** status. These modules have been tested and are production-ready.

## Module Categories

### Core Modules

Foundation modules that provide essential platform functionality.

| Module                              | Summary                                                                                                                                                                                                                              |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Area Management](spp_area)         | Establishes direct associations between registrants, beneficiary groups, and their corresponding geographical administrative areas. It validates registrant-area linkages against official area types, ensuring data integrity.     |
| [Base (Common)](spp_base_common)    | The base module that provides the main menu, generic configuration, user role management base module, area management base module, and hiding of non-OpenSPP menus. All implementation-specific base modules depend on this module. |
| [Base Settings](spp_base_setting)   | Provides fundamental configurations for country implementations, establishing core organizational structures such as Country Offices. It also enables tailored user interface adaptations and streamlines user management.          |
| [Programs](spp_programs)            | Manage cash and in-kind entitlements, integrate with inventory, and enhance program management features for comprehensive social protection and agricultural support.                                                               |
| [Registry](spp_registry)            | Consolidated registry management for individuals, groups, and membership.                                                                                                                                                           |
| [Security](spp_security)            | Central security definitions for OpenSPP modules.                                                                                                                                                                                   |

### API V2 Modules

RESTful API modules built on FastAPI for external system integration.

| Module                                             | Summary                                                        |
| -------------------------------------------------- | -------------------------------------------------------------- |
| [API V2](spp_api_v2)                               | Core API V2 module providing FastAPI-based RESTful endpoints.  |
| [API V2 - Cycles](spp_api_v2_cycles)               | API endpoints for program cycle management.                    |
| [API V2 - Data](spp_api_v2_data)                   | API endpoints for data export and reporting.                   |
| [API V2 - Entitlements](spp_api_v2_entitlements)   | API endpoints for entitlement management.                      |
| [API V2 - Products](spp_api_v2_products)           | API endpoints for product catalog management.                  |
| [API V2 - Service Points](spp_api_v2_service_points) | API endpoints for service point management.                  |
| [API V2 - Vocabulary](spp_api_v2_vocabulary)       | API endpoints for vocabulary/lookup data.                      |

### Studio Modules

No-code configuration tools for implementers.

| Module                                               | Summary                                                                                                                                                         |
| ---------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Custom Fields](spp_custom_field)                    | Enables administrators to define and add custom data fields directly to registrant profiles, tailoring data collection for specific social protection programs. |
| [Studio](spp_studio)                                 | No-code customization interface for OpenSPP.                                                                                                                    |
| [Studio - Change Requests](spp_studio_change_requests) | No-code change request type builder.                                                                                                                          |
| [Studio - Events](spp_studio_events)                 | No-code event type designer for data collection.                                                                                                                |

### Change Request Modules

Workflow modules for managing data change requests.

| Module                                               | Summary                                                                                                       |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| [Change Request V2](spp_change_request_v2)           | Configuration-driven change request system with UX improvements, conflict detection and duplicate prevention. |
| [CR Types - Advanced](spp_cr_types_advanced)         | Advanced change request types with custom Python strategies for membership and lifecycle operations.          |
| [CR Types - Base](spp_cr_types_base)                 | Basic change request types with field mapping strategy.                                                       |

### CEL Modules

Common Expression Language modules for rule-based logic.

| Module                                    | Summary                                                                         |
| ----------------------------------------- | ------------------------------------------------------------------------------- |
| [CEL Domain Query Builder](spp_cel_domain)| Write simple CEL-like expressions to filter records (OpenSPP/OpenG2P friendly). |
| [CEL Expression Widget](spp_cel_widget)   | Reusable CEL expression editor with syntax highlighting and autocomplete.       |

### GIS Modules

Geographic Information System modules for spatial data and mapping.

| Module                        | Summary                                                                                    |
| ----------------------------- | ------------------------------------------------------------------------------------------ |
| [GIS](spp_gis)                | GIS core plus area geo fields and importer extensions (points/polygons, layers, queries). |
| [GIS Reports](spp_gis_report) | Geographic visualization and reporting for social protection data.                        |

### Monitoring Modules

Modules for audit, compliance, and grievance management.

| Module                                   | Summary                                                                                                                                                                                                                                                             |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Approval](spp_approval)                 | Standardized approval workflows with multi-tier sequencing and CEL rules.                                                                                                                                                                                           |
| [Audit](spp_audit)                       | Comprehensively tracks all data modifications and user actions across the platform, recording old and new values. It enhances accountability and data integrity by maintaining an immutable history of changes. Supports multiple backends (database, file, syslog, HTTP). |
| [Grievance Redress Mechanism](spp_grm)   | Provides a centralized Grievance Redress Mechanism for receiving, tracking, and resolving beneficiary complaints and feedback. It supports multi-channel submission and manages resolution workflows through customizable stages.                                   |

### Security & Identity Modules

Modules for access control, encryption, privacy, and security features.

| Module                                 | Summary                                                                                                                                                                                                                                |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Consent](spp_consent)                 | DPV-aligned consent management implementing ISO/IEC TS 27560:2023 for GDPR-compliant consent lifecycle management.                                                                                                                     |
| [Key Management](spp_key_management)   | Centralized cryptographic key management with pluggable providers.                                                                                                                                                                     |
| [QR Credentials](spp_claim_169)        | MOSIP Claim 169 QR code identity credential generation for registrants with configurable attribute mapping.                                                                                                                            |
| [User Roles](spp_user_roles)           | Defines and manages distinct user roles, categorizing them as global or local, to implement area-based access control. It restricts user access to specific geographical areas and automates underlying system permission assignments. |

### Integration Modules

Modules for external system integration and data exchange.

| Module                                            | Summary                                                                                                                                                                                                                                |
| ------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Banking](spp_banking)                            | Manages bank account details for registrants and payment processing.                                                                                                                                                                   |
| [DCI Client](spp_dci_client)                      | Base DCI client infrastructure with OAuth2 and data source management for interoperability.                                                                                                                                            |
| [DCI Client - CRVS](spp_dci_client_crvs)          | Connect to Civil Registration and Vital Statistics registries via DCI API.                                                                                                                                                             |
| [DCI Client - Disability](spp_dci_client_dr)      | Connect to Disability Registries via DCI API for disability status verification.                                                                                                                                                       |
| [DCI Client - IBR](spp_dci_client_ibr)            | Connect to Identity Bureau for duplication checks via DCI API.                                                                                                                                                                         |
| [DCI Server](spp_dci_server)                      | DCI API server infrastructure with FastAPI routers for receiving external requests.                                                                                                                                                    |
| [Document Management System](spp_dms)             | Provides a centralized system for managing and organizing program-related documents within a structured directory tree. It facilitates efficient document retrieval through categorization and indexed storage.                        |
| [Event Data](spp_event_data)                      | Records and tracks events related to individual and group registrants from surveys, field visits, and external systems like ODK and KoBoToolbox.                                                                                       |
| [Service Points](spp_service_points)              | Manages physical or virtual locations for social protection service delivery, establishing and categorizing operational service points. It links these points to hierarchical geographical areas, company entities, and user accounts. |
| [Source Tracking](spp_source_tracking)            | Track data provenance and source information for registrants.                                                                                                                                                                          |
| [Vocabulary](spp_vocabulary)                      | Centralized vocabulary and lookup value management.                                                                                                                                                                                    |

### Utility Modules

Helper modules providing common utilities and tools.

| Module                                      | Summary                                                                                                                  |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| [Hide Menus: Base](spp_hide_menus_base)     | Administrators can manage the visibility of navigation menus, streamlining the user interface for specific user groups. |
| [Registry Search Portal](spp_registry_search) | Search-first registry interface for privacy protection.                                                                |
| [Versioning](spp_versioning)                | Artifact versioning with scheduled activation.                                                                           |

### Starter & Demo Modules

Pre-configured bundles and demonstration data.

| Module                                                | Summary                                                                         |
| ----------------------------------------------------- | ------------------------------------------------------------------------------- |
| [Demo](spp_demo)                                      | Core demo module with data generator and sample data.                           |
| [MIS Demo V2](spp_mis_demo_v2)                        | Demo Generator V2 for SP-MIS programs with fixed stories and volume generation. |
| [Starter: Social Registry](spp_starter_social_registry) | Complete Social Registry bundle with API, DCI, and Change Request support.    |
| [Starter: SP-MIS](spp_starter_sp_mis)                 | Complete SP-MIS bundle with Social Registry, Programs, and Service Points.      |

### Theme & Branding

| Module                             | Summary                                                                     |
| ---------------------------------- | --------------------------------------------------------------------------- |
| [Branding Kit](spp_branding_kit)   | Branding customization, URL routing (`/openspp`), and telemetry management. |
| [Theme](theme_openspp_muk)         | OpenSPP visual theme and branding.                                          |

```{toctree}
:maxdepth: 1
:hidden:

spp_api_v2
spp_api_v2_cycles
spp_api_v2_data
spp_api_v2_entitlements
spp_api_v2_products
spp_api_v2_service_points
spp_api_v2_vocabulary
spp_approval
spp_area
spp_audit
spp_banking
spp_base_common
spp_base_setting
spp_branding_kit
spp_cel_domain
spp_cel_widget
spp_change_request_v2
spp_claim_169
spp_consent
spp_cr_types_advanced
spp_cr_types_base
spp_custom_field
spp_dci_client
spp_dci_client_crvs
spp_dci_client_dr
spp_dci_client_ibr
spp_dci_server
spp_demo
spp_dms
spp_event_data
spp_gis
spp_gis_report
spp_grm
spp_hide_menus_base
spp_key_management
spp_mis_demo_v2
spp_programs
spp_registry
spp_registry_search
spp_security
spp_service_points
spp_source_tracking
spp_starter_social_registry
spp_starter_sp_mis
spp_studio
spp_studio_change_requests
spp_studio_events
spp_user_roles
spp_versioning
spp_vocabulary
theme_openspp_muk
```
