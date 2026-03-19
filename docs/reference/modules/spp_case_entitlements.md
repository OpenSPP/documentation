---
openspp:
  doc_status: draft
---

# Entitlements Integration

**Module:** `spp_case_entitlements`

## Overview

Links cases to program entitlements for case-entitlement relationship management

## Purpose

This module is designed to:

- **Link cases to entitlements:** Associate program entitlements with case records for unified case-entitlement tracking.
- **Track entitlement status:** Compute and store counts of total, approved, and pending entitlements per case.
- **Calculate entitlement values:** Sum the total monetary value of approved entitlements linked to a case.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `spp_security` | Central security definitions for OpenSPP modules |
| `spp_case_base` | Core case management functionality for OpenSPP |
| `spp_programs` | Manage cash and in-kind entitlements, integrate with inve... |

## Key Features

### Entitlement Relationship

Cases are linked to entitlements through a many-to-many relationship. When a partner is selected on a case, entitlements for that partner are automatically loaded.

| Field | Type | Description |
| --- | --- | --- |
| `entitlement_ids` | Many2many | Entitlements related to the case |
| `entitlement_count` | Integer | Total number of linked entitlements |
| `has_entitlements` | Boolean | Whether the case has any entitlements |

### Status Tracking

The module computes entitlement status breakdowns from linked entitlement states.

| Field | Type | Description |
| --- | --- | --- |
| `approved_entitlement_count` | Integer | Number of approved entitlements |
| `pending_entitlement_count` | Integer | Number of pending entitlements |
| `total_entitlement_amount` | Monetary | Sum of approved entitlement amounts |

### Quick Actions

The module provides action buttons to view filtered entitlement lists directly from a case:

- View all entitlements
- View only approved entitlements
- View only pending entitlements

## Integration

- **spp_case_base:** Extends the `spp.case` model with entitlement fields and computed statistics.
- **spp_programs:** Reads from `spp.entitlement` records to populate case-level entitlement data. Auto-installs when both `spp_case_base` and `spp_programs` are present.
