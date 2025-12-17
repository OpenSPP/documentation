---
myst:
  html_meta:
    "description": "API v2 authentication (OAuth2 client credentials) and JWT details"
    "property=og:title": "API v2 Authentication"
    "keywords": "OpenSPP, API v2, OAuth2, JWT, client credentials"
openspp:
  doc_status: unverified
---

# Authentication

API v2 uses OAuth 2.0 **client credentials**. Tokens are **JWT** signed with `HS256`.

## Get an access token

Endpoint:

- `POST /api/v2/spp/oauth/token`

Request body (JSON):

```json
{
  "grant_type": "client_credentials",
  "client_id": "<client-id>",
  "client_secret": "<client-secret>"
}
```

Response (JSON):

```json
{
  "access_token": "<jwt>",
  "token_type": "Bearer",
  "expires_in": 3600,
  "scope": "individual:read group:search"
}
```

Notes:
- The token lifetime is currently **1 hour** (`expires_in: 3600`).
- The token endpoint is rate-limited (IP-based) to reduce brute-force attempts.

## Use the token

Send the token on requests:

```http
Authorization: Bearer <access_token>
```

## JWT signing secret

The server loads the JWT secret from:

1. Environment variable `OPENSPP_JWT_SECRET` (recommended in production)
2. System parameter `spp_api_v2.jwt_secret`

The secret is validated at runtime (minimum length and entropy). If it is missing or too weak, API requests will fail with a server configuration error.

