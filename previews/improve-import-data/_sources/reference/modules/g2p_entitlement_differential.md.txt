---
orphan: true
---

# G2P Entitlement Differential

The G2P Entitlement Differential module extends the core cash entitlement management features of OpenSPP. It introduces advanced capabilities for adjusting cash entitlement amounts, primarily by applying inflation rates, and provides enhanced control over beneficiary selection for entitlement calculations.

## Purpose

This module enhances the precision and responsiveness of cash-based social protection programs by allowing dynamic adjustments to entitlement values. It addresses the challenges of maintaining the real value of cash transfers and accurately targeting beneficiaries in evolving economic and social landscapes.

*   **Apply Inflation Adjustments**: Automatically adjust cash entitlement amounts based on a defined inflation rate to preserve their real purchasing power over time. This ensures beneficiaries receive transfers that reflect current economic conditions.
*   **Refine Beneficiary Selection**: Implement specific conditions to filter and select beneficiaries for entitlement calculations, enabling more targeted and flexible program design. For example, focusing on beneficiaries in specific geographic areas (e.g., country > province > district) or those meeting updated socio-economic criteria.
*   **Maintain Program Equity**: Ensure the fair and consistent distribution of benefits by accounting for economic fluctuations and allowing precise targeting of beneficiary groups.
*   **Streamline Financial Planning**: Provide tools for program administrators to manage and forecast entitlement costs more accurately, reflecting real-world economic changes.

## Dependencies and Integration

This module builds upon and integrates directly with the OpenSPP Cash Entitlement module, enhancing its core functionalities.

*   **OpenSPP Cash Entitlement ([spp_entitlement_cash](spp_entitlement_cash))**: This module is a direct extension of the `spp_entitlement_cash` module. It inherits and overrides key entitlement calculation processes, such as `prepare_entitlements`, to introduce differential adjustments like inflation. It leverages the existing framework for defining entitlement rules and managing beneficiaries, adding a layer of dynamic modification.

## Additional Functionality

The G2P Entitlement Differential module provides key features to ensure cash entitlements remain relevant and equitable.

### Inflation Adjustment for Cash Entitlements

Program administrators can enable and specify an inflation rate directly within the entitlement manager. When active, this feature automatically recalculates the `initial_amount` of generated cash entitlements by applying the defined inflation multiplier. This crucial capability helps maintain the real value of cash transfers, protecting beneficiaries from the erosion of purchasing power due to inflation.

### Dynamic Beneficiary Filtering

The module provides an enhanced mechanism for selecting beneficiaries during the entitlement calculation process. It allows for the application of additional, flexible conditions to filter beneficiaries from a broader pool. This capability supports highly targeted interventions, ensuring that specific groups of beneficiaries, based on updated criteria or dynamic conditions, receive the intended entitlements.

### Entitlement Item Naming

A `name` field is added to individual cash entitlement items. This allows for clearer identification and tracking of specific entitlement components or adjustments within the system. It helps administrators organize and understand the different elements that constitute a beneficiary's total entitlement.

## Conclusion

The G2P Entitlement Differential module empowers OpenSPP programs to adapt to changing economic realities and refine beneficiary targeting, ensuring cash transfers remain impactful and equitable.