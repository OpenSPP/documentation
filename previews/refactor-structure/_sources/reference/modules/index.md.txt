
# OpenSPP modules

## SPP modules

```{toctree}
:maxdepth: 1
:hidden:

spp_api
spp_api_records
spp_area
spp_area_base
spp_area_gis
spp_attendance
spp_attendance_generated
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
spp_change_request_add_group_to_group
spp_change_request_base
spp_change_request_change_info
spp_change_request_change_info_generated
spp_change_request_create_farm
spp_change_request_create_group
spp_change_request_edit_farm
spp_change_request_edit_farmer
spp_consent
spp_custom_field
spp_custom_field_custom_filter
spp_custom_field_recompute_daily
spp_custom_fields_ui
spp_custom_filter
spp_custom_filter_farmer_registry
spp_custom_filter_ui
spp_cycle_attendance_compliance
spp_cycle_attendance_compliance_generated
spp_dashboard_base
spp_dashboard_base_generated
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
spp_ethnic_group
spp_ethnic_group_generated
spp_event_data
spp_event_data_program_membership
spp_event_demo
spp_exclusion_filter
spp_farmer_registry_base
spp_farmer_registry_dashboard
spp_farmer_registry_default_ui
spp_farmer_registry_default_ui_generated
spp_farmer_registry_demo
spp_grm
spp_grm_generated
spp_hide_menus
spp_hide_menus_base
spp_hide_menus_base_generated
spp_hide_menus_generated
spp_idpass
spp_idqueue
spp_import_dci_api
spp_import_match
spp_irrigation
spp_land_record
spp_manual_eligibility
spp_manual_entitlement
spp_mis_demo
spp_oauth
spp_openid_vci
spp_openid_vci_group
spp_openid_vci_individual
spp_pmt
spp_pos
spp_pos_id_redemption
spp_pos_id_redemption_generated
spp_program_id
spp_programs
spp_programs_compliance_criteria
spp_programs_sp
spp_qr_scanner
spp_qr_scanner_generated
spp_registrant_import
spp_registrant_tag
spp_registry_approval
spp_registry_approval_generated
spp_registry_approval_group
spp_registry_approval_group_generated
spp_registry_approval_individual
spp_registry_approval_individual_generated
spp_registry_base
spp_registry_base_generated
spp_registry_data_source
spp_registry_group_hierarchy
spp_scan_id_document
spp_service_point_device
spp_service_points
spp_starter
spp_user_roles
```

