---
orphan: true
---

# G2P Registry Rest Api

The 'G2P Registry Rest Api' module provides a robust set of RESTful API endpoints, enabling external systems and integrations to securely interact with the OpenSPP G2P Registry. It acts as the primary interface for creating, updating, and querying individual and group registrant data within the platform.

## Purpose

This module serves as the crucial gateway for external applications to access and manage the core G2P Registry data. It accomplishes this by:

*   **Enabling External System Integration**: Provides a standardized, programmatic interface for other applications to connect with OpenSPP's G2P Registry.
*   **Managing Individual Registrant Data**: Facilitates the creation and update of individual profiles, including personal details, identification documents, and contact information.
*   **Managing Group Registrant Data**: Supports the creation and update of group profiles, allowing for the registration of households or other collective entities.
*   **Ensuring Data Integrity**: Implements essential validations to ensure that incoming data adheres to predefined standards, such as verifying ID types, group types, and gender against system configurations.
*   **Securing API Access**: Enforces secure communication by requiring authentication for all API interactions, protecting sensitive registrant data.

## Dependencies and Integration

This module is foundational, extending OpenSPP's core API capabilities and relying on other modules for its data structures and processing logic:

*   **[G2P Registry Membership](g2p_registry_membership)**: This module processes and integrates data related to group memberships and individual roles within groups. The API leverages the data models and business logic defined in the Membership module when handling group-related operations.
*   **FastAPI**: It extends the core FastAPI integration within OpenSPP, providing the framework for defining and exposing the RESTful endpoints. This dependency ensures a modern, high-performance API.
*   **Extendable FastAPI**: Builds upon the `fastapi` module to offer a flexible and extensible structure for defining new API endpoints and customizing existing ones, allowing OpenSPP to grow with evolving program needs.

## Additional Functionality

The 'G2P Registry Rest Api' module offers the following key features for managing registrant data:

### Comprehensive Registrant Data Management
The module provides endpoints to create and update detailed profiles for both individual and group registrants. For individuals, this includes personal information like names (given, family, additional), birthdate, birthplace, email, address, and an optional profile image. For groups, it manages the group name, registration date, email, address, and specifies if it's a partial group.

### Robust Identification and Contact Information Processing
It supports the processing of multiple identification documents (IDs) for each registrant, including the ID type, value, expiry date, status, and description. Similarly, it manages multiple phone numbers, identifying a primary contact number. The API validates that provided ID types exist within the system, preventing data entry errors.

### Gender and Group Type Validation
The API includes built-in validation for demographic data. When processing individual registrants, it ensures that the provided gender information aligns with predefined gender types in the system. For groups, it validates the specified group 'kind' (e.g., Household, Cooperative) against the system's configured group types, ensuring data consistency.

### Secure API Authentication
All interactions with the G2P Registry API endpoints require authentication. The module is configured to use Basic Authentication, ensuring that only authorized external systems or users with valid credentials can access and modify sensitive registrant data.

## Conclusion

The 'G2P Registry Rest Api' module is the essential interface that empowers external systems to securely and efficiently manage individual and group registrant data within the OpenSPP platform.