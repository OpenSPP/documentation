---
openspp:
  doc_status: draft
---

# Indicators

**Module:** `spp_gis_indicators`

## Overview

Choropleth visualization for area-level indicators

## Purpose

This module is designed to:

- **Visualize area-level indicators as choropleth maps:** Map CEL variable values to color-coded geographic areas for spatial analysis of social protection metrics.
- **Define color scales:** Create and manage reusable color schemes (sequential, diverging, categorical) based on ColorBrewer palettes for data visualization.
- **Configure indicator layers:** Link CEL variables to color scales with classification methods to control how data values are mapped to colors on the map.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `spp_gis` | GIS core plus area geo fields and importer extensions (po... |
| `spp_hxl_area` | HXL import with area-level aggregation for humanitarian i... |
| `spp_registry` | Consolidated registry management for individuals, groups,... |
| `spp_security` | Central security definitions for OpenSPP modules |

## Key Features

### Color Scales

Color scales define the color palettes used for choropleth visualization.

| Field | Description |
| --- | --- |
| Scale Name | Name of the color scheme (e.g., "Blues", "RdYlGn") |
| Scale Type | Sequential (low to high), Diverging (negative to positive), or Categorical (distinct values) |
| Colors (JSON) | JSON array of hex color codes (minimum 2 colors required) |

The module validates hex color format (#RGB or #RRGGBB) and provides a `get_color_for_value` method that maps data values to colors based on the scale type. Sequential scales use linear mapping, while diverging scales map relative to a center point.

### Indicator Layer Configuration

Indicator layers configure how area-level indicators appear as choropleth maps.

| Field | Description |
| --- | --- |
| Indicator Variable | CEL variable containing area-level indicator values |
| Period Key | Period identifier for filtering (e.g., "2024-12", "current") |
| Incident/Disaster | Optional filter by specific hazard incident |
| Color Scale | Color scheme to use |
| Classification Method | Quantile (equal count per class), Equal Interval (equal range per class), or Manual Breaks |
| Number of Classes | Number of color classes (2-10) |
| Manual Break Points | Comma-separated break values for manual classification |

The module computes break values from actual indicator data and generates an HTML legend showing the color-to-value mapping for display on the map.

### Data Layer Extension

The module extends `spp.gis.data.layer` to support indicator-based choropleth visualization. Choropleth layers can be configured with either a direct value field or an indicator layer configuration, and the `get_feature_colors` method returns a mapping of area IDs to hex colors for rendering.

## Integration

- **spp_gis:** Extends the GIS data layer model to add indicator-based choropleth configuration alongside the base field-based approach.
- **spp_hxl_area:** Reads indicator values from `spp.hxl.area.indicator` records to compute classification breaks and assign colors per area.
- **spp_hazard:** Optionally filters indicators by hazard incident via the `incident_id` field on indicator layer configuration.
