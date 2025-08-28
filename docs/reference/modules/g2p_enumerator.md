# G2P Enumerator

The G2P Enumerator module is a core component for capturing, managing, and linking essential field-collected data—such as geographical coordinates and enumerator details—directly to registrant records within OpenSPP. It ensures that crucial context from data collection activities is preserved and associated with individuals and groups.

## Purpose

This module streamlines the process of field data collection by:

*   **Capturing Geolocation Data**: Records precise location details, including latitude, longitude, altitude, and accuracy, for enumeration activities, which is vital for verifying registrant locations and program targeting.
*   **Linking Enumeration Events to Registrants**: Associates individual and group registrant records with specific data collection events, providing a clear record of when and where the data was gathered.
*   **Assigning Unique Enumerator IDs (EIDs)**: Automatically generates and assigns a unique EID to each new registrant, ensuring distinct identification of individuals and groups within the enumeration process.
*   **Tracking Data Creator**: Records the EID of the OpenSPP user who created a registrant record, providing an audit trail and accountability for data entry.

This module is crucial for programs that rely on field visits for data collection, enabling accurate mapping, verification, and traceability of registrant information.

## Dependencies and Integration

The G2P Enumerator module extends the core registrant functionality within OpenSPP by integrating with foundational modules:

*   **[G2P Registry: Group](g2p_registry_group)** and **[G2P Registry: Individual](g2p_registry_individual)**: This module enhances both individual and group registrant records by adding fields for enumeration details, EIDs, and location data. It allows these registrant types to be directly linked to specific enumeration events.
*   **Base (Odoo `base`)**: It leverages the fundamental Odoo framework, particularly extending the `res.partner` model, which serves as the underlying structure for all registrants (individuals and groups) in OpenSPP. This integration ensures that enumeration data is seamlessly incorporated into the existing registrant profiles.

By integrating with these modules, G2P Enumerator ensures that field-collected data enriches the central registrant database, providing a comprehensive view of each individual and group.

## Additional Functionality

### Enumeration Event Management

Users can record and manage details about specific data collection events. Each event captures the date of collection, the identifying user ID of the enumerator, and the precise geographical coordinates (latitude, longitude, altitude, and accuracy) relevant to that enumeration activity. This provides a detailed log of field operations.

### Registrant Data Enrichment

The module significantly enhances registrant records (both individuals and groups) by embedding critical enumeration context:

*   **Linking to Enumeration Data**: Each registrant record can be linked to a specific enumeration event, automatically inheriting the data collection date and the primary enumerator's user ID from that event. This establishes a clear connection between the registrant and the circumstances of their data capture.
*   **Unique Registrant EIDs**: Upon creation, every new registrant (individual or group) automatically receives a unique Enumerator ID (EID). This EID serves as a distinct identifier for the registrant, crucial for managing and referencing records collected during field operations.
*   **Creator Traceability**: The module tracks and records the EID of the OpenSPP user who initially created a registrant's record. This feature provides an important audit trail, enhancing data governance and accountability for data entry.

## Conclusion

The G2P Enumerator module is fundamental to OpenSPP, providing robust capabilities for capturing, linking, and tracking essential field-collected data, thereby enhancing the integrity and contextual richness of all registrant records.