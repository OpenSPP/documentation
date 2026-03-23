---
openspp:
  doc_status: draft
---

# Session Integration

**Module:** `spp_case_session`

## Overview

Link sessions and training attendance to cases

## Purpose

This module is designed to:

- **Link cases to required sessions:** Associate training or group sessions with cases so attendance requirements are tracked.
- **Compute attendance compliance:** Calculate attendance rates and determine compliance status based on session participation.
- **View cases from sessions:** Provide a reverse link so sessions display their related cases.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `spp_security` | Central security definitions for OpenSPP modules |
| `spp_case_base` | Core case management functionality for OpenSPP |
| `spp_session_tracking` | Track attendance at required sessions and trainings for s... |

## Key Features

### Session Tracking on Cases

Cases track required sessions and the client's attendance at those sessions.

| Field | Type | Description |
| --- | --- | --- |
| `session_ids` | Many2many | Sessions the client is expected to attend |
| `session_attendance_ids` | One2many | Attendance records for linked sessions |
| `session_count` | Integer | Number of required sessions |

### Attendance Compliance

The module computes an attendance rate and assigns a compliance level:

| Field | Type | Description |
| --- | --- | --- |
| `session_attendance_rate` | Float | Percentage of required sessions attended |
| `session_compliance` | Selection | Compliance status based on attendance rate |

Compliance thresholds:

| Status | Attendance Rate |
| --- | --- |
| `compliant` | 80% or higher |
| `partial` | 50% to 79% |
| `non_compliant` | Below 50% |
| `not_applicable` | No required sessions |

### Session Back-Link

The `spp.session` model is extended with:

| Field | Type | Description |
| --- | --- | --- |
| `case_ids` | Many2many | Cases that require attendance at this session |
| `case_count` | Integer | Number of related cases |

## Integration

- **spp_case_base:** Extends `spp.case` with session tracking fields and compliance computation.
- **spp_session_tracking:** Links to `spp.session` and reads `spp.session.attendance` records to compute attendance rates. Extends `spp.session` with a reverse link to cases.
