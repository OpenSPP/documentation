---
myst:
  html_meta:
    "title": "Social Registry 2 for Social Protection Programs"
    "description": "OpenSPP Social Registry product configuration for centralized beneficiary identification, registration, and needs assessment"
    "keywords": "OpenSPP, social registry, beneficiary identification, targeting, social protection, needs assessment"
---

# OpenSPP Social Registry

The OpenSPP-based Social Registry base module contains everything that is necessary to setup a foundational Social Registry. It provides all the needed building blocks but can also be expanded with additional modules to perfectly suit the specific needs.

## What are the functionalities of OpenSPP Social Registry?

**Registration and data collection:** Designing a registry that matches the specific use case is foundational to make sure that the Social Registry can fullfill its purpos. OpenSPP makes it easy to ensure that the relevant fields are present and easily accessible, either through the use of custom fields or by modifying the module to perfectly match your use case. OpenSPP Social Registry allows for ingesting data through either bulk import, registration through the UI or interoperability with other systems (see below).

Read more about {doc}`Unified and hierarchical beneficiary registry <../features/unified_registry>` and {doc}`Key terminology <../concepts/registrant_concepts>`. 

**Targeting and integrated service delivery:** The OpenSPP Social Registry can serve as a central data repository to support a wide array of programs. It provides a flexible approach to eligibility and targeting allowing a government to automatically identify citizens who meet either simple criteria, such as age or other single features, or more complex, intersecting criteria. This functionality ensures that the registry can prevent duplication and allow for a coordinated, integrated approach.

Read more about {doc}`Eligibility and targeting <../features/eligibility_targeting>`. 

**Monitoring, reporting, and public accountability:** OpenSPP Social Registry provides a suite of tools for oversight and public accountability. It tracks all data modifications and user actions, creating a secure and transparent record of every change. It also manages user access and permissions, ensuring data security and integrity. For high-level decision-making, the system provides data analysis tools and dashboards to inform policy and resource allocation.

Read more about {doc}`Auditable change management <../features/change_management>` and {doc}`Grievance Redress Mechanism (GRM) <../features/grievance_redress>`. 

**Interoperability with other systems:** The OpenSPP platform, including the OpenSPP Social Registry, uses a well-documented RESTful API that enables the registry to share and receive information securely with other national databases, such as those for National IDs, health, and civil registration. This allows the government to pull information directly, ensuring that the information is up-to-date.

Read more about {doc}`Data integration and interoperability (APIs) <../features/data_integration_apis>`. 

## OpenSPP modules included in the OpenSPP Social Registry

The preconfigured OpenSPP Social Registry product is intended to provide the basic use cases of a social registry. Note that in addition to the base product you will most likely want to add additional modules in order to match your specific needs.

The following modules are included in the OpenSPP Social Registry product:

- **{doc}`OpenSPP Base <../../reference/modules/spp_base>`**: Provides the fundamental core structure for all registrant profiles.
- **{doc}`OpenSPP Base Settings <../../reference/modules/spp_base_setting>`**: Provides essential settings and customizations.
- **{doc}`OpenSPP Custom Fields <../../reference/modules/spp_custom_field>`**: Allows for tailoring data collection to specific local needs.
- **{doc}`OpenSPP Area Management <../../reference/modules/spp_area>`**: Includes additional features for managing and organizing geographical areas within the system
- **{doc}`OpenSPP OpenID VCI Individual <../../reference/modules/spp_openid_vci_individual>`**: Enables the issuance of Verifiable Credentials (VCs) for individual registrants.
- **{doc}`OpenSPP Custom Filter <../../reference/modules/spp_custom_filter>`**: Allows control over fields displayed in filter dropdowns.
- **{doc}`OpenSPP User Roles <../../reference/modules/spp_user_roles>`**: Manages user access and permissions to the registry data, ensuring data security and integrity.
