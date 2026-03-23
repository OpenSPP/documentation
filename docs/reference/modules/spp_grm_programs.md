---
openspp:
  doc_status: draft
---

# Programs Integration

**Module:** `spp_grm_programs`

## Overview

Link GRM tickets to OpenSPP programs, entitlements, and payments

## Purpose

This module is designed to:

- **Link GRM tickets to programs:** Associate grievance tickets with specific programs, program memberships, cycles, entitlements, and payments.
- **Display program context on tickets:** Show enrollment status, entitlement amounts, and payment amounts directly on the ticket form.
- **Auto-fill related fields:** Cascade field values when a program, membership, cycle, entitlement, or payment is selected on a ticket.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `spp_security` | Central security definitions for OpenSPP modules |
| `spp_grm` | Provides a centralized Grievance Redress Mechanism for re... |
| `spp_programs` | Manage cash and in-kind entitlements, integrate with inve... |

## Key Features

### Program-Related Fields on Tickets

The module adds the following fields to `spp.grm.ticket`:

| Field | Description |
| --- | --- |
| Related Program | The program related to the complaint |
| Program Membership | Specific enrollment related to the complaint |
| Program Cycle | Specific cycle related to the complaint |
| Related Entitlement | Specific entitlement being disputed |
| Related Payment | Specific payment being disputed |
| Enrollment Status | Computed from the linked program membership state |
| Entitlement Amount | Computed from the linked entitlement record |
| Payment Amount | Computed from the linked payment record |

### Cascading Field Auto-Fill

When a user selects a value in one of the program-related fields, downstream fields are automatically populated:

- Selecting a **registrant and program** auto-fills the program membership.
- Selecting a **program membership** auto-fills the program and registrant.
- Selecting a **cycle** auto-fills the program and clears entitlement/payment.
- Selecting an **entitlement** auto-fills the cycle, program, and registrant.
- Selecting a **payment** auto-fills the entitlement, cycle, and registrant.

### Navigation Actions

Smart buttons allow navigating directly from a ticket to the related program, entitlement, or payment record.

## Integration

- **spp_grm:** Extends `spp.grm.ticket` with program-related fields and onchange logic.
- **spp_programs:** Links to `spp.program`, `spp.program.membership`, `spp.cycle`, `spp.entitlement`, and `spp.payment` models.
- **Auto-install:** This module auto-installs when both `spp_grm` and `spp_programs` are present.
