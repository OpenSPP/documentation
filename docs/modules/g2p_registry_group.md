# G2P Registry Groups

```{warning}

**Work in Progress**: This document is actively being developed and updated. Content may be incomplete or subject to change.
```

This document describes the **G2P Registry: Groups** module within the OpenSPP framework. This module builds upon the **G2P Registry: Base** module to provide specific functionality for managing groups of registrants.

### Purpose

The **G2P Registry: Groups** module focuses on:

* **Defining Group Types**:  Allows administrators to create and manage different categories of groups (e.g., households, cooperatives, farmer groups).
* **Representing Groups as Registrants**: Extends the concept of a "registrant" from the **G2P Registry: Base** module to include groups, enabling groups to be managed alongside individual registrants.
* **Categorizing Groups**:  Associates each group with a specific group type, providing structure and context to group data. 

### Dependencies and Integration

1. **[g2p_registry_base](g2p_registry_base)**: This module inherits directly from the **G2P Registry: Base** module, leveraging its core features for managing registrant information, IDs, relationships, and more. This inheritance model ensures that groups can be managed using the same tools and workflows as individual registrants, providing a consistent user experience.

2. **Contacts (res.partner)**:  Similar to the **G2P Registry: Base** module, this module utilizes the Odoo Contacts module to represent groups as entities.  The group-specific functionalities are added as extensions to the existing contact model.

### Additional Functionality

* **Group Kinds ([g2p.group.kind](g2p.group.kind))**:
    * Introduces a new model to define and manage different types of groups within the system.
    * Enforces unique naming to avoid duplication.

* **Group Representation**:
    * Leverages the `res.partner` model (inherited from **Contacts**) to represent groups as entities.
    * Adds a dedicated field (`kind`) to link each group to its designated group type.

### Conclusion

The **G2P Registry: Groups** module enhances the OpenSPP platform by providing a structured way to manage groups of registrants.  It integrates seamlessly with the **G2P Registry: Base** module, maintaining consistency in data management and user experience. This module is essential for social protection programs and farmer registries where group-level management is crucial. 
