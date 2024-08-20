# g2p_payment_simple_mpesa

```{warning}

**Work in Progress**: This document is actively being developed and updated. Content may be incomplete or subject to change.
```

## Overview

The `g2p_payment_simple_mpesa` module provides a simple interface to manage payments for social protection programs using the Mpesa mobile money platform. 

This module builds upon the existing payment manager framework provided by the [g2p_programs](g2p_programs) module and extends it with Mpesa specific functionality.

## Functionality

The module allows program managers to:

* Configure connection details to an Mpesa payment gateway, including authentication and payment endpoint URLs, API timeout, username, and password.
* Select the appropriate payee identification field (e.g., phone number, email, bank account number) from available options.
* Automatically create payment batches for efficient processing.
* Trigger the payment process to transfer funds to beneficiaries via Mpesa.
* Monitor the status of individual payments and batches.

## Integration

* **[g2p_programs](g2p_programs):** This module inherits and extends the base payment manager model (`g2p.program.payment.manager`) provided by the `g2p_programs` module, integrating seamlessly with the existing program and payment batch management functionalities.
* **[g2p_registry_base](g2p_registry_base):** Leverages the registry system for accessing beneficiary information such as phone numbers or other chosen identifiers for payment disbursement.

## Key Features:

* **Simplified Mpesa Integration:**  Provides a straightforward configuration process for connecting to an Mpesa payment gateway.
* **Automated Batch Processing:**  Automates the creation and processing of payment batches, reducing manual effort.
* **Flexible Payee Identification:** Supports various payee identification methods, enabling flexibility in program design.
* **Real-time Status Tracking:** Allows monitoring of payment status at both the individual and batch level.

## Limitations:

* **Simple Integration:** This module is designed for basic Mpesa integrations. More complex workflows or specific API requirements might necessitate customization.
* **Limited Error Handling:** While the module provides basic error handling, a more robust error logging and recovery mechanism could be beneficial for mission-critical implementations. 
