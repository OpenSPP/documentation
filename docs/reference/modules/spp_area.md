---
openspp:
  doc_status: draft
---

# OpenSPP Area Management


## Overview

OpenSPP Area Management establishes direct associations between registrants, beneficiary groups, and their corresponding geographical administrative areas. It validates registrant-area linkages against official area types and supports hierarchical area structures for geographic targeting and access control.

## Purpose

This module is designed to:

- **Define geographic hierarchies:** Establish multi-level area structures (Country, Region, District, Village, etc.).
- **Link registrants to locations:** Associate individuals and groups with specific administrative areas.
- **Enable geographic targeting:** Support program targeting based on location criteria.
- **Control area-based access:** Restrict user access to data within assigned geographic areas.
- **Validate area assignments:** Ensure registrant locations match valid area types in the hierarchy.

## Module Dependencies

| Dependency        | Purpose                                   |
| ----------------- | ----------------------------------------- |
| `base`            | Odoo core framework                       |
| `spp_base_common` | OpenSPP main menu and configuration       |
| `spp_user_roles`  | Area-based role assignments               |
| `spp_registry`    | Registrant models for area linking        |
| `queue_job`       | Background processing for bulk operations |
| `spp_security`    | Security groups and access control        |

### External Dependencies

| Package    | Purpose                                 |
| ---------- | --------------------------------------- |
| `openpyxl` | Excel file support for area data import |

## Key Features

### Area Hierarchy

Define multi-level geographic structures:

| Level   | Example              | Typical Use                   |
| ------- | -------------------- | ----------------------------- |
| Level 1 | Country              | Top-level container           |
| Level 2 | Region/State         | Major administrative division |
| Level 3 | District/County      | Local government area         |
| Level 4 | Municipality/Commune | Township level                |
| Level 5 | Village/Ward         | Community level               |

### Area Types

Configure area types to define the hierarchy:

| Field       | Purpose                         |
| ----------- | ------------------------------- |
| Name        | Display name for the area type  |
| Level       | Position in hierarchy (1 = top) |
| Parent Type | Required parent area type       |

### Area Records

Each area contains:

| Field  | Description                         |
| ------ | ----------------------------------- |
| Name   | Official area name                  |
| Code   | Unique identifier code              |
| Type   | Area type from configured hierarchy |
| Parent | Parent area in hierarchy            |
| Tags   | Classification tags                 |

### Area Import

Bulk import areas from external sources:

- Excel file upload with hierarchical data
- Language-specific name imports
- Validation against area type hierarchy
- Background processing for large datasets

### Area Tags

Categorize areas for filtering and targeting:

| Use Case                | Example Tags                     |
| ----------------------- | -------------------------------- |
| Program targeting       | "Urban", "Rural", "Coastal"      |
| Priority classification | "High Priority", "Vulnerable"    |
| Administrative          | "Active", "Merged", "Deprecated" |

## Integration

### With Registry

Registrants are assigned to areas:

| Registrant Type | Area Assignment     |
| --------------- | ------------------- |
| Individual      | Residence area      |
| Group           | Group location area |

Area assignment enables:

- Geographic filtering in searches
- Location-based eligibility criteria
- Area-restricted data access

### With User Roles

Area-based access control flow:

```
User Role Assignment
    ├── Role Type (Global or Local)
    ├── Permission Level (Viewer, Officer, Manager)
    └── Area Assignment (for Local roles)
            └── Access limited to assigned area and children
```

### With Programs

Geographic targeting for programs:

| Feature     | How Areas Are Used                    |
| ----------- | ------------------------------------- |
| Eligibility | Include/exclude registrants by area   |
| Targeting   | Focus programs on specific regions    |
| Reporting   | Aggregate results by geographic level |

### Configuration Flow

1. **Define Area Types:** Set up your geographic hierarchy
2. **Import/Create Areas:** Populate the area tree
3. **Assign Registrants:** Link individuals and groups to areas
4. **Configure User Access:** Assign local roles with area restrictions

## Views

### Individual Integration

Area fields appear on individual records:

| Field | Purpose                             |
| ----- | ----------------------------------- |
| Area  | Primary residence/registration area |

### Group Integration

Area fields appear on group records:

| Field | Purpose                          |
| ----- | -------------------------------- |
| Area  | Group location/registration area |

### User Integration

Area assignments for access control:

| Field          | Purpose                                     |
| -------------- | ------------------------------------------- |
| Assigned Areas | Areas the user can access (for local roles) |

## Technical Details

| Property       | Value        |
| -------------- | ------------ |
| Technical Name | `spp_area`   |
| Category       | OpenSPP/Core |
| Version        | 19.0.1.3.1   |
| License        | LGPL-3       |
| Application    | Yes          |

## Are you stuck?

### Cannot assign area to registrant

**Symptom:** Area dropdown shows no options or wrong areas.

**Cause:** Area type validation may be restricting available areas.

**Solution:** Check that:

1. Areas exist at the expected level in the hierarchy
2. The registrant type allows the area type being selected
3. User has permission to view the areas

### Area import failing

**Symptom:** Excel import shows errors or incomplete data.

**Cause:** Data may not match expected hierarchy or format.

**Solution:**

1. Verify Excel columns match expected format
2. Ensure parent areas are imported before children
3. Check for duplicate codes
4. Review import log for specific errors

### User cannot see registrants in their area

**Symptom:** Local role user sees no data despite area assignment.

**Cause:** Area assignment may not include child areas, or registrants not properly linked.

**Solution:**

1. Verify user's area assignment includes the correct hierarchy
2. Check that registrants have area assignments
3. Ensure area record rules are properly configured

## See Also

- {doc}`spp_registry` - Registrant models linked to areas
- {doc}`spp_security` - Security groups for area management
- {doc}`spp_programs` - Geographic targeting in programs
