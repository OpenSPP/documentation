---
openspp:
  doc_status: draft
  products: [core]
---

# Verifiable Credentials

OpenSPP supports the issuance of [Verifiable Credentials (VCs)](https://www.w3.org/TR/vc-data-model/) through the OpenID for Verifiable Credential Issuance (OpenID4VCI) standard. This enables registrants to receive cryptographically signed digital credentials that can be verified independently without contacting OpenSPP directly.

## Overview

Verifiable Credentials in OpenSPP allow:

- **Individuals** to receive digital proof of their registration status, identity attributes, and program enrollment
- **Groups** (households, families) to receive credentials representing group identity and membership
- **Program beneficiaries** to receive credentials proving their enrollment and entitlement status

These credentials follow the W3C Verifiable Credentials Data Model and are issued through a standards-compliant OpenID4VCI flow, making them interoperable with any system that supports the same standards.

## Architecture

The VC issuance system in OpenSPP consists of several layers:

1. **Base VCI layer** (`g2p_openid_vci`) -- Provides the OpenID4VCI endpoint infrastructure, credential signing, and key management
2. **OpenSPP VCI layer** (`spp_openid_vci`) -- Extends the base layer with OpenSPP-specific credential types and registrant data mapping
3. **Individual credentials** (`spp_openid_vci_individual`) -- Issues VCs for individual registrants with personal identity attributes
4. **Group credentials** (`spp_openid_vci_group`) -- Issues VCs for groups representing household or family identity
5. **Program beneficiary credentials** (`g2p_openid_vci_programs`) -- Issues VCs for program enrollment and beneficiary status

## Credential Issuance Flow

1. A registrant (or authorized system) initiates a credential request through the OpenID4VCI protocol
2. OpenSPP authenticates the request and verifies the registrant's identity
3. The appropriate credential type is selected based on the request (individual, group, or program)
4. OpenSPP assembles the credential with the relevant attributes from the registry
5. The credential is cryptographically signed and returned to the requester
6. The issued credential can be independently verified by any relying party using OpenSPP's public key

## Integration Points

### For credential verifiers

Systems that need to verify credentials issued by OpenSPP can:

- Retrieve OpenSPP's public keys through the standard OpenID discovery endpoint
- Verify the cryptographic signature on any credential without contacting OpenSPP
- Check credential revocation status through the published revocation list

### For credential wallets

Digital wallet applications can:

- Use the OpenID4VCI protocol to request and receive credentials from OpenSPP
- Store credentials locally for offline presentation
- Present credentials to relying parties using standard presentation protocols

## Related Module Documentation

For detailed technical documentation of each module:

- [G2P OpenID VCI: Base](../modules/g2p_openid_vci) -- Core VCI infrastructure
- [OpenSPP OpenID VCI](../modules/spp_openid_vci) -- OpenSPP-specific VCI extensions
- [OpenSPP OpenID VCI Individual](../modules/spp_openid_vci_individual) -- Individual credential issuance
- [OpenSPP OpenID VCI Group](../modules/spp_openid_vci_group) -- Group credential issuance
- [G2P OpenID VCI: Program Beneficiaries](../modules/g2p_openid_vci_programs) -- Program beneficiary credentials
