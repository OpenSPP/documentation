---
openspp:
  doc_status: draft
---

# Hazard & Emergency Management

**Module:** `spp_hazard`

## Overview

Provides hazard classification, incident recording, and impact assessment for emergency response. Links registrants to disaster events with geographic scope and severity tracking to enable targeted humanitarian assistance.

## Purpose

This module is designed to:

- **Classify hazard types:** Organize hazards in a hierarchical category tree (e.g., Natural > Storm > Typhoon) for standardized incident categorization.
- **Record hazard incidents:** Track specific disaster events with temporal scope, geographic areas, severity levels, and lifecycle status.
- **Assess impact on registrants:** Record how individual registrants are affected by incidents, including damage level, impact type, and verification status.
- **Identify affected populations:** Find registrants located in areas affected by an incident for targeted humanitarian response.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `base` | Odoo core framework |
| `spp_security` | Central security definitions for OpenSPP modules |
| `spp_registry` | Consolidated registry management for individuals, groups,... |
| `spp_area` | Establishes direct associations between OpenSPP registran... |
| `spp_gis` | GIS core plus area geo fields and importer extensions (po... |

## Key Features

### Hazard Categories

Categories (`spp.hazard.category`) organize hazard types in a parent-child hierarchy with computed full path names (e.g., "Natural > Storm > Typhoon").

| Field | Description |
| --- | --- |
| Name / Code | Category identifier (code must be unique) |
| Parent Category | Parent in the hierarchy |
| Subcategories | Child categories |
| Incident Count | Number of incidents using this category |

### Hazard Incidents

Incidents (`spp.hazard.incident`) represent specific disaster events with lifecycle tracking.

| Field | Description |
| --- | --- |
| Name / Code | Incident identifier (e.g., "Typhoon Yolanda") |
| Category | Hazard category classification |
| Start Date / End Date | Temporal scope (end date empty if ongoing) |
| Status | Alert, Active, Recovery, or Closed |
| Severity | Level 1 (Minor) through Level 5 (Catastrophic) |
| Affected Areas | Geographic areas impacted by the incident |
| Area Details | Per-area severity overrides, notes, and population estimates |

Incidents can identify potentially affected registrants by searching for all registrants located in the affected areas.

### Impact Types

Impact types (`spp.hazard.impact.type`) classify how registrants are affected. Each type belongs to a category: Physical, Economic, Health, or Social. Pre-installed types include Displacement, Property Damage, Livelihood Loss, Injury, and others.

### Hazard Impacts

Impact records (`spp.hazard.impact`) document how a specific registrant was affected by an incident.

| Field | Description |
| --- | --- |
| Incident | The hazard event |
| Registrant | The affected registrant |
| Impact Type | Classification of the impact |
| Damage Level | Minimal, Moderate, Severe, Critical, Partially Damaged, or Totally Damaged |
| Impact Date | Date when the impact occurred |
| Verification Status | Reported, Verified, Disputed, or Closed |
| Verified By / Date | User and timestamp of verification |

A `bulk_create_impacts` utility method creates impact records for all registrants in a given area, processing in batches of 500 and skipping duplicates.

### Registrant Extensions

The module extends `res.partner` with hazard impact tracking:

| Field | Description |
| --- | --- |
| Hazard Impacts | All impact records for this registrant |
| Impact Count | Total number of impact records |
| Has Active Impact | Whether the registrant has an impact from an active/alert/recovery incident |

### Geofence Extension

The module adds a "Hazard Zone" geofence type and an optional link to a hazard incident on geofence records.

## Integration

- **spp_registry:** Extends `res.partner` with impact tracking fields and the ability to query impact history.
- **spp_area:** Links incidents to geographic areas and uses area-based registrant lookup for affected population identification.
- **spp_gis:** Extends `spp.gis.geofence` with the "Hazard Zone" type and incident linkage.
- **mail:** Uses `mail.thread` and `mail.activity.mixin` on incidents and impacts for audit trail tracking.

```{toctree}
:maxdepth: 1
:hidden:

spp_hazard_programs
```
