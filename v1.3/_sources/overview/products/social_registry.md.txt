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

*Read more about {doc}`Unified and hierarchical beneficiary registry <../features/unified_registry>` and {doc}`Key terminology <../concepts/registrant_concepts>`.* 

**Targeting and integrated service delivery –** Flexible approach to eligibility and targeting - identify eligible beneficiaries based on simple criteria such as age or complex combinations of factors.

*Read more about {doc}`Eligibility and targeting <../features/eligibility_targeting>`.* 

**Monitoring and accountability –** Track changes and manage user permissions to ensure data security and integrity. Access dashboards for decision-making, transparency and long term monitoring.

*Read more about {doc}`Auditable change management <../features/change_management>` and {doc}`Grievance Redress Mechanism (GRM) <../features/grievance_redress>`.* 

**Interoperability with other systems –** Connect seamlessly with other national databases (ID, health, civil registry) via secure APIs to make updates or to pull information directly, ensuring that the information is up-to-date.

*Read more about {doc}`Data integration and interoperability (APIs) <../features/data_integration_apis>`.* 

## Who is it for?

**Government agencies** wanting to have a reliable up to date registry that can act as foundation for interventions

**NGOs** delivering services at national or local level

**Policy makers** needing reliable data for planning and resource allocation

## Next Step

The OpenSPP Social Registry is an open-source product, built and supported by the OpenSPP community. Read more about {doc}`installing OpenSPP Social Registry <../../getting_started/social_installation>`.

## OpenSPP modules included in the OpenSPP Social Registry

The preconfigured OpenSPP Social Registry product is intended to provide support for the fundamental use cases of a social registry.

The following modules are included in the OpenSPP Social Registry product:

- **{doc}`OpenSPP Base <../../reference/modules/spp_base>`**: Provides the fundamental core structure for all registrant profiles.
- **{doc}`OpenSPP Base Settings <../../reference/modules/spp_base_setting>`**: Provides essential settings and customizations.
- **{doc}`OpenSPP Custom Fields <../../reference/modules/spp_custom_field>`**: Allows for tailoring data collection to specific local needs.
- **{doc}`OpenSPP Area Management <../../reference/modules/spp_area>`**: Includes additional features for managing and organizing geographical areas within the system
- **{doc}`OpenSPP OpenID VCI Individual <../../reference/modules/spp_openid_vci_individual>`**: Enables the issuance of Verifiable Credentials (VCs) for individual registrants.
- **{doc}`OpenSPP Custom Filter <../../reference/modules/spp_custom_filter>`**: Allows control over fields displayed in filter dropdowns.
- **{doc}`OpenSPP User Roles <../../reference/modules/spp_user_roles>`**: Manages user access and permissions to the registry data, ensuring data security and integrity.

## Expanding the Social Registry

The OpenSPP-based Social Registry contains everything that is necessary to set up a foundational Social Registry. It can however be expanded with additional functionalities to perfectly suit the specific needs, read more about {doc}`module installation <../../getting_started/module_installation>`.
