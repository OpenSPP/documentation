---
openspp:
  doc_status: draft
  products: [core]
---

# Farm details, seasons, and activities

This guide is for **implementers** configuring farm activity tracking, seasonal records, and asset management.

## Seasons

Seasons define time periods for agricultural activity tracking:

| Field | What it means |
|-------|---------------|
| **Name** | Season label (e.g., "2025 Wet Season") |
| **Farm** | Which farm this season belongs to |
| **Start Date** | Season start |
| **End Date** | Season end |

Seasons allow tracking activities (planting, harvesting) within specific time frames, enabling year-over-year comparison.

## Activities

Activities record what a farm produces or raises during a season:

| Field | What it means |
|-------|---------------|
| **Farm** | Which farm |
| **Season** | Which season |
| **Activity Type** | Crop, Livestock, or Aquaculture |
| **Species/Variety** | What is grown/raised (from vocabulary) |
| **Area** | Land area used (for crops) |
| **Quantity** | Head count (for livestock) or volume |

### Activity patterns

| Activity Type | Key Fields | Example |
|--------------|------------|---------|
| Crop | Species, area (hectares), expected yield | Rice, 1.5 ha, 4 tons |
| Livestock | Species, head count, purpose | Cattle, 12 head, dairy |
| Aquaculture | Species, pond area, stocking density | Tilapia, 0.5 ha, 5000 fingerlings |

## Assets

Assets track farm equipment and infrastructure:

| Field | What it means |
|-------|---------------|
| **Farm** | Which farm |
| **Asset Type** | Category (from vocabulary) |
| **Name** | Description |
| **Quantity** | Number of items |
| **Condition** | Current state |

### Common asset types

| Category | Examples |
|----------|---------|
| Machinery | Tractor, water pump, thresher |
| Infrastructure | Irrigation system, greenhouse, storage facility |
| Vehicles | Truck, motorcycle |
| Tools | Hand tools, sprayers |

## Extension services

Extension records track agricultural advisory services provided to farms:

| Field | What it means |
|-------|---------------|
| **Farm** | Which farm received the service |
| **Service Type** | Kind of extension service |
| **Date** | When the service was provided |
| **Provider** | Who provided the service |
| **Notes** | Details and recommendations |

## Are You Stuck?

**How do I set up seasons for a new year?**

Create season records for each farm with the appropriate date ranges. Seasons are per-farm, so you can have different agricultural calendars for different regions.

**Activities from vocabulary not showing expected crops?**

Ask your administrator to install the **Farmer Registry Vocabularies** module for the complete FAO-aligned crop and livestock lists.

**Can I track multiple activities per season?**

Yes. A farm can have many activities in one season (e.g., rice + vegetables in the same wet season).

**How do I report on aggregate farm data?**

If the `spp_farmer_registry_dashboard` module is installed, it provides CEL-based metrics and trends across farms. Note: this module is currently in Alpha status and requires `spp_dashboard_base`.

## Next steps

- {doc}`overview` - Farmer registry fundamentals
- {doc}`/config_guide/vocabulary/overview` - Configure agricultural vocabularies
- {doc}`/config_guide/session_tracking/overview` - Track farmer training sessions
