---
myst:
  html_meta:
    "title": "Farmer Registry for Agricultural Social Protection"
    "description": "OpenSPP Farmer Registry product configuration bridging agriculture and social protection for rural communities"
    "keywords": "OpenSPP, farmer registry, agricultural programs, rural communities, social protection, smallholder farmers"
---

# OpenSPP Farmer Registry
*A digital platform to manage and strengthen farmer data systems*

The **OpenSPP Farmer Registry** is a modular digital platform designed to be a single, reliable source of truth for agricultural data. It helps governments, organizations, and partners move from guesswork to data-driven decision-making, ensuring that farmers and rural communities receive the right support at the right time.

## Key features

**Farmer and farm registration –** OpenSPP Farmer Registry is specifically designed with agricultural aspects in mind and contains all the common fields - farmers, crops, livestock, land parcels, and farming practices.

*Read more about {doc}`Unified and hierarchical beneficiary registry <features/unified_registry>`.*

**Targeting and integrated service delivery –** Use detailed agricultural and demographic information to design and deliver tailored interventions based on the agricultural information, regardless of if it is simpler criteria or advanced, combined criteria.

*Read more about {doc}`Eligibility and targeting <features/eligibility_targeting>`.*

**Geo-spatial analysis and shock response –** The integration of a Geographic Information System (GIS) allows to combine geographic information with farm data to identify trends, manage risks, and support disaster or climate response.

*Read more about {doc}`Geospatial (GIS) and land management <features/gis_land_management>`.*

**Monitoring and accountability –** Track changes and manage user permissions to ensure data security and integrity. Access dashboards for high-level decision-making, transparency and long term monitoring.

*Read more about {doc}`Auditable change management <features/change_management>` and {doc}`Grievance Redress Mechanism (GRM) <features/grievance_redress>`.*

**Interoperability with other systems –** Connect seamlessly with other national databases (ID, health, civil registry) via secure APIs to make updates or to pull information directly, ensuring that the information is up-to-date.

*Read more about {doc}`Data integration and interoperability (APIs) <features/data_integration_apis>`.*

## Who is it for?

**Governments** implementing national farmer registries

**Agricultural ministries and agencies** designing support programs

**NGOs** working on rural development and food security

## Next step

The OpenSPP Farmer Registry is an open-source product, built and supported by the OpenSPP community. Read more about {doc}`installing OpenSPP Farmer Registry <../get_started/modules/farmer_installation>`.

## OpenSPP modules included in the OpenSPP Farmer Registry

The preconfigured OpenSPP Farmer Registry product is intended to provide the basic use cases of a farmer registry.

The following modules are included in the OpenSPP Farmer Registry product:

- **{doc}`OpenSPP Registry <../../reference/modules/spp_registry>`**: Consolidated registry management for individuals, groups, and membership.
- **{doc}`OpenSPP Registry Search Portal <../../reference/modules/spp_registry_search>`**: Search-first registry interface for privacy protection.
- **{doc}`OpenSPP Security <../../reference/modules/spp_security>`**: Central security definitions for OpenSPP modules.
- **{doc}`OpenSPP User Roles <../../reference/modules/spp_user_roles>`**: Defines and manages distinct user roles for area-based access control.
- **{doc}`OpenSPP Area Management <../../reference/modules/spp_area>`**: Establishes direct associations between OpenSPP registrants, beneficiary groups, and their corresponding geographical administrative areas.
- **{doc}`OpenSPP Vocabulary <../../reference/modules/spp_vocabulary>`**: Standardized code list management system for OpenSPP.
- **{doc}`OpenSPP Farmer Registry <../../reference/modules/spp_farmer_registry>`**: Core farmer and farm registration data model.
- **{doc}`OpenSPP Farmer Registry Vocabularies <../../reference/modules/spp_farmer_registry_vocabularies>`**: Agricultural vocabulary for crops, livestock and farming practices.
- **{doc}`OpenSPP Land Record <../../reference/modules/spp_land_record>`**: Records and manages land parcels linked to farmers.
- **{doc}`OpenSPP Irrigation <../../reference/modules/spp_irrigation>`**: Tracks irrigation infrastructure and water source data.
- **{doc}`OpenSPP GIS <../../reference/modules/spp_gis>`**: Geospatial mapping and geographic analysis for registry data.
- **{doc}`OpenSPP Consent <../../reference/modules/spp_consent>`**: DPV-aligned consent management for social protection programs.
- **{doc}`OpenSPP Source Tracking <../../reference/modules/spp_source_tracking>`**: Track data provenance and source information for registrants.
- **{doc}`OpenSPP Banking / Bank Details <../../reference/modules/spp_banking>`**: Financial account and mobile money details for beneficiaries.
- **{doc}`OpenSPP Custom Fields <../../reference/modules/spp_custom_field>`**: Configurable custom fields for programme-specific registry data.
- **{doc}`OpenSPP Programs <../../reference/modules/spp_programs>`**: Manages cash and in-kind entitlements and programme delivery.
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
- **{doc}`OpenSPP API V2 - Cycles <../../reference/modules/spp_api_v2_cycles>`**: API V2 cycle endpoints; auto-activates with `spp_programs`.
- **{doc}`OpenSPP DCI Client <../../reference/modules/spp_dci_client>`**: Base DCI client infrastructure with OAuth2 and data source management.
- **{doc}`OpenSPP DCI Client - CRVS <../../reference/modules/spp_dci_client_crvs>`**: Connect to CRVS registries via DCI API.
- **{doc}`OpenSPP DCI Client - IBR <../../reference/modules/spp_dci_client_ibr>`**: Connect to IBR for duplication checks via DCI API.
- **{doc}`OpenSPP DCI Client - Disability Registry <../../reference/modules/spp_dci_client_dr>`**: Connect to Disability Registry via DCI API.
- **{doc}`OpenSPP DCI Server <../../reference/modules/spp_dci_server>`**: Exposes the Farmer Registry as a DCI-compliant queryable endpoint.

## Expanding the Farmer Registry

The OpenSPP-based Farmer Registry contains everything that is necessary to set up a foundational Farmer Registry. It can however be expanded with additional functionalities to perfectly suit the specific needs, read more about {doc}`module installation <../get_started/modules/index>`.
