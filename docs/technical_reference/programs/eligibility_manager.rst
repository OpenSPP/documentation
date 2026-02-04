***************************************
Eligibility Manager
***************************************

The eligibility manager verifies if a :term:`beneficiary<beneficiary>` is eligible for a given program. The :term:`eligibility<eligibility>`
determination can be based on data stored in OpenSPP or on an external system using API calls.

Overview
========

The ``BaseEligibilityManager`` class defines the interface for eligibility verification.
``DefaultEligibilityManager`` is the default implementation that should be used in most cases.

OpenSPP extends the default eligibility manager through ``spp_programs`` to add
area-based filtering and registrant-specific validation.

Key Methods
===========

BaseEligibilityManager
----------------------

The base eligibility manager provides the following abstract methods:

``enroll_eligible_registrants(program_memberships)``
    Validate if registrants match the criteria needed to be enrolled in a program.
    Returns the filtered list of eligible program memberships.

``verify_cycle_eligibility(cycle, membership)``
    Validate if a beneficiary matches the criteria needed to be enrolled in a specific cycle.
    Returns the filtered list of eligible cycle memberships.

``import_eligible_registrants()``
    Import eligible registrants into the program based on the configured eligibility domain.

DefaultEligibilityManager
-------------------------

The default implementation provides:

- **Domain-based filtering**: Uses Odoo domain expressions to filter eligible registrants
- **Target type support**: Filters by individual or group based on program configuration
- **Disabled registrant exclusion**: Automatically excludes disabled registrants
- **Batch import**: Supports asynchronous import for large datasets using job queues

OpenSPP Extensions
==================

The ``spp_programs`` module extends ``DefaultEligibilityManager`` with:

- **Area-based filtering**: Filter eligibility by administrative areas (``admin_area_ids``)
- **Registrant validation**: Ensures only valid registrants (``is_registrant=True``) are included
- **Target type awareness**: Respects the program's target type configuration
