---
openspp:
  doc_status: draft
---

# GIS API

**Module:** `spp_api_v2_gis`

## Overview

OGC API - Features compliant GIS endpoints for QGIS and GovStack GIS BB.

## Purpose

This module is designed to:

- **Serve OGC API - Features endpoints:** Provide standards-compliant GIS endpoints for interoperability with QGIS and GovStack GIS Building Block.
- **Manage geofences:** Allow API clients to create, list, read, update, and delete areas of interest with GeoJSON geometry.
- **Export spatial data:** Generate GeoPackage or ZIP of GeoJSON files for offline use in desktop GIS applications.
- **Run spatial and proximity queries:** Compute aggregated statistics for registrants within polygons, buffers, or proximity to reference points.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `spp_api_v2` | OpenSPP API V2 - Standards-aligned, consent-respecting AP... |
| `spp_gis` | GIS core plus area geo fields and importer extensions (po... |
| `spp_gis_report` | Geographic visualization and reporting for social protect... |
| `spp_area` | Establishes direct associations between OpenSPP registran... |
| `spp_hazard` | Provides hazard classification, incident recording, and i... |
| `spp_vocabulary` | OpenSPP: Vocabulary |
| `spp_indicator` | Publishable indicators based on CEL variables for dashboa... |
| `spp_analytics` | Query engine for indicators, simulations, and GIS analytics |

## Key Features

### OGC API - Features

Implements the OGC API - Features Core standard (Part 1: Core) with the following endpoints:

| Method | Path | Description |
| --- | --- | --- |
| GET | `/gis/ogc/` | Landing page with API metadata |
| GET | `/gis/ogc/conformance` | Conformance classes declaration |
| GET | `/gis/ogc/collections` | List all feature collections |
| GET | `/gis/ogc/collections/{id}` | Single collection metadata |
| GET | `/gis/ogc/collections/{id}/items` | Feature items as GeoJSON |
| GET | `/gis/ogc/collections/{id}/items/{fid}` | Single feature by ID |
| GET | `/gis/ogc/collections/{id}/qml` | QGIS style file (extension) |

Collections are derived from GIS report data layers and indicator layers. The QML endpoint is a custom extension that generates QGIS styling templates for each collection.

### Geofence Management

Geofences represent saved areas of interest with GeoJSON geometry. The module extends the geofence model with additional types (`service_area`, `targeting_area`) and incident metadata from the hazard module.

| Method | Path | Description |
| --- | --- | --- |
| POST | `/gis/geofences` | Create a geofence from GeoJSON |
| GET | `/gis/geofences` | List geofences with optional type/incident filters |
| GET | `/gis/geofences/{id}` | Read a single geofence |
| DELETE | `/gis/geofences/{id}` | Delete a geofence |

### Data Export

| Method | Path | Description |
| --- | --- | --- |
| GET | `/gis/export/geopackage` | Export layers as GeoPackage or ZIP of GeoJSON for offline QGIS use |

Supports filtering by layer IDs, admin level, and optional inclusion of user geofences.

### Spatial and Proximity Queries

| Method | Path | Description |
| --- | --- | --- |
| POST | `/gis/query/proximity` | Query registrant statistics by proximity to reference points |
| POST | `/gis/query/spatial` | Query registrant statistics within a GeoJSON polygon or buffer |

Proximity queries accept lists of reference point coordinates with a radius and return aggregated statistics for registrants within or beyond the specified distance. Spatial queries support polygon containment and buffer distance operations.

### Statistics Endpoint

Area-level aggregated statistics are exposed for dashboard consumption, computing indicator values broken down by administrative areas.

## Integration

- **spp_gis / spp_gis_report:** GIS report layers and indicator layers are mapped to OGC feature collections. The catalog service reads layer configurations to build collection metadata.
- **spp_analytics:** Spatial and proximity queries delegate statistics computation to the analytics service for consistent aggregation with access control.
- **spp_hazard:** Geofence properties include incident information (code and name) from linked hazard incident records.
- **spp_api_v2:** Provides the FastAPI framework, OAuth middleware, and scope-based authorization (requires `gis:read` and/or `gis:write` scopes).
