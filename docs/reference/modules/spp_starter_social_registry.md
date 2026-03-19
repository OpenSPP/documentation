---
openspp:
  doc_status: draft
---

# Starter: Social Registry

**Module:** `spp_starter_social_registry`

## Overview

The Social Registry Starter module is a comprehensive bundle for deploying a production-ready social registry system. It installs all necessary components for managing populations, including registry management, change requests, API access, external system integration, and no-code configuration tools.

## Purpose

This module is designed to:

- **Simplify deployment:** Install a complete social registry with a single module
- **Enable population tracking:** Manage individuals and household groups
- **Support data governance:** Provide change request workflows for data maintenance
- **Enable interoperability:** Connect to external registries via DCI standards
- **Provide API access:** Expose registry data through standards-aligned REST APIs

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `spp_registry` | Consolidated registry management for individuals, groups,... |
| `spp_registry_search` | Search-first registry interface for privacy protection |
| `spp_security` | Central security definitions for OpenSPP modules |
| `spp_area` | Establishes direct associations between OpenSPP registran... |
| `spp_vocabulary` | OpenSPP: Vocabulary |
| `spp_consent` | DPV-aligned consent management for social protection prog... |
| `spp_source_tracking` | Track data provenance and source information for registrants |
| `job_worker` | Background job worker |
| `spp_change_request_v2` | Configuration-driven change request system with UX improv... |
| `spp_cr_types_base` | Basic change request types with field mapping strategy |
| `spp_cel_domain` | Write simple CEL-like expressions to filter records (Open... |
| `spp_studio` | No-code customization interface for OpenSPP |
| `spp_api_v2` | OpenSPP API V2 - Standards-aligned, consent-respecting AP... |
| `spp_api_v2_data` | REST API endpoints for Variable Data push/pull. |
| `spp_dci_client` | Base DCI client infrastructure with OAuth2 and data sourc... |
| `spp_dci_client_crvs` | Connect to CRVS registries via DCI API |
| `spp_dci_client_ibr` | Connect to IBR for duplication checks via DCI API |
| `spp_dci_client_dr` | Connect to Disability Registry via DCI API |

## Key Features

### Registry Management

Track individuals and groups (households):

| Feature            | Description                                     |
| ------------------ | ----------------------------------------------- |
| Individual Records | Store personal information, IDs, and attributes |
| Group Records      | Manage households and other group types         |
| Group Membership   | Link individuals to groups with roles           |
| Privacy Protection | Search-first interface prevents bulk browsing   |

### Change Request System

Manage data modifications through workflows:

| CR Type         | Description                       |
| --------------- | --------------------------------- |
| Edit Individual | Modify individual registrant data |
| Edit Group      | Modify group/household data       |
| Update ID       | Change identification documents   |

### API V2

Standards-aligned REST API:

| Feature                  | Description                                |
| ------------------------ | ------------------------------------------ |
| Consent-Based Access     | Data sharing controlled by consent records |
| External Identifiers     | Never exposes internal database IDs        |
| Vocabulary Endpoints     | Access standardized code lists             |
| Change Request Endpoints | Submit and track data changes via API      |

### DCI Client Integration

Connect to external registries:

| Integration | Description                             |
| ----------- | --------------------------------------- |
| CRVS        | Civil Registration and Vital Statistics |
| IBR         | Identity-Based Registry                 |
| DR          | Disability Registry                     |

### Logic Studio

No-code expression building:

| Feature         | Description                            |
| --------------- | -------------------------------------- |
| CEL Expressions | Build complex filters without coding   |
| Visual Builder  | Point-and-click expression creation    |
| Testing         | Validate expressions before deployment |

### Vocabularies

Standardized terminology:

| Feature                 | Description                                 |
| ----------------------- | ------------------------------------------- |
| Pre-loaded Lists        | Gender, relationships, marital status, etc. |
| International Standards | ISO, WHO, ILO compliance                    |
| Custom Vocabularies     | Add organization-specific codes             |

## Integration

The Social Registry Starter serves as the foundation for:

- **spp_starter_sp_mis:** Extends with program management for SP-MIS deployments
- **External systems:** REST API enables integration with third-party applications
- **Government registries:** DCI client connects to national ID and vital statistics systems

## Use Cases

| Use Case                   | Description                                 |
| -------------------------- | ------------------------------------------- |
| National Social Registries | Country-wide beneficiary databases          |
| Humanitarian Registration  | Emergency response population tracking      |
| Population Databases       | General demographic record keeping          |
| ID Management Systems      | Identity document tracking without programs |
