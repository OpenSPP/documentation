---
myst:
  html_meta:
    "title": "Farmer Registry for Agricultural Social Protection"
    "description": "OpenSPP Farmer Registry product configuration bridging agriculture and social protection for rural communities"
    "keywords": "OpenSPP, farmer registry, agricultural programs, rural communities, social protection, smallholder farmers"
---

# OpenSPP Farmer Registry

The OpenSPP based Farmer Registry base module is designed to include all the foundational parts of a modular and integrated digital farmer registry. It can act as a single, auditable source of truth for all agricultural data and shift agricultural support from an era of guesswork to a data-driven approach, fundamentally optimizing policy design and delivery.

## What are the functionalities of OpenSPP Farmer Registry?

**Registration and data collection:** The registry module included in OpenSPP Farmer Registry is specifically designed with agricultural aspects in mind, besides basic demographics it also covers aspects such as crops grown, livestock owned, and farming techniques. It also includes geospatial data, such as land parcel ownership and the visual mapping of farm boundaries, which is a critical component for enabling geographically-based targeting. This comprehensive data collection ensures that the registry contains the necessary information to segment and categorize farmers based on a rich set of criteria.

Read more about {doc}`Unified and hierarchical beneficiary registry <../features/unified_registry>` and {doc}`Key terminology <../concepts/registrant_concepts>`. 

**Targeting and integrated service delivery:** The OpenSPP Farmer Registry provides the intelligence required for strategic and targeted planning and allows the design of interventions based on the agricultural specific information stored in the registry, regardless of if it is simpler criteria or advanced, combined criteria.

Read more about {doc}`Eligibility and targeting <../features/eligibility_targeting>`. 

**Geo-spatial analysis and shock response:** The integration of a Geographic Information System (GIS) elevates the OpenSPP Farmer Registy module to a powerful tool for policy and program management. This technology allows the combination of traditional criteria and geospatial information to correctly pinpoint both causes of identified trends and possible interventions.

Read more about {doc}`Geospatial (GIS) and land management <../features/gis_land_management>`. 

**Monitoring, reporting, and public accountability:** OpenSPP Farmer Registry provides a suite of tools for oversight and public accountability. It tracks all data modifications and user actions, creating a secure and transparent record of every change. It also manages user access and permissions, ensuring data security and integrity. For high-level decision-making, the system provides data analysis tools and dashboards to inform policy and resource allocation as well as conducting impact evaluations to quantify the program's effect. This capability is crucial for proving program effectiveness to donors, stakeholders, and citizens.

Read more about {doc}`Auditable change management <../features/change_management>` and {doc}`Grievance Redress Mechanism (GRM) <../features/grievance_redress>`. 

## OpenSPP modules included in the OpenSPP Farmer Registry

The preconfigured OpenSPP Farmer Registry product is intended to provide the basic use cases of a farmer registry. Note that in addition to the base product you will most likely want to add additional modules in order to match your specific needs.

The following modules are included in the OpenSPP Farmer Registry product:

- **{doc}`OpenSPP Base <../../reference/modules/spp_base>`**: Provides the fundamental core structure for all registrant profiles.
- **{doc}`OpenSPP Base Settings <../../reference/modules/spp_base_setting>`**: Provides essential settings and customizations.
- **{doc}`OpenSPP Custom Fields <../../reference/modules/spp_custom_field>`**: Allows for tailoring data collection to specific local needs.
- **{doc}`OpenSPP Area Management <../../reference/modules/spp_area>`**: Includes additional features for managing and organizing geographical areas within the system
- **{doc}`OpenSPP OpenID VCI Individual <../../reference/modules/spp_openid_vci_individual>`**: Enables the issuance of Verifiable Credentials (VCs) for individual registrants.
- **{doc}`OpenSPP Custom Filter <../../reference/modules/spp_custom_filter>`**: Allows control over fields displayed in filter dropdowns.
- **{doc}`OpenSPP User Roles <../../reference/modules/spp_user_roles>`**: Manages user access and permissions to the registry data, ensuring data security and integrity.
- **{doc}`OpenSPP Area GIS <../../reference/modules/spp_area_gis>`**: Integrates GIS capabilities to enable visualization on maps.
- **{doc}`OpenSPP Base GIS <../../reference/modules/spp_base_gis>`**: Provides Geographical Information System (GIS) capabilities to OpenSPP.
- **{doc}`OpenSPP Farmer Registry Base <../../reference/modules/spp_farmer_registry_base>`**: Base module for managing farmer registries, linking farmers to farms, land, and agricultural activities.
- **{doc}`OpenSPP Farmer Registry Default UI <../../reference/modules/spp_farmer_registry_default_ui>`**: Default UI for Farmer Registry Base.
- **{doc}`OpenSPP Irrigation <../../reference/modules/spp_irrigation>`**: Provides tools for managing and visualizing irrigation infrastructure within OpenSPP, enabling efficient tracking, planning, and analysis of irrigation systems and their impact.
- **{doc}`OpenSPP Land Record <../../reference/modules/spp_land_record>`**: Enables the management and geospatial visualization of land records within OpenSPP.
- **{doc}`OpenSPP Registry Group Hierarchy <../../reference/modules/spp_registry_group_hierarchy>`**: Introduces hierarchical relationships between groups.