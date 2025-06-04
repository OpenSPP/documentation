---
review-status: needs-review
review-date: 2025-06-04
reviewer: migration-script
migration-notes: "Added during 2025 documentation reorganization"
---

# OpenG2P Entitlement: Voucher Module

```{warning}

**Work in Progress**: This document is actively being developed and updated. Content may be incomplete or subject to change.
```

## Overview

The [g2p_entitlement_voucher](g2p_entitlement_voucher) module extends the OpenG2P Entitlement functionality by providing a mechanism to generate and manage vouchers associated with entitlements. This module is particularly useful for social protection programs that utilize vouchers as a means of delivering benefits to beneficiaries.

## Features

* **Voucher Generation:** The module enables the generation of vouchers for approved entitlements. This process can be automated to trigger upon entitlement approval or manually initiated by authorized users.
* **Voucher Configuration:** Program administrators can define voucher templates and configure various aspects of voucher generation, such as the file format, content, and storage location.
* **Voucher Printing:** The module provides a convenient way to print generated vouchers directly from the entitlement record.
* **Integration with Payment Files:**  Leverages the [g2p_payment_files](g2p_payment_files) module to facilitate voucher creation using predefined templates and configurations.
* **Encryption Support:** Integrates with the [g2p_encryption](g2p_encryption) module to allow for the secure encryption of sensitive data within the vouchers.

## Dependencies

- **[g2p_encryption](g2p_encryption):**  This dependency is used for encrypting sensitive data included in the vouchers.
- **[g2p_programs](g2p_programs):** This module provides the core functionality for managing social protection programs and entitlements, upon which this module builds.
- **[g2p_payment_files](g2p_payment_files):**  This module provides the framework for defining and managing payment file configurations, which are utilized for voucher generation.

## Workflow

1. **Configuration:** Program administrators configure voucher generation settings within the [Entitlement Manager]([g2p_programs](g2p_programs)#entitlement-manager) associated with the program. This includes selecting a voucher file configuration, storage location for generated vouchers, and optional encryption settings.

2. **Entitlement Approval:** When an entitlement is approved, the system can automatically generate a voucher based on the predefined configurations.
3. **Voucher Access:** Users can access and print the generated voucher directly from the entitlement record.

## Benefits

* **Streamlined Benefit Delivery:** Automating voucher generation reduces manual effort and ensures timely delivery of benefits to beneficiaries.
* **Enhanced Security:** Integration with encryption capabilities protects sensitive data stored within the vouchers.
* **Improved Accountability:**  The module maintains a record of generated vouchers, providing an audit trail for tracking and accountability purposes. 
* **Flexibility and Customization:**  Administrators have the flexibility to tailor voucher generation and content according to program-specific requirements. 
