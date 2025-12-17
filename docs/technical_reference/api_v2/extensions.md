---
myst:
  html_meta:
    "description": "API v2 extension fields and capability discovery"
    "property=og:title": "API v2 Extensions"
    "keywords": "OpenSPP, API v2, extensions, capability statement"
openspp:
  doc_status: unverified
---

# Extensions

API v2 supports optional module-specific fields through an **extension mechanism**.

## Discover extensions

The public capability statement lists active extensions:

- `GET /api/v2/spp/metadata`

## Request extensions in responses

Some resource endpoints accept a query parameter:

- `_extensions` = comma-separated list of extension names

Example:

```bash
curl "http://localhost:8069/api/v2/spp/Individual/urn%3Agov%3Axx%3Aid%3Anational-id%7C123?_extensions=farmer" \
  -H "Authorization: Bearer <access_token>"
```

Notes:
- Extensions requested must be registered and enabled in the server.
- Consent rules may restrict whether extensions are included (depending on your deployment’s consent configuration).

