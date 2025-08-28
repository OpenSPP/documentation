# G2P Registry Addl Info Rest Api

This module extends OpenSPP's REST API to include the flexible, program-specific additional information captured for individual registrants and group members. It enables external systems to seamlessly read, create, and update all relevant registrant data, including custom fields, through API calls.

## Purpose

This module ensures that all program-specific data for OpenSPP registrants is fully accessible and manageable via the platform's REST API. Its key capabilities include:

*   **Exposing Custom Registrant Data:** It makes the flexible `additional_g2p_info` field, defined by specific social protection programs, available through the OpenSPP REST API. This allows external applications to interact with the full scope of beneficiary information.
*   **Enabling External System Integration:** The module empowers external systems, such as mobile applications or partner databases, to seamlessly integrate with OpenSPP to manage comprehensive registrant profiles.
*   **Facilitating Data Exchange:** It supports robust data exchange by ensuring that all relevant registrant details, including core information and program-specific additions, can be retrieved and updated in a unified manner.
*   **Supporting Diverse Program Needs:** By exposing the customizable additional information field, the module allows programs to tailor data collection without requiring core system modifications, and then access that data externally. For example, an external system can update a beneficiary's specific "enrollment status" or "disability type" field.

## Dependencies and Integration

This module acts as a crucial bridge, integrating capabilities from two foundational OpenSPP modules to serve external systems.

It depends on the [G2P Registry: Rest API Module](g2p_registry_rest_api), which provides the core RESTful API framework for interacting with registrant and group data. This module extends the existing API endpoints from `g2p_registry_rest_api` to include the additional information.

It also depends on the [G2P Registry: Additional Info Module](g2p_registry_addl_info), which introduces the flexible `additional_g2p_info` field for individual registrants and group members within OpenSPP. This module specifically makes that flexible data field accessible via the API.

By combining these, `g2p_registry_addl_info_rest_api` serves external systems by providing a complete data picture. It allows them to read and write all relevant registrant details, including custom program-specific data, thereby enhancing OpenSPP's interoperability.

## Additional Functionality

The module's primary function is to extend OpenSPP's API capabilities to encompass the rich, program-specific data managed within the system.

### API Access to Program-Specific Data

This module enables external users and systems to read, create, and update the flexible `additional_g2p_info` field for both individual registrants and group members through the REST API. This field stores unstructured, program-specific data in JSON format, accommodating diverse data points such as a beneficiary's unique identifiers from other systems, specific health conditions, or detailed household assets. It ensures that any custom data configured and collected within OpenSPP via the `g2p_registry_addl_info` module is fully integrated into API-driven workflows.

### Comprehensive Registrant Data Exchange

The module extends existing API endpoints for registrants and group members to seamlessly include the `additional_g2p_info` field in API requests and responses. This means external systems can retrieve or submit all registrant details—including core identifying information and any program-specific additions—in a single, unified API call. This capability simplifies data synchronization processes and ensures that external applications always have a complete and up-to-date view of beneficiary information, crucial for effective program management and reporting.

## Conclusion

The `g2p_registry_addl_info_rest_api` module ensures that all program-specific, flexible data for OpenSPP registrants and groups is fully accessible and manageable through the platform's REST API, facilitating comprehensive external system integration.