***************************************
Eligibility Manager
***************************************
.. currentmodule:: odoo.addons.g2p_programs.models.managers.eligibility_manager

The eligibility manager verifies if a beneficiary is eligible for a given program. The eligibility
determination can be based on data stored in OpenSPP or on an external system using API calls.

:mod:`odoo.addons.g2p_programs.models.managers.eligibility_manager` provides the class  :class:`BaseEligibilityManager` define
the interface for this manager. :class:`DefaultEligibilityManager` is the default implementation of this class
that should be used in most of the cases.


.. autoclass:: BaseEligibilityManager
    :members:
