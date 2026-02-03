---
openspp:
  doc_status: draft
---

# User Roles


## Overview

The OpenSPP User Roles module extends the standard Odoo role-based access control with area-based permissions. It enables organizations to define global and local roles, where local roles can restrict user access to specific geographical areas within the system.

## Purpose

This module is designed to:

- **Implement area-based access control:** Restrict users to specific geographical regions using the `spp_area` module integration
- **Categorize roles:** Distinguish between global roles (system-wide access) and local roles (area-restricted access)
- **Automate permission management:** Automatically assign underlying system groups based on role assignments
- **Simplify role administration:** Provide a centralized interface for managing user roles and their associated permissions

## Module Dependencies

| Dependency         | Description                                |
| ------------------ | ------------------------------------------ |
| **base**           | Core Odoo framework                        |
| **mail**           | Messaging and notification support         |
| **spp_registry**   | OpenSPP registry for registrant management |
| **base_user_role** | Base user role management from OCA         |
| **spp_security**   | OpenSPP security framework                 |

## Key Features

### Role Types

The module introduces a role type classification:

| Role Type  | Description                                                       |
| ---------- | ----------------------------------------------------------------- |
| **Global** | System-wide access without geographical restrictions              |
| **Local**  | Access restricted to specific areas defined in the area hierarchy |

### Stored Role Display

The module provides a stored `role_ids_stored` field that enables displaying user roles in list views, addressing a limitation of the base module's computed field.

### Protected Groups

When synchronizing user groups from roles, the module protects essential system groups from accidental removal:

- `base.group_user` - Internal User
- `base.group_no_one` - Technical Features
- `mail.group_mail_template_editor` - Mail Template Editor
- `base.group_portal` - Portal
- `base.group_public` - Public

### Default Role Lines

New users can automatically inherit role configurations from a template user, ensuring consistent baseline permissions across the organization.

## Integration

### With spp_area

Local roles leverage the area hierarchy to restrict user access to specific geographical regions. When a user has a local role, their access is filtered based on their assigned areas.

### With spp_registry

The module integrates with the registry to enable area-based filtering of registrant data, ensuring users only see registrants within their authorized geographical scope.

### With base_user_role

Extends the OCA base_user_role module to add:

- Role type classification (global/local)
- Bulk role update actions
- Protected group handling during synchronization

## Configuration

### Creating a New Role

| Field     | Description                                   |
| --------- | --------------------------------------------- |
| Name      | Display name for the role                     |
| Role Type | Select "Global" or "Local"                    |
| Groups    | Odoo security groups to assign with this role |
| Users     | Users who have this role assigned             |

### Assigning Roles to Users

Roles are assigned through role lines on the user record:

| Field      | Description                            |
| ---------- | -------------------------------------- |
| Role       | The role to assign                     |
| Date From  | Optional start date for the assignment |
| Date To    | Optional end date for the assignment   |
| Is Enabled | Toggle to enable/disable the role line |

## Technical Details

### Auto-Install Behavior

This module auto-installs when both `spp_registry` and `base_user_role` are installed, ensuring role management is available whenever the registry is in use.

### Scheduled Actions

The module includes scheduled actions (cron jobs) for maintaining role synchronization across users.
