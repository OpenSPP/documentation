---
review-status: needs-review
review-date: 2025-06-04
reviewer: migration-script
migration-notes: "Added during 2025 documentation reorganization"
---

***************************************
Entitlement Manager
***************************************
.. currentmodule:: odoo.addons.g2p_programs.models.managers.entitlement_manager

The entitlement manager determines what a :term:`beneficiary<beneficiary>` is entitled to for a given cycle.


:mod:`odoo.addons.g2p_programs.models.managers.entitlement_manager` provides the class  :class:`BaseEntitlementManager` define
the interface for this manager. :class:`DefaultCashEntitlementManager` is the default implementation of this class
for cash distribution.

The :class:`BaseEntitlementManager` can be extended to implement any other type of distribution such as ``in-kind``.


.. autoclass:: BaseEntitlementManager
    :members:

.. autoclass:: DefaultCashEntitlementManager
    :members:
    :undoc-members:
