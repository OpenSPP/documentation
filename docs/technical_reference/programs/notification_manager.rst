***************************************
Notification Manager
***************************************
.. currentmodule:: odoo.addons.spp_programs.models.managers.notification_manager

The notification managers allow notifying :term:`beneficiaries<beneficiaries>` of some events happening in the programs or cycles.

:mod:`odoo.addons.spp_programs.models.managers.notification_manager` provides the class  :class:`BaseNotificationManager` define
the interface for this manager. :class:`SMSNotificationManager` is the default implementation.

.. autoclass:: BaseNotificationManager
    :members:

.. autoclass:: SMSNotificationManager
    :members:
    :undoc-members:

.. autoclass:: SMSTemplate
    :members:
    :undoc-members:
