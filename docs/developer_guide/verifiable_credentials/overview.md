---
openspp:
  doc_status: draft
---

# Verifiable Credentials Overview

This guide is for **developers** implementing verifiable credentials in OpenSPP or integrating with OpenSPP's credential system.

## What Are Verifiable Credentials?

Verifiable Credentials (VCs) are a W3C standard for issuing digital credentials that can be cryptographically verified without contacting the issuer. Think of them as digital equivalents of physical credentials like driver's licenses, diplomas, or benefit cards—but with enhanced privacy and security.

### The Three-Party Model

```{mermaid}
graph LR
    A[Issuer<br/>OpenSPP Registry] -->|1. Issues VC| B[Holder<br/>Beneficiary Wallet]
    B -->|2. Presents VC| C[Verifier<br/>Service Provider]
    C -->|3. Verifies| A

    style A fill:#e1f5ff
    style B fill:#fff4e1
    style C fill:#f0f0f0
```

| Party | Role | Example in OpenSPP |
|-------|------|-------------------|
| **Issuer** | Creates and signs credentials | OpenSPP registry issuing entitlement credentials |
| **Holder** | Receives, stores, and presents credentials | Beneficiary with digital wallet on mobile device |
| **Verifier** | Checks credential validity | Bank verifying entitlement before cash disbursement |

### Key Properties

**Cryptographically Secure**
- Credentials are digitally signed by the issuer
- Tampering is immediately detectable
- No need to contact issuer during verification

**Privacy-Preserving**
- Holders control what information to disclose
- Selective disclosure reveals only necessary claims
- Unlinkable presentations prevent tracking

**Portable**
- Standards-based format works across systems
- Holder can move credentials between wallets
- Compatible with international identity frameworks

## Why Use Verifiable Credentials in OpenSPP?

### Beneficiary Empowerment

Traditional benefit systems require beneficiaries to repeatedly prove their status to different service providers, each time sharing sensitive information and waiting for verification. With VCs, beneficiaries hold cryptographically verifiable proof of their entitlements and can present them instantly.

**Example**: A beneficiary receives a cash transfer entitlement. Instead of carrying a paper voucher or waiting for the service provider to call the registry, they present a verifiable credential from their wallet. The provider verifies it instantly without accessing the registry database.

### Use Cases

#### 1. Entitlement Credentials

```json
{
  "type": ["VerifiableCredential", "EntitlementCredential"],
  "credentialSubject": {
    "entitlementId": "ENT-2024-001234",
    "programName": "Cash Transfer Program",
    "amount": {"value": 5000, "currency": "USD"},
    "validFrom": "2024-01-01",
    "validUntil": "2024-12-31"
  }
}
```

**Scenario**: Bank tellers verify entitlement credentials before disbursing cash, eliminating manual registry lookups and reducing wait times.

#### 2. Program Membership Credentials

```json
{
  "type": ["VerifiableCredential", "ProgramMembershipCredential"],
  "credentialSubject": {
    "programId": "urn:openspp:program:health-insurance-2024",
    "programName": "National Health Insurance",
    "enrollmentDate": "2024-01-15",
    "membershipStatus": "active"
  }
}
```

**Scenario**: Healthcare providers verify program membership at point of service without real-time connectivity to the registry.

#### 3. Identity Credentials

```json
{
  "type": ["VerifiableCredential", "RegistrantProfileCredential"],
  "credentialSubject": {
    "id": "did:web:registry.example:beneficiary:abc123",
    "givenName": "Jane",
    "familyName": "Doe",
    "birthDate": "1985-03-15"
  }
}
```

**Scenario**: Beneficiaries prove their identity when accessing services, with selective disclosure hiding sensitive fields like exact birthdate.

### Benefits

| Benefit | Description | Impact |
|---------|-------------|--------|
| **Offline Verification** | Credentials verifiable without internet | Service delivery in remote areas |
| **Privacy by Design** | Selective disclosure minimizes data exposure | GDPR compliance, reduced PII risk |
| **Fraud Reduction** | Cryptographic signatures prevent forgery | Fewer duplicate claims, less identity theft |
| **Interoperability** | Standards-based credentials work across systems | Cross-agency coordination, portability |
| **Reduced Load** | Fewer registry lookups during verification | Better performance, lower hosting costs |

## Architecture Overview

OpenSPP's VC implementation follows a modular architecture:

```
┌─────────────────────────────────────────────────────────────┐
│                     OpenSPP VC System                       │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────────┐    ┌──────────────────┐              │
│  │ Credential Types │    │  Wallet Storage  │              │
│  │  Configuration   │    │   & Recovery     │              │
│  └────────┬─────────┘    └────────┬─────────┘              │
│           │                       │                         │
│           └───────────┬───────────┘                         │
│                       ▼                                     │
│          ┌────────────────────────┐                         │
│          │   spp_verifiable_      │                         │
│          │     credentials        │                         │
│          │                        │                         │
│          │  - SD-JWT Engine       │                         │
│          │  - Status Lists        │                         │
│          │  - DID Management      │                         │
│          └───────────┬────────────┘                         │
│                      │                                      │
│          ┌───────────┼────────────┐                         │
│          ▼           ▼            ▼                         │
│   ┌──────────┐ ┌──────────┐ ┌──────────┐                   │
│   │OpenID4VCI│ │ W3C VC   │ │Encryption│                   │
│   │  Module  │ │  Format  │ │ & Signing│                   │
│   └──────────┘ └──────────┘ └──────────┘                   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Core Modules

| Module | Purpose |
|--------|---------|
| `spp_verifiable_credentials` | Core VC models, SD-JWT engine, status lists |
| `spp_openid_vci` | OpenID4VCI protocol implementation |
| `spp_openid_vci_rest_api` | REST API endpoints for credential issuance |
| `spp_encryption` | Key management and cryptographic signing |
| `spp_api_v2_verifiable_credentials` | API v2 integration for VCs |

## Standards Compliance

OpenSPP implements the following standards:

| Standard | Version | Purpose |
|----------|---------|---------|
| **W3C VC Data Model** | 2.0 | Core credential format and structure |
| **SD-JWT VC** | Draft 13+ | Selective disclosure mechanism |
| **OpenID4VCI** | 1.0 | Credential issuance protocol |
| **OpenID4VP** | 1.0 | Credential presentation protocol (partial) |
| **Bitstring Status List** | 1.0 | Efficient revocation checking |
| **DID:web** | 1.0 | Decentralized identifier method |

See {doc}`w3c_vc` for detailed information about W3C VC support.

## Security Model

### Cryptographic Foundations

**Signing Algorithm**: ES256 (ECDSA with P-256 and SHA-256)
- Industry standard for verifiable credentials
- Hardware security module (HSM) support
- Automatic key rotation with overlap periods

**Selective Disclosure**: SD-JWT with salted hashes
- Claims hashed individually with 128-bit random salts
- Holder chooses which claims to reveal
- Prevents correlation between presentations

**Holder Binding**: Key Binding JWT (KB-JWT)
- Proves holder possesses credential
- Contains nonce and audience to prevent replay
- Required for high-value credentials

### Trust Model

```{mermaid}
graph TD
    A[DID:web Issuer Identity] --> B[Public Key Resolution]
    B --> C[Signature Verification]
    C --> D[Status List Check]
    D --> E{Valid Credential}

    F[Credential Policies] --> E

    style E fill:#90EE90
    style A fill:#e1f5ff
```

**No Certificate Authorities Required**
- DID:web method uses HTTPS and DNS for trust
- Public keys published at well-known URLs
- No dependency on centralized PKI

**Revocation Without Tracking**
- Bitstring status lists enable privacy-preserving revocation
- Verifiers check bit positions in compressed lists
- No ability to track individual verification events

## Getting Started

### Prerequisites

Before implementing VCs in OpenSPP, you should understand:
- Python and Odoo development basics
- JWT (JSON Web Tokens) structure
- Public key cryptography concepts
- RESTful API design

### Next Steps

1. **Understand the Standards**: Read {doc}`w3c_vc` to learn the W3C VC data model
2. **Learn Issuance**: Review {doc}`oidc4vci` for OpenID4VCI protocol details
3. **Implement**: Follow {doc}`implementation` for step-by-step integration guide

## Are You Stuck?

**Don't understand the difference between VCs and traditional APIs?**

Traditional APIs require the verifier to contact the issuer every time:
```
Beneficiary → Service Provider → [Internet] → OpenSPP Registry
```

With VCs, the beneficiary presents a pre-signed credential:
```
Beneficiary → Service Provider
              (verifies locally)
```

This works offline and doesn't expose registry access to service providers.

**Confused about selective disclosure?**

Think of a driver's license at a bar. You need to prove you're over 21, but you don't need to show your exact birthdate or home address. Selective disclosure lets you prove "over 21" without revealing "born 1985-03-15".

With SD-JWT, claims like `birthDate`, `address`, and `nationalId` can be individually disclosed or hidden.

**Not sure when to use VCs vs. API tokens?**

Use **VCs** when:
- Beneficiaries present credentials to third parties
- Offline verification is required
- Privacy and selective disclosure are important
- Long-lived credentials (months to years)

Use **API tokens** when:
- System-to-system integration
- Real-time data synchronization
- Short-lived access (minutes to hours)
- No holder involvement

## See Also

- {doc}`w3c_vc` - W3C Verifiable Credentials Data Model
- {doc}`oidc4vci` - OpenID for Verifiable Credential Issuance
- {doc}`implementation` - Implementation Guide
- {doc}`/developer_guide/extending/custom_modules` - Creating Custom Modules
- {doc}`/developer_guide/api_v2/overview` - OpenSPP API v2
