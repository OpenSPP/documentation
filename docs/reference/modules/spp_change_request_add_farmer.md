# OpenSPP Change Request Add Farmer

The OpenSPP Change Request Add Farmer module (technical name: `spp_change_request_add_farmer`) provides a structured and validated workflow for incorporating new individual farmers into existing farmer groups within the OpenSPP registry. It ensures that all additions are properly documented, approved, and integrated into the system.

## Purpose

This module streamlines the process of expanding farmer groups, offering a clear and accountable method for managing new memberships:

*   **Streamline Farmer Group Enrollment:** Facilitates a structured process for adding new individual farmers to existing registered groups, such as cooperatives or community associations. This ensures efficient and organized expansion of farmer groups.
*   **Ensure Data Integrity and Validation:** Implements crucial validation steps, such as requiring at least one farmer to be added per request, to maintain accuracy and completeness of the farmer registry.
*   **Manage Supporting Documentation:** Allows users to attach and manage relevant documents, like ID scans or consent forms, directly within the change request, ensuring a comprehensive record for each new group member.
*   **Integrate with Membership Management:** Automatically creates and updates group membership records upon approval, accurately reflecting the new farmer's role and start date within the target group.
*   **Audit Trail and Accountability:** Provides a clear, traceable workflow for every addition, enhancing transparency and accountability in managing farmer group compositions.

## Dependencies and Integration

This module integrates seamlessly with several core OpenSPP components to provide its functionality:

*   **[OpenSPP Change Request](spp_change_request):** This module extends the core Change Request framework, inheriting its multi-step approval workflow, status tracking, and audit capabilities for all farmer addition requests.
*   **[OpenSPP Farmer Registry Base](spp_farmer_registry_base):** Provides the foundational data structures and context for managing farmer-specific information, ensuring consistency with the overall farmer registry.
*   **[G2P Registry Individual](g2p_registry_individual) & [G2P Registry Group](g2p_registry_group):** Leverages these modules to identify and manage the individual farmers being added and the existing groups they are joining, respectively. It ensures that only registered individuals can be added to registered groups.
*   **[G2P Registry Membership](g2p_registry_membership):** Crucially, upon approval, this module utilizes `g2p_registry_membership` to formally establish the new individual's membership within the specified group, including their role and start date.
*   **[OpenSPP ID Pass](spp_idpass):** Integrates with `spp_idpass` to capture and manage ID document details, supporting identity verification for new farmer additions.
*   **OpenSPP DMS (Document Management System):** This module extends the DMS models to allow direct attachment of supporting files and directories to the 'Add Farmer' change request. This ensures all relevant documents, such as scanned ID cards or consent forms, are securely stored and linked to the specific request.

## Additional Functionality

The module offers specialized features to manage the farmer addition process effectively:

### Request Initiation and Group Selection
Users initiate a change request specifically for adding farmers. They select the target *existing group* (e.g., "Sunrise Coffee Cooperative" or "Local Women Farmers' Association") from the registry that the new farmers will join. This action links the entire request to the specific group needing new members.

### Farmer Details and Membership Assignment
Within the request, users add individual farmers by selecting them from the existing pool of registered individuals. For each farmer, users specify their intended role within the group (e.g., "Member," "Dependent," or "Head of Household") and the effective start date of their membership. The system validates that only eligible individuals, who are not already part of another group, can be selected for membership, preventing duplicate entries.

### Document Management and Identity Verification
The module supports attaching relevant supporting documents, such as scanned ID cards, proof of residency, or signed consent forms, directly to the change request using the integrated Document Management System (DMS). A dedicated field is available for capturing ID document details, which serves as a placeholder for future integration with ID scanning solutions to streamline identity verification processes.

### Automated Membership Creation
Upon successful approval of the 'Add Farmer' change request, the system automatically creates formal membership records within the [G2P Registry: Membership](g2p_registry_membership) module. This ensures that the new farmers are officially linked to their respective groups with their designated roles and start dates, updating the live registry data without requiring any manual intervention.

## Conclusion

The OpenSPP Change Request Add Farmer module is essential for systematically expanding farmer groups within OpenSPP, ensuring new members are added through a validated and fully documented process.