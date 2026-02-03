---
openspp:
  doc_status: draft
---

# OpenSPP API V2 - Cycles


## Overview

OpenSPP API V2 - Cycles extends the core API V2 module with RESTful endpoints for program cycle management. It enables external systems to query cycle information for coordination of disbursement schedules and program timeline tracking.

## Purpose

This module is designed to:

- **Expose cycle data:** Provide read access to program cycle information via REST API
- **Support external coordination:** Allow payment systems and other platforms to synchronize with cycle schedules
- **Maintain API consistency:** Follow OpenSPP API V2 patterns for authentication and response formats

## Module Dependencies

| Dependency       | Description                                                   |
| ---------------- | ------------------------------------------------------------- |
| **spp_api_v2**   | Core API V2 module providing authentication and base patterns |
| **spp_programs** | Program and cycle management models                           |

## Key Features

### Cycle Search

Query cycles with filtering by program, status, date ranges, and other criteria. Results include cycle details needed for external system coordination.

### Cycle Lookup

Retrieve detailed information for a specific cycle using its name as the external identifier.

### Consistent Authentication

All endpoints require OAuth 2.0 authentication through the core API V2 module.

## API Endpoints

| Endpoint              | Method | Description                         |
| --------------------- | ------ | ----------------------------------- |
| `/Cycle`              | GET    | Search cycles with optional filters |
| `/Cycle/{identifier}` | GET    | Read a specific cycle by name       |

### Search Parameters

| Parameter  | Type   | Description                  |
| ---------- | ------ | ---------------------------- |
| program    | string | Filter by program identifier |
| state      | string | Filter by cycle state        |
| start_date | date   | Filter by start date         |
| end_date   | date   | Filter by end date           |

### Response Fields

| Field      | Type    | Description                        |
| ---------- | ------- | ---------------------------------- |
| name       | string  | Cycle identifier (used in lookups) |
| program    | string  | Program identifier                 |
| state      | string  | Current cycle state                |
| start_date | date    | Cycle start date                   |
| end_date   | date    | Cycle end date                     |
| sequence   | integer | Cycle sequence number              |

## Integration

### With Core API V2

This module extends `spp_api_v2` and inherits:

- OAuth 2.0 authentication
- Consistent error handling
- Standard response formats
- API client access control

### With Programs Module

Cycle data comes from `spp_programs`, including:

- Cycle definitions and states
- Program associations
- Date ranges and sequences

### Auto-Installation

This module auto-installs when both `spp_api_v2` and `spp_programs` are present, ensuring cycle endpoints are available whenever the prerequisites exist.

## Are you stuck?

### Cycle not found error

**Symptom:** 404 error when requesting a cycle
**Cause:** Invalid cycle name or cycle does not exist
**Solution:** Use the cycle's exact name as shown in the program management interface

### Empty search results

**Symptom:** Search returns no cycles
**Cause:** Filters exclude all cycles or no cycles exist for the program
**Solution:** Verify program has cycles defined, adjust filter parameters

### Access denied to cycle

**Symptom:** 403 error when accessing cycle
**Cause:** API client lacks access to the associated program
**Solution:** Configure the API client with access to the required program
