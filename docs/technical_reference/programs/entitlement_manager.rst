***************************************
Entitlement Manager
***************************************

The entitlement manager determines what a :term:`beneficiary<beneficiary>` is entitled to for a given cycle.

Overview
========

The ``BaseEntitlementManager`` class defines the interface for entitlement management.
OpenSPP provides multiple implementations for different distribution types:

- **Cash entitlements**: ``spp_entitlement_cash`` module
- **In-kind entitlements**: ``spp_entitlement_in_kind`` module
- **Basket entitlements**: ``spp_entitlement_basket`` module

Key Methods
===========

BaseEntitlementManager
----------------------

The base entitlement manager provides the following abstract methods:

``prepare_entitlements(cycle, beneficiaries)``
    Generate entitlement records for the given beneficiaries in a cycle.
    This is called during cycle preparation.

``validate_entitlements(cycle, entitlements)``
    Validate entitlement records before approval. Can implement business rules
    and compliance checks.

``approve_entitlements(cycle, entitlements)``
    Approve entitlements for disbursement. Updates entitlement state and
    triggers any approval workflows.

``set_pending_validation_entitlements(cycle)``
    Mark entitlements as pending validation, typically after preparation.

Entitlement Types
=================

Cash Entitlements
-----------------

The ``spp_entitlement_cash`` module provides cash-based entitlements with:

- Fixed or formula-based amount calculation
- Currency support
- Transfer fee handling
- Payment integration

In-Kind Entitlements
--------------------

The ``spp_entitlement_in_kind`` module provides goods-based entitlements with:

- Product catalog integration
- Quantity calculation
- Warehouse/inventory management
- Bundle/kit support

Basket Entitlements
-------------------

The ``spp_entitlement_basket`` module provides composite entitlements with:

- Multiple items per entitlement
- Mixed cash and in-kind items
- Flexible composition rules
