---
openspp:
  doc_status: draft
---

# Indicator Studio

**Module:** `spp_indicator_studio`

## Overview

Studio UI for managing publishable indicators

## Purpose

This module is designed to:

- **Provide Studio UI for indicators:** Add list, form, kanban, and search views for managing publishable indicators within the OpenSPP Studio configuration interface.
- **Manage indicator categories:** Expose metric category management under the Studio settings menu.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `spp_indicator` | Publishable indicators based on CEL variables for dashboa... |
| `spp_studio` | No-code customization interface for OpenSPP |

## Key Features

### Indicator Management Views

Provides a complete set of views for managing indicators:

| View | Description |
| --- | --- |
| List | Sortable table showing name, label, variable, format, category, privacy settings, and publication toggles |
| Form | Full editor with sections for identity, data source, presentation, publication channels, privacy (k-anonymity), and context overrides |
| Kanban | Card view grouped by category, showing publication badges (GIS, Dashboard, API) |
| Search | Filters by publication channel, sensitive data flag, and archived status; grouping by category, format, or source type |

### Studio Menu Integration

Adds indicator management under the Studio configuration menu:

| Menu Item | Location |
| --- | --- |
| All Indicators | Studio > Settings > Indicators |
| Categories | Studio > Settings > Indicators > Categories |

Both menu items are restricted to users with the Studio Manager security group.

### Auto-Install Behavior

This is a bridge module that auto-installs when both `spp_indicator` and `spp_studio` are present. It contains no Python models of its own -- it provides only views, menus, and security access rules.

## Integration

- **spp_indicator:** Provides views and menu actions for the `spp.indicator` and `spp.indicator.context` models defined in this module.
- **spp_studio:** Registers indicator menus under the Studio configuration hierarchy, using the Studio Manager security group for access control.
- **spp_metric:** Exposes the `spp.metric.category` action for category management within the indicators menu.
