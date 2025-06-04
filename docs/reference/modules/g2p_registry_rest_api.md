---
review-status: needs-review
review-date: 2025-06-04
reviewer: migration-script
migration-notes: "Added during 2025 documentation reorganization"
---

# G2P Registry: Rest API Module

```{warning}

**Work in Progress**: This document is actively being developed and updated. Content may be incomplete or subject to change.
```

## Overview

The [g2p_registry_rest_api](g2p_registry_rest_api) module extends the functionality of the OpenG2P platform by providing a RESTful API for interacting with the [g2p_registry_membership](g2p_registry_membership) module. This module allows external systems and applications to seamlessly access and manage data related to groups and individuals within the registry.

## Features

- **RESTful API Endpoints:** Exposes API endpoints for performing CRUD (Create, Read, Update, Delete) operations on group and individual records.
- **Integration with FastAPI:** Leverages the FastAPI framework for building high-performance and scalable APIs.
- **Security:** Implements role-based access control to restrict API access based on user permissions defined in the `g2p_security.xml` file.
- **Customizable Endpoints:** Allows for the creation of custom API endpoints to cater to specific integration needs.

## Dependencies

This module directly depends on the following modules:

- **[g2p_registry_membership](g2p_registry_membership):** Provides the core functionality for managing groups and individuals within the registry.
- **fastapi:** A modern, fast (high-performance), web framework for building APIs with Python.
- **extendable_fastapi:** Extends the FastAPI framework with additional features for DCI integration.

## Functionality

The module enhances the OpenG2P platform by:

- **Enabling external system integration:** Provides a standardized way for other systems, such as mobile applications or data analysis tools, to interact with the registry data.
- **Automating data exchange:** Allows for automated data synchronization between the OpenG2P platform and other systems.
- **Building custom applications:** Enables the development of custom applications that leverage the registry data through its API.

## Security

The [g2p_registry_rest_api](g2p_registry_rest_api) module enforces security through the following mechanisms:

- **Role-based access control:** Defines specific roles (`Rest API POST` and `Rest API GET`) that grant access to different API endpoints and operations.
- **DCI authentication:** Leverages DCI's built-in authentication system to authenticate API requests.

## Conclusion

The [g2p_registry_rest_api](g2p_registry_rest_api) module plays a crucial role in enhancing the interoperability and extensibility of the OpenG2P platform. By providing a comprehensive RESTful API, it enables seamless data exchange and integration with external systems, empowering organizations to build more connected and efficient social protection programs. 
