---
openspp:
  doc_status: draft
---

# Indicator

**Module:** `spp_indicator`

## Overview

Publishable indicators based on CEL variables for dashboards, GIS, and APIs

## Purpose

This module is designed to:

- **Publish indicators from CEL variables:** Link CEL variable computations to named, categorized indicators that can be selectively published to GIS, dashboards, APIs, and reports.
- **Protect privacy with small cell suppression:** Apply k-anonymity-based suppression to prevent re-identification of individuals when indicator counts fall below configurable thresholds.
- **Configure context-specific presentation:** Override indicator labels, formats, grouping, icons, and privacy thresholds per publication context (GIS, dashboard, API, report).

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `spp_metric` | Unified metric foundation for indicators and simulations |
| `spp_metric_service` | Computation services for fairness, distribution, breakdow... |
| `spp_cel_domain` | Write simple CEL-like expressions to filter records (Open... |
| `spp_security` | Central security definitions for OpenSPP modules |

## Key Features

### Indicator Definition

Each indicator links a CEL variable to a publishable metric with presentation settings.

| Field | Description |
| --- | --- |
| Name | Technical identifier in snake_case (e.g., `children_under_5`) |
| Label | Human-readable display label (translatable) |
| Variable | CEL variable that provides the computation (must be aggregate, computed, or field type) |
| Format | Aggregation/display format: Count, Sum, Average, Percentage, Ratio, or Currency |
| Category | Metric category for organizing indicators in displays |
| Unit | Unit of measurement (e.g., people, households, %) |

### Publication Channels

Each indicator can be independently toggled for publication to:

| Channel | Description |
| --- | --- |
| GIS | Available in GIS/QGIS spatial queries |
| Dashboard | Available in dashboard widgets |
| API | Available in external API responses |
| Reports | Available in reports and exports |

### Privacy Protection (k-Anonymity)

Indicators enforce small cell suppression to protect individual privacy.

| Field | Description |
| --- | --- |
| Minimum Count (k) | Suppress values when the underlying count is below this threshold (default: 5) |
| Suppression Display | How to show suppressed values: Null/Empty, `*` (Suppressed), or `< [threshold]` |
| Sensitive Data | Flag for sensitive attributes (disability, health) warranting higher thresholds |

### Context-Specific Configuration

Each indicator can have per-context overrides for different publication channels.

| Field | Description |
| --- | --- |
| Context | GIS, Dashboard, API, or Report |
| Label Override | Different label for this context |
| Format Override | Different format for this context |
| Minimum Count Override | Higher or lower privacy threshold per context |
| GIS Threshold Mode | Color threshold calculation: Quartiles, Equal Intervals, Natural Breaks, or Manual |
| Dashboard Widget Type | Widget style: Number, Gauge, or Chart |

## Integration

- **spp_metric:** Inherits the `spp.metric.base` abstract model for shared identity, presentation, and categorization fields.
- **spp_metric_service:** Delegates privacy suppression to the `spp.metric.privacy` service for unified k-anonymity enforcement.
- **spp_cel_domain:** Sources indicator computations from CEL variables, which define the underlying data queries and expressions.
- **spp_indicator_studio:** Provides the Studio UI for managing indicators (views, menus, and actions).
