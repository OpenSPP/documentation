---
openspp:
  doc_status: draft
---

# Graduation Integration

**Module:** `spp_case_graduation`

## Overview

Link graduation assessments to cases for exit management

## Purpose

This module is designed to:

- **Link cases to graduation assessments:** Associate graduation assessment records with cases so that exit management is tracked within the case workflow.
- **Track graduation readiness:** Compute graduation status, readiness score, and assessment counts directly on the case record.
- **Create assessments from cases:** Provide quick actions to create new graduation assessments pre-filled with case and partner context.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `spp_security` | Central security definitions for OpenSPP modules |
| `spp_case_base` | Core case management functionality for OpenSPP |
| `spp_graduation` | Manage graduation and exit from time-bound social protect... |

## Key Features

### Graduation Tracking on Cases

Each case computes graduation statistics from its linked assessments, sorted by assessment date.

| Field | Type | Description |
| --- | --- | --- |
| `graduation_assessment_ids` | One2many | All assessments linked to the case |
| `graduation_assessment_count` | Integer | Number of assessments |
| `latest_graduation_assessment_id` | Many2one | Most recent assessment |
| `graduation_readiness` | Float | Readiness score from the latest assessment |

### Graduation Status

The `graduation_status` field is computed from the latest assessment's state and recommendation:

| Status | Condition |
| --- | --- |
| `not_assessed` | No assessments exist |
| `in_progress` | Latest assessment is in draft |
| `pending_approval` | Latest assessment is submitted |
| `approved` | Approved with "graduate" recommendation, no graduation date |
| `graduated` | Approved with graduation date set |
| `deferred` | Recommendation is "defer" |

### Assessment Back-Link

The module extends `spp.graduation.assessment` with a `case_id` field, enabling assessments to reference back to their originating case.

## Integration

- **spp_case_base:** Extends `spp.case` with graduation assessment fields and computed status.
- **spp_graduation:** Extends `spp.graduation.assessment` with a `case_id` Many2one field linking assessments back to cases.
