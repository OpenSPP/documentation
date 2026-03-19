---
openspp:
  doc_status: draft
---

# Starter: Farmer Registry

**Module:** `spp_starter_farmer_registry`

## Overview

Complete Farmer Registry bundle with API, DCI, and Program support

## Purpose

This module is designed to:

- **Provide a one-click farmer registry deployment:** Bundle all modules needed for a complete farmer registry into a single installable package, including social registry foundations, farmer-specific fields, land management, GIS, and program support.
- **Set deployment-specific defaults:** Configure system parameters such as the smallholder farm size threshold (default: 5.0 hectares, adjustable per region following FAO recommendations).

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `spp_starter_social_registry` | Complete Social Registry bundle with API, DCI, and Change... |
| `spp_farmer_registry` | Farmer Registry with vocabulary-based fields, CEL variabl... |
| `spp_farmer_registry_vocabularies` | FAO-aligned vocabularies for farmer registry (crops, live... |
| `spp_land_record` | The OpenSPP Land Record module digitizes and centralizes ... |
| `spp_irrigation` | Manages detailed irrigation assets by type, capacity, and... |
| `spp_gis` | GIS core plus area geo fields and importer extensions (po... |
| `spp_programs` | Manage cash and in-kind entitlements, integrate with inve... |

## Key Features

### Bundled Modules

This is a meta-module that installs the following functional areas in a single step:

| Area | Modules Included |
| --- | --- |
| Social Registry Foundation | `spp_starter_social_registry` (includes registry, security, area, vocabulary, API, DCI) |
| Farmer Registry | `spp_farmer_registry`, `spp_farmer_registry_vocabularies` |
| Land & GIS | `spp_land_record`, `spp_irrigation`, `spp_gis` |
| Programs | `spp_programs` for subsidies and grants |

### Configuration Parameters

Sets the following system parameter on installation:

| Parameter | Default | Description |
| --- | --- | --- |
| `spp.farmer.smallholder_threshold` | 5.0 | Maximum farm size (hectares) to qualify as a smallholder. Varies by region (Sub-Saharan Africa: 2 ha, South Asia: 2 ha, Southeast Asia: 3 ha, Latin America: 5-10 ha). |

## Integration

- **spp_starter_social_registry:** Inherits the complete social registry foundation, ensuring all prerequisite modules (registry, security, area, vocabulary, API, DCI, change requests) are installed.
- **spp_farmer_registry:** Provides farmer-specific fields and CEL variables on the registry.
- **spp_land_record / spp_irrigation:** Adds land parcel and irrigation asset management for agricultural contexts.
- **spp_gis:** Enables geographic mapping and spatial analysis for farmer locations and land parcels.
- **spp_programs:** Provides program management for agricultural subsidies, grants, and entitlements.
