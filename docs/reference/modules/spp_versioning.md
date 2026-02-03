---
openspp:
  doc_status: draft
---

# Versioning


## Overview

The Versioning module provides a unified framework for managing version history and lifecycle of any artifact in OpenSPP. It enables snapshot creation, scheduled activation with future effective dates, optional approval workflows, and usage tracking to prevent archiving artifacts that are in use.

## Purpose

This module is designed to:

- **Maintain version history:** Create snapshots of configuration artifacts over time
- **Schedule future changes:** Set effective dates for versions to activate automatically
- **Control quality:** Enforce test gates and approval workflows before publishing
- **Track dependencies:** Monitor which programs or processes use each artifact to prevent breaking changes

## Module Dependencies

| Dependency       | Description                            |
| ---------------- | -------------------------------------- |
| **spp_security** | OpenSPP security groups and privileges |
| **mail**         | Activity tracking and notifications    |

## Key Features

### Versioned Mixin

Any model can inherit versioning capabilities by using the `spp.versioned.mixin`:

| Field                 | Description                                 |
| --------------------- | ------------------------------------------- |
| is_test_pass_required | Require all tests to pass before publishing |
| is_approval_required  | Require approval workflow before activation |

### Version States

| State      | Description                  |
| ---------- | ---------------------------- |
| Draft      | Initial state, can be edited |
| Scheduled  | Waiting for effective date   |
| Current    | Active version in use        |
| Superseded | Replaced by a newer version  |

### Snapshot Fields

Configure which fields to capture in version snapshots with different strategies:

| Strategy    | Description                                    |
| ----------- | ---------------------------------------------- |
| **shallow** | Store only IDs for related records             |
| **embed**   | Store IDs plus snapshot of related record data |
| **follow**  | Cascade versioning to related records          |

### Scheduled Activation

Versions can be scheduled to activate at a future date:

1. Create a new version with changes
2. Set the effective date
3. A scheduled job activates the version when the date arrives
4. Previous version automatically becomes "Superseded"

### Test Gate

When enabled, the test gate prevents publishing until all associated tests pass:

- Configured per artifact with `is_test_pass_required`
- Checks test records returned by `_get_test_records()`
- Blocks publishing if any test has status other than "passed"

### Approval Workflow

Optional approval can be required before versions activate:

- Configured per artifact with `is_approval_required`
- Integrates with OpenSPP approval system
- Versions wait in "Pending Approval" until approved

### Usage Tracking

The module tracks which artifacts are used by other records:

| Information Tracked | Description                    |
| ------------------- | ------------------------------ |
| Consumer Model      | The model using the artifact   |
| Consumer Record     | The specific record using it   |
| Usage Type          | How the artifact is being used |

This prevents archiving artifacts that are actively used.

## Integration

The Versioning module integrates with:

- **spp_studio:** Versions logic expressions and computed fields
- **spp_programs:** Tracks eligibility criteria and indicator definitions
- **spp_approval:** Provides approval workflow for sensitive version changes

## Developer Usage

To add versioning to a model:

```python
class MyModel(models.Model):
    _inherit = ["my.model", "spp.versioned.mixin"]

    def _get_version_snapshot_fields(self):
        return [
            "name",                      # scalar field
            "description",               # scalar field
            "category_id",               # relation (shallow by default)
            ("program_id", "embed"),     # relation with embed strategy
            ("variable_ids", "follow"),  # cascade version to related
        ]

    def _get_test_records(self):
        return self.test_ids  # Return associated test records
```

## Are you stuck?

### Cannot publish version - tests failing

**Symptom:** Error "X test(s) must pass before publishing"

**Cause:** The artifact has test gate enabled and some tests are not passing

**Solution:** Run the failing tests listed in the error message. Fix any issues and ensure all tests show "passed" status before attempting to publish.

### Cannot archive artifact - in use

**Symptom:** Error "Cannot archive: used by X program(s)"

**Cause:** The artifact is referenced by active programs or other records

**Solution:** Remove the artifact from all programs or records using it before archiving. Use the "View Usages" action to see where it is used.

### Scheduled version did not activate

**Symptom:** A version scheduled for a past date is still in "Scheduled" state

**Cause:** The scheduled job may not have run, or there was an error during activation

**Solution:** Check the scheduled actions in Odoo settings. Verify the cron job for version activation is active and running. Check system logs for any errors.

### Version history not showing

**Symptom:** No versions appear in the version history

**Cause:** No versions have been created for this artifact yet

**Solution:** Use the "Create Version" action to create a snapshot of the current state. This initializes the version history.
