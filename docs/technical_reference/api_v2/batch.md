---
myst:
  html_meta:
    "description": "API v2 batch and transaction bundle processing"
    "property=og:title": "API v2 Batch"
    "keywords": "OpenSPP, API v2, batch, transaction, bundle"
---

# Batch and transactions

API v2 supports bundling multiple operations into a single request:

- `POST /api/v2/spp/$batch`

## Bundle types

- `transaction`: all-or-nothing (rollback if any entry fails)
- `batch`: independent operations (partial success allowed)

## Placeholders (urn:uuid:...)

Bundle entries can define `fullUrl` placeholders like `urn:uuid:individual-1`, and later entries can reference them. After creation, placeholders are resolved to actual resource identifiers.

## Supported operations

Bundle entries support standard operations such as:

- `POST {ResourceType}`
- `PUT {ResourceType}/{system}|{value}`
- `GET {ResourceType}/{system}|{value}`

For the full request/response schema, see the OpenAPI schema at `/api/v2/spp/openapi.json`.

