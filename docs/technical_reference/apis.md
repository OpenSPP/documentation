---
myst:
  html_meta:
    "description": "OpenSPP API V2 technical reference"
    "property=og:title": "OpenSPP API V2"
    "keywords": "OpenSPP, API, REST, OAuth2, Odoo 19"
---

# API V2

OpenSPP V2 exposes an **official REST API** implemented by the Odoo module `spp_api_v2`.

The API is designed for interoperability and integrations:

- No internal database IDs in requests or responses
- OAuth 2.0 **client credentials** flow returning **JWT** access tokens
- Capability discovery via a `/metadata` endpoint

## Base URL

All endpoints are served under:

- `/api/v2/spp/`

## Authentication (OAuth 2.0 client credentials)

Request a token:

```bash
curl -X POST http://localhost:8069/api/v2/spp/oauth/token \
  -H "Content-Type: application/json" \
  -d '{
    "grant_type": "client_credentials",
    "client_id": "<client-id>",
    "client_secret": "<client-secret>"
  }'
```

Use the token:

```bash
curl http://localhost:8069/api/v2/spp/metadata \
  -H "Authorization: Bearer <access_token>"
```

### JWT signing secret

JWT tokens are signed using one of:

- Environment variable `OPENSPP_JWT_SECRET` (recommended for production)
- System parameter `spp_api_v2.jwt_secret` (auto-generated on install if missing)

## Core endpoints

This list reflects what is implemented in the `spp_api_v2` module:

- `POST /oauth/token` (get JWT access token; rate limited)
- `GET /metadata` (capability statement)
- `GET|POST|PUT /Individual` and `GET|PUT /Individual/{identifier}`
- `GET|POST|PUT /Group` and `GET|PUT /Group/{identifier}`
- `GET|POST|PUT /Program` and `GET|PUT /Program/{identifier}`
- `GET|POST|PUT /ProgramMembership` and `GET|PUT /ProgramMembership/{identifier}`
- `POST /$batch` (batch/transaction-style operations)

## Configuration in OpenSPP

After installing `spp_api_v2`, administrators manage API clients in the OpenSPP UI:

- **OpenSPP → Configuration → API V2 → API Clients**

API clients define `client_id`, `client_secret`, and scopes (for example `individual:read`, `group:search`).

## Rate limiting

The OAuth token endpoint is rate-limited (IP-based) to reduce brute force attacks.

Other endpoint rate limiting is implemented as middleware utilities, but may not be enforced on all endpoints by default (depending on which dependencies are enabled in routers).
