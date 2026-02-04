---
openspp:
  doc_status: draft
---

# API V2

**Module:** `spp_api_v2`

## Overview

OpenSPP API V2 is the core API module providing standards-aligned, consent-respecting RESTful endpoints for social protection data exchange. Built on FastAPI, it establishes the foundation for all API V2 extension modules and enforces consistent security, authentication, and data access patterns across the platform.

## Purpose

This module is designed to:

- **Provide secure API access:** OAuth 2.0 client credentials flow for authentication with JWT tokens
- **Enforce consent-based access:** All data access requires explicit consent from registrants
- **Use external identifiers only:** Never exposes database IDs, using namespace URIs for all identifier types
- **Track data provenance:** Records source information for all data modifications per ADR-008
- **Enable extensibility:** Module-specific fields via a standardized extension mechanism

## Module Dependencies

| Dependency              | Description                                               |
| ----------------------- | --------------------------------------------------------- |
| **base**                | Odoo base module                                          |
| **fastapi**             | FastAPI integration for Odoo                              |
| **spp_security**        | Central security definitions for access control           |
| **spp_registry**        | Registry models for individuals and groups                |
| **spp_consent**         | Consent management for data access authorization          |
| **spp_vocabulary**      | Standardized vocabularies for gender, relationships, etc. |
| **spp_programs**        | Program and membership management                         |
| **spp_source_tracking** | Data provenance tracking                                  |

## Key Features

### External Identifiers

The API exclusively uses external identifiers with namespace URIs. Database IDs are never exposed in any endpoint, ensuring data portability and security.

### Consent-Based Access Control

Every data read operation verifies that appropriate consent exists. Without valid consent, the API returns appropriate error responses rather than exposing protected data.

### OAuth 2.0 Authentication

The module implements the OAuth 2.0 client credentials flow:

1. API clients register and receive credentials
2. Clients exchange credentials for JWT tokens
3. Tokens authenticate all subsequent requests

### Vocabulary Integration

All coded values (gender, relationship types, etc.) use the `spp.vocabulary` system with namespace URIs, ensuring consistent terminology across integrations.

### Source Tracking

Every create and update operation records:

- The API client that made the request
- Timestamp of the operation
- Source system information

### Extensible Field System

Extension modules can register additional fields through the API extension mechanism, allowing domain-specific data without modifying core schemas.

## API Endpoints

The core module provides endpoints for:

| Resource              | Endpoints                                                             | Description                      |
| --------------------- | --------------------------------------------------------------------- | -------------------------------- |
| **Individual**        | `GET /Individual`, `GET /Individual/{identifier}`, `POST /Individual` | Individual registrant management |
| **Group**             | `GET /Group`, `GET /Group/{identifier}`, `POST /Group`                | Group/household management       |
| **Program**           | `GET /Program`, `GET /Program/{identifier}`                           | Program information              |
| **ProgramMembership** | `GET /ProgramMembership`, `POST /ProgramMembership`                   | Program enrollment               |
| **Authentication**    | `POST /token`                                                         | OAuth 2.0 token endpoint         |

## Configuration

### API Client Setup

| Field            | Required | Description                          |
| ---------------- | -------- | ------------------------------------ |
| Name             | Yes      | Client identifier                    |
| Client ID        | Yes      | OAuth 2.0 client ID                  |
| Client Secret    | Yes      | OAuth 2.0 client secret (shown once) |
| Allowed Programs | No       | Restrict access to specific programs |
| Active           | Yes      | Enable/disable the client            |

### Filter Configuration

The module includes pre-configured filters for:

- Individual searches
- Group searches
- Program queries
- Program membership queries

## Integration

### With Other API V2 Modules

This module serves as the foundation for all API V2 extensions:

- **spp_api_v2_cycles** - Adds cycle endpoints
- **spp_api_v2_data** - Adds variable data push/pull
- **spp_api_v2_entitlements** - Adds entitlement endpoints
- **spp_api_v2_products** - Adds product catalog endpoints
- **spp_api_v2_service_points** - Adds service point endpoints
- **spp_api_v2_vocabulary** - Adds vocabulary lookup endpoints

### With External Systems

The API follows G2P Connect and related standards, enabling integration with:

- National ID systems
- Payment service providers
- Data collection tools (ODK, KoBoToolbox)
- Other social protection platforms

## Architecture Decision Records

This module implements patterns defined in:

- **ADR-007:** Namespace URIs for Identifiers
- **ADR-008:** Source Tracking and Provenance
- **ADR-009:** Terminology System
