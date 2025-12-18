# OpenSPP Farmer Registry Demo

```{warning}

**Work in Progress**: This document is actively being developed and updated. Content may be incomplete or subject to change.
```

## Overview

The [spp_farmer_registry_demo](spp_farmer_registry_demo) module is a demonstration module for OpenSPP that provides pre-populated data for the farmer registry. It builds upon the [spp_farmer_registry_base](spp_farmer_registry_base) module and its dependencies to showcase the functionalities of the farmer registry with realistic sample data.

## Purpose

This module aims to:

* Populate the farmer registry with sample data, including farmers, groups, farm details, agricultural activities, and assets.
* Provide a starting point for users to explore the farmer registry and its various features.
* Demonstrate how different modules, such as [spp_registry](spp_registry), [queue_job](queue_job), and [spp_base_demo](spp_base_demo), integrate to create a comprehensive farmer registry system.

## Module Dependencies and Integration

* **[spp_farmer_registry_base](spp_farmer_registry_base):** This module depends heavily on [spp_farmer_registry_base](spp_farmer_registry_base), inheriting its models and views to extend them with demo data generation capabilities.
* **[spp_registry](spp_registry):** Leverages [spp_registry](spp_registry) for creating group memberships between individual farmers and farm groups.
* **[queue_job](queue_job):** Uses [queue_job](queue_job) to handle the generation of large datasets in the background, improving performance and user experience.
* **[spp_registry](spp_registry):** Depends on [spp_registry](spp_registry) for the basic registrant models and functionalities.
* **[spp_registry](spp_registry):** Uses [spp_registry](spp_registry) for creating and managing farm groups as registrants.
* **[spp_base_demo](spp_base_demo):** Inherits from [spp_base_demo](spp_base_demo) to include basic demo data, such as genders.
* **[spp_registry](spp_registry):** Utilizes [spp_registry](spp_registry) for creating individual farmer registrants.

## Additional Functionality

The [spp_farmer_registry_demo](spp_farmer_registry_demo) module introduces the following key functionalities:

* **Sample Data Generation:** The module includes a dedicated model, `spp.generate.farmer.data`, and a corresponding form view for generating sample farmer data. This form allows users to specify:
    * The number of farm groups to generate.
    * The locale for generating realistic data based on specific regions.
    * Once the data generation is triggered, the module creates a queue job that populates the database with realistic farmer data, including:
        * Farm Groups: Groups of farmers with detailed information like family name, national ID, contact details, and education level.
        * Individual Farmers: Members of farm groups with personal information and links to their respective groups.
        * Land Records: Land parcels associated with farm groups, including coordinates and geographical polygons.
        * Agricultural Activities: Details of crop, livestock, and aquaculture activities undertaken by each farm group, linked to specific land parcels.
        * Farm Details: Comprehensive information about farm types, sizes, legal status, infrastructure, technologies, and financial services utilized by each farm group.
        * Farm Assets: Data on farm machinery and other assets owned by each farm group, categorized by type and quantity.

* **Data Realism:**  The module utilizes external libraries like `faker` to generate realistic and region-specific data for names, contact details, and other attributes. This ensures that the sample data reflects real-world scenarios.
* **GIS Integration:** The demo data integrates with the GIS functionalities of [spp_farmer_registry_base](spp_farmer_registry_base) to visualize the generated farms and land parcels on a map, providing a visual representation of the farmer registry.

## Conclusion

The [spp_farmer_registry_demo](spp_farmer_registry_demo) module provides a valuable tool for understanding and demonstrating the functionalities of the OpenSPP farmer registry system. By populating the database with realistic sample data, it allows users to explore the system, understand its data structures, and test its various features without having to manually create large datasets. This module simplifies the process of getting started with OpenSPP and showcases the platform's capabilities for managing comprehensive and detailed farmer registries. 
