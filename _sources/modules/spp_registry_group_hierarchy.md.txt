# OpenSPP Registry Group Hierarchy

```{warning}

**Work in Progress**: This document is actively being developed and updated. Content may be incomplete or subject to change.
```

This module builds upon the existing OpenSPP group and membership management functionalities to introduce a hierarchical structure for groups. It allows groups to be nested within other groups, creating a parent-child relationship between them.  This hierarchy is beneficial for representing complex organizational structures within social protection programs or farmer registries. 

## Purpose

The **SPP Registry Group Hierarchy** module aims to:

* **Enable Group Nesting**: Allow groups to be members of other groups, creating a multi-level hierarchical structure.
* **Flexible Membership**:  Allow both individuals and groups to be members of a group, providing flexibility in representing different organizational models.
* **Enhanced Data Management**: Improve the organization and management of groups by providing a visual representation of the group hierarchy. 

## Dependencies and Integration

1. **OpenSPP Registry (**spp_registry**)**: Inherits core registry functionalities for managing registrant information, IDs, and relationships. 

2. **OpenSPP Registry (**spp_registry**)**: Leverages the group model to represent both parent and child groups within the hierarchy. 

3. **OpenSPP Registry (**spp_registry**)**: Uses the individual model to maintain individual memberships within groups, regardless of the group's position in the hierarchy. 

4. **OpenSPP Registry (**spp_registry**)**:  Extends the membership functionality to allow groups to be members of other groups, establishing the parent-child relationship.

## Additional Functionality 

* **Flexible Group Membership (`spp.group.role`)**:
    * Introduces a new field (`allow_all_member_type`) in the `spp.group.role` model.
    * This field allows administrators to define whether a specific group type can have both individual and group members.

* **Dynamic Individual Domain (`spp.group.membership`)**:
    * Modifies the individual selection field within the `spp.group.membership` model to dynamically adjust its options based on the group's type.
    * If a group type allows both individual and group members, the individual selection field will display all registrants (excluding the group itself to prevent circular relationships).
    * If a group type only allows individual members, the field will display only individuals.

* **Unified Member View (`spp.group.membership`)**:
    * Introduces a modified form view for `spp.group.membership`.
    * This view provides a unified interface for managing both individual and group memberships within a parent group.
    * It dynamically displays relevant information based on whether the member is an individual or another group.

* **Enhanced User Interface**:
    * Extends the group form view to visually represent the group hierarchy, allowing users to easily navigate between parent and child groups.
    * Provides clear indicators of a group's parent and child groups.

## Conclusion

The **SPP Registry Group Hierarchy** module adds significant value to OpenSPP by introducing the concept of nested groups. This allows for a more accurate and organized representation of complex structures commonly found in social protection programs and farmer cooperatives.  The module integrates seamlessly with existing OpenSPP components, providing a user-friendly experience for managing multi-level group structures. 
