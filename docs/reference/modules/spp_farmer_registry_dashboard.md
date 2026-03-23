---
openspp:
  doc_status: draft
---

# Dashboard

**Module:** `spp_farmer_registry_dashboard`

## Overview

Farmer registry dashboard with CEL-based metrics and trends

## Purpose

This module is designed to:

- **Display farmer registry metrics:** Provide pre-configured dashboard metrics for monitoring farmer registrations, farm types, land usage, and activity trends.
- **Leverage CEL-based computation:** Use CEL variables and the dashboard base framework to compute and display farmer-specific KPIs.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `spp_farmer_registry` | Farmer Registry with vocabulary-based fields, CEL variabl... |
| `spp_dashboard_base` |  |
| `spp_studio` | No-code customization interface for OpenSPP |
| `spreadsheet_dashboard` | Spreadsheet-based dashboards |
| `spp_security` | Central security definitions for OpenSPP modules |

## Key Features

### Dashboard Configuration

The module installs via XML data files:

- **Dashboard metrics:** Pre-defined metric definitions for farmer registry KPIs
- **Dashboards:** Spreadsheet-based dashboard layouts configured for the farmer registry context

This is a data-only module with no Python models of its own. All dashboard rendering and metric computation is handled by the `spp_dashboard_base` and `spreadsheet_dashboard` dependencies.

## Integration

- **spp_farmer_registry:** Reads farm data (registrants, activities, land records) to compute dashboard metrics.
- **spp_dashboard_base:** Provides the dashboard metric computation framework.
- **spp_studio:** Enables no-code configuration of additional dashboard metrics.
- **spreadsheet_dashboard:** Renders the dashboard using Odoo's spreadsheet dashboard framework.
