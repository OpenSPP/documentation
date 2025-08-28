# OpenSPP Change Request Edit Farm

The `spp_change_request_edit_farm` module provides a specialized workflow for managing and applying changes to existing farm records within the OpenSPP farmer registry. It ensures that updates to farm details, agricultural activities, and assets are systematically reviewed and approved before being applied to the live data.

## Purpose

This module streamlines the process of updating comprehensive farm information, ensuring data accuracy and accountability. It accomplishes this by:

*   **Standardizing Farm Data Updates**: Establishes a formal process for submitting and tracking modifications to registered farm details.
*   **Managing Agricultural Activities**: Allows for recording and updating details about various agricultural practices, including crop cultivation, livestock rearing, and aquaculture.
*   **Tracking Farm Assets**: Enables the maintenance of an inventory of farm assets and machinery associated with a specific farm.
*   **Updating Land Records**: Facilitates changes to land parcel information, including names, acreage, and geographical coordinates.
*   **Ensuring Data Integrity**: Integrates with a change request approval workflow to validate and authorize all proposed modifications before they are applied.

## Dependencies and Integration

The `spp_change_request_edit_farm` module integrates with several core OpenSPP modules to deliver its functionality:

*   **[OpenSPP Change Request](spp_change_request)**: This is the foundational module, providing the core framework for submitting, reviewing, and approving all types of change requests, including those for farm edits.
*   **[G2P Registry Individual](g2p_registry_individual)**: While focused on farms (groups), it relies on the individual registry to identify the applicant associated with the change request, often the head of the farm group.
*   **[G2P Registry Group](g2p_registry_group)**: This module extends the group registrant model, allowing farms to be managed as specific types of groups and providing the underlying structure for farm records.
*   **[G2P Registry Membership](g2p_registry_membership)**: It uses membership information to link individuals to farm groups, helping identify the primary contact for a farm.
*   **[OpenSPP Service Points](spp_service_points)**: Enables the submission of farm edit requests through designated service points, facilitating localized data updates.
*   **[spp_idpass](spp_idpass)**: This module can integrate to capture or verify ID document details relevant to the farm or the applicant making the change request.
*   **[OpenSPP Farmer Registry Base](spp_farmer_registry_base)**: Provides the fundamental data models for farms, agricultural activities, and assets that this module extends and updates.

## Additional Functionality

The `spp_change_request_edit_farm` module offers several key features for managing farm data edits:

### Farm Details and Identification
Users can modify essential information about a farm, including its official group name and the specific kind of group it represents (e.g., "Farm"). The module also supports capturing details from an ID document scanner, which can be used to verify the identity of the person submitting the change request.

### Agricultural Activities Management
This module allows for comprehensive updates to the agricultural activities associated with a farm. Users can add, modify, or remove records for crop cultivation, livestock rearing, and aquaculture activities, ensuring an accurate representation of the farm's operations.

### Farm Assets and Machinery
Users can maintain a detailed inventory of farm assets and machinery. This includes updating information about existing assets or adding new ones, providing a clear picture of the farm's resources.

### Land Records and Legal Status
The module facilitates updates to land parcel information, such as the parcel name, acreage, and geographical coordinates (both point and polygon data). It also allows for modification of the land's legal status, indicating whether it is owned, leased, or held under other arrangements.

### Document Management System Integration
All change requests for farm edits can be supported by attached documents. The module integrates with the OpenSPP Document Management System (DMS) to store relevant files and directories, providing crucial evidence and an audit trail for all modifications.

### Change Request Validation and Application
Before any changes are applied, the module enforces a validation process, requiring that a specific farm (registrant_id) is selected for editing. Upon approval, the module automatically updates the live farm record in the registry, ensuring that all related agricultural activities and assets are correctly linked to the modified farm.

## Conclusion

The `spp_change_request_edit_farm` module is critical for maintaining accurate and up-to-date farm information within OpenSPP, providing a structured and auditable process for all farm-related data modifications.