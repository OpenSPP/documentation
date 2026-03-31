---
openspp:
  doc_status: draft
  products: [core]
---

# Developer guide

**For: developers** (Python developers extending OpenSPP)

This guide is for developers who want to extend OpenSPP, integrate it with other systems, or contribute to the core platform. It covers the technical architecture, development setup, API integration, and best practices for building on OpenSPP.

## Topics covered

- **[Setup](setup/index.md)**: Setting up your development environment for OpenSPP development
- **[Architecture](architecture/index.md)**: Understanding the system design, module structure, and technical decisions
- **[Custom modules](custom_modules/index.md)**: Creating Odoo modules for OpenSPP — the module scaffold, manifest, models, and views
- **[Custom program managers](custom_managers/index.md)**: Building custom eligibility, entitlement, cycle, and payment managers
- **[Custom change request types](change_request_types/index.md)**: Building complex CR types that go beyond Studio's basic support
- **[API V2](api_v2/index.md)**: Using the official REST API with OAuth 2.0 and consent-based access
- **[DCI integration](dci/index.md)**: Implementing Digital Convergence Initiative protocols
- **[Verifiable credentials](verifiable_credentials/index.md)**: W3C Verifiable Credentials and OIDC4VCI support
- **[Other integrations](integrations/index.md)**: Connecting to OIDC/eSignet, Keycloak, and external APIs
- **[Security and encryption](security/index.md)**: PII encryption, key management, and security scanning
- **[CEL](cel/index.md)**: Common Expression Language for scoring, eligibility, and dynamic queries
- **[Studio](studio/index.md)**: No-code configuration and making modules Studio-aware
- **[Audit and versioning](audit/index.md)**: Audit logging, record versioning, and data provenance
- **[Contributing](contributing/index.md)**: Code style, pre-commit hooks, and pull request workflow
- **[Testing](testing/index.md)**: Writing and running unit, integration, and end-to-end tests

```{toctree}
:maxdepth: 2
:hidden:

setup/index
architecture/index
custom_modules/index
custom_managers/index
change_request_types/index
api_v2/index
dci/index
verifiable_credentials/index
integrations/index
security/index
cel/index
studio/index
audit/index
contributing/index
testing/index
```

<!-- Hidden until ready: drims/index, migration/index -->
