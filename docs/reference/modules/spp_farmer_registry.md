---
openspp:
  doc_status: draft
---

# Farmer Registry

**Module:** `spp_farmer_registry`

## Overview

Farmer Registry with vocabulary-based fields, CEL variables, and Logic Studio integration

## Purpose

This module is designed to:

- **Register farms as groups:** Extend `res.partner` with farm-specific fields using `_inherits` delegation to `spp.farm.details`, so farms are first-class registrants.
- **Classify farm details:** Record farm type, land tenure, holder type, and data source using FAO-aligned vocabulary codes instead of fixed selection fields.
- **Track agricultural activities:** Manage crop, livestock, and aquaculture activities with cascading species selection from FAO ICC, FAO Livestock, and FAO ASFIS vocabularies.
- **Manage farm assets and land:** Track equipment, machinery, and extension services; link to land records and irrigation modules for parcel-level management.
- **Provide CEL variables:** Extend the CEL variable system with farm-specific aggregate targets for building eligibility rules based on farm data.
- **Manage agricultural seasons:** Control when farm activities can be recorded with a state machine (draft, active, closed) and overlap prevention.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `spp_registry` | Consolidated registry management for individuals, groups,... |
| `spp_registry_search` | Search-first registry interface for privacy protection |
| `spp_security` | Central security definitions for OpenSPP modules |
| `spp_area` | Establishes direct associations between OpenSPP registran... |
| `spp_vocabulary` | OpenSPP: Vocabulary |
| `spp_farmer_registry_vocabularies` | FAO-aligned vocabularies for farmer registry (crops, live... |
| `spp_cel_domain` | Write simple CEL-like expressions to filter records (Open... |
| `spp_studio` | No-code customization interface for OpenSPP |
| `spp_land_record` | The OpenSPP Land Record module digitizes and centralizes ... |
| `spp_irrigation` | Manages detailed irrigation assets by type, capacity, and... |
| `spp_gis` | GIS core plus area geo fields and importer extensions (po... |

### External Dependencies

| Package | Purpose |
| --- | --- |
| `shapely` | |
| `geojson` | |
| `pyproj` | |

## Key Features

### Farm Details

Farm classification fields are stored in `spp.farm.details` and accessed transparently on the partner via delegation:

| Field | Vocabulary Namespace | Description |
| --- | --- | --- |
| Farm Type | `urn:openspp:vocab:farm-type` | Crop, livestock, aquaculture, or mixed |
| Land Tenure | `urn:openspp:vocab:land-tenure` | Ownership or use rights classification |
| Holder Type | `urn:openspp:vocab:holder-type` | Individual, joint, or institutional (FAO WCA 2020) |
| Data Source | `urn:openspp:vocab:data-source` | Census, self-registration, or field visit |

Acreage fields track total farm size and breakdown by use (crops, livestock, aquaculture, leased out, fallow).

### Computed Farm Indicators

| Field | Description |
| --- | --- |
| `farm_size_hectares` | Alias for total farm size used by CEL variables |
| `is_smallholder` | True if total size is at or below configurable threshold (default 5 ha) |
| `has_productive_land` | True if any land is under crops, livestock, or aquaculture |
| `total_livestock_heads` | Sum of all livestock activity quantities |

### Agricultural Activities

Activities (`spp.farm.activity`) use cascading vocabulary selection based on activity type:

| Activity Type | Species Vocabulary |
| --- | --- |
| Crop Cultivation | `urn:fao:icc:1.1` (FAO ICC Crop Classification) |
| Livestock Rearing | `urn:fao:livestock:2020` (FAO Livestock Classification) |
| Aquaculture | `urn:fao:asfis:2024` (FAO ASFIS Species List) |

Activities track quantity, area planted, expected/actual yield, purpose, cultivation method, and link to agricultural seasons and land parcels.

### Agricultural Seasons

Seasons (`spp.farm.season`) control when activities can be recorded:

- State machine: Draft, Active, Closed with manager-only transitions
- Overlap prevention between active seasons (configurable)
- Force close option for closing before end date
- Prevents activity modifications in closed seasons

### CEL Variable Extension

Extends CEL variables with farm-specific aggregate targets for building eligibility expressions:

| Target | Related Field |
| --- | --- |
| `farm_crop_activities` | `farm_crop_act_ids` |
| `farm_livestock_activities` | `farm_livestock_act_ids` |
| `farm_aquaculture_activities` | `farm_aquaculture_act_ids` |
| `land_parcels` | `farm_land_rec_ids` |

### GIS Support

Farms can have GPS coordinates stored as GeoJSON points. The `get_geojson()` method generates GeoJSON FeatureCollections with coordinate transformation from EPSG:3857 to WGS84.

## Integration

- **spp_registry:** Farms are `res.partner` records (groups) with `_inherits` delegation to `spp.farm.details`.
- **spp_vocabulary / spp_farmer_registry_vocabularies:** All classification fields use vocabulary codes with FAO-aligned namespace URIs.
- **spp_cel_domain / spp_studio:** CEL variables with farm-specific aggregate targets enable no-code eligibility rule building.
- **spp_land_record:** Land parcels are linked to farms and activities for parcel-level tracking.
- **spp_irrigation:** Irrigation assets are associated with farm land parcels.
- **spp_gis:** Farm GPS coordinates enable geographic visualization.

```{toctree}
:maxdepth: 1
:hidden:

spp_farmer_registry_cr
spp_farmer_registry_dashboard
spp_farmer_registry_demo
spp_farmer_registry_vocabularies
```
