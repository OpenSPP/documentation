---
openspp:
  doc_status: draft
  products: [core]
---

# OpenSPP as DCI Server

**For: developers**

Expose OpenSPP registry data to external DCI-compliant systems — national MIS dashboards querying beneficiary data, programs checking for duplicates, or research platforms pulling anonymized records.

## Prerequisites

- The core DCI modules installed: `spp_dci`, `spp_dci_server`
- Familiarity with FastAPI routers and Odoo's `fastapi` module integration
- Understanding of {doc}`protocol` — message envelope, HTTP Signature, endpoints

## Architecture

```{mermaid}
sequenceDiagram
    participant External as External System
    participant Middleware as Bearer + Signature<br/>middleware
    participant Router as FastAPI router<br/>(spp_dci_server)
    participant SearchSvc as Registry search<br/>implementation
    participant DB as res.partner

    External->>Middleware: POST /dci_api/v1/registry/sync/search<br/>Bearer + signed envelope
    Middleware->>Middleware: Validate token + signature
    Middleware->>Router: Authorized request
    Router->>SearchSvc: execute search
    SearchSvc->>DB: search(domain)
    DB-->>SearchSvc: partners
    SearchSvc->>SearchSvc: map to DCI Person/Group
    SearchSvc-->>Router: SearchResponse
    Router-->>External: 200 OK signed envelope
```

The `spp_dci_server` module ships the FastAPI app, routers, and middleware. The actual search implementation for a given registry type (Social Registry, CRVS, Disability, etc.) is loaded dynamically at request time — if the implementation module for the requested `reg_type` is not installed, the router returns a rejection envelope with reason code `rjct.search.not_supported`.

## Module layout

```{note}
`spp_dci_server` provides the infrastructure only. A registry-type-specific implementation module is needed to actually serve search requests. At the time of writing, no such implementation module ships in `openspp-modules-v2/` — server-side DCI is "infrastructure present, registry search implementation pending." Until one is installed, search requests will receive a rejection response.
```

The modules relevant to the server role:

| Module | Purpose |
|--------|---------|
| `spp_dci` | Core: envelope schemas, signing service, shared enums |
| `spp_dci_server` | Server infrastructure: FastAPI app (`/dci_api/v1`), signature middleware, sender registry, subscription model, transaction model |

### What `spp_dci_server` provides

```text
spp_dci_server/
├── data/fastapi_endpoint_data.xml    # Registers /dci_api/v1 FastAPI app
├── middleware/
│   ├── signature.py                  # Bearer + HTTP Signature verification
│   └── rate_limit.py                 # Per-sender rate limiting
├── routers/
│   ├── search.py                     # POST /registry/sync/search
│   ├── async_router.py               # POST /registry/search, subscribe, unsubscribe, txn/status
│   ├── receipt.py                    # POST /receipt
│   ├── callbacks.py                  # Callback response utilities
│   └── jwks.py                       # GET /.well-known/jwks.json
├── models/
│   ├── sender_registry.py            # spp.dci.sender.registry
│   ├── subscription.py               # spp.dci.subscription
│   ├── transaction.py                # spp.dci.transaction (async tracking)
│   ├── server_key.py                 # Server-side signing keys
│   └── fastapi_endpoint_dci.py
└── services/
    ├── response_signer.py            # Signs outbound responses
    ├── consent_adapter.py            # DCIConsentAdapter — consent filtering
    └── vocabulary_adapter.py         # Vocabulary mapping
```

## Configuration

The DCI server reads its behavior from Odoo system parameters (`ir.config_parameter`).

| Parameter | Default | Purpose |
|-----------|---------|---------|
| `dci.api_tokens` | *(none)* | Comma-separated allowlist of accepted Bearer tokens |
| `dci.bypass_bearer_auth` | `false` | Dev-mode: skip Bearer validation. Must be `false` in production. |
| `dci.allow_unsigned_requests` | `false` | Dev-mode: accept unsigned envelopes. Must be `false` in production. |

Set these in **Settings → Technical → Parameters → System Parameters**.

## Signing keys

The server needs at least one signing key to produce signed response envelopes.

**Model:** `spp.dci.signing.key` (from `spp_dci`)

Each key record stores the algorithm (`ed25519` or `rs256`), the key ID, and the private-key material. Public keys are automatically exposed via `/dci_api/v1/.well-known/jwks.json` for external systems to fetch.

The model provides an `action_generate_key` method — in the Odoo UI, create a new signing key, pick the algorithm, and click **Generate** to produce the key material.

## Registering external senders

Before an external system can call the DCI server, its sender identity must be registered so the server can verify its signatures.

**Model:** `spp.dci.sender.registry` (inherits `spp.api.client`)

Key fields:

