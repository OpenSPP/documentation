---
myst:
  html_meta:
    "description": "API v2 error model and common HTTP responses"
    "property=og:title": "API v2 Errors"
    "keywords": "OpenSPP, API v2, errors, OperationOutcome"
---

# Errors and responses

API v2 uses standard HTTP status codes. Some endpoints return a structured error body similar to an `OperationOutcome`.

## Common status codes

- `400` Invalid request (for example malformed identifier format)
- `401` Missing/invalid/expired token
- `403` Access denied (missing scope, consent requirement, or enumeration protection)
- `404` Resource not found (only for non-consent-protected reads)
- `409` Version conflict (when `If-Match` is provided and does not match)
- `422` Validation errors (for example invalid field values during create/update)
- `429` Too many requests (rate limiting)

## OperationOutcome body

Batch operations and some validation errors return an `OperationOutcome`-style body:

```json
{
  "resourceType": "OperationOutcome",
  "issue": [
    {
      "severity": "error",
      "code": "invalid",
      "diagnostics": "Failed to create resource: <details>"
    }
  ]
}
```

## Consent and enumeration protection

If an API client is configured to require consent, `GET /Individual/{identifier}` and `GET /Group/{identifier}` may return `403 Access denied` both when:

- the record does not exist, or
- the record exists but there is no applicable consent

This is intended to reduce the risk of user enumeration through the API.

