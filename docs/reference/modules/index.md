---
review-status: needs-review
review-date: 2025-06-04
reviewer: migration-script
migration-notes: "Added during 2025 documentation reorganization"
---

# OpenSPP Modules Index

```{warning}

**Work in Progress**: This document is actively being developed and updated. Content may be incomplete or subject to change.
```

## SPP Modules

| Module | Summary |
| ------ | ------- |
| [OpenSPP API](spp_api) | Establishes a RESTful API framework for OpenSPP, allowing external systems to securely read, create, update, and delete platform data. Customizable API endpoints, robust authentication, comprehensive logging, and flexible data field mapping enhance integration and auditing capabilities. |
| [OpenSPP API Records](spp_api_records) | It exposes RESTful API endpoints, enabling external systems to programmatically access and manage OpenSPP's core operational data. These endpoints facilitate querying, creating, updating, and deleting records for entities like service points, social protection programs, product definitions, and beneficiary entitlements. |
| [OpenSPP Area Management](spp_area) | Establishes direct associations between OpenSPP registrants, beneficiary groups, and their corresponding geographical administrative areas. It validates registrant-area linkages against official area types, ensuring data integrity and enabling targeted program delivery and analysis. |
| [OpenSPP Area GIS](spp_area_gis) | Integrates GIS capabilities into OpenSPP's Area management, enabling visualization on maps, associating coordinates, defining polygons, and facilitating spatial analysis for improved targeting and monitoring of social protection programs. |
| [OpenSPP Audit Config](spp_audit_config) | Administrators define and manage comprehensive audit rules within this module, specifying which data models, fields, and operations require tracking across the OpenSPP platform. The module ensures data integrity and accountability by logging user and timestamp details, and it enables cross-record auditing through parent-child relationships for consolidated change views. |
| [SPP Audit Log](spp_audit_log) | Comprehensively tracks all data modifications and user actions across the OpenSPP platform, recording old and new values for configured data. It enhances accountability and data integrity by maintaining an immutable history of changes, crucial for internal audits, compliance, and detecting unauthorized alterations. |
| [G2P Registry: Audit Post](spp_audit_post) | OpenSPP Audit Post extends core audit logging by automatically posting audit log messages to related parent records. It consolidates changes from child records onto the parent's communication timeline, leveraging the mail module for message posting. |
| [OpenSPP Auto-Update Entitlements](spp_auto_update_entitlements) | Automatically reviews and updates the state of entitlements based on their redemption status at the end of each program cycle. It assigns precise states, including a new 'Partially Redeemed' status, to ensure accurate records for program closure, reporting, and auditing. |
| [OpenSPP Base](spp_base) | Establishes core system settings and generates unique identifiers for records, enhancing registrant profiles with attributes like tags, gender, and type. The module also integrates Top-up Cards for identification and provides fundamental user interface elements with initial security configurations for user roles. |
| [OpenSPP Base API](spp_base_api) | Provides foundational API functions and methods for robust data exchange between OpenSPP and external systems or internal modules. It enables efficient record management, complex data retrieval, and external system integration primarily through APIs and XML-RPC protocols. |
| [OpenSPP Base Demo](spp_base_demo) | The OpenSPP Base Demo module populates the system with essential sample data, enabling immediate exploration and understanding of core functionalities. It includes diverse sample registrants, social protection programs, and products, providing foundational demo data while conforming to the g2p_registry_individual module's data models. |
| [OpenSPP Base GIS](spp_base_gis) | This module stores and organizes geospatial data, including points, lines, and polygons, for visualization on interactive maps. It enables spatial querying, custom map layer configuration, and integrates location awareness across OpenSPP modules for targeted program management. |
| [OpenSPP Base GIS Demo](spp_base_gis_demo) | Demonstrates the integration of Geographical Information System (GIS) capabilities within OpenSPP, illustrating how to extend data models with various geographical field types. It provides examples for defining custom geospatial data models and visualizing diverse geographical entities, including points, lines, and polygons, on interactive maps. |
| [OpenSPP Base GIS REST](spp_base_gis_rest) | The module provides RESTful API endpoints for secure, programmatic access to OpenSPP's Geographical Information System data, leveraging OAuth 2. 0 and Basic authentication. |
| [OpenSPP Base Settings](spp_base_setting) | OpenSPP Base Setting provides fundamental configurations for country implementations, establishing core organizational structures such as Country Offices. It also enables tailored user interface adaptations and streamlines user management by linking individuals to specific Country Offices for context-aware data access. |
| [OpenSPP Program Entitlement Basic Cash Spent](spp_basic_cash_entitlement_spent) | Records beneficiary expenditures against allocated cash entitlements within social protection programs to monitor utilization. It automatically calculates remaining balances and extends the g2p. |
| [OpenSPP Change Request](spp_change_request) | The OpenSPP Change Request module streamlines the modification of registrant information through a structured, auditable framework. Configurable multi-stage validation workflows ensure proper review and approval, while a comprehensive audit trail records all actions before systematically applying approved changes to registrant records. |
| [OpenSPP Change Request Demo: Add Child/Member](spp_change_request_add_children_demo) | The module formalizes the process of adding new individuals to existing groups within the OpenSPP registry via a dedicated Change Request framework. It integrates ID scanning for rapid data entry, automates new registrant profile creation and group membership updates, and stores supporting documents in the DMS. |
| [OpenSPP Change Request: Add Farmer](spp_change_request_add_farmer) | Provides a specialized workflow for adding new farmers to existing groups in the registry. |
| [OpenSPP Consent](spp_consent) | This module establishes a comprehensive system for managing and tracking explicit consent from individuals and groups within social protection programs. It records specific consent agreements linked to registrants, tracks consent validity with expiry dates, and enables configuration of diverse consent types. |
| [OpenSPP Custom Fields](spp_custom_field) | The module enables administrators to define and add custom data fields directly to registrant profiles, tailoring data collection for specific social protection programs. It supports field differentiation by registrant type, integrates new data points into records, and provides dedicated sections for read-only program indicators. |
| [OpenSPP Custom Field Custom Filter Integration](spp_custom_field_custom_filter) | OpenSPP's filtering system gains custom-defined data field integration, allowing administrators to use program-specific criteria for record segmentation. This enables the construction of highly specific queries, enhancing data analysis and streamlining operational processes for targeted interventions. |
| [OpenSPP Custom Field Recompute Daily](spp_custom_field_recompute_daily) | The OpenSPP Custom Field Recompute Daily module automates the daily recalculation of designated computed fields, ensuring data accuracy and currency. It optimizes system performance by processing large datasets asynchronously in configurable batches, leveraging the Queue Job module. |
| [OpenSPP Custom Fields UI](spp_custom_fields_ui) | The OpenSPP Custom Fields UI module provides a user interface for program implementers to define and manage custom data fields for registrants. It extends registrant profiles by associating custom data with individuals or groups, supporting program-specific indicators and calculated data points within the OpenSPP platform. |
| [OpenSPP Custom Filter](spp_custom_filter) | The module empowers administrators to precisely control which fields appear in Odoo's filtering interface. This capability streamlines data searches, reduces UI clutter, and enhances the user experience by ensuring only relevant fields are available for filtering. |
| [OpenSPP Custom Filter UI](spp_custom_filter_ui) | The module customizes the OpenSPP user interface to enable advanced filtering of res. partner records. |
| [OpenSPP Data Export](spp_data_export) | The spp_data_export module enhances OpenSPP's capability to extract large volumes of program data to Excel, overcoming standard export tool limitations regarding file size and row capacity. It proactively manages Excel's maximum row capacity and overrides default export functionality to ensure complete and reliable data for external analysis. |
| [OpenSPP DCI API Server](spp_dci_api_server) | Exposes OpenSPP's individual and household registry data via a DCI-compliant RESTful API. Secures data exchange through client credential management and token-based authentication for external systems. |
| [OpenSPP Demo](spp_demo) | The spp_demo module populates the OpenSPP system with sample data, creating a realistic demonstration and testing environment for social protection programs. It leverages core OpenSPP modules to illustrate data flow, module interactions, and custom field integration for user exploration and training. |
| [OpenSPP Document Management System](spp_dms) | The OpenSPP Dms module provides a centralized system for managing and organizing program-related documents within a structured directory tree. It facilitates efficient document retrieval through categorization and indexed storage, automatically capturing essential file metadata such as size, type, and data integrity checksums. |
| [OpenSPP SQL Query Eligibility Manager](spp_eligibility_sql) | Define complex program eligibility criteria using SQL queries for flexible and automated beneficiary enrollment within OpenSPP. |
| [OpenSPP Tag Based Eligibility Manager](spp_eligibility_tags) | OpenSPP Eligibility Tags defines and manages program eligibility criteria based on registrant tags and geographical areas. It automates beneficiary identification by dynamically combining selected tags and areas, extending G2P Programs with a specific eligibility calculation method. |
| [OpenSPP Encryption Module](spp_encryption) | Implements advanced cryptographic services for OpenSPP, enabling data encryption, decryption, digital signing, and signature verification for sensitive program information. It securely manages cryptographic keys in JWK format and distributes public keys via JWKS, facilitating secure inter-system verification and data integrity. |
| [OpenSPP Entitlement Transactions](spp_ent_trans) | The OpenSPP Ent Trans module records and manages all entitlement redemption transactions, establishing a transparent and auditable history for cash and in-kind benefits delivered to beneficiaries. It captures detailed information for each redemption, linking transactions to specific entitlements, service points, and devices, and employs UUIDs to ensure data integrity. |
| [OpenSPP Entitlement Basket](spp_entitlement_basket) | The OpenSPP Entitlement Basket module enables program administrators to define and manage structured baskets of goods and services for beneficiary entitlements. It automates entitlement calculation, integrates with inventory management, and supports a controlled lifecycle with role-based validation for in-kind distributions. |
| [OpenSPP Cash Entitlement](spp_entitlement_cash) | OpenSPP Entitlement Cash establishes a framework for managing cash-based benefits within social protection programs, allowing administrators to define detailed calculation rules and automate the disbursement process. It automatically computes entitlements, manages payment validation workflows, and facilitates secure fund disbursement, incorporating financial controls and maintaining comprehensive audit trails.. |
| [OpenSPP In-Kind Entitlement](spp_entitlement_in_kind) | This module manages the distribution of non-cash benefits within social protection programs, defining in-kind entitlements and automating their generation for eligible beneficiaries. It integrates with inventory management to track stock and facilitates redemption of goods through designated service points, supporting structured distribution workflows. |
| [OpenSPP Event Data](spp_event_data) | Records and tracks events related to individual and group registrants, providing a chronological history of changes and actions within the OpenSPP system. |
| [OpenSPP Event Data Program Membership](spp_event_data_program_membership) | This module allows users to record and track program membership-related events, such as enrollment, suspension, or exit, and link them to specific program membership records within OpenSPP. |
| [OpenSPP Event Demo](spp_event_demo) | OpenSPP Event Demo offers predefined event types, data models, and user interfaces for tracking specific social protection program interactions. It extends registrant profiles to display active event statuses and serves as a practical blueprint for custom event type implementation, leveraging the spp_event_data framework. |
| [OpenSPP Exclusion Filter](spp_exclusion_filter) | Administrators can define and apply specific exclusion criteria based on registrant attributes or existing program participation. The module automates eligibility checks during program creation, systematically filtering out ineligible individuals to refine the beneficiary pool. |
| [OpenSPP Farmer Registry Base](spp_farmer_registry_base) | Manages comprehensive farmer profiles, detailing farm operations, size, legal status, and specific agricultural practices. Furthermore, it links farmers and farms to land records with geographic data, tracks agricultural activities by season, and oversees farm assets and extension services. |
| [OpenSPP Farmer Registry Dashboard](spp_farmer_registry_dashboard) | Provides interactive dashboards and reports for visualizing data from the OpenSPP Farmer Registry, offering insights into key metrics and trends related to registered farmers. |
| [OpenSPP Farmer Registry Demo](spp_farmer_registry_demo) | Generates and populates the OpenSPP Farmer Registry with comprehensive, realistic sample data. It integrates with core registry models to provide diverse farmer profiles, farm details, and agricultural activities, facilitating system exploration, training, and testing. |
| [ID PASS](spp_idpass) | OpenSPP Idpass securely generates and manages digital identification passes for program registrants, streamlining beneficiary verification and access to social protection services. The module automates ID generation using existing registrant data, offers configurable templates with expiry rules, and integrates with external services via secure API calls. |
| [OpenSPP ID Queue](spp_idqueue) | Manages the complete lifecycle of ID card requests for registrants, centralizing their creation, tracking, and final distribution. It streamlines approval workflows, automates ID card generation through integration with external services, and facilitates batch processing with comprehensive audit trails. |
| [OpenSPP Import: DCI API](spp_import_dci_api) | Integrates OpenSPP with external Digital Civil Identity (DCI) compliant registries for automated import and synchronization of individual and family registrant data. It automatically creates or updates registrant profiles, manages hierarchical location data, and facilitates family group creation within OpenSPP. |
| [OpenSPP Import Match](spp_import_match) | OpenSPP Import Match enhances data import processes by intelligently matching incoming records against existing data, preventing duplication and ensuring registry integrity. It provides configurable matching logic and supports seamless updates to existing records during bulk data onboarding. |
| [OpenSPP Irrigation](spp_irrigation) | Manages detailed irrigation assets by type, capacity, and unique identifiers, leveraging integrated GIS capabilities to map and display infrastructure locations and boundaries. The module models water distribution networks by defining and linking irrigation sources to destinations, providing critical data for strategic planning of resource allocation and infrastructure projects. |
| [OpenSPP Land Record](spp_land_record) | The OpenSPP Land Record module digitizes and centralizes land parcel information, linking it to associated farms, ownership details, and lease agreements. It captures and displays geographical boundaries and coordinates on interactive maps, supporting land use classification and program planning. |
| [OpenSPP Manual Entitlement](spp_manual_entitlement) | Administrators directly create entitlements for beneficiaries within specific program cycles, accommodating exceptional eligibility criteria not covered by automated rules. A step-by-step wizard guides entitlement creation, preventing duplicates for beneficiaries within a program cycle and supporting scalable asynchronous processing. |
| [OpenSPP API: Oauth](spp_oauth) | The module establishes an OAuth 2. 0 authentication framework, securing OpenSPP API communication for integrated systems and applications. |
| [OpenSPP OpenID VCI](spp_openid_vci) | The module issues and manages Verifiable Credentials for OpenSPP program registrants, leveraging OpenID Connect for Verifiable Presentations. It generates QR codes for secure digital sharing, integrates registrant data into VCs, and ensures credential authenticity through digital signing and encryption. |
| [OpenSPP OpenID VCI Group](spp_openid_vci_group) | Extends OpenSPP's Verifiable Credential issuance capabilities to manage and represent groups of registrants. Generates standardized VCs encapsulating group information from registry data, providing a verifiable digital identity for efficient verification and integration with group management. |
| [OpenSPP OpenID VCI Individual](spp_openid_vci_individual) | The spp_openid_vci_individual module extends OpenSPP's Verifiable Credential issuance to individual registrants, enabling secure digital identity and attribute proofs using OpenID4VP and DIDs. It integrates VC issuance directly into individual profiles, supporting verifiable presentations and customizable issuer configurations for program-specific data. |
| [OpenSPP Proxy Means Testing](spp_pmt) | This module calculates a Proxy Means Testing (PMT) score for registrant groups, objectively prioritizing beneficiaries for social protection programs. It enables defining custom field weights, implementing area-specific weighting, and automating score computation based on diverse indicators. |
| [OpenSPP POS](spp_pos) | The OpenSPP Pos module extends the standard Odoo Point of Sale system to facilitate secure redemption of social protection entitlements for beneficiaries. It performs real-time validation of entitlement codes and designates specific products purchasable using these benefits. |
| [OpenSPP Program ID](spp_program_id) | Assigns and manages unique, immutable identifiers for every social protection program within the OpenSPP platform. This core component extends program records to ensure distinct identification, facilitating streamlined data management, enhanced reporting, and seamless system integration. |
| [OpenSPP Programs](spp_programs) | Manage cash and in-kind entitlements, integrate with inventory, and enhance program management features for comprehensive social protection and agricultural support. |
| [OpenSPP Programs: Compliance Criteria](spp_programs_compliance_criteria) | Administrators can define and manage dynamic compliance criteria for social protection program beneficiaries, extending initial enrollment requirements. The module automates beneficiary evaluation against these rules, flags non-compliant individuals, and enables configurable compliance filtering during program operations. |
| [OpenSPP Programs: Service Points Integration](spp_programs_sp) | OpenSPP Programs Sp extends core program management by integrating service points directly into entitlement and beneficiary processes. It automatically links beneficiaries' assigned service points to their entitlements, supporting both cash and in-kind benefit distribution. |
| [OpenSPP Registrant Import](spp_registrant_import) | Streamlines the import of registrant data into OpenSPP, simplifies data mapping, and automates unique ID generation. |
| [OpenSPP Registrant Tags](spp_registrant_tag) | OpenSPP registrants gain enhanced tagging capabilities through this module, allowing granular categorization by specific attributes, program statuses, or needs. It extends the G2P Registry Base module, improving data findability and facilitating targeted interventions with flexible tag management. |
| [OpenSPP Data Source](spp_registry_data_source) | Establishes a secure framework for OpenSPP to connect with external data systems like national registries and social protection databases. It facilitates structured data retrieval, defines field mapping, configures secure authentication methods, and manages specific API endpoints. |
| [OpenSPP Registry Group Hierarchy](spp_registry_group_hierarchy) | The module introduces hierarchical relationships among OpenSPP registry groups, enabling the creation of nested structures where groups can contain both individuals and other sub-groups. It extends g2p. |
| [OpenSPP Registry: Scan ID Document](spp_scan_id_document) | The module integrates direct ID document scanning into OpenSPP, enabling users to capture physical identification documents directly within registrant profiles. This functionality streamlines identity data collection by minimizing manual transcription errors and provides a verifiable digital record for compliance and auditing. |
| [OpenSPP Service Point Device](spp_service_point_device) | Registers and tracks physical terminal devices, maintaining a comprehensive inventory of operational hardware within the OpenSPP platform. It captures device specifications, manages operational status, and associates each terminal with a specific service point, including designation of top-up locations. |
| [OpenSPP Service Points Management](spp_service_points) | The OpenSPP Service Points module manages physical or virtual locations for social protection service delivery, establishing and categorizing operational service points. It links these points to hierarchical geographical areas, company entities, and user accounts, integrating with spp_area and g2p_registry_base for comprehensive organizational and location management. |
| [OpenSPP: Starter](spp_starter) | A guided setup wizard configures new OpenSPP instances, defining core program requirements and automatically installing relevant OpenSPP modules. It specializes system deployment based on program type selection and performs initial data cleanup for a production-ready environment. |
| [OpenSPP User Roles](spp_user_roles) | The OpenSPP User Roles module defines and manages distinct user roles, categorizing them as global or local, to implement area-based access control. It restricts user access to specific geographical areas by leveraging the spp_area module and automates underlying system permission assignments. |

