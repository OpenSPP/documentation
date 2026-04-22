---
openspp:
  doc_status: draft
  products: [core]
---

# API V2

**For: developers**

The official OpenSPP REST API (V2) provides a modern, secure, and standards-compliant interface for integrating with OpenSPP. Built on FastAPI, it replaces the legacy XML-RPC API with OAuth 2.0 authentication, consent-based access control, external identifier references, and RFC 9457 error responses.

## How to use this section

1. Read {doc}`overview` for the design philosophy and core concepts
2. Read the reference pages for the features you need:
   - {doc}`authentication` for OAuth 2.0 and scopes
   - {doc}`external_identifiers`, {doc}`consent`, {doc}`errors` for cross-cutting concerns
   - {doc}`resources`, {doc}`search`, {doc}`batch` for core operations
3. Follow the {doc}`tutorial` to tie everything together in a working Python client
4. Consult {doc}`studio_integration` and the extension APIs as you need them

## Prerequisites

- Familiarity with REST APIs and HTTP
- Ability to issue HTTP requests from your integration environment (Python, JavaScript, curl, etc.)
- An OpenSPP deployment with `spp_api_v2` installed
- An API client registered in OpenSPP with the scopes you need (see {doc}`authentication`)

## When do you need API V2?

The API is the primary integration surface between OpenSPP and external systems. Use it when you need to:

| Requirement | API V2 | Alternative |
|-------------|:-:|-------------|
| Read/write registrants from an external system | Yes | |
| Trigger operations from a portal or mobile app | Yes | |
| Bulk-import beneficiary data | Yes (`$bulk`, `$batch`) | |
| Integrate with DCI-compliant systems | Yes | DCI client module |
| Automate change requests across systems | Yes | |
| Extend OpenSPP with internal Python code | | {doc}`/developer_guide/custom_modules/index` |
| Add custom program logic | | {doc}`/developer_guide/custom_managers/index` |
| Build no-code CR types | | {doc}`/config_guide/change_request_types/index` |

## Core topics

| Topic | Description |
|-------|-------------|
| {doc}`overview` | Design philosophy, base URL, core principles, FHIR-inspired patterns |
| {doc}`authentication` | OAuth 2.0, JWT tokens, scopes, and rate limiting |
| {doc}`external_identifiers` | Namespaced external IDs instead of database IDs |
| {doc}`consent` | Privacy-first consent mechanisms and field-level access |
| {doc}`resources` | Individual, Group, Program, and ProgramMembership resources |
| {doc}`search` | Query parameters, pagination, sorting, and advanced filters |
| {doc}`batch` | Transaction bundles, batch operations, and bulk export |
| {doc}`errors` | Error responses (RFC 9457) and status codes |
| {doc}`tutorial` | Build a working Python API client end-to-end |
| {doc}`studio_integration` | Studio custom fields and CEL variables via API |

## Extension APIs

These modules add domain-specific endpoints when installed alongside the core `spp_api_v2` module:

| Topic | Module | Description |
|-------|--------|-------------|
| {doc}`entitlements_cycles` | `spp_api_v2_entitlements`, `spp_api_v2_cycles` | Cash/in-kind entitlements and distribution cycles |
| {doc}`products_service_points` | `spp_api_v2_products`, `spp_api_v2_service_points` | Product catalog and distribution locations |
| {doc}`change_requests` | `spp_api_v2_change_request` | Data change request workflow with approvals |
| {doc}`data_api` | `spp_api_v2_data` | External data push/pull for variable caching |
| {doc}`simulation` | `spp_api_v2_simulation` | Scenario-based program simulation and analysis |
| {doc}`gis` | `spp_api_v2_gis` | Spatial queries, geofences, and OGC Features |

```{note}
API V2 completely replaces the legacy XML-RPC API. New integrations should use API V2.
```

## See also

- {doc}`/developer_guide/dci/index` — DCI protocol integration
- {doc}`/developer_guide/custom_modules/index` — building custom Odoo modules

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
tutorial
studio_integration
entitlements_cycles
products_service_points
change_requests
data_api
simulation
gis
```
