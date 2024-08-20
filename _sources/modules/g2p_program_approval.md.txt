# OpenG2P Program Approval Module

```{warning}

**Work in Progress**: This document is actively being developed and updated. Content may be incomplete or subject to change.
```

## Overview

The [g2p_program_approval](g2p_program_approval) module enhances the OpenG2P [g2p_programs](g2p_programs) module by introducing an approval workflow for entitlements. This module enables program managers to define multi-stage approval processes, assign approval rights to user groups, and track the approval status of individual entitlements.

## Features

* **Multi-stage Approval Workflow:** Define custom approval stages with specific states and responsible user groups.
* **Granular Approval Rights:** Assign approval permissions to different user groups at each stage of the workflow.
* **Approval Status Tracking:** Monitor the approval status of individual entitlements throughout the approval process.
* **Seamless Integration:** Integrates directly with the [g2p_programs](g2p_programs) module, extending its functionality.

## Functionality and Integration

The [g2p_program_approval](g2p_program_approval) module extends the functionality of the [g2p_programs](g2p_programs) module by adding the following features:

* **Approval Mapping:** Program managers can define a sequence of approval stages for entitlements using the `ProgramApprovalMapping` model. Each stage is associated with a state, a responsible user group, and an optional sequence number.
* **Entitlement Manager Approval:** The `DefaultEntitlementManagerApproval` model is extended to manage the approval process. It uses the defined approval mapping to determine the next stage and responsible group for each entitlement.
* **Entitlement Approval Status:** The `G2PApprovalEntitlement` model, which inherits from the `g2p.entitlement` model in [g2p_programs](g2p_programs), now includes an `approval_state` field to track the current approval status of the entitlement.
* **User Interface Enhancements:** The module modifies the user interface to display the approval status of entitlements and provide buttons for approving or rejecting them.

## Benefits

* **Enhanced Accountability:**  The approval workflow enforces accountability by clearly defining roles and responsibilities for approving entitlements.
* **Improved Transparency:**  Tracking the approval status of entitlements provides transparency into the decision-making process.
* **Streamlined Workflow:** Automating the approval process reduces manual effort and improves the efficiency of entitlement management.

## Conclusion

The [g2p_program_approval](g2p_program_approval) module enhances the OpenG2P platform by providing a robust and customizable approval workflow for managing entitlements. By integrating seamlessly with the [g2p_programs](g2p_programs) module, it strengthens the platform's capabilities for managing social protection programs effectively. 
