---
openspp:
  doc_status: draft
---

# OpenSPP API V2 - Entitlements


## Overview

OpenSPP API V2 - Entitlements extends the core API V2 module with RESTful endpoints for querying cash and in-kind entitlements. This module enables payment service providers, audit systems, and external platforms to access entitlement information for disbursement processing and reconciliation.

## Purpose

This module is designed to:

- **Expose entitlement data:** Provide read access to entitlement records via REST API
- **Support payment integration:** Enable payment providers to retrieve disbursement details
- **Enable auditing:** Allow external audit systems to verify entitlement records
- **Handle both entitlement types:** Support cash transfers and in-kind distributions

## Module Dependencies

| Dependency       | Description                                                   |
| ---------------- | ------------------------------------------------------------- |
| **spp_api_v2**   | Core API V2 module providing authentication and base patterns |
| **spp_programs** | Entitlement models for cash and in-kind transfers             |

## Key Features

### Entitlement Search

Query entitlements with filtering by program, cycle, beneficiary, status, and other criteria. Results include all details needed for payment processing.

### Entitlement Lookup

Retrieve detailed information for a specific entitlement using its code (UUID) as the external identifier.

### Cash and In-Kind Support

The API handles both entitlement types:

- **Cash entitlements:** Amount, currency, payment method
- **In-kind entitlements:** Products, quantities, units of measure

### Consistent Authentication

All endpoints require OAuth 2.0 authentication through the core API V2 module.

## API Endpoints

| Endpoint                    | Method | Description                               |
| --------------------------- | ------ | ----------------------------------------- |
| `/Entitlement`              | GET    | Search entitlements with optional filters |
| `/Entitlement/{identifier}` | GET    | Read a specific entitlement by code       |

### Search Parameters

| Parameter        | Type   | Description                      |
| ---------------- | ------ | -------------------------------- |
| program          | string | Filter by program identifier     |
| cycle            | string | Filter by cycle name             |
| beneficiary      | string | Filter by beneficiary identifier |
| state            | string | Filter by entitlement state      |
| entitlement_type | string | Filter by type (cash or inkind)  |

### Response Fields (Cash)

| Field       | Type    | Description                   |
| ----------- | ------- | ----------------------------- |
| code        | string  | Entitlement identifier (UUID) |
| program     | string  | Program identifier            |
| cycle       | string  | Cycle name                    |
| beneficiary | string  | Beneficiary identifier        |
| amount      | decimal | Transfer amount               |
| currency    | string  | Currency code                 |
| state       | string  | Current entitlement state     |
| valid_from  | date    | Entitlement validity start    |
| valid_until | date    | Entitlement validity end      |

### Response Fields (In-Kind)

| Field       | Type    | Description                   |
| ----------- | ------- | ----------------------------- |
| code        | string  | Entitlement identifier (UUID) |
| program     | string  | Program identifier            |
| cycle       | string  | Cycle name                    |
| beneficiary | string  | Beneficiary identifier        |
| product     | string  | Product identifier            |
| qty         | decimal | Quantity                      |
| unit        | string  | Unit of measure               |
| state       | string  | Current entitlement state     |

## Integration

### With Core API V2

This module extends `spp_api_v2` and inherits:

- OAuth 2.0 authentication
- External identifier patterns (uses UUID codes, not database IDs)
- Consent-based access control
- Standard response formats

### With Programs Module

Entitlement data comes from `spp_programs`, including:

- Cash entitlement records
- In-kind entitlement records
- Program and cycle associations
- Beneficiary linkages

### With Payment Systems

Common integration patterns include:

- Payment providers polling for approved entitlements
- Reconciliation of disbursed payments
- Audit trail verification

### Auto-Installation

This module auto-installs when both `spp_api_v2` and `spp_programs` are present, ensuring entitlement endpoints are available whenever the prerequisites exist.

## Are you stuck?

### Entitlement not found error

**Symptom:** 404 error when requesting an entitlement
**Cause:** Invalid entitlement code or entitlement does not exist
**Solution:** Use the entitlement's exact UUID code, not a human-readable reference

### Empty search results

**Symptom:** Search returns no entitlements
**Cause:** Filters exclude all entitlements or consent not granted
**Solution:** Verify consent exists for the API client, adjust filter parameters

### Missing beneficiary information

**Symptom:** Entitlement returned but beneficiary field is empty
**Cause:** Consent not granted for the beneficiary's data
**Solution:** Ensure consent records allow the API client to access beneficiary details

### Amount shows as zero

**Symptom:** Cash entitlement amount is 0
**Cause:** Entitlement not yet calculated or in draft state
**Solution:** Verify entitlement state is approved and calculation has completed
