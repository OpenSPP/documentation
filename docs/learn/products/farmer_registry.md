---
openspp:
  doc_status: draft
  products: [core]
---

# Farmer Registry

A Farmer Registry is a specialized system for collecting and managing data about farm holdings and agricultural households. OpenSPP's Farmer Registry extends the Social Registry with agricultural data collection, land parcel tracking, and GIS integration for mapping and spatial analysis.

**Who is this for:** Agricultural ministries managing farmer support programs, rural development agencies, farming cooperatives, and organizations coordinating food security interventions.

## What Farmer Registry Does

Agricultural programs need detailed information about farms, land, and farming practices. Farmer Registry provides:

- **Farmer profiles** with agricultural experience, training, and household data
- **Farm registration** capturing farm types, sizes, and characteristics
- **Land parcel tracking** with GPS coordinates and boundary mapping
- **GIS integration** for spatial analysis and visualization in QGIS
- **Livestock and crop tracking** for comprehensive agricultural data
- **Extension services management** linking farmers to training and advisory support

## Core Workflows

| Workflow | Purpose | Key Users |
|----------|---------|-----------|
| **Farmer Registration** | Collect farmer demographics and agricultural experience | Enumerators, Extension Officers |
| **Farm Registration** | Document farm characteristics, types, and legal status | Agricultural Officers |
| **Land Parcel Mapping** | Capture GPS boundaries and land use data | GIS Specialists |
| **Extension Services** | Track training, advisory services, and farmer support | Extension Officers |

## Agricultural Data Model

Farmer Registry captures comprehensive agricultural information:

### Farmer Profile
- National ID and contact information
- Agricultural experience (years farming)
- Formal agricultural training and certifications
- Household composition and demographics

### Farm Characteristics
| Attribute | Description |
|-----------|-------------|
| Farm Type | Crop, livestock, aquaculture, mixed |
| Total Size | Hectares of total farm area |
| Cultivated Area | Area under active cultivation |
| Leased Area | Rented or borrowed land |
| Legal Status | Owned, leased, cooperative, communal |

### Agricultural Activities
- **Crop cultivation** - Species grown, seasonal patterns, yields
- **Livestock** - Animals raised, herd sizes, breeds
- **Aquaculture** - Fish farming, pond areas, species
- **Mixed farming** - Combined agricultural activities

## GIS Integration

Farmer Registry includes powerful geospatial capabilities:

### Mapping Features
- **GPS coordinate capture** - Record farm and parcel locations
- **Boundary mapping** - Define land parcel boundaries
- **GeoJSON API** - Standard format for spatial data exchange
- **QGIS integration** - Visualize and analyze in desktop GIS

### Spatial Analysis
- **Land use mapping** - Categorize and track land utilization
- **Proximity analysis** - Distance to markets, water sources, roads
- **Satellite imagery integration** - Monitor crop conditions remotely
- **Climate data overlay** - Weather patterns and risk assessment

```{mermaid}
graph LR
    A[Register<br/>Farmer] --> B[Register<br/>Farm]
    B --> C[Map Land<br/>Parcels]
    C --> D[Link to<br/>Programs]
    E[Extension<br/>Services] --> A
    F[GIS<br/>Analysis] --> C
```

## Key Capabilities

### Farmer Profiles
- **Comprehensive demographics** - Full household and individual data
- **Agricultural history** - Years of experience, crops grown, training received
- **Contact management** - Phone, address, location coordinates
- **Document storage** - Land titles, ID cards, certifications

### Farm Management
- **Multiple farms per farmer** - Track all holdings for a household
- **Farm categorization** - Classify by type, size, and purpose
- **Seasonal tracking** - Monitor activities across growing seasons
- **Asset inventory** - Farm equipment, machinery, infrastructure

### Land Records
- **Parcel registration** - Unique identification for each land plot
- **Tenure tracking** - Ownership status, leases, disputes
- **Use classification** - Crops, pasture, fallow, forest
- **Irrigation systems** - Water sources and irrigation infrastructure

### Extension Services
- **Training records** - Courses completed, certifications earned
- **Advisory visits** - Extension officer interactions
- **Input distribution** - Seeds, fertilizers, tools provided
- **Program participation** - Agricultural support programs enrolled

## How It Works

```{mermaid}
graph TB
    A[Mass Registration<br/>or On-Demand] --> B[Farmer<br/>Profile]
    B --> C[Farm<br/>Registration]
    C --> D[Land Parcel<br/>Mapping]
    D --> E[GIS Analysis<br/>& Visualization]
    F[Extension<br/>Services] --> B
    G[Agricultural<br/>Programs] --> C
```

1. **Farmer registration** - Collect demographic and agricultural experience data
2. **Farm registration** - Document farm characteristics and legal status
3. **Land parcel mapping** - Capture GPS coordinates and boundaries
4. **GIS integration** - Visualize data in maps, perform spatial analysis
5. **Program integration** - Link farmers to agricultural support programs
6. **Extension tracking** - Record training and advisory services delivered

## Security & Access Control

| Role | Access Level | Typical Users |
|------|--------------|---------------|
| Registry Viewer | Read-only access to farmer data | Analysts, auditors |
| Enumerator | Create and update farmer registrations | Field data collectors |
| Agricultural Officer | Manage farms and land records | Extension officers |
| GIS Specialist | Access spatial data and mapping tools | GIS analysts |
| Registry Manager | Full administration and configuration | System administrators |

## Dependencies

Farmer Registry extends Social Registry with agricultural modules:

- **spp_registry** - Core registry (inherited from Social Registry)
- **spp_gis** - Geospatial capabilities and GeoJSON API
- **spp_land_record** - Land parcel management
- **spp_irrigation** - Irrigation system tracking
- **spp_custom_field** - Custom field support for country-specific data

## Next Steps

**New to Farmer Registry?**
- {doc}`/get_started/installation/docker` - Install OpenSPP
- {doc}`/user_guide/index` - Learn the interface

**Setting up for your organization?**
- {doc}`/config_guide/index` - Configuration overview

**Understanding the concepts?**
- {doc}`/learn/concepts/registry` - Registry concepts explained

## Learn More

- [FAO Farmer Registries](https://socialprotection.org/discover/blog/farmers-registry-tool-support-small-scale-agriculture-and-rural-poverty-reduction) - FAO guidance on farmer registry design
- [DCI Farmer Registry Working Group](https://socialprotection.org/sites/default/files/multimedia_files/Interoperability-in-Action-Farmer-Workshop-27-April-Workshop-4.pdf) - Interoperability standards

## Global Examples

Farmer registries are increasingly integrated with social protection systems:

| Country | Registry | Notable Features |
|---------|----------|------------------|
| Brazil | CAF (Cadastro de Agricultura Familiar) | Integrated with Cadastro Único, supports multiple programs |
| Lebanon | National Farmers Registry | Multidimensional rural poverty index, linked to social assistance |
| India (Karnataka) | FRUITS | Integrated with Kutumba SP-MIS and Aadhaar, automatic benefit enrollment |
