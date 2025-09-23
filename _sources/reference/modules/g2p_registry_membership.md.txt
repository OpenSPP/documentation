---
orphan: true
---

# G2P Registry: Membership

The G2P Registry Membership module defines and manages the relationships between individuals and groups within OpenSPP. It provides the framework for assigning individuals to various groups, specifying their roles, and tracking their membership over time, ensuring accurate and up-to-date group composition data.

## Purpose

This module enables OpenSPP to effectively manage the dynamic structure of beneficiaries within social protection programs and farmer registries. It accomplishes this by:

*   **Defining Membership Roles**: Allows administrators to establish various roles (e.g., "Head of Household," "Family Member," "Cooperative Lead") that individuals can hold within a group. This provides clear categorization of responsibilities and relationships.
*   **Assigning Individuals to Groups**: Facilitates the process of linking individual registrants to specific groups, such as households, community associations, or farmer cooperatives.
*   **Tracking Membership Lifecycle**: Records the start and end dates of an individual's membership in a group, providing a historical record and enabling the system to determine active and inactive members.
*   **Ensuring Data Integrity**: Enforces rules to prevent duplicate individual entries within a group and validates that unique roles (like "Head of Household") are assigned to only one individual per group.
*   **Providing Group Composition Insights**: Automatically calculates and displays the total number of individuals associated with each group, offering a quick overview of group size.

This module is crucial for programs that require a clear understanding of who belongs to which group, enabling targeted interventions and accurate reporting at both individual and group levels. For example, it helps identify all members of a household for benefit distribution or list all individuals associated with a specific farmer cooperative.

## Dependencies and Integration

The G2P Registry Membership module integrates closely with other core OpenSPP components to manage comprehensive registrant data:

*   **[G2P Registry Groups](g2p_registry_group)**: This module builds directly upon the G2P Registry Groups module, which defines groups as registrants. It allows for the assignment of individuals *to* these established groups.
*   **[G2P Registry Individual](g2p_registry_individual)**: It relies on the G2P Registry Individual module, which manages individual registrant profiles. This module links these individual profiles as members *within* groups.
*   **Contacts (res.partner)**: Both individuals and groups are represented as `res.partner` records (contacts) in OpenSPP. This module establishes the membership links between these contact records.
*   **Queue Job (queue_job)**: This module utilizes the queue job system to efficiently recompute group-level indicators, such as the total number of members, in the background. This ensures that group statistics remain up-to-date without impacting user performance.

This module is foundational, providing the essential structure for understanding how individuals are organized into social units. Other modules can leverage its data to filter beneficiaries by group, understand household composition, or report on group-level demographics.

## Additional Functionality

### Flexible Membership Kinds
Users can define various types of membership roles, such as "Head of Household," "Spouse," "Child," or "Dependent." For specific roles, the system allows configuration to ensure that only one individual can hold that unique role within a given group (e.g., only one "Head of Household"). This flexibility supports diverse program requirements and social structures.

### Membership Lifecycle and Status
The module captures the start and, optionally, the end date of an individual's membership in a group. Based on these dates, the system automatically determines if a membership is currently "active" or "inactive." This provides a clear historical record of affiliations and ensures that only current members are considered for active program participation.

### Automated Group Composition and Validation
The module automatically calculates and displays the "Number of individuals" within each group, providing an immediate overview of its size. It enforces crucial data integrity rules, preventing an individual from being listed as a member of the same group multiple times and validating that unique roles are respected across all group members.

### Seamless Data Navigation
From any group membership record, users can easily navigate to view the full profile of the individual member or the details of the associated group. This feature enhances usability by providing direct access to related information, streamlining data review and management workflows.

## Conclusion

The G2P Registry Membership module is vital for accurately modeling the social structures of beneficiaries, enabling OpenSPP to manage individuals within their relevant group contexts for effective program delivery and comprehensive reporting.