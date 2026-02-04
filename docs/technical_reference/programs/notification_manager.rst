***************************************
Notification Manager
***************************************

The notification managers allow notifying :term:`beneficiaries<beneficiaries>` of events
happening in programs or cycles, such as enrollment confirmations, entitlement approvals,
and payment disbursements.

Overview
========

The ``BaseNotificationManager`` class defines the interface for sending notifications.
Multiple implementations are available for different communication channels:

- **SMS notifications**: Send text messages to beneficiaries
- **Email notifications**: Send email messages (when configured)

Key Methods
===========

BaseNotificationManager
-----------------------

The base notification manager provides the following abstract methods:

``send_notification(program, cycle, beneficiaries, template)``
    Send notifications to the specified beneficiaries using the given template.
    The template defines the message content and can include dynamic placeholders.

``on_cycle_started(cycle)``
    Hook called when a cycle starts. Can be used to send enrollment notifications.

``on_entitlement_approved(cycle, entitlements)``
    Hook called when entitlements are approved. Can notify beneficiaries of their
    approved benefits.

``on_payment_sent(cycle, payments)``
    Hook called when payments are disbursed. Can send payment confirmation messages.

SMS Notification Manager
========================

The SMS notification manager provides:

- **Template-based messages**: Define reusable message templates with placeholders
- **Bulk sending**: Efficiently send messages to large groups of beneficiaries
- **Delivery tracking**: Track message delivery status (when supported by provider)
- **Provider integration**: Connect to SMS gateway providers

SMS Templates
-------------

SMS templates support the following placeholders:

- ``{beneficiary_name}``: The beneficiary's name
- ``{program_name}``: The program name
- ``{cycle_name}``: The cycle name
- ``{amount}``: The entitlement amount (for cash programs)
- ``{date}``: Relevant date (enrollment, payment, etc.)

Configuration
=============

Notification managers are configured per program and can be enabled/disabled
as needed. Multiple notification managers can be active for a single program
to support different communication channels.
