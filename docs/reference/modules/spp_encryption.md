---
openspp:
  doc_status: draft
---

# Encryption: Base

**Module:** `spp_encryption`

## Overview

Implements advanced cryptographic services for OpenSPP, enabling data encryption, decryption, digital signing, and signature verification for sensitive program information. It securely manages cryptographic keys in JWK format and distributes public keys via JWKS, facilitating secure inter-system verification and data integrity.

## Purpose

This module is designed to:

- **Encrypt and decrypt data:** Provide JWE (JSON Web Encryption) services using RSA-OAEP with A256GCM for protecting sensitive program data.
- **Sign and verify tokens:** Create and verify JWT (JSON Web Tokens) using RS256 for secure inter-system authentication and data integrity.
- **Distribute public keys:** Expose public keys in JWKS (JSON Web Key Set) format for external systems to verify signatures.
- **Sign credentials with Linked Data Proofs:** Support JSON-LD credential signing with URDNA2015 normalization and multiple proof types (RSA, ECDSA, Ed25519), with a fallback for environments without remote context access.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `spp_security` | Central security definitions for OpenSPP modules |
| `spp_key_management` | Centralized cryptographic key management with pluggable p... |

### External Dependencies

| Package | Purpose |
| --- | --- |
| `jwcrypto>=1.5.6` | |

## Key Features

### Encryption Provider

The base model (`spp.encryption.provider`) defines a pluggable interface with type-dispatched methods:

| Method | Description |
| --- | --- |
| `encrypt_data()` | Encrypt raw bytes using JWE |
| `decrypt_data()` | Decrypt JWE-encrypted data |
| `jwt_sign()` | Sign data and return a JWT string |
| `jwt_verify()` | Verify a JWT signature and return validity |
| `get_jwks()` | Get public keys in JWKS format |
| `sign_credential_ld_proof()` | Sign a JSON-LD credential with Linked Data Proof |

### JWCrypto Implementation

The JWCrypto provider (`type = "jwcrypto"`) implements all operations using the `jwcrypto` Python library:

- **Key storage:** Links to `spp.asymmetric.key` records from `spp_key_management` for secure encrypted key storage
- **Key generation:** Supports RSA (2048/3072/4096-bit), EC (P-256, P-384, P-521, secp256k1), and Ed25519 key types via a UI action
- **Encryption:** Uses JWE with RSA-OAEP algorithm and A256GCM content encryption
- **Signing:** Uses JWT with RS256 algorithm

### Linked Data Proof Signing

For verifiable credential use cases, the module supports JSON-LD proof signing:

- Normalizes proof and credential documents using URDNA2015 algorithm
- Creates SHA-256 digests of normalized documents
- Signs the combined digest using JWT
- Includes bundled local copies of W3C security and credentials contexts to avoid network dependencies
- Configurable fallback to deterministic JSON serialization when JSON-LD normalization fails

## Integration

- **spp_key_management:** Delegates all key storage and retrieval to the centralized key management module, ensuring keys are stored encrypted.
- **spp_security:** Inherits security group definitions for access control to encryption operations.
