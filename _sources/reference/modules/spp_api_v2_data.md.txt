---
openspp:
  doc_status: draft
---

# API V2 - Data

**Module:** `spp_api_v2_data`

## Overview

OpenSPP API V2 - Data extends the core API V2 module with endpoints for variable data push and pull operations. This module enables external systems to contribute calculated values and retrieve variable data for registrants, supporting data exchange with analytics platforms, survey systems, and external data providers.

## Purpose

This module is designed to:

- **Push variable values:** Accept computed values from external systems into OpenSPP
- **Pull variable data:** Expose variable values for registrants to authorized systems
- **Manage data freshness:** Support invalidation of cached values when source data changes
- **List available variables:** Provide discovery of defined variables in the system

## Module Dependencies

| Dependency         | Description                                                   |
| ------------------ | ------------------------------------------------------------- |
| **spp_api_v2**     | Core API V2 module providing authentication and base patterns |
| **spp_cel_domain** | CEL domain query builder for variable definitions             |

## Key Features

### Data Push

External systems can push calculated variable values into OpenSPP. This supports scenarios where:

- External analytics compute scores or indicators
- Survey systems provide collected data
- Partner systems share derived metrics

### Data Pull

Authorized systems can retrieve variable values for specific subjects, enabling:

- Eligibility checks by external platforms
- Data sharing with authorized partners
- Reporting and analytics integration

### Cache Invalidation

When source data changes, the invalidation endpoint ensures stale cached values are cleared, maintaining data accuracy across the system.

### Variable Discovery

The variables endpoint lists all defined variables, helping external systems understand available data points for integration.

## API Endpoints

| Endpoint           | Method | Description                                |
| ------------------ | ------ | ------------------------------------------ |
| `/Data/push`       | POST   | Push variable values from external systems |
| `/Data/pull`       | GET    | Pull variable values for subjects          |
| `/Data/invalidate` | POST   | Invalidate cached values                   |
| `/Data/variables`  | GET    | List available variables                   |

### Push Request Format

| Field          | Type   | Required | Description                            |
| -------------- | ------ | -------- | -------------------------------------- |
| subject_id     | string | Yes      | External identifier for the registrant |
| variable_code  | string | Yes      | Variable code to update                |
| value          | any    | Yes      | Value to store                         |
| effective_date | date   | No       | When the value became effective        |
| source         | string | No       | Source system identifier               |

### Pull Parameters

| Parameter      | Type   | Description                            |
| -------------- | ------ | -------------------------------------- |
| subject_id     | string | External identifier for the registrant |
| variable_codes | list   | Variables to retrieve (empty for all)  |
| as_of_date     | date   | Point-in-time value retrieval          |

## Integration

### With Core API V2

This module extends `spp_api_v2` and inherits:

- OAuth 2.0 authentication
- External identifier patterns (no database IDs)
- Provider-based access control
- Source tracking on writes

### With CEL Domain Module

Variable definitions come from `spp_cel_domain`, which provides:

- Variable code definitions
- Data type specifications
- Computation rules

### With External Systems

Common integration patterns include:

- **Survey platforms:** Push collected data from ODK/KoBoToolbox
- **Analytics systems:** Push computed scores and indicators
- **Partner registries:** Bi-directional data sharing
- **Reporting tools:** Pull aggregated variable data

## Configuration

### API Client Permissions

| Setting           | Description                                |
| ----------------- | ------------------------------------------ |
| Can Push Data     | Allow this client to push variable values  |
| Can Pull Data     | Allow this client to pull variable values  |
| Allowed Variables | Restrict access to specific variable codes |
