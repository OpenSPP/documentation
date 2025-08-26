***************************************
Eligibility Manager
***************************************

.. meta::
   :review-status: reviewed
   :review-date: 2025-08-26
   :reviewer: claude-code

The eligibility manager verifies if a :term:`beneficiary<beneficiary>` is eligible for a given program. The :term:`eligibility<eligibility>`
determination can be based on data stored in OpenSPP or on an external system using API calls.

The ``g2p_programs.models.managers.eligibility_manager`` module provides the classes that define
the interface for this manager. ``BaseEligibilityManager`` defines the abstract base class,
and ``DefaultEligibilityManager`` is the default implementation that should be used in most cases.


EligibilityManager
==================

.. autoclass:: odoo.addons.g2p_programs.models.managers.eligibility_manager.EligibilityManager
    :members:

BaseEligibilityManager
======================

.. autoclass:: odoo.addons.g2p_programs.models.managers.eligibility_manager.BaseEligibilityManager
    :members:

DefaultEligibilityManager
==========================

.. autoclass:: odoo.addons.g2p_programs.models.managers.eligibility_manager.DefaultEligibilityManager
    :members:
