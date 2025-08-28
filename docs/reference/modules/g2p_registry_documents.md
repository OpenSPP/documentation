# G2P Registry Documents

The G2P Registry Documents module provides essential functionality for attaching, storing, and managing supporting documents directly within OpenSPP registrant profiles. It ensures that all necessary paperwork, identification, and evidence related to individuals and groups are centrally accessible and securely stored.

## Purpose

This module streamlines the management of registrant documentation by offering a dedicated system to link files directly to profiles. It ensures that comprehensive and verifiable records are maintained for all participants in social protection programs and farmer registries.

*   **Attach Documents to Registrants:** Users can upload and associate various types of documents, such as national ID cards, birth certificates, or application forms, directly with individual or group registrant profiles.
*   **Centralized Document Access:** All supporting documents for a specific registrant are consolidated and easily viewable from their profile, providing a complete and immediate overview.
*   **Secure and Scalable Storage:** It leverages OpenSPP’s robust document management system to securely store files, ensuring data integrity and scalability for large volumes of documentation.
*   **Facilitate Compliance and Audits:** By maintaining a clear link between registrants and their documents, the module supports program compliance, simplifies verification processes, and aids in external audits.
*   **Support Diverse Document Types:** The module handles a wide range of file formats, allowing for the comprehensive collection of textual, image, and other digital evidence.

## Dependencies and Integration

The G2P Registry Documents module extends core OpenSPP capabilities by integrating closely with existing registry and document management components.

It builds upon the robust file storage and management provided by the `[G2P Documents](g2p_documents)` module, ensuring that all uploaded files benefit from secure storage backends and metadata handling. This module extends `g2p_documents`'s capabilities by specifically linking files to registrant records.

The module integrates with the foundational `[G2P Registry Base](g2p_registry_base)` module, which defines the core registrant model (``res.partner``). It adds the capability to attach documents directly to these base registrant records, supporting both `[G2P Registry Individual](g2p_registry_individual)` and `[G2P Registry Groups](g2p_registry_group)` profiles. This ensures a consistent approach to document management across all registrant types.

## Additional Functionality

The G2P Registry Documents module offers key features to enhance document management for social protection programs:

### Direct Document Attachment to Registrant Profiles

Users can easily upload and link documents directly to an individual or group registrant's profile page. This allows for the immediate association of supporting evidence, such as proof of identity, household manifests, or application forms, with the relevant registrant. The system supports various file types, including images, PDFs, and other digital formats.

### Consolidated View of Supporting Documents

Each registrant's profile includes a dedicated section displaying all attached supporting documents. This centralized view provides a comprehensive overview of all collected evidence, making it simple for program staff to review and verify information without navigating to separate systems. Documents are listed with their names and types for quick identification.

### Document Preview and Access

The module allows users to preview attached documents directly within the system interface, streamlining the review process. For documents stored externally (e.g., in cloud storage), it provides direct links for easy access and download. This functionality ensures that program staff can quickly inspect content without needing to download files locally.

### Secure and Scalable Document Handling

Leveraging the underlying `G2P Documents` module, all files attached via this module are stored using configured secure storage backends, such as cloud-based solutions. This ensures that sensitive registrant data is protected, highly available, and scalable to accommodate the needs of large-scale social protection programs.

## Conclusion

The G2P Registry Documents module is vital for maintaining complete, verifiable, and securely stored documentation for all registrants within OpenSPP, supporting efficient program administration and compliance.