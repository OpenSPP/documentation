---
myst:
  html_meta:
    "description": "API v2 search: simple query parameters and advanced filters"
    "property=og:title": "API v2 Search"
    "keywords": "OpenSPP, API v2, search, filters, presets"
---

# Search and filters

API v2 provides:

- Simple searches using query parameters (`GET /{Resource}`)
- Advanced searches using filter expressions (`POST /{Resource}/_search`)

For discoverability, you can query available filters and presets:

- `GET /api/v2/spp/{Resource}/_filters`

Where `{Resource}` is one of `Individual`, `Group`, `Program`, `ProgramMembership`.

## Simple search (query parameters)

Example:

```bash
curl "http://localhost:8069/api/v2/spp/Individual?name=Santos&_count=20&_offset=0" \
  -H "Authorization: Bearer <access_token>"
```

Date parameters support prefixes:

- `ge2024-01-01` (>=)
- `le2024-12-31` (<=)
- `eq2024-06-01` (=)

## Filter metadata discovery

The filter metadata endpoint returns:

- Supported filter fields (and allowed operators)
- Whether custom filters are allowed
- Named presets (if configured)

Example:

```bash
curl "http://localhost:8069/api/v2/spp/Individual/_filters" \
  -H "Authorization: Bearer <access_token>"
```

## Advanced search (POST /_search)

Endpoint:

- `POST /api/v2/spp/{Resource}/_search`

Request body (example):

```json
{
  "filter_logic": "AND",
  "filters": [
    { "field": "name", "operator": "ilike", "value": "Santos" }
  ],
  "pagination": { "count": 20, "offset": 0 },
  "sort": [{ "field": "name", "direction": "asc" }]
}
```

Notes:
- Use `GET /{Resource}/_filters` to learn which filter names and operators are available in your deployment.
- Advanced search returns a `Bundle` (searchset) with pagination links.

