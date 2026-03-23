---
openspp:
  doc_status: draft
---

# HDX COD Integration

**Module:** `spp_area_hdx`

## Overview

HDX Common Operational Datasets (COD) integration for downloading admin boundaries with polygons. Supports humanitarian coordination with P-code standardization and GPS-based area lookup.

## Purpose

This module is designed to:

- **Import administrative boundaries from HDX:** Download Common Operational Datasets (COD) from the Humanitarian Data Exchange, including GeoJSON polygons for admin boundary areas.
- **Standardize P-codes:** Store and look up areas using official P-codes from COD datasets, enabling interoperability with humanitarian coordination systems.
- **Locate areas by GPS coordinates:** Find which administrative area contains a given GPS point using PostGIS spatial queries.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `spp_area` | Establishes direct associations between OpenSPP registran... |
| `spp_gis` | GIS core plus area geo fields and importer extensions (po... |

### External Dependencies

| Package | Purpose |
| --- | --- |
| `requests` | HTTP client for downloading datasets from the HDX API |
| `geojson` | Parsing and validating GeoJSON geometry data |

## Key Features

### COD Source Management

The `spp.hdx.cod.source` model maintains a registry of COD datasets per country. Each source tracks:

| Field | Description |
| --- | --- |
| Country | Country linked to the COD dataset |
| HDX Dataset ID | Identifier on HDX (e.g., `cod-ab-lka`) |
| Resources | GeoJSON resources available at each admin level |
| Last Sync / Import | Timestamps of most recent operations |

The **Sync from HDX** action fetches dataset metadata from the HDX API and creates resource records for each available admin level.

### COD Resource Tracking

Each `spp.hdx.cod.resource` represents a single admin-level GeoJSON file within a COD dataset. Resources store field mappings (P-code field, name field, parent P-code field) and track download history and feature counts.

### Import Wizard

A multi-step wizard (`spp.hdx.cod.import.wizard`) supports two import modes:

| Mode | Description |
| --- | --- |
| Download from HDX | Fetch GeoJSON directly from the HDX API for selected admin levels |
| Upload GeoJSON File | Import from a manually uploaded GeoJSON file |

The wizard provides a preview step showing counts of areas to update, P-codes not found, and new areas to create. Import options include:

- **Update existing areas** matched by P-code with new polygons
- **Create missing areas** for unmatched P-codes
- **Update names** from COD data

Field mappings for P-code, name, local name, and parent P-code are auto-detected from GeoJSON properties or can be set manually. Features are processed in batches of 100 for efficiency.

### GPS-Based Area Lookup

The module extends `spp.area` with PostGIS spatial query methods:

| Method | Description |
| --- | --- |
| `find_by_coordinates(lat, lon, level)` | Find the most specific area containing a GPS point, optionally filtered by admin level |
| `find_all_containing(lat, lon)` | Return all areas at all levels containing the point, ordered from country level to most specific |
| `find_by_pcode(pcode)` | Look up an area by HDX P-code, falling back to the code field |

### HDX-Specific Area Fields

| Field | Description |
| --- | --- |
| `hdx_pcode` | Official P-code from COD dataset (unique, indexed) |
| `hdx_last_update` | Timestamp of last update from HDX |

## Integration

- **spp_area:** Extends the `spp.area` model with HDX P-code fields and GPS lookup methods. Imported boundaries update existing area records matched by P-code or code.
- **spp_gis:** Uses the `geo_polygon` PostGIS geometry column for spatial containment queries (`ST_Contains`). Imported GeoJSON geometry is stored in this column.
