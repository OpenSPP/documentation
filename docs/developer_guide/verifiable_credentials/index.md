---
openspp:
  doc_status: draft
  products: [core]
---

# Verifiable Credentials

This guide is for **developers** implementing or extending OpenSPP's verifiable credentials functionality.

## What You'll Learn

OpenSPP V2 supports W3C Verifiable Credentials (VC) and OpenID for Verifiable Credential Issuance (OpenID4VCI), enabling secure, privacy-preserving digital identity and credential management. This allows beneficiaries to receive and present verifiable credentials from their digital wallets.

**Key capabilities:**
- Issue verifiable credentials for entitlements, program memberships, and identity
- Implement selective disclosure with SD-JWT for privacy protection
- Support wallet integration via OpenID4VCI protocol
- Manage credential lifecycle including revocation
- Verify credentials cryptographically without contacting the registry

## Documentation Structure

```{toctree}
:maxdepth: 2

overview
w3c_vc
oidc4vci
implementation
```

## Quick Links

### Getting Started

**New to Verifiable Credentials?**
Start with {doc}`overview` to understand the three-party model (issuer, holder, verifier) and why VCs matter for social protection programs.

**Ready to implement?**
Jump to {doc}`implementation` for step-by-step instructions on creating custom credential types and implementing issuance flows.

### Reference Documentation

**{doc}`overview`**
- What are verifiable credentials and why use them
- Three-party model (issuer, holder, verifier)
- Use cases: entitlements, program membership, identity
- Architecture overview and module structure
- Security model and trust mechanisms

**{doc}`w3c_vc`**
- W3C VC Data Model 2.0 implementation
- SD-JWT format for selective disclosure
- Credential types and configuration
- DID:web method for identifiers
- Revocation via Bitstring Status Lists
- Testing and validation

**{doc}`oidc4vci`**
- OpenID4VCI protocol flows
- Pre-authorized code and authorization code grants
- Issuer metadata discovery
- REST API endpoints implementation
- Security considerations (tokens, proof of possession, PIN protection)
- Testing credential issuance

**{doc}`implementation`**
- Development environment setup
- Creating custom credential types
- Implementing credential subject mixin
- Push and pull issuance models
- UI integration and portal access
- Testing strategies and performance optimization

## Standards Implemented

