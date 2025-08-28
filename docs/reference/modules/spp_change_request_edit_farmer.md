# OpenSPP Change Request Edit Farmer

The OpenSPP Change Request Edit Farmer module provides a structured workflow for submitting, reviewing, and applying updates to existing farmer records within the OpenSPP registry. It ensures that all modifications to critical farmer data follow a formal approval process.

## Purpose

This module formalizes the process of updating farmer information, ensuring data accuracy and maintaining a clear audit trail. It accomplishes this by:

*   **Standardizing Farmer Data Updates**: Introduces a consistent, multi-step process for modifying existing farmer profiles, from initiation to final application.
*   **Ensuring Data Integrity and Validation**: Applies validations to critical fields like birthdates and mobile numbers, preventing errors and maintaining high data quality.
*   **Facilitating Supporting Document Management**: Allows for the attachment and management of necessary documents, such as scanned identification, to support requested changes.
*   **Streamlining Approval Workflows**: Integrates with the broader change request framework to route updates through defined validation sequences for authorization.
*   **Providing an Audit Trail**: Records every stage of the change request, offering full transparency on who requested, reviewed, and approved each modification.

## Dependencies and Integration

The `spp_change_request_edit_farmer` module extends and integrates with several core OpenSPP modules to deliver its functionality:

*   **[OpenSPP Change Request](spp_change_request)**: This is the foundational module that provides the generic change request framework. `spp_change_request_edit_farmer` leverages its core workflow for request stages, validation, and approval.
*   **[G2P Registry Individual](g2p_registry_individual)**: Relies on this module to access and manage the individual farmer's core demographic data. Changes initiated by this module directly modify the individual records managed here.
*   **[G2P Registry Group](g2p_registry_group)**: Used for identifying and linking farmers to their associated groups, if applicable, during the change request process.
*   **[G2P Registry Membership](g2p_registry_membership)**: Integrates to understand and potentially update a farmer's membership details within groups.
*   **[OpenSPP Service Points](spp_service_points)**: Enables the submission of change requests from designated service points or agents, linking the request to its origin.
*   **[spp_idpass](spp_idpass)**: Utilized for processing and capturing details from scanned identification documents, which often serve as evidence for farmer data updates.
*   **[OpenSPP Farmer Registry Base](spp_farmer_registry_base)**: Builds upon this module to access farmer-specific data fields and ensure consistency with the overall farmer registry structure.

## Additional Functionality

The `spp_change_request_edit_farmer` module provides a comprehensive set of features for managing farmer data updates:

### Initiating and Tracking Farmer Updates

Users can initiate a change request to modify an existing farmer's profile. The module provides a dedicated form for selecting the target farmer and specifying the fields to be updated. Each request proceeds through a configurable workflow, ensuring proper review and approval before any changes are applied to the live farmer record.

### Comprehensive Farmer Data Fields

The module allows for updates to a wide range of farmer-specific information. Key fields include:

*   **Personal Identification**: Updates to National ID Number and details captured from scanned ID documents.
*   **Demographic Information**: Modifications to family name, given name, additional name, gender, marital status, and farmer date of birth.
*   **Contact Details**: Adjustments to mobile telephone number and email address.
*   **Household and Education**: Updates to farmer household size, postal address, formal agricultural training status, and highest education level.

### Data Validation and Constraints

To maintain data quality, the module incorporates several validation rules:

*   **Birthdate Validation**: Prevents users from entering future dates for a farmer's birthdate, ensuring logical and accurate records.
*   **Mobile Number Validation**: Ensures that entered mobile telephone numbers adhere to correct country-specific formats, improving contactability.
*   **Required Fields**: Mandates the selection of a specific farmer for the change request to proceed, preventing ambiguous updates.

### Document Management System Integration

The module integrates with OpenSPP's Document Management System (DMS) to securely store supporting documents. Users can attach files and directories related to the change request, such as scanned ID cards, proof of address, or other relevant evidence. This ensures that all changes are backed by verifiable documentation.

### Live Data Application

Upon final approval of a change request, the module automatically updates the corresponding live farmer record in the registry. This includes modifying demographic fields, updating phone numbers, and registering new or updated national ID numbers. The system also ensures that any name changes are reflected across the farmer's profile.

```{note}
The module allows viewing the associated group details directly from the change request, providing context to the farmer's affiliations.
```

## Conclusion

The `spp_change_request_edit_farmer` module is essential for maintaining accurate and up-to-date farmer information within OpenSPP. It provides a robust, auditable, and user-friendly system for managing changes to farmer records, crucial for the integrity of social protection programs and farmer registries.