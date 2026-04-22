---
openspp:
  doc_status: draft
  products: [core]
---

# OpenSPP as DCI Client

**For: developers**

Query external DCI-compliant registries from OpenSPP — verify births against a national CRVS, check for duplicate enrollments in an IBR, or look up disability status for eligibility targeting.

## Prerequisites

- `spp_dci_client` installed, plus the specialized client for your use case (`spp_dci_client_crvs`, `spp_dci_client_ibr`, `spp_dci_client_dr`)
- A configured `spp.dci.data.source` record for each external registry
- A registered signing key (`spp.dci.signing.key`) for outbound message signing
- Familiarity with {doc}`protocol` — message envelope, HTTP Signature, query types

## Architecture

```{mermaid}
sequenceDiagram
    participant Code as OpenSPP code<br/>(service/model/job)
    participant Service as CRVSService /<br/>IBRService / DRService
    participant DCIClient as DCIClient<br/>(spp_dci_client)
    participant External as External registry

    Code->>Service: call domain method<br/>(e.g., verify_birth)
    Service->>DCIClient: search_by_id(...)
    DCIClient->>DCIClient: acquire OAuth token<br/>sign envelope
    DCIClient->>External: POST /registry/sync/search<br/>Bearer + signature
    External-->>DCIClient: signed response envelope
    DCIClient->>DCIClient: verify response signature
    DCIClient-->>Service: response dict
    Service-->>Code: domain result<br/>(e.g., birth record / None)
```

All client calls are **synchronous Python** — no `async`/`await` in OpenSPP code. The `_async` in method names like `search_async()` refers to the DCI protocol mode (the async HTTP endpoint), not to Python async/await.

## Module layout

```{note}
Every specialized client (`spp_dci_client_crvs`, `spp_dci_client_ibr`, `spp_dci_client_dr`) is a thin wrapper over the base `DCIClient`. The wrappers add domain-specific convenience methods and concrete helper data classes; they do not add new authentication or signing behavior.
```

| Module | Purpose |
|--------|---------|
| `spp_dci_client` | Base client (`DCIClient`) — HTTP, OAuth 2.0, outbound signature |
| `spp_dci_client_crvs` | `CRVSService` — birth verification, death check, event subscription |
| `spp_dci_client_ibr` | `IBRService` — duplicate enrollment checks, beneficiary search |
| `spp_dci_client_dr` | `DRService` — disability status, functional assessment |

## Configuring a data source

**Model:** `spp.dci.data.source`

Create one record per external registry. The `code` field is the lookup key services use to find the right data source (e.g., the CRVS service defaults to `code="crvs_main"`).

Key fields:

| Field | Purpose |
|-------|---------|
| `name` | Human-readable name |
| `code` | Unique lookup code (`crvs_main`, `ibr_national`, `dr_main`, etc.) |
| `registry_type` | `SOCIAL_REGISTRY`, `IBR`, `CRVS`, `DR`, `FR` |
| `base_url` | Base URL of the external registry (e.g., `https://crvs.example.org/api/v1`) |
| `auth_type` | `none`, `bearer`, `basic`, or `oauth2` (most external registries use `oauth2`) |
| `bearer_token` | Static Bearer token (when `auth_type=bearer`) |
| `oauth2_token_url`, `oauth2_client_id`, `oauth2_client_secret`, `oauth2_scope` | OAuth 2.0 client-credentials fields |
| `oauth2_credential_location` | `body` (RFC 6749) or `query` (OpenCRVS workaround) |
| `signing_key_id` | Link to `spp.dci.signing.key` used to sign outbound messages |
| `our_sender_id` | The `sender_id` we present to this external registry |
| `our_callback_uri` | Callback URL for async responses |
| `receiver_id` | The registry's `receiver_id` (defaults to `base_url` if unset) |
| `search_endpoint` | Path for sync search (default `/registry/sync/search`) |
| `subscribe_endpoint` | Path for subscribe (default `/registry/subscribe`) |
| `auth_endpoint` | Path for OAuth token (default `/oauth2/client/token`) |
| `verify_ssl` | Whether to verify TLS certificates |
| `timeout` | Request timeout in seconds (default 30) |

Useful methods:

| Method | Purpose |
|--------|---------|
| `test_connection()` | Exercises the configured auth + a trivial request, updates `state` |
| `get_by_code(code)` | Class method — look up data source by its `code` |
| `get_by_registry_type(registry_type)` | Return recordset of sources for a given registry type |
| `get_oauth2_token(force_refresh=False)` | Acquires/caches an OAuth token |
| `clear_oauth2_token_cache()` | Force next request to re-authenticate |

