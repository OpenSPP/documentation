---
openspp:
  doc_status: draft
---

# Case Management Base

**Module:** `spp_case_base`

## Overview

Core case management functionality for OpenSPP

## Purpose

This module is designed to:

- **Manage social protection cases:** Create and track cases for individuals, households, or groups through a configurable stage-based workflow.
- **Plan and track interventions:** Build versioned intervention plans with goals, expected outcomes, and individual intervention tasks that track progress.
- **Record case activities:** Log visits (home, office, phone, virtual), case notes, assessments, and service referrals with full history.
- **Automate review scheduling:** Cron-based reminders for overdue and upcoming case reviews with Odoo activity integration.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `base` | Odoo core framework |
| `mail` | Communication and activity tracking |
| `portal` | Portal access capabilities |
| `spp_security` | Central security definitions for OpenSPP modules |

## Key Features

### Case Records

Each case (`spp.case`) tracks a client through the case management lifecycle with these core attributes:

| Field | Description |
| --- | --- |
| Case Number | Auto-generated reference (e.g., CASE-2026-00001) |
| Case Type | Configurable type classification |
| Intensity Level | Level 1 (Low), Level 2 (Medium), or Level 3 (High) |
| Priority | Low, Medium, High, or Urgent |
| Client | Link to a `res.partner` record (individual, household, or group) |
| Stage | Configurable workflow stage (supports kanban views) |
| Case Worker | Assigned user responsible for the case |
| Supervisor / Team | Optional supervisory assignment |
| Intake Source | Walk-in, referral, outreach, GRM, program enrollment, or other |

Cases also track risk factors, vulnerabilities, presenting issues, review dates, and closure information (reason, outcome, summary).

### Workflow Stages

Stages (`spp.case.stage`) are fully configurable with:

- Phase classification (intake, assessment, planning, implementation, monitoring, closure)
- Closed flag for terminal stages
- Plan requirement flag (blocks entry if no approved intervention plan)
- Minimum intensity level requirement
- Kanban view support with `group_expand`

### Intervention Plans

Plans (`spp.case.intervention.plan`) support a versioned approval workflow:

| State | Description |
| --- | --- |
| Draft | Initial creation |
| Pending Approval | Submitted for supervisor review |
| Approved | Approved with recorded approver and date |
| Active | Currently being implemented |
| Completed | All interventions finished |
| Revised | Superseded by a new version |

Each plan version links to its predecessor. Only one plan per case can be marked as current. Plans contain individual interventions (`spp.case.intervention`) with target dates, completion tracking, and progress percentage calculation.

### Case Activities

| Model | Description |
| --- | --- |
| `spp.case.visit` | Home, office, phone, or virtual visits with purpose and notes |
| `spp.case.note` | Progress notes, assessments, general notes, and supervision notes |
| `spp.case.referral` | Service referrals with status tracking |
| `spp.case.assessment` | Structured assessments linked to cases |

### Review Management

A cron job checks for overdue case reviews and creates Odoo activities for case workers:

- Overdue reviews generate immediate todo activities
- Reviews due within 3 days generate warning activities (if not already created)
- Review frequency is configurable per case type, defaulting to 30 days

### Case Configuration

| Model | Description |
| --- | --- |
| `spp.case.type` | Case type definitions with default intensity and review frequency |
| `spp.case.stage` | Workflow stage configuration |
| `spp.case.risk.factor` | Risk factor taxonomy |
| `spp.case.vulnerability` | Vulnerability taxonomy |
| `spp.case.closure.reason` | Closure reason options |
| `spp.case.team` | Team definitions with members and supervisor |

## Integration

- **mail:** Cases and intervention plans inherit `mail.thread` for change tracking. Cases also inherit `mail.activity.mixin` for scheduled review activities.
- **spp_security:** Security groups and record rules control access to case data based on user roles.
- **spp_case_cel:** Extends case creation to apply CEL-based triage and assignment rules automatically (optional module).
- **spp_case_demo:** Provides a demo data generator for populating case management with realistic test data (optional module).

```{toctree}
:maxdepth: 1
:hidden:

spp_case_cel
spp_case_demo
spp_case_entitlements
spp_case_graduation
spp_case_programs
spp_case_registry
spp_case_session
```
