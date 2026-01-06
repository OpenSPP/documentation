---
openspp:
  doc_status: draft
---

# DRIMS Architecture

This guide helps **developers** understand how DRIMS fits together so they can extend it effectively.

## When You Need This

Use this guide if you need to:
- Add custom fields to DRIMS models
- Create new alert types
- Extend approval workflows
- Integrate DRIMS with external systems
- Build country-specific extensions

**If you just need to configure DRIMS** (warehouses, alerts, approvals), see {doc}`/config_guide/drims/index` instead. Most customization doesn't require code.

## Mental Model

DRIMS manages disaster relief through five interconnected workflows, all tied to a specific disaster incident:

```{mermaid}
graph TB
    subgraph "Disaster Response"
        INC[Incident]
    end

    subgraph "Supply Chain"
        DON[Donations] --> WH[Warehouse Stock]
        WH --> DSP[Dispatches]
        DSP --> RET[Returns]
        RET --> WH
    end

    subgraph "Coordination"
        REQ[Requests] --> DSP
        ALR[Alerts] -.-> WH
        ALR -.-> REQ
    end

    INC --> DON
    INC --> REQ
    INC --> ALR
```

**Key concepts:**

1. **Everything links to an Incident** - Donations, requests, dispatches, and alerts all reference a specific disaster event
2. **Requests drive dispatches** - Field staff submit requests, approvers approve, warehouses fulfill
3. **Alerts monitor health** - Automated checks flag low stock, SLA breaches, and expiring items
4. **Stock flows through Odoo** - DRIMS extends `stock.picking` and `stock.warehouse`, not replaces them

## Core Entities

DRIMS introduces these models (all prefixed `spp.drims.*`):

| Model | Purpose | Source |
|-------|---------|--------|
| `donation` | Track incoming relief supplies | {gh-drims}`models/drims_donation.py` |
| `request` | Field requests for relief supplies | {gh-drims}`models/drims_request.py` |
| `return` | Items returned from distribution | {gh-drims}`models/drims_return.py` |
| `alert` | Automated monitoring alerts | {gh-drims}`models/drims_alert.py` |
| `personnel` | Deployed staff tracking | {gh-drims}`models/drims_personnel.py` |

DRIMS also extends these existing models:

| Model | Extensions Added | Source |
|-------|------------------|--------|
| `spp.hazard.incident` | KPI fields, relationships | {gh-drims}`models/hazard_incident.py` |
| `stock.warehouse` | DRIMS flags, tier, area | {gh-drims}`models/stock_warehouse.py` |
| `stock.picking` | Incident, POD, beneficiaries | {gh-drims}`models/stock_picking.py` |
| `res.users` | Area/warehouse assignments | {gh-drims}`models/res_users.py` |

## Workflows

### Donation Flow

```{mermaid}
stateDiagram-v2
    [*] --> announced
    announced --> received: Mark Received
    announced --> cancelled: Cancel
    received --> inspected: Inspect
    received --> cancelled: Cancel
    inspected --> stocked: Stock
    inspected --> rejected: Reject
    stocked --> [*]
    cancelled --> [*]
    rejected --> [*]
```

Donations create `stock.picking` records of type `donation_receipt` when stocked.

### Request & Approval Flow

Requests use `spp.approval.mixin` for approval state, plus a separate fulfillment state:

```{mermaid}
stateDiagram-v2
    state "Approval" as approval {
        [*] --> draft
        draft --> pending: Submit
        pending --> approved: Approve
        pending --> rejected: Reject
        pending --> revision: Request changes
        revision --> pending: Re-submit
    }

    state "Fulfillment" as fulfillment {
        approved --> allocated: Assign warehouse
        allocated --> dispatched: Ship items
        dispatched --> delivered: Confirm POD
    }
```

**Key insight:** Approval and fulfillment are tracked separately. A request can be approved but not yet dispatched.

### Dispatch Flow

Dispatches are `stock.picking` records with `drims_type='request_dispatch'`. DRIMS adds:
- `date_departed` / `date_arrived` for transit tracking
- {term}`POD` ({term}`Proof of Delivery`) fields for confirmation
- `beneficiary_count` for reporting

## Extension Patterns

### Adding Fields to DRIMS Models

Use standard Odoo inheritance:

```python
from odoo import models, fields

class DrimsRequestExtension(models.Model):
    _inherit = "spp.drims.request"

    local_approval_required = fields.Boolean(
        string="Requires Local Approval",
        help="Check if this request needs local government sign-off"
    )
```

### Creating Custom Alert Types

1. Add a vocabulary code for your alert type
2. Implement a check method
3. Register a cron job

See {doc}`extending` for complete examples with tests.

### Adding KPIs to Incidents

Extend `spp.hazard.incident` with computed fields:

```python
class HazardIncidentKPI(models.Model):
    _inherit = "spp.hazard.incident"

    avg_response_hours = fields.Float(
        compute="_compute_avg_response_hours",
        store=True,
    )

    @api.depends("drims_request_ids.picking_ids.date_departed")
    def _compute_avg_response_hours(self):
        # Calculate average time from request to first dispatch
        ...
```

## Module Dependencies

```{mermaid}
graph LR
    subgraph "Required"
        HAZ[spp_hazard]
        AREA[spp_area]
        VOC[spp_vocabulary]
        APR[spp_approval]
        STOCK[stock]
    end

    subgraph "Optional"
        SVC[spp_service_points]
        CEL[spp_cel_domain]
    end

    DRIMS[spp_drims]

    HAZ --> DRIMS
    AREA --> DRIMS
    VOC --> DRIMS
    APR --> DRIMS
    STOCK --> DRIMS
    SVC -.-> DRIMS
    CEL -.-> DRIMS
```

Key dependencies:
- **spp_hazard** - Provides incident model that DRIMS extends
- **spp_area** - Geographic hierarchy for request destinations and user scoping
- **spp_vocabulary** - Controlled vocabularies for priorities, donor types, clusters
- **spp_approval** - Approval workflow mixin used by requests
- **stock** - Odoo's inventory system, extended for DRIMS operations

## Security Model

DRIMS uses `spp_security` patterns:

| Group | Access |
|-------|--------|
| DRIMS Viewer | Read all |
| DRIMS Field Officer | Create requests, confirm deliveries (scoped by area) |
| DRIMS Warehouse Staff | Manage inventory, process donations/dispatches (scoped by warehouse) |
| DRIMS Request Approver | Approve/reject requests |
| DRIMS Manager | Full access |

Access is scoped by:
- **Geographic area** - Users see only requests/dispatches for their assigned areas
- **Warehouse** - Warehouse staff see only their assigned warehouses

Record rules use `drims_area_ids` and `drims_warehouse_ids` on `res.users`.

## Source Files

| Area | Path |
|------|------|
| Models | {gh-drims}`models/` |
| Security | {gh-drims}`security/` |
| Vocabularies | {gh-drims}`data/` |
| Views | {gh-drims}`views/` |

## See Also

- {doc}`extending` - Step-by-step extension examples with tests
- {doc}`/config_guide/drims/index` - Configuration without code
- {gh-drims}`README.md` - Module overview
