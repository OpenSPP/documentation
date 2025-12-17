---
myst:
  html_meta:
    "description": "OAuth 2.0 and OpenID Connect related technical reference for OpenSPP V2"
    "property=og:title": "OAuth 2.0 / OIDC"
    "keywords": "OpenSPP, OAuth2, OIDC, JWT, Odoo 19"
---

# OAuth 2.0 / OIDC

OpenSPP V2 uses OAuth-style concepts in multiple places.

## API V2 authentication (OAuth 2.0 client credentials)

The official OpenSPP REST API (see {doc}`apis`) implements an OAuth 2.0 **client credentials** flow:

- Token endpoint: `POST /api/v2/spp/oauth/token`
- Token type: JWT (Bearer)

JWT verification uses the shared secret configured via:

- `OPENSPP_JWT_SECRET` (environment variable; recommended for production), or
- `spp_api_v2.jwt_secret` (system parameter; generated on install if missing)

## Verifiable Credentials (OIDC4VCI)

OpenSPP also implements verifiable credential issuance flows based on OpenID specifications (OIDC4VCI / OIDC4VP).

Documentation for this area will live under Technical Reference once the V2 VC implementation is finalized.

