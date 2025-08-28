# OpenSPP Change Request Create Farm

The OpenSPP Change Request Create Farm module provides a specialized and structured workflow for registering new farm entities within the OpenSPP farmer registry. It facilitates the comprehensive capture of farm, farmer, land, and agricultural activity data through a formal change request process, ensuring data accuracy and system integrity.

## Purpose

This module streamlines the integration of new farm data into the OpenSPP platform, ensuring all necessary information is captured and validated through a controlled process. It empowers users to:

*   **Formalize New Farm Registrations:** Establish a standardized procedure for adding new farm entities, ensuring all required data is collected and tracked.
*   **Capture Comprehensive Farm Data:** Collect detailed information spanning farm identification, farmer demographics, land records, and specific agricultural activities.
*   **Leverage Change Request Workflows:** Integrate new farm creation into the existing OpenSPP change request system, allowing for multi-step review, approval, and auditing.
*   **Maintain Data Quality:** Implement essential validations for farmer details, land information, and contact numbers, ensuring the accuracy and consistency of the registry.
*   **Support Document Management:** Facilitate the attachment and management of all supporting documents relevant to the new farm registration, such as ID copies or land titles.

## Dependencies and Integration

The `spp_change_request_create_farm` module extends and integrates with several core OpenSPP modules to deliver its comprehensive functionality:

*   [OpenSPP Change Request](spp_change_request): Provides the foundational framework for submitting, reviewing, and approving all change requests, including the creation of new farms.
*   [G2P Registry Individual](g2p_registry_individual): Manages the individual details of the farmer associated with the new farm, ensuring their personal data is accurately recorded.
*   [G2P Registry Group](g2p_registry_group): Utilizes the group registry to represent the farm as a distinct entity, allowing it to be managed as a collective registrant.
*   [G2P Registry Membership](g2p_registry_membership): Establishes and manages the relationship between the individual farmer and the farm group, defining their role within the farm.
*   [OpenSPP Service Points](spp_service_points): Enables the initiation of new farm registration requests through designated service points, often located closer to beneficiaries.
*   [OpenSPP IDPass](spp_idpass): Supports the integration of ID scanning and verification processes, enhancing the accuracy of farmer identification during registration.
*   [OpenSPP Farmer Registry Base](spp_farmer_registry_base): Provides the underlying models for managing agricultural activities (crops, livestock, aquaculture) and farm assets, which are then populated by this module.
*   [OpenSPP Land Record](spp_land_record): Integrates land parcel details and geospatial information, linking specific land records to the newly created farm.

## Additional Functionality

The module offers a robust set of features to support the creation of new farm records:

### Farm and Farmer Profile Creation

Users can define new farm entities by specifying a unique **Group Name** and assigning a **Group Kind**, typically "Farm." Concurrently, comprehensive details about the primary farmer are captured, including their **Family Name**, **Given Name**, **National ID Number**, **Mobile Telephone Number**, **Date of Birth**, **Sex**, **Highest Education Level**, **Marital Status**, and **Household Size**. This ensures a complete profile for both the farm and its associated farmer.

### Agricultural Activities and Asset Inventory

The module allows for detailed recording of various agricultural practices. Users can specify **Crop Agricultural Activities**, **Livestock Agricultural Activities**, and **Aquaculture Agricultural Activities** associated with the farm. Additionally, it supports a comprehensive inventory of **Farm Assets** and **Farm Machinery**, providing a holistic view of the farm's operational capacity.

### Land Record and Legal Status Management

Essential land information can be entered directly, including the **Parcel Name/ID**, **Acreage**, and **Geographical Coordinates** (both point and polygon data). Users can also specify the **Legal Status** of the land, such as "Owned by self," "Leased from actual owner," or "Owned by government," which is crucial for tenure security and program eligibility.

### Data Validation and Document Management

The module includes critical data validations to ensure accuracy. It enforces mandatory fields for the Group Name, Group Kind, and key farmer details. Date fields, such as the farmer's birthdate, are validated to prevent future dates, and mobile telephone numbers are checked for correct formatting based on country codes. Furthermore, integration with the Document Management System (DMS) allows users to attach and manage supporting documents like scanned ID documents and land deeds directly within the change request.

## Conclusion

The OpenSPP Change Request Create Farm module provides a structured and validated workflow for integrating new farm entities and their associated farmer, land, and activity data into the OpenSPP registry, serving as a critical component for effective social protection programs and farmer registries.