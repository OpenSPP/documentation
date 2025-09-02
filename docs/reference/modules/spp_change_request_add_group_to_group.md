---
orphan: true
---

# Change Request: Add Group to a Group

The 'spp_change_request_add_group_to_group' module provides a structured workflow for establishing hierarchical relationships between groups within the OpenSPP registry. It enables the formal process of adding existing groups as members to other existing parent groups, supporting complex organizational structures.

## Purpose

This module accomplishes the following key objectives:

*   **Establish Group Hierarchies**: Enables the creation of nested group structures by allowing existing groups to be added as members to a designated parent group (e.g., adding a "Village Youth Group" to a "District Community Council").
*   **Streamline Group Membership Changes**: Provides a formal, auditable workflow for modifying group compositions, ensuring all additions are properly documented and approved through a change request process.
*   **Enhance Organizational Structure**: Facilitates the representation of complex organizational relationships within the registry, improving data clarity and management for social protection programs and farmer registries.
*   **Ensure Data Integrity**: Implements validation steps to prevent incorrect or duplicate group memberships, maintaining the accuracy and consistency of the group registry.
*   **Support Evidence Collection**: Allows for the attachment of supporting documents (e.g., meeting minutes, official requests) to each change request, providing a comprehensive audit trail.

## Dependencies and Integration

This module works in conjunction with several other OpenSPP components to deliver its functionality:

*   **[OpenSPP Change Request](spp_change_request)**: This is the foundational module that provides the overarching framework for all change requests, including stages, approvals, and general management. This module extends `spp_change_request` to define a specific type of change for adding groups to groups.
*   **[G2P Registry Groups](g2p_registry_group)**: It leverages this module for the core management and definition of groups within the system. Both the parent group and the member groups are managed by `g2p_registry_group`.
*   **[G2P Registry Membership](g2p_registry_membership)**: This module is critical as it handles the actual creation of membership records. Upon approval, `spp_change_request_add_group_to_group` utilizes `g2p_registry_membership` to formalize the link between a parent group and its new member group.
*   **[OpenSPP Registry Group Hierarchy](spp_registry_group_hierarchy)**: This module enables the very concept of groups being members of other groups. `spp_change_request_add_group_to_group` provides the specific change request mechanism to implement and manage these hierarchical relationships.

## Additional Functionality

The module introduces specialized features to manage the addition of groups to groups efficiently:

*   **Controlled Group Selection**: Users begin by selecting the existing *parent group* to which new *member groups* will be added. The system provides a filtered list, ensuring that only valid, existing groups can be chosen as the parent, preventing incorrect associations.
*   **Adding Member Groups**: Users can then add one or more existing groups as members to the selected parent group. The system intelligently filters the available options, presenting only groups that are not already members of the target parent group, thus preventing duplicate memberships.
*   **Defining Membership Roles**: For each member group being added, users must specify its `kind` or role within the parent group (e.g., "Affiliate Organization," "Sub-committee," "Local Chapter"). This allows for detailed classification and understanding of the relationship between the parent and member groups.
*   **Documentation and Validation**: The module integrates with the Document Management System (DMS) to allow attaching relevant files and directories as evidence for the change request, such as official resolutions or application forms. Before submission, the system validates that at least one member group has been specified for addition, ensuring meaningful requests.
*   **Automated Membership Creation**: Upon successful approval of the change request through the standard OpenSPP change request workflow, the system automatically creates the necessary group membership records. This action formally establishes the hierarchical link between the parent and member groups within the registry.
*   **Direct Group Details Access**: A convenient feature allows users to directly open a read-only form view of the selected parent group's details. This provides quick access to contextual information without leaving the change request form.

## Conclusion

The 'spp_change_request_add_group_to_group' module is essential for managing complex group structures within OpenSPP, providing a formal and auditable process for building and maintaining hierarchical relationships between groups in social protection programs and farmer registries.