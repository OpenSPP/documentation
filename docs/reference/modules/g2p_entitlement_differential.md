# OpenG2P Entitlement: Differential Module

```{warning}

**Work in Progress**: This document is actively being developed and updated. Content may be incomplete or subject to change.
```

## Overview

The [g2p_entitlement_differential](g2p_entitlement_differential) module extends the functionality of the [spp_entitlement_cash](spp_entitlement_cash) module to provide more flexibility and control over calculating cash entitlements in social protection programs. This module introduces features that allow program implementers to adjust entitlement amounts based on factors like inflation and define more complex entitlement rules.

## Features

* **Inflation Adjustment:** Enables automatic adjustment of entitlement amounts based on a defined inflation rate. This ensures that the real value of benefits is maintained over time.
* **Flexible Entitlement Rules:** Allows for more complex entitlement calculation logic by providing greater control over beneficiary selection and amount determination.
* **Enhanced User Interface:** Provides an improved user interface for managing entitlement rules, including a more intuitive way to define and organize entitlement items.

## Integration with Other Modules

This module directly depends on the [spp_entitlement_cash](spp_entitlement_cash) module and inherits its core functionalities. It extends the existing features by providing additional fields and methods for differential entitlement calculation.

## Key Functionality

* **Inflation Adjustment:**
    - Adds an "Enable Inflation" checkbox and an "Inflation Rate" field to the entitlement manager form.
    - When enabled, the module automatically multiplies the initial entitlement amount by the defined inflation rate during the entitlement preparation process.
* **Flexible Entitlement Rules:**
    - Modifies the beneficiary selection process to allow for more complex conditions using the `_get_all_beneficiaries` method. This allows program implementers to define rules based on various beneficiary attributes.
* **Enhanced User Interface:**
    - Replaces the "Sequence" field with a "Name" field in the entitlement item tree and form views. This provides a clearer way to identify and manage individual entitlement items.

## Benefits

* **Improved Accuracy:** Enables more accurate calculation of entitlement amounts by considering factors like inflation.
* **Increased Flexibility:** Allows program implementers to design and implement more responsive and adaptable social protection programs.
* **Enhanced Transparency:** Provides a clear and auditable trail of the entitlement calculation process, promoting accountability and trust.

## Conclusion

The [g2p_entitlement_differential](g2p_entitlement_differential) module is a valuable addition to the OpenSPP suite for organizations looking to implement dynamic and equitable social protection programs. Its ability to handle complex entitlement scenarios and adjust to changing economic conditions makes it an essential tool for ensuring effective and impactful social assistance.
