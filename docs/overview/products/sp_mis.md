---
myst:
  html_meta:
    "title": "Social Protection Management Information System (SP-MIS)"
    "description": "OpenSPP SP-MIS product configuration for comprehensive social protection program management from enrollment to payment"
    "keywords": "OpenSPP, SP-MIS, social protection, management information system, beneficiary management, payments"
---
# OpenSPP SP-MIS (Social Protection Management Information System)

The OpenSPP SP-MIS base module is a comprehensive platform designed to manage the entire lifecycle of a social protection program. The solution can support the delivery of both routine and emergency interventions, as both cash and in-kind. The system can also leverage documents and verifiable credentials to enhance security, reduce fraud, and empower beneficiaries by granting them control over their personal data.

## What are the functionalities of OpenSPP SP-MIS?

**Registration and data collection:** A well-functioning SP-MIS is built upon a dynamic, continuous database that acts as a "single, up-to-date source of truth" for all related information. The OpenSPP SP-MIS allows for various ways of ingesting data depending on the specific use case. It is possible to perform imports of data, link the SP-MIS to other systems or perform a fresh registration, either to ingest all data or to update existing data. The registry can also be created on a per need basis, adding registrants when they apply for or are deemed eligible for the support. As circumstances change, citizens can submit requests to update their information through a structured workflow, ensuring the data remains current and reliable.

Read more about {doc}`Unified and hierarchical beneficiary registry <../features/unified_registry>` and {doc}`Key terminology <../concepts/registrant_concepts>`. 

**Verifiable Credentials:** To enhance security, streamline processes, and foster trust, the OpenSPP SP-MIS is supported by a modern, standards-based ecosystem of verifiable credentials. It allows for creating and managing ID types, assigning unique IDs to individuals or groups, and generating printable documents embedded with scannable QR codes that can cryptographically attest to program eligibility.The platform is also built to work with other digital public goods, creating a seamless and secure chain of trust. 

**Targeting and integrated service delivery:** The OpenSPP SP-MIS can serve as a central data repository to support a wide array of programs. It provides a flexible approach to eligibility and targeting allowing a government to automatically identify citizens who meet either simple criteria, such as age or other single features, or more complex, intersecting criteria. This functionality ensures that the registry can prevent duplication and allow for a coordinated, integrated approach.

Read more about {doc}`Eligibility and targeting <../features/eligibility_targeting>`. 

**Program and Distribution Management:** A core feature in OpenSPP SP-MIS is its ability to support the delivery of both cash and in-kind entitlements. The platform can automate cash transfers by integrating with Financial Service Providers, creating payment lists, or issuing vouchers. These payments can be delivered through various channels, including mobile money or e-wallets. For in-kind transfers, the system supports the entire supply chain, including the management and distribution of both food and non-food items. The platform can handle stock management and warehouse management, or it can be linked to other Enterprise Resource Planning (ERP) systems to coordinate the delivery of goods.

Read more about {doc}`End-to-end program and entitlement management <../features/program_management>`, {doc}`Pluggable payment and disbursement <../features/payment_disbursement>` and {doc}`In-kind benefits and inventory management (GRM) <../features/in_kind_benefits>`. 

**Monitoring, reporting, and public accountability:** A modern SP-MIS must be transparent and accountable to build citizen trust. OpenSPP SP-MIS provides a suite of tools for oversight and accountability, with a secure audit log that tracks all data modifications and user actions. For high-level decision-making, the system provides customizable dashboards and data analysis tools that can provide meaningful, actionable insights . This capability is crucial for tracking program performance, demonstrating effectiveness to donors, and building public trust.

Read more about {doc}`Auditable change management <../features/change_management>` and {doc}`Grievance Redress Mechanism (GRM) <../features/grievance_redress>`. 

**Interoperability with other systems:** The OpenSPP platform, including the OpenSPP SP-MIS, uses a well-documented RESTful API that enables the registry to share and receive information securely with other national databases, such as those for National IDs, health, and civil registration. This allows the government to pull information directly, ensuring that the information is up-to-date.

Read more about {doc}`Data integration and interoperability (APIs) <../features/data_integration_apis>`. 

**Geo-spatial analysis and shock response:** The integration of a Geographic Information System (GIS) allows OpenSPP SP-MIS to expand with geospatial data. This means that the information on registrants can be fused with real-time, external data sources such as flood or wildfire maps. In the case of an emergency, this allows the system to quickly generate a precise list of affected individuals who are already registered and verified, enabling a swift and targeted response without the need for time-consuming, emergency-specific registration and needs assessments.

Read more about {doc}`Geospatial (GIS) and land management <../features/gis_land_management>`. 

## OpenSPP modules included in the OpenSPP SP-MIS:

The preconfigured OpenSPP SP-MIS product is intended to provide the basic use cases of an SP-MIS. Note that in addition to the base product you will most likely want to add additional modules in order to match your specific needs.

The following modules are included in the OpenSPP SP-MIS product:

- **{doc}`OpenSPP Base <../../reference/modules/spp_base>`**: Provides the fundamental core structure for all registrant profiles.
- **{doc}`OpenSPP Base Settings <../../reference/modules/spp_base_setting>`**: Provides essential settings and customizations.
- **{doc}`OpenSPP Custom Fields <../../reference/modules/spp_custom_field>`**: Allows for tailoring data collection to specific local needs.
- **{doc}`OpenSPP Area Management <../../reference/modules/spp_area>`**: Includes additional features for managing and organizing geographical areas within the system
- **{doc}`OpenSPP OpenID VCI Individual <../../reference/modules/spp_openid_vci_individual>`**: Enables the issuance of Verifiable Credentials (VCs) for individual registrants.
- **{doc}`OpenSPP Custom Filter <../../reference/modules/spp_custom_filter>`**: Allows control over fields displayed in filter dropdowns.
- **{doc}`OpenSPP User Roles <../../reference/modules/spp_user_roles>`**: Manages user access and permissions to the registry data, ensuring data security and integrity.
- **{doc}`OpenSPP Programs <../../reference/modules/spp_programs>`**: Manage cash and in-kind entitlements, integrate with inventory, and enhance program management features.
- **{doc}`OpenSPP Program ID <../../reference/modules/spp_program_id>`**: Generates and manages unique IDs for social protection programs.
- **{doc}`OpenSPP Cash Entitlement <../../reference/modules/spp_entitlement_cash>`**: Manage cash-based entitlements for beneficiaries within social protection programs, including defining calculation rules, automating disbursement, and tracking payments.
- **{doc}`OpenSPP In-Kind Entitlement <../../reference/modules/spp_entitlement_in_kind>`**: Manages the distribution of in-kind entitlements within social protection programs, handling inventory, service points, and beneficiary redemption.
- **{doc}`OpenSPP Entitlement Transactions <../../reference/modules/spp_ent_trans>`**: Records and manages transactions related to entitlement redemptions.
