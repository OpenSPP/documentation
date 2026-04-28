---
openspp:
  doc_status: draft
  products: [core]
---

# GIS configuration

This guide is for **implementers** configuring map-based visualization for geographic analysis, coverage mapping, and spatial reporting.

## Prerequisites

```{important}
The `spp_gis` module must be installed. See {doc}`/get_started/modules/index` for module installation instructions.
```

## What you'll find here

- **{doc}`overview`** - GIS concepts, raster layers (base maps), and color schemes
- **{doc}`data_layers`** - Data layer configuration, choropleth maps, and classification methods
- **{doc}`report_templates`** - GIS report templates and indicator layers

```{toctree}
:hidden:
:maxdepth: 1

overview
data_layers
report_templates
```

## Quick start

1. Navigate to **Settings > GIS Configuration**
2. Add a **Raster Layer** (base map) - OpenStreetMap is pre-configured
3. Create a **Data Layer** to visualize model data on the map
4. Choose **Basic** mode (single color) or **Choropleth** mode (color by value)
5. Configure **Color Schemes** for consistent visualization
