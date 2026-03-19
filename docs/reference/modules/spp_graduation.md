---
openspp:
  doc_status: draft
---

# Graduation Management

**Module:** `spp_graduation`

## Overview

Manage graduation and exit from time-bound social protection programs

## Purpose

This module is designed to:

- **Define graduation pathways:** Configure structured exit paths from social protection programs, distinguishing between positive exits (graduation) and negative exits (removal).
- **Assess beneficiary readiness:** Record and score criteria-based assessments to determine whether a beneficiary is ready to graduate from a program.
- **Manage approval workflows:** Route graduation assessments through draft, submitted, approved, and rejected states with full audit tracking.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `base` | Odoo core framework |
| `spp_registry` | Consolidated registry management for individuals, groups,... |
| `spp_security` | Central security definitions for OpenSPP modules |
| `mail` | Communication and activity tracking |

### External Dependencies

| Package | Purpose |
| --- | --- |
| `python-dateutil` | Date arithmetic for computing post-graduation monitoring end dates |

## Key Features

### Graduation Pathways

Pathways define how beneficiaries exit a program. Each pathway specifies whether the exit is positive (graduation) or negative (removal), and whether an assessment and approval are required.

| Field | Description |
| --- | --- |
| Name / Code | Identifier for the pathway |
| Is Positive Exit | Distinguishes graduation from removal |
| Is Assessment Required | Whether a formal assessment must be completed |
| Is Approval Required | Whether a supervisor must approve the exit |
| Post Graduation Monitoring Months | Duration of monitoring after graduation (default: 12 months) |

### Graduation Criteria

Each pathway has one or more criteria that define what readiness means. Criteria are weighted and can be marked as required (must be met regardless of overall score).

| Field | Description |
| --- | --- |
| Name / Code | Identifier for the criterion |
| Weight | Relative importance in the overall score calculation (must be > 0) |
| Assessment Method | Self Report, Verification Required, Computed from Data, or Field Observation |
| Is Required | If true, must be individually met regardless of overall score |

### Graduation Assessments

Assessments evaluate a beneficiary against a pathway's criteria. Each assessment includes criteria responses with scores (0-1), evidence attachments, and an overall recommendation.

| Field | Description |
| --- | --- |
| Beneficiary | The registrant being assessed |
| Pathway | The graduation pathway used for evaluation |
| Assessor | User conducting the assessment |
| Readiness Score | Computed weighted average of criteria response scores (0-1) |
| Is Required Criteria Met | Whether all required criteria have been individually met |
| Recommendation | Graduate, Extend Participation, Exit (Non-graduation), or Defer Assessment |
| State | Draft, Submitted, Approved, or Rejected |

When an assessment is approved with a "Graduate" recommendation, the graduation date is automatically set. The monitoring end date is computed based on the pathway's post-graduation monitoring period.

## Integration

- **spp_registry:** Links assessments to registrants via `partner_id` with domain filtering for `is_registrant = True`.
- **mail:** Uses `mail.thread` and `mail.activity.mixin` on assessments for chatter-based audit trails and state change tracking.
