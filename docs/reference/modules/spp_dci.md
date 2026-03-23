---
openspp:
  doc_status: draft
---

# DCI Core

**Module:** `spp_dci`

## Overview

Core DCI (Digital Convergence Initiative) API components

## Purpose

This module is designed to:

- **Provide DCI-compliant data schemas:** Define Pydantic models for all Digital Convergence Initiative (DCI/SPDCI) message types including search, subscription, receipts, and notifications.
- **Manage cryptographic signing keys:** Generate, activate, and revoke Ed25519 and RSA-256 keypairs for DCI message authentication.
- **Support message signing and verification:** Implement HTTP Signature signing and verification following the draft-cavage specification.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `base` | Odoo core framework |
| `spp_registry` | Consolidated registry management for individuals, groups,... |

### External Dependencies

| Package | Purpose |
| --- | --- |
| `pydantic` | Schema validation for DCI message types |
| `cryptography` | Key generation, signing, and verification (Ed25519, RSA) |

## Key Features

### DCI Message Schemas

Pydantic schemas implementing the SPDCI API standard:

| Schema Group | Models | Description |
| --- | --- | --- |
| Envelope | `DCIEnvelope`, `DCIMessageHeader`, `DCICallbackHeader` | Three-part message structure (signature, header, message) |
| Person | `Person`, `Name`, `DisabilityInfo`, `RelatedPerson` | Individual person entity with identifiers and demographics |
| Group | `Group`, `Member` | Household/family unit with member list |
| Search | `SearchRequest`, `SearchResponse`, `SearchCriteria` | Registry search with pagination and expression queries |
| Subscription | `SubscribeRequest`, `SubscribeResponse`, `UnsubscribeRequest` | Event subscription management |
| Receipt | `ReceiptRequest`, `ReceiptResponse` | Delivery confirmation for async notifications |
| Common | `Identifier`, `Address`, `GeoCoordinates`, `Place` | Shared types across all message schemas |

### Constants and Enumerations

The module defines SPDCI-compliant enumerations:

| Enum | Values |
| --- | --- |
| `RegistryType` | Social Registry, CRVS, IBR, Disability Registry, Functional Registry |
| `QueryType` | idtype-value, expression, predicate, graphql |
| `RequestStatus` | rcvd, pdng, succ, rjct |
| `SexCategory` | male, female, other, unknown (ISO 5218) |
| `IdentifierType` | UIN, BRN, MRN, DRN |

### Signing Key Management

The `spp.dci.signing.key` model manages cryptographic keys with a lifecycle:

| State | Description |
| --- | --- |
| `draft` | Key record created, keypair not yet generated |
| `active` | Key is available for signing messages |
| `revoked` | Key is permanently disabled |

Key features:
- Supports Ed25519 and RSA-256 algorithms
- Generates PEM-encoded keypairs
- Produces JWKS entries for the `/.well-known/jwks.json` endpoint
- Private keys restricted to system admin group

### Message Signing

The `DCISigner` class creates HTTP Signatures per the draft-cavage specification:
- Computes SHA-256 digest of header and message
- Signs with Ed25519 private key
- Produces a signature string with created/expires timestamps (5-minute validity)

The `DCIVerifier` class validates signatures by parsing the header, checking expiration, recomputing the digest, and verifying the cryptographic signature.

### Response Helpers

Utility functions for building DCI server responses:
- `build_signed_envelope()` constructs and signs a complete DCI response envelope
- `build_error_search_response_item()` creates properly coded rejection responses
- `get_response_action()` maps request actions to SPDCI response actions

## Integration

- **spp_registry:** DCI schemas map to OpenSPP registry entities (individuals as Person, groups as Group with Member lists).
- **Downstream modules:** The schemas and signing infrastructure are consumed by `spp_dci_server` (API endpoints) and `spp_dci_client` (outbound DCI queries).

```{toctree}
:maxdepth: 1
:hidden:

spp_dci_client
spp_dci_client_crvs
spp_dci_client_dr
spp_dci_client_ibr
spp_dci_demo
spp_dci_server
```
