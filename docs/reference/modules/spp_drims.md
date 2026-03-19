---
openspp:
  doc_status: draft
---

# DRIMS - Disaster Response Inventory Management

**Module:** `spp_drims`

## Overview

Disaster relief inventory management for donations, requests, and distribution tracking. Links to hazard incidents with multi-tier approval workflows and warehouse operations.

## Purpose

This module is designed to:

- **Track donations:** Record in-kind donations linked to hazard incidents with a state machine (announced, received, inspected, stocked) and state transition validation.
- **Manage relief requests:** Submit, approve, allocate, and dispatch supply requests with FIFO stock allocation, SLA tracking, and fulfillment progress monitoring.
- **Coordinate warehouse operations:** Extend Odoo stock warehouses with DRIMS-specific fields for disaster relief, including incident linkage, GIS location, coverage areas, and stock health indicators.
- **Monitor alerts:** Automated scheduled checks for low stock, expiring inventory, and SLA breaches with urgency-based styling and team assignment.
- **Track returns:** Manage returned items from distribution points with condition tracking, disposition decisions (restock, repair, dispose), and restocking workflows.
- **Deploy personnel:** Track field staff, volunteers, and team members deployed across areas with roles, organizations, and cluster assignments.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `base` | Odoo core framework |
| `mail` | Communication and activity tracking |
| `stock` | Inventory and warehouse management |
| `spp_alerts` | Generic alert engine for threshold monitoring, expiry tra... |
| `spp_security` | Central security definitions for OpenSPP modules |
| `spp_vocabulary` | OpenSPP: Vocabulary |
| `spp_area` | Establishes direct associations between OpenSPP registran... |
| `spp_hazard` | Provides hazard classification, incident recording, and i... |
| `spp_gis` | GIS core plus area geo fields and importer extensions (po... |
| `spp_gis_report` | Geographic visualization and reporting for social protect... |
| `spp_service_points` | The OpenSPP Service Points module manages physical or vir... |
| `spp_approval` | Standardized approval workflows with multi-tier sequencin... |
| `spp_cel_domain` | Write simple CEL-like expressions to filter records (Open... |
| `spp_audit` | Comprehensively tracks all data modifications and user ac... |
| `job_worker` | Background job worker |

## Key Features

### Donation Management

Donations (`spp.drims.donation`) follow a strict state machine with validated transitions:

| State | Description |
| --- | --- |
| Announced | Donation pledged by donor |
| Received | Items physically received at warehouse, stock picking created |
| Inspected | Quality inspection completed (via inspection wizard with condition/disposition per item) |
| Stocked | Items put away into warehouse inventory, stock picking validated |
| Cancelled / Rejected | Terminal states, pending pickings are cancelled |

Donations track donor type, restrictions, and line items with pledged vs. received quantities.

### Request Workflow

Requests (`spp.drims.request`) go through approval and fulfillment stages:

- **Submission:** Validates request has items, triggers approval workflow
- **Approval:** Multi-tier approval via `spp_approval` mixin, with reject and request-revision actions
- **Allocation:** FIFO stock allocation with preview wizard showing availability before committing
- **Dispatch:** Creates outgoing stock pickings with move lines per allocated item
- **Fulfillment tracking:** Computes allocation %, fulfillment %, and quantity progress per line

### SLA Monitoring

Requests include configurable SLA tracking based on priority level:

| Priority | Default SLA Hours |
| --- | --- |
| Critical | 4 |
| High | 8 |
| Routine | 24 |
| Low | 48 |

SLA status (on time, warning, breached) is computed and stored for dashboard filtering. Thresholds are configurable via system parameters.

### Alert Engine

The DRIMS alert model (`spp.drims.alert`) extends the base alert system with scheduled cron jobs:

| Alert Type | Trigger |
| --- | --- |
| Low Stock | Available stock falls below 50% of needed quantity |
| Expiry | Lot expiration date within 30 days (requires `product_expiry`) |
| SLA Breach | Request past its needed date and not delivered |
| SLA Warning | Request within 2 days of deadline and not dispatched |

Alerts include urgency states (overdue, urgent, soon, normal), team assignment, and navigation links to related records.

### Request Templates

Reusable templates (`spp.drims.request.template`) allow creating pre-configured request item lists. Templates can be personal or shared across users, and a wizard enables creating requests from templates with incident and area selection.

### Incident Dashboard KPIs

The module extends hazard incidents with computed KPIs using a hybrid caching strategy via `spp.data.value`:

| KPI | Description |
| --- | --- |
| Donation count / value | Total donations and their monetary value |
| Request count / pending | Total and pending approval requests |
| Stock value / units / items | Current warehouse inventory metrics |
| Distributed value | Value of completed dispatch pickings |
| Beneficiaries served | Count from completed dispatches in last 30 days |
| Active / critical alerts | Alert counts by state and priority |
| Return count / value | Item returns and their value |

### Personnel Tracking

Deployed personnel (`spp.drims.personnel`) are tracked with deployment area, organization, role, cluster assignment, and status (deployed, standby, on leave, returned). Days deployed is computed automatically.

## Integration

- **stock:** Creates incoming pickings for donation receipts, outgoing pickings for request dispatches, and incoming pickings for returns. Extends `stock.warehouse` with DRIMS configuration fields.
- **spp_hazard:** Extends `spp.hazard.incident` with donation/request/alert/return KPIs, warehouse linkage, coordination modes, and alert threshold overrides.
- **spp_approval:** Requests use the approval mixin for multi-tier approval workflows with configurable approval definitions.
- **spp_alerts:** DRIMS alerts inherit from `spp.alert` and add incident, warehouse, product, and request context.
- **spp_gis / spp_gis_report:** Warehouses have GIS point locations; GIS reports support DRIMS request and incident area data sources.
- **spp_vocabulary:** All states, types, priorities, donor types, and other classifiers are vocabulary-driven for extensibility.
- **spp_audit:** Audit rules track changes to DRIMS records.
- **spp_service_points:** Requests can specify service points as distribution locations.

```{toctree}
:maxdepth: 1
:hidden:

spp_drims_sl
spp_drims_sl_demo
```
