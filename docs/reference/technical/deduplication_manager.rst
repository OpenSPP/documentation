***************************************
Deduplication Manager
***************************************

The deduplication manager allows to define how :term:`beneficiaries<beneficiaries>` are deduplicated within a program.

The ``g2p_programs.models.managers.deduplication_manager`` module provides the classes that define
the interface for this manager. ``BaseDeduplication`` defines the abstract base class,
and several implementations are provided for different deduplication strategies.


DeduplicationManager
====================

.. autoclass:: odoo.addons.g2p_programs.models.managers.deduplication_manager.DeduplicationManager
    :members:

BaseDeduplication
=================

.. autoclass:: odoo.addons.g2p_programs.models.managers.deduplication_manager.BaseDeduplication
    :members:

DefaultDeduplication
====================

.. autoclass:: odoo.addons.g2p_programs.models.managers.deduplication_manager.DefaultDeduplication
    :members:

IDDocumentDeduplication
=======================

.. autoclass:: odoo.addons.g2p_programs.models.managers.deduplication_manager.IDDocumentDeduplication
    :members:

PhoneNumberDeduplication
========================

.. autoclass:: odoo.addons.g2p_programs.models.managers.deduplication_manager.PhoneNumberDeduplication
    :members:

IDPhoneEligibilityManager
==========================

.. autoclass:: odoo.addons.g2p_programs.models.managers.deduplication_manager.IDPhoneEligibilityManager
    :members:

IDDocumentDeduplicationEligibilityManager
==========================================

.. autoclass:: odoo.addons.g2p_programs.models.managers.deduplication_manager.IDDocumentDeduplicationEligibilityManager
    :members:

PhoneNumberDeduplicationEligibilityManager
===========================================

.. autoclass:: odoo.addons.g2p_programs.models.managers.deduplication_manager.PhoneNumberDeduplicationEligibilityManager
    :members: