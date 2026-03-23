---
openspp:
  doc_status: draft
---

# Land Record

**Module:** `spp_land_record`

## Overview

The OpenSPP Land Record module digitizes and centralizes land parcel information, linking it to associated farms, ownership details, and lease agreements. It captures and displays geographical boundaries and coordinates on interactive maps, supporting land use classification and program planning.

## Purpose

This module is designed to:

- **Record land parcels:** Create and manage land parcel records with acreage, land use classification, and unique identifiers linked to farms.
- **Track ownership and leases:** Associate land parcels with owners and lessees, including lease start and end date tracking with validation.
- **Map parcel boundaries:** Store point coordinates and polygon boundaries for each parcel using GIS fields.
- **Export as GeoJSON:** Generate GeoJSON representations of land records with coordinate projection support for mapping applications.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `base` | Odoo core framework |
| `spp_base_common` | The OpenSPP base module that provides the main menu, gene... |
| `spp_gis` | GIS core plus area geo fields and importer extensions (po... |
| `spp_registry` | Consolidated registry management for individuals, groups,... |
| `spp_security` | Central security definitions for OpenSPP modules |
| `spp_farmer_registry_vocabularies` | FAO-aligned vocabularies for farmer registry (crops, live... |

## Key Features

### Land Parcel Records

Each land record captures parcel information linked to a farm.

| Field | Description |
| --- | --- |
| Parcel Name/ID | Unique name or identifier for the land parcel |
| Farm | Link to the farm partner that this parcel belongs to |
| Acreage | Area measurement of the parcel |
| Land Use | Vocabulary-based classification from `urn:openspp:vocab:land-use` |
| Coordinates | GIS point location of the parcel |
| Land Polygons | GIS polygon boundary of the parcel |

### Ownership and Lease Tracking

| Field | Description |
| --- | --- |
| Owner | Partner record representing the parcel owner |
| Lessee | Partner record representing the current lessee |
| Lease Start | Start date of the lease agreement |
| Lease End | End date of the lease agreement (validated to be after start date) |

The module validates that lease end dates cannot precede lease start dates, with both server-side constraints and client-side warnings on date changes.

### GeoJSON Export

The `get_geojson()` method generates a GeoJSON FeatureCollection from land records with:

- Configurable geometry type filtering (point, polygon, or all)
- Coordinate reprojection between spatial reference systems (default: EPSG:3857 to EPSG:4326)
- Feature properties including parcel name, land use, and acreage

## Integration

- **spp_gis:** Uses `GeoPointField` and `GeoPolygonField` to store and display parcel locations and boundaries on interactive maps.
- **spp_registry:** Links land records to farm and owner/lessee partner records.
- **spp_farmer_registry_vocabularies:** Uses the land use vocabulary for standardized parcel classification.
- **mail.thread:** Inherits message tracking for audit trail on land record changes.
