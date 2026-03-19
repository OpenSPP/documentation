---
openspp:
  doc_status: draft
  products: [core]
---

# Farmer Registry

A Farmer Registry is a specialized system for collecting and managing data about farm holdings and agricultural households. OpenSPP's Farmer Registry extends the Social Registry with agricultural data collection, land parcel tracking, and GIS integration for mapping and spatial analysis.

**Who is this for:** Agricultural ministries managing farmer support programs, rural development agencies, farming cooperatives, and organizations coordinating food security interventions.

## What Farmer Registry does

Agricultural programs need detailed information about farms, land, and farming practices. Farmer Registry provides:

- **Farmer profiles** with agricultural experience, training, and household data
- **Farm registration** capturing farm types, sizes, and characteristics
- **Land parcel tracking** with GPS coordinates and boundary mapping
- **GIS integration** for spatial analysis and visualization in QGIS
- **Livestock and crop tracking** for comprehensive agricultural data
- **Extension services management** linking farmers to training and advisory support

## Core workflows

| Workflow | Purpose | Key users |
|----------|---------|-----------|
| **Farmer registration** | Collect farmer demographics and agricultural experience | Enumerators, Extension Officers |
| **Farm registration** | Document farm characteristics, types, and legal status | Agricultural Officers |
| **Land parcel mapping** | Capture GPS boundaries and land use data | GIS Specialists |
| **Extension services** | Track training, advisory services, and farmer support | Extension Officers |

## Agricultural data model

Farmer Registry captures comprehensive agricultural information:

### Farmer profile
- National ID and contact information
- Agricultural experience (years farming)
- Formal agricultural training and certifications
- Household composition and demographics

### Farm characteristics
| Attribute | Description |
|-----------|-------------|
| Farm type | Crop, livestock, aquaculture, mixed |
| Total size | Hectares of total farm area |
| Cultivated area | Area under active cultivation |
| Leased area | Rented or borrowed land |
| Legal status | Owned, leased, cooperative, communal |

### Agricultural activities
- **Crop cultivation** - Species grown, seasonal patterns, yields
- **Livestock** - Animals raised, herd sizes, breeds
- **Aquaculture** - Fish farming, pond areas, species
- **Mixed farming** - Combined agricultural activities

## GIS integration

Farmer Registry includes powerful geospatial capabilities:

### Mapping features
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
    A[Register<br/>farmer] --> B[Register<br/>farm]
    B --> C[Map Land<br/>parcels]
    C --> D[Link to<br/>programs]
    E[Extension<br/>services] --> A
    F[GIS<br/>analysis] --> C
```

## Key capabilities

### Farmer profiles
- **Comprehensive demographics** - Full household and individual data
- **Agricultural history** - Years of experience, crops grown, training received
- **Contact management** - Phone, address, location coordinates
- **Document storage** - Land titles, ID cards, certifications

### Farm management
- **Multiple farms per farmer** - Track all holdings for a household
- **Farm categorization** - Classify by type, size, and purpose
- **Seasonal tracking** - Monitor activities across growing seasons
- **Asset inventory** - Farm equipment, machinery, infrastructure

### Land records
- **Parcel registration** - Unique identification for each land plot
- **Tenure tracking** - Ownership status, leases, disputes
- **Use classification** - Crops, pasture, fallow, forest
- **Irrigation systems** - Water sources and irrigation infrastructure

### Extension services
- **Training records** - Courses completed, certifications earned
- **Advisory visits** - Extension officer interactions
- **Input distribution** - Seeds, fertilizers, tools provided
- **Program participation** - Agricultural support programs enrolled

## How it works

```{mermaid}
graph TB
    A[Mass registration<br/>or on-demand] --> B[Farmer<br/>profile]
    B --> C[Farm<br/>registration]
    C --> D[Land parcel<br/>Mapping]
    D --> E[GIS analysis<br/>& visualization]
    F[Extension<br/>services] --> B
    G[Agricultural<br/>programs] --> C
```

1. **Farmer registration** - Collect demographic and agricultural experience data
2. **Farm registration** - Document farm characteristics and legal status
3. **Land parcel mapping** - Capture GPS coordinates and boundaries
4. **GIS integration** - Visualize data in maps, perform spatial analysis
5. **Program integration** - Link farmers to agricultural support programs
6. **Extension tracking** - Record training and advisory services delivered

## Security and access Ccntrol

| Role | Access level | Typical users |
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

## Next steps

**New to Farmer Registry?**
- {doc}`/get_started/installation/docker` - Install OpenSPP
- {doc}`/user_guide/index` - Learn the interface

**Setting up for your organization?**
- {doc}`/config_guide/index` - Configuration overview

**Understanding the concepts?**
- {doc}`/learn/concepts/registry` - Registry concepts explained

## Learn more

- [FAO Farmer Registries](https://socialprotection.org/discover/blog/farmers-registry-tool-support-small-scale-agriculture-and-rural-poverty-reduction) - FAO guidance on farmer registry design
- [DCI Farmer Registry Working Group](https://socialprotection.org/sites/default/files/multimedia_files/Interoperability-in-Action-Farmer-Workshop-27-April-Workshop-4.pdf) - Interoperability standards

## Global examples

Farmer registries are increasingly integrated with social protection systems:

| Country | Registry | Notable Features |
|---------|----------|------------------|
| Brazil | CAF (Cadastro de Agricultura Familiar) | Integrated with Cadastro Único, supports multiple programs |
| Lebanon | National Farmers Registry | Multidimensional rural poverty index, linked to social assistance |
| India (Karnataka) | FRUITS | Integrated with Kutumba SP-MIS and Aadhaar, automatic benefit enrollment |
