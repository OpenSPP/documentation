---
openspp:
  doc_status: draft
---

# Scoring

**Module:** `spp_scoring`

## Overview

Configurable scoring and assessment framework for beneficiary targeting

## Purpose

This module is designed to:

- **Define scoring models:** Create configurable scoring methodologies with indicators, weights, and thresholds for assessing registrants (e.g., Proxy Means Test, vulnerability index).
- **Calculate scores:** Evaluate registrants against scoring models using a central engine that supports multiple calculation methods.
- **Classify registrants:** Automatically assign classifications (e.g., "Extremely Poor", "Vulnerable") based on score thresholds.
- **Process scores in batch:** Score large populations synchronously or asynchronously using job_worker for background processing.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `base` | Odoo core framework |
| `mail` | Communication and activity tracking |
| `spp_security` | Central security definitions for OpenSPP modules |
| `spp_registry` | Consolidated registry management for individuals, groups,... |
| `spp_cel_domain` | Write simple CEL-like expressions to filter records (Open... |
| `spp_cel_widget` | Reusable CEL expression editor with syntax highlighting a... |
| `job_worker` | Background job worker |

## Key Features

### Scoring Models

A scoring model defines a complete scoring methodology. Each model has:

| Field | Description |
| --- | --- |
| Name / Code | Human-readable name and unique identifier |
| Category | Purpose classification: Poverty Assessment, Vulnerability Assessment, Eligibility Scoring, Triage/Prioritization, or Custom |
| Calculation Method | How the total score is computed: Weighted Sum, CEL Formula, Lookup Table, External Service, or Custom Plugin |
| Validity Period | Effective and end dates controlling when the model is active |
| Strict Mode | When enabled, scoring fails if required indicators are missing |

Models must pass validation (indicators exist, thresholds exist, weights sum correctly, CEL expressions compile) before they can be activated.

### Indicators

Each indicator defines a single scoring component:

| Field | Description |
| --- | --- |
| Field Path | Dot-notation path to the registrant field (e.g., `household.roof_material`) |
| Weight | Multiplier applied to the indicator score |
| Calculation Type | Direct Value, Value Mapping, Range Mapping, CEL Formula, or Derived/Computed |
| Default Handling | Default value and score when data is missing |
| Min/Max Score | Constraints on the indicator score |

### Value Mappings

For mapped and range indicators, value mappings translate field values into scores:

- **Exact mapping:** Maps specific values to scores (e.g., "concrete" = 5, "thatch" = 1)
- **Range mapping:** Maps numeric ranges to scores (e.g., 0-2 hectares = 1, 2-5 hectares = 3)

### Thresholds and Classifications

Thresholds map score ranges to classification labels:

| Field | Description |
| --- | --- |
| Min/Max Score | Inclusive score range for this classification |
| Classification Code | Machine-readable code (e.g., `EXTREME_POOR`) |
| Classification Label | Human-readable label (e.g., "Extremely Poor") |
| Display Color | Visual color coding (red, orange, yellow, green, blue, purple, gray) |

### Scoring Engine

The central scoring engine (`spp.scoring.engine`) calculates scores:

- Processes each indicator to extract field values and compute weighted scores
- Supports CEL formula-based total score calculation
- Captures a full breakdown with per-indicator contributions
- Stores input snapshots for audit and reproducibility
- Provides `get_or_calculate_score` to reuse recent scores within a configurable age

### Batch Processing

For scoring large populations:

- Synchronous processing for datasets under 1,000 registrants
- Asynchronous chunked processing via `job_worker` for larger datasets (chunks of 500)
- Batch job tracking with progress counters (successful/failed counts)
- Support for `fail_fast` mode to stop on first error

### Scoring Results

Each scoring result stores:

- The calculated total score and classification
- A JSON breakdown showing each indicator's contribution
- An inputs snapshot capturing field values at calculation time
- Metadata: calculation date, mode (manual/batch/automatic), model version
- Per-indicator detail records for relational querying

Performance indexes on `(registrant_id, model_id, calculation_date)` support efficient lookups at scale.

### Data Integration

When activated, scoring models automatically:

- Create CEL variables (e.g., `pmt_2024_urban_score`) for use in targeting expressions
- Cache scoring results in the unified data store (`spp.data.value`) for CEL access
- Register as indicator providers so scores can be queried via `metric("scoring.<model_code>")`

## Integration

- **spp_cel_domain / spp_cel_widget:** CEL expressions can be used for indicator formulas and total score calculation. Score variables are accessible in CEL targeting expressions.
- **job_worker:** Provides asynchronous batch scoring for large populations, with chunked processing and progress tracking.
- **spp_registry:** Scores are calculated against registrant records (`res.partner`), reading field values via configurable field paths.
- **spp_indicators (optional):** Scoring models register as indicator providers, making scores available via `metric()` in CEL expressions.

```{toctree}
:maxdepth: 1
:hidden:

spp_scoring_programs
```
