---
openspp:
  doc_status: draft
---

# CEL Rules

**Module:** `spp_case_cel`

## Overview

CEL-based triage and assignment rules for case management

## Purpose

This module is designed to:

- **Automatically triage new cases:** Evaluate CEL expressions against case properties on creation to set intensity level, priority, case type, risk factors, and vulnerabilities.
- **Automatically assign cases:** Match cases to teams and workers based on CEL conditions, with optional workload balancing across team members.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `spp_security` | Central security definitions for OpenSPP modules |
| `spp_case_base` | Core case management functionality for OpenSPP |
| `spp_cel_domain` | Write simple CEL-like expressions to filter records (Open... |

## Key Features

### Triage Rules

Triage rules (`spp.case.triage.rule`) automatically categorize and prioritize new cases. Rules are evaluated in sequence order, and the first matching rule is applied.

| Field | Description |
| --- | --- |
| Condition (CEL) | CEL expression evaluated against case context |
| Set Intensity Level | Override intensity to Level 1, 2, or 3 |
| Set Priority | Override priority to low, medium, high, or urgent |
| Set Case Type | Override the case type |
| Add Risk Factors | Risk factors to attach to matching cases |
| Add Vulnerabilities | Vulnerabilities to attach to matching cases |

Available context variables in CEL expressions: `case`, `client`, `case_type`, `intake_source`, `client_type`, `presenting_issue`, `risk_factors`, `vulnerabilities`.

### Assignment Rules

Assignment rules (`spp.case.assignment.rule`) determine which case worker or team should handle a case. Rules are evaluated in sequence order after triage, only when no case worker is already assigned.

| Field | Description |
| --- | --- |
| Condition (CEL) | CEL expression evaluated against case context |
| Assign to Team | Team to assign the case to |
| Assign to Worker | Specific case worker to assign |
| Assign Supervisor | Supervisor to assign |
| Consider Workload | If enabled, assigns to the team member with the lowest active caseload |
| Max Cases per Worker | Skip workers at or above this active case count (default 25) |

Available context variables: `case`, `case_type`, `intensity`, `priority`, `client`, `client_type`, `intake_source`.

### Workload Balancing

When workload consideration is enabled on an assignment rule, the module counts each team member's active cases and assigns the case to the member with the lowest caseload, skipping anyone who has reached the maximum case limit.

### Match Statistics

Both triage and assignment rules track how many cases they have matched, providing visibility into rule effectiveness.

## Integration

- **spp_case_base:** Extends the `spp.case` model's `create()` method to apply triage rules first, then assignment rules. This runs automatically on every new case.
- **spp_cel_domain:** CEL expressions are parsed and evaluated using the `cel_parser` module. Expressions support comparison operators, boolean logic, and access to Odoo record fields through the context variables.
