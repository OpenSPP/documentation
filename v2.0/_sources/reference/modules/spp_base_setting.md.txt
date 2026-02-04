---
openspp:
  doc_status: draft
---

# Base Settings

**Module:** `spp_base_setting`

## Overview

OpenSPP Base Settings provides fundamental configurations for country-specific implementations. It establishes core organizational structures such as Country Offices, enables tailored user interface adaptations, and streamlines user management by linking system users to specific organizational contexts.

## Purpose

This module is designed to:

- **Define Country Offices:** Establish organizational units that represent physical or administrative offices within a country deployment.
- **Enable context-aware access:** Link users to specific Country Offices for targeted data access and permissions.
- **Support multi-office deployments:** Allow a single OpenSPP installation to serve multiple organizational units with appropriate data segregation.
- **Customize UI per deployment:** Provide configuration options for adapting the interface to specific country requirements.

## Module Dependencies

| Dependency     | Purpose                                                |
| -------------- | ------------------------------------------------------ |
| `base`         | Odoo core framework                                    |
| `spp_security` | Security groups and access control definitions         |
| `spp_registry` | Registry model integration for user-registrant linking |

## Key Features

### Country Office Management

Country Offices serve as organizational anchors for:

| Function        | Description                                         |
| --------------- | --------------------------------------------------- |
| User Assignment | Link users to their operating office                |
| Data Scoping    | Restrict data visibility to office-relevant records |
| Reporting       | Group reports and statistics by office              |
| Configuration   | Apply office-specific settings                      |

### User-Office Linking

Each system user can be associated with a Country Office, which:

- Determines their default data context
- Influences which records they can view and modify
- Integrates with the area-based access control from `spp_user_roles`

### Configuration Options

The module provides settings for:

- Office hierarchy and relationships
- Default office assignment rules
- Office-specific customizations

## Integration

### With Registry

When users are linked to Country Offices, their access to registry records (individuals and groups) can be scoped accordingly. This works in conjunction with area-based access control.

### With User Roles

Country Office assignment complements the role system:

| Component       | Provides                                     |
| --------------- | -------------------------------------------- |
| User Roles      | Permission levels (Viewer, Officer, Manager) |
| Country Office  | Organizational context                       |
| Area Assignment | Geographic scope                             |

Together, these determine what a user can do and which data they can access.

### Configuration Flow

1. Create Country Offices representing your organizational structure
2. Assign users to their appropriate office
3. Configure area assignments for geographic access control
4. Apply role-based permissions for functionality access

## Technical Details

| Property       | Value                     |
| -------------- | ------------------------- |
| Technical Name | `spp_base_setting`        |
| Category       | OpenSPP/Core              |
| Version        | 19.0.1.3.1                |
| License        | LGPL-3                    |
| Application    | No (configuration module) |

## See Also

- {doc}`spp_security` - Security definitions for access control
- {doc}`spp_registry` - Registry records scoped by office
- {doc}`spp_area` - Geographic area management for location-based access
