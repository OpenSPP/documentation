---
orphan: true
---

# G2P Mts

The `g2p_mts` module integrates OpenSPP's G2P Registry with external Micro-Transfer Systems (MTS), enabling the secure and efficient transfer of registrant data for payment processing or other services. It acts as a bridge, allowing OpenSPP to share specific registrant information with external systems based on defined criteria.

## Purpose

The `g2p_mts` module streamlines the process of extracting and securely transmitting registrant data from the OpenSPP G2P Registry to external Micro-Transfer Systems (MTS). It ensures that only relevant and authorized information is shared, facilitating various social protection operations like beneficiary authentication or payment disbursements.

Key capabilities include:

*   **Configurable Data Extraction**: Defines specific criteria (filters) to select which registrants from the G2P Registry are included in a data transfer.
*   **Customizable Field Selection**: Specifies which fields (e.g., name, birthdate, ID) for selected registrants are sent to the MTS, ensuring data minimization.
*   **Secure Data Transmission**: Encapsulates and securely sends the extracted registrant data to the designated external MTS endpoint for further processing.
*   **Automated Data Management**: Manages the lifecycle of certain sensitive identification data (like Virtual IDs) based on configurable rules, enhancing data privacy.
*   **Integration with MTS Connector**: Extends the core MTS Connector functionality to specifically handle data sourced from the OpenSPP G2P Registry.

This module is vital for ensuring that social protection programs can seamlessly interact with payment providers or other external systems, allowing for efficient beneficiary management and service delivery. For example, it can extract all registrants eligible for a specific benefit payment in a certain region and securely provide their details to a mobile money provider.

## Dependencies and Integration

The `g2p_mts` module builds upon and extends core OpenSPP functionalities to achieve its integration capabilities:

-   **[MTS Connector](mts_connector)**: This is the primary module extended by `g2p_mts`. The `g2p_mts` module adds the "OpenG2P Registry" as a specific input type option within the `MTS Connector` configuration, allowing users to define MTS jobs that source data directly from the G2P Registry.
-   **[G2P Registry Base](g2p_registry_base)**: The `g2p_mts` module directly interacts with the core registrant data managed by `G2P Registry Base`. It queries and extracts information from the `res.partner` model (representing registrants) and their associated identification records (`g2p.reg.id`), ensuring that only authorized and filtered data is prepared for transfer.

This module acts as a specialized data provider for the `MTS Connector`, enabling it to leverage the rich, structured data of the `G2P Registry Base` for various external system interactions.

## Additional Functionality

### Configuring Registry Data for MTS
Users can define precisely which registrant data to send to an external MTS. This configuration occurs within the `MTS Connector` setup, where the `MTS Input Type` is set to 'OpenG2P Registry'.

*   **Registry Filters**: Specify criteria using standard Odoo domain syntax to select a subset of registrants. For example, `[["is_registrant", "=", True], ["reg_ids.id_type", "=like", "MOSIP VID"]]` would select all active registrants with a MOSIP Virtual ID.
*   **Selected Fields**: Choose specific fields from the registrant's profile (e.g., `given_name`, `birthdate`, `phone`) that the MTS requires. This ensures data minimization and adherence to privacy principles by only sharing necessary information.
*   **JSON Validation**: The module validates that the entered filters and field lists are correctly formatted JSON, preventing configuration errors before data processing.

### Automated Virtual ID (VID) Management
The module includes a critical feature for managing sensitive Virtual IDs, particularly in scenarios involving token-based authentication.

*   **VID Deletion Rule**: A scheduled job can be configured to automatically delete a registrant's Virtual ID (VID) if a corresponding UIN (Unique Identification Number) token is present. This process helps enhance security and privacy by removing temporary or sensitive identifiers once a more permanent or tokenized ID is in use.
*   **Configurable Deletion Scope**: Administrators can define a search domain to specify which registrants are subject to this automated VID deletion, allowing for targeted application of the privacy measure.
*   **ID Type Configuration**: The system allows for defining which specific `g2p.id.type` records represent Virtual IDs and UIN tokens, ensuring the automated process correctly identifies and manages the relevant identifiers.

## Conclusion

The `g2p_mts` module is a crucial component of OpenSPP, enabling secure and configurable data exchange between the G2P Registry and external Micro-Transfer Systems for streamlined program operations and beneficiary services. It ensures efficient, privacy-aware data sharing, supporting the dynamic needs of social protection programs.