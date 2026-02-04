---
openspp:
  doc_status: draft
---

# Hide Menus Base

**Module:** `spp_hide_menus_base`

## Overview

The Hide Menus Base module allows administrators to control the visibility of navigation menus in OpenSPP. This streamlines the user interface by hiding non-essential menus for specific user groups, reducing complexity and focusing users on relevant functionality.

## Purpose

This module is designed to:

- **Simplify navigation:** Hide menus that are not relevant to specific user roles
- **Reduce interface clutter:** Remove non-OpenSPP menus from the navigation for focused workflows
- **Maintain flexibility:** Allow administrators to show or hide menus as needed
- **Support extensibility:** Provide a foundation for other modules to control menu visibility

## Module Dependencies

| Dependency       | Description                            |
| ---------------- | -------------------------------------- |
| **base**         | Odoo core menu system                  |
| **spp_security** | OpenSPP security groups and privileges |

## Key Features

### Menu Visibility Configuration

Administrators can configure which menus are visible or hidden:

| Field          | Description                                      |
| -------------- | ------------------------------------------------ |
| Menu           | The Odoo menu item to control                    |
| State          | Show or Hidden                                   |
| Default Groups | Original security groups (preserved when hiding) |
| XML ID         | Technical identifier for the menu                |

### Hide and Show Operations

The module provides two main operations:

**Hide Menu:**

1. Stores the menu's current group assignments
2. Replaces groups with the "Hide Menus User" group
3. Updates state to "Hidden"

**Show Menu:**

1. Restores the original group assignments
2. Updates state to "Show"

### Security Group

| Group           | Description                              |
| --------------- | ---------------------------------------- |
| Hide Menus User | Users in this group can see hidden menus |

By default, only users explicitly added to this group will see menus that have been hidden.

### Non-Destructive Changes

Menu visibility changes are reversible:

- Original group assignments are preserved
- Showing a hidden menu restores original permissions
- No menu records are deleted

## Integration

The Hide Menus Base module integrates with:

- **ir.ui.menu:** Modifies Odoo's core menu visibility through group assignments
- **spp_security:** Works within OpenSPP's security framework
- **Other hide_menus modules:** Provides the base infrastructure for domain-specific menu hiding
