***************************************
Program Manager
***************************************

The program manager determines which registrants/groups are included in the program and
coordinates the overall program lifecycle including cycle creation and beneficiary enrollment.

Overview
========

The ``BaseProgramManager`` class defines the interface for program management operations.
``DefaultProgramManager`` is the default implementation that handles cycle creation,
beneficiary enrollment, and coordination with other managers.

Key Methods
===========

BaseProgramManager
------------------

The base program manager provides the following abstract methods:

``last_cycle()``
    Returns the last (most recent) cycle of the program, sorted by sequence number.

``new_cycle()``
    Create the next cycle of the program. Handles automatic naming, sequencing,
    and optionally copies enrolled beneficiaries from the previous cycle.

``enroll_eligible_registrants(state=None)``
    Enroll eligible registrants in the program. Coordinates with eligibility managers
    to verify eligibility and update enrollment states.

``mark_enroll_eligible_as_done()``
    Callback executed when asynchronous enrollment completes. Updates program lock
    status and computes beneficiary statistics.

DefaultProgramManager
---------------------

The default implementation provides:

- **Automatic cycle creation**: Creates cycles with automatic naming (``Cycle 1``, ``Cycle 2``, etc.)
- **Beneficiary copying**: Optionally copies enrolled beneficiaries to new cycles
- **Asynchronous enrollment**: Uses job queues for large-scale eligibility checks
- **State management**: Handles draft, enrolled, and not_eligible states
- **Statistics computation**: Updates beneficiary counts after enrollment operations

Configuration Options
=====================

The default program manager supports the following configuration:

``number_of_cycles``
    Number of cycles to create (default: 1)

``copy_last_cycle_on_new_cycle``
    Whether to copy enrolled beneficiaries from the previous cycle (default: True)

Job Queue Integration
=====================

For programs with many beneficiaries, the enrollment process uses job queues:

- **MIN_ROW_JOB_QUEUE** (200): Below this threshold, enrollment runs synchronously
- **MAX_ROW_JOB_QUEUE** (10000): Batch size for asynchronous jobs

When the beneficiary count exceeds ``MIN_ROW_JOB_QUEUE``, enrollment is processed
in batches of ``MAX_ROW_JOB_QUEUE`` using background jobs.
