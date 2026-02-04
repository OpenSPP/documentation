---
openspp:
  doc_status: draft
---

# API V2 - Service Points

**Module:** `spp_api_v2_service_points`

## Overview

OpenSPP API V2 - Service Points extends the core API V2 module with RESTful endpoints for querying service point information. This module enables external systems to access service point locations for distribution planning, beneficiary routing, and payment provider coordination.

## Purpose

This module is designed to:

- **Expose service point data:** Provide read access to physical and virtual service delivery locations
- **Support distribution planning:** Enable external systems to coordinate with service point networks
- **Enable beneficiary routing:** Allow platforms to direct beneficiaries to appropriate service points
- **Integrate with payment providers:** Share service point information for cash disbursement

## Module Dependencies

| Dependency             | Description                                                   |
| ---------------------- | ------------------------------------------------------------- |
| **spp_api_v2**         | Core API V2 module providing authentication and base patterns |
| **spp_service_points** | Service point management models                               |

## Key Features

### Service Point Search

Query service points with filtering by area, type, status, and other criteria. Results include location and operational details needed for external coordination.

### Service Point Lookup

Retrieve detailed information for a specific service point using its name or identifier.

### Location Information

Service points include geographic data for mapping and routing applications.

### Consistent Authentication

All endpoints require OAuth 2.0 authentication through the core API V2 module.

## API Endpoints

| Endpoint                     | Method | Description                                 |
| ---------------------------- | ------ | ------------------------------------------- |
| `/ServicePoint`              | GET    | Search service points with optional filters |
| `/ServicePoint/{identifier}` | GET    | Read a specific service point by name or ID |

### Search Parameters

| Parameter | Type    | Description                   |
| --------- | ------- | ----------------------------- |
| area      | string  | Filter by administrative area |
| type      | string  | Filter by service point type  |
| active    | boolean | Filter by active status       |
| program   | string  | Filter by associated program  |

### Response Fields

| Field     | Type    | Description                     |
| --------- | ------- | ------------------------------- |
| name      | string  | Service point name (identifier) |
| type      | string  | Service point type              |
| area      | string  | Administrative area             |
| address   | string  | Physical address                |
| latitude  | decimal | Geographic latitude             |
| longitude | decimal | Geographic longitude            |
| phone     | string  | Contact phone number            |
| active    | boolean | Whether service point is active |
| programs  | list    | Associated programs             |

## Integration

### With Core API V2

This module extends `spp_api_v2` and inherits:

- OAuth 2.0 authentication
- External identifier patterns (uses name, not database IDs)
- Standard response formats
- Consistent error handling

### With Service Points Module

Service point data comes from `spp_service_points`, including:

- Service point definitions
- Geographic locations
- Area associations
- Program linkages

### With External Systems

Common integration patterns include:

- **Payment providers:** Retrieve service points for cash distribution
- **Mobile applications:** Display nearby service points to beneficiaries
- **Distribution planning:** Coordinate in-kind deliveries
- **Mapping systems:** Visualize service point coverage

### Auto-Installation

This module auto-installs when both `spp_api_v2` and `spp_service_points` are present, ensuring service point endpoints are available whenever the prerequisites exist.
