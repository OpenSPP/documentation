---
openspp:
  doc_status: draft
orphan: true
---

# Demo module

The Farmer Registry demo module (`spp_farmer_registry_demo`) provides ready-to-use demonstration data for exploring Farmer Registry capabilities. It is designed for training, product demonstrations, and system testing without requiring manual data setup.

## What's included

| Item | Count |
|------|-------|
| Named farmer personas | 8 |
| Edge case personas | 3 |
| Farm cooperatives (group-of-groups) | 2 |
| Volume farms (generated) | ~730 |
| Demo programs | 5 |
| Geographic areas (Philippine provinces) | 8 |
| Change requests at various workflow stages | Yes |
| Pre-configured eligibility rules (Logic Packs) | Yes |

## Demo programs

Five agricultural subsidy programs are pre-configured with CEL-based eligibility and benefit formulas:

| Program | Description |
|---------|-------------|
| Input Subsidy | Per-hectare scaling for smallholders with productive land |
| Equipment Grant | Experience-based grant for farmers with 2+ years of experience |
| Livestock Support | Per-head scaling for livestock owners |
| Climate Resilience | Targets farms with idle or fallow land |
| Aquaculture Support | Activity-specific support for aquaculture farmers |

## Demo personas

Eight named farmer personas cover realistic agricultural scenarios, plus three edge cases for testing eligibility boundaries:

| Name | Story |
|------|-------|
| Maria Santos | 2ha rice farmer; eligible for Input Subsidy (smallholder with productive land) |
| Juan Dela Cruz | 3ha mixed farmer with crops and livestock; eligible for Input Subsidy and Equipment Grant |
| Rosa Garcia | Female-headed livestock farm with 20 goats; eligible for Livestock Support |
| Amir Mangudadatu | 4ha drought-affected farm with 1ha idle land; eligible for Climate Resilience |
| Sofia Martinez | Female smallholder transitioning to organic farming; 2ha of vegetables and maize |
| Ramon dela Cruz | 0.5ha tilapia fishpond on leased land; eligible for Aquaculture Support |
| Sittie Pangandaman | 1.5ha crop farm, experienced farmer (12 years); eligible for Input Subsidy and Equipment Grant |
| Danilo Villanueva | 5ha mixed commercial farm at smallholder threshold; eligibility depends on threshold configuration |

**Edge cases:**

| Name | Story |
|------|-------|
| AgriCorp Holdings | 50ha commercial farm; ineligible for smallholder programs — demonstrates targeting exclusion |
| Idle Land Farm | 3ha farm with all land idle; ineligible for Input Subsidy but may qualify for Climate Resilience |
| New Farmer | 2ha smallholder with 1 year experience; eligible for Input Subsidy but not Equipment Grant |

**Farm cooperatives (group-of-groups):**

| Name | Description |
|------|-------------|
| Nueva Ecija Rice Cooperative | Rice cooperative with Maria Santos and Sofia Martinez as member farms (4ha combined) |
| BARMM Farmers Federation | Federation in Bangsamoro with Amir Mangudadatu and Sittie Pangandaman farms (5.5ha combined) |

## Demo users

Two users are pre-configured for testing change request approval workflows:

| Role | Username | Purpose |
|------|----------|---------|
| CR Local Validator | demo_cr_local_validator | Reviews change requests at the local level |
| CR HQ Validator | demo_cr_hq_validator | Reviews and approves change requests at HQ level |

## Change request types

| CR type | Description |
|---------|-------------|
| Update Farm Details | Modify core farm information |
| Manage Farm Activity | Add, update, or remove crop and livestock activities |
| Manage Farm Assets | Record or update machinery and equipment |
| Manage Land Parcels | Add or modify land parcel records |

## Geographic data

The demo generates farms across 8 Philippine provinces with GPS coordinates and land parcel polygons for GIS visualization.

## Installing the demo

The Farmer Registry demo is installed as a standard Odoo module (`spp_farmer_registry_demo`). After installation:

1. Navigate to **Settings > Demo Data > Load Farmer Demo**
2. Click **Load Demo Data** to generate all farmers, programs, and cooperatives

Read more about {doc}`module installation </get_started/modules/index>`.