| Module | Summary |
| ------ | ------- |
| [API](spp_api) | Establishes a RESTful API framework for OpenSPP, allowing external systems to securely read, create, update, and delete platform data. Customizable API endpoints, robust authentication, comprehensive logging, and flexible data field mapping enhance integration and auditing capabilities. |
| [API Records](spp_api_records) | It exposes RESTful API endpoints, enabling external systems to programmatically access and manage OpenSPP's core operational data. These endpoints facilitate querying, creating, updating, and deleting records for entities like service points, social protection programs, product definitions, and beneficiary entitlements. |
| [Area Management](spp_area) | Establishes direct associations between OpenSPP registrants, beneficiary groups, and their corresponding geographical administrative areas. It validates registrant-area linkages against official area types, ensuring data integrity and enabling targeted program delivery and analysis. |
| [Area Management (Base)](spp_area_base) | This module enables management of geographical areas, linking them to registrants for targeted interventions and analysis in social protection programs. |
| [Area GIS](spp_area_gis) | Integrates GIS capabilities into OpenSPP's Area management, enabling visualization on maps, associating coordinates, defining polygons, and facilitating spatial analysis for improved targeting and monitoring of social protection programs. |
| [Attendance](spp_attendance) | This module accurately tracks participant attendance for social protection program activities, capturing essential details like date, time, location, and activity type. It integrates attendance records to inform conditional benefit eligibility and leverages spp_oauth to secure API endpoints for external data submission. |
| [Audit Config](spp_audit_config) | Administrators define and manage comprehensive audit rules within this module, specifying which data models, fields, and operations require tracking across the OpenSPP platform. The module ensures data integrity and accountability by logging user and timestamp details, and it enables cross-record auditing through parent-child relationships for consolidated change views. |
| [SPP Audit Log](spp_audit_log) | Comprehensively tracks all data modifications and user actions across the OpenSPP platform, recording old and new values for configured data. It enhances accountability and data integrity by maintaining an immutable history of changes, crucial for internal audits, compliance, and detecting unauthorized alterations. |
| [Audit Post](spp_audit_post) | OpenSPP Audit Post extends core audit logging by automatically posting audit log messages to related parent records. It consolidates changes from child records onto the parent's communication timeline, leveraging the mail module for message posting. |
| [Auto-Update Entitlements](spp_auto_update_entitlements) | Automatically reviews and updates the state of entitlements based on their redemption status at the end of each program cycle. It assigns precise states, including a new 'Partially Redeemed' status, to ensure accurate records for program closure, reporting, and auditing. |
| [Base](spp_base) | Establishes core system settings and generates unique identifiers for records, enhancing registrant profiles with attributes like tags, gender, and type. The module also integrates Top-up Cards for identification and provides fundamental user interface elements with initial security configurations for user roles. |
| [Base API](spp_base_api) | Provides foundational API functions and methods for robust data exchange between OpenSPP and external systems or internal modules. It enables efficient record management, complex data retrieval, and external system integration primarily through APIs and XML-RPC protocols. |
| [Base Demo](spp_base_demo) | The OpenSPP Base Demo module populates the system with essential sample data, enabling immediate exploration and understanding of core functionalities. It includes diverse sample registrants, social protection programs, and products, providing foundational demo data while conforming to the g2p_registry_individual module's data models. |
| [Base GIS](spp_base_gis) | This module stores and organizes geospatial data, including points, lines, and polygons, for visualization on interactive maps. It enables spatial querying, custom map layer configuration, and integrates location awareness across OpenSPP modules for targeted program management. |
| [Base GIS Demo](spp_base_gis_demo) | Demonstrates the integration of Geographical Information System (GIS) capabilities within OpenSPP, illustrating how to extend data models with various geographical field types. It provides examples for defining custom geospatial data models and visualizing diverse geographical entities, including points, lines, and polygons, on interactive maps. |
| [Base GIS REST](spp_base_gis_rest) | The module provides RESTful API endpoints for secure, programmatic access to OpenSPP's Geographical Information System data, leveraging OAuth 2.0 and Basic authentication. |
| [Base Settings](spp_base_setting) | OpenSPP Base Setting provides fundamental configurations for country implementations, establishing core organizational structures such as Country Offices. It also enables tailored user interface adaptations and streamlines user management by linking individuals to specific Country Offices for context-aware data access. |
| [Program Entitlement Basic Cash Spent](spp_basic_cash_entitlement_spent) | Records beneficiary expenditures against allocated cash entitlements within social protection programs to monitor utilization. It automatically calculates remaining balances and extends the g2p.entitlement model. |
| [Change Request](spp_change_request) | The OpenSPP Change Request module streamlines the modification of registrant information through a structured, auditable framework. Configurable multi-stage validation workflows ensure proper review and approval, while a comprehensive audit trail records all actions before systematically applying approved changes to registrant records. |
| [Change Request Demo: Add Child/Member](spp_change_request_add_children_demo) | The module formalizes the process of adding new individuals to existing groups within the OpenSPP registry via a dedicated Change Request framework. It integrates ID scanning for rapid data entry, automates new registrant profile creation and group membership updates, and stores supporting documents in the DMS. |
| [Change Request: Add Farmer](spp_change_request_add_farmer) | Provides a specialized workflow for adding new farmers to existing groups in the registry. |
| [Change Request: Add Group to a Group](spp_change_request_add_group_to_group) | Manages change requests to add individual farmers into an existing group, validating memberships and capturing supporting documents. |
| [Change Request Base](spp_change_request_base) | Streamlines the process of handling changes to registrant information within the OpenSPP system, providing a structured framework for submitting, reviewing, approving, and applying modifications. |
| [Change Information Change Request](spp_change_request_change_info) | Manages a structured process for updating an individual registrant's core personal and identification details within the OpenSPP platform. It integrates ID scanning for automatic data population, enforces data integrity with validation rules, and securely stores supporting documents in dedicated DMS directories. |
| [Change Request: Create Farm](spp_change_request_create_farm) | Facilitates change requests to register new farms, collecting farmer, land, and asset details for review and approval. |
| [Change Request: Create Group](spp_change_request_create_group) | Provides a specialized workflow for adding new group in the registry. |
| [Change Request: Edit Farm](spp_change_request_edit_farm) | Supports change requests that update existing farm groups, including land records, assets, and registrant information. |
| [Change Request: Edit Farmer](spp_change_request_edit_farmer) | Provides a specialized workflow for updating existing Farmer in the registry. |
| [Consent](spp_consent) | This module establishes a comprehensive system for managing and tracking explicit consent from individuals and groups within social protection programs. It records specific consent agreements linked to registrants, tracks consent validity with expiry dates, and enables configuration of diverse consent types. |
| [Custom Fields](spp_custom_field) | The module enables administrators to define and add custom data fields directly to registrant profiles, tailoring data collection for specific social protection programs. It supports field differentiation by registrant type, integrates new data points into records, and provides dedicated sections for read-only program indicators. |
| [Custom Field Custom Filter Integration](spp_custom_field_custom_filter) | OpenSPP's filtering system gains custom-defined data field integration, allowing administrators to use program-specific criteria for record segmentation. This enables the construction of highly specific queries, enhancing data analysis and streamlining operational processes for targeted interventions. |
| [Custom Field Recompute Daily](spp_custom_field_recompute_daily) | The OpenSPP Custom Field Recompute Daily module automates the daily recalculation of designated computed fields, ensuring data accuracy and currency. It optimizes system performance by processing large datasets asynchronously in configurable batches, leveraging the Queue Job module. |
| [Custom Fields UI](spp_custom_fields_ui) | The OpenSPP Custom Fields UI module provides a user interface for program implementers to define and manage custom data fields for registrants. It extends registrant profiles by associating custom data with individuals or groups, supporting program-specific indicators and calculated data points within the OpenSPP platform. |
| [Custom Filter](spp_custom_filter) | The module empowers administrators to precisely control which fields appear in Odoo's filtering interface. This capability streamlines data searches, reduces UI clutter, and enhances the user experience by ensuring only relevant fields are available for filtering. |
| [Custom Filter Farmer Registry](spp_custom_filter_farmer_registry) | Customizes the OpenSPP UI to enhance filtering for Farmer Registry, improving usability and efficiency in managing registrants within social protection programs. |
| [Custom Filter UI](spp_custom_filter_ui) | Customizes the OpenSPP UI to enhance filtering for Res Partners, improving usability and efficiency in managing registrants within social protection programs. |
| [Cycle: Attendance Compliance](spp_cycle_attendance_compliance) | Program managers define and enforce attendance requirements as eligibility criteria for beneficiaries within social protection program cycles. The module integrates with external attendance systems to automatically fetch records, then evaluates beneficiaries against defined thresholds to ensure ongoing program eligibility. |
| [Dashboard: Base](spp_dashboard_base) | Establishes the foundational framework and consistent user interface components for analytical dashboards across the OpenSPP platform. It delivers core data visualization elements, including reusable metrics, charts, and data cards, enabling other modules to build specialized program-specific dashboards. |
| [Data Export](spp_data_export) | The spp_data_export module enhances OpenSPP's capability to extract large volumes of program data to Excel, overcoming standard export tool limitations regarding file size and row capacity. It proactively manages Excel's maximum row capacity and overrides default export functionality to ensure complete and reliable data for external analysis. |
| [DCI API Server](spp_dci_api_server) | Exposes OpenSPP's individual and household registry data via a DCI-compliant RESTful API. Secures data exchange through client credential management and token-based authentication for external systems. |
| [Document Management System](spp_dms) | The OpenSPP Dms module provides a centralized system for managing and organizing program-related documents within a structured directory tree. It facilitates efficient document retrieval through categorization and indexed storage, automatically capturing essential file metadata such as size, type, and data integrity checksums. |
| [SQL Query Eligibility Manager](spp_eligibility_sql) | Define complex program eligibility criteria using SQL queries for flexible and automated beneficiary enrollment within OpenSPP. |
| [Tag Based Eligibility Manager](spp_eligibility_tags) | OpenSPP Eligibility Tags defines and manages program eligibility criteria based on registrant tags and geographical areas. It automates beneficiary identification by dynamically combining selected tags and areas, extending G2P Programs with a specific eligibility calculation method. |
| [Encryption Module](spp_encryption) | Implements advanced cryptographic services for OpenSPP, enabling data encryption, decryption, digital signing, and signature verification for sensitive program information. It securely manages cryptographic keys in JWK format and distributes public keys via JWKS, facilitating secure inter-system verification and data integrity. |
| [Entitlement Transactions](spp_ent_trans) | The OpenSPP Ent Trans module records and manages all entitlement redemption transactions, establishing a transparent and auditable history for cash and in-kind benefits delivered to beneficiaries. It captures detailed information for each redemption, linking transactions to specific entitlements, service points, and devices, and employs UUIDs to ensure data integrity. |
| [Entitlement Basket](spp_entitlement_basket) | The OpenSPP Entitlement Basket module enables program administrators to define and manage structured baskets of goods and services for beneficiary entitlements. It automates entitlement calculation, integrates with inventory management, and supports a controlled lifecycle with role-based validation for in-kind distributions. |
| [Cash Entitlement](spp_entitlement_cash) | OpenSPP Entitlement Cash establishes a framework for managing cash-based benefits within social protection programs, allowing administrators to define detailed calculation rules and automate the disbursement process. It automatically computes entitlements, manages payment validation workflows, and facilitates secure fund disbursement, incorporating financial controls and maintaining comprehensive audit trails. |
| [In-Kind Entitlement](spp_entitlement_in_kind) | This module manages the distribution of non-cash benefits within social protection programs, defining in-kind entitlements and automating their generation for eligible beneficiaries. It integrates with inventory management to track stock and facilitates redemption of goods through designated service points, supporting structured distribution workflows. |
| [OpenSPP: Ethnic Group](spp_ethnic_group) | Establishes a standardized framework for defining and managing ethnic group classifications within the OpenSPP platform. It enhances demographic data accuracy in registrant profiles, supporting targeted program design and detailed reporting by integrating with g2p_registry_base. |
| [Event Data](spp_event_data) | Records and tracks events related to individual and group registrants, providing a chronological history of changes and actions within the OpenSPP system. |
| [Event Data Program Membership](spp_event_data_program_membership) | This module allows users to record and track program membership-related events, such as enrollment, suspension, or exit, and link them to specific program membership records within OpenSPP. |
| [Event Demo](spp_event_demo) | OpenSPP Event Demo offers predefined event types, data models, and user interfaces for tracking specific social protection program interactions. It extends registrant profiles to display active event statuses and serves as a practical blueprint for custom event type implementation, leveraging the spp_event_data framework. |
| [Exclusion Filter](spp_exclusion_filter) | Administrators can define and apply specific exclusion criteria based on registrant attributes or existing program participation. The module automates eligibility checks during program creation, systematically filtering out ineligible individuals to refine the beneficiary pool. |
| [Farmer Registry Base](spp_farmer_registry_base) | Manages comprehensive farmer profiles, detailing farm operations, size, legal status, and specific agricultural practices. Furthermore, it links farmers and farms to land records with geographic data, tracks agricultural activities by season, and oversees farm assets and extension services. |
| [Farmer Registry Dashboard](spp_farmer_registry_dashboard) | Provides interactive dashboards and reports for visualizing data from the OpenSPP Farmer Registry, offering insights into key metrics and trends related to registered farmers. |
| [Farmer Registry Default UI](spp_farmer_registry_default_ui) | This module delivers the essential user interface components for managing OpenSPP farmer and farm registry data. It enables streamlined farmer registration, efficient farm management, and accessible entry of agricultural activity and asset information. |
| [Farmer Registry Demo](spp_farmer_registry_demo) | Generates and populates the OpenSPP Farmer Registry with comprehensive, realistic sample data. It integrates with core registry models to provide diverse farmer profiles, farm details, and agricultural activities, facilitating system exploration, training, and testing. |
| [- Grievance Redress Mechanism](spp_grm) | Provides a centralized Grievance Redress Mechanism for receiving, tracking, and resolving beneficiary complaints and feedback. It supports multi-channel submission, manages resolution workflows through customizable stages, and links grievances directly to individual or group registrants. |
| [Hide Non-OpenSPP Menus](spp_hide_menus) | The module automatically hides non-core OpenSPP menus to streamline the user interface. It removes Calendar, Contacts, Accounting, Event, Stock, and UTM from the main navigation, focusing users on social protection program management. |
| [Hide Non-OpenSPP Menus: Base](spp_hide_menus_base) | Administrators can manage the visibility of OpenSPP navigation menus, streamlining the user interface for specific user groups. The module modifies ir.ui.menu records to control menu visibility, providing a foundation for other modules to selectively hide non-essential navigation items. |
| [POS: ID Redemption](spp_pos_id_redemption) | Enables secure redemption of social protection entitlements at Point of Sale terminals through beneficiary unique identification. The module integrates ID verification with entitlement management, automatically mapping cash entitlements to products and tracking voucher status in real-time. |
| [QR Scanner](spp_qr_scanner) | The OpenSPP QR Scanner module identifies individuals and accesses information through scanning beneficiary-specific QR codes. This capability streamlines field operations by enabling rapid data retrieval and minimizing manual data entry errors for program delivery and monitoring. |
| [Registry Approval: Base](spp_registry_approval) | This module implements a structured workflow for managing the lifecycle of OpenSPP registry entries, ensuring beneficiary data meets required standards through a formal approval process. It introduces distinct states for each entry and restricts approval actions to authorized personnel, preventing premature program enrollment. |
| [Registry Approval: Group](spp_registry_approval_group) | Extending the OpenSPP registry's approval framework, this module enables formal validation and management of collective entity records. It integrates the existing workflow to ensure group data undergoes a structured review process, maintaining data integrity for program enrollment. |
| [Registry Approval: Individual](spp_registry_approval_individual) | Manages the validation and official status of individual registrants by extending the base registry approval process within social protection programs. It ensures individual beneficiary data undergoes a dedicated review workflow, applying core approval states to enhance data quality and enable precise program enrollment. |
| [Registry: Base](spp_registry_base) | The module establishes the OpenSPP-specific foundation for managing individual beneficiaries and various group types. It extends core G2P Registry functionalities by providing specialized import templates and tools for efficient registrant data population. |

