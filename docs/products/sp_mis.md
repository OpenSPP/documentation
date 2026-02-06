---
myst:
  html_meta:
    "title": "Social Protection Management Information System (SP-MIS)"
    "description": "OpenSPP SP-MIS product configuration for comprehensive social protection program management from enrollment to payment"
    "keywords": "OpenSPP, SP-MIS, social protection, management information system, beneficiary management, payments"
---
# OpenSPP SP-MIS
*A digital system to manage the full lifecycle of social protection programs*

The **OpenSPP Social Protection Management Information System (SP-MIS)** is a comprehensive platform designed to manage the entire lifecycle of a social protection program. It supports both routine and emergency interventions, whether cash or in-kind, and empowers citizens through secure, verifiable credentials.

## Key features

**Easy registration and data collection –** Build and maintain a continuously updated database through imports, system integrations, or direct registration. Structured workflows support reliable updates, whether initiated by the citizens or registrars.

*Read more about {doc}`Unified and hierarchical beneficiary registry <features/unified_registry>`.*
<!--**Verifiable Credentials –** Issue unique IDs and documents with QR codes through secure and streamlined processes to attest to program eligibility. -->

**Targeting and integrated service delivery –** With a flexible approach to eligibility and targeting, the OpenSPP SP-MIS can serve as a central data repository to support a wide array of programs.

*Read more about {doc}`Eligibility and targeting <features/eligibility_targeting>`.*

**Program and Distribution Management –** A core feature in OpenSPP SP-MIS is its ability to support the delivery of both cash and in-kind entitlements. Automate cash transfers via financial service providers, issue vouchers, or manage food and non-food item distribution, including stock and warehouse management.

*Read more about {doc}`End-to-end program and entitlement management <features/program_management>`, {doc}`Pluggable payment and disbursement <features/payment_disbursement>` and {doc}`In-kind benefits and inventory management (GRM) <features/in_kind_benefits>`.*

**Change management through formal change requests –** Route sensitive updates through configurable approval workflows with role-based controls and full audit trails. Track what changed, who made the change, and why, ensuring data integrity, accountability, and trust in program decisions.

*Read more about {doc}`Auditable change management <features/change_management>`.*

<!--TODO: EXPAND ON THIS **Approval Workflows**: Multi-level approval for sensitive operations-->

**Monitoring, reporting, and public accountability –** Maintain full audit trails, track all user actions, and provide dashboards and analytics for evidence-based decision-making. This capability is crucial for tracking program performance, demonstrating effectiveness to donors, and building public trust.

*Read more about {doc}`Auditable change management <features/change_management>` and {doc}`Grievance Redress Mechanism (GRM) <features/grievance_redress>`.*

**Interoperability with other systems –** Connect securely with other national databases (e.g., ID, health, civil registration) through RESTful APIs to pull information directly, ensuring that the information is up-to-date.

*Read more about {doc}`Data integration and interoperability (APIs) <features/data_integration_apis>`.*

## Who is it for?

**Governments** managing national or local social protection systems

**Social protection agencies** delivering cash or in-kind programs

**NGOs and development partners** supporting vulnerable households

## OpenSPP modules included

The preconfigured OpenSPP SP-MIS product is intended to provide the basic use cases of an SP-MIS.

The following modules are included in the OpenSPP SP-MIS product:

- **{doc}`OpenSPP Registry <../../reference/modules/spp_registry>`**: Consolidated registry management for individuals, groups, and membership.
- **{doc}`OpenSPP Registry Search Portal <../../reference/modules/spp_registry_search>`**: Search-first registry interface for privacy protection.
- **{doc}`OpenSPP Security <../../reference/modules/spp_security>`**: Central security definitions for OpenSPP modules.
- **{doc}`OpenSPP Area Management <../../reference/modules/spp_area>`**: Establishes direct associations between OpenSPP registrants, beneficiary groups, and their corresponding geographical administrative areas.
- **{doc}`OpenSPP Vocabulary <../../reference/modules/spp_vocabulary>`**: Standardized code list management system for OpenSPP.
- **{doc}`OpenSPP Consent <../../reference/modules/spp_consent>`**: DPV-aligned consent management for social protection programs.
- **{doc}`OpenSPP Source Tracking <../../reference/modules/spp_source_tracking>`**: Track data provenance and source information for registrants.
- **{doc}`OpenSPP Change Request V2 <../../reference/modules/spp_change_request_v2>`**: Configuration-driven change request system with UX improvements, conflict detection and duplicate prevention".
- **{doc}`OpenSPP CR Types - Base <../../reference/modules/spp_cr_types_base>`**: Basic change request types with field mapping strategy.
- **{doc}`OpenSPP CEL Domain Query Builder <../../reference/modules/spp_cel_domain>`**: Write simple CEL-like expressions to filter records.
- **{doc}`OpenSPP Studio <../../reference/modules/spp_studio>`**: No-code customization interface for OpenSPP.
- **{doc}`OpenSPP API V2 <../../reference/modules/spp_api_v2>`**: Standards-aligned, consent-respecting API for social protection data exchange.
- **{doc}`OpenSPP API V2 - Data <../../reference/modules/spp_api_v2_data>`**: REST API endpoints for Variable Data push/pull.
- **{doc}`OpenSPP DCI Client <../../reference/modules/spp_dci_client>`**: Base DCI client infrastructure with OAuth2 and data source management
- **{doc}`OpenSPP DCI Client - CRVS <../../reference/modules/spp_dci_client_crvs>`**: Connect to CRVS registries via DCI API.
- **{doc}`OpenSPP DCI Client - IBR <../../reference/modules/spp_dci_client_ibr>`**: Connect to IBR for duplication checks via DCI API.
- **{doc}`OpenSPP DCI Client - Disability Registry <../../reference/modules/spp_dci_client_dr>`**: Connect to Disability Registry via DCI API.
- **{doc}`OpenSPP Programs <../../reference/modules/spp_programs>`**: Manage cash and in-kind entitlements, integrate with inventory, and enhance program management features.
- **{doc}`OpenSPP Approval <../../reference/modules/spp_approval>`**: Standardized approval workflows with multi-tier sequencing and CEL rules.
- **{doc}`OpenSPP Event Data <../../reference/modules/spp_event_data>`**: Records and tracks events related to individual and group registrants."
- **{doc}`OpenSPP Service Points Management <../../reference/modules/spp_service_points>`**: Manages physical or virtual locations for social protection service delivery.
- **{doc}`OpenSPP User Roles <../../reference/modules/spp_user_roles>`**: Defines and manages distinct user roles to implement area-based access control.

## Expanding the SPMIS

The OpenSPP-based SPMIS contains everything that is necessary to set up a foundational SPMIS. It can however be expanded with additional functionalities to perfectly suit the specific needs, read more about {doc}`module installation <../get_started/modules/index>`.

<!--
### Common features to expand with

**Geo-spatial analysis and shock response –** Integrate GIS and external data (e.g., flood maps) with already known information to rapidly identify and assist affected households during crises without the need for time-consuming, emergency-specific registration and needs assessments.

*Read more about {doc}`Geospatial (GIS) and land management <features/gis_land_management>`.*
-->

## Next step

The OpenSPP SP-MIS is an open-source product, built and supported by the OpenSPP community. Read more about {doc}`installing OpenSPP SP-MIS <../get_started/modules/spmis_installation>`.
