# G2P Registry Rest Api Extension Demo

This module serves as a practical demonstration of how to extend the G2P Registry's REST API. It illustrates how to add custom fields to the data models used by the API, allowing external systems to retrieve or send additional, tailored information without modifying core OpenSPP modules.

## Purpose

This module showcases the flexibility of OpenSPP's G2P Registry REST API by demonstrating its extensibility. It provides a clear example for developers to understand how to customize API responses and requests without altering core modules.

*   **Demonstrates API Extensibility:** Clearly illustrates the process of adding new fields to existing API data structures, empowering developers to tailor the API to unique project requirements.
*   **Enhances Group Data Visibility:** Specifically, it extends the group information retrieved via the API to include an 'active' status, providing external systems with a direct indicator of a group's current operational state.
*   **Provides a Customization Blueprint:** Serves as a practical guide and template for developers looking to add their own custom data fields or modify existing API data models.
*   **Facilitates Granular Data Exchange:** Enables more precise and comprehensive data exchange between OpenSPP and integrated external applications by allowing the inclusion of application-specific data points.

## Dependencies and Integration

This module is designed to work as an extension of the core [G2P Registry: Rest API Module](g2p_registry_rest_api). It specifically depends on `g2p_registry_rest_api` to access and extend its defined data models.

Instead of providing new standalone functionality, this module integrates by modifying the structure of data exchanged through the `g2p_registry_rest_api`. It demonstrates how to add new fields to the existing `GroupInfoOut` data model, which is used when external systems request group information from the G2P Registry. This approach allows for non-disruptive customization of API payloads.

## Additional Functionality

This module primarily focuses on demonstrating how to extend API data models, rather than introducing new standalone features.

*   **Extending API Data Models for Groups:**
    This module provides a concrete example of how to add custom fields to the `GroupInfoOut` data model, which defines the structure of group information returned by the REST API. This capability allows developers to include specific data points relevant to their external applications or reporting needs without altering the base API module.
*   **Displaying Group 'Active' Status:**
    Specifically, the module extends the `GroupInfoOut` model to include an `active: bool` field. When external systems query group information via the API, they will now receive an additional field indicating whether the group is currently active or inactive in the OpenSPP system. This enhances the clarity and utility of group data for integrated applications.
*   **Blueprint for Custom API Payloads:**
    Beyond the 'active' status, this module acts as a general blueprint. Developers can follow this pattern to add any number of custom fields, such as specific identifiers, statuses, or related data, to other API data models (e.g., individual profiles, program enrollments) exposed by the [G2P Registry: Rest API Module](g2p_registry_rest_api). This ensures the API can be tailored to meet diverse integration requirements.

## Conclusion

The `g2p_registry_rest_api_extension_demo` module serves as an essential guide, demonstrating the powerful extensibility of OpenSPP's G2P Registry REST API for tailored data exchange and integration.