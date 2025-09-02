---
orphan: true
---

# OpenG2P Program Payment (Payment Hub EE)

This module integrates OpenSPP with the Payment Hub EE (PHEE), an external payment processing system. It enables OpenSPP to efficiently manage and disburse payments for social protection programs by automating the creation, preparation, and secure transmission of payment instructions to the PHEE.

## Purpose

The G2P Payment Phee module streamlines the process of disbursing funds to beneficiaries for social protection programs. It ensures secure and scalable payment operations by:

*   **Integrating with External Payment Hubs:** Connects OpenSPP to the Payment Hub EE for bulk payment processing, acting as a bridge for financial transactions.
*   **Automating Payment Batch Creation:** Automatically groups approved entitlements into manageable payment batches, reducing manual effort and potential errors.
*   **Configuring Flexible Payee Identification:** Allows administrators to define how beneficiaries are identified for payments, supporting various identifiers like bank account numbers, phone numbers, or registrant IDs.
*   **Securing API Communication:** Provides robust configuration options for API endpoints and authentication parameters to ensure secure and reliable data exchange with the external payment hub.
*   **Generating Payment Files:** Creates structured CSV files containing all necessary payment details for each batch, ready for transmission or manual review.

## Dependencies and Integration

This module extends core OpenSPP functionalities to facilitate external payment processing.

*   **`base`**: As a foundational Odoo module, `base` provides essential technical structures and features required for the module's operation.
*   **`g2p_registry_base`**: This module relies on `g2p_registry_base` for access to fundamental registrant data, including bank accounts, phone numbers, email addresses, and various identification types, which are crucial for correctly identifying payees.
*   **`g2p_programs`**: The `g2p_payment_phee` module extends the payment management capabilities defined within `g2p_programs`. It adds "Payment Hub EE" as a specific payment manager option, allowing program administrators to select and configure PHEE for payment cycles. It leverages program cycles, approved entitlements, and existing payment records from `g2p_programs` to initiate and track disbursements.

## Additional Functionality

The G2P Payment Phee module provides comprehensive features for managing the entire payment disbursement workflow with the Payment Hub EE.

### Payment Hub EE Integration Setup

Users configure the necessary endpoints and authentication details to establish secure communication with the Payment Hub EE. This includes setting the Authentication, Payment, Status, and Details Endpoint URLs, along with authentication parameters such as Tenant ID, Username, Password, Grant Type, and Authorization credentials. This setup ensures that OpenSPP can securely authenticate and interact with the external payment system.

### Automated Payment Batch Management

The module automates the process of organizing approved entitlements into payment batches. Users can enable an option to "Automatically Create Batch" and define a `Max Batch Size` (e.g., 500 payments per batch). During the payment preparation phase, the system generates individual `g2p.payment` records from approved entitlements and groups them into `g2p.payment.batch` records according to the specified size.

### Flexible Payee Identification

OpenSPP allows for flexible configuration of how beneficiaries are identified for payments sent to the PHEE. Administrators can select a `Payee ID Field` from options like Bank Account Number, IBAN, Phone, Email, or Registrant ID. For Registrant ID, a specific `Payee DFSP ID Type` (e.g., National ID) can be chosen, ensuring the correct identifier is extracted from the beneficiary's profile.

### Payment Transaction Parameters

Users define various parameters that govern how payment transactions are structured and sent. This includes specifying the `Payment Mode` (e.g., 'IMMEDIATE'), the `Payer ID Type`, and the `Payer ID` that the Payment Hub EE will use to identify the sender. Additionally, `Batch Transaction Type Header` and `Batch Transaction Purpose Header` (e.g., "G2P Payment") can be set, along with a `Filename Prefix` for generated CSV files and a `Batch Request Timeout` for API calls.

### Payment Preparation and Sending

The module manages the lifecycle of payments, from preparation to transmission. The `prepare_payments` function creates payment records from approved entitlements and can optionally generate CSV files for each batch as attachments. The `send_payments` function then securely transmits these prepared payment batches to the configured Payment Hub EE API. This process updates the status of individual payments and batches, providing visibility into the disbursement process.

## Conclusion

The G2P Payment Phee module is essential for OpenSPP, enabling secure and efficient bulk payment disbursements for social protection programs through seamless integration with the Payment Hub EE.