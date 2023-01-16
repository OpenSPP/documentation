***************************************
Entitlement Manager
***************************************
.. currentmodule:: odoo.addons.g2p_programs.models.managers.entitlement_manager

The entitlement manager determines what a beneficiary is entitled to for a given cycle.


:mod:`odoo.addons.g2p_programs.models.managers.entitlement_manager` provides the class  :class:`BaseEntitlementManager` define
the interface for this manager. :class:`DefaultCashEntitlementManager` is the default implementation of this class
for cash distribution.

The :class:`BaseEntitlementManager` can be extended to implement any other type of distribution such as ``in-kind``.


.. autoclass:: BaseEntitlementManager
    :members:

.. autoclass:: DefaultCashEntitlementManager
    :members:
    :undoc-members:
