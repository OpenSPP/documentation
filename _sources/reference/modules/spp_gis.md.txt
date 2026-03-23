---
openspp:
  doc_status: draft
---

# GIS

**Module:** `spp_gis`

## Overview

The GIS module (`spp_gis`) provides Geographic Information System capabilities for OpenSPP, enabling spatial data storage, visualization, and analysis. It extends the administrative area model with geographic fields and provides map-based views for visualizing beneficiary locations and program coverage.

## Purpose

This module is designed to:

- **Store geographic data:** Add point and polygon geometry fields to records
- **Visualize locations:** Display registrants, service points, and areas on interactive maps
- **Enable spatial queries:** Filter records by geographic criteria (within area, near point, etc.)
- **Support multiple layers:** Configure raster and vector data layers for map displays

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `base` | Odoo core framework |
| `web` | Web interface components |
| `contacts` | Base contact model extension |
| `spp_security` | Central security definitions for OpenSPP modules |
| `spp_area` | Establishes direct associations between OpenSPP registran... |
| `spp_vocabulary` | OpenSPP: Vocabulary |
| `spp_registry` | Consolidated registry management for individuals, groups,... |

### External Dependencies

| Package | Purpose |
| --- | --- |
| `shapely` | |
| `pyproj` | |
| `geojson` | |

## Key Features

### Geometry Fields

The module adds geographic field types to Odoo:

| Field Type        | Description                 | Example Use                |
| ----------------- | --------------------------- | -------------------------- |
| `GeoPoint`        | Single coordinate (lat/lng) | Beneficiary home location  |
| `GeoPolygon`      | Closed area boundary        | Administrative area border |
| `GeoMultiPolygon` | Multiple polygon areas      | Discontinuous regions      |
| `GeoLineString`   | Linear path                 | Road or boundary line      |

### Area Geographic Extensions

Administrative areas (`spp.area`) gain geographic capabilities:

| Feature        | Description                          |
| -------------- | ------------------------------------ |
| `geo_polygon`  | Area boundary as polygon geometry    |
| `geo_centroid` | Calculated center point              |
| `geo_area_km2` | Calculated area in square kilometers |

### Data Layers

Configure map layers for visualization:

| Layer Type    | Description                                      |
| ------------- | ------------------------------------------------ |
| Vector layers | Display points, lines, polygons from database    |
| Raster layers | Background imagery (satellite, terrain, streets) |
| Color schemes | Configurable palettes for thematic mapping       |

### GIS Views

Custom view types for map-based display:

```xml
<record id="view_partner_gis" model="ir.ui.view">
    <field name="name">res.partner.gis.view</field>
    <field name="model">res.partner</field>
    <field name="type">gis</field>
    <field name="arch" type="xml">
        <gis_view>
            <field name="geo_point"/>
            <field name="name"/>
        </gis_view>
    </field>
</record>
```

### Spatial Queries

Filter records by geographic criteria:

| Query Type  | Description                        | Example                     |
| ----------- | ---------------------------------- | --------------------------- |
| Within area | Records inside a polygon           | Beneficiaries in district X |
| Near point  | Records within distance of a point | Service points within 10km  |
| Intersects  | Records overlapping an area        | Areas touching a boundary   |

## Integration

### With Registry

Registrants can have geographic locations:

```python
partner = env["res.partner"].browse(partner_id)
partner.geo_point = "POINT(125.6 7.1)"  # Longitude, Latitude
```

### With Area Hierarchy

Areas display their boundaries on maps:

```python
area = env["spp.area"].browse(area_id)
# Get GeoJSON for the area
geojson = area.get_geojson()
```

### With Programs

Visualize program coverage geographically:

- Map beneficiary locations by program
- Show coverage gaps by area
- Analyze geographic distribution of entitlements

```{toctree}
:maxdepth: 1
:hidden:

spp_gis_indicators
spp_gis_report
spp_gis_report_programs
spp_registrant_gis
```
