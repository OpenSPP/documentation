# G2P Registry: Membership Module

This document outlines the **G2P Registry: Membership** module within the OpenSPP platform. This module focuses on managing memberships between individual registrants and registered groups.

### Purpose

The module's primary goal is to define and track the relationship between individuals and groups within the OpenSPP system. It allows for nuanced categorization of memberships and provides tools to monitor changes in group composition over time.

### Module Integration and Dependencies

* **[g2p_registry_individual](g2p_registry_individual)**:  This module utilizes the individual registrant model for linking memberships. It also extends the individual's form view to display group affiliations and provides direct access to manage these memberships. 
* **[g2p_registry_group](g2p_registry_group)**: The membership module seamlessly integrates with the group registrant model.  It extends the group form view with a dedicated "Members" tab to manage individuals associated with the group. This tab facilitates a comprehensive overview of membership roles and durations.
* **Contacts (res.partner)**: This module leverages the standard Odoo Contacts module to streamline navigation and access to detailed information for both individual and group registrants linked to a membership. 
* **Queue Job (queue_job)**: The module utilizes the Queue Job module to enhance performance. It delegates the computation of group indicators to background jobs, ensuring that long-running calculations do not disrupt user experience.

### Additional Functionality

1. **Group Membership Model (g2p.group.membership)**:
    * This core model stores all membership data. 
    * **Key fields include**:
        * **Group:** (Required, Many-to-one) Defines the specific group the individual is a member of.
        * **Individual:** (Required, Many-to-one) Identifies the individual member.
        * **Kind:** (Many-to-many) Categorizes the nature of the membership (e.g., "Head of Household," "Dependent").
        * **Start Date:** (Datetime) Records the membership's commencement date.
        * **End Date:** (Datetime, Optional)  Marks the membership's termination date.

2. **Membership Kinds (g2p.group.membership.kind)**:
    * Defines and manages various roles or types of memberships.
    * Allows administrators to enforce uniqueness within a group for specific kinds (e.g., only one "Head of Household" per group).

3. **Data Validation**:
    * Prevents redundant memberships (same individual in the same group).
    * Enforces chronological consistency, ensuring the end date is not before the start date.
    * Restricts the creation of multiple memberships with the same unique "kind" within a group.

4. **User Interface Enhancements**:
    * Adds user-friendly buttons on individual and group forms for direct access and management of associated memberships.
    * Provides a dedicated tree view to list and filter group memberships, enhancing data accessibility and management.

### Conclusion

The **G2P Registry: Membership** module is essential for managing and tracking individuals within groups, crucial for social protection programs and farmer registries. It delivers a flexible, robust system to define, categorize, and track memberships, ensuring data integrity. This, in turn, facilitates comprehensive analysis of group composition and dynamics within the OpenSPP ecosystem. 
