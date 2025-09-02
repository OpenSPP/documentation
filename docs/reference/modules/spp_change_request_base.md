---
orphan: true
---

# Change Request Base

The `spp_change_request_base` module provides a robust framework for managing all modifications to registrant information within the OpenSPP platform. It establishes a structured, auditable process for submitting, reviewing, approving, and applying changes to vital data, ensuring accuracy and accountability.

## Purpose

This module streamlines the critical task of updating registrant information, which is fundamental to the effective operation of social protection programs. It ensures that all changes are handled systematically, maintaining data integrity and program reliability.

*   **Standardizes Change Submission:** Provides a consistent method for users to submit any required updates to registrant profiles, such as address changes or family composition modifications.
*   **Enforces Controlled Workflows:** Implements a clear, multi-stage process (draft, pending, validated, applied) for reviewing and approving changes, preventing unauthorized or erroneous data modifications.
*   **Ensures Data Integrity and Auditability:** Maintains a comprehensive history of all requested changes, including who submitted, reviewed, and approved them, ensuring data accuracy and full accountability.
*   **Integrates Document Management:** Automatically links relevant supporting documents directly to each change request, centralizing all information needed for review and approval.
*   **Facilitates User Assignment and Collaboration:** Allows change requests to be assigned to specific users or teams, promoting efficient collaboration and clear ownership throughout the validation process.

## Dependencies and Integration

The `spp_change_request_base` module integrates seamlessly with core OpenSPP functionalities and other key modules to deliver its capabilities.

*   **Base OpenSPP Functionality:** It relies on the fundamental `base` module for core system operations, user management, and data models.
*   **Document Management System ([spp_dms](spp_dms)):** This is a critical dependency. The module automatically creates a dedicated folder within the [spp_dms](spp_dms) for every new change request. This ensures all supporting documentation—like identification cards or proof of address—is securely stored and directly accessible from the change request itself.

This module also serves as a foundational component for other OpenSPP modules that interact with registrant data. Any module needing to modify a registrant's `res.partner` record will leverage `spp_change_request_base` to ensure these updates follow a controlled and auditable process. This includes modules for beneficiary enrollment, program eligibility, and case management, guaranteeing that all changes to a registrant's profile are managed through a standardized workflow.

## Additional Functionality

The `spp_change_request_base` module offers several key features to manage the lifecycle of registrant data changes.

### Structured Change Request Lifecycle

The module defines a clear lifecycle for every change request, moving through distinct states: **Draft**, **Pending Validation**, **Validated**, **Applied**, **Rejected**, and **Cancelled**. Users can initiate a request in a **Draft** state, submit it for **Pending Validation**, and then validators can **Validate** or **Reject** it. Once fully **Validated**, the changes can be **Applied** to the registrant's record. Requests can also be **Cancelled** at various stages or **Reset to Draft** if further modifications are needed before validation. This structured flow ensures that changes are systematically reviewed and approved.

### Dynamic Assignment and Role-Based Validation

Each change request is assigned to a specific user responsible for its processing. The module facilitates reassignment, allowing administrators or authorized users to transfer ownership of a request. Furthermore, the validation process is role-based: a change request can only be validated by users belonging to specific validation groups, ensuring that only qualified personnel approve changes at each stage. This includes checks to prevent deletion of requests unless they are in a **Draft** state and being deleted by their original creator.

### Comprehensive Document Attachment

Every change request automatically generates a dedicated folder within OpenSPP's Document Management System ([spp_dms](spp_dms)). This allows users to attach all necessary supporting documents, such as copies of identification, marriage certificates, or proof of address, directly to the request. This centralized document storage ensures that all evidence for a change is readily available to validators and maintains a complete record for auditing purposes.

### Customizable Validation Sequences

The module supports the definition of customizable validation sequences for different types of change requests. This means that an "Address Change" might require a different set of approvals than a "Family Member Addition." Each sequence consists of multiple validation stages, and each stage can be assigned to a specific user group (e.g., "Data Entry Team," "Regional Manager," "Headquarters Approval"). This flexibility allows programs to tailor validation workflows to their specific operational needs and compliance requirements.

### Registrant Data Linkage and History

The module extends the core `res.partner` model, enabling a direct link between change requests and individual registrant records. This means that users can view a complete history of all change requests associated with a particular registrant, providing a transparent audit trail of every modification made to their profile. This linkage is crucial for understanding the evolution of a registrant's data over time and for ensuring the accuracy of information used in program delivery.

## Conclusion

The `spp_change_request_base` module is a vital component of OpenSPP, centralizing and standardizing the process for updating critical registrant information. It provides a controlled, auditable, and flexible framework that ensures data integrity and operational efficiency across all social protection programs.