---
orphan: true
---

# G2P Program Cycleless

The 'G2P Program Cycleless' module extends OpenSPP's G2P Programs functionality to support social protection initiatives that operate without distinct, time-bound program cycles. It simplifies the management of ongoing programs by automating cycle-related processes, allowing for continuous benefit delivery and streamlined operations.

## Purpose

This module enables OpenSPP to manage programs that deliver continuous support, eliminating the administrative overhead of managing explicit program cycles. It accomplishes this by:

*   **Enabling Continuous Program Operation**: Allows programs to run indefinitely without requiring manual creation, activation, or closure of specific cycles. This is ideal for ongoing subsidy programs or long-term support initiatives.
*   **Automating Cycle Management**: When a program is marked as cycleless, the system automatically maintains a single, always-active cycle in the background. Users no longer need to create or manage individual cycles, simplifying program administration.
*   **Streamlining Entitlement Processing**: Entitlements are directly managed under the program's continuous active state. This removes the step of associating entitlements with specific cycles, making the process more direct and intuitive.
*   **Direct Payment Execution**: Provides immediate access to payment preparation and sending functionalities directly from the program's dashboard. This accelerates the disbursement process for programs with continuous payment flows.
*   **Supporting Diverse Program Models**: Facilitates the implementation of programs such as ongoing cash transfers, unconditional basic income schemes, or reimbursement programs, which do not naturally fit a cycle-based structure.

## Dependencies and Integration

This module primarily extends the core capabilities of the [G2P Programs](g2p_programs) module. It integrates by:

*   **Extending G2P Programs**: It adds the `is_cycleless` flag to the `g2p.program` model, allowing administrators to designate a program as cycleless. This flag fundamentally alters how the program is managed within OpenSPP.
*   **Modifying Program Management**: It enhances the `g2p.program.manager.default` model to automatically create and maintain a default active cycle when a program is marked as cycleless, ensuring continuous operation without user intervention.
*   **Streamlining Entitlement Views**: It integrates with the `g2p.program.entitlement.manager.default` model to ensure that entitlement views are simplified and directly tied to the program's continuous state, rather than a specific cycle.

## Additional Functionality

### Continuous Program Management

By marking a program with the 'Is Cycleless' option, administrators transform its operational model. The system automatically handles the underlying concept of a 'default active cycle', making it transparent to the user. This means that an active program is always ready for entitlement generation and payment processing, without the need for manual cycle setup or transitions.

### Simplified Entitlement Processing

For cycleless programs, the system presents entitlements directly under the program, removing the need to navigate through specific program cycles. The "Entitlements" section on the program dashboard will display all current entitlements associated with the program's continuous operation. Furthermore, for programs specifically designated as 'Reimbursement Programs', the entitlement section will be intuitively labeled "Reimbursements" for clearer context.

### Direct Payment Workflows

This module introduces "Prepare Payments" and "Send Payments" buttons directly on the active cycleless program's dashboard. This allows program managers to initiate payment processes without first selecting a specific cycle. The system automatically applies these actions to the program's continuous active state, significantly speeding up the payment workflow for ongoing benefit distributions.

### Flexible Program Models

The module also enhances support for various program types. For example, if a program is designated as a reimbursement program, the user interface will automatically adjust to use terms like "Reimbursements" instead of "Entitlements," providing a more tailored and intuitive experience for specific program designs.

## Conclusion

The 'G2P Program Cycleless' module simplifies the administration of ongoing social protection programs in OpenSPP by enabling continuous operation and automating cycle management, thereby enhancing efficiency and program responsiveness.