---
openspp:
  doc_status: draft
---

# Area Integration

**Module:** `spp_hxl_area`

## Overview

HXL import with area-level aggregation for humanitarian indicators. Import HXL-tagged field data and aggregate to area-level metrics for coordination.

## Purpose

This module is designed to:

- **Import HXL-tagged data:** Parse HXL-tagged CSV/Excel files using the `libhxl` library, auto-detect columns, and map them to area identifiers and aggregation targets.
- **Match data to geographic areas:** Resolve imported rows to `spp.area` records using configurable strategies (P-code, name, GPS coordinates, or fuzzy name matching).
- **Aggregate to area-level indicators:** Apply configurable aggregation rules (count, sum, average, min, max, percentage) to produce per-area indicator values.
- **Sync indicators for CEL expressions:** Automatically write aggregated values to `spp.data.value` so they can be used in CEL eligibility criteria and other expressions.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `spp_hxl` | Humanitarian Exchange Language (HXL) support for data int... |
| `spp_area` | Establishes direct associations between OpenSPP registran... |
| `spp_cel_domain` | Write simple CEL-like expressions to filter records (Open... |
| `spp_hazard` | Provides hazard classification, incident recording, and i... |
| `spp_security` | Central security definitions for OpenSPP modules |
| `job_worker` | Background job worker |

### External Dependencies

| Package | Purpose |
| --- | --- |
| `libhxl` | Python library for parsing and validating HXL-tagged data files |

## Key Features

### Import Profiles

Reusable configurations that define how HXL data maps to areas and what aggregations to perform.

| Field | Description |
| --- | --- |
| Area Matching Strategy | How to match rows to areas: P-code, Name, GPS, or Fuzzy Name |
| Area Column HXL Tag | HXL tag identifying the area column (e.g., `#adm2+pcode`) |
| Target Admin Level | Administrative level for area matching |
| Latitude/Longitude Tags | HXL tags for GPS-based matching |
| Default Incident | Optionally link all imported data to a hazard incident |

### Aggregation Rules

Define how to transform raw HXL data into area-level indicators.

| Field | Description |
| --- | --- |
| Aggregation Type | Count, Sum, Average, Min, Max, Count Distinct, or Percentage |
| Source Column HXL Tag | Which HXL column to aggregate |
| Filter Expression | Python expression to filter rows before aggregation |
| Target Variable | CEL variable to store the result |
| Disaggregate By | Comma-separated HXL attributes for disaggregation (e.g., `+f,+m`) |
| Output HXL Tag | HXL tag for re-exporting the aggregated indicator |

### Import Batches

Track individual import executions with full audit trail.

| Field | Description |
| --- | --- |
| State | Draft, Columns Mapped, Processing, Completed, or Failed |
| Statistics | Total rows, matched rows, unmatched rows, areas updated, indicators created |
| Column Mappings | Auto-detected mappings with confidence scores, adjustable before processing |
| Error Log | Detailed error information if the import fails |

Import processing runs asynchronously via the job queue.

### Area Indicators

Stores aggregated indicator values per area with support for:

- Period-based tracking (e.g., monthly snapshots)
- Incident/disaster event linking
- JSON-based disaggregation storage
- Automatic sync to `spp.data.value` for CEL expression access

### Import Wizard

A guided wizard for importing HXL data that provides:

- File upload with automatic HXL column detection
- Data preview showing the first rows
- Area matching preview with match/unmatch counts
- List of unmatched area values for troubleshooting

## Integration

- **spp_hxl:** Uses the HXL hashtag and attribute registries for column detection and tag matching.
- **spp_area:** Matches imported data rows to geographic areas using P-code, name, or GPS strategies.
- **spp_hazard:** Links imported data to hazard incidents for disaster response coordination.
- **spp_cel_domain:** Syncs aggregated indicators to `spp.data.value` so area-level metrics are available in CEL expressions for eligibility criteria.
- **job_worker:** Runs import processing asynchronously in the background to handle large files.
