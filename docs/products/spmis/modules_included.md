---
openspp:
  doc_status: draft
---

# Modules included

The OpenSPP SP-MIS product includes the following 34 modules. Together they provide the foundational capabilities for managing the full lifecycle of a social protection program.

- **{doc}`OpenSPP Registry </reference/modules/spp_registry>`**: Consolidated registry management for individuals, groups, and membership.
- **{doc}`OpenSPP Registry Search Portal </reference/modules/spp_registry_search>`**: Search-first registry interface for privacy protection.
- **{doc}`OpenSPP Security </reference/modules/spp_security>`**: Central security definitions for OpenSPP modules.
- **{doc}`OpenSPP Area Management </reference/modules/spp_area>`**: Establishes direct associations between OpenSPP registrants, beneficiary groups, and their corresponding geographical administrative areas.
- **{doc}`OpenSPP Vocabulary </reference/modules/spp_vocabulary>`**: Standardized code list management system for OpenSPP.
- **{doc}`OpenSPP Consent </reference/modules/spp_consent>`**: DPV-aligned consent management for social protection programs.
- **{doc}`OpenSPP Source Tracking </reference/modules/spp_source_tracking>`**: Track data provenance and source information for registrants.
- **{doc}`OpenSPP Source Tracking - Programs </reference/modules/spp_source_tracking_programs>`**: Source tracking for program memberships; auto-activates with `spp_programs`.
- **{doc}`OpenSPP Banking / Bank Details </reference/modules/spp_banking>`**: Financial account and mobile money details for beneficiaries.
- **{doc}`OpenSPP Custom Fields </reference/modules/spp_custom_field>`**: Configurable custom fields for programme-specific registry data.
- **{doc}`OpenSPP Change Request V2 </reference/modules/spp_change_request_v2>`**: Configuration-driven change request system with UX improvements, conflict detection and duplicate prevention.
- **{doc}`OpenSPP CR Types - Base </reference/modules/spp_cr_types_base>`**: Basic change request types with field mapping strategy.
- **{doc}`OpenSPP Document Management System </reference/modules/spp_dms>`**: Attaches and manages documents against registry and programme records.
- **{doc}`OpenSPP CEL Domain Query Builder </reference/modules/spp_cel_domain>`**: Write simple CEL-like expressions to filter records.
- **{doc}`OpenSPP CEL Expression Widget </reference/modules/spp_cel_widget>`**: UI widget for composing CEL expressions within OpenSPP forms.
- **{doc}`OpenSPP Studio </reference/modules/spp_studio>`**: No-code customization interface for OpenSPP.
- **{doc}`OpenSPP Studio - Programs </reference/modules/spp_studio_programs>`**: Program scoping for Studio configurations; auto-activates with `spp_programs`.
- **{doc}`OpenSPP Audit </reference/modules/spp_audit>`**: Audit logging of user actions and data changes.
- **{doc}`OpenSPP Audit - Programs </reference/modules/spp_audit_programs>`**: Program and cycle audit rules; auto-activates with `spp_programs`.
- **{doc}`OpenSPP Versioning </reference/modules/spp_versioning>`**: Point-in-time versioning of registry and programme records.
- **{doc}`OpenSPP API V2 </reference/modules/spp_api_v2>`**: Standards-aligned, consent-respecting API for social protection data exchange.
- **{doc}`OpenSPP API V2 - Data </reference/modules/spp_api_v2_data>`**: REST API endpoints for Variable Data push/pull.
- **{doc}`OpenSPP API V2 - Cycles </reference/modules/spp_api_v2_cycles>`**: API V2 cycle endpoints; auto-activates with `spp_programs`.
- **{doc}`OpenSPP API V2 - Programs </reference/modules/spp_api_v2_programs>`**: API V2 Program and Program Membership endpoints; auto-activates with `spp_programs`.
- **{doc}`OpenSPP DCI Client </reference/modules/spp_dci_client>`**: Base DCI client infrastructure with OAuth2 and data source management.
- **{doc}`OpenSPP DCI Client - CRVS </reference/modules/spp_dci_client_crvs>`**: Connect to CRVS registries via DCI API.
- **{doc}`OpenSPP DCI Client - IBR </reference/modules/spp_dci_client_ibr>`**: Connect to IBR for duplication checks via DCI API.
- **{doc}`OpenSPP DCI Client - Disability Registry </reference/modules/spp_dci_client_dr>`**: Connect to Disability Registry via DCI API.
- **{doc}`OpenSPP DCI Server </reference/modules/spp_dci_server>`**: Exposes the SP-MIS as a DCI-compliant queryable endpoint.
- **{doc}`OpenSPP Programs </reference/modules/spp_programs>`**: Manage cash and in-kind entitlements, integrate with inventory, and enhance program management features.
- **{doc}`OpenSPP Approval </reference/modules/spp_approval>`**: Standardized approval workflows with multi-tier sequencing and CEL rules.
- **{doc}`OpenSPP Event Data </reference/modules/spp_event_data>`**: Records and tracks events related to individual and group registrants.
- **{doc}`OpenSPP Service Points Management </reference/modules/spp_service_points>`**: Manages physical or virtual locations for social protection service delivery.
- **{doc}`OpenSPP User Roles </reference/modules/spp_user_roles>`**: Defines and manages distinct user roles to implement area-based access control.

## Expanding the SP-MIS

The base SP-MIS includes everything needed to set up a foundational system. It can be expanded with additional modules to suit specific needs. Read more about {doc}`module installation </get_started/modules/index>`.