The OAuth token is cached per process on the data source record. Tokens are automatically refreshed when they expire; call `clear_oauth2_token_cache()` if you need to force a refresh (e.g., after rotating credentials).

## The base `DCIClient`

**Module:** `spp_dci_client.services.client`
**Class:** `DCIClient`

```python
from odoo.addons.spp_dci_client.services.client import DCIClient

data_source = env["spp.dci.data.source"].get_by_code("crvs_main")
client = DCIClient(data_source, env)
```

The constructor takes a data source record and the Odoo environment. It validates that `base_url` and `our_sender_id` are configured and raises at construction time if not.

### Methods

All methods are synchronous. The `_async` in `search_async` refers to the DCI protocol's async mode, not Python asyncio.

| Method | Purpose |
|--------|---------|
| `search(query_type, query_value, record_type="PERSON", page=1, page_size=10, registry_type=None, registry_event_type=None)` | Synchronous search via `/registry/sync/search` |
| `search_async(query_type, query_value, record_type="PERSON", page=1, page_size=10, registry_type=None, registry_event_type=None, callback_url=None)` | Async search via `/registry/search` — returns 202 immediately, delivers results via callback |
| `search_by_id(identifier_type, identifier_value, record_type="PERSON", page=1, page_size=10, async_mode=False, registry_event_type=None)` | Convenience for `idtype-value` queries |
| `search_by_id_opencrvs(identifier_type, identifier_value, event_type="birth", page=1, page_size=10, async_mode=False)` | OpenCRVS-compatible identifier lookup |
| `search_by_predicate(predicate, record_type="PERSON", page=1, page_size=10, async_mode=False)` | CEL-style predicate query |
| `search_by_expression(expression, record_type="PERSON", page=1, page_size=10, registry_type=None, registry_event_type=None, async_mode=False, use_opencrvs_format=False)` | Expression query (AND/OR composition) |
| `search_by_date_range(start_date, end_date, attribute_name="dateOfEvent", event_type=None, record_type="PERSON", page=1, page_size=10, async_mode=False, use_opencrvs_format=False)` | Simplified date-range search |

There is no separate `authenticate()` method — OAuth token acquisition happens inside `_make_request()` on each call and is cached on the data source record.

### Example

```python
client = DCIClient(data_source, env)

# Lookup by national ID
response = client.search_by_id(
    identifier_type="UIN",
    identifier_value="12345678",
)

# Extract the record list from the response envelope
records = (
    response.get("message", {})
    .get("search_response", [{}])[0]
    .get("data", {})
    .get("reg_records", [])
)
```

## CRVS client — `spp_dci_client_crvs`

**Class:** `CRVSService` (`spp_dci_client_crvs/services/crvs_service.py`)

```python
from odoo.addons.spp_dci_client_crvs.services.crvs_service import CRVSService

service = CRVSService(env, data_source_code="crvs_main")
```

Note the constructor shape: `(env, data_source_code)` — code string first, data source looked up internally.

### Methods

| Method | Returns | Purpose |
|--------|---------|---------|
| `verify_birth(identifier_type, identifier_value)` | `dict \| None` | Verify a birth record. Returns dict with `birth_date`, `person_name`, `mother_name`, `father_name`, `place_of_birth`, or `None` if not found. |
| `check_death(identifier_type, identifier_value)` | `bool` | True if the person is recorded as deceased. |
| `subscribe_events(event_types=None)` | `list[str]` | Subscribe to CRVS vital events. Defaults to `['BIRTH', 'DEATH']`. Returns subscription codes. |

### Example

```python
service = CRVSService(env, data_source_code="crvs_main")

birth = service.verify_birth("BRN", "BR-2024-0042")
if birth:
    print(f"Verified birth: {birth['person_name']} on {birth['birth_date']}")
```

## IBR client — `spp_dci_client_ibr`

**Class:** `IBRService` (`spp_dci_client_ibr/services/ibr_service.py`)

```python
from odoo.addons.spp_dci_client_ibr.services.ibr_service import IBRService

data_source = env["spp.dci.data.source"].get_by_code("ibr_main")
service = IBRService(data_source, env)
```

```{important}
`IBRService` takes `(data_source, env)` — record first, then env. This is **reversed** from `CRVSService` and `DRService`, which both take `(env, data_source_code)`. Mixing them up raises a `TypeError` at construction.
```

### Methods

