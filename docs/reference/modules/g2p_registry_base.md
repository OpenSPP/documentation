---
orphan: true
---

# G2P Registry Base

The `g2p_registry_base` module establishes the foundational framework for managing individuals and groups within OpenSPP. It provides the core data models and essential functionalities required for any social protection program or farmer registry to operate effectively.

## Purpose

This module forms the bedrock for all G2P operations, ensuring accurate, structured, and manageable information about beneficiaries and their connections. It accomplishes this by:

*   **Comprehensive Registrant Profiles:** Captures and maintains detailed information for individuals and groups, including demographic data (e.g., civil status, occupation, income), contact details, and their active status within programs.
*   **Unique Identification Management:** Supports the creation of various ID types (e.g., National ID, Passport) with configurable validation rules, ensuring data accuracy and preventing duplicate records.
*   **Relationship Tracking:** Establishes and manages complex relationships between registrants (e.g., family members, group affiliations) with defined types, inverse relationships, and specific timeframes.
*   **Geographic Area Classification:** Organizes registrants within a hierarchical geographic structure, enabling granular reporting and targeted program delivery at levels such as country > province > district.
*   **Robust Data Integrity:** Implements strong validation rules for critical data points like phone numbers, identification values, and dates, thereby maintaining high data quality across the system.

## Dependencies and Integration

The `g2p_registry_base` module builds upon core OpenSPP functionalities and integrates seamlessly with other modules to provide a holistic registry solution. It extends the standard `res.partner` model, transforming it into a comprehensive registrant profile.

This module primarily depends on the `contacts` module, which provides the underlying contact management framework that `g2p_registry_base` enhances for registrant-specific needs. It also utilizes the `portal` module to enable secure access for registrants to view their information and interact with the system.

Serving as a foundational component, `g2p_registry_base` provides the essential data models and business logic for managing individuals and groups, their IDs, phone numbers, and relationships. This makes it a critical dependency for other G2P modules, such as [G2P Registry Individual](g2p_registry_individual) and [G2P Registry Group](g2p_registry_group), which further specialize in managing specific types of registrants.

## Additional Functionality

### Registrant Lifecycle and Demographic Management

The module enables comprehensive management of registrant profiles throughout their lifecycle. Users can disable or enable registrant records, along with recording a detailed reason and date for such changes, supporting various program statuses. It tracks essential information such as the registrant's registration date and includes key demographic fields like civil status, occupation, and income.

```{note}
The system prevents negative income values, automatically flagging and correcting them to zero to maintain data consistency. Specific user roles, such as registrars, have restricted permissions for deleting records to ensure data integrity and prevent unauthorized data loss.
```

### Identity and Contact Information

This module provides robust tools for managing registrant identities and contact details. It supports the creation of various ID types, allowing administrators to define custom validation rules using regular expressions to ensure the format and validity of entered ID numbers. Each registrant can hold multiple IDs, but each ID type must be unique per registrant. Additionally, the module manages multiple phone numbers for each registrant, offering features for sanitizing numbers to a standard format (e.g., E.164) and applying custom regex validations. Phone numbers can also be individually disabled or enabled as needed.

### Relationship Tracking

Users can define and manage diverse relationships between registrants, such as "Parent of" or "Spouse," allowing for a comprehensive view of social structures. Each relationship type can have an inverse name (e.g., "Child of") and be designated as bidirectional. Relationships can be established with specific start and end dates, facilitating the historical tracking and management of evolving connections. The system includes validations to prevent the creation of duplicate or overlapping active relationships between the same two registrants.

### Geographic and Categorization Features

The module includes features for categorizing registrants by geographic districts, linking them to specific states or provinces within a country's administrative structure. This capability is crucial for enabling granular reporting, targeted program interventions, and localized service delivery. Furthermore, registrants can be assigned multiple custom tags, allowing for flexible categorization and filtering based on program-specific criteria, such as "Vulnerable," "Displaced," or "Program X Beneficiary."

## Conclusion

The `g2p_registry_base` module is the essential foundation of OpenSPP, providing the core capabilities for managing comprehensive registrant data, identities, relationships, and geographic classifications crucial for effective social protection programs.