---
orphan: true
---

# G2P Mis Importer

The G2P MIS Importer module facilitates the automated synchronization of beneficiary and group data from an external Management Information System (MIS) into OpenSPP. It ensures that OpenSPP's registrant records are consistently updated with the latest information from an authoritative external source, streamlining data management for social protection programs.

## Purpose

The module is designed to bridge the gap between external data sources and OpenSPP's internal registry, accomplishing several key objectives:

*   **Automated Data Import**: Regularly pulls comprehensive beneficiary and group data, including personal details, identification, contact information, and bank accounts, from a configured external MIS.
*   **Maintain Data Consistency**: Ensures that OpenSPP's registrant records reflect the most current information from the external system, reducing discrepancies and improving data accuracy.
*   **Centralized Program Registrations**: Integrates external program enrollment details directly into OpenSPP's program management framework, linking beneficiaries to specific programs defined within the platform.
*   **Reduce Manual Effort**: Eliminates the need for manual data entry or complex reconciliation processes, saving time and minimizing human error in managing large datasets of program participants.

## Dependencies and Integration

This module works in conjunction with other OpenSPP components to deliver its functionality:

*   **[G2P Programs](g2p_programs)**: The G2P MIS Importer links imported individuals and groups to specific social protection programs defined within the G2P Programs module. It ensures that external program enrollments are correctly associated with OpenSPP's program structure, facilitating unified program management.
*   **Queue Job**: The module leverages the Queue Job system to schedule and execute data import tasks asynchronously. This enables large data synchronizations to run efficiently in the background without impacting user performance or system responsiveness.
*   **Core OpenSPP Registrant Models**: The module directly populates and updates `res.partner` records, which serve as the foundation for individual and group registrants within OpenSPP's G2P Registry. This ensures that all imported data contributes to a unified beneficiary database, accessible across the platform.

## Additional Functionality

### External System Configuration
Users configure the connection details for the external MIS within OpenSPP. This setup involves specifying the API endpoints for data retrieval, secure login, and logout, along with authentication credentials such as database name, username, and password. This configuration is essential for establishing a secure and functional link to the external system.

### Scheduled Data Synchronization
The module enables administrators to set up automated, recurring data imports from the external MIS. Users can define the synchronization frequency, for example, every 10 minutes, and the system then automatically pulls new or updated beneficiary and group records, ensuring OpenSPP always has the latest information.

### Registrant and Group Data Import
It imports comprehensive data for both individual registrants and groups into OpenSPP. For individuals, this includes names, various identification documents, phone numbers, email addresses, physical addresses, bank account details, and demographic information such as gender and birthdate. For groups, it imports group-specific details, manages their membership information, and links individual members to their respective groups within OpenSPP.

### Incremental Updates
To optimize performance and resource usage, the module is designed to import only new records or update existing ones that have changed since the last synchronization. It tracks the last update timestamp from the external system, preventing unnecessary re-import of unchanged data and ensuring efficient data management.

### Connection Testing
Before initiating full data synchronization, users can perform a connection test to the external MIS. This verifies that the configured API URLs and authentication credentials are correct and that OpenSPP can successfully communicate with the external system, providing immediate feedback on connectivity status.

## Conclusion

The G2P MIS Importer module is essential for seamlessly integrating external program and beneficiary data into OpenSPP, ensuring data consistency and automating the synchronization of critical information for social protection programs.