---
myst:
  html_meta:
    "description": "How consent affects API v2 responses"
    "property=og:title": "API v2 Consent Model"
    "keywords": "OpenSPP, API v2, consent, privacy, data access"
---

# Consent model (response filtering)

API v2 is designed to support consent-aware access to social registry and program data.

## Where consent is managed

Consent records are managed in the OpenSPP UI (not via API endpoints by default).

In a standard configuration, consent management is available under:

- **Registry → Configuration → Consent Management**

## How consent affects API responses

When an API client has `require_consent` enabled:

- Single-resource reads (`GET /Individual/{identifier}`, `GET /Group/{identifier}`) apply consent filtering and may return `403 Access denied` when consent is missing or does not cover the requested data.
- Search endpoints return results, but each resource is filtered (often down to identifier-only) when consent is missing.

When an API client has a legal basis that does not require consent (for example “public interest”), the server may allow access without an individual consent record, but still applies scope restrictions.

## Consent status header

For some read endpoints, the server may include:

- `X-Consent-Status: ...`

This header is informational and reflects the consent outcome for that response.

