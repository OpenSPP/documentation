---
orphan: true
---

# G2P Odk Importer

The G2P Odk Importer module connects OpenSPP with ODK Central, enabling the seamless and automated transfer of data collected through ODK forms directly into OpenSPP's registrant registries. This module automates the crucial step of bringing field-collected data into the core social protection platform.

## Purpose

This module streamlines data collection and registration processes by facilitating the direct import of ODK form submissions into OpenSPP:

*   **Automates Data Ingestion:** It automatically pulls new and updated records from ODK Central, eliminating manual data entry and reducing human error in registrant onboarding.
*   **Maps ODK Data to Registries:** Users define how data from ODK forms maps to OpenSPP's individual or group registrant records, ensuring consistency and proper categorization.
*   **Supports Bulk and On-Demand Imports:** The module allows for scheduled, automatic imports of large datasets, as well as immediate, on-demand imports for specific records or urgent updates.
*   **Integrates Media Attachments:** It processes and stores media files (like photos or scanned documents) submitted via ODK forms, linking them directly to the corresponding registrant records.
*   **Accelerates Program Outreach:** By quickly transferring beneficiary data from the field to the system, it significantly speeds up registration and enrollment, enabling faster program delivery.

## Dependencies and Integration

The G2P Odk Importer module operates as a crucial connector, integrating OpenSPP's registry with external data collection tools.

It relies on the `queue_job` module to manage background processing, ensuring that large data imports from ODK do not impact system performance or responsiveness. This allows for efficient handling of extensive datasets without blocking user operations.

The module stores any media files, such as photos or scanned IDs, collected through ODK forms by integrating with the [G2P Documents](g2p_documents) module. This ensures that all supporting documents are securely managed and linked to the relevant registrant records within OpenSPP.

Critically, this module extends the [G2P Registry Base](g2p_registry_base) by creating and updating registrant records in OpenSPP. It populates essential registrant details, including personal information, phone numbers, identification documents, and group memberships or relationships, directly from the imported ODK data.

## Additional Functionality

The G2P Odk Importer provides a robust set of features to manage the connection and data flow between ODK Central and OpenSPP:

### ODK Connection Configuration

Users can define and manage multiple ODK Central configurations within OpenSPP. Each configuration specifies the ODK base URL, login credentials, project ID, and the specific ODK form ID from which data will be imported. A "Test Connection" feature allows administrators to verify connectivity and authentication with the ODK Central server before initiating any imports.

### Flexible Data Mapping

A powerful JSON Formatter allows users to define how fields from an ODK form submission map to the corresponding fields in OpenSPP's registrant records. This uses `jq` expressions, providing a flexible way to transform, select, and combine data elements from the raw ODK JSON into the structure required by OpenSPP, ensuring data accuracy and consistency.

### Automated and On-Demand Data Import

The module offers multiple ways to import data:

*   **Scheduled Imports:** Administrators can set up cron jobs to automatically pull new or updated ODK form submissions at predefined intervals, such as hourly or daily. This ensures OpenSPP's registries are consistently updated with the latest field data.
*   **Manual Bulk Import:** Users can trigger an immediate import of all new or modified records from an ODK form since the last synchronization time, useful for ad-hoc updates or initial data loads.
*   **Single Record Import by Instance ID:** For specific cases, users can import an individual ODK form submission by providing its unique instance ID. This is particularly useful for correcting errors or quickly onboarding a single registrant without waiting for a scheduled import.

```{note}
To enable the single record import feature, ensure the 'Enable ODK import by Instance ID' setting is active in the system's configuration.
```

### Comprehensive Data Handling

Beyond basic registrant details, the importer handles complex data structures from ODK forms. It automatically creates or updates individual or group registrant records, populating associated data such as multiple phone numbers, various identification documents (e.g., national ID, birth certificate), and establishing relationships for group members. The module also processes media attachments, storing images as profile pictures or other files as supporting documents linked to the registrant.

## Conclusion

The G2P Odk Importer is essential for bridging the gap between field-level data collection via ODK and OpenSPP's centralized social protection registries, ensuring timely, accurate, and automated data integration.