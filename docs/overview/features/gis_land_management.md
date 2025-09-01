# Geospatial (GIS) and Land Management

OpenSPP integrates Geographic Information System (GIS) capabilities to manage, visualize, and analyze location-based data, enabling precise geographic targeting for {term}`social protection` programs and comprehensive land record management for agricultural interventions.

## Spatial Intelligence

Location matters profoundly in social protection delivery. Natural disasters affect specific geographic areas, agricultural support must account for land characteristics and ownership, and service delivery points need strategic placement to ensure accessibility. Traditional text-based systems struggle to capture and utilize spatial relationships effectively—understanding that a {term}`household` is within a flood zone, calculating the total area under cultivation by program {term}`beneficiaries <beneficiary>`, or identifying underserved areas all require spatial analysis capabilities that go beyond simple address fields.

OpenSPP's GIS integration transforms location from static data points into actionable intelligence. For emergency response programs, the platform can instantly identify all registered households within disaster-affected areas using precise geographic boundaries rather than approximate administrative units. Agricultural programs can link farmers to specific land parcels, track land use patterns, assess irrigation coverage, and calculate area-based subsidies with precision. The visual mapping interface makes geographic patterns immediately apparent—clusters of vulnerability, gaps in service coverage, or areas of program overlap that would remain hidden in tabular data. This spatial intelligence enables more effective resource allocation, better program targeting, and evidence-based decisions about where to expand services or establish new distribution points.

## GIS Capabilities

* **Hierarchical Administrative Boundaries**: Define and manage nested geographic areas from country level down to villages with precise polygon boundaries
* **Interactive Map Visualization**: Display {term}`registrants <registrant>`, service points, and program coverage on interactive maps with multiple data layers
* **Geospatial Data Capture**: Record precise locations using GPS coordinates for households, farms, distribution centers, and infrastructure
* **Land Parcel Management**: Define agricultural plots with boundaries, link them to farmers, and track ownership or usage rights
* **Spatial Eligibility Criteria**: Target programs based on geographic criteria such as distance from services or location within specific zones
* **Area Calculation and Analysis**: Automatically calculate land areas for subsidy determination and analyze spatial distribution patterns
* **Irrigation Infrastructure Mapping**: Track irrigation systems, water sources, and coverage areas for agricultural planning
* **Disaster Impact Assessment**: Overlay hazard maps with beneficiary locations to rapidly identify affected populations

## Technical Foundation

The GIS and land management functionality is delivered through specialized modules:

* **[spp_base_gis](/reference/modules/spp_base_gis.md)**: Core GIS framework and mapping infrastructure
* **[spp_area](/reference/modules/spp_area.md)**: Administrative area definition and management
* **[spp_area_gis](/reference/modules/spp_area_gis.md)**: GIS-enabled area management with spatial operations
* **[spp_land_record](/reference/modules/spp_land_record.md)**: Land parcel registration and ownership tracking
* **[spp_irrigation](/reference/modules/spp_irrigation.md)**: Irrigation infrastructure mapping and management
* **[spp_farmer_registry_base](/reference/modules/spp_farmer_registry_base.md)**: Integration of spatial data with farmer registries
* **[spp_base_gis_rest](/reference/modules/spp_base_gis_rest.md)**: REST API for GIS data access and operations