# G2P Openid Vci Programs

The `g2p_openid_vci_programs` module extends OpenSPP's Verifiable Credential issuance capabilities to specifically manage and issue digital credentials for beneficiaries of social protection programs. It enables OpenSPP to attest to an individual's enrollment and status within a specific program using secure, verifiable digital documents.

## Purpose

This module enables OpenSPP to serve as a trusted issuer of Verifiable Credentials (VCs) that confirm an individual's beneficiary status within a social protection program. It significantly enhances the transparency and verifiability of program participation.

*   **Issue Program-Specific Beneficiary Credentials:** OpenSPP can issue digital credentials proving an individual's enrollment and status in a particular social protection program. This provides beneficiaries with a portable and verifiable proof of their benefits.
*   **Automate Beneficiary Data Retrieval:** The module automatically collects relevant beneficiary data, including personal details, registered IDs, and program membership status, to populate the Verifiable Credential. This streamlines the issuance process and reduces manual data entry.
*   **Ensure Enrollment Verification:** It rigorously validates that an individual requesting a credential is an actively enrolled beneficiary in the specified program before issuing the VC. This prevents unauthorized credential issuance and maintains program integrity.
*   **Enhance Trust and Security:** By leveraging Verifiable Credentials, the module provides a secure, tamper-evident way for beneficiaries to share their program status with third parties, such as financial institutions or service providers, without exposing sensitive underlying data.
*   **Support Digital Identity for Social Protection:** It contributes to a robust digital identity framework for social protection, allowing for more efficient and auditable interactions between beneficiaries and various service providers.

## Dependencies and Integration

This module builds upon and extends the core functionalities of two other foundational OpenSPP modules:

*   **[G2P OpenID VCI](g2p_openid_vci)**: This is the primary dependency. The `g2p_openid_vci_programs` module extends the generic Verifiable Credential Issuer model from `g2p_openid_vci` to introduce a specialized "Beneficiary" issuer type. This allows OpenSPP to create VCI issuers specifically for program beneficiaries.
*   **[G2P Programs](g2p_programs)**: This module provides the essential data for social protection programs and their membership. `g2p_openid_vci_programs` integrates with `g2p_programs` to link VCI issuers directly to specific social protection programs and to retrieve critical beneficiary enrollment and membership status information required for credential issuance.

## Additional Functionality

### Program-Specific Beneficiary Issuer Configuration
Administrators can configure new Verifiable Credential Issuers within OpenSPP that are specifically designated for program beneficiaries. Each "Beneficiary" issuer is directly linked to a particular social protection program, ensuring that credentials issued by it are relevant to that program. This allows for clear segregation and management of credential types based on the program they represent.

### Automated Beneficiary Status Verification
When a Verifiable Credential is requested, the module automatically verifies the individual's identity against their registered IDs and confirms their active enrollment status within the linked social protection program. If the individual's ID is not found or if they are not currently enrolled in the program, the system will prevent the issuance of the credential, ensuring data accuracy and program security.

### Comprehensive Beneficiary Data Inclusion
Upon successful verification, the module dynamically gathers all necessary beneficiary information to populate the Verifiable Credential. This includes personal details of the beneficiary, their specific membership status in the program, and general details about the social protection program itself, creating a rich and verifiable digital attestation of their status. The credential will include details such as the beneficiary's name, address, program ID, and enrollment dates.

### Standardized Credential Types
The module automatically assigns a default credential type, `OpenG2PBeneficiaryVerifiableCredential`, for all beneficiary-related VCs. This standardization ensures consistency and interoperability, making it easier for external verifiers to recognize and process these credentials.

## Conclusion

The `g2p_openid_vci_programs` module is crucial for enabling OpenSPP to securely issue verifiable digital credentials that confirm an individual's status as a beneficiary of a social protection program, enhancing trust and streamlining interactions across the ecosystem.