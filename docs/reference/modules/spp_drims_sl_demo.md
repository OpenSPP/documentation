---
openspp:
  doc_status: draft
---

# Sri Lanka Demo

**Module:** `spp_drims_sl_demo`

## Overview

Demo data generator for DRIMS Sri Lanka implementation. Creates sample incidents, donations, requests, and stock for demonstrations.

## Purpose

This module is designed to:

- **Generate demo incidents:** Create realistic disaster scenarios (monsoon floods, landslides, drought) with affected areas, per-area severity, and coordination modes.
- **Populate demo donations:** Generate donations from UN agencies and NGOs at various workflow stages (announced through stocked), including lot creation for tracked products.
- **Create demo requests:** Generate supply requests at different states (draft, pending, approved, rejected) with some intentionally overdue for SLA alert demonstration.
- **Populate warehouse stock:** Add initial inventory to all DRIMS warehouses with storable products, lot tracking, and some near-expiry lots for alert demos.
- **Import geographic data:** Import Sri Lanka areas from the official admin boundary Excel file and HDX polygon boundaries for choropleth visualization.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `spp_drims_sl` | Sri Lanka-specific configuration for DRIMS disaster respo... |
| `spp_area_hdx` | HDX Common Operational Datasets (COD) integration for dow... |
| `spp_gis_report` | Geographic visualization and reporting for social protect... |

### External Dependencies

| Package | Purpose |
| --- | --- |
| `faker` | |

## Key Features

### Demo Generator Wizard

A transient model (`spp.drims.demo.generator`) provides a wizard with configurable demo modes:

| Mode | Incidents | Donations/Incident | Requests/Incident | Personnel/Incident |
| --- | --- | --- | --- | --- |
| Quick | 1 | 3 | 5 | 5 |
| Standard | 2 | 5 | 10 | 8 |
| Full | 3 | 8 | 15 | 15 |

### Generated Data

- **Incidents:** Based on realistic Sri Lanka disaster scenarios with multi-area severity and coordination modes (lead agency, cluster, consortium)
- **Donations:** Random donor selection from configured agencies, progressed through the donation workflow to target states
- **Requests:** Include overdue requests for SLA breach demonstration, at-risk requests for SLA warnings, and future-dated normal requests with OCHA cluster assignments
- **Completed dispatches:** Creates validated outgoing pickings with beneficiary counts, POD GPS coordinates, and delivery confirmation for dashboard KPIs
- **Personnel:** Deployed staff with Sri Lankan names, random roles/organizations/clusters, and varied deployment statuses
- **Alerts:** Creates guaranteed sample alerts (low stock, SLA breach, SLA warning) plus runs the alert engine cron jobs to generate additional alerts

### Area Import

Imports Sri Lanka administrative boundaries from an Excel file using the `spp.area.import` system, then assigns area types based on admin level. Links warehouses to their geographic areas and adds GPS coordinates. Optionally imports HDX polygon boundaries (GeoJSON) for choropleth maps using geometry simplification via Shapely.

## Integration

- **spp_drims_sl:** Uses the Sri Lanka configuration (warehouses, products, agencies, users) as the foundation for demo data generation.
- **spp_area_hdx:** Imports HDX COD polygon boundaries for provinces and districts to enable geographic visualization.
- **spp_gis_report:** Refreshes GIS report data after demo generation for choropleth display. Extends GIS report source models to include DRIMS requests.
