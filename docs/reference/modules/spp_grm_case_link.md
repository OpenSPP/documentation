---
openspp:
  doc_status: draft
---

# Case Link

**Module:** `spp_grm_case_link`

## Overview

Links GRM tickets with Case Management cases for escalation

## Purpose

This module is designed to:

- **Escalate GRM tickets to cases:** Provide a wizard-driven workflow for converting grievance tickets into formal case management records.
- **Link tickets and cases bidirectionally:** Track which GRM ticket originated a case and which cases have related tickets.
- **Create follow-up tickets from cases:** Allow case workers to create new GRM tickets linked to an existing case.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `spp_security` | Central security definitions for OpenSPP modules |
| `spp_grm` | Provides a centralized Grievance Redress Mechanism for re... |
| `spp_case_base` | Core case management functionality for OpenSPP |

## Key Features

### Ticket-to-Case Escalation Wizard

The escalation wizard (`spp.grm.escalate.wizard`) guides users through creating a case from a GRM ticket. The wizard presents the ticket details and allows configuration of the new case.

| Field | Description |
| --- | --- |
| Case Type | Type of case to create |
| Intensity Level | Level 1 (Low), Level 2 (Medium), or Level 3 (High) |
| Case Worker | Defaults to the ticket assignee |
| Supervisor | Optionally set from the selected team |
| Team | Team responsible for the case |
| Copy Description | Copy the ticket description as the case's presenting issue |
| Close Ticket | Optionally close the ticket after escalation with a decision code |

The wizard validates that the ticket is not already linked to a case, creates the case record, posts cross-reference messages on both the ticket and the case chatter, and optionally closes the ticket with a "Referred to Case" decision.

### Case Extensions

Cases gain the following fields from this module:

| Field | Description |
| --- | --- |
| Source GRM Ticket | The ticket that initiated this case |
| Related Tickets | All GRM tickets linked to this case |
| GRM Ticket Count | Computed count of related tickets |

Cases also gain an action to create follow-up GRM tickets pre-populated with the case's partner and context.

### Ticket Extensions

Tickets gain a `Related Case` field and a smart button to view the linked case or open the escalation wizard.

## Integration

- **spp_grm:** Extends `spp.grm.ticket` with a `case_id` field and escalation actions.
- **spp_case_base:** Extends `spp.case` with source ticket tracking and follow-up ticket creation.
- **Auto-install:** This module auto-installs when both `spp_grm` and `spp_case_base` are present.
