---
openspp:
  doc_status: draft
---

# Change Request Types

**Module:** `spp_farmer_registry_cr`

## Overview

Farmer-specific change request types for farm details and activities

## Purpose

This module is designed to:

- **Update farm details via change requests:** Enable field officers to propose changes to farm classification (type, tenure, size) through an approval workflow before modifying the registry.
- **Manage farm activities via change requests:** Support adding, editing, and removing crop, livestock, and aquaculture activities through controlled change requests.
- **Manage land parcels via change requests:** Handle land parcel additions, updates, and removals with approval before applying to the farm record.
- **Manage farm assets via change requests:** Control asset and machinery changes through the change request workflow.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `spp_change_request_v2` | Configuration-driven change request system with UX improv... |
| `spp_farmer_registry` | Farmer Registry with vocabulary-based fields, CEL variabl... |
| `spp_land_record` | The OpenSPP Land Record module digitizes and centralizes ... |

## Key Features

### Change Request Types

The module registers four farmer-specific change request types via XML data:

| CR Type | Description |
| --- | --- |
| Update Farm Details | Modify farm type, holder type, land tenure, acreage, and other classification fields |
| Manage Farm Activity | Add, edit, or remove crop/livestock/aquaculture activities |
| Manage Land Parcel | Add, edit, or remove land parcel records |
| Manage Farm Asset | Add, edit, or remove farm assets and machinery |

### Operation Controls

Each change request type has configurable operation toggles:

| Toggle | Controls |
| --- | --- |
| `allow_activity_add/update/remove` | Whether activities can be added, edited, or removed |
| `allow_parcel_add/update/remove` | Whether land parcels can be added, edited, or removed |
| `allow_asset_add/update/remove` | Whether assets can be added, edited, or removed |

### Apply Strategies

Each CR type has a corresponding apply strategy that validates and applies changes to the farm registrant:

- **Update Farm Details:** Copies vocabulary-based fields and acreage values from the CR detail to the farm
- **Manage Farm Activity:** Creates, updates, or deletes activity records based on the operation type
- **Manage Land Parcel:** Creates, updates, or deletes land record entries
- **Manage Farm Asset:** Creates, updates, or deletes asset/machinery entries

## Integration

- **spp_change_request_v2:** Uses the V2 change request framework with detail models, apply strategies, and approval definitions.
- **spp_farmer_registry:** Targets farm registrants (groups with farm details) and applies changes to farm-specific fields and related records.
- **spp_land_record:** Land parcel change requests create or modify `spp.land.record` entries linked to farms.