## G2P modules

OpenSPP builds upon the robust foundation of OpenG2P, leveraging its extensive suite of modules to enhance social protection program management. Below is a comprehensive list of G2P modules that are integral to OpenSPP's functionality:

- [Auth ID OIDC](g2p_auth_id_oidc)
- [Auth OIDC](g2p_auth_oidc)
- [Bank](g2p_bank)
- [Bank REST API](g2p_bank_rest_api)
- [Change Log](g2p_change_log)
- [Connect Demo](g2p_connect_demo)
- [Disable Password Login](g2p_disable_password_login)
- [Documents](g2p_documents)
- [Encryption](g2p_encryption)
- [Encryption Keymanager](g2p_encryption_keymanager)
- [Encryption REST API](g2p_encryption_rest_api)
- [Entitlement Differential](g2p_entitlement_differential)
- [Entitlement In Kind](g2p_entitlement_in_kind)
- [Entitlement Voucher](g2p_entitlement_voucher)
- [Enumerator](g2p_enumerator)
- [Formio](g2p_formio)
- [MIS Importer](g2p_mis_importer)
- [MTS](g2p_mts)
- [Notifications Base](g2p_notifications_base)
- [Notifications Fast2SMS](g2p_notifications_fast2sms)
- [Notifications REST API](g2p_notifications_rest_api)
- [Notifications Voucher](g2p_notifications_voucher)
- [Notifications WiSERV](g2p_notifications_wiserv)
- [ODK Importer](g2p_odk_importer)
- [ODK Importer Program](g2p_odk_importer_program)
- [ODK User Mapping](g2p_odk_user_mapping)
- [OpenID VCI](g2p_openid_vci)
- [OpenID VCI Programs](g2p_openid_vci_programs)
- [OpenID VCI REST API](g2p_openid_vci_rest_api)
- [Payment Cash](g2p_payment_cash)
- [Payment Files](g2p_payment_files)
- [Payment Connect](g2p_payment_g2p_connect)
- [Payment Interop Layer](g2p_payment_interop_layer)
- [Payment PHEE](g2p_payment_phee)
- [Payment Simple M-Pesa](g2p_payment_simple_mpesa)
- [Portal Auth](g2p_portal_auth)
- [Profile Image](g2p_profile_image)
- [Program Approval](g2p_program_approval)
- [Program Assessment](g2p_program_assessment)
- [Program Autoenrol](g2p_program_autoenrol)
- [Program Cycleless](g2p_program_cycleless)
- [Program Documents](g2p_program_documents)
- [Program Registrant Info](g2p_program_registrant_info)
- [Program Registrant Info REST API](g2p_program_registrant_info_rest_api)
- [Program Reimbursement](g2p_program_reimbursement)
- [Programs](g2p_programs)
- [Programs REST API](g2p_programs_rest_api)
- [Proxy Means Test](g2p_proxy_means_test)
- [Registry Additional Info](g2p_registry_addl_info)
- [Registry Additional Info REST API](g2p_registry_addl_info_rest_api)
- [Registry Base](g2p_registry_base)
- [Registry Documents](g2p_registry_documents)
- [Registry Encryption](g2p_registry_encryption)
- [Registry Group](g2p_registry_group)
- [Registry Individual](g2p_registry_individual)
- [Registry Membership](g2p_registry_membership)
- [Registry REST API](g2p_registry_rest_api)
- [Registry REST API Extension Demo](g2p_registry_rest_api_extension_demo)
- [Service Provider Beneficiary Management](g2p_service_provider_beneficiary_management)
- [Service Provider Portal Base](g2p_service_provider_portal_base)
- [Social Registry Importer](g2p_social_registry_importer)
- [Superset Dashboard](g2p_superset_dashboard)
- [Theme](g2p_theme)