| Field | Purpose |
|-------|---------|
| `sender_id` | Unique identifier the external system uses in the `sender_id` header |
| `public_key` | PEM-encoded public key used for signature verification |
| `jwks_url` | Alternative to inline `public_key` — URL to fetch the sender's JWKS |
| `algorithm` | `ed25519` or `rs256` |
| `auto_approve` | If true, the sender's subscribe requests are auto-approved |
| `rate_limit_per_minute` | Per-sender per-minute rate limit |
| `rate_limit_per_day` | Per-sender per-day rate limit |
| `organization_type` / `legal_basis` | Inherited from `spp.api.client` for consent filtering |

Methods:

| Method | Purpose |
|--------|---------|
| `fetch_public_key()` | Fetches from `jwks_url` and caches into `public_key` |
| `get_verifier()` | Returns a `DCIVerifier` configured with this sender's key |
| `get_by_sender_id(sender_id)` | Class method — look up the sender record by its DCI ID |

## Endpoints

The full endpoint inventory is in {doc}`protocol`. Summary:

| Method | Path | Router file |
|--------|------|-------------|
| POST | `/dci_api/v1/registry/sync/search` | `routers/search.py` |
| POST | `/dci_api/v1/registry/search` (async) | `routers/async_router.py` |
| POST | `/dci_api/v1/registry/subscribe` | `routers/async_router.py` |
| POST | `/dci_api/v1/registry/unsubscribe` | `routers/async_router.py` |
| POST | `/dci_api/v1/registry/sync/txn/status` | `routers/async_router.py` |
| POST | `/dci_api/v1/receipt` | `routers/receipt.py` |
| GET  | `/dci_api/v1/.well-known/jwks.json` | `routers/jwks.py` |

All POST endpoints run through the Bearer + HTTP Signature middleware. The JWKS endpoint is public.

## Consent filtering

Responses should be filtered according to the sender's legal basis and per-registrant consent. The server provides a `DCIConsentAdapter` class in `spp_dci_server/services/consent_adapter.py` that wraps the `spp_api_v2` consent infrastructure for DCI use.

Key methods on `DCIConsentAdapter`:

| Method | Purpose |
|--------|---------|
| `can_access_registrant(registrant_id, resource_type)` | Returns bool — whether this sender can access this registrant |
| `filter_dci_response(registrant_id, dci_data, resource_type, log_access)` | Strips unconsented fields from a response dict |
| `build_consented_domain(base_domain)` | Augments an Odoo search domain with consent filters |
| `log_dci_access(registrant_id, resource_type, action, fields_accessed)` | Records access for audit |

A search implementation should call these before returning records.

## Async search and subscriptions

For long-running searches or event subscriptions, use the async endpoints. The response pattern:

1. Client POSTs to `/dci_api/v1/registry/search` with a signed envelope containing `sender_uri` in the header
2. Server validates and enqueues the work via `queue_job`, returns `202 Accepted` with a correlation ID
3. When processing completes, the server POSTs the result envelope to the client's `sender_uri`
4. Client may poll `/dci_api/v1/registry/sync/txn/status` with the correlation ID for status

Transactions are tracked in `spp.dci.transaction`. Subscriptions are tracked in `spp.dci.subscription` with states `pending` → `active` (on auto-approve or manual confirm) → `cancelled`.

## Testing locally

During development you often need to call the DCI server without a full signed envelope. Set both bypass flags in system parameters:

```
dci.bypass_bearer_auth = true
dci.allow_unsigned_requests = true
```

When either flag is true, the signature middleware logs a `CRITICAL` warning on every request. Do not ship these values to production.

A simpler end-to-end local path: install the `spp_dci_demo` module, which seeds a working CRVS-integration flow you can exercise without any external systems.

## Common mistakes

**Forgetting to populate `dci.api_tokens`.** Without at least one token in the allowlist, every request with a `Bearer` header is rejected as invalid. Set the parameter before your first integration test.

**Relying on Bearer alone.** Bearer validation and signature verification are both enforced. A request with a valid Bearer token but an invalid or missing signature returns 401.

**Treating `spp_dci_server` as a fully operational search server.** The module ships the infrastructure; an implementation module for the registry type is required to actually answer searches. Without one, searches return a rejection.

**Not activating signing keys.** Keys must be in `state=active` to be included in the JWKS output. External systems that verify your responses fetch the JWKS; a newly created but inactive key won't appear there.

**Returning unfiltered registry data.** Use `DCIConsentAdapter` to filter responses. Returning raw `res.partner` fields bypasses consent and legal-basis controls.

**Hardcoding the sender_id.** The server's `sender_id` comes from system parameter `dci.sender_id`. Let deployments override it per environment rather than baking it into code.

**Copying the request header verbatim in responses.** Swap `sender_id` and `receiver_id` on the way back: your server's ID becomes the sender, the caller's ID becomes the receiver.

## See also

- {doc}`client_role` — OpenSPP as DCI client
- {doc}`protocol` — message envelope, signatures, endpoints
- {doc}`overview` — DCI architecture and use cases
- [DCI API Standards](https://github.com/spdci/api-standards)
