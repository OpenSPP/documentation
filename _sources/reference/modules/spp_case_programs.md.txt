---
openspp:
  doc_status: draft
---

# Programs Integration

**Module:** `spp_case_programs`

## Overview

Links cases to OpenSPP programs and provides compliance tracking

## Purpose

This module is designed to:

- **Link cases to program enrollments:** Associate program membership records with cases to provide program context within case management.
- **Track program-triggered cases:** Record which program triggered a case (e.g., non-compliance detection).
- **Display enrollment summaries:** Compute active program counts and enrolled program names directly on the case form.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `spp_security` | Central security definitions for OpenSPP modules |
| `spp_case_base` | Core case management functionality for OpenSPP |
| `spp_programs` | Manage cash and in-kind entitlements, integrate with inve... |

## Key Features

### Program Enrollment Tracking

When a partner is selected on a case, their program memberships are automatically loaded.

| Field | Type | Description |
| --- | --- | --- |
| `program_membership_ids` | Many2many | Program enrollments related to the case |
| `triggered_by_program_id` | Many2one | Program that triggered this case |
| `has_active_enrollment` | Boolean | Whether the client has active enrollments |
| `active_program_count` | Integer | Number of active program enrollments |
| `enrolled_program_names` | Char | Comma-separated list of enrolled program names |

Active enrollments include memberships in `enrolled` or `paused` states.

### Quick Actions

- **View program enrollments:** Open a list of all program memberships linked to the case.
- **View triggered program:** Navigate directly to the program that triggered the case.

## Integration

- **spp_case_base:** Extends `spp.case` with program enrollment fields and a triggering program reference.
- **spp_programs:** Reads from `spp.program.membership` to populate enrollment data and links to `spp.program` for the triggering program. Auto-installs when both `spp_case_base` and `spp_programs` are present.
