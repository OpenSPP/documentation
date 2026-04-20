---
openspp:
  doc_status: draft
  products: [core]
---

# GIS configuration overview

This guide is for **implementers** setting up geographic visualization in OpenSPP. You should understand basic mapping concepts but don't need GIS expertise.

## Mental model

GIS in OpenSPP has three layers:

| Layer | What it does | Example |
|-------|--------------|---------|
| **Raster layer** | Background map (the base map you see) | OpenStreetMap, satellite imagery, WMS service |
| **Data layer** | Overlays data from OpenSPP models on the map | Registrant locations, area boundaries |
| **Color scheme** | Consistent color palettes for visualization | Green-to-Red for poverty levels |

Think of it like building a map with transparencies: the **raster layer** is the printed base map, **data layers** are transparent overlays with your data points and boundaries, and **color schemes** ensure everything uses consistent, readable colors.

## Key concepts

### Raster layers (base maps)

Raster layers provide the background map. OpenSPP supports three types:

| Type | Description | Best for |
|------|-------------|----------|
| **OpenStreetMap** | Free, community-maintained maps | General purpose, always available |
| **WMS (Web Map Service)** | Maps from external map providers | Specialized maps (terrain, satellite) |
| **Image** | Static image overlay | Custom reference maps |

#### OpenStreetMap styles

| Style | Description |
|-------|-------------|
| Streets | Standard road map |
| Satellite | Aerial/satellite imagery |
| Topographic | Elevation and terrain |
| Dark | Dark theme for data visualization |
| Voyage | Clean, minimal cartographic style |

#### WMS configuration

| Field | What it means |
|-------|---------------|
| **Service URL** | Web address of the map service |
| **WMS Layer Name** | Which map layer to display |
| **Opacity** | Transparency level (0% = invisible, 100% = solid) |

### Color schemes

Centralized palettes for consistent visualization across all maps:

| Field | What it means |
|-------|---------------|
| **Name** | Scheme label (e.g., "Poverty Scale") |
| **Code** | Unique identifier |
| **Scheme Type** | Sequential, Diverging, or Qualitative |
| **Colors** | List of colors used in the palette (selected via color picker) |
| **Default Steps** | Number of discrete color classes |
| **Color-blind Safe** | Accessibility flag |
| **Is Default** | System default scheme |

#### Scheme types

| Type | When to use | Example |
|------|-------------|---------|
| **Sequential** | Values from low to high | Poverty rate (light → dark) |
| **Diverging** | Values with a meaningful midpoint | Change from baseline (red ← neutral → green) |
| **Qualitative** | Categories without ordering | Program types (distinct colors) |

## Navigation

| Menu | Purpose |
|------|---------|
| **Settings > GIS Configuration > Color Schemes** | Manage color palettes |
| **Settings > GIS Configuration > Raster Layers** | Configure base maps |
| **Settings > GIS Configuration > Data Layers** | Create data overlays |

```{figure} /_images/en-us/config_guide/gis/01-gis-color-schemes.png
:alt: GIS color schemes list showing available palettes
GIS color schemes list showing available palettes.
```

## Common use cases

### Use case 1: Basic area map

**Goal:** Display administrative areas on a map.

**Setup:**
1. Ensure areas have geographic coordinates or polygons
2. The default OpenStreetMap raster layer provides the base map
3. Area boundaries are displayed automatically on GIS views

### Use case 2: Coverage heat map

**Goal:** Show beneficiary density across areas using color gradients.

**Setup:**
1. Create a choropleth data layer (see {doc}`data_layers`)
2. Map it to the area model with a beneficiary count field
3. Select a sequential color scheme (e.g., light-to-dark blue)
4. Areas with more beneficiaries appear darker

## Are You Stuck?

**Maps not loading?**

The GIS feature requires special database extensions. Ask your system administrator to verify that the **GIS module** is installed and that geographic extensions are enabled on the database.

**Base map tiles not showing?**

Verify internet connectivity from the server. OpenStreetMap tiles require network access. For offline environments, use a local WMS tile server.

**Color scheme looks wrong?**

Check that the scheme type matches your data. Sequential for ordered values, diverging for values around a midpoint, qualitative for categories.

**Can I use Google Maps as a base layer?**

Not directly. Google Maps requires a paid API key and has license restrictions. Use OpenStreetMap or a WMS service as alternatives.

## Next steps

- {doc}`data_layers` - Configure data overlays and choropleth maps
- {doc}`report_templates` - Set up GIS reports
- {doc}`/config_guide/area_management/overview` - Configure areas for GIS visualization
