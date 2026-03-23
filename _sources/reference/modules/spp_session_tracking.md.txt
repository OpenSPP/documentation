---
openspp:
  doc_status: draft
---

# Session Tracking

**Module:** `spp_session_tracking`

## Overview

Track attendance at required sessions and trainings for social protection programs

## Purpose

This module is designed to:

- **Schedule and manage sessions:** Create training sessions, workshops, or meetings with defined types, facilitators, and participants.
- **Track attendance:** Record which participants attended each session, including excused absences with reasons.
- **Monitor compliance:** Calculate attendance rates against expected participants and minimum attendance thresholds.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `base` | Odoo core framework |
| `mail` | Communication and activity tracking |
| `spp_area` | Establishes direct associations between OpenSPP registran... |
| `spp_security` | Central security definitions for OpenSPP modules |

## Key Features

### Session Types

Define reusable session type configurations:

| Field | Description |
| --- | --- |
| Name / Code | Identifier for the session type |
| Frequency | Weekly, Bi-weekly, Monthly, Quarterly, or One-time |
| Required Attendance % | Minimum attendance percentage for compliance (default: 80%) |
| Duration (Hours) | Default session length |
| Track Topics | Whether to track which topics are covered per session |
| Topics | List of topics available for this session type |

### Sessions

Each session represents a scheduled event:

| Field | Description |
| --- | --- |
| Session Type | Links to a session type configuration |
| Date / Start Time / End Time | Scheduling with automatic duration calculation |
| Facilitator / Co-Facilitators | Assigned users responsible for the session |
| Location / Area | Physical location and linked geographic area |
| Expected Participants | Registrants expected to attend |
| Max Participants | Optional capacity limit |
| Topics Covered | Topics addressed during the session (when topic tracking is enabled) |
| State | Scheduled, In Progress, Completed, or Cancelled |

Sessions follow a strict state workflow: Scheduled can transition to In Progress or Cancelled; In Progress can transition to Completed or Cancelled. Completed and Cancelled are terminal states.

### Attendance Records

Each attendance record links a participant to a session:

| Field | Description |
| --- | --- |
| Participant | The registrant who was expected or attended |
| Attended | Whether the participant was present |
| Attendance Time | Timestamp of attendance |
| Excused | Whether the absence was excused |
| Excuse Reason | Reason for excused absence |

A unique constraint ensures each participant has only one attendance record per session. Attendance count and rate are computed automatically based on attended records versus expected participants.

## Integration

- **spp_area:** Sessions can be linked to geographic areas for location-based reporting and analysis.
- **mail:** Sessions inherit mail.thread for activity tracking and change logging.
