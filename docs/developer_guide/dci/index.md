---
openspp:
  doc_status: draft
  products: [core]
---

# DCI Integration

**For: developers**

Integrate OpenSPP with Digital Convergence Initiative (DCI)-compliant social protection systems — either by exposing OpenSPP registry data through DCI endpoints or by consuming data from external DCI registries (CRVS, IBR, disability registries, etc.).

## How to use this section

1. Read {doc}`overview` to understand DCI architecture and the interaction patterns (sync/async search, subscribe/notify)
2. Read the role-specific guide for your scenario:
   - {doc}`server_role` — expose OpenSPP registry data to external DCI clients
   - {doc}`client_role` — query external DCI registries from OpenSPP
3. Consult {doc}`protocol` for message envelope, HTTP Signature, and endpoint reference

## Prerequisites

- Familiarity with Odoo module structure and FastAPI
- Understanding of HTTP Message Signatures (draft-cavage / RFC 9421)
- Familiarity with Bearer token authentication patterns
- Basic knowledge of async operations with `queue_job`
- Familiarity with the OpenSPP registry structure (`res.partner`, `spp.registry.id`)

## When do you need DCI?

| Scenario | Module(s) to install | Role | Guide |
|----------|---------------------|------|-------|
| Expose OpenSPP as a DCI server for external MIS systems | `spp_dci`, `spp_dci_server` | Server | {doc}`server_role` |
| Import births/deaths from a national CRVS | `spp_dci`, `spp_dci_client`, `spp_dci_client_crvs` | Client | {doc}`client_role` |
| Check for duplicate enrollments in other programs (IBR) | `spp_dci`, `spp_dci_client`, `spp_dci_client_ibr` | Client | {doc}`client_role` |
| Query a Disability Registry for eligibility targeting | `spp_dci`, `spp_dci_client`, `spp_dci_client_dr` | Client | {doc}`client_role` |
| Try an end-to-end DCI example out of the box | `spp_dci_demo` | Demo | Install the module |
| Understand DCI message formats / protocol details | `spp_dci` (core) | Either | {doc}`protocol` |
| Build a custom OpenSPP endpoint that isn't DCI-compliant | — | N/A | Use {doc}`/developer_guide/api_v2/index` instead |

## OpenSPP DCI modules

| Module | Purpose | Role |
|--------|---------|------|
| `spp_dci` | Core DCI infrastructure — message envelope, HTTP Signature, JWKS, shared schemas | Foundation |
| `spp_dci_server` | DCI server infrastructure — FastAPI app (`/dci_api/v1`), signature middleware, sender registry, subscriptions, transactions | Server |
| `spp_dci_client` | Base DCI client (`DCIClient`) — synchronous HTTP client with OAuth 2.0 and outbound signature handling | Client |
| `spp_dci_client_crvs` | CRVS client (`CRVSService`) for birth verification and death lookups | Client |
| `spp_dci_client_ibr` | IBR client (`IBRService`) for duplicate enrollment checks | Client |
| `spp_dci_client_dr` | Disability Registry client (`DRService`) for PWD status queries | Client |
| `spp_dci_demo` | End-to-end demo layered on `spp_mis_demo_v2` — birth verification for child benefit enrollment | Demo |

```{note}
**Server-side registry search needs an implementation module.** `spp_dci_server` provides the infrastructure (routers, middleware, models), but the actual search implementation for a given registry type is loaded dynamically. Until an implementation module is installed, search requests receive a rejection response. See {doc}`server_role` for details.
```

## Common integration scenarios

### As a DCI server

**Example:** A national MIS queries OpenSPP's Social Registry for beneficiary data.

```{mermaid}
graph LR
    A[External MIS] -->|DCI Search Request| B[OpenSPP DCI Server]
    B -->|Query Registry| C[res.partner]
    C -->|Results| B
    B -->|Signed DCI Response| A
```

See {doc}`server_role` for implementation details.

### As a DCI client

**Example:** OpenSPP imports birth registrations from a national CRVS.

```{mermaid}
graph LR
    A[OpenSPP DCI Client] -->|DCI Search Request| B[National CRVS]
    B -->|Birth Records| A
    A -->|Create Registrants| C[res.partner]
```

See {doc}`client_role` for implementation details.

## See also

- {doc}`/developer_guide/api_v2/index` — the general-purpose REST API (not DCI-specific)
- [DCI API Standards](https://github.com/spdci/api-standards) — official DCI specifications
- [G2P Connect](https://g2pconnect.cdpi.dev) — related protocol documentation
- [ADR-015](https://github.com/OpenSPP/openspp-modules-v2/blob/main/docs/architecture/decisions/ADR-015-dci-api-integration.md) — OpenSPP DCI architecture decision

```{toctree}
:maxdepth: 2
:hidden:

overview
server_role
client_role
protocol
```
