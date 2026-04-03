---
myst:
  html_meta:
    "title": "Social Registry for Social Protection Programs"
    "description": "OpenSPP Social Registry product configuration for centralized beneficiary identification, registration, and needs assessment"
    "keywords": "OpenSPP, social registry, beneficiary identification, targeting, social protection, needs assessment"
---

# OpenSPP Social Registry
*A flexible and secure platform to manage social program data*

The **OpenSPP Social Registry** is a digital platform that helps governments and organizations manage information about individuals and households. It provides a single, reliable source of data to improve targeting, reduce duplication, and coordinate services.

## Key features

**Easy registration and data collection –** Prepare the registry with all the fields needed. Collect information through bulk upload, direct entry in the UI, or secure connections with existing systems.

*Read more about {doc}`Unified and hierarchical beneficiary registry <features/unified_registry>`.*

**Change management through formal change requests –** Route sensitive updates through configurable approval workflows with role-based controls and full audit trails. Track what changed, who made the change, and why, ensuring data integrity, accountability, and trust in program decisions.

*Read more about {doc}`Auditable change management <features/change_management>`.*

**Targeting and integrated service delivery –** Flexible approach to eligibility and targeting - identify eligible beneficiaries based on simple criteria such as age or complex combinations of factors.

*Read more about {doc}`Eligibility and targeting <features/eligibility_targeting>`.*

**Monitoring and accountability –** Track changes and manage user permissions to ensure data security and integrity. Access dashboards for decision-making, transparency and long term monitoring.

*Read more about {doc}`Auditable change management <features/change_management>` and {doc}`Grievance Redress Mechanism (GRM) <features/grievance_redress>`.*

**Interoperability with other systems –** Connect seamlessly with other national databases (ID, health, civil registry) via secure APIs to make updates or to pull information directly, ensuring that the information is up-to-date.

*Read more about {doc}`Data integration and interoperability (APIs) <features/data_integration_apis>`.*

## Who is it for?

**Government agencies** wanting to have a reliable up to date registry that can act as foundation for interventions

**NGOs** delivering services at national or local level

**Policy makers** needing reliable data for planning and resource allocation

## OpenSPP modules included

The preconfigured OpenSPP Social Registry product is intended to provide support for the fundamental use cases of a social registry.

The following modules are included in the OpenSPP Social Registry product:

- **{doc}`OpenSPP Registry <../../reference/modules/spp_registry>`**: Consolidated registry management for individuals, groups, and membership.
- **{doc}`OpenSPP Registry Search Portal <../../reference/modules/spp_registry_search>`**: Search-first registry interface for privacy protection.
- **{doc}`OpenSPP Security <../../reference/modules/spp_security>`**: Central security definitions for OpenSPP modules.
- **{doc}`OpenSPP User Roles <../../reference/modules/spp_user_roles>`**: Defines and manages distinct user roles for area-based access control.
- **{doc}`OpenSPP Area Management <../../reference/modules/spp_area>`**: Establishes direct associations between OpenSPP registrants, beneficiary groups, and their corresponding geographical administrative areas.
- **{doc}`OpenSPP Vocabulary <../../reference/modules/spp_vocabulary>`**: Standardized code list management system for OpenSPP.
- **{doc}`OpenSPP Consent <../../reference/modules/spp_consent>`**: DPV-aligned consent management for social protection programs.
- **{doc}`OpenSPP Source Tracking <../../reference/modules/spp_source_tracking>`**: Track data provenance and source information for registrants.
- **{doc}`OpenSPP Banking / Bank Details <../../reference/modules/spp_banking>`**: Financial account and mobile money details for beneficiaries.
- **{doc}`OpenSPP Custom Fields <../../reference/modules/spp_custom_field>`**: Configurable custom fields for programme-specific registry data.
- **{doc}`OpenSPP Change Request V2 <../../reference/modules/spp_change_request_v2>`**: Configuration-driven change request system with UX improvements, conflict detection and duplicate prevention.
- **{doc}`OpenSPP CR Types - Base <../../reference/modules/spp_cr_types_base>`**: Basic change request types with field mapping strategy.
- **{doc}`OpenSPP Document Management System <../../reference/modules/spp_dms>`**: Attaches and manages documents against registry and programme records.
- **{doc}`OpenSPP CEL Domain Query Builder <../../reference/modules/spp_cel_domain>`**: Write simple CEL-like expressions to filter records.
- **{doc}`OpenSPP CEL Expression Widget <../../reference/modules/spp_cel_widget>`**: UI widget for composing CEL expressions within OpenSPP forms.
- **{doc}`OpenSPP Studio <../../reference/modules/spp_studio>`**: No-code customization interface for OpenSPP.
- **{doc}`OpenSPP Audit <../../reference/modules/spp_audit>`**: Audit logging of user actions and data changes.
- **{doc}`OpenSPP Versioning <../../reference/modules/spp_versioning>`**: Point-in-time versioning of registry and programme records.
- **{doc}`OpenSPP API V2 <../../reference/modules/spp_api_v2>`**: Standards-aligned, consent-respecting API for social protection data exchange.
- **{doc}`OpenSPP API V2 - Data <../../reference/modules/spp_api_v2_data>`**: REST API endpoints for Variable Data push/pull.
- **{doc}`OpenSPP API V2 - Vocabulary <../../reference/modules/spp_api_v2_vocabulary>`**: API V2 vocabulary endpoints; auto-activates with `spp_vocabulary`.
- **{doc}`OpenSPP API V2 - Change Request <../../reference/modules/spp_api_v2_change_request>`**: API V2 change request endpoints; auto-activates with `spp_change_request_v2`.
- **{doc}`OpenSPP DCI Client <../../reference/modules/spp_dci_client>`**: Base DCI client infrastructure with OAuth2 and data source management
- **{doc}`OpenSPP DCI Client - CRVS <../../reference/modules/spp_dci_client_crvs>`**: Connect to CRVS registries via DCI API.
- **{doc}`OpenSPP DCI Client - IBR <../../reference/modules/spp_dci_client_ibr>`**: Connect to IBR for duplication checks via DCI API.
- **{doc}`OpenSPP DCI Client - Disability Registry <../../reference/modules/spp_dci_client_dr>`**: Connect to Disability Registry via DCI API.
- **{doc}`OpenSPP DCI Server <../../reference/modules/spp_dci_server>`**: Exposes the Social Registry as a DCI-compliant queryable endpoint.

## Expanding the Social Registry

The OpenSPP-based Social Registry contains everything that is necessary to set up a foundational Social Registry. It can however be expanded with additional functionalities to perfectly suit the specific needs, read more about {doc}`module installation <../get_started/modules/index>`.

## Next step

The OpenSPP Social Registry is an open-source product, built and supported by the OpenSPP community. Read more about {doc}`installing OpenSPP Social Registry <../get_started/modules/social_installation>`.
