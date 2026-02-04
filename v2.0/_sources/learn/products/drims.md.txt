---
openspp:
  doc_status: draft
  products: [core]
---

# DRIMS - Disaster Response Inventory Management

DRIMS is OpenSPP's disaster relief inventory management system. It manages the complete lifecycle of emergency supplies—from donation pledges through warehouse storage to distribution and returns—enabling humanitarian organizations and government agencies to coordinate disaster response operations.

**Who is this for:** Humanitarian organizations, government disaster response agencies, UN clusters, and implementing partners coordinating emergency relief operations.

## What DRIMS does

When a disaster strikes, relief supplies flow in from multiple donors and must reach affected populations quickly. DRIMS provides:

- **Donation tracking** from pledge announcement through warehouse receipt
- **Multi-tier request approval** for relief supplies from field locations
- **Dispatch management** with {term}`Waybill` generation and {term}`Proof of Delivery`
- **Real-time inventory visibility** across central, regional, and mobile warehouses
- **Stock health monitoring** with automated alerts for low stock and expiring items
- **{term}`OCHA` {term}`Cluster` coordination** for multi-agency humanitarian response

## Core workflows

DRIMS manages four interconnected workflows:

| Workflow | Purpose | Key users |
|----------|---------|-----------|
| **Donations** | Track pledged and received supplies from UN agencies, NGOs, governments, and private donors | Warehouse Staff |
| **Requests** | Submit and approve relief supply requests from distribution points and field teams | Field Officers, Approvers |
| **Dispatches** | Pick, pack, and deliver supplies with waybill documentation | Warehouse Staff, Logistics |
| **Returns** | Process damaged, expired, or excess items returned from the field | Warehouse Staff |

All operations are linked to specific **disaster incidents** to maintain clear accountability and enable incident-specific reporting.

## OCHA cluster integration

DRIMS implements the standard [OCHA/{term}`IASC` humanitarian cluster system](https://www.humanitarianresponse.info/en/coordination/clusters) for coordinated disaster response:

| Cluster | Example supplies |
|---------|------------------|
| Food security | Rice, fortified foods, agricultural inputs |
| Health | Medical kits, vaccines, PPE |
| WASH | Water purification tablets, jerry cans, hygiene kits |
| Shelter | Tents, tarpaulins, blankets, tools |
| Nutrition | Therapeutic foods, supplements |
| Protection | Safety supplies, dignity kits |
| Education | School supplies, temporary classroom kits |

Each request and deployed personnel can be tagged with a cluster, enabling:
- Sector-specific reporting to cluster leads
- Gap identification across humanitarian sectors
- **{term}`4W Report`s** (Who does What, Where, When) for coordination meetings

## Key capabilities

### Inventory management

- **Multi-warehouse support** - Central, regional, and mobile warehouses
- **Lot tracking** - Batch numbers and expiry dates for perishables
- **Stock health indicators** - Visual status (critical/warning/good) based on thresholds
- **Real-time dashboard** - Stock levels, values, and distribution metrics

### Alerts and monitoring

- **Low stock alerts** - Automatic detection when inventory falls below thresholds
- **SLA monitoring** - Track request fulfillment against delivery deadlines
- **Expiry alerts** - Warnings for items approaching expiration dates
- **Activity feed** - Real-time audit trail of all DRIMS operations

### Coordination

DRIMS supports multiple coordination modes for disaster response:

| Mode | Description | Use case |
|------|-------------|----------|
| {term}`Lead Agency` | Single agency coordinates all partners | Government-led national response |
| Cluster system | UN-led sector coordination | Large-scale humanitarian emergencies |
| Consortium | NGO-led partner coordination | Multi-NGO regional response |
| Bilateral | Direct agency-to-agency | Focused bilateral assistance |

### Personnel Directory

Track deployed disaster response staff by:
- **Role** - Field Coordinator, Warehouse Manager, Logistics Officer
- **Humanitarian cluster** assignment
- **Organization** and organization role (lead, {term}`Implementing Partner`, {term}`Funding Partner`, {term}`Technical Partner`)
- **Location** and incident assignment

## Quick Start Guides

**For government staff and field workers:**
- {doc}`/user_guide/drims/donations` - How to process incoming donations
- {doc}`/user_guide/drims/requests` - Submit relief supply requests
- {doc}`/user_guide/drims/dispatches` - Pick and dispatch supplies
- {doc}`/user_guide/drims/dashboard` - Monitor operations and alerts

**For implementers configuring DRIMS:**
- {doc}`/config_guide/drims/warehouses` - Configure warehouses and stock thresholds
- {doc}`/config_guide/drims/approval_chains` - Set up multi-tier request approval
- {doc}`/config_guide/drims/alerts` - Configure low stock and expiry alerts

## How it works

```{mermaid}
graph LR
    A[Donation<br/>Announced] --> B[Donation<br/>Received]
    B --> C[Warehouse<br/>Stock]
    D[Field Request<br/>Submitted] --> E[Request<br/>Approved]
    E --> F[Dispatch<br/>Created]
    C --> F
    F --> G[Supplies<br/>Delivered]
    G --> H[Beneficiaries<br/>Served]
    G -.-> I[Returns<br/>Processed]
    I --> C
```

1. **Donors announce pledges** - UN agencies, NGOs, governments, or private donors commit supplies
2. **Donations received** - Warehouse staff inspect and stock items with lot/expiry tracking
3. **Field teams request supplies** - Distribution points submit requests for specific items and quantities
4. **Approval workflow** - Multi-tier approval based on request value and priority
5. **Warehouse dispatch** - Picking operations with waybill generation
6. **Proof of delivery** - Field confirmation of receipt
7. **Returns processing** - Handle damaged, expired, or excess items

## Security and access control

DRIMS includes role-based access control:

| Role | Access level | Typical users |
|------|--------------|---------------|
| DRIMS Viewer | Read-only access to all data | Coordination staff, donors |
| Field Officer | Create requests, confirm deliveries | Distribution point managers |
| Warehouse Staff | Manage inventory, process donations/dispatches | Warehouse managers, stock clerks |
| Request Approver | Approve/reject supply requests | Program managers, cluster leads |
| District Coordinator | Coordinate within assigned districts | District disaster management officers |
| DRIMS Manager | Full administration and configuration | DRIMS system administrators |

## Dependencies

DRIMS integrates with other OpenSPP modules:

- **spp_hazard** - Disaster incident management
- **spp_area** - Geographic area hierarchy for location tracking
- **spp_approval** - Multi-tier approval workflow engine
- **spp_alerts** - Alert management and notifications
- **spp_audit** - Complete audit trail of operations

## Next steps

**New to DRIMS?** Start with the user guides:
- {doc}`/user_guide/drims/index` - DRIMS user guide overview

**Setting up DRIMS for your organization?** See the implementer guides:
- {doc}`/config_guide/drims/index` - Configuration overview
- {doc}`/config_guide/drims/warehouses` - Configure warehouses and locations

**Questions?**
- {doc}`/reference/glossary/humanitarian` - DRIMS terminology and humanitarian terms

## Learn more

- [OCHA Cluster Coordination](https://www.humanitarianresponse.info/en/coordination/clusters) - UN cluster approach
- [4W Reporting Guidelines](https://www.humanitarianresponse.info/en/applications/tools/category/4w-who-does-what-where-when) - Humanitarian reporting standards
- [IASC Reference Module](https://interagencystandingcommittee.org/iasc-transformative-agenda/iasc-reference-module-cluster-coordination-country-level-revised-july-2015) - Cluster coordination at country level
