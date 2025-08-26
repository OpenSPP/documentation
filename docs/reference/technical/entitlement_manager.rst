***************************************
Entitlement Manager
***************************************
The entitlement manager determines what a :term:`beneficiary<beneficiary>` is entitled to for a given cycle.

The ``g2p_programs.models.managers.entitlement_manager`` module provides the classes that define
the interface for this manager. ``BaseEntitlementManager`` defines the abstract base class,
and ``DefaultCashEntitlementManager`` is the default implementation for cash distribution.

The ``BaseEntitlementManager`` can be extended to implement any other type of distribution such as ``in-kind``.


BaseEntitlementManager
======================

.. autoclass:: odoo.addons.g2p_programs.models.managers.entitlement_manager.BaseEntitlementManager
    :members:

DefaultCashEntitlementManager
==============================

.. autoclass:: odoo.addons.g2p_programs.models.managers.entitlement_manager.DefaultCashEntitlementManager
    :members:
