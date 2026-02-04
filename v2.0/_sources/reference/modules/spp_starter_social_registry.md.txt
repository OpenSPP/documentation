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

| Category              | Modules                                                                    | Description                                               |
| --------------------- | -------------------------------------------------------------------------- | --------------------------------------------------------- |
| **Core Registry**     | spp_registry, spp_registry_search                                          | Individual and group management with search-first privacy |
| **Security**          | spp_security                                                               | Role-based access control                                 |
| **Geographic**        | spp_area                                                                   | Administrative boundary management                        |
| **Vocabulary**        | spp_vocabulary                                                             | Standardized code lists                                   |
| **Data Management**   | spp_consent, spp_source_tracking                                           | Consent management and data provenance                    |
| **Async Processing**  | queue_job                                                                  | Background job processing                                 |
| **Change Requests**   | spp_change_request_v2, spp_cr_types_base                                   | Data change workflows                                     |
| **Expression Engine** | spp_cel_domain                                                             | CEL-based expressions                                     |
| **No-Code UI**        | spp_studio                                                                 | Visual configuration tools                                |
| **API**               | spp_api_v2, spp_api_v2_data                                                | REST API with consent-based access                        |
| **DCI Integration**   | spp_dci_client, spp_dci_client_crvs, spp_dci_client_ibr, spp_dci_client_dr | External registry connections                             |

### Auto-Installing Modules

These modules install automatically when dependencies are met:

- **spp_api_v2_vocabulary:** API endpoints for vocabularies (with spp_api_v2 + spp_vocabulary)
- **spp_api_v2_change_request:** API endpoints for change requests (with spp_api_v2 + spp_change_request_v2)

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
