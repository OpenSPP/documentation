---
openspp:
  doc_status: draft
  products: [core]
---

# Developer Guide

This guide is for developers who want to extend OpenSPP, integrate it with other systems, or contribute to the core platform. It covers the technical architecture, development setup, API integration, and best practices for building on OpenSPP.

## API V2

The primary way to integrate with OpenSPP is through the REST API (V2). It provides endpoints for managing registrants (individuals and groups), programs, enrollments, and more.

- {doc}`api_v2/index` -- Full API reference including authentication, resource operations, search, batch processing, and error handling

## DCI Integration

OpenSPP implements the [DCI Interface Standards v1.0](https://standards.spdci.org/standards/standards-for-interoperability-interfaces/structure-and-versioning-of-the-standards) for registry interoperability, enabling data exchange with systems such as civil registration and vital statistics (CRVS) platforms.

- {doc}`dci/index` -- Server and client implementation guide for the DCI specification

## Verifiable Credentials

OpenSPP supports the issuance of Verifiable Credentials (VCs) through the OpenID for Verifiable Credential Issuance (OpenID4VCI) standard, enabling secure and privacy-preserving digital identity for registrants.

- {doc}`verifiable_credentials/index` -- Overview of VC issuance for individuals, groups, and program beneficiaries

## Other topics

- **[Setup](setup/index.md)**: Setting up your development environment for OpenSPP development
- **[Architecture](architecture/index.md)**: Understanding the system design, module structure, and technical decisions
- **[Extending OpenSPP](extending/index.md)**: Creating custom modules, managers, and workflows
- **[Other integrations](integrations/index.md)**: Connecting to OIDC/eSignet, Keycloak, and external APIs

```{toctree}
:maxdepth: 3
:hidden:

setup/index
architecture/index
extending/index
api_v2/index
dci/index
verifiable_credentials/index
integrations/index
```
