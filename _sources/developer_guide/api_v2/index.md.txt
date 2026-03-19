---
openspp:
  doc_status: draft
  products: [core]
---

# API V2

This guide is for **developers** integrating with OpenSPP.

**NEW V2** - Complete redesign of the OpenSPP API

The official OpenSPP REST API (V2) provides a modern, secure, and standards-compliant interface for integrating with OpenSPP. This API replaces the legacy XML-RPC API and follows REST best practices, OAuth 2.0 authentication, and consent-based access control.

## Topics Covered

| Topic | Description |
|-------|-------------|
| {doc}`overview` | API design philosophy and core concepts |
| {doc}`authentication` | Secure authentication using OAuth 2.0 |
| {doc}`external_identifiers` | Using external IDs instead of database IDs |
| {doc}`consent` | Privacy-first consent mechanisms |
| {doc}`resources` | Available API resources and operations |
| {doc}`search` | Advanced query and filtering |
| {doc}`batch` | Processing multiple records efficiently |
| {doc}`errors` | Error responses and status codes |
| {doc}`studio_integration` | Studio custom fields and variables via API |

```{note}
This completely replaces the legacy XML-RPC API. New integrations should use API V2.
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
```
