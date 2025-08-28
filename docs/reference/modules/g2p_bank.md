# G2P Bank

The **G2P Bank** module provides essential functionality for managing bank account details within the OpenSPP platform. It ensures that accurate and standardized financial information is captured and maintained for both individual and group registrants, facilitating secure and efficient payment disbursements.

## Purpose

The **G2P Bank** module is designed to streamline the management of registrant bank account information, primarily focusing on International Bank Account Numbers (IBANs). It accomplishes the following key objectives:

*   **Standardizes Bank Account Data**: Ensures all bank account details, especially IBANs, adhere to international formats for consistency across the system.
*   **Automates IBAN Handling**: Automatically generates or validates IBANs based on provided bank and account details, reducing manual entry errors.
*   **Integrates with Registrant Profiles**: Directly links bank accounts to the respective individual or group registrant profiles, providing a comprehensive financial record.
*   **Facilitates Secure Disbursements**: Provides reliable and validated banking information crucial for the accurate and timely transfer of funds in social protection programs.
*   **Supports Payment Processing**: Offers the foundational data required by payment modules for successful financial transactions to beneficiaries.

This module ensures that programs can confidently manage and use bank details for various financial operations, from cash transfers to direct deposits, minimizing processing delays and errors.

## Dependencies and Integration

The **G2P Bank** module seamlessly integrates with core OpenSPP components and extends standard Odoo functionality:

*   **[Contacts](contacts)**: This module extends the standard Odoo `res.partner.bank` model, which is inherently linked to the `res.partner` model (managed by the `contacts` module). This allows bank accounts to be directly associated with any contact, including registrants.
*   **[G2P Registry Individual](g2p_registry_individual)**: It enables the association of bank account details with individual registrants, ensuring that personal payment information is linked to their profile.
*   **[G2P Registry Groups](g2p_registry_group)**: It allows for bank accounts to be assigned to group registrants (e.g., households, cooperatives), supporting payments made to collective entities.

By leveraging these dependencies, the `g2p_bank` module ensures that bank account information is an integral part of both individual and group registrant records, providing a unified view of beneficiary data.

## Additional Functionality

The module focuses on robust and accurate management of bank account information:

*   **Bank Account Recording**: Users can record and manage multiple bank accounts for each individual or group registrant. This includes capturing the bank's country, BIC/SWIFT code, and the specific account number.
*   **Automated IBAN Generation and Validation**: A core feature is the automatic computation and validation of the International Bank Account Number (IBAN). When the bank's country, BIC, and account number are provided, the system generates a compliant IBAN, or validates an existing one, ensuring adherence to international banking standards and significantly reducing potential payment errors.
*   **Direct Linkage to Registrants**: Each bank account record is directly tied to a specific individual or group registrant. This clear association is vital for ensuring that payments are directed to the correct beneficiary and simplifies financial reconciliation.

## Conclusion

The **G2P Bank** module is fundamental to OpenSPP's financial operations, providing a standardized and reliable system for managing bank account details essential for accurate and secure payment disbursements to beneficiaries.