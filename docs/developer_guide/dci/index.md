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
- Understanding of OAuth 2.0 and API authentication
- Basic knowledge of async operations with `queue_job`
- Familiarity with the OpenSPP registry structure (`res.partner`, `spp.registry.id`)

## When do you need DCI?

| Scenario | Module(s) to install | Role | Guide |
|----------|---------------------|------|-------|
| Expose OpenSPP as a Social Registry to external MIS dashboards | `spp_dci_server`, `spp_dci_server_social` | Server | {doc}`server_role` |
| Import births/deaths from a national CRVS | `spp_dci_client`, `spp_dci_client_crvs` | Client | {doc}`client_role` |
| Check for duplicate enrollments in other programs (IBR) | `spp_dci_client`, `spp_dci_client_ibr` | Client | {doc}`client_role` |
| Query a Disability Registry for eligibility targeting | `spp_dci_client`, `spp_dci_client_dr` | Client | {doc}`client_role` |
| Understand DCI message formats / protocol details | `spp_dci` (core) | Either | {doc}`protocol` |
| Build a custom OpenSPP endpoint that isn't DCI-compliant | — | N/A | Use {doc}`/developer_guide/api_v2/index` instead |

## OpenSPP DCI modules

| Module | Purpose | Role |
|--------|---------|------|
| `spp_dci` | Core DCI infrastructure — message envelope, HTTP Signature, JWKS, shared schemas | Foundation |
| `spp_dci_server` | Base DCI server infrastructure — routers, middleware, transaction tracking | Server |
| `spp_dci_server_social` | Social Registry server implementation — beneficiary/household search endpoints | Server |
| `spp_dci_client` | Base DCI client with OAuth 2.0 and signature handling | Client |
| `spp_dci_client_crvs` | CRVS client for birth/death lookups | Client |
| `spp_dci_client_ibr` | IBR client for duplicate enrollment checks | Client |
| `spp_dci_client_dr` | Disability Registry client | Client |

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
