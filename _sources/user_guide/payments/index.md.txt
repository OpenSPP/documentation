---
openspp:
  doc_status: draft
  products: [payments]
  applies_to:
    - sp_mis
---

# Payments

**Applies to:** SP-MIS

The Payments section covers distributing benefits to beneficiaries through service points and Point of Sale systems. This section guides you through viewing service points and understanding payment workflows.

## What You Will Learn

- **Service Points** - View and understand service point locations where payments are distributed
- **Point of Sale** - Use the POS interface to disburse cash benefits at service points

## How Payments Work

Payments in OpenSPP follow this workflow:

1. **Entitlements are created** - When a program cycle runs, entitlements are generated for enrolled beneficiaries
2. **Entitlements are approved** - Program managers review and approve entitlements for payment
3. **Payments are disbursed** - Approved payments are distributed at service points using the Point of Sale system

```{toctree}
:maxdepth: 2
:hidden:

service_points
```

## Related Guides

- {doc}`/tutorial/user_guides/point_of_sales` - Complete guide to using the Point of Sale interface
- {doc}`/user_guide/programs/index` - Managing social protection programs and cycles
