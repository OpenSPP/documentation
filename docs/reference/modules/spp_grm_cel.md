---
openspp:
  doc_status: draft
---

# CEL Rules

**Module:** `spp_grm_cel`

## Overview

CEL-based routing and escalation rules for GRM tickets

## Purpose

This module is designed to:

- **Route tickets automatically:** Evaluate CEL expressions against incoming tickets and assign them to the appropriate team, user, severity, and priority.
- **Escalate tickets by rule:** Automatically escalate tickets based on CEL conditions and time-based triggers, updating severity, priority, and assignees.
- **Schedule periodic escalation checks:** Run a cron job to evaluate escalation rules against all open tickets on a recurring basis.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `spp_security` | Central security definitions for OpenSPP modules |
| `spp_grm` | Provides a centralized Grievance Redress Mechanism for re... |
| `spp_cel_domain` | Write simple CEL-like expressions to filter records (Open... |
| `spp_case_base` | Core case management functionality for OpenSPP |

## Key Features

### Routing Rules

Routing rules (`spp.grm.routing.rule`) automatically assign newly created tickets based on CEL conditions. Rules are evaluated in sequence order, and the first matching rule is applied.

| Field | Description |
| --- | --- |
| Condition (CEL) | CEL expression evaluated against ticket properties |
| Assign to Team | Team to assign the ticket to |
| Assign to User | User to assign the ticket to |
| Set Severity | Override ticket severity (low, medium, high, critical) |
| Set Priority | Override ticket priority |
| Match Count | Statistics counter for how many tickets matched this rule |

CEL expressions have access to context variables including `ticket`, `category`, `channel`, `stage`, `severity`, `priority`, `partner`, `team`, `user`, and helper functions like `days_since()`, `hours_since()`, and `is_business_day()`.

### Escalation Rules

Escalation rules (`spp.grm.escalation.rule`) automatically escalate tickets when conditions are met. Unlike routing rules, multiple escalation rules can apply to the same ticket.

| Field | Description |
| --- | --- |
| Condition (CEL) | CEL expression evaluated against ticket properties |
| Trigger After Hours | Time-based trigger (escalate if ticket is open longer than N hours) |
| Escalate to User | User to escalate to |
| Escalate to Team | Team to escalate to |
| Escalate Severity/Priority | Increase severity or priority to a specified level |
| Send Notification | Send email using a configured mail template |
| Create Case | Automatically create a case management record |
| Case Type | Type of case to create when escalating |

### Ticket Extension

The module extends `spp.grm.ticket` to:

- Apply routing rules automatically on ticket creation.
- Check escalation rules when the ticket stage changes.
- Track which routing rule and escalation rules were applied to each ticket.
- Provide a manual "Escalate" action for on-demand escalation rule evaluation.

### Scheduled Escalation Check

A cron job (`check_escalations`) periodically searches all open tickets and evaluates active escalation rules against them. This enables time-based escalation scenarios (e.g., escalate if no response within 48 hours).

## Integration

- **spp_cel_domain:** Uses the CEL parser to validate and evaluate rule conditions against ticket context.
- **spp_grm:** Extends `spp.grm.ticket` with automatic routing on create and escalation on stage change.
- **spp_case_base:** Optionally creates `spp.case` records as part of escalation actions.
- **Auto-install:** This module auto-installs when both `spp_grm` and `spp_cel_domain` are present.
