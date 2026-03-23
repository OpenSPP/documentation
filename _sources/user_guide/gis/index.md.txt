---
openspp:
  doc_status: draft
---

# Geographic Information System (GIS)

This section is for **users** — field officers, program managers, and decision-makers who need to view registry data geographically.

The GIS features let you see where registrants live, which areas are covered by a program, and how indicators are distributed on an interactive map — instead of looking at rows in a table.

## What you'll find here

- **{doc}`maps_and_reports`** — Configure map layers, view area boundaries, add GPS coordinates to registrants, and generate geographic coverage reports

## Before you start

The following must be in place before using GIS features:

- Geographic areas (barangay, municipality, province) must be configured in the system
- The `spp_gis` module must be installed
- The database server must have the PostGIS extension enabled (a server-level requirement — coordinate with your system administrator)

```{toctree}
:maxdepth: 2
:hidden:

maps_and_reports
```
