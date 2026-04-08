---
openspp:
  doc_status: draft
  products: [core]
---

# API V2

This guide is for **developers** integrating with OpenSPP.

The official OpenSPP REST API (V2) provides a modern, secure, and standards-compliant interface for integrating with OpenSPP. Built on FastAPI, it replaces the legacy XML-RPC API and follows REST best practices with OAuth 2.0 authentication, consent-based access control, and RFC 9457 error responses.

## Core Topics

| Topic | Description |
|-------|-------------|
| {doc}`overview` | API design philosophy, core concepts, and metadata |
| {doc}`authentication` | OAuth 2.0, JWT tokens, scopes, and rate limiting |
| {doc}`external_identifiers` | Namespaced external IDs instead of database IDs |
| {doc}`consent` | Privacy-first consent mechanisms and field-level access |
| {doc}`resources` | Individual, Group, Program, and ProgramMembership resources |
| {doc}`search` | Query parameters, pagination, sorting, and advanced filters |
| {doc}`batch` | Transaction bundles, batch operations, and bulk export |
| {doc}`errors` | Error responses (RFC 9457) and status codes |
| {doc}`studio_integration` | Studio custom fields and CEL variables via API |

## Extension APIs

| Topic | Module | Description |
|-------|--------|-------------|
| {doc}`entitlements_cycles` | `spp_api_v2_entitlements`, `spp_api_v2_cycles` | Cash/in-kind entitlements and distribution cycles |
| {doc}`products_service_points` | `spp_api_v2_products`, `spp_api_v2_service_points` | Product catalog and distribution locations |
| {doc}`change_requests` | `spp_api_v2_change_request` | Data change request workflow with approvals |
| {doc}`data_api` | `spp_api_v2_data` | External data push/pull for variable caching |
| {doc}`simulation` | `spp_api_v2_simulation` | Scenario-based program simulation and analysis |
| {doc}`gis` | `spp_api_v2_gis` | Spatial queries, geofences, and OGC Features |

```{note}
API V2 completely replaces the legacy XML-RPC API. New integrations should use API V2. Extension APIs require installing the corresponding module.
```

```{toctree}
:maxdepth: 2
:hidden:

overview
authentication
external_identifiers
consent
resources
search
batch
errors
studio_integration
entitlements_cycles
products_service_points
change_requests
data_api
simulation
gis
```
