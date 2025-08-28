# G2P Programs Rest Api

This module provides a RESTful API for managing program enrollments for individuals and groups within OpenSPP. It allows external systems to interact programmatically with the platform's social protection program data, facilitating seamless integration and automation.

## Purpose

The `g2p_programs_rest_api` module empowers external systems to manage program participation data, extending OpenSPP's core program management capabilities through a standardized API.

*   **Manage Registrant Program Enrollments:** Create, update, and retrieve program enrollment details for individual registrants, including their current state and historical participation.
*   **Handle Group Program Memberships:** Associate entire groups with specific social protection programs and manage the enrollment details for individuals within those groups via the API.
*   **Automate Program Assignment:** Enable automated assignment of beneficiaries to social protection programs from external systems or for efficient batch processing.
*   **Integrate External Systems:** Facilitate seamless data exchange between OpenSPP and other applications, such as mobile enrollment tools or partner databases, for program-related information.
*   **Streamline Data Updates:** Efficiently update program enrollment statuses, such as initial enrollment dates or exit dates, for beneficiaries across various programs through programmatic interfaces.

## Dependencies and Integration

This module builds upon existing OpenSPP functionalities to provide its API services, creating a comprehensive interface for program data.

*   **[G2P Registry: Rest API](g2p_registry_rest_api)**: This module forms the foundational API layer for managing individuals and groups in the OpenSPP registry. `g2p_programs_rest_api` extends its data models, allowing program enrollment information to be included when creating, updating, or querying registrant and group membership data through the API.
*   **[G2P Programs](g2p_programs)**: This core module defines the social protection programs themselves, their cycles, and eligibility rules. `g2p_programs_rest_api` exposes the data structures related to program membership defined in `g2p_programs` via the API, enabling external systems to interact with these program-specific records.

## Additional Functionality

### Program Enrollment for Individuals
Users can create and manage program enrollments for individual registrants directly through the API. This includes specifying the program name and the enrollment date. The API also allows for retrieving a registrant's full history of program participation, including the program ID, current state (e.g., active, exited), enrollment date, and any exit dates.

### Group-Based Program Membership Management
The module extends the API for group memberships to include program enrollment details for the group's members. When managing a group's membership via the API, it is now possible to simultaneously assign or update program enrollments for the individuals within that group. This simplifies the process for programs that onboard beneficiaries in a group context.

### Standardized Data Exchange for Program Membership
The module defines clear and consistent data structures for program membership information, both for incoming data (e.g., when enrolling a registrant) and outgoing data (e.g., when querying enrollment status). This standardization ensures reliable data exchange with external systems, facilitating easier integration and reducing potential data errors.

## Conclusion

The `g2p_programs_rest_api` module is crucial for extending OpenSPP's program management capabilities, enabling external systems to programmatically manage and access social protection program enrollment data for individuals and groups.