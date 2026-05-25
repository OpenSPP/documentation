---
openspp:
  doc_status: draft
---

# Demo module

The DRIMS demo module (`spp_drims_sl_demo`) provides ready-to-use Sri Lanka demonstration data for exploring disaster response inventory management capabilities. It is designed for training, product demonstrations, and system testing.

## What's included

| Item | Description |
|------|-------------|
| Demo incidents | Realistic disaster scenarios based on Sri Lanka hazard types |
| Donations | Donations from UN agencies and NGOs at various workflow stages |
| Supply requests | Requests at different states including overdue for SLA demonstration |
| Warehouse stock | Initial inventory across all DRIMS warehouses with lot tracking |
| Geographic data | Sri Lanka administrative boundaries with HDX polygon data for maps |
| Personnel | Deployed staff with varied roles, clusters, and organizations |
| Alerts | Sample low-stock, SLA breach, and SLA warning alerts |

## Demo incidents

Three disaster scenario types are available (configurable by demo mode):

| Incident type | Description |
|---------------|-------------|
| Monsoon floods | Multi-area flood event with severity mapping |
| Landslide | Localized event affecting specific districts |
| Drought | Slow-onset event affecting agricultural areas |

## Demo modes

The demo generator supports three volume modes:

| Mode | Incidents | Donations per incident | Requests per incident | Personnel per incident |
|------|-----------|----------------------|----------------------|----------------------|
| Quick | 1 | 3 | 5 | 5 |
| Standard | 2 | 5 | 10 | 8 |
| Full | 3 | 8 | 15 | 15 |

## Supply requests

Requests are generated at different states to demonstrate workflow stages:

| State | Purpose |
|-------|---------|
| Draft | Not yet submitted |
| Pending | Awaiting approval |
| Approved | Ready for dispatch |
| Rejected | Declined requests |
| Overdue | Intentionally past SLA deadline for alert demonstration |

## Geographic data

The demo imports Sri Lanka administrative boundaries from the official admin boundary dataset and HDX polygon data, linking warehouses to their geographic areas and enabling choropleth map visualizations.

## Installing the demo

The DRIMS demo is installed as a standard Odoo module (`spp_drims_sl_demo`). Read more about {doc}`module installation </get_started/modules/index>`.

## Missing documentation

The following items are not yet available:

- **DRIMS installation guide** — The `get_started/modules/drims_installation.md` page does not exist. The DRIMS product page cannot currently link to a step-by-step installation guide.
- **Try DRIMS guide** — A step-by-step walkthrough for exploring the DRIMS demo data (equivalent to the {doc}`Try SP-MIS guide </get_started/try_our_products/try_spmis/index>`) does not yet exist.
- **Demo user list** — Pre-configured demo usernames, roles, and passwords for the DRIMS demo have not been documented.
