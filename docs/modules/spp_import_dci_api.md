# OpenSPP Import: DCI API

```{warning}

**Work in Progress**: This document is actively being developed and updated. Content may be incomplete or subject to change.
```

## Overview

The [spp_import_dci_api](spp_import_dci_api.md) module is an OpenSPP extension that enables the integration of external registries, particularly those adhering to the [DCI (Digital Convergence Initiative)](https://spdci.org/) standard, into the OpenSPP ecosystem. 

## Purpose

This module streamlines the process of importing and synchronizing registrant data from DCI-compliant registries into the OpenSPP registry. This facilitates efficient data sharing and interoperability between different systems. For more information, visit [Digital Convergence Initiative](https://spdci.org/).

## Key Features

* **API Endpoints:**
    *  Exposes RESTful API routes specifically designed for interacting with DCI-compliant systems. 
    *  Handles authentication and authorization for secure data exchange.
* **Data Mapping:**
    *  Maps incoming DCI data fields to the corresponding fields within the OpenSPP registry.
    *  Handles data transformations to ensure compatibility between the two systems.
* **Import Processes:**
    *  Provides automated workflows for importing new registrants and updating existing records.
    *  Includes data validation steps to maintain data integrity within the OpenSPP registry.

## Dependencies and Integration

## 1. OpenSPP Programs ([spp_programs](spp_programs.md))

* **Integration:** Utilizes program definitions and eligibility criteria from [spp_programs](spp_programs.md) to potentially assign imported registrants to relevant programs based on their DCI attributes. 

## 2. SPP Programs ([spp_programs](spp_programs.md))

* **Integration:** Similar to [spp_programs](spp_programs.md), this module might utilize in-kind entitlement logic from [spp_programs](spp_programs.md) if the imported DCI data includes information relevant to in-kind benefits.

## 3. OpenSPP Registry ([spp_registry](spp_registry.md))

* **Integration:**  Relies heavily on [spp_registry](spp_registry.md) for core registry functionality:
    *   **Registrant Creation:** Creates new registrant records using the base model provided by [spp_registry](spp_registry.md).
    *   **ID Management:** Leverages `spp.reg.id` from [spp_registry](spp_registry.md) to store and manage DCI-provided identifiers.
    *   **Relationships:**  Potentially utilizes the `spp.reg.rel` model to establish relationships between imported registrants based on DCI data. 

## 4. SPP Registry Data Source ([spp_registry_data_source](spp_registry_data_source.md))

* **Integration:** Depends on [spp_registry_data_source](spp_registry_data_source.md) for:
    * **Data Source Configuration:** Retrieves connection details and API specifications of the external DCI registry from data source configurations defined in this module. 

## 5. OpenSPP Registry ([spp_registry](spp_registry.md))

* **Integration:**  Extends the individual registrant model (`res.partner`) from [spp_registry](spp_registry.md):
    *   **Data Population:** Populates individual-specific fields within the OpenSPP registry using mapped DCI data (e.g., name, birthdate, gender). 

## Additional Functionality

## CRVS Integration

The module includes specialized components for interacting with CRVS (Civil Registration and Vital Statistics) systems, which are often DCI-compliant. These components include:

* **Location Management:**
    *   Models CRVS-specific location hierarchies (`spp.crvs.location.type`, `spp.crvs.location`).
    *   Imports and synchronizes location data from the CRVS system.
* **Beneficiary Fetching:**
    *   Provides tools (`spp.fetch.crvs.beneficiary`) to search and retrieve beneficiary data from CRVS systems based on specific criteria.
    *   Supports complex search queries using logical operators and field filters. 
* **Data Import and Processing:**
    *   Processes retrieved CRVS data, creating or updating registrant records in OpenSPP (`spp.crvs.imported.individuals`).
    *   Handles the creation of family groups and relationships based on CRVS data. 

## Conclusion

The [spp_import_dci_api](spp_import_dci_api) module enhances the OpenSPP platform by enabling seamless data exchange with external DCI-compliant registries, including specialized integration with CRVS systems. This promotes interoperability, streamlines data management, and expands the potential reach of OpenSPP implementations. For more information, visit [Digital Convergence Initiative](https://spdci.org/).
