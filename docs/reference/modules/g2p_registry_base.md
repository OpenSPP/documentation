---
review-status: needs-review
review-date: 2025-06-04
reviewer: migration-script
migration-notes: "Added during 2025 documentation reorganization"
---

# G2P Registry Base

```{warning}

**Work in Progress**: This document is actively being developed and updated. Content may be incomplete or subject to change.
```

This document outlines the functionality of the **G2P Registry: Base** module within the OpenSPP ecosystem. This module is the foundational layer upon which other OpenSPP registry modules are built.  It provides core features for managing registrant data, relationships, and identification, leaving specialized functionalities to dependent modules.

## Purpose

The **G2P Registry: Base** module aims to:

* Establish a standardized structure for storing and managing registrant data.
* Provide essential fields and functionalities common to various registry types.
* Enable flexible extension and customization through dependent modules.

## Module Dependencies and Integration

1. **Contacts (res.partner)**:  This module extends the Odoo Contacts functionality by adding fields specific to registrants, including:
    * **Registration Date**: Records the date a registrant was added to the system.
    * **Disabled**:  Flags a registrant as inactive, with optional reasons and timestamps for disabling and enabling.
    * **Registrant Type**: Differentiates between individuals and groups. 
    * **Tags**: Allows for flexible categorization of registrants using custom tags.

    By leveraging the existing Contacts module, the **G2P Registry: Base** module ensures seamless integration with other Odoo applications that utilize contact information.

2. **Web (web)**:  The **G2P Registry: Base** module uses the Web module to provide a user-friendly interface for managing registry data within the Odoo backend. 

3. **Portal (portal)**: The Portal module is utilized for potential future features, enabling secure access to registry data for external stakeholders (e.g., registrants themselves) through a dedicated online portal. 

## Additional Functionality

Beyond extending the Contacts module, the **G2P Registry: Base** module introduces:

* **Registrant IDs ([g2p.reg.id](g2p.reg.id))**: This feature allows multiple forms of identification to be associated with a single registrant, supporting a variety of ID types with customizable validation rules.
* **Phone Numbers ([g2p.phone.number](g2p.phone.number))**:  Manages multiple phone numbers per registrant, incorporating features for validation, disabling/enabling numbers, and storing the date each number was collected.
* **Registrant Relationships ([g2p.reg.rel](g2p.reg.rel))**: Establishes and tracks relationships between registrants (both individual-to-individual and individual-to-group), defining the type of relationship and allowing for date ranges and disabling/enabling of relationships.
* **Tags ([g2p.registrant.tags](g2p.registrant.tags))**: Provides a flexible tagging system to categorize and filter registrants based on specific criteria.
* **Districts ([g2p.district](g2p.district))**: Adds the capability to define and manage geographical districts, allowing for location-based organization of registrants. 

## Conclusion

The **G2P Registry: Base** module lays the groundwork for building robust and adaptable registries within OpenSPP. By focusing on core registry features and integrating seamlessly with essential Odoo modules, it provides a solid foundation for specialized registry applications. 