| Standard | Version | Purpose |
|----------|---------|---------|
| [W3C VC Data Model](https://www.w3.org/TR/vc-data-model-2.0/) | 2.0 | Core credential format |
| [SD-JWT VC](https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/) | Draft 13+ | Selective disclosure |
| [OpenID4VCI](https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html) | 1.0 | Credential issuance protocol |
| [OpenID4VP](https://openid.net/specs/openid-4-verifiable-presentations-1_0.html) | 1.0 | Credential presentation (partial) |
| [Bitstring Status List](https://www.w3.org/TR/vc-bitstring-status-list/) | 1.0 | Efficient revocation |
| [DID:web](https://w3c-ccg.github.io/did-method-web/) | 1.0 | Decentralized identifiers |

## Core Modules

| Module | Purpose |
|--------|---------|
| `spp_verifiable_credentials` | Core VC models, SD-JWT engine, status lists |
| `spp_openid_vci` | OpenID4VCI protocol base implementation |
| `spp_openid_vci_rest_api` | REST API endpoints for credential issuance |
| `spp_encryption` | Key management and cryptographic signing |
| `spp_api_v2_verifiable_credentials` | API v2 integration for VCs |

## Common Tasks

### Issue a Credential

```python
# Get credential type
credential_type = env['spp.credential.type'].search([
    ('code', '=', 'EntitlementCredential')
], limit=1)

# Get subject (e.g., entitlement)
entitlement = env['spp.entitlement'].browse(entitlement_id)

# Issue credential (returns SD-JWT string)
vc = entitlement.issue_credential(credential_type.id)
```

### Create a Credential Offer

```python
# Create offer for beneficiary wallet
offer_service = env['spp.credential.offer']
offer = offer_service.create({})
offer = offer.create_offer(
    credential_subject=entitlement,
    credential_type=credential_type,
    holder_wallet_did='did:web:wallet.example:holder123'
)

# Generate QR code URI
qr_uri = offer.get_credential_offer_uri()
```

### Verify a Credential

```python
# Parse and verify SD-JWT VC
sd_jwt_service = env['spp.sd.jwt']
result = sd_jwt_service.verify_sd_jwt_vc(
    sd_jwt=credential_string,
    expected_nonce=nonce,
    expected_audience='https://verifier.example'
)

if result['valid']:
    claims = result['verified_claims']
else:
    print(f"Verification failed: {result['error']}")
```

### Revoke a Credential

```python
# Find wallet credential
wallet_credential = env['spp.wallet.credential'].search([
    ('credential_subject_id', '=', entitlement.id),
    ('credential_subject_model', '=', 'spp.entitlement'),
])

# Revoke with reason
wallet_credential.action_revoke(reason="Entitlement cancelled")
```

## Are You Stuck?

**Not sure where to start?**

Read {doc}`overview` first to understand the concepts, then follow {doc}`implementation` for hands-on coding.

**Getting verification errors?**

Check {doc}`w3c_vc` for common issues with credential structure, signatures, and status lists.

**Wallet integration not working?**

See {doc}`oidc4vci` for OpenID4VCI protocol details and debugging steps.

**Need to create a custom credential type?**

Follow the step-by-step guide in {doc}`implementation` under "Creating Custom Credential Types."

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                  OpenSPP VC System                          │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌────────────────┐    ┌────────────────┐                  │
│  │  Credential    │    │    Wallet      │                  │
│  │  Issuance      │    │   Management   │                  │
│  │  (OpenID4VCI)  │    │   & Storage    │                  │
│  └───────┬────────┘    └───────┬────────┘                  │
│          │                     │                            │
│          └──────────┬──────────┘                            │
│                     ▼                                       │
│        ┌────────────────────────┐                           │
│        │spp_verifiable_         │                           │
│        │  credentials           │                           │
│        │                        │                           │
│        │ - SD-JWT Engine        │                           │
│        │ - Credential Types     │                           │
│        │ - Status Lists         │                           │
│        │ - DID Management       │                           │
│        └───────────┬────────────┘                           │
│                    │                                        │
│        ┌───────────┼────────────┐                           │
│        ▼           ▼            ▼                           │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐                    │
│  │ W3C VC   │ │Encryption│ │ Registry │                    │
│  │  Format  │ │& Signing │ │  Models  │                    │
│  └──────────┘ └──────────┘ └──────────┘                    │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## Implementation Status

| Component | Status | Notes |
|-----------|--------|-------|
| Core VC Module | ✅ Complete | Alpha stage |
| SD-JWT Engine | ✅ Complete | Issue, parse, present, verify |
| OpenID4VCI Issuance | ✅ Complete | Token + credential endpoints |
| Wallet Model | ✅ Complete | Storage and recovery |
| Status Lists | ✅ Complete | Bitstring revocation |
| OpenID4VP | ⚠️ Partial | Verification logic complete, endpoints pending |

## Related Documentation

- {doc}`/developer_guide/api_v2/overview` - API v2 for programmatic access
- {doc}`/developer_guide/extending/custom_modules` - Creating custom Odoo modules
- {doc}`/howto/developer_guides/development_setup` - Development setup

## External Resources

- [W3C Verifiable Credentials Data Model 2.0](https://www.w3.org/TR/vc-data-model-2.0/)
- [OpenID for Verifiable Credential Issuance](https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html)
- [SD-JWT Specification](https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/)
- [Bitstring Status List v1.0](https://www.w3.org/TR/vc-bitstring-status-list/)
- [EU Digital Identity Wallet ARF](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework)
