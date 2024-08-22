# g2p_payment_g2p_connect Module

```{warning}

**Work in Progress**: This document is actively being developed and updated. Content may be incomplete or subject to change.
```

This module extends the OpenSPP's payment management capabilities by integrating with the G2P Connect standard. It provides a dedicated payment manager for handling disbursements and status checks through G2P Connect-compliant APIs.

## Purpose

The `g2p_payment_g2p_connect` module enables seamless integration with financial service providers (FSPs) that adhere to the G2P Connect standard. It facilitates the secure and efficient transfer of funds to beneficiaries enrolled in social protection programs.

## Functionality

- **G2P Connect Payment Manager:** A specialized payment manager (`g2p.program.payment.manager.g2p.connect`) handles G2P Connect-specific configurations, including:
    - Payment and status endpoint URLs
    - Payee ID type and format
    - API timeout and security settings
- **Automated Batch Processing:** Automatically creates and sends payment batches to the specified G2P Connect endpoint.
- **Status Check Cron Job:**  Periodically queries the G2P Connect status endpoint to update payment statuses within OpenSPP.
- **Payee ID Flexibility:**  Supports various payee identification methods like bank account numbers, IBANs, phone numbers, email addresses, and registrant IDs.
- **Integration with Payment Files:** Leverages the existing [g2p_payment_files](g2p_payment_files) module for generating and managing payment files.
- **Configurable Payment Domain:** Allows users to define a domain filter to select specific payment batches for sending through G2P Connect.

## Integration with Other Modules

This module extends the functionality of the following modules:

- **[g2p_registry_membership](g2p_registry_membership):** Retrieves beneficiary information and group head details for payment processing.
- **[g2p_programs](g2p_programs):**  Associates G2P Connect payment managers with specific social protection programs.
- **[g2p_payment_files](g2p_payment_files):**  Inherits functionalities for payment file configuration and management. 

## Benefits

- **Standardized Integration:**  Streamlines the connection with G2P Connect-compliant FSPs, reducing integration efforts.
- **Automated Disbursements:**  Enables efficient and timely payment processing through automated batch creation and transmission.
- **Real-time Status Updates:**  Provides up-to-date payment statuses within OpenSPP, allowing for timely reconciliation and issue resolution.
- **Enhanced Transparency and Accountability:**  Ensures secure and traceable fund transfers, promoting transparency and accountability in DCI programs. 
