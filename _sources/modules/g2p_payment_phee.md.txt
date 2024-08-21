# g2p_payment_phee Module

```{warning}

**Work in Progress**: This document is actively being developed and updated. Content may be incomplete or subject to change.
```

This module extends the OpenG2P platform to integrate with the **Payment Hub Enterprise Edition (PHEE)** for disbursing payments to beneficiaries.

## Overview

The [g2p_payment_phee](g2p_payment_phee) module provides a dedicated payment manager for interacting with the PHEE API.  This manager enables automated batch creation, payment preparation, and secure transmission of payment instructions to the PHEE system.

## Key Features

* **PHEE Integration:** Enables seamless integration with the PHEE platform for efficient payment processing.
* **Payment Manager:** Introduces a specialized `G2PPaymentHubEEManager` model that handles PHEE-specific payment operations.
* **Automated Batch Creation:** Supports automatic creation of payment batches, streamlining the disbursement process.
* **CSV File Generation:** Generates CSV files containing payment instructions in the format required by PHEE.
* **Configuration Settings:** Allows administrators to configure PHEE API endpoints, authentication credentials, and other payment-related parameters.

## Dependencies

* **[g2p_registry_base](g2p_registry_base):** Provides core registry functionality.
* **[g2p_programs](g2p_programs):** Manages social protection programs, cycles, entitlements, and payments.

## Functionality and Integration

This module extends the functionality of the [g2p_programs](g2p_programs) module by adding a PHEE-specific payment manager. It leverages existing data structures for programs, cycles, entitlements, and payments to generate payment instructions. 

The module's payment manager automates the process of:

1. **Preparing Payments:** Creating payment records associated with approved entitlements.
2. **Batching Payments:** Grouping payments into batches based on configurable parameters.
3. **Generating CSV Files:** Creating CSV files containing payment details in the PHEE-compliant format.
4. **Sending Payments:** Transmitting payment batches to the PHEE API for processing.

## Configuration

The module provides configuration settings for specifying PHEE API endpoints, authentication credentials, and other parameters. This allows administrators to tailor the integration to their specific PHEE environment.

## Usage

Once configured, the PHEE payment manager can be used to prepare, batch, and send payments to beneficiaries. The module's automated features streamline the disbursement process, enhancing efficiency and reducing manual intervention. 
