# G2P Odk User Mapping

The G2P Odk User Mapping module establishes a critical link between OpenSPP's internal partner records and the individuals collecting data through ODK Central. It enables the system to understand who is submitting ODK forms by mapping their ODK app user accounts to specific OpenSPP partners, such as field agents or enumerators.

## Purpose

This module streamlines the management of field data collectors and enhances data traceability by directly associating ODK app users with OpenSPP partners:

*   **Link Field Agents to OpenSPP Partners:** Establishes a direct connection between individuals collecting data via ODK forms and their corresponding partner records within OpenSPP, such as field agents or enumerators.
*   **Automated ODK App User Synchronization:** Automatically fetches and updates the list of ODK app users from ODK Central based on configured ODK connections, ensuring OpenSPP has current user information.
*   **Enhanced Data Traceability:** Improves the traceability of collected data by associating ODK form submissions with the specific ODK app user and their linked OpenSPP partner, providing clarity on data origin.
*   **Flexible ODK Configuration per Partner:** Allows different OpenSPP partners to be associated with distinct ODK Central configurations, enabling decentralized or multi-project data collection efforts.
*   **Streamlined Partner Management:** Simplifies the process of managing field staff by centralizing their ODK user accounts and OpenSPP partner records, facilitating better oversight and operational efficiency.

## Dependencies and Integration

The G2P Odk User Mapping module extends core OpenSPP functionalities and integrates closely with its data collection ecosystem.

It depends on the `base` module for fundamental system operations and data models. The `account` module is also listed as a dependency, highlighting its reliance on the core `res.partner` model, which is often linked to accounting and contact management in OpenSPP.

Critically, this module relies on `g2p_odk_importer` to provide the foundational ODK Central connection configurations. While `g2p_odk_importer` handles the import of form data, `g2p_odk_user_mapping` enhances it by enabling the identification and mapping of the specific ODK user who submitted the data. This module extends the `res.partner` model by adding fields to store ODK-specific configurations and the linked ODK app user, making partners identifiable within the ODK data flow.

## Additional Functionality

The module provides robust features for managing ODK app users and linking them to OpenSPP partners:

### ODK App User Management

OpenSPP automatically retrieves and stores a list of ODK app users from a configured ODK Central instance. Each ODK app user is identified by their display name and a unique ODK App User ID, providing a comprehensive roster of individuals authorized to collect data. This list is dynamically updated when ODK configurations are changed or refreshed for a partner.

### Partner-Specific ODK Configuration

Users can associate an OpenSPP partner (e.g., a field agent) with a specific ODK Central configuration. This allows for scenarios where different partners might operate under distinct ODK projects or even separate ODK Central instances, providing flexibility in program implementation. When an ODK configuration is linked to a partner, the system automatically fetches the relevant ODK app users for that configuration.

### Linking ODK App Users to Partners

Once ODK app users are retrieved, administrators can link a specific ODK App User to an OpenSPP partner record. This direct association ensures that any data submitted by that ODK App User can be attributed back to the corresponding OpenSPP partner, improving data governance and accountability. The link facilitates identifying who collected specific data points.

## Conclusion

The G2P Odk User Mapping module is essential for bridging OpenSPP's partner management with ODK Central's data collection, ensuring that field data is properly attributed and managed within the social protection platform.