# G2P Registry: Additional Info REST API Module

```{warning}

**Work in Progress**: This document is actively being developed and updated. Content may be incomplete or subject to change.
```

This module extends the functionality of the [g2p_registry_rest_api](g2p_registry_rest_api) and [g2p_registry_addl_info](g2p_registry_addl_info) modules by providing API endpoints for managing additional G2P (Government-to-Person) information associated with registrants and group memberships. 

### Functionality and Integration

This module introduces two new classes:

- **RegistrantAddlInfoIn** and **RegistrantAddlInfoOut**: These classes, extending the existing `RegistrantInfoIn` and `RegistrantInfoOut` classes from the [g2p_registry_rest_api](g2p_registry_rest_api) module, add fields for handling additional G2P information during data input and output for individual registrants. This allows external systems to read and write this custom information through the API.

- **GroupMembersInfoIn**:  This class extends the `GroupMembersInfoIn` class from the [g2p_registry_rest_api](g2p_registry_rest_api) module and adds a field for managing additional G2P information associated with group memberships. This facilitates exchanging custom group-related data via the API.

By integrating with the core registry and REST API modules, this module enables a seamless flow of additional G2P data, ensuring that external systems can access and manage this crucial information alongside the standard registry data.

### Key Features:

- **API Endpoints for Additional G2P Info:** Provides dedicated API endpoints for managing additional G2P information related to individual registrants and group memberships.
- **Data Model Extension:** Extends the existing data models for registrants and group memberships to accommodate additional G2P information.
- **Seamless Integration:** Integrates smoothly with the [g2p_registry_rest_api](g2p_registry_rest_api) module, leveraging its existing infrastructure for authentication, authorization, and data handling.

### Benefits:

- **Enhanced Data Management:** Enables efficient management of custom G2P data alongside standard registry information.
- **Improved Interoperability:** Facilitates data exchange with external systems that require access to additional G2P information.
- **Flexibility and Customization:** Allows for tailored data structures to meet the specific needs of different social protection programs. 
