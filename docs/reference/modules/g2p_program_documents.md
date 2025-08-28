# G2P Program Documents

The G2P Program Documents module enhances OpenSPP's core document and program management capabilities by enabling the direct association of documents with specific program enrollments and individual benefit entitlements. This module ensures that all program-related documentation is systematically organized, easily accessible, and integrated directly into the lifecycle of social protection programs.

## Purpose

This module streamlines document management for G2P programs, providing critical capabilities for compliance, auditability, and efficient program operations:

*   **Associate Documents with Program Enrollments:** Users can securely link beneficiary identification, application forms, and other supporting documents directly to a beneficiary's membership within a specific program. This centralizes all relevant information for a beneficiary's participation.
*   **Attach Documents to Specific Entitlements:** The module allows for attaching documents, such as proof of delivery or signed receipts, to individual benefit disbursements or entitlements. This provides a granular audit trail for each benefit issued.
*   **Automate Document Flow to Entitlements:** When new entitlements are generated, the system can automatically copy and link relevant documents from the beneficiary's program membership, reducing manual effort and ensuring consistent documentation.
*   **Configure Program-Specific Document Storage:** Each G2P program can define its own preferred document storage backend, allowing for tailored storage solutions based on program requirements or regional data policies.
*   **Enhance Auditability and Compliance:** By linking documents directly to program memberships and entitlements, the module significantly improves the ability to audit program operations, verify beneficiary eligibility, and ensure compliance with regulatory requirements.

## Dependencies and Integration

The G2P Program Documents module builds upon and integrates deeply with other foundational OpenSPP modules to deliver its functionality.

It extends the capabilities of the [G2P Documents](g2p_documents) module, utilizing its underlying infrastructure for secure file storage and management. This module specifically enhances the `storage.file` and `storage.backend` models to introduce direct links to program memberships and entitlements, tailoring the general document storage for G2P program needs.

Furthermore, this module is tightly integrated with the [G2P Programs](g2p_programs) module. It extends core program entities such as `g2p.program`, `g2p.program_membership`, and `g2p.entitlement` to incorporate document fields and management directly into the program lifecycle. This integration ensures that documentation is a seamless part of program definition, beneficiary enrollment, and benefit issuance processes.

## Additional Functionality

The G2P Program Documents module offers several key features to enhance document management within social protection programs:

### Program-Specific Document Storage Configuration

Each G2P program can be configured with its own dedicated document storage backend. This allows program administrators to select appropriate storage solutions (e.g., local server, cloud storage like S3) based on data residency requirements, security policies, or performance needs unique to that program. This flexibility ensures that document storage aligns with specific program operational contexts.

### Linking Documents to Program Membership

Users can upload and associate various types of documents, such as beneficiary application forms, identity documents, or household surveys, directly with a beneficiary's membership in a specific G2P program. This feature centralizes all documentation relevant to a beneficiary's enrollment and ongoing participation, making it easy to review their program-specific history and eligibility.

### Linking Documents to Entitlements

The module enables the attachment of documents directly to individual entitlements, which represent specific benefit disbursements or services provided. For instance, users can upload signed receipts, proof of delivery, or verification photos for each payment cycle. This granular linking provides a robust audit trail, critical for accountability and fraud prevention.

### Automated Document Association

To streamline workflows, the module can automatically link relevant documents to newly generated entitlements. When a beneficiary receives a new benefit, documents previously attached to their program membership, such as their national ID, can be automatically associated with the new entitlement. This reduces manual data entry and ensures that all necessary supporting documentation is consistently available for each benefit.

## Conclusion

The G2P Program Documents module is essential for creating a robust, auditable, and efficient documentation system within OpenSPP, directly linking critical documents to program enrollments and individual benefit entitlements.