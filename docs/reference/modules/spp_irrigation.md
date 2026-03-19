---
openspp:
  doc_status: draft
---

# Irrigation

**Module:** `spp_irrigation`

## Overview

Manages detailed irrigation assets by type, capacity, and unique identifiers, leveraging integrated GIS capabilities to map and display infrastructure locations and boundaries. The module models water distribution networks by defining and linking irrigation sources to destinations, providing critical data for strategic planning of resource allocation and infrastructure projects.

## Purpose

This module is designed to:

- **Record irrigation assets:** Create and manage irrigation infrastructure records with type classification, capacity, and unique identifiers.
- **Map infrastructure locations:** Store point coordinates and polygon boundaries for each irrigation asset using GIS fields.
- **Model water distribution networks:** Define source-to-destination relationships between irrigation assets to represent water flow paths.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `base` | Odoo core framework |
| `spp_gis` | GIS core plus area geo fields and importer extensions (po... |
| `spp_security` | Central security definitions for OpenSPP modules |
| `spp_registry` | Consolidated registry management for individuals, groups,... |
| `spp_farmer_registry_vocabularies` | FAO-aligned vocabularies for farmer registry (crops, live... |

## Key Features

### Irrigation Asset Records

Each irrigation asset captures infrastructure details linked to a farm.

| Field | Description |
| --- | --- |
| Name/ID | Unique name or identifier for the irrigation asset |
| Farm | Link to the farm (group registrant) that owns or uses this asset |
| Asset Type | Vocabulary-based type from `urn:openspp:vocab:irrigation-asset-type` |
| Total Capacity | Numeric capacity value for the asset |
| Coordinates | GIS point location of the asset |
| Geo Polygon | GIS polygon boundary of the asset |

### Water Distribution Network

Irrigation assets can be linked to model water flow:

| Relationship | Description |
| --- | --- |
| Irrigation Sources | Other irrigation assets that supply water to this asset |
| Irrigation Destinations | Other irrigation assets that receive water from this asset |

Both relationships use many-to-many links, allowing complex distribution networks where a single source can feed multiple destinations and vice versa.

## Integration

- **spp_gis:** Uses `GeoPointField` and `GeoPolygonField` to store and display irrigation asset locations and boundaries on maps.
- **spp_registry:** Links irrigation assets to farm registrants (group partners) for ownership tracking.
- **spp_farmer_registry_vocabularies:** Uses the irrigation asset type vocabulary for standardized infrastructure classification.
