---
openspp:
  doc_status: draft
---

# API: Oauth

**Module:** `spp_oauth`

## Overview

The module establishes an OAuth 2.0 authentication framework, securing OpenSPP API communication for integrated systems and applications.

## Purpose

This module is designed to:

- **Manage RSA key pairs:** Store OAuth 2.0 RSA public and private keys in Odoo system parameters, configurable through the Settings UI.
- **Sign JWT tokens:** Generate RS256-signed JSON Web Tokens using the configured private key for API authentication.
- **Verify JWT tokens:** Decode and validate incoming JWT access tokens using the configured public key.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `spp_security` | Central security definitions for OpenSPP modules |
| `base` | Odoo core framework |

### External Dependencies

| Package | Purpose |
| --- | --- |
| `pyjwt>=2.4.0` | JWT encoding, decoding, and verification |
| `cryptography` | RSA key handling for RS256 algorithm support |

## Key Features

### RSA Key Configuration

OAuth RSA keys are stored as Odoo system parameters and managed through Settings.

| Parameter | Description |
| --- | --- |
| `spp_oauth.oauth_priv_key` | RSA private key for signing JWT tokens |
| `spp_oauth.oauth_pub_key` | RSA public key for verifying JWT tokens |

Both keys are configurable via the `res.config.settings` form in the Odoo Settings UI.

### JWT Token Operations

The module provides utility functions for JWT token management:

| Function | Description |
| --- | --- |
| `calculate_signature` | Encodes a JWT with custom header and payload, signed with the RS256 algorithm |
| `verify_and_decode_signature` | Verifies a JWT access token against the public key and returns the decoded payload |

All JWT operations use the RS256 (RSA + SHA-256) algorithm. Key retrieval and token errors raise `OpenSPPOAuthJWTException` with automatic error logging.

## Integration

- **spp_api_v2:** Provides the JWT signing and verification infrastructure used by the OpenSPP API v2 token endpoint for OAuth 2.0 authentication.
- **spp_security:** Inherits central security definitions for access control over key management.
