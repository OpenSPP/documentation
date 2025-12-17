---
myst:
  html_meta:
    "description": "API v2 client configuration and scope model"
    "property=og:title": "API v2 Clients and Scopes"
    "keywords": "OpenSPP, API v2, scopes, OAuth client, access control"
---

# Clients and scopes

API v2 is accessed through **API clients** (not Odoo user logins). An administrator creates an API client, shares its credentials with an integrating system, and assigns scopes describing what the client is allowed to do.

## Create an API client in the UI

After installing `spp_api_v2`, the configuration menu is available under:

- **Registry → Configuration → API V2 → API Clients**

Each API client has:
- `client_id` (generated, read-only)
- `client_secret` (shown in the form; regenerate if you suspect it was exposed)
- Organization (`partner_id`)
- Consent settings (`require_consent`, `legal_basis`, optional legal reference)
- Scopes (`scope_ids`)

## Scopes

Scopes are defined as a pair:

- `resource` (for example `individual`, `group`, `program`, `program_membership`)
- `action` (for example `read`, `search`, `create`, `update`, `delete`, `all`)

The token endpoint returns a space-separated `scope` string built from the client’s configured scopes (for example `individual:read group:search`).

## Consent-related settings

API v2 can require explicit consent for data access.

- When `require_consent` is enabled, read endpoints apply consent filtering and may return access-denied responses for consent-protected resources.
- When `legal_basis` is set to a basis which does not require consent (for example “public interest”), the server applies client scope restrictions but does not require an individual consent record for access.

For how this impacts responses, see {doc}`Consent behavior <consent_model>`.

## Rate limiting

The OAuth token endpoint is rate-limited (IP-based).

The module also includes a general rate-limit dependency (token-hash/IP based) which can be enabled on endpoints, but is not necessarily applied to all routers by default.

