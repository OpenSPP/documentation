---
openspp:
  doc_status: draft
---

# Programs Integration

**Module:** `spp_hazard_programs`

## Overview

Links hazard impacts to program eligibility and entitlements. Enables emergency programs to use hazard data for targeting and benefit calculation.

## Purpose

This module is designed to:

- **Link programs to hazard incidents:** Associate social protection programs with the disaster incidents they respond to, enabling emergency-mode operations.
- **Determine emergency eligibility:** Identify registrants eligible for a program based on verified hazard impacts and qualifying damage levels.
- **Track response programs per incident:** View which programs are responding to a given incident and how many registrants are potentially affected.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `spp_hazard` | Provides hazard classification, incident recording, and i... |
| `spp_programs` | Manage cash and in-kind entitlements, integrate with inve... |

## Key Features

### Program Extension

The module adds the following fields to `spp.program`:

| Field | Description |
| --- | --- |
| Target Incidents | Hazard incidents this program responds to |
| Is Emergency Program | Computed; true if any target incident is in alert, active, or recovery status |
| Qualifying Damage Levels | Minimum damage level for eligibility: Any, Moderate and Above, Severe and Above, or Critical/Totally Damaged Only |
| Emergency Mode | When enabled, relaxed compliance rules apply |
| Potentially Affected Registrants | Computed count of registrants with verified impacts meeting the damage threshold |

The `get_emergency_eligible_registrants` method returns all registrants who have verified impacts from the program's target incidents and meet the qualifying damage level threshold.

### Incident Extension

Incidents gain a `Response Programs` field showing which programs are linked, along with a program count and a navigation action to view those programs.

## Integration

- **spp_hazard:** Extends `spp.hazard.incident` with a many-to-many link to programs. Reads `spp.hazard.impact` records to compute eligible registrants based on verification status and damage level.
- **spp_programs:** Extends `spp.program` with emergency response fields, damage level thresholds, and registrant eligibility queries.
- **Auto-install:** This module auto-installs when both `spp_hazard` and `spp_programs` are present.
