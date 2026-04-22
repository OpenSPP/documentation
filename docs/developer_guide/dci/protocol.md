---
openspp:
  doc_status: draft
  products: [core]
---

# DCI Protocol Details

**For: developers**

The wire-level details of the DCI protocol as implemented in OpenSPP — message envelope, HTTP Signature format, endpoint paths, query types, and data schemas.

## Prerequisites

- Familiarity with OAuth 2.0 and Bearer token authentication
- Basic understanding of HTTP Message Signatures (draft-cavage / RFC 9421)
- Familiarity with Pydantic-style JSON schemas

## Message envelope

Every DCI message uses a three-part envelope — a signature header string, a message header object, and a message body object. The schema is defined in `spp_dci/schemas/envelope.py`.

```json
{
  "signature": "namespace=\"dci\", kidId=\"openspp|key1|ed25519\", algorithm=\"ed25519\", created=\"1705315800\", expires=\"1705316100\", headers=\"(created) (expires) digest\", signature=\"<base64>\"",
  "header": {
    "version": "1.0.0",
    "message_id": "uuid",
    "message_ts": "2026-04-22T10:30:00Z",
    "action": "search",
    "sender_id": "external.mis.gov",
    "sender_uri": "https://external.mis.gov/dci/callback",
    "receiver_id": "openspp",
    "total_count": 1,
    "is_msg_encrypted": false
  },
  "message": {
    "transaction_id": "uuid",
    "search_request": [...]
  }
}
```

### Header fields

| Field | Type | Notes |
|-------|------|-------|
| `version` | string | DCI version, default `"1.0.0"` |
| `message_id` | string | UUID for this message |
| `message_ts` | datetime | ISO-8601 timestamp |
| `action` | string | `search`, `subscribe`, `notify`, `unsubscribe` |
| `sender_id` | string | Sender's DCI identifier |
| `sender_uri` | string or null | Callback URL — required for async operations |
| `receiver_id` | string | Receiver's DCI identifier |
| `total_count` | integer | Number of items in the message body (default 0) |
| `is_msg_encrypted` | bool | Envelope-level encryption flag (default false) |

Callback responses additionally include `status` (`rcvd`, `pdng`, `succ`, `rjct`), `status_reason_code`, `status_reason_message`, and `completed_count`. See the `DCICallbackHeader` model.

## HTTP Signature

The `signature` field is a key=value parameter string following the draft-cavage HTTP Message Signatures style. OpenSPP's implementation is in `spp_dci/services/signing.py`.

### Signature format

```
namespace="dci",
kidId="{sender_id}|{key_id}|{algorithm}",
algorithm="{algorithm}",
created="{unix_ts}",
expires="{unix_ts + 300}",
headers="(created) (expires) digest",
signature="{base64_signature}"
```

- **`namespace`** is always `"dci"`
- **`kidId`** encodes the sender, key identifier, and algorithm, separated by `|`
- **`algorithm`** is `ed25519` (recommended) or `rs256`
- **`expires`** is `created + 300` — the signature is valid for 5 minutes
- **`headers`** lists which virtual headers are signed, always `(created) (expires) digest` in the current implementation
- **`signature`** is the base64-encoded cryptographic signature

Note: the `signature` field in the envelope stores the raw parameter string starting with `namespace="dci", ...`. There is no `Signature: ` HTTP-header prefix — that prefix only applies if you transmit the signature as an HTTP header rather than inside the envelope.

### Signing string

The receiver verifies the signature against a signing string built from three lines:

```
(created): 1705315800
(expires): 1705316100
digest: aGVsbG8gd29ybGQ=
```

- Each line is `{label}: {value}` with a literal space after the colon
- Lines are joined by `\n`
- The `digest` value is a base64-encoded SHA-256 of the canonical JSON serialization of `{header, message}`

### Digest computation

