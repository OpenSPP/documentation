---
orphan: true
---

# OpenSPP Modules Index

```{warning}

**Work in Progress**: This document is actively being developed and updated. Content may be incomplete or subject to change.
```

## SPP Modules

| Module | Summary |
| ------ | ------- |
| [OpenSPP Base API](spp_base_api) | Provides foundational API functions and methods for seamless interaction with the OpenSPP system, enabling data exchange via APIs or XML-RPC. |
| [OpenSPP Programs](spp_programs) | Manage cash and in-kind entitlements, integrate with inventory, and enhance program management features for comprehensive social protection and agricultural support. |
| [OpenSPP User Roles](spp_user_roles) | Enhances user role management with local roles and area-based access control for improved data security and granularity in OpenSPP. |
| [OpenSPP DCI API Server](spp_dci_api_server) | Provides a DCI-compliant RESTful API for secure data exchange with OpenSPP's registry. |
| [OpenSPP In-Kind Entitlement](spp_entitlement_in_kind) | Manages the distribution of in-kind entitlements within social protection programs, handling inventory, service points, and beneficiary redemption. |
| [OpenSPP Encryption Module](spp_encryption) | Provides secure encryption, decryption, signing, and verification of data within OpenSPP using JWCrypto. |
| [OpenSPP Data Source](spp_registry_data_source) | Provides a framework for integrating external data sources into OpenSPP, enabling connection to and retrieval of data from external systems like farmer registries and social protection programs. |
| [OpenSPP Farmer Registry Demo](spp_farmer_registry_demo) | Provides pre-populated demo data for the OpenSPP Farmer Registry, showcasing its features with realistic sample data. |
| [OpenSPP Registrant Import](spp_registrant_import) | Streamlines the import of registrant data into OpenSPP, simplifies data mapping, and automates unique ID generation. |
| [OpenSPP Data Export](spp_data_export) | Enables exporting large datasets to Excel by overriding the default export functionality and providing error handling for exceeding Excel row limits. |
| [OpenSPP Audit Config](spp_audit_config) | This module allows administrators to define and manage audit rules to track and log changes made to critical data within the OpenSPP platform, ensuring data security and integrity. |
| [OpenSPP SQL Query Eligibility Manager](spp_eligibility_sql) | Define complex program eligibility criteria using SQL queries for flexible and automated beneficiary enrollment within OpenSPP. |
| [OpenSPP Custom Fields UI](spp_custom_fields_ui) | Provides a user-friendly interface for defining and managing custom fields for registrants within the OpenSPP platform, allowing implementers to tailor data collection to program-specific needs. |
| [OpenSPP Service Point Device](spp_service_point_device) | This module allows managing terminal devices associated with each service point, tracking their model, Android version, and active status. |
| [SPP Audit Log](spp_audit_log) | Provides audit logging functionality to track data changes and user actions within OpenSPP, enhancing transparency and accountability. |
| [OpenSPP API Records](spp_api_records) | Provides RESTful API endpoints for accessing and managing OpenSPP's core data, including service points, programs, products, and entitlements. |
| [OpenSPP Programs: Compliance Criteria](spp_programs_compliance_criteria) | Manages compliance criteria within social protection programs, allowing administrators to define and enforce additional eligibility requirements beyond initial program criteria. |
| [OpenSPP Proxy Means Testing](spp_pmt) | Calculates a Proxy Means Testing (PMT) score for groups of registrants to aid in beneficiary identification and prioritization for social protection programs. |
| [OpenSPP Import Match](spp_import_match) | Enhances data imports in OpenSPP by enabling the matching of imported records with existing data to prevent duplicates and ensure data integrity. |
| [OpenSPP Base GIS](spp_base_gis) | Provides Geographical Information System (GIS) capabilities to OpenSPP, enabling visualization and interaction with geospatial data on maps, integrating with modules like Registries and Targeting & Eligibility for enhanced program management. |
| [OpenSPP Base GIS Demo](spp_base_gis_demo) | Demonstrates the GIS capabilities of the OpenSPP Base GIS module by providing practical examples and use cases with GIS views, data layers, and raster layers. |
| [OpenSPP OpenID VCI](spp_openid_vci) | Enables the issuance and management of Verifiable Credentials (VCs) within the OpenSPP platform, leveraging OpenID Connect for Verifiable Presentations (OpenID4VP) to provide secure and verifiable digital credentials for registrants. |
| [OpenSPP Event Data](spp_event_data) | Records and tracks events related to individual and group registrants, providing a chronological history of changes and actions within the OpenSPP system. |
| [OpenSPP Service Points Management](spp_service_points) | This module enables the management of service points, linking them to geographical areas, company entities, and user accounts for streamlined service delivery within OpenSPP. |
| [OpenSPP Import: DCI API](spp_import_dci_api) | Enables integration with external registries, particularly those adhering to the DCI (Digital Civil Identity) standard, for importing and synchronizing registrant data into OpenSPP. |
| [OpenSPP Base Settings](spp_base_setting) | Provides essential settings and customizations for OpenSPP implementations, including Country Office management and user interface adaptations. |
| [OpenSPP Change Request: Add Farmer](spp_change_request_add_farmer) | Provides a specialized workflow for adding new farmers to existing groups in the registry. |
| [OpenSPP Base Demo](spp_base_demo) | Provides demonstration data for the OpenSPP system, including sample registrants, programs, and products to facilitate user exploration and training. |
| [OpenSPP API: Oauth](spp_oauth) | Provides OAuth 2.0 authentication for secure access to the OpenSPP API. |
| [OpenSPP Land Record](spp_land_record) | This module enables the management and geospatial visualization of land records within OpenSPP, linking land parcels to farms, tracking ownership, and supporting land governance initiatives. |
| [OpenSPP Base](spp_base) | Provides essential configurations, UI customizations, and base functionalities for the OpenSPP system, including top-up card management and integration with other OpenSPP modules for areas, service points, programs, and custom fields. |
| [OpenSPP Manual Entitlement](spp_manual_entitlement) | Provides a mechanism for manually creating entitlements for beneficiaries within specific program cycles in OpenSPP, offering flexibility for programs with unique eligibility criteria or situations not covered by automated rules. |
| [OpenSPP Entitlement Basket](spp_entitlement_basket) | This module allows you to define baskets of goods and services that beneficiaries are entitled to receive, simplifying in-kind entitlement management within social protection programs. |
| [OpenSPP Demo](spp_demo) | Provides demonstration data and functionalities for the OpenSPP system, showcasing its capabilities in managing social protection programs and registries with pre-populated data for exploration and testing. |
| [OpenSPP Registry Group Hierarchy](spp_registry_group_hierarchy) | Introduces hierarchical relationships between groups, allowing for nested group structures within social protection programs and farmer registries. |
| [OpenSPP Event Demo](spp_event_demo) | Provides demonstration data and functionalities for the OpenSPP event tracking system, showcasing practical applications through predefined event types, data models, views, and wizards. |
| [OpenSPP API](spp_api) | Provides a framework for building and managing a RESTful API for the OpenSPP platform, including API definition, documentation, security, and logging. |
| [OpenSPP Farmer Registry Dashboard](spp_farmer_registry_dashboard) | Provides interactive dashboards and reports for visualizing data from the OpenSPP Farmer Registry, offering insights into key metrics and trends related to registered farmers. |
| [OpenSPP Registrant Tags](spp_registrant_tag) | Provides enhanced tagging capabilities for registrants in OpenSPP, allowing for better organization and management of registrant data. |
| [OpenSPP Custom Field Recompute Daily](spp_custom_field_recompute_daily) | Enables daily recomputation of specified fields to maintain data accuracy and improve performance by offloading intensive calculations. |
| [OpenSPP OpenID VCI Individual](spp_openid_vci_individual) | Enables the issuance of Verifiable Credentials (VCs) for individual registrants within the OpenSPP platform, integrating with OpenID Connect for Verifiable Presentations and Decentralized Identifiers. |
| [OpenSPP Auto-Update Entitlements](spp_auto_update_entitlements) | Automatically updates entitlement states based on their redemption status at the end of program cycles in OpenSPP. |
| [OpenSPP POS](spp_pos) | Extend Odoo POS to redeem entitlements from OpenSPP for secure and efficient beneficiary transactions. |
| [OpenSPP Change Request](spp_change_request) | Streamlines the process of handling changes to registrant information within the OpenSPP system, providing a structured framework for submitting, reviewing, approving, and applying modifications. |
| [OpenSPP Program Entitlement Basic Cash Spent](spp_basic_cash_entitlement_spent) | Tracks cash spending by beneficiaries against allocated entitlements in basic cash programs, calculating remaining balances and supporting program monitoring. |
| [OpenSPP Event Data Program Membership](spp_event_data_program_membership) | This module allows users to record and track program membership-related events, such as enrollment, suspension, or exit, and link them to specific program membership records within OpenSPP. |
| [OpenSPP ID Queue](spp_idqueue) | Manages ID card requests, approvals, batch printing, and distribution for registrants within social protection programs and farmer registries. |
| [OpenSPP: Starter](spp_starter) | No summary provided |
| [OpenSPP Area Management](spp_area) | This module enables management of geographical areas, linking them to registrants for targeted interventions and analysis in social protection programs. |
| [OpenSPP Programs: Service Points Integration](spp_programs_sp) | Extends OpenSPP Programs to integrate service points, enabling the association of beneficiaries and entitlements with designated service delivery locations for improved program efficiency and targeted benefit distribution. |
| [OpenSPP Base GIS REST](spp_base_gis_rest) | Provides RESTful API endpoints for accessing and querying geospatial data within OpenSPP, secured with OAuth 2.0. |
| [OpenSPP Consent](spp_consent) | No summary provided |
| [OpenSPP Custom Filter UI](spp_custom_filter_ui) | Customizes the OpenSPP UI to enhance filtering for Res Partners, improving usability and efficiency in managing registrants within social protection programs. |
| [OpenSPP Change Request Demo: Add Child/Member](spp_change_request_add_children_demo) | Provides a demonstration of adding children or members to an existing group in the registry using the OpenSPP Change Request framework, including a dedicated form, ID scanning integration, and automated data updates. |
| [OpenSPP Registry: Scan ID Document](spp_scan_id_document) | Enables the scanning of physical ID documents directly into a registrant's profile, streamlining data entry and improving accuracy in the OpenSPP Registry. |
| [OpenSPP Program ID](spp_program_id) | Generates and manages unique IDs for social protection programs, enhancing identification and integration within the OpenSPP platform. |
| [OpenSPP OpenID VCI Group](spp_openid_vci_group) | Enables the issuance of Verifiable Credentials (VCs) for groups of registrants, integrating with group management to represent group identity and attributes. |
| [OpenSPP Registry: Audit Post](spp_audit_post) | Enables posting of audit log messages to related parent records, providing a centralized view of changes across interconnected data in social protection programs. |
| [OpenSPP Exclusion Filter](spp_exclusion_filter) | This module enhances the OpenSPP program creation process by enabling the configuration and application of exclusion filters, ensuring that only eligible registrants are considered for enrollment in new programs. |
| [OpenSPP Farmer Registry Base](spp_farmer_registry_base) | Base module for managing farmer registries, linking farmers to farms, land, and agricultural activities. |
| [OpenSPP Irrigation](spp_irrigation) | Provides tools for managing and visualizing irrigation infrastructure within OpenSPP, enabling efficient tracking, planning, and analysis of irrigation systems and their impact. |
| [OpenSPP Custom Fields](spp_custom_field) | Adds customizable fields to registrant profiles for enhanced data collection and program management in OpenSPP. |
| [OpenSPP Custom Filter](spp_custom_filter) | Enhances Odoo's filtering system by allowing administrators to control which fields are displayed in filter dropdowns, improving user experience and data management. |
| [ID PASS](spp_idpass) | No summary provided |
| [OpenSPP Area GIS](spp_area_gis) | Integrates GIS capabilities into OpenSPP's Area management, enabling visualization on maps, associating coordinates, defining polygons, and facilitating spatial analysis for improved targeting and monitoring of social protection programs. |
| [OpenSPP Custom Field Custom Filter Integration](spp_custom_field_custom_filter) | Allows administrators to enable custom fields for filtering, enhancing data analysis and program operations. |
| [OpenSPP Document Management System](spp_dms) | Provides a centralized system for managing and organizing documents within OpenSPP, facilitating efficient storage, retrieval, and categorization of files related to social protection programs. |
| [OpenSPP Tag Based Eligibility Manager](spp_eligibility_tags) | Define eligibility criteria for programs based on registrant tags and geographical areas, automating beneficiary identification and improving targeting accuracy. |
| [OpenSPP Entitlement Transactions](spp_ent_trans) | This module records and manages transactions related to entitlement redemptions, providing a transparent history for both cash and in-kind benefits. |
| [OpenSPP Cash Entitlement](spp_entitlement_cash) | Manage cash-based entitlements for beneficiaries within social protection programs, including defining calculation rules, automating disbursement, and tracking payments. |

