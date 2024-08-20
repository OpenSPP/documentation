# G2P Bank Module

```{warning}

**Work in Progress**: This document is actively being developed and updated. Content may be incomplete or subject to change.
```

This document outlines the functionality of the **G2P Bank** module within the OpenSPP framework. This module extends the functionality of individual and group registries to manage their bank details.

### Purpose

The **G2P Bank** module aims to:

* Provide an interface for storing and managing bank account information for both individual and group registrants within the OpenSPP system.
* Ensure data consistency and accuracy by calculating and displaying IBANs based on provided bank details.
* Integrate seamlessly with existing individual and group registry views to provide a consolidated view of registrant information.

### Module Dependencies and Integration

1. **Contacts (res.partner)**: This module directly leverages the Odoo Contacts module and its inherent bank account management features (`res.partner.bank`). This ensures consistency and avoids data redundancy by utilizing the existing framework for storing bank information.

2. **[g2p_registry_individual](g2p_registry_individual)**: This module integrates with the individual registry by extending the individual registrant view to include a dedicated page for managing bank details. This allows users to easily view and manage bank information associated with individual registrants.

3. **[g2p_registry_group](g2p_registry_group)**:  Similar to its integration with the individual registry, this module extends the group registrant view to include a bank details management section. This facilitates the tracking of bank accounts associated with groups, such as cooperatives or farmer groups.

### Additional Functionality

* **IBAN Calculation**: The module automatically calculates and displays the International Bank Account Number (IBAN) based on the entered bank account number and bank details. This feature leverages the `schwifty` Python library for accurate IBAN generation, ensuring data consistency and reducing manual errors. 

* **Integrated Bank Details Views**:  The module seamlessly integrates bank details management into both the individual and group registry views.  This provides a unified and centralized location for managing all aspects of a registrant's profile, including their bank information.

### Conclusion

The **G2P Registry: Bank Details** module enhances OpenSPP by providing a structured and efficient way to manage bank account information for both individual and group registrants.  Its tight integration with existing core modules ensures data consistency, simplifies data entry, and improves the overall user experience for managing registrant information within the platform. 
