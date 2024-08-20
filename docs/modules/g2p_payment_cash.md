# OpenG2P Program Payment: Cash

```{warning}

**Work in Progress**: This document is actively being developed and updated. Content may be incomplete or subject to change.
```

This module extends the OpenG2P platform to handle cash disbursements for social protection programs. 

## Overview

The [g2p_payment_cash](g2p_payment_cash) module provides a streamlined approach to managing and recording cash payments for entitlements within the OpenG2P system. It integrates seamlessly with the core program management functionalities offered by the [g2p_programs](g2p_programs) module and builds upon the file-based payment management system provided by the [g2p_payment_files](g2p_payment_files) module. 

## Functionality

This module introduces:

- **Cash Payment Manager:**  A specialized payment manager dedicated to handling cash disbursements. This manager allows users to prepare payment batches, but instead of generating payment files, it directly marks the payments as "reconciled" and "paid" within the system, simulating the act of distributing cash directly to beneficiaries.

- **Simplified Payment Workflow:** Beneficiaries with approved entitlements can have their payments processed and recorded as "paid" directly within the system. This eliminates the need for generating intermediary payment files, simplifying the workflow for cash-based programs.

- **Integration with Entitlements:**  The module extends the functionality of the `g2p.entitlement` model.  A new button, "Record Cash Payment", appears on approved entitlements when the program is configured to use the Cash Payment Manager.  Clicking this button initiates the cash payment process.

## Integration

- **[g2p_programs](g2p_programs):** This module relies on the core program management features provided by [g2p_programs](g2p_programs) for managing beneficiaries, programs, and entitlements. 

- **[g2p_payment_files](g2p_payment_files):**  While this module doesn't generate payment files, it inherits the base functionality and structure of the file-based payment manager from [g2p_payment_files](g2p_payment_files).

## Benefits

- **Streamlined Cash Disbursements:**  Simplifies the payment process for programs using cash disbursements.
- **Enhanced Record Keeping:** Ensures accurate and transparent recording of cash payments within the system.
- **Improved Efficiency:** Reduces manual processes and potential errors associated with cash handling. 
