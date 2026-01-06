---
openspp:
  doc_status: draft
---

# DRIMS Developer Guide

This guide is for **Python developers** extending DRIMS with custom code. If you're configuring DRIMS through the UI (eligibility rules, workflows, vocabularies), see the implementer guide instead.

## When to Use This Guide

DRIMS is designed to be configured without code for most use cases. Use this guide when you need to:

- **Create custom models** - New entities beyond donations, requests, and alerts
- **Add computed fields** - Complex calculations that can't be done with CEL expressions
- **Implement custom workflows** - State transitions beyond the standard approval flow
- **Integrate external systems** - API endpoints, webhooks, or data synchronization
- **Extend existing models** - Add fields or methods to core DRIMS models
- **Create custom alert types** - Monitoring logic beyond stock levels and SLAs
- **Build country-specific modules** - Localized extensions like `spp_drims_sl`

**The 80/20 rule:** If you can configure it through Settings, Studio, or the UI, you should. This guide covers the 20% of cases that require code.

## Prerequisites

Before extending DRIMS, you should understand:

- **Python 3.11+** - DRIMS runs on Python 3.11
- **Odoo basics** - Model inheritance, field types, ORM methods
- **Git workflows** - Branching, committing, pull requests
- **OpenSPP architecture** - Read the [OpenSPP Developer Guide](../../index.md) first
- **DRIMS concepts** - Understand donations, requests, dispatches from the user guide

You'll also need a working development environment. See {doc}`/howto/developer_guides/development_setup` for setup instructions.

## Module Overview

DRIMS (`spp_drims`) is structured following OpenSPP conventions:

```
spp_drims/
├── models/                    # Core business logic
│   ├── donation.py           # Donation management
│   ├── request.py            # Relief requests with approval workflow
│   ├── alert.py              # Automated monitoring alerts
│   ├── personnel.py          # Personnel directory
│   ├── returns.py            # Return handling
│   ├── stock_picking.py      # Dispatch extensions (extends Odoo stock)
│   └── stock_warehouse.py    # Warehouse extensions (extends Odoo stock)
├── wizard/                    # Transient models for operations
│   ├── bulk_approve_wizard.py
│   └── report_4w_wizard.py
├── views/                     # UI definitions (XML)
├── data/                      # Master data and configuration
│   ├── vocabulary_*.xml      # Controlled vocabularies
│   ├── ir_cron.xml           # Scheduled jobs (alert checks)
│   └── audit_rules.xml       # Audit trail configuration
├── security/                  # Access control
│   ├── groups.xml            # Security groups
│   ├── ir.model.access.csv   # Model-level permissions
│   └── rules.xml             # Record-level rules
└── docs/                      # Technical documentation
```

## Key Models

DRIMS defines these core models:

| Model | Purpose | Key Features |
|-------|---------|--------------|
| `spp.drims.donation` | Track incoming relief supplies | Multi-state workflow, lot tracking, donor management |
| `spp.drims.request` | Relief supply requests | Approval workflow, multi-tier, SLA monitoring |
| `spp.drims.alert` | Automated monitoring | Stock levels, expiry dates, SLA breaches |
| `spp.drims.personnel` | Personnel directory | Deployment tracking, role-based filtering |
| `spp.drims.return` | Return handling | Damage tracking, restocking workflow |

DRIMS also **extends** these Odoo/OpenSPP models:

| Model | Extensions |
|-------|-----------|
| `stock.warehouse` | DRIMS flag, tier classification, health indicators |
| `stock.picking` | Transaction types, incident linking, proof of delivery |
| `spp.hazard.incident` | DRIMS KPIs (stock value, beneficiaries served) |
| `res.users` | Area/warehouse assignments for security |

For the complete data model with relationships, see the [Architecture](architecture.md) page.

## Module Dependencies

DRIMS integrates with multiple OpenSPP and Odoo modules:

```{mermaid}
graph TD
    subgraph "Core Odoo"
        BASE[base]
        MAIL[mail]
        STOCK[stock]
    end

    subgraph "OpenSPP Core"
        SEC[spp_security]
        VOC[spp_vocabulary]
        AREA[spp_area]
        AUD[spp_audit]
        APR[spp_approval]
        ALR[spp_alerts]
        CEL[spp_cel_domain]
        SVC[spp_service_points]
    end

    subgraph "Domain Modules"
        HAZ[spp_hazard]
        DRIMS[spp_drims]
    end

    subgraph "Country Extensions"
        SL[spp_drims_sl]
        DEMO[spp_drims_sl_demo]
    end

    BASE --> DRIMS
    MAIL --> DRIMS
    STOCK --> DRIMS
    SEC --> DRIMS
    VOC --> DRIMS
    AREA --> DRIMS
    AUD --> DRIMS
    APR --> DRIMS
    ALR --> DRIMS
    CEL --> DRIMS
    SVC --> DRIMS
    HAZ --> DRIMS
    DRIMS --> SL
    SL --> DEMO
```

**Key dependencies:**
- **`stock`** (Odoo) - Warehouse, picking, quant, lot management
- **`spp_hazard`** - Disaster incident management
- **`spp_approval`** - Approval workflow mixin for requests
- **`spp_vocabulary`** - Controlled vocabularies (18+ namespaces)
- **`spp_area`** - Geographic hierarchy for security and routing

## Extension Points

DRIMS is designed to be extended. Common extension patterns:

### 1. Add Fields to Existing Models

Extend models using Odoo inheritance:

```python
from odoo import models, fields

class DrimsRequestExtension(models.Model):
    _inherit = "spp.drims.request"

    custom_priority_score = fields.Integer(
        string="Priority Score",
        compute="_compute_priority_score",
    )

    def _compute_priority_score(self):
        for request in self:
            # Your custom logic
            request.custom_priority_score = ...
```

### 2. Create Custom Alert Types

Add vocabulary codes and implement cron methods:

```python
class DrimsAlert(models.Model):
    _inherit = "spp.drims.alert"

    def _cron_check_custom_alerts(self):
        """Scheduled job to generate custom alerts."""
        # Your monitoring logic
        self._create_alert_if_needed(...)
```

### 3. Customize Approval Rules

Use CEL expressions in `spp_approval` for dynamic approval routing:

```python
# Approval rules based on request value
request.total_value > 10000  # Route to senior approver
```

### 4. Build Country Modules

Create country-specific extensions like `spp_drims_sl`:

- Custom area hierarchies
- Localized vocabularies
- Country-specific warehouses and partners
- Demo data generators

### 5. Integrate External Systems

Use Odoo's API for integration:

- **XML-RPC / JSON-RPC** - Standard Odoo API
- **REST endpoints** - Custom controllers
- **Webhooks** - `mail.thread` notifications

For detailed patterns and complete examples, see [Extending DRIMS](extending.md).

## What You'll Find Here

This section contains:

```{toctree}
:maxdepth: 2
:hidden:

architecture
extending
```

- **[Architecture](architecture.md)** - Data model, workflows, and technical design
- **[Extending DRIMS](extending.md)** - Patterns for common customizations

## See Also

- [DRIMS User Guide](../../user_guide/drims/index.md) - How to use DRIMS
- [DRIMS Implementer Guide](../../implementer_guide/drims/index.md) - How to configure DRIMS
- [OpenSPP Developer Guide](../../index.md) - OpenSPP development principles
- [spp_drims README](https://github.com/openspp/openspp-modules-v2/tree/main/spp_drims) - Module repository
