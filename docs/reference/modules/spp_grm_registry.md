---
openspp:
  doc_status: draft
---

# Registry Integration

**Module:** `spp_grm_registry`

## Overview

Link GRM tickets to OpenSPP registry (registrants)

## Purpose

This module is designed to:

- **Link GRM tickets to registrants:** Associate grievance tickets with individual registrants, their households, and geographic areas from the OpenSPP registry.
- **Detect repeat tickets:** Automatically identify when a registrant has filed multiple tickets within the last six months.
- **Display ticket history on registrant profiles:** Show GRM ticket counts and actions on registrant and household partner records.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `spp_security` | Central security definitions for OpenSPP modules |
| `spp_grm` | Provides a centralized Grievance Redress Mechanism for re... |
| `spp_registry` | Consolidated registry management for individuals, groups,... |

## Key Features

### Registry Fields on Tickets

The module adds the following fields to `spp.grm.ticket`:

| Field | Description |
| --- | --- |
| Registrant | Individual registrant filing the complaint (filtered by household) |
| Household | Household group related to the complaint |
| Geographic Area | Area of the registrant |

When a registrant is selected, the ticket's `partner_id` and `area_id` are automatically populated. Changing the household clears the registrant selection.

### Repeat Ticket Detection

The module automatically computes repeat ticket information for each ticket:

| Field | Description |
| --- | --- |
| Repeat Count | Number of tickets from the same registrant in the last 6 months |
| Is Repeat | Boolean flag indicating whether this is a repeat ticket |
| Previous Tickets | Links to the registrant's other recent tickets |

A "View Previous Tickets" action allows quick navigation to the registrant's ticket history.

### Registrant Profile Extension

The module extends `res.partner` with GRM ticket tracking:

| Field | Description |
| --- | --- |
| GRM Tickets (Registrant) | All tickets where this partner is the registrant |
| Total GRM Tickets | Count of all tickets filed by this registrant |
| Open GRM Tickets | Count of currently open tickets |
| GRM Tickets (Household) | All tickets related to this household |
| Household GRM Tickets | Count of household-level tickets |

Smart buttons on the partner form allow viewing tickets as either registrant or household.

## Integration

- **spp_grm:** Extends `spp.grm.ticket` with registrant, household, and area fields plus repeat detection.
- **spp_registry:** Uses `res.partner` with `is_registrant` and `is_group` domain filters, and reads `area_id` and `individual_membership_ids` for auto-fill.
- **Auto-install:** This module auto-installs when both `spp_grm` and `spp_registry` are present.