| Method | Returns | Purpose |
|--------|---------|---------|
| `check_duplication(partner)` | `dict` | Checks if the partner is already enrolled in other programs. Returns `{is_duplicate, matched_programs, raw_response}`. Raises `UserError` if the partner has no identifiers. |
| `search_beneficiary(identifier_type, identifier_value)` | `list[dict]` | Search for beneficiary records by identifier. |

### Helper classes

The service module exports two helper classes useful when building your own responses:

- `DuplicationResult(is_duplicate, matched_programs, raw_response)` — with `.to_dict()`
- `BeneficiaryInfo(identifier_type, identifier_value, name, programs, metadata)` — with `.to_dict()`

### Example

```python
service = IBRService(data_source, env)

result = service.check_duplication(partner)
if result["is_duplicate"]:
    raise UserError(
        f"Already enrolled in: {', '.join(result['matched_programs'])}"
    )
```

## Disability Registry client — `spp_dci_client_dr`

**Class:** `DRService` (`spp_dci_client_dr/services/dr_service.py`)

```python
from odoo.addons.spp_dci_client_dr.services.dr_service import DRService

service = DRService(env, data_source_code="dr_main")
```

Constructor shape matches CRVS: `(env, data_source_code)`.

### Methods

| Method | Returns | Purpose |
|--------|---------|---------|
| `get_disability_status(partner)` | `dict \| None` | Retrieve disability status. Returns dict with `has_disability`, `disability_types`, `functional_scores`, `assessment_date`, `source_registry`, or `None`. |
| `get_functional_assessment(identifier_type, identifier_value)` | `dict \| None` | Washington Group scores (1-4) across Vision, Hearing, Mobility, Cognition, Self-Care, Communication. |
| `is_pwd(partner)` | `bool` | True if the partner is a person with disability. |
| `sync_disability_data(partner)` | — | Refresh local disability records from the remote registry. |

### Example

```python
service = DRService(env, data_source_code="dr_main")

status = service.get_disability_status(partner)
if status and status["has_disability"]:
    print(f"Disability types: {', '.join(status['disability_types'])}")
    mobility_score = status["functional_scores"].get("Mobility")
```

## Trying a working flow: `spp_dci_demo`

The `spp_dci_demo` module ships an end-to-end demo that layers a birth-verification workflow on top of `spp_mis_demo_v2`. Install it to see `CRVSService.verify_birth()` exercised in a child-benefit enrollment flow.

Dependencies: `spp_mis_demo_v2`, `spp_dci_client`, `spp_change_request_v2`, `spp_programs`.

## Common mistakes

**Wrong constructor shape.** `CRVSService` and `DRService` take `(env, code)`; `IBRService` takes `(data_source, env)`. Mixing them raises `TypeError`. A common error is `IBRService(env, code)` — this passes an env where a data source record is expected.

**Using the wrong data source code.** The CRVS service defaults to `"crvs_main"`, the DR service to `"dr_main"`. If your deployment uses a different code, pass it explicitly: `CRVSService(env, data_source_code="crvs_ph")`.

**Expecting an `authenticate()` method.** The base `DCIClient` has no public `authenticate()` method. OAuth token acquisition happens automatically inside `_make_request()` and is cached on the data source record.

**Treating async as Python asyncio.** `DCIClient.search_async(...)` is a synchronous Python call that uses the DCI protocol's async endpoint. It returns immediately after the server accepts the request; actual results arrive via a callback to `our_callback_uri` on the data source. No `await` is needed or supported.

**Not setting `our_sender_id` on the data source.** The client constructor raises immediately if `our_sender_id` is blank — external registries identify you by this value.

**Missing signing key on the data source.** Without a `signing_key_id`, outbound messages cannot be signed and external registries that require signatures will reject your requests with a signature-related `err.*` code.

**Sharing OAuth tokens across workers.** Tokens are cached per-process on the data source record. For high-volume use, either increase the token lifetime on the authorization server side or call `clear_oauth2_token_cache()` to force a refresh in each worker.

**Assuming CEL variables are pre-registered.** There is no `spp_dci_indicators` module shipped. If you want DCI data to drive CEL-based eligibility, you'll need to register your own CEL variables whose compute functions call `CRVSService`, `IBRService`, or `DRService`. See {doc}`/developer_guide/cel/index`.

## See also

- {doc}`server_role` — OpenSPP as DCI server
- {doc}`protocol` — message envelope, signatures, endpoints
- {doc}`overview` — DCI architecture and use cases
- {doc}`/developer_guide/cel/index` — CEL expressions for program eligibility
- [DCI API Standards](https://github.com/spdci/api-standards)
