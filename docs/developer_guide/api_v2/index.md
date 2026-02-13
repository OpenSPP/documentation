---
openspp:
  doc_status: draft
  products: [core]
---

# API V2

This guide is for **developers and integrators** connecting external systems to OpenSPP.

The official OpenSPP REST API (V2) provides a modern, secure, and standards-compliant interface for interoperability between OpenSPP and other systems such as civil registries, social protection platforms, payment providers, and humanitarian coordination tools. The API follows REST best practices, OAuth 2.0 authentication, and consent-based access control.

```{tip}
New to the API? Start with the {doc}`quickstart` to make your first API call in minutes. Download the [Postman collection](postman_collection.json) to start testing immediately.
```

## Getting Started

| Guide | Description |
|-------|-------------|
| {doc}`quickstart` | Make your first API call in 5 minutes |
| {doc}`overview` | API design philosophy and core concepts |
| {doc}`authentication` | Set up OAuth 2.0 authentication |

## Working with Data

| Guide | Description |
|-------|-------------|
| {doc}`individuals` | Create, read, update, and search individual registrants |
| {doc}`groups` | Manage households, add/remove members, merge and split groups |
| {doc}`programs` | Query programs and manage beneficiary enrollments |
| {doc}`search` | Advanced search, filtering, sorting, and pagination |
| {doc}`batch` | Create or update multiple records in a single request |
| {doc}`bulk_export` | Export multiple known records efficiently |

## Reference

| Guide | Description |
|-------|-------------|
| {doc}`external_identifiers` | How external identifiers work |
| {doc}`consent` | Consent-based access control and privacy |
| {doc}`resources` | Resource overview, scopes, and common patterns |
| {doc}`errors` | Error codes, formats, and handling strategies |
| {doc}`studio_integration` | Studio custom fields and variables via API |

## Downloads

- [Postman Collection](postman_collection.json) -- Pre-built API requests for testing and learning
- [OpenAPI Specification](openapi.yaml) -- Machine-readable API definition (OpenAPI 3.0)

```{note}
API V2 is the recommended integration path for all new system-to-system connections. It replaces the legacy XML-RPC API.
```

```{toctree}
:maxdepth: 2
:hidden:

quickstart
overview
authentication
external_identifiers
individuals
groups
programs
resources
search
batch
bulk_export
consent
errors
studio_integration
```
