# G2P Payment Cash

The `g2p_payment_cash` module within OpenSPP enables the management and processing of cash-based payments for social protection programs. It provides a direct and auditable method for disbursing benefits where physical cash distribution is the primary mechanism, ensuring beneficiaries receive their support effectively.

## Purpose

The **G2P Payment Cash** module provides a comprehensive framework for:

*   **Facilitates Cash Disbursements**: Allows program managers to designate cash as the primary payment method for specific programs or cycles. This is crucial for reaching beneficiaries in areas with limited access to banking or digital payment infrastructure.
*   **Streamlines Payment Preparation**: Prepares approved entitlements for cash disbursement, grouping them into manageable batches based on program cycles and defined criteria.
*   **Manages Batch Tags**: Supports the assignment of "Batch Tags" to cash payment batches, enabling organized tracking and reporting of physical cash distributions. For example, batches could be tagged by distribution point (e.g., "District A - Payout Point 1") or specific distribution dates.
*   **Direct Payment Reconciliation**: Automatically marks payments as 'paid' and 'reconciled' within the system once the cash disbursement is confirmed. This ensures accurate financial records and up-to-date beneficiary payment statuses.
*   **Empowers Direct Action on Entitlements**: Provides a direct action button on approved entitlements, allowing for immediate preparation and marking of individual cash payments.

## Dependencies and Integration

*   **G2P Programs ([g2p_programs](g2p_programs))**: This module integrates directly with the G2P Programs module, extending its capabilities to include 'Cash Payment Manager' as an available payment method for programs. Program administrators select this manager to define how benefits are disbursed for a given program cycle.
*   **G2P Payment Files ([g2p_payment_files](g2p_payment_files))**: The `g2p_payment_cash` module inherits core payment preparation and batching logic from `g2p_payment_files`. While it overrides the final "sending" mechanism for direct cash, it utilizes the same underlying framework for creating payment batches and managing entitlements, ensuring consistency in how payments are structured before disbursement.

## Additional Functionality

### Cash Payment Manager Selection
Program administrators can configure a social protection program to use "Cash Payment Manager" as its default method for benefit disbursement. This selection ensures that all payment processing for that program will follow cash-specific workflows, tailored for physical distribution.

### Direct Entitlement Payment
For individual approved entitlements, the module provides a "Prepare and Send Payment" action button. When selected, the system processes the entitlement for cash payment, immediately marking it as paid and reconciled. This feature is useful for managing ad-hoc or individual cash disbursements outside of larger batch processes.

### Batch Tagging for Cash Disbursements
The module allows program managers to associate multiple "Batch Tags" with cash payment managers. These tags help categorize and track physical cash distribution events, such as linking payments to specific distribution points, dates, or field teams. This enhances operational oversight and reporting for cash-based programs.

### Automated Payment Reconciliation
Once cash payments are processed through this module, the system automatically updates the status of the individual payments and their associated batches to "reconciled" and "paid". This provides real-time visibility into the financial status of cash disbursements, confirming that the funds have been successfully transferred to beneficiaries.

## Conclusion

The `g2p_payment_cash` module is essential for OpenSPP, enabling efficient and traceable management of direct cash benefit disbursements for social protection programs, particularly in contexts where physical cash distribution is the primary method.