***************************************
Notification Manager
***************************************
The notification managers allow notifying :term:`beneficiaries<beneficiaries>` of some events happening in the programs or cycles.

The ``g2p_programs.models.managers.notification_manager`` module provides the classes that define
the interface for this manager. ``BaseNotificationManager`` defines the abstract base class,
and ``SMSNotificationManager`` is the default implementation.


BaseNotificationManager
========================

.. autoclass:: odoo.addons.g2p_programs.models.managers.notification_manager.BaseNotificationManager
    :members:

SMSNotificationManager
======================

.. autoclass:: odoo.addons.g2p_programs.models.managers.notification_manager.SMSNotificationManager
    :members:

SMSTemplate
===========

.. autoclass:: odoo.addons.g2p_programs.models.managers.notification_manager.SMSTemplate
    :members:
