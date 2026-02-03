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

| Module                                    | Summary                                                                                                                                                                                                                                     |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [OpenSPP Base (Common)](spp_base_common)  | The OpenSPP base module that provides the main menu, generic configuration, user role management base module, area management base module, and hiding of non-OpenSPP menus. All implementation-specific base modules depend on this module. |
| [OpenSPP Base Settings](spp_base_setting) | Provides fundamental configurations for country implementations, establishing core organizational structures such as Country Offices. It also enables tailored user interface adaptations and streamlines user management.                  |
| [OpenSPP Security](spp_security)          | Central security definitions for OpenSPP modules.                                                                                                                                                                                           |
| [OpenSPP Registry](spp_registry)          | Consolidated registry management for individuals, groups, and membership.                                                                                                                                                                   |
| [OpenSPP Area Management](spp_area)       | Establishes direct associations between OpenSPP registrants, beneficiary groups, and their corresponding geographical administrative areas. It validates registrant-area linkages against official area types, ensuring data integrity.     |
| [OpenSPP Programs](spp_programs)          | Manage cash and in-kind entitlements, integrate with inventory, and enhance program management features for comprehensive social protection and agricultural support.                                                                       |

### API V2 Modules

RESTful API modules built on FastAPI for external system integration.

| Module                                                       | Summary                                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------------------- |
| [OpenSPP API V2](spp_api_v2)                                 | Core API V2 module providing FastAPI-based RESTful endpoints for OpenSPP. |
| [OpenSPP API V2 - Cycles](spp_api_v2_cycles)                 | API endpoints for program cycle management.                               |
| [OpenSPP API V2 - Data](spp_api_v2_data)                     | API endpoints for data export and reporting.                              |
| [OpenSPP API V2 - Entitlements](spp_api_v2_entitlements)     | API endpoints for entitlement management.                                 |
| [OpenSPP API V2 - Products](spp_api_v2_products)             | API endpoints for product catalog management.                             |
| [OpenSPP API V2 - Service Points](spp_api_v2_service_points) | API endpoints for service point management.                               |
| [OpenSPP API V2 - Vocabulary](spp_api_v2_vocabulary)         | API endpoints for vocabulary/lookup data.                                 |

### Studio Modules

No-code configuration tools for implementers.

| Module                                                         | Summary                                                                                                                                                         |
| -------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [OpenSPP Studio](spp_studio)                                   | No-code customization interface for OpenSPP.                                                                                                                    |
| [OpenSPP Studio - Change Requests](spp_studio_change_requests) | No-code change request type builder.                                                                                                                            |
| [OpenSPP Studio - Events](spp_studio_events)                   | No-code event type designer for data collection.                                                                                                                |
| [OpenSPP Custom Fields](spp_custom_field)                      | Enables administrators to define and add custom data fields directly to registrant profiles, tailoring data collection for specific social protection programs. |

### Change Request Modules

Workflow modules for managing data change requests.

| Module                                             | Summary                                                                                                       |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| [OpenSPP Change Request V2](spp_change_request_v2) | Configuration-driven change request system with UX improvements, conflict detection and duplicate prevention. |
| [OpenSPP CR Types - Base](spp_cr_types_base)       | Basic change request types with field mapping strategy.                                                       |

### CEL Modules

Common Expression Language modules for rule-based logic.

| Module                                          | Summary                                                                         |
| ----------------------------------------------- | ------------------------------------------------------------------------------- |
| [CEL Domain Query Builder](spp_cel_domain)      | Write simple CEL-like expressions to filter records (OpenSPP/OpenG2P friendly). |
| [OpenSPP CEL Expression Widget](spp_cel_widget) | Reusable CEL expression editor with syntax highlighting and autocomplete.       |

### GIS Modules

Geographic Information System modules for spatial data and mapping.

| Module                                | Summary                                                                                           |
| ------------------------------------- | ------------------------------------------------------------------------------------------------- |
| [OpenSPP GIS](spp_gis)                | GIS core plus area geo fields and importer extensions (points/polygons, layers, spatial queries). |
| [OpenSPP GIS Reports](spp_gis_report) | Geographic visualization and reporting for social protection data.                                |

### Monitoring Modules

Modules for audit, compliance, and grievance management.

| Module                                         | Summary                                                                                                                                                                                                                                                                    |
| ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [OpenSPP Audit](spp_audit)                     | Comprehensively tracks all data modifications and user actions across the platform, recording old and new values. It enhances accountability and data integrity by maintaining an immutable history of changes. Supports multiple backends (database, file, syslog, HTTP). |
| [OpenSPP Grievance Redress Mechanism](spp_grm) | Provides a centralized Grievance Redress Mechanism for receiving, tracking, and resolving beneficiary complaints and feedback. It supports multi-channel submission and manages resolution workflows through customizable stages.                                          |
| [OpenSPP Approval](spp_approval)               | Standardized approval workflows with multi-tier sequencing and CEL rules.                                                                                                                                                                                                  |

### Security & Identity Modules

Modules for access control, encryption, and security features.

| Module                                       | Summary                                                                                                                                                                                                                                |
| -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [OpenSPP User Roles](spp_user_roles)         | Defines and manages distinct user roles, categorizing them as global or local, to implement area-based access control. It restricts user access to specific geographical areas and automates underlying system permission assignments. |
| [OpenSPP Key Management](spp_key_management) | Centralized cryptographic key management with pluggable providers.                                                                                                                                                                     |

### Integration Modules

Modules for external system integration and data exchange.

| Module                                                  | Summary                                                                                                                                                                                                                                |
| ------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [OpenSPP Service Points Management](spp_service_points) | Manages physical or virtual locations for social protection service delivery, establishing and categorizing operational service points. It links these points to hierarchical geographical areas, company entities, and user accounts. |
| [OpenSPP Event Data](spp_event_data)                    | Records and tracks events related to individual and group registrants from surveys, field visits, and external systems like ODK and KoBoToolbox.                                                                                       |
| [OpenSPP Document Management System](spp_dms)           | Provides a centralized system for managing and organizing program-related documents within a structured directory tree. It facilitates efficient document retrieval through categorization and indexed storage.                        |
| [OpenSPP Banking: Bank Details](spp_banking)            | Manages bank account details for registrants and payment processing.                                                                                                                                                                   |
| [OpenSPP Source Tracking](spp_source_tracking)          | Track data provenance and source information for registrants.                                                                                                                                                                          |
| [OpenSPP Vocabulary](spp_vocabulary)                    | Centralized vocabulary and lookup value management.                                                                                                                                                                                    |

### Utility Modules

Helper modules providing common utilities and tools.

| Module                                                | Summary                                                                                                                         |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| [OpenSPP Registry Search Portal](spp_registry_search) | Search-first registry interface for privacy protection.                                                                         |
| [OpenSPP Hide Menus: Base](spp_hide_menus_base)       | Administrators can manage the visibility of OpenSPP navigation menus, streamlining the user interface for specific user groups. |
| [OpenSPP Versioning](spp_versioning)                  | Artifact versioning with scheduled activation.                                                                                  |

### Starter & Demo Modules

Pre-configured bundles and demonstration data.

| Module                                                          | Summary                                                                         |
| --------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| [OpenSPP Starter: SP-MIS](spp_starter_sp_mis)                   | Complete SP-MIS bundle with Social Registry, Programs, and Service Points.      |
| [OpenSPP Starter: Social Registry](spp_starter_social_registry) | Complete Social Registry bundle with API, DCI, and Change Request support.      |
| [OpenSPP Demo](spp_demo)                                        | Core demo module with data generator and sample data for OpenSPP.               |
| [OpenSPP MIS Demo V2](spp_mis_demo_v2)                          | Demo Generator V2 for SP-MIS programs with fixed stories and volume generation. |

### Theme

| Module                             | Summary                            |
| ---------------------------------- | ---------------------------------- |
| [OpenSPP Theme](theme_openspp_muk) | OpenSPP visual theme and branding. |

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
spp_cel_domain
spp_cel_widget
spp_change_request_v2
spp_cr_types_base
spp_custom_field
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
