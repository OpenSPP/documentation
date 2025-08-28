# G2P Openid Vci

The `g2p_openid_vci` module enables OpenSPP to function as a secure and interoperable issuer of Verifiable Credentials (VCs) using OpenID Connect Verifiable Credentials Issuer (OpenID VCI) standards. It allows the platform to generate and manage digital proofs of identity, program participation, or beneficiary status, enhancing trust and streamlining interactions within social protection programs.

## Purpose

This module equips OpenSPP with the capability to issue digital credentials that are secure, verifiable, and interoperable. It accomplishes this by:

*   **Configuring OpenSPP as a Credential Issuer**: Establishes OpenSPP as a trusted entity capable of issuing digital credentials, defining its unique identifier and the types of credentials it can provide.
*   **Defining Credential Types**: Allows administrators to specify the structure and content for various verifiable credentials, such as "Program Enrollment Credential" or "Beneficiary Status Credential."
*   **Managing Authorization for Issuance**: Implements robust access controls, ensuring that only authorized applications and users can request and receive specific credentials.
*   **Generating Signed Credentials**: Automates the process of creating cryptographically signed digital credentials based on existing registrant data, ensuring their authenticity and integrity.
*   **Providing Standardized Metadata**: Publishes essential information about the issuer and its supported credentials, enabling external systems and digital wallets to easily discover and interact with OpenSPP as a credential provider.

This module's value lies in enabling secure, digital proof of claims, reducing the need for physical documents, and simplifying verification processes for beneficiaries and partner organizations. For example, a beneficiary could receive a digital "Food Aid Recipient" credential that can be instantly verified by a distribution agent.

## Dependencies and Integration

The `g2p_openid_vci` module integrates closely with core OpenSPP components to perform its functions:

*   **[G2P Registry Base](g2p_registry_base)**: This module relies on the registrant data managed by the G2P Registry Base module. It retrieves crucial information about individuals and groups (e.g., names, IDs, addresses, program enrollments) to populate the content of verifiable credentials.
*   **[G2P Encryption](g2p_encryption)**: The `g2p_openid_vci` module utilizes the G2P Encryption module for all cryptographic operations. This includes securely signing Verifiable Credentials to ensure their tamper-evidence and authenticity, as well as managing JSON Web Key Sets (JWKS) for secure token validation.

This module acts as a foundational service, allowing other G2P modules to leverage its capabilities for issuing standardized digital proofs related to program enrollment, benefit distribution, and other social protection activities.

## Additional Functionality

### Issuer Management and Configuration

Administrators can define and manage multiple OpenID VCI issuers within OpenSPP, each with specific settings. This includes assigning a unique issuer ID, specifying the supported credential formats (e.g., LDP-VC), and defining the scope of credentials each issuer can provide. This flexibility allows OpenSPP to serve various credentialing needs across different programs or regions.

### Credential Definition and Issuance

The module facilitates the definition of various verifiable credential types through configurable templates. When a credential request is received, the system dynamically retrieves relevant beneficiary or program data from the registry, formats it according to the defined template, and generates a cryptographically signed digital credential. This ensures that the issued credentials are both accurate and secure.

### Secure Authorization and Access Control

To maintain the security of credential issuance, the module implements robust authorization rules. Administrators can configure which external applications or "audiences" are permitted to request credentials from specific OpenSPP issuers, and define trusted external issuers for authenticating incoming requests. This prevents unauthorized access and ensures that only legitimate parties can obtain credentials.

### Standardized Metadata and Discovery

The `g2p_openid_vci` module automatically generates and exposes standardized metadata for each configured issuer. This metadata allows external systems, such as digital wallets or partner applications, to easily discover the types of credentials OpenSPP can issue and understand how to interact with the platform for credential requests. It also manages JSON-LD contexts to ensure semantic interoperability of the credentials.

## Conclusion

The `g2p_openid_vci` module is crucial for OpenSPP, enabling it to securely issue verifiable digital credentials and fostering trust, efficiency, and interoperability across social protection programs.