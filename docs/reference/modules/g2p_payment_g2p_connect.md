# G2P Payment G2P Connect

This module integrates OpenSPP with external payment systems using the G2P Connect standard. It automates the secure transfer of payment instructions and status updates, streamlining digital benefit disbursements to beneficiaries.

## Purpose

The G2P Payment G2P Connect module provides a critical bridge for OpenSPP to interact with external digital payment providers, enabling efficient and reliable benefit delivery. It accomplishes the following:

*   **Facilitates Direct Integration with External Payment Systems:** Connects OpenSPP to various Financial Service Providers (FSPs) or payment gateways that adhere to the G2P Connect protocol. This enables seamless digital disbursement of benefits, crucial for reaching beneficiaries quickly and securely.
*   **Offers Flexible Payee Identification:** Supports multiple methods for identifying beneficiaries for payment, such as bank account numbers, IBANs, phone numbers, email addresses, or specific registrant IDs. This ensures payments reach the correct individuals through their preferred or available channels.
*   **Automates Payment Batches and Status Tracking:** Automatically groups payments into batches and initiates their transfer to the external payment system. It then continuously monitors and updates the status of these payments (e.g., paid, failed) within OpenSPP, providing real-time visibility into disbursement progress.
*   **Ensures Secure and Traceable Transactions:** Formats payment data according to the G2P Connect standard, incorporating security elements like digital signatures. This ensures secure communication and provides a clear audit trail for each transaction, which is critical for accountability in social protection programs.
*   **Provides Configurable Payment Endpoints:** Allows administrators to define specific API endpoints for sending payments and retrieving status updates. This offers flexibility to integrate with various G2P Connect-compliant systems and adapt to different country or program requirements.

## Dependencies and Integration

The G2P Payment G2P Connect module extends and integrates with several core OpenSPP modules to deliver its functionality:

*   **Base (`base`)**: This module relies on fundamental OpenSPP functionalities, extending core system capabilities to manage payment connections and configurations.
*   **G2P Registry Membership (`g2p_registry_membership`)**: It utilizes information about group memberships to accurately identify the correct individual (e.g., the head of a household) when payments are targeted at a group. This ensures that funds are directed to the appropriate beneficiary within a household or collective.
*   **G2P Programs (`g2p_programs`)**: This module serves as a specific implementation of a payment manager within the G2P Programs framework. It extends program management capabilities by providing the mechanism to actually disburse payments defined within a program's cycles and entitlements.
*   **G2P Payment Files (`g2p_payment_files`)**: By inheriting from `g2p.program.payment.manager.file`, this module leverages the foundational structure for managing payment-related configurations and batch processing, although its primary role is direct API integration rather than file generation.

## Additional Functionality

The G2P Payment G2P Connect module provides robust features for managing digital payment integrations:

### Configurable Payee Identification
Users can select the primary identifier for beneficiaries, such as "Bank Account Number," "IBAN," "Phone," "Email," or a specific "Registrant ID Type." This flexibility accommodates diverse financial inclusion landscapes and beneficiary preferences. The system automatically formats the selected identifier with appropriate prefixes (e.g., `phone:`) for consistent communication with the external payment system. When a registrant is part of a group, the module intelligently identifies the designated group head (e.g., Head of Household) to ensure payments are directed to the appropriate individual within the household or group.

### Automated Payment Processing and Status Monitoring
The module can automatically group pending payments into batches and initiate their transfer to the configured Payment Endpoint URL. This streamlines the disbursement process, reducing manual intervention. Upon sending payments, an automated background task (cron job) is created to regularly query the Status Endpoint URL for updates on each payment's progress. Payment statuses (e.g., "paid," "failed") are automatically updated in OpenSPP, providing real-time reconciliation and reducing manual tracking efforts.

### Secure API Communication and Error Handling
Payments are sent via secure API calls to external G2P Connect-compliant systems, including necessary authentication and message formatting (e.g., digital signatures). The system monitors API responses and logs any communication errors or failures during the disbursement or status check processes. These errors are recorded and made visible to administrators for investigation and resolution. Administrators can define a "Filter Batches to Send" rule using OpenSPP's domain syntax to control which specific payment batches are eligible for automated sending, ensuring targeted disbursements.

### Customizable Connection Settings
Administrators define the specific "Payment Endpoint URL" and "Status Endpoint URL" for integration with their chosen external payment provider. An "API Timeout" can be set to manage the duration the system waits for a response from the external payment system, preventing indefinite hangs and improving system responsiveness. A "Locale" setting ensures that payment communications are sent with the appropriate language and regional context, supporting multilingual operations.

## Conclusion

The G2P Payment G2P Connect module is a critical component for enabling secure, automated, and traceable digital payment disbursements to beneficiaries through external G2P Connect-compliant payment systems within OpenSPP.