## G2P Modules

| Module | Summary |
| ------ | ------- |
| [G2P Auth: OIDC - Reg ID](g2p_auth_id_oidc) | No summary provided |
| [G2P Registry: Bank Details](g2p_bank) | No summary provided |
| [G2P Registry: Bank Details Rest API](g2p_bank_rest_api) | No summary provided |
| [G2P Connect Demo](g2p_connect_demo) | No summary provided |
| [G2P Encryption: Base](g2p_encryption) | No summary provided |
| [G2P Encryption: Keymanager](g2p_encryption_keymanager) | No summary provided |
| [G2P Encryption: Rest API](g2p_encryption_rest_api) | No summary provided |
| [OpenG2P Entitlement: Differential](g2p_entitlement_differential) | No summary provided |
| [OpenG2P Entitlement: In-Kind](g2p_entitlement_in_kind) | No summary provided |
| [OpenG2P Entitlement: Voucher](g2p_entitlement_voucher) | No summary provided |
| [G2P OpenID VCI: Base](g2p_openid_vci) | No summary provided |
| [G2P OpenID VCI: Program Beneficiaries](g2p_openid_vci_programs) | No summary provided |
| [OpenG2P Program Payment: Cash](g2p_payment_cash) | No summary provided |
| [OpenG2P Program Payments: In Files](g2p_payment_files) | No summary provided |
| [OpenG2P Program Payment: G2P Connect Payment Manager](g2p_payment_g2p_connect) | No summary provided |
| [OpenG2P Program Payment (Payment Interoperability Layer)](g2p_payment_interop_layer) | No summary provided |
| [OpenG2P Program Payment (Payment Hub EE)](g2p_payment_phee) | No summary provided |
| [OpenG2P Program Payment: Simple Mpesa Payment Manager](g2p_payment_simple_mpesa) | No summary provided |
| [OpenG2P Program: Approval](g2p_program_approval) | No summary provided |
| [OpenG2P Program: Assessment](g2p_program_assessment) | No summary provided |
| [OpenG2P Programs: Autoenrol](g2p_program_autoenrol) | No summary provided |
| [OpenG2P Programs: Cycleless](g2p_program_cycleless) | No summary provided |
| [OpenG2P Program: Documents](g2p_program_documents) | No summary provided |
| [G2P Program: Registrant Info](g2p_program_registrant_info) | No summary provided |
| [G2P Program : Program Registrant Info Rest API](g2p_program_registrant_info_rest_api) | No summary provided |
| [OpenG2P Programs: Reimbursement](g2p_program_reimbursement) | No summary provided |
| [OpenG2P Programs](g2p_programs) | No summary provided |
| [G2P Programs: REST API](g2p_programs_rest_api) | No summary provided |
| [G2P: Proxy Means Test](g2p_proxy_means_test) | No summary provided |
| [G2P Registry: Additional Info](g2p_registry_addl_info) | No summary provided |
| [G2P Registry: Additional Info REST API](g2p_registry_addl_info_rest_api) | No summary provided |
| [G2P Registry: Base](g2p_registry_base) | No summary provided |
| [G2P Registry: Encryption](g2p_registry_encryption) | No summary provided |
| [G2P Registry: Groups](g2p_registry_group) | No summary provided |
| [G2P Registry: Individual](g2p_registry_individual) | No summary provided |
| [G2P Registry: Membership](g2p_registry_membership) | No summary provided |
| [G2P Registry: Rest API](g2p_registry_rest_api) | No summary provided |
| [G2P Registry: Rest API Extension Demo](g2p_registry_rest_api_extension_demo) | No summary provided |

```{toctree}
---
caption: Getting Started
maxdepth: 2
hidden: true
---

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
g2p_auth_id_oidc
g2p_bank
g2p_bank_rest_api
g2p_connect_demo
g2p_encryption
g2p_encryption_keymanager
g2p_encryption_rest_api
g2p_entitlement_differential
g2p_entitlement_in_kind
g2p_entitlement_voucher
g2p_openid_vci
g2p_openid_vci_programs
g2p_payment_cash
g2p_payment_files
g2p_payment_g2p_connect
g2p_payment_interop_layer
g2p_payment_phee
g2p_payment_simple_mpesa
g2p_program_approval
g2p_program_assessment
g2p_program_autoenrol
g2p_program_cycleless
g2p_program_documents
g2p_program_registrant_info
g2p_program_registrant_info_rest_api
g2p_program_reimbursement
g2p_programs
g2p_programs_rest_api
g2p_proxy_means_test
g2p_registry_addl_info
g2p_registry_addl_info_rest_api
g2p_registry_base
g2p_registry_encryption
g2p_registry_group
g2p_registry_individual
g2p_registry_membership
g2p_registry_rest_api
g2p_registry_rest_api_extension_demo
```