# g2p_openid_vci Module

## Overview

The `g2p_openid_vci` module extends OpenSPP's capabilities to manage and issue Verifiable Credentials (VCs) based on OpenID Connect for Verifiable Presentations (OpenID4VP) and Decentralized Identifiers (DIDs). This module enables the system to act as an issuer of VCs, empowering individuals with digital credentials that represent claims about their identity or attributes.

## Purpose

- **Issue Verifiable Credentials:** Provide a mechanism to generate and issue VCs conforming to W3C standards like Verifiable Credentials Data Model and DID specification.
- **Manage Issuers:**  Define and manage multiple VCI issuers with distinct configurations for supported credential types, formats, and security settings.
- **Integration with OpenID Connect:** Leverage OpenID Connect flows for authorization and authentication, ensuring only authorized entities can request and receive VCs.
- **Encryption and Signing:** Utilize the [g2p_encryption](g2p_encryption) module to digitally sign issued credentials, guaranteeing their authenticity and integrity.

## Role and Integration

This module builds upon the foundation laid by [g2p_registry_base](g2p_registry_base) and [g2p_encryption](g2p_encryption) modules:

- **[g2p_registry_base](g2p_registry_base):** The module depends on registrant data managed by [g2p_registry_base](g2p_registry_base). It fetches information like name, address, and registered IDs from this module to populate VC claims.
- **[g2p_encryption](g2p_encryption):**  The module integrates with [g2p_encryption](g2p_encryption) to securely sign issued VCs using configured encryption providers. This ensures the trustworthiness and tamper-proof nature of issued credentials.

## Functionality

1. **VCI Issuer Management:** 
   - Define multiple VCI issuers, each representing a distinct entity capable of issuing VCs.
   - Configure issuer details: 
     - **Name and Type:** Descriptive name and the type of VCs issued (e.g., OpenG2PRegistryVerifiableCredential).
     - **Scope and Format:** Define the intended purpose (scope) of issued VCs and the supported VC format (e.g., `ldp_vc`).
     - **Unique Issuer ID (DID):**  Specify the DID representing the issuer.
     - **Encryption Provider:** Select the encryption provider from [g2p_encryption](g2p_encryption) for signing credentials.
   - **Authentication Settings:**  Configure OpenID Connect-based authentication:
     - Specify allowed OpenID issuers, audience values, client IDs, and JSON Web Key Set (JWKS) endpoints for verifying authentication tokens.
   - **Credential Format and Metadata:**  Define the structure and content of issued VCs using JSON and JQ (JSON Query) for dynamic data population.

2. **VC Issuance:**
   - The module handles incoming credential requests conforming to the OpenID4VP specification.
   - It validates requests against configured issuers, scopes, and authentication settings.
   - Upon successful validation, it fetches relevant registrant data from [g2p_registry_base](g2p_registry_base), populates the VC claims, and digitally signs the credential using the selected encryption provider.
   - Finally, it returns the issued VC in the requested format.

## Example Usage

1. **Configure a VCI Issuer:** An administrator defines a new issuer representing a government agency issuing proof of address VCs. They configure the issuer details, OpenID Connect authentication settings, and define the VC format using a JSON template.
2. **Credential Request:** A relying party application (e.g., a bank) initiates a VC request, authenticating through an OpenID Connect provider approved by the issuer.
3. **VC Issuance and Verification:** The `g2p_openid_vci` module validates the request, fetches the user's address information from [g2p_registry_base](g2p_registry_base), populates the VC, signs it, and sends it back to the relying party. The relying party can then verify the VC's signature and authenticity.

## Conclusion

The `g2p_openid_vci` module empowers OpenSPP to participate in a decentralized identity ecosystem. By issuing verifiable credentials, OpenSPP enhances trust and streamlines data sharing within its network and with external entities.
