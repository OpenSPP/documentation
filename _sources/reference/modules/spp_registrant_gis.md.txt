---
openspp:
  doc_status: draft
---

# Registrant GIS

**Module:** `spp_registrant_gis`

## Overview

Adds GPS coordinates to registrants for spatial queries

## Purpose

This module is designed to:

- **Add GPS coordinates to registrants:** Extends each registrant record with a GeoPoint field for storing latitude/longitude coordinates.
- **Enable spatial queries:** Allows proximity-based targeting and geographic analysis of registrant locations.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `spp_gis` | GIS core plus area geo fields and importer extensions (po... |
| `spp_registry` | Consolidated registry management for individuals, groups,... |

## Key Features

### GPS Coordinates Field

Adds a `coordinates` GeoPoint field to `res.partner` (registrant records). This field stores geographic coordinates (latitude/longitude) that can be used for:

- Mapping registrant locations
- Proximity-based targeting and filtering
- Geographic analysis and reporting

## Integration

- **spp_gis:** Uses the GeoPoint field type provided by the GIS module for storing spatial data.
- **spp_registry:** Extends the registrant model (`res.partner`) to include geographic coordinates alongside other registrant data.