```{toctree}
:maxdepth: 1
:hidden:

spp_api
spp_api_records
spp_area
spp_area_gis
spp_audit_config
spp_audit_log
spp_audit_post
spp_auto_update_entitlements
spp_base
spp_base_api
spp_base_demo
spp_base_gis
spp_base_gis_demo
spp_base_gis_rest
spp_base_setting
spp_basic_cash_entitlement_spent
spp_change_request
spp_change_request_add_children_demo
spp_change_request_add_farmer
spp_consent
spp_custom_field
spp_custom_field_custom_filter
spp_custom_field_recompute_daily
spp_custom_fields_ui
spp_custom_filter
spp_custom_filter_ui
spp_data_export
spp_dci_api_server
spp_demo
spp_dms
spp_eligibility_sql
spp_eligibility_tags
spp_encryption
spp_ent_trans
spp_entitlement_basket
spp_entitlement_cash
spp_entitlement_in_kind
spp_event_data
spp_event_data_program_membership
spp_event_demo
spp_exclusion_filter
spp_farmer_registry_base
spp_farmer_registry_dashboard
spp_farmer_registry_demo
spp_idpass
spp_idqueue
spp_import_dci_api
spp_import_match
spp_irrigation
spp_land_record
spp_manual_entitlement
spp_oauth
spp_openid_vci
spp_openid_vci_group
spp_openid_vci_individual
spp_pmt
spp_pos
spp_program_id
spp_programs
spp_programs_compliance_criteria
spp_programs_sp
spp_registrant_import
spp_registrant_tag
spp_registry_data_source
spp_registry_group_hierarchy
spp_scan_id_document
spp_service_point_device
spp_service_points
spp_starter
spp_user_roles
```
