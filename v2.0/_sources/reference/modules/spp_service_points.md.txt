---
openspp:
  doc_status: draft
---

# Service Points

**Module:** `spp_service_points`

## Overview

The OpenSPP Service Points module manages physical or virtual locations where social protection services are delivered. It enables organizations to define, categorize, and manage service delivery points while linking them to geographical areas, company entities, and user accounts.

## Purpose

This module is designed to:

- **Manage service delivery locations:** Define and track physical or virtual service points
- **Link to geographical areas:** Associate service points with the area hierarchy for location-based management
- **Support agent management:** Create and manage user accounts for service point staff
- **Track service point status:** Monitor active/disabled status and contract information

## Module Dependencies

| Dependency           | Description                                |
| -------------------- | ------------------------------------------ |
| **spp_registry**     | OpenSPP registry for registrant management |
| **phone_validation** | Phone number formatting and validation     |
| **spp_area**         | Geographical area hierarchy                |
| **spp_security**     | OpenSPP security framework                 |
| **spp_vocabulary**   | Controlled vocabulary management           |

## Key Features

### Service Point Management

Each service point record contains:

| Field           | Description                                       |
| --------------- | ------------------------------------------------- |
| Name            | Agent or service point name                       |
| Area            | Linked geographical area                          |
| Service Types   | Categories of services offered (vocabulary-based) |
| Phone Number    | Contact phone with international formatting       |
| Address         | Physical location address                         |
| Country         | Country for phone validation                      |
| Company         | Linked company entity (res.partner)               |
| Active Contract | Contract status indicator                         |
| Disabled        | Service point enabled/disabled state              |
| Disabled Date   | When the service point was disabled               |
| Disabled Reason | Explanation for disabling                         |

### Service Type Classification

Service types are managed through the vocabulary system using the namespace `urn:openspp:vocab:service-types`. This allows organizations to define their own service categories.

### Phone Number Handling

The module provides:

- Automatic phone number sanitization
- International format validation
- Country-aware formatting
- Computed sanitized phone field for consistent storage

### Company and Individual Linking

Service points can be linked to company entities, automatically associating all individuals (contacts) under that company with the service point:

```
Service Point
    └── Company (res.partner with is_company=True)
        ├── Individual 1 (contact)
        ├── Individual 2 (contact)
        └── Individual 3 (contact)
```

### User Account Creation

The module can automatically create user accounts for company contacts:

| Action              | Description                                                      |
| ------------------- | ---------------------------------------------------------------- |
| Create Users        | Creates Odoo user accounts for all contacts with email addresses |
| Auto-assigns        | Adds users to the service point users group                      |
| Links Service Point | Associates users with their service point                        |

## Integration

### With spp_area

Service points are linked to the geographical area hierarchy, enabling:

- Area-based filtering and reporting
- Location-aware access control
- Regional service point management

### With spp_registry

The module extends `res.partner` to:

- Add service point relationships to registrants
- Compute individual service points based on group membership
- Maintain service point associations when registrants move between groups

### With spp_vocabulary

Service types are managed through controlled vocabularies, ensuring consistent categorization across the system.

## Configuration

### Creating a Service Point

| Field         | Required | Description                                        |
| ------------- | -------- | -------------------------------------------------- |
| Name          | Yes      | Service point identifier                           |
| Area          | No       | Geographical area link                             |
| Service Types | No       | Categories from vocabulary                         |
| Phone Number  | No       | Contact phone                                      |
| Address       | No       | Physical location                                  |
| Country       | No       | For phone formatting (defaults to company country) |
| Company       | No       | Associated company entity                          |

### Managing Service Point Status

To disable a service point:

1. Click the "Disable" button
2. The system automatically records the disable date
3. Optionally provide a reason for disabling

To re-enable:

1. Click the "Enable" button
2. Disabled date and reason are cleared

## Security

### Security Groups

The module defines a dedicated security group for service point users:

| Group                                    | Description                       |
| ---------------------------------------- | --------------------------------- |
| `spp_service_points.service_point_users` | Users operating at service points |

### Record Rules

Access rules ensure users can only view and manage service points within their authorized scope based on area assignments.

## Technical Details

### Application Module

This module is marked as an Odoo application (`application: True`), meaning it appears in the Apps menu and can be installed independently.

### Registrant Service Point Computation

When a registrant's parent (group/household) changes, the system automatically recomputes their service point associations based on the new parent's linked service points.
