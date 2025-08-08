# OpenG2P Programs: Cycleless Module

```{warning}

**Work in Progress**: This document is actively being developed and updated. Content may be incomplete or subject to change.
```

## Overview

The [g2p_program_cycleless](g2p_program_cycleless) module extends the functionality of the [g2p_programs](g2p_programs) module to support **cycleless** social protection programs. 

Traditional social protection programs often operate in cycles, with distinct periods for enrollment, payment preparation, and disbursement. However, some programs, especially those focused on **continuous or on-demand support**, may benefit from a cycleless approach.

This module allows program managers to designate a program as **cycleless**, eliminating the need to manage distinct program cycles. This simplifies program administration and provides greater flexibility in managing beneficiary entitlements and payments.

## Key Features

* **Cycleless Program Designation:**  The module adds a new field to the `g2p.program` model, allowing administrators to mark a program as cycleless.
* **Simplified Interface:** For cycleless programs, the user interface is adapted to hide cycle-related elements, presenting a more streamlined experience.
* **Automatic Cycle Management:** When a program is marked as cycleless, the module automatically manages a single, always-active cycle in the background. This simplifies program operations without sacrificing the underlying data structure.
* **Unified Entitlement Management:**  Beneficiary entitlements are managed within the context of the always-active cycle, providing a unified view for administrators.
* **Streamlined Payment Processing:** Payment preparation and disbursement processes are adapted for the cycleless model.

## Integration with Other Modules

This module directly extends the [g2p_programs](g2p_programs) module. It leverages existing data structures and functionalities from this module, such as:

* **Program Model:** Utilizes the `g2p.program` model to manage program configurations and settings.
* **Cycle Model:** Leverages the `g2p.cycle` model to represent the always-active cycle in the background. 
* **Entitlement Management:** Integrates with the entitlement management functionalities provided by the [g2p_programs](g2p_programs) module.

## Benefits of Using the Cycleless Module

* **Simplified Program Administration:** Reduced complexity for programs that do not require distinct operational cycles.
* **Increased Flexibility:**  Enables more dynamic and responsive program delivery, particularly for on-demand or continuous support programs.
* **Streamlined User Experience:**  Provides a more intuitive interface for managing cycleless programs. 

## Use Cases

* **Emergency Cash Transfers:** Rapidly provide assistance to beneficiaries in response to unforeseen events without the need for pre-defined cycles.
* **Conditional Cash Transfers with Rolling Enrollment:**  Allow beneficiaries to enroll and become eligible for benefits on an ongoing basis, rather than within fixed enrollment periods.
* **Continuous Social Assistance:**  Support programs that provide ongoing assistance based on evolving needs and circumstances, such as disability benefits. 
