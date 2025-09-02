---
orphan: true
---

# Change Request: Create Group

The `spp_change_request_create_group` module provides a specialized and structured workflow for formally adding new groups to the OpenSPP registry. It facilitates the creation of new organizational entities, such as farmer cooperatives or households, and optionally their primary members, through a controlled change request process.

## Purpose

This module streamlines the expansion of the OpenSPP registry by enabling the systematic creation of new groups. It addresses the need for a formal process when registering new collective entities or households, ensuring data quality and auditability.

*   **Streamlined Group Registration**: Provides a dedicated, step-by-step process for registering new groups within the OpenSPP system.
*   **Integrated Member Creation**: Allows for the simultaneous creation of a new group and, optionally, its primary individual member, including their demographic and contact details.
*   **Formalized Workflow**: Leverages the OpenSPP Change Request framework to ensure all new group registrations follow a structured, auditable approval process.
*   **Comprehensive Data Capture**: Collects essential group attributes, such as name and kind, and detailed information for associated individuals, including unique identification and contact numbers.
*   **Supporting Document Management**: Integrates with the Document Management System to attach and manage all necessary supporting evidence for the new group and its members.

## Dependencies and Integration

The `spp_change_request_create_group` module extends and integrates with several core OpenSPP modules to deliver its functionality:

*   **OpenSPP Change Request (`spp_change_request`)**: This module is built upon the foundational change request framework, ensuring all new group creations follow a structured, auditable workflow with defined stages and validations.
*   **G2P Registry: Group (`g2p_registry_group`)**: It relies on this module for the underlying data model and business logic related to groups, including the definition of various group kinds.
*   **G2P Registry: Individual (`g2p_registry_individual`)**: This module utilizes the individual registrant model when a primary member is optionally registered alongside a new group, capturing their personal and contact details.
*   **G2P Registry: Membership (`g2p_registry_membership`)**: It establishes the link between a newly created individual and the new group, defining their membership relationship and kind.
*   **OpenSPP Service Points (`spp_service_points`)**: Integrates with the service point infrastructure, allowing group creation requests to be initiated and processed through designated service centers.
*   **OpenSPP ID Pass (`spp_idpass`)**: Supports the capture of ID document details, potentially through scanning, as part of the evidence required for group or individual registration.
*   **OpenSPP Base (`spp_base`)**: As a fundamental OpenSPP module, it provides core system configurations and extensions that this module leverages for consistent operation.

## Additional Functionality

### New Group Details Definition
Users can define a new group by providing its name and selecting an appropriate group kind, such as "Farmer Cooperative" or "Household." The system ensures that both the group name and group kind are mandatory to maintain data integrity and proper classification.

### Optional Primary Member Registration
Alongside creating a new group, users have the option to register a primary individual member. This includes capturing comprehensive demographic details such as family name, given name, additional name, mobile number, sex, marital status, birthdate, birth place, and email. The system automatically computes the full name from the provided parts and validates the birthdate to ensure it is not set in the future.

### Unique Identification and Contact Validation
For the optional primary member, a Unique Identification (UID) number can be recorded, with built-in validation ensuring it is exactly 12 digits long. Mobile telephone numbers are also validated against country-specific formats, enhancing data accuracy for communication and outreach.

### Supporting Document Management
The module integrates seamlessly with the OpenSPP Document Management System (DMS). This allows users to attach supporting documents, such as scanned ID documents or official registration papers, directly to the group creation request, providing comprehensive evidence for the registration.

### Automated Registry Update
Upon successful validation and approval through the change request workflow, the system automatically creates the new group and, if specified, the associated individual member and their membership link in the live registry. This ensures an efficient and error-free update of the core OpenSPP data.

## Conclusion

The `spp_change_request_create_group` module is vital for systematically expanding the OpenSPP registry by enabling the formal creation of new groups and their initial members through a controlled and auditable change request process.