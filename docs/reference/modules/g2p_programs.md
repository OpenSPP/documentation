---
orphan: true
---

# OpenG2P Programs

The 'g2p_programs' module is the central operational hub within OpenSPP for defining, managing, and executing social protection programs and farmer registries. It provides a comprehensive framework to administer the full lifecycle of a program, from initial setup and beneficiary enrollment to benefit disbursement and financial reconciliation.

## Purpose

This module enables organizations to efficiently manage their social protection and farmer registry initiatives by providing key capabilities:

*   **Program Definition and Configuration**: Users define new programs, specify their objectives, and configure the operational workflows for beneficiary management and benefit delivery. This ensures programs are structured and aligned with their specific goals.
*   **Beneficiary Lifecycle Management**: It manages beneficiaries from enrollment through eligibility checks, deduplication, and status changes (e.g., enrolled, paused, exited), maintaining an accurate and up-to-date registry for each program.
*   **Program Cycle Administration**: The module organizes program activities into distinct cycles, allowing for phased benefit distribution and clear tracking of progress for each program period.
*   **Entitlement and Payment Processing**: It facilitates the creation, approval, and disbursement of benefits (entitlements) to eligible beneficiaries, with robust financial tracking and batch processing for payments. This streamlines the delivery of aid and ensures accountability.
*   **Operational Oversight and Reporting**: Users gain insights into program performance through various statistics, reports, and the ability to track key metrics like beneficiary counts, entitlement statuses, and payment progress.

## Dependencies and Integration

The 'g2p_programs' module integrates extensively with other OpenSPP and Odoo modules to provide its comprehensive functionality:

*   **[G2P Registry Base](g2p_registry_base)**: This foundational module provides the core registrant (beneficiary) data structure, including identification, contact information, and relationships, which 'g2p_programs' uses to manage program participants.
*   **[G2P Registry Individual](g2p_registry_individual)** and **[G2P Registry Groups](g2p_registry_group)**: These modules define whether a program's beneficiaries are individuals or groups, allowing 'g2p_programs' to manage the appropriate registrant types.
*   **[G2P Registry Membership](g2p_registry_membership)**: If a program targets groups, this module helps manage the specific roles and relationships of individuals within those groups, providing a detailed view of group composition.
*   **[G2P Bank](g2p_bank)**: Essential for cash-based programs, this module integrates beneficiary bank account details, enabling direct financial disbursements.
*   **Account**: The standard Odoo accounting module is used for managing disbursement journals, tracking program funds, and recording all financial transactions related to entitlements and payments.
*   **Queue Job**: This module handles background processing of large or time-consuming tasks, such as eligibility checks for many beneficiaries or batch processing of payments, ensuring the system remains responsive.
*   **Event SMS** and **Calendar**: These modules can be leveraged for sending automated notifications to beneficiaries (e.g., payment alerts) and scheduling program-related events or deadlines.

The 'g2p_programs' module acts as the operational layer that brings together beneficiary data, financial tools, and program management logic to deliver benefits effectively.

## Additional Functionality

### Program Definition and Management

Users can establish new social protection programs and configure their core attributes. This includes defining a program's name, description, and specifying whether it targets individual beneficiaries or groups (e.g., households, farmer cooperatives). The module allows for the flexible assignment of "managers" (e.g., Eligibility, Deduplication, Payment Managers) that dictate specific program workflows and logic. Programs can be set to 'Active' or 'Ended', with the ability to reactivate them, and automatically manage associated accounting journals for financial oversight.

### Beneficiary Enrollment and Deduplication

The module supports the enrollment of eligible beneficiaries into specific programs, tracking their status within the program (e.g., enrolled, paused, exited, duplicated). It provides tools to verify beneficiary eligibility based on program criteria and to perform deduplication checks. Deduplication managers help identify and manage instances where beneficiaries might be registered multiple times, ensuring program integrity and preventing double-dipping.

### Cycle and Entitlement Processing

Programs are structured into cycles, representing distinct periods for benefit delivery. Users can create new cycles, define their start and end dates, and easily import eligible beneficiaries from the overall program or a previous cycle. Within each cycle, the module generates entitlements for beneficiaries, which define the type and amount of benefits they are due. Entitlements follow a lifecycle (e.g., draft, pending approval, approved, paid), and once approved, a unique Entitlement Reference Number (ERN) can be generated for tracking.

### Payment Disbursement and Financial Reporting

The module facilitates the preparation and processing of payments corresponding to approved entitlements. Payments can be grouped into batches for efficient processing and managed through various states (e.g., issued, sent, reconciled). Comprehensive statistics are available for each payment batch, including the number and amount of issued, sent, paid, and failed transactions. This module also integrates with the accounting system to ensure all disbursements are properly recorded and managed, supporting financial reconciliation and generating reports like voucher cards and summary reports for program monitoring.

## Conclusion

The 'g2p_programs' module is the cornerstone of OpenSPP, providing an end-to-end solution for managing social protection programs and farmer registries. It streamlines program operations from setup and beneficiary management to benefit delivery and financial accountability, ensuring efficient and transparent program execution.