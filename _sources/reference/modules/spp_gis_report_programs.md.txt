---
openspp:
  doc_status: draft
---

# Reports - Programs

**Module:** `spp_gis_report_programs`

## Overview

Add program context filtering to GIS reports

## Purpose

This module is designed to:

- **Filter GIS reports by program:** Add program context to GIS reports so that geographic visualizations can be scoped to registrants enrolled in a specific program.
- **Extend the report wizard:** Allow users to select a program when generating a GIS report, enforcing program selection when a template requires it.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `spp_gis_report` | Geographic visualization and reporting for social protect... |
| `spp_programs` | Manage cash and in-kind entitlements, integrate with inve... |

## Key Features

### Program Context Filter on GIS Reports

The module adds a `Program Context` field to the GIS report model. When a program is selected and the report's source model is `res.partner`, the report domain is extended to include only registrants enrolled in that program (via `program_membership_ids.program_id`).

### Report Wizard Extension

The GIS report wizard gains a `Program` field. When generating a report:

- The selected program is validated if the template requires it.
- The program ID is included in the report creation values.
- The program ID is appended to the report code suffix to ensure unique report codes per program.

## Integration

- **spp_gis_report:** Extends the report model (`spp.gis.report`) and wizard (`spp.gis.report.wizard`) with program context filtering.
- **spp_programs:** Uses the `spp.program` model and filters registrants by their `program_membership_ids` relationship.
- **Auto-install:** This module auto-installs when both `spp_gis_report` and `spp_programs` are present.
