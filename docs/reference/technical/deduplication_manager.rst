***************************************
Deduplication Manager
***************************************

The deduplication manager allows to define how :term:`beneficiaries<beneficiaries>` are deduplicated within a program.

The :mod:`g2p_programs.models.managers.deduplication_manager` module provides the classes that define the interface for this manager. 
:class:`~odoo.addons.g2p_programs.models.managers.deduplication_manager.BaseDeduplication` defines the abstract base class, 
and several implementations are provided for different deduplication strategies.

DeduplicationManager
====================

.. autoclass:: odoo.addons.g2p_programs.models.managers.deduplication_manager.DeduplicationManager
    :members:

BaseDeduplication
=================

.. autoclass:: odoo.addons.g2p_programs.models.managers.deduplication_manager.BaseDeduplication
    :members:

