---
openspp:
  doc_status: draft
---

# Security

**Module:** `spp_security`

## Overview

OpenSPP Security provides the central security definitions for all OpenSPP modules. It establishes the foundational security groups, privileges, and module categories that other modules build upon. This module ensures consistent access control across the entire platform.

## Purpose

This module is designed to:

- **Define security categories:** Organize security groups into logical domains (Registry, Programs, Payments, etc.).
- **Establish the administrator group:** Create the central admin group that inherits all domain-level manager permissions.
- **Provide the privilege framework:** Define the Odoo 19 privilege structure for clean user settings UI.
- **Enable modular security:** Allow domain modules to define their own groups that automatically integrate with the central admin.

## Module Dependencies

| Dependency | Purpose                                         |
| ---------- | ----------------------------------------------- |
| `base`     | Odoo core framework and security infrastructure |

## Key Features

### Security Categories

The module defines categories that organize security groups in the user settings interface:

| Category             | Description                               | Sequence |
| -------------------- | ----------------------------------------- | -------- |
| Administration       | System administration and configuration   | 1        |
| Registry             | Beneficiary and group registry management | 10       |
| Programs             | Program and cycle management              | 20       |
| Scoring              | Scoring and assessment framework          | 25       |
| Entitlements         | Entitlement management and processing     | 30       |
| Change Requests      | Change request workflow management        | 40       |
| Approvals            | Approval workflow management              | 50       |
| Payments             | Payment processing and disbursement       | 60       |
| Grievance Management | Grievance/ticket management               | 70       |
| Areas and GIS        | Geographic area and GIS management        | 100      |
| API Access           | API and external integration access       | 120      |
| Audit and Compliance | Audit logging and compliance management   | 130      |

### Three-Tier Security Model

Each domain module implements a three-tier security structure:

| Level       | Group Name        | Permissions                                                       |
| ----------- | ----------------- | ----------------------------------------------------------------- |
| **Viewer**  | `group_*_viewer`  | Read-only access to domain records                                |
| **Officer** | `group_*_officer` | Create and update records (inherits Viewer)                       |
| **Manager** | `group_*_manager` | Full access including delete and configuration (inherits Officer) |

### Administrator Group

The central `group_spp_admin` automatically inherits all manager-level permissions from installed domain modules:

```
OpenSPP Administrator
    ├── Registry Manager (when spp_registry installed)
    ├── Programs Manager (when spp_programs installed)
    ├── Payments Manager (when spp_payments installed)
    └── [Other domain managers...]
```

Odoo system administrators (`base.group_system`) automatically receive OpenSPP admin access.

### Utility Groups

Special-purpose groups for specific access patterns:

| Group                 | Purpose                                                     |
| --------------------- | ----------------------------------------------------------- |
| Restricted: Self Only | Users can only see their own user record (for field agents) |

## Integration

### Domain Module Pattern

When a domain module is installed, it:

1. Defines its Viewer, Officer, and Manager groups
2. Links its Manager group to `group_spp_admin`
3. Defines record rules for data access

Example from a domain module:

```xml
<!-- Link domain manager to central admin -->
<record id="spp_security.group_spp_admin" model="res.groups">
    <field name="implied_ids" eval="[Command.link(ref('group_registry_manager'))]"/>
</record>
```

### With User Roles

The security groups integrate with `spp_user_roles` for:

- Role-based group assignment
- Area-based access restrictions
- Automated permission management

## Technical Details

| Property       | Value                      |
| -------------- | -------------------------- |
| Technical Name | `spp_security`             |
| Category       | OpenSPP/Core               |
| Version        | 19.0.1.0.0                 |
| License        | LGPL-3                     |
| Application    | No (infrastructure module) |
