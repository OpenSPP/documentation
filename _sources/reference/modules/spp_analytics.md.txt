---
openspp:
  doc_status: draft
---

# Analytics

**Module:** `spp_analytics`

## Overview

Query engine for indicators, simulations, and GIS analytics

## Purpose

This module is designed to:

- **Compute aggregation queries:** Provide a unified entry point for all statistics computation, including counts, indicator values, and demographic breakdowns.
- **Define targeting scopes:** Resolve sets of registrant IDs from CEL expressions, administrative areas, spatial polygons/buffers, area tags, or explicit ID lists.
- **Enforce access control:** Restrict what data users can query through configurable access rules with k-anonymity thresholds, scope type restrictions, and dimension limits.
- **Cache query results:** Store and retrieve aggregation results with TTL-based expiration to improve performance for frequently requested queries.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `base` | Odoo core framework |
| `spp_cel_domain` | Write simple CEL-like expressions to filter records (Open... |
| `spp_area` | Establishes direct associations between OpenSPP registran... |
| `spp_registry` | Consolidated registry management for individuals, groups,... |
| `spp_security` | Central security definitions for OpenSPP modules |
| `spp_metric_service` | Computation services for fairness, distribution, breakdow... |

## Key Features

### Aggregation Scopes

Scopes define WHAT to aggregate by resolving to a set of registrant IDs. All scope types ultimately produce a list of `res.partner` IDs.

| Scope Type | Description |
| --- | --- |
| CEL Expression | Filter registrants using CEL expressions against individual or group profiles |
| Administrative Area | Select registrants in an area, optionally including child areas |
| Area Tags | Select registrants in all areas matching specific tags |
| Within Polygon | Spatial query using GeoJSON polygon (requires PostGIS bridge module) |
| Within Distance | Spatial buffer query by center point and radius in km |
| Explicit IDs | Directly specified list of registrant IDs |

Each scope can have caching enabled with a custom TTL and displays an approximate registrant count.

### Analytics Service

The `spp.analytics.service` is the main entry point for all aggregation queries. It accepts a scope (record, ID, or inline dict), a list of statistics to compute, and optional group-by dimensions for demographic breakdowns.

The service resolves the user's access level from `spp.analytics.access.rule` records rather than accepting it as a parameter, preventing callers from bypassing restrictions.

Convenience methods are provided for common patterns:

- `compute_for_area()` -- aggregate by administrative area
- `compute_for_expression()` -- aggregate by CEL expression
- `compute_fairness()` -- analyze equity across dimensions
- `compute_distribution()` -- compute distribution statistics for amounts

### Indicator Registry

The `spp.analytics.indicator.registry` maps statistic names to computation strategies using a lookup chain:

1. Built-in statistics (count, gini coefficient)
2. `spp.indicator` records (via CEL variables)
3. `spp.cel.variable` records (direct CEL evaluation)

### Access Control

Access rules determine what level of data access a user or group has:

| Setting | Description |
| --- | --- |
| Access Level | Aggregates only (counts/statistics) or individual records |
| K-anonymity Threshold | Minimum count for a cell before suppression (1-100) |
| Allowed Scope Types | All, area-based only, or predefined scopes only |
| Inline Scopes | Whether ad-hoc scope definitions are permitted |
| Allowed Dimensions | Restrict which demographic dimensions can be used for group-by |
| Max Group-by Dimensions | Limit on number of simultaneous breakdown dimensions (max 10) |
| Area Restrictions | Limit queries to specific areas and optionally their children |

User-specific rules take precedence over group-based rules, evaluated in sequence order.

### Result Caching

Aggregation results are cached with scope-type-specific TTLs:

| Scope Type | TTL |
| --- | --- |
| Area / Area Tags | 1 hour |
| CEL Expression | 15 minutes |
| Explicit IDs | 30 minutes |
| Spatial Polygon / Buffer | No cache |

A scheduled cron job cleans up expired cache entries. Scopes can also be manually refreshed.

## Integration

- **spp_cel_domain:** CEL expressions are compiled and evaluated via the CEL executor service to resolve registrants matching targeting criteria.
- **spp_area:** Area-based scopes resolve registrants by searching `res.partner` records linked to areas (including child areas and indirect membership through groups).
- **spp_metric_service:** Privacy enforcement (k-anonymity suppression), fairness analysis, distribution statistics, and demographic breakdowns are delegated to the metric service layer.
- **spp_api_v2_simulation / spp_api_v2_gis:** These API modules consume the analytics service as their statistics computation backend.
