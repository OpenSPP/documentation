---
myst:
  html_meta:
    "description": "OpenSPP API v2 (REST) technical reference"
    "property=og:title": "OpenSPP API v2"
    "keywords": "OpenSPP, API v2, REST, OAuth2, JWT, Odoo 19"
---

# API v2 (REST)

API v2 is the official REST API implemented by the Odoo module `spp_api_v2`.

## Base URL and discovery

- Base URL: `/api/v2/spp`
- OpenAPI schema: `/api/v2/spp/openapi.json`
- Capability statement (public): `/api/v2/spp/metadata`

## Authentication and authorization

- Authentication: OAuth 2.0 **client credentials** (`POST /api/v2/spp/oauth/token`) returning a **JWT** access token.
- Authorization: API client **scopes** (for example `individual:read`, `group:search`, `program_membership:create`).

## Identifier format

Resources are addressed using external identifiers in the form:

- `{system}|{value}`

Where:
- `system` is a namespace URI (for example `urn:gov:xx:id:national-id`)
- `value` is the identifier value in that namespace

In URLs, the `{system}|{value}` segment should be URL-encoded (the `|` character in particular).

## Key behaviors

- No internal database IDs in requests or responses.
- Consent-aware responses (when the API client is configured to require consent).
- Optional optimistic locking via `ETag` / `If-Match` on update endpoints.
- Batch/transaction operations via `POST /api/v2/spp/$batch`.

```{toctree}
---
maxdepth: 2
---

authentication
clients_and_scopes
resources
search
batch
extensions
errors
consent_model
```

