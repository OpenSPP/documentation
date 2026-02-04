***************************************
Cycle Manager
***************************************

The cycle manager handles the lifecycle of program cycles, including creation, state transitions,
and beneficiary enrollment within cycles.

Overview
========

The ``BaseCycleManager`` class defines the interface for cycle management operations.
``DefaultCycleManager`` is the default implementation that should be used in most cases.

OpenSPP extends the default cycle manager through ``spp_programs`` to add additional
functionality such as cycle linking (previous/next cycle references) and in-kind entitlement
statistics.

Key Methods
===========

BaseCycleManager
----------------

The base cycle manager provides the following abstract methods that must be implemented:

``new_cycle(name, start_date, sequence)``
    Create a new cycle for the program with the given name, start date, and sequence number.

``open_cycle(cycle)``
    Transition a cycle from draft to open state, making it active for enrollment.

``close_cycle(cycle)``
    Close an active cycle, preventing further modifications.

``add_beneficiaries(cycle, beneficiaries, state)``
    Add beneficiaries to a cycle with the specified enrollment state.

DefaultCycleManager
-------------------

The default implementation provides:

- Automatic cycle sequencing
- Beneficiary copying from previous cycles (configurable)
- Entitlement preparation with job queue support for large datasets
- State management with validation

OpenSPP Extensions
==================

The ``spp_programs`` module extends ``DefaultCycleManager`` with:

- **Cycle linking**: Maintains ``prev_cycle_id`` and ``next_cycle_id`` references
- **In-kind statistics**: Computes in-kind entitlement counts after preparation
- **Custom hooks**: ``on_start_date_change`` for date-based triggers
