---
openspp:
  doc_status: draft
  products: [core]
---

# Developer Guide

This guide is for developers and integrators building connections between OpenSPP and external systems. The focus is on **interoperability** -- how to exchange data with OpenSPP programmatically using standard protocols and APIs.

## API V2

The primary way to integrate with OpenSPP is through the REST API (V2). It provides endpoints for managing registrants (individuals and groups), programs, enrollments, and more.

- {doc}`api_v2/index` -- Full API reference including authentication, resource operations, search, batch processing, and error handling

## DCI Integration

OpenSPP implements the [DCI Interface Standards v1.0](https://standards.spdci.org/standards/standards-for-interoperability-interfaces/structure-and-versioning-of-the-standards) for registry interoperability, enabling data exchange with systems such as civil registration and vital statistics (CRVS) platforms.

- {doc}`dci` -- Server and client implementation guide for the DCI specification

## Verifiable Credentials

OpenSPP supports the issuance of Verifiable Credentials (VCs) through the OpenID for Verifiable Credential Issuance (OpenID4VCI) standard, enabling secure and privacy-preserving digital identity for registrants.

- {doc}`verifiable_credentials` -- Overview of VC issuance for individuals, groups, and program beneficiaries

```{toctree}
:maxdepth: 3
:hidden:

api_v2/index
dci
verifiable_credentials
```
