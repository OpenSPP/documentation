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

<!--*Read more about {doc}`Unified and hierarchical beneficiary registry <../features/unified_registry>` and {doc}`Key terminology <../concepts/registrant_concepts>`.* -->

**Verifiable Credentials –** Issue unique IDs and documents with QR codes through secure and streamlined processes to attest to program eligibility. 

**Targeting and integrated service delivery –** With a flexible approach to eligibility and targeting, the OpenSPP SP-MIS can serve as a central data repository to support a wide array of programs.

<!--*Read more about {doc}`Eligibility and targeting <../features/eligibility_targeting>`.*-->

**Program and Distribution Management –** A core feature in OpenSPP SP-MIS is its ability to support the delivery of both cash and in-kind entitlements. Automate cash transfers via financial service providers, issue vouchers, or manage food and non-food item distribution, including stock and warehouse management.

<!--*Read more about {doc}`End-to-end program and entitlement management <../features/program_management>`, {doc}`Pluggable payment and disbursement <../features/payment_disbursement>` and {doc}`In-kind benefits and inventory management (GRM) <../features/in_kind_benefits>`.*-->

**Monitoring, reporting, and public accountability –** Maintain full audit trails, track all user actions, and provide dashboards and analytics for evidence-based decision-making. This capability is crucial for tracking program performance, demonstrating effectiveness to donors, and building public trust.

<!--*Read more about {doc}`Auditable change management <../features/change_management>` and {doc}`Grievance Redress Mechanism (GRM) <../features/grievance_redress>`.*-->

**Interoperability with other systems –** Connect securely with other national databases (e.g., ID, health, civil registration) through RESTful APIs to pull information directly, ensuring that the information is up-to-date.

<!--*Read more about {doc}`Data integration and interoperability (APIs) <../features/data_integration_apis>`.*-->

**Geo-spatial analysis and shock response –** Integrate GIS and external data (e.g., flood maps) with already known information to rapidly identify and assist affected households during crises without the need for time-consuming, emergency-specific registration and needs assessments.

<!--*Read more about {doc}`Geospatial (GIS) and land management <../features/gis_land_management>`.*-->

## Who is it for?

**Governments** managing national or local social protection systems

**Social protection agencies** delivering cash or in-kind programs

**NGOs and development partners** supporting vulnerable households

## Next Step

The OpenSPP SP-MIS is an open-source product, built and supported by the OpenSPP community. Read more about {doc}`installing OpenSPP SP-MIS <../get_started/modules/spmis_installation>`.
<!--
## OpenSPP modules included in the OpenSPP SP-MIS:

The preconfigured OpenSPP SP-MIS product is intended to provide the basic use cases of an SP-MIS.

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
-->
## Expanding the SPMIS

The OpenSPP-based SPMIS contains everything that is necessary to set up a foundational SPMIS. It can however be expanded with additional functionalities to perfectly suit the specific needs, read more about {doc}`module installation <../get_started/modules/index>`.
