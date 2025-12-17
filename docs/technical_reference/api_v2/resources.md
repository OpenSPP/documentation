---
myst:
  html_meta:
    "description": "API v2 resources and endpoint summary"
    "property=og:title": "API v2 Resources"
    "keywords": "OpenSPP, API v2, Individual, Group, Program, ProgramMembership"
openspp:
  doc_status: unverified
---

# Resources

All endpoints are under the `/api/v2/spp` base URL.

## Identifier path parameters

Most read/update endpoints use an `{identifier}` path parameter in the form:

- `{system}|{value}`

`system` is a namespace URI (for example `urn:gov:xx:id:national-id`). Because `system` is part of the URL path, it should be URL-encoded.

## Individual

Endpoints:

- `GET /api/v2/spp/Individual/{identifier}`
- `GET /api/v2/spp/Individual` (search)
- `POST /api/v2/spp/Individual` (create)
- `PUT /api/v2/spp/Individual/{identifier}` (update)

Search parameters (`GET /Individual`):

- `identifier` = `system|value`
- `name` (substring match)
- `birthdate` (with optional prefixes `ge`, `le`, `gt`, `lt`, `eq`, `ne`)
- `gender` = `system|code` (vocabulary code)
- `address` (substring search across address fields)
- `_lastUpdated` (with optional date prefixes)
- `_count` (1–100), `_offset` (>=0), `_sort` (field, prefix `-` for desc)

Headers:

- Single reads may return `ETag: "<versionId>"`
- Single reads may return `X-Consent-Status: active|...` (depending on consent outcome)
- Updates accept `If-Match: "<versionId>"` (optional optimistic locking)

## Group

Endpoints:

- `GET /api/v2/spp/Group/{identifier}`
- `GET /api/v2/spp/Group` (search)
- `POST /api/v2/spp/Group` (create)
- `PUT /api/v2/spp/Group/{identifier}` (update)

Search parameters (`GET /Group`):

- `identifier` = `system|value`
- `name`
- `type`
- `member` = `Individual/{system}|{value}`
- `_count`, `_offset`

## Program

Endpoints:

- `GET /api/v2/spp/Program/{identifier}`
- `GET /api/v2/spp/Program` (search)

Notes:
- Programs are created/managed in the UI; API v2 currently treats them as read-only.
- Program identifiers are currently derived from program name (slug format) unless additional identifier storage is configured in the deployment.

Search parameters (`GET /Program`):

- `name`
- `status` (`active` or `ended`)
- `targetType` (`individual` or `group`)
- `_count`, `_offset`

## ProgramMembership

Endpoints:

- `GET /api/v2/spp/ProgramMembership/{identifier}`
- `GET /api/v2/spp/ProgramMembership` (search)
- `POST /api/v2/spp/ProgramMembership` (create)
- `PUT /api/v2/spp/ProgramMembership/{identifier}` (update)

Search parameters (`GET /ProgramMembership`):

- `beneficiary` = `Individual/{system}|{value}` or `Group/{system}|{value}`
- `program` = `Program/{system}|{value}`
- `status`
- `_count`, `_offset`

Consent notes:
- ProgramMembership responses are consent-filtered based on the beneficiary.

