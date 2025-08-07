---
review-status: needs-review
review-date: 2025-06-04
reviewer: migration-script
migration-notes: "Added during 2025 documentation reorganization"
---

# G2P Registry Membership

```{warning}

**Work in Progress**: This document is actively being developed and updated. Content may be incomplete or subject to change.
```

This document outlines the functionality of the **G2P Registry: Membership** module within the OpenSPP ecosystem. This module focuses on managing relationships between individual registrants and groups, adding an essential layer of organization and data management to the platform.

## Purpose

The **G2P Registry: Membership** module aims to:

* **Define Relationships:** Introduce different types of relationships (or roles) that individuals can have within groups (e.g., Head of Household, Member, Dependent).
* **Track Group Members:** Enable the system to associate individual registrants with specific groups.
* **Manage Membership Timeframes:**  Record start and end dates for each membership, allowing for accurate historical tracking of group composition over time.

## Module Dependencies and Integration

1. **G2P Registry: Individual ([g2p_registry_individual](g2p_registry_individual))**: This module relies on the individual registrant data managed by the **G2P Registry: Individual** module.  It directly links individuals to groups, leveraging the individual profiles created and managed within that module.

2. **G2P Registry: Group ([g2p_registry_group](g2p_registry_group))**: It integrates closely with the group management capabilities provided by the **G2P Registry: Group** module.  It uses the group definitions and data structures from this module to establish and track membership.

3. **Contacts (res.partner)**: Leverages the Odoo Contacts module to access and display information about individuals and groups within the membership management interface.

## Additional Functionality

The module introduces the following key elements:

* **Group Membership Model (g2p.group.membership):** 
    * Stores data about individual memberships in groups, including the group, the individual member, the type of relationship, start date, and optional end date.
    * Includes computed fields for status (active/inactive) and a flag to indicate if the membership has ended.
    * Provides methods to directly open the linked individual or group forms for easy navigation and data viewing.

* **Group Membership Kind Model (g2p.group.membership.kind):**
    * Allows administrators to define and manage different types of relationships within groups (e.g., Head of Household, Member, Dependent).
    * Includes an option to mark a kind as "unique," enforcing that only one member within a group can have this relationship type. 

* **Data Validation and Constraints:**
    * Implements validation rules to prevent duplicate memberships (the same individual cannot be added to the same group twice with the same relationship).
    * Includes logic to ensure the end date of a membership cannot be earlier than the start date.

* **User Interface Enhancements:**
    * Adds dedicated tabs or sections within both the Individual and Group forms to display and manage memberships. 
    * Provides views (tree, form) to manage group memberships directly.

## Conclusion

The **G2P Registry: Membership** module is crucial for representing and managing the complex relationships between individuals and groups within OpenSPP. It integrates seamlessly with other core registry modules, providing a comprehensive system for tracking group composition, roles within groups, and membership history.  This functionality is essential for social protection programs and farmer registries that rely on accurate and up-to-date information about individuals' group affiliations. 
