---
openspp:
  doc_status: draft
---

# GIS Reports


## Overview

The GIS Reports module (`spp_gis_report`) enables non-technical users to create, configure, and view geographic visualizations of social protection data. It provides template-based report creation, data aggregation by administrative area, and color-coded thematic maps.

## Purpose

This module is designed to:

- **Enable geographic reporting:** Create choropleth maps showing data distribution across areas
- **Support data aggregation:** Roll up data to administrative levels (national, regional, district)
- **Provide normalization options:** Display data per capita, per square kilometer, or as percentages
- **Integrate with external tools:** Export GeoJSON for use in QGIS, Power BI, or other GIS software

## Module Dependencies

| Dependency       | Description                                  |
| ---------------- | -------------------------------------------- |
| `spp_area`       | Administrative area hierarchy                |
| `spp_gis`        | Core GIS functionality and geometry fields   |
| `spp_registry`   | Registry data for aggregation                |
| `spp_vocabulary` | Vocabulary terms for categorization          |
| `spp_cel_domain` | CEL expressions for data filtering           |
| `queue_job`      | Background job processing for large datasets |

### External Python Dependencies

| Package   | Description                           |
| --------- | ------------------------------------- |
| `numpy`   | Numerical computations for statistics |
| `shapely` | Geometric operations                  |

## Key Features

### Report Templates

Pre-built templates for common use cases:

| Category          | Templates                                              |
| ----------------- | ------------------------------------------------------ |
| Coverage Analysis | Beneficiary density, coverage rate, gap analysis       |
| Disaster Response | Affected population, request status, fulfillment rates |
| Demographics      | Age distribution, gender breakdown, disability rates   |

### Report Configuration

| Setting            | Description                                                |
| ------------------ | ---------------------------------------------------------- |
| Name               | Report identifier                                          |
| Category           | Grouping for report organization                           |
| Target Model       | Source data model (`res.partner`, `spp.entitlement`, etc.) |
| Filter Expression  | CEL expression to filter source records                    |
| Aggregation Field  | Field to aggregate (count, sum, average)                   |
| Aggregation Method | How to combine values (count, sum, avg, min, max)          |
| Area Level         | Administrative level for grouping                          |

### Normalization Methods

| Method     | Description          | Use Case                     |
| ---------- | -------------------- | ---------------------------- |
| Raw count  | Absolute numbers     | Total beneficiaries per area |
| Per km²    | Density by area size | Population density mapping   |
| Per capita | Rate per population  | Coverage percentage          |
| Percentage | Share of total       | Distribution analysis        |

### Hierarchical Rollup

Data automatically rolls up through the area hierarchy:

```
Village (Level 4) → District (Level 3) → Region (Level 2) → National (Level 1)
```

Each level shows aggregated data from its children.

### Color Schemes

Color-blind safe palettes by default:

| Scheme      | Description                         |
| ----------- | ----------------------------------- |
| Sequential  | Light to dark for increasing values |
| Diverging   | Two-color scale with neutral middle |
| Categorical | Distinct colors for categories      |

### Data Refresh

| Trigger   | Description                             |
| --------- | --------------------------------------- |
| Manual    | Click refresh button on report          |
| Scheduled | Cron job updates at configured interval |
| On-demand | Triggered by data changes               |

## Integration

### GeoJSON API

Export report data for external tools:

```
GET /api/gis-report/{report_id}/geojson
```

Response includes:

- Area geometries as GeoJSON features
- Aggregated values as feature properties
- Metadata (report name, timestamp, color scale)

### With GIS Views

Reports display as thematic map layers:

```xml
<field name="report_id" widget="gis_report_layer"/>
```

### With Programs

Analyze program performance geographically:

- Coverage rates by district
- Entitlement distribution maps
- Beneficiary density analysis

## Are you stuck?

### Report shows no data

**Symptom:** The map displays but all areas show zero or no color.

**Cause:** The filter expression may exclude all records, or area assignments are missing.

**Solution:**

1. Test the filter expression in the CEL editor to verify it returns records
2. Check that source records have `area_id` assigned
3. Verify the area level setting matches your area hierarchy
4. Check that aggregation field contains valid values

### Slow report loading

**Symptom:** Reports take a long time to generate or time out.

**Cause:** Large datasets or complex aggregations can be slow.

**Solution:**

1. Use scheduled refresh instead of real-time calculation
2. Add indexes to frequently filtered fields
3. Simplify the filter expression if possible
4. Consider using queue_job for background processing

### Colors don't reflect data range

**Symptom:** All areas show the same color despite different values.

**Cause:** The color scale may not match the data distribution.

**Solution:**

1. Check the color scheme configuration
2. Verify min/max values are set appropriately
3. For skewed data, consider using quantile breaks instead of linear
4. Review the normalization method (raw values vs. per capita may need different scales)
