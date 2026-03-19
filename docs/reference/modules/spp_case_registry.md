---
openspp:
  doc_status: draft
---

# Registry Integration

**Module:** `spp_case_registry`

## Overview

OpenSPP Case Registry Integration module for OpenSPP.

## Purpose

This module is designed to:

- **Link cases to registrants and households:** Associate individual registrants, households, and household members with case records.
- **Detect previous cases:** Automatically find and display previous cases for the same registrant or household.
- **View cases from registrant profiles:** Add case counts and navigation actions to the registrant (res.partner) form.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `spp_security` | Central security definitions for OpenSPP modules |
| `spp_case_base` | Core case management functionality for OpenSPP |
| `spp_registry` | Consolidated registry management for individuals, groups,... |
| `spp_area` | Establishes direct associations between OpenSPP registran... |

## Key Features

### Registrant and Household Links

Cases are enriched with registry-specific fields for individual and group registrants.

| Field | Type | Description |
| --- | --- | --- |
| `registrant_id` | Many2one | Primary individual registrant (non-group) |
| `household_id` | Many2one | Related household (group registrant) |
| `household_member_ids` | Many2many | Other household members involved in the case |
| `area_id` | Many2one | Geographic area of the client |

When a registrant is selected, the household is auto-populated from group membership, and the area is loaded from the registrant's profile. When a household is selected, its members are auto-loaded.

### Previous Case Detection

The module automatically computes previous cases for the same registrant or household, enabling case workers to review history.

| Field | Type | Description |
| --- | --- | --- |
| `previous_case_ids` | Many2many | Previous cases for the same registrant/household |
| `previous_case_count` | Integer | Number of previous cases |

### Registrant-Side Case View

The `res.partner` model is extended with reverse links to cases:

| Field | Type | Description |
| --- | --- | --- |
| `case_registrant_ids` | One2many | Cases where this partner is the registrant |
| `case_household_ids` | One2many | Cases where this partner is the household |
| `case_count` | Integer | Total cases (as registrant or household) |
| `case_active_count` | Integer | Active cases only |

An action button on the partner form opens all related cases.

## Integration

- **spp_case_base:** Extends `spp.case` with registrant, household, and area fields.
- **spp_registry:** Uses `spp.group.membership` to resolve household memberships and populate household members.
- **spp_area:** Links cases to geographic areas via `spp.area`. Auto-installs when both `spp_case_base` and `spp_registry` are present.
