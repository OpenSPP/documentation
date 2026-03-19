---
openspp:
  doc_status: draft
---

# Metric Service

**Module:** `spp_metric_service`

## Overview

Computation services for fairness, distribution, breakdown, and privacy

## Purpose

This module is designed to:

- **Analyze targeting fairness:** Compute equity scores and disparity ratios across demographic groups to assess whether program targeting reaches different populations proportionally.
- **Compute distribution statistics:** Calculate Gini coefficients, Lorenz curves, percentiles, and other inequality metrics from numerical value sets.
- **Break down registrants by dimensions:** Categorize registrants by configurable demographic dimensions (gender, age group, disability, area, etc.) and compute per-group counts.
- **Enforce privacy protections:** Apply k-anonymity with complementary suppression to prevent re-identification of individuals in small groups.
- **Cache dimension evaluations:** Cache demographic dimension evaluation results for improved performance on repeated breakdown computations.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `base` | Odoo core framework |
| `spp_cel_domain` | Write simple CEL-like expressions to filter records (Open... |
| `spp_area` | Establishes direct associations between OpenSPP registran... |
| `spp_registry` | Consolidated registry management for individuals, groups,... |

## Key Features

### Fairness Analysis Service

Analyzes whether program targeting reaches demographic groups proportionally.

| Output | Description |
| --- | --- |
| Equity Score | 0-100 score that decreases when disparities are detected |
| Disparity Ratio | Per-group ratio of group coverage to overall coverage |
| Status | `proportional`, `low_coverage`, or `under_represented` per group |
| Overall Coverage | Ratio of beneficiaries to total population |

The service supports field-based dimensions (Many2one, Selection, Boolean fields) using efficient `read_group` queries, and CEL expression-based dimensions for custom categorization logic.

### Distribution Service

Computes inequality and distribution statistics from a list of numerical values.

| Metric | Description |
| --- | --- |
| Gini Coefficient | Inequality measure from 0.0 (perfect equality) to 1.0 (perfect inequality) |
| Lorenz Deciles | Cumulative income share at each population decile |
| Percentiles | P10, P25, P50 (median), P75, P90 values |
| Basic Statistics | Count, total, minimum, maximum, mean, median, standard deviation |

### Breakdown Service

Categorizes registrants by one or more demographic dimensions and counts per combination.

Results are keyed by pipe-separated dimension values (e.g., `male|urban`) with per-cell counts and human-readable labels. Uses the dimension cache service for performance.

### Privacy Service

Enforces k-anonymity with complementary suppression on aggregated results.

| Feature | Description |
| --- | --- |
| Primary Suppression | Suppress cells with counts below the k threshold (default: 5) |
| Complementary Suppression | Also suppress sibling cells to prevent derivation from marginal totals |
| Dimension-Aware | Multi-dimensional suppression checks each dimension slice independently |
| Display Modes | Suppressed values shown as null, `*`, or `< [threshold]` |
| Access Levels | Strip individual record IDs from aggregate-level results |

### Demographic Dimensions

Configurable dimensions for group-by analysis.

| Field | Description |
| --- | --- |
| Dimension Type | Field-based (direct field lookup) or CEL Expression (custom logic) |
| Field Path | Dot-notation path for field-based dimensions (e.g., `gender_id.code`) |
| CEL Expression | Expression returning a category value per registrant |
| Label Mappings | JSON-based mapping from dimension values to display labels |
| Default Value | Fallback value when evaluation returns nothing |

### Dimension Cache

Caches dimension evaluation results using Odoo's `ormcache` for performance improvement on repeated computations. Cache keys include the dimension ID, write date, and a hash of registrant IDs. Cache invalidates automatically when dimension configuration changes.

## Integration

- **spp_cel_domain:** Uses the CEL service to evaluate expression-based dimensions for custom categorization of registrants.
- **spp_registry:** Queries `res.partner` registrant records for population baselines and demographic field lookups.
- **spp_area:** Supports area-based demographic dimensions for geographic breakdowns.
- **spp_indicator:** Provides the privacy suppression service (`spp.metric.privacy`) used by indicators for k-anonymity enforcement.
