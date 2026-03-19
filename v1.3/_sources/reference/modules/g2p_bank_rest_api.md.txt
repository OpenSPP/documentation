---
orphan: true
---

# G2P Bank Rest Api

The `g2p_bank_rest_api` module extends OpenSPP's RESTful API capabilities, allowing external systems to seamlessly interact with and manage bank account details for individuals and groups registered within the platform. It provides the necessary endpoints for creating, updating, and retrieving registrant bank information programmatically.

## Purpose

This module is essential for enabling automated financial processes and data exchange by exposing registrant bank details through a standardized API. It accomplishes the following:

*   **Exposes Bank Account Data**: Makes bank account numbers and associated bank information for registrants accessible to external systems via a secure API.
*   **Enables Programmatic Updates**: Allows external applications to create or update bank details for individuals and groups, integrating financial data directly into the registry.
*   **Facilitates Financial Disbursements**: Provides the necessary data integration layer for connecting OpenSPP with payment gateways or financial service providers to process G2P (Government-to-Person) payments.
*   **Streamlines Registrant Onboarding**: Integrates bank detail submission into the broader registrant enrollment process, allowing for comprehensive profile creation through a single API interaction.
*   **Ensures Data Consistency**: When bank details are submitted, the module automatically manages the creation or linking of bank records within OpenSPP, maintaining data integrity.

## Dependencies and Integration

The `g2p_bank_rest_api` module builds upon and integrates with core OpenSPP components to deliver its functionality:

*   **[G2P Registry: Rest API Module](g2p_registry_rest_api)**: This module extends the existing REST API framework provided by `g2p_registry_rest_api`. It adds the specific logic to handle bank account information when individual or group registrant data is sent or received through the API.
*   **[G2P Bank Module](g2p_bank)**: It relies on the data models and business logic established by the `g2p_bank` module for managing bank details. When bank information is submitted via the API, `g2p_bank_rest_api` uses `g2p_bank`'s capabilities to correctly store and link these details to the respective individual or group.

This module primarily serves external systems and integrations by providing a structured interface to interact with registrant bank data, which is foundational for any financially oriented social protection program.

## Additional Functionality

### Automated Bank Detail Processing via API

This module allows external systems to submit bank account information (such as bank name and account number) as part of the data payload when creating or updating individual or group registrants. OpenSPP automatically processes this information, creating new bank records if a bank name is unrecognized and linking the account number to the specified registrant. This capability simplifies the comprehensive registration of beneficiaries, including their financial information, through a single API call.

### Seamless Integration with Registrant Data

The `g2p_bank_rest_api` module ensures that bank details are treated as an integral part of an individual's or group's profile within the OpenSPP registry. When external systems query registrant data, the associated bank accounts can be included, providing a holistic view of the beneficiary. This unified approach prevents data silos and enhances the utility of the registrant information for various program functions.

### Support for Financial Transactions

By providing a robust API for managing bank details, this module lays the groundwork for critical financial operations. It enables the platform to store and retrieve the necessary bank account information for processing G2P payments, managing financial aid disbursements, or integrating with mobile money providers. This is crucial for programs requiring direct financial transfers to beneficiaries.

## Conclusion

The `g2p_bank_rest_api` module is critical for OpenSPP's interoperability, enabling external systems to manage and integrate bank account details for registrants efficiently. It underpins automated financial processes and enhances the platform's capacity to support G2P payment programs.