The digest is computed over the canonical JSON of an object containing the header and message (not the envelope as a whole — the signature is computed before it's added):

```python
content = {"header": header, "message": message}
canonical_json = json.dumps(content, sort_keys=True, separators=(",", ":"))
digest = base64.b64encode(hashlib.sha256(canonical_json.encode()).digest()).decode()
```

Both `sort_keys=True` and the compact `separators=(",", ":")` are essential — any whitespace difference between sender and receiver produces different digests and verification fails.

### Clock skew

The server allows up to 60 seconds of clock skew between `created`/`expires` and its own clock. Systems with drift beyond that will see `err.signature.expired` or `err.signature.not_yet_valid` style failures.

## Authentication

The DCI server requires **two parallel authentication mechanisms** on every protected request:

### 1. Bearer token (allowlist)

```
Authorization: Bearer <token>
```

The token is validated against the `dci.api_tokens` Odoo system parameter — a comma-separated list of accepted tokens. This is a pre-shared-secret scheme, not OAuth 2.0. The DCI server does not issue tokens dynamically; administrators rotate tokens by editing the system parameter.

Two development-mode bypass flags exist:

| System parameter | Default | Effect |
|------------------|---------|--------|
| `dci.bypass_bearer_auth` | `false` | If `true`, skips bearer validation entirely |
| `dci.allow_unsigned_requests` | `false` | If `true`, accepts requests with no valid DCI signature |

Both must be `false` in production.

### 2. HTTP Signature (sender identity + message integrity)

Beyond bearer validation, every request body must contain a valid DCI envelope whose `signature` can be verified against the sender's registered public key. The server:

1. Parses the envelope and extracts `sender_id` from the header
2. Looks up that sender in `spp.dci.sender.registry`
3. Uses the registered `public_key` (or fetches the sender's JWKS via `jwks_url`)
4. Verifies the signature against the signing string built from `(created)`, `(expires)`, and the computed digest

A request that passes bearer validation but fails signature verification returns `401 Unauthorized` with a status reason code like `err.signature.invalid` or `err.signature.expired`.

## Base URL and endpoint paths

The DCI server mounts under FastAPI root path `/dci_api/v1` (configured in `spp_dci_server/data/fastapi_endpoint_data.xml`). Full URLs have the form:

```
https://<host>/dci_api/v1/<path>
```

### Endpoints

| Method | Path | Purpose |
|--------|------|---------|
| POST | `/dci_api/v1/registry/sync/search` | Synchronous search — returns results immediately |
| POST | `/dci_api/v1/registry/search` | Asynchronous search — returns `202 Accepted` with a correlation ID; results delivered via callback |
| POST | `/dci_api/v1/registry/subscribe` | Subscribe to registry events |
| POST | `/dci_api/v1/registry/unsubscribe` | Cancel subscriptions by code |
| POST | `/dci_api/v1/registry/sync/txn/status` | Poll transaction status for an async operation |
| POST | `/dci_api/v1/receipt` | Send a receipt for a prior operation (e.g., after processing a notification) |
| GET  | `/dci_api/v1/.well-known/jwks.json` | Public signing keys (no auth) |

All `POST` endpoints require Bearer + HTTP Signature auth. The `GET` JWKS endpoint is public.

## Query types

Search requests carry a `search_criteria.query_type` that selects how the `query` payload is interpreted. The schema is defined in `spp_dci/schemas/search.py` and the enum values are in `spp_dci/schemas/constants.py`.

### `idtype-value`

Simple identifier lookup:

```json
{
  "query_type": "idtype-value",
  "query": {
    "type": "UIN",
    "value": "12345678"
  }
}
```

Valid identifier types are defined by `IdentifierType` enum: `UIN`, `BRN`, `MRN`, `DRN`. Deployments may use their own values if both sides agree.

### `expression`

Conditional query with AND/OR composition:

```json
{
  "query_type": "expression",
  "query": {
    "seq": [
      {"attribute": "birth_date", "operator": ">=", "value": "1990-01-01"},
      {"attribute": "sex", "operator": "=", "value": "female"}
    ]
  }
}
```

- `seq` — list of conditions combined with AND
- `or_` — list of expressions combined with OR
- Conditions can nest (an `or_` inside a `seq`, etc.)

Supported operators: `=`, `>`, `<`, `>=`, `<=`, `in`, `contains`.

### `predicate`

CEL-style predicate expression:

```json
{
  "query_type": "predicate",
  "query": "person.age >= 18 && person.has_disability == true"
}
```

## Registry type values

The `reg_type` field in search/subscribe criteria uses namespaced URIs, defined in `spp_dci/schemas/constants.py::RegistryType`:

| Enum name | Wire value |
|-----------|------------|
| `SOCIAL_REGISTRY` | `ns:org:RegistryType:Social` |
| `CRVS` | `ns:org:RegistryType:Civil` |
| `IBR` | `ns:org:RegistryType:IBR` |
| `DISABILITY_REGISTRY` | `ns:org:RegistryType:DR` |
| `FUNCTIONAL_REGISTRY` | `ns:org:RegistryType:FR` |

When building requests, use the `.value` of the enum (the namespaced URI), not the enum name.

## Event type values

`reg_event_type` is defined by `RegistryEventType`:

`REGISTRATION`, `UPDATE`, `DELETE`, `BIRTH`, `DEATH`, `MARRIAGE`, `DIVORCE`, `ENROLLMENT`, `DISENROLLMENT`, `BENEFIT_DISBURSEMENT`.

## Status values

Responses carry a `status` field in the envelope header (for callbacks) or in each search response item. Values are in `RequestStatus`:

| Value | Meaning |
|-------|---------|
| `rcvd` | Request received and accepted for processing |
| `pdng` | Processing in progress |
| `succ` | Completed successfully |
| `rjct` | Rejected — see status reason |

## Status reason codes

When a request or item is rejected, the response includes a dotted-lowercase reason code. These come from enums in `spp_dci/schemas/constants.py`.

### Message-level errors (`err.*`)

Typically issued by auth middleware before the router runs:

| Code | Meaning |
|------|---------|
| `err.auth.missing_header` | Authorization header absent |
| `err.auth.invalid_format` | Authorization header not `Bearer <token>` |
| `err.signature.missing` | Envelope has no signature |
| `err.signature.invalid` | Signature verification failed |
| `err.signature.expired` | Signature `expires` timestamp in the past |

### Search-level errors (`rjct.*`)

Issued by the search service when it rejects a request:

| Code | Meaning |
|------|---------|
| `rjct.reference_id.invalid` | Reference ID malformed or missing |
| `rjct.search_criteria.invalid` | Criteria failed validation |
| `rjct.filter.invalid` | Filter predicate malformed |
| `rjct.sort.invalid` | Sort spec malformed |
| `rjct.pagination.invalid` | Pagination fields out of range |
| `rjct.timestamp.invalid` | `message_ts` missing or malformed |
| `rjct.search.too_many_records_found` | Too many matches — narrow the query |
| `rjct.message_id.duplicate` | Message ID replayed |
| `rjct.action.not_supported` | Unknown or unsupported `action` value |
| `rjct.total_count.limit_exceeded` | More than the allowed number of items in the envelope |

Similar `rjct.*` enums exist for `SubscribeStatusReasonCode` and `UnsubscribeStatusReasonCode`.

## Data schemas

### Person

The `Person` schema (`spp_dci/schemas/person.py`) carries identity, demographic, contact, and (optionally) disability fields:

| Field | Type | Notes |
|-------|------|-------|
| `identifier` | list of `Identifier` | One or more external IDs |
| `name` | `Name` | Given, surname, second, maiden, prefix, suffix |
| `sex` | `SexCategory` | `male`, `female`, `other`, `unknown` |
| `birth_date` | date | |
| `death_date` | date | |
| `address` | list of `Address` | |
| `phone_number` | list of string | |
| `email` | list of string | |
| `registration_date` | datetime | |
| `last_updated` | datetime | |

Identifier has `identifier_type` (e.g., `UIN`) and `identifier_value`.

### Group

`Group` schema (`spp_dci/schemas/group.py`):

| Field | Type | Notes |
|-------|------|-------|
| `group_identifier` | list of `Identifier` | |
| `group_type` | `AssistanceUnitEnum` | `member`, `household`, `family` |
| `address` | list of `Address` | |
| `poverty_score` | float | |
| `group_head_info` | `Member` | |
| `group_size` | int | |
| `member_list` | list of `Member` | |
| `additional_attributes` | list of `AdditionalAttribute` | Key-value extensions |
| `registration_date` | datetime | |
| `last_updated` | datetime | |

### Disability info

Disability data (`DisabilityInfo`) uses the Washington Group short-set model:

- `disability_limitation_type` — `VISION`, `HEARING`, `MOBILITY`, `COGNITION`, `SELF_CARE`, `COMMUNICATION`
- `functional_severity` — integer 1-4 where 1=no difficulty, 4=cannot do at all

### Common types

| Type | Fields |
|------|--------|
| `Name` | `surname`, `given_name`, `second_name`, `maiden_name`, `prefix`, `suffix` |
| `Address` | `address_line_1`, `address_line_2`, `locality`, `sub_region_code`, `region_code`, `postal_code`, `country_code`, `geo_location` |
| `Identifier` | `identifier_type`, `identifier_value` |
| `Period` | `start`, `end` |

## Field mappings (DCI ↔ res.partner)

When mapping DCI `Person` objects to/from OpenSPP's `res.partner`:

| DCI field | res.partner field | Notes |
|-----------|-------------------|-------|
| `identifier[].identifier_type` | `reg_ids.id_type_id` | Lookup via `spp.id.type` |
| `identifier[].identifier_value` | `reg_ids.value` | Direct mapping |
| `name.given_name` | `given_name` | Direct |
| `name.surname` | `family_name` | Direct |
| `name.prefix`, `name.suffix` | *(not mapped)* | `res.partner` has no prefix/suffix fields; store in `addl_name` or extend the model if needed |
| `sex` | `gender_id.code` | Vocabulary lookup |
| `birth_date` | `birthdate` | Direct |
| `address[]` | partner address fields | Pick primary; see `spp_registry` models |
| `phone_number[]` | `phone_number_ids` | One-to-many |
| `email[]` | `email` | First email only |

The `reg_ids` field is a One2many from `res.partner` to `spp.registry.id` (`spp_registry/models/registrant.py`).

## JWKS endpoint

`GET /dci_api/v1/.well-known/jwks.json` publishes the public keys of every active `spp.dci.signing.key` record. Example response:

```json
{
  "keys": [
    {
      "kty": "OKP",
      "kid": "openspp|key1|ed25519",
      "use": "sig",
      "alg": "EdDSA",
      "crv": "Ed25519",
      "x": "<base64url>"
    }
  ]
}
```

The `kid` format is `{sender_id}|{key_id}|{algorithm}`. External registries that verify OpenSPP's signatures fetch this endpoint to discover the current set of keys.

## Common mistakes

**Wrong digest format.** The signing string uses `digest: <base64>` — no `SHA-256=` prefix, no other algorithm labels. Getting this wrong silently breaks verification.

**Whitespace in JSON before hashing.** The digest must be computed over `json.dumps(..., sort_keys=True, separators=(",", ":"))`. Any pretty-printing or default whitespace changes the bytes and breaks the digest match.

**Signature expires in 5 minutes.** Don't cache signed envelopes; sign fresh on every request. If your client builds and serializes slowly, your requests can age out before they land.

**Bearer token and HTTP Signature are both required.** Passing the bearer token alone returns 401. Both mechanisms must succeed.

**Using the wrong registry type string.** Use `"ns:org:RegistryType:Social"` on the wire, not `"SOCIAL_REGISTRY"`. The enum name differs from the value.

**Confusing `err.*` and `rjct.*` codes.** `err.*` codes come from the auth middleware (before the router executes). `rjct.*` codes come from the search/subscribe business logic. The two namespaces don't overlap.

**Not swapping `sender_id` and `receiver_id` on responses.** A response's `sender_id` is the server's ID; `receiver_id` is the original caller. Copying the request header verbatim is wrong.

**Missing `message_id` uniqueness.** Every message needs a fresh UUID for `message_id`. Replaying an ID triggers `rjct.message_id.duplicate`.

## See also

- {doc}`overview` — DCI architecture and interaction patterns
- {doc}`server_role` — exposing OpenSPP as a DCI server
- {doc}`client_role` — querying external DCI registries from OpenSPP
- [DCI API Standards](https://github.com/spdci/api-standards) — upstream DCI specifications
- [HTTP Message Signatures](https://www.rfc-editor.org/rfc/rfc9421.html) — RFC 9421
