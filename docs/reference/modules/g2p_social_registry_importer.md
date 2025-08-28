# G2P Social Registry Importer

The `g2p_social_registry_importer` module enables OpenSPP to seamlessly integrate with external Social Registries, facilitating the direct import of beneficiary and household data. This module ensures that OpenSPP maintains an up-to-date and accurate registrant database for effective social protection program management.

## Purpose

This module provides a robust mechanism for bringing external social registry data into OpenSPP, offering several key capabilities:

*   **Connect to External Social Registries**: Establishes secure connections to external Social Registry systems, enabling the retrieval of beneficiary information.
*   **Import Individual and Group Data**: Allows for the import of both individual registrants and entire group or household structures, capturing the full scope of social registry data.
*   **Update Existing Beneficiary Records**: Intelligently identifies existing registrants in OpenSPP and updates their information with the latest data from the Social Registry, preventing duplicate entries.
*   **Assign to G2P Programs**: Automatically assigns newly imported or updated registrants to specified G2P programs, streamlining the enrollment process.
*   **Track Import Status**: Records whether each registrant record was newly created or updated during the import process, providing clear traceability.

This module significantly reduces the need for manual data entry, minimizes errors, and ensures that OpenSPP always operates with the most current beneficiary information, which is critical for accurate eligibility determination and benefit disbursement.

## Dependencies and Integration

This module works in conjunction with several other OpenSPP components to deliver its functionality:

*   **OpenSPP Data Source ([spp_registry_data_source](spp_registry_data_source))**: This foundational module provides the framework for configuring and managing connections to external systems. The G2P Social Registry Importer leverages this to define the external Social Registry's API endpoints, authentication methods, and specific search paths.
*   **G2P Programs ([g2p_programs](g2p_programs))**: Once beneficiary data is imported, this module enables the automatic assignment of these registrants to specific social protection programs configured within the G2P Programs module. This ensures imported individuals or groups are immediately linked to relevant program activities.
*   **G2P Registry Membership ([g2p_registry_membership](g2p_registry_membership))**: For imported group-based registrants, this module is crucial for defining and managing the relationships (e.g., Head of Household, Member) between individuals and their respective groups.
*   **Contacts (res.partner)**: All imported beneficiary data, whether for individuals or groups, is stored within OpenSPP's core Contacts model. This module enhances the `res.partner` model by adding a flag to indicate if a registrant was imported from a Social Registry.

## Additional Functionality

The `g2p_social_registry_importer` module offers advanced features to control and optimize the import process:

### Configurable Data Source Connection
Users define the connection parameters for the external Social Registry, including the base URL, authentication details, and specific API paths for data retrieval and authentication. This flexible setup, managed through the Data Source module, allows OpenSPP to integrate with various external registry implementations.

### Targeted Import for Individuals and Groups
The module allows users to specify whether the import targets individual registrants or groups/households from the Social Registry. Additionally, users can opt to automatically assign all imported registrants to a specific G2P program, simplifying program enrollment.

### Intelligent Record Handling and Updates
The system uses unique identifiers from the Social Registry to determine if an incoming record corresponds to an existing registrant in OpenSPP. If a match is found, the existing record is updated; otherwise, a new registrant profile is created. The module tracks if a record was `Created?` or `Updated?` during the import.

### Customizable Data Queries
Users can define specific GraphQL queries to precisely control which data fields are fetched from the external Social Registry and apply filters. This capability allows for highly targeted imports, ensuring only relevant data is retrieved and processed by OpenSPP.

### Scalable Bulk Import Processing
For large social registries with extensive beneficiary lists, the module supports asynchronous processing of bulk imports. This ensures that the system remains responsive and operational even when handling thousands of records, efficiently importing data in the background. The `Last synced on` field tracks the most recent successful data synchronization.

## Conclusion

The `g2p_social_registry_importer` module is a vital component of OpenSPP, providing the essential capability to synchronize beneficiary data from external Social Registries. It ensures OpenSPP operates with accurate and current information, forming a critical foundation for effective social protection program delivery.