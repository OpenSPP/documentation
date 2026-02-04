---
orphan: true
openspp:
  doc_status: draft
  products: [drims]
---

# DRIMS Configuration Guide

This guide is for **implementers** configuring DRIMS for disaster response operations. You should be comfortable with logic builders like Kobo or CommCare, but you don't need Python skills.

## What You'll Find Here

- **Warehouses** - Enable warehouses for DRIMS, set tiers, assign to areas
- **Approval Chains** - Configure multi-tier approval workflows
- **Alerts** - Customize low stock, SLA, and expiry warning thresholds
- **Vocabularies** - Define donor types, priorities, transport modes

```{toctree}
:hidden:
:maxdepth: 1

warehouses
approval_chains
alerts
vocabularies
```

## Quick Links

- {doc}`warehouses` - Set up warehouse tiers and geographic assignments
- {doc}`approval_chains` - Configure request approval workflows
- {doc}`alerts` - Set alert thresholds for monitoring

---

## Mental Model

DRIMS configuration follows this hierarchy:

```
Incident (disaster event)
  ↓
Warehouses (where supplies are stored)
  ↓
Users (who can access which warehouses/areas)
  ↓
Operations (donations, requests, dispatches)
  ↓
Alerts (automated monitoring)
```

**Key concepts:**

1. **Everything links to an Incident** - All donations, requests, and dispatches are tied to a specific disaster response
2. **Warehouses have tiers** - Central (main depot), Regional (province/district), Mobile (temporary field sites)
3. **Geographic scoping** - Users see only requests/dispatches for their assigned areas
4. **Approval workflows** - Requests follow configurable approval chains before dispatch
5. **Automated monitoring** - Alert engine runs scheduled checks for low stock, SLA breaches, and expiring items

## Before You Start

**Required permissions:**
- You need **DRIMS Manager** access to configure the system
- For testing, you'll also need **DRIMS Officer** to create sample operations

**Prerequisites:**
- Geographic area hierarchy configured (provinces, districts, etc.)
- At least one warehouse created in Odoo Inventory
- Hazard incidents module installed (`spp_hazard`)

**Recommended:**
- Review the DRIMS user guide to understand operational workflows
- Have a list of your organization's warehouses and staff roles ready

## Configuration Areas

| Area | What You Configure | Where |
|------|-------------------|-------|
| **Warehouses** | Enable for DRIMS, set tier, assign geographic area | DRIMS → Inventory → Warehouses |
| **Approval Chains** | Define who approves requests, set approval levels | DRIMS → Configuration → Approval Rules |
| **Alert Thresholds** | Low stock %, SLA warning days, expiry warning days | Settings → DRIMS or per-incident overrides |
| **Vocabularies** | Donor types, priorities, transport modes, item conditions | Studio → Vocabularies |
| **User Roles** | Assign security groups, geographic areas, warehouses | Settings → Users & Companies → Users |
| **Personnel** | Track deployed staff, roles, locations | DRIMS → Coordination → Personnel |

## Next Steps

After configuration, users can begin operations:

- **Receiving donations** - Record pledges and incoming supplies
- **Processing requests** - Field staff submit needs, approvers review
- **Managing dispatches** - Warehouse staff pick and ship items
- **Monitoring alerts** - Review low stock, SLA warnings, expiry notices

See the [DRIMS User Guide](../../user_guide/drims/index.md) for operational tasks.

## Are You Stuck?

**Can't see DRIMS menu items?**
Check that you have the **DRIMS Manager** or **DRIMS Officer** security group. Contact your system administrator to assign permissions.

**Warehouses not appearing in DRIMS?**
You must enable the "DRIMS Warehouse" checkbox on each warehouse. Go to **DRIMS → Inventory → Warehouses**, open the warehouse, and check the "DRIMS Warehouse" field.

**Geographic areas not loading?**
DRIMS requires the `spp_area` module with configured area hierarchy. Check **DRIMS → Configuration → Areas** to verify areas exist.

**Alert thresholds not triggering?**
Alert jobs run on schedule (low stock every 4 hours, SLA every 2 hours, expiry daily). Check that scheduled actions are enabled in **Settings → Technical → Automation → Scheduled Actions**.

## When You Need Custom Development

Most DRIMS configuration can be done through the interface. You only need custom development for:

- Custom alert types beyond low stock/SLA/expiry
- Integration with external systems (3PL, OCHA HDX, etc.)
- Custom entitlement calculations for beneficiary-based distribution
- Advanced reporting beyond 4W reports and dashboards
