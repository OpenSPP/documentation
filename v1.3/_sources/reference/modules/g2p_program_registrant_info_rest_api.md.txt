---
orphan: true
---

# G2P Program Registrant Info Rest Api

The `g2p_program_registrant_info_rest_api` module provides a RESTful API for external systems to access and manage program-specific application information for registrants within OpenSPP. It extends existing program membership APIs to seamlessly integrate detailed application data.

## Purpose

This module enables external systems to interact with the granular application details collected from registrants for various social protection programs. Its key capabilities include:

*   **Expose Program Application Data:** Makes detailed, program-specific application information available through standard API endpoints for external consumption.
*   **Integrate with Program Memberships:** Allows for the creation, update, and retrieval of program-specific application data directly when managing program memberships.
*   **Support Dynamic Data Structures:** Accommodates flexible and dynamic application forms by supporting JSON data structures for program-specific details.
*   **Facilitate External System Integration:** Enables seamless data exchange between OpenSPP and external applications, such as mobile enrollment apps or government portals.
*   **Enhance Data Accessibility:** Provides structured access to crucial application data, supporting informed decision-making and efficient program management from external platforms.

This module ensures that detailed application information, such as eligibility criteria responses or supporting document details, can be managed and retrieved alongside a registrant's program enrollment status. For example, an external system can submit a new program application, including all specific form fields, and enroll the registrant in one API call.

## Dependencies and Integration

This module acts as an extension layer, enhancing the capabilities of other core OpenSPP modules by exposing their data via a REST API.

*   **[G2P Programs REST API](g2p_programs_rest_api)**: This module extends the data models defined in `g2p_programs_rest_api`, specifically augmenting program membership operations. It allows program-specific registrant information to be included directly when creating, updating, or querying program memberships.
*   **[G2P Program: Registrant Info](g2p_program_registrant_info)**: This module relies on `g2p_program_registrant_info` as its foundational data source. It provides the REST API layer for the program-specific application data models and logic defined within `g2p_program_registrant_info`.

By integrating with these modules, `g2p_program_registrant_info_rest_api` serves as a critical bridge, allowing external systems to programmatically interact with the detailed application and enrollment processes within OpenSPP.

## Additional Functionality

The module provides robust functionality for managing program-specific registrant application data through its API.

### Enriching Program Membership APIs

This module extends the existing REST APIs for program memberships to include detailed program-specific application information. When creating or updating a program membership, external systems can directly provide the associated application details. Conversely, when retrieving program membership data, the API response will include the relevant program registrant information, such as application status and submitted form data. This ensures a comprehensive view of a registrant's program journey.

### Accessing Program-Specific Application Data

The module provides structured access to the program-specific application information collected for each registrant. This allows external systems to query and retrieve the full details of an application, including any custom fields or data points gathered during the enrollment process. This capability is vital for external dashboards, reporting tools, or other systems needing to analyze or display detailed application statuses and content.

### Supporting Dynamic Application Forms

OpenSPP programs often require varied data collection forms. This module supports dynamic data structures for program-specific application information, typically stored as JSON. This flexibility ensures that the API can accommodate diverse application requirements without needing code changes, allowing programs to collect and manage unique sets of data through a standardized interface.

## Conclusion

The `g2p_program_registrant_info_rest_api` module is essential for enabling external systems to seamlessly access and manage detailed, program-specific application information for registrants within OpenSPP. It enhances the platform's interoperability by exposing critical program enrollment data through a comprehensive and flexible REST API.