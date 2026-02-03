---
openspp:
  doc_status: draft
---

# Base (Common)


## Overview

OpenSPP Base (Common) is the foundational module that all implementation-specific configurations depend on. It provides the main navigation menu, generic system configuration, and integrates core components like user role management and area management into a unified OpenSPP experience.

## Purpose

This module is designed to:

- **Provide the main menu structure:** Establishes the primary OpenSPP navigation menu that users see after logging in.
- **Unify core components:** Integrates registry, security, user roles, and area management into a cohesive platform.
- **Hide non-OpenSPP menus:** Streamlines the user interface by hiding standard Odoo menus that are not relevant to social protection workflows.
- **Define global and local roles:** Establishes the role-based access framework used throughout the platform.
- **Apply visual theming:** Provides OpenSPP-specific styling for the Odoo 19 Community Edition interface.

## Module Dependencies

| Dependency            | Purpose                                                          |
| --------------------- | ---------------------------------------------------------------- |
| `base`                | Odoo core framework                                              |
| `spp_user_roles`      | Role-based access control with global and local role definitions |
| `spp_hide_menus_base` | Menu visibility management for cleaner UI                        |
| `spp_base_setting`    | Country office and organizational configuration                  |
| `spp_registry`        | Core beneficiary and group registry                              |
| `spp_security`        | Central security group and privilege definitions                 |

## Key Features

### Main Menu Integration

The module creates the primary OpenSPP menu structure that organizes all platform functionality:

- Registry access (Individuals and Groups)
- Programs and entitlements
- Configuration and settings
- Administration tools

### Role-Based Access

Defines two categories of user roles:

| Role Type        | Scope                  | Use Case                                 |
| ---------------- | ---------------------- | ---------------------------------------- |
| **Global Roles** | System-wide access     | Administrators, central program managers |
| **Local Roles**  | Area-restricted access | Field officers, regional coordinators    |

### UI Customization

Includes custom styling for:

- Navigation bar appearance
- Color schemes (light and dark mode support)
- OpenSPP branding elements

## Integration

### With Other Modules

As the common base, this module is automatically installed when using any OpenSPP implementation module. It ensures:

- Consistent menu structure across all modules
- Unified security model
- Standard look and feel

### Implementation Pattern

Implementation-specific modules (e.g., for a specific country deployment) should depend on `spp_base_common` rather than individual core modules:

```python
"depends": [
    "spp_base_common",
    # Implementation-specific dependencies
]
```

## Technical Details

| Property       | Value                      |
| -------------- | -------------------------- |
| Technical Name | `spp_base_common`          |
| Category       | OpenSPP/Core               |
| Version        | 19.0.1.3.0                 |
| License        | LGPL-3                     |
| Application    | No (infrastructure module) |

## See Also

- {doc}`spp_security` - Security definitions used by this module
- {doc}`spp_registry` - Registry functionality integrated here
- {doc}`spp_base_setting` - Configuration settings this module depends on
