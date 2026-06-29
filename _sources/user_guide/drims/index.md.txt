---
openspp:
  doc_status: draft
  products: [drims]
  applies_to:
    - drims
---

# DRIMS user guide

This guide is for **program staff, warehouse workers, and field officers** who use DRIMS to manage disaster relief supplies.

## What is DRIMS?

DRIMS (Disaster Response Inventory Management System) helps you track emergency supplies from incoming donations through to delivery to affected communities.

With DRIMS you can:

- **Record donations** from organizations and inspect items into your warehouse
- **Request relief supplies** for disaster-affected areas
- **Allocate and dispatch** items from warehouses to distribution points
- **Monitor stock levels** across all your warehouses in real time
- **Handle returns** when items come back from the field

All operations are linked to a **disaster incident** (for example, "2025 Flooding — Western Region") so everything can be tracked by emergency.

## The relief supply workflow

```
Donation → Receive → Inspect → Stock
                                  ↓
                           Request submitted
                                  ↓
                           Approved (Ready for Allocation)
                                  ↓
                           Stock allocated (Ready for Dispatch)
                                  ↓
                           Dispatch created → Picked → Departed
                                  ↓
                           Delivered (Proof of Delivery)
```

A single approved request can have **multiple partial dispatches** — useful when only some stock is available now and more arrives later.

## User roles

Your role determines what you can do in DRIMS:

| Role | What you can do |
|------|-----------------|
| **Viewer** | View all DRIMS information; no changes |
| **Field Officer** | Create and submit requests for your assigned areas; confirm deliveries |
| **Warehouse Staff** | Receive donations, manage stock, validate dispatches |
| **Approver** | Review and approve or reject requests |
| **Coordinator** | Allocate stock to approved requests; create dispatches |
| **Manager** | Full access to all DRIMS features and settings |

If you see a message saying you don't have permission, ask your system administrator to assign you the right role.

## Guides in this section

```{toctree}
:maxdepth: 1

dashboard
donations
manage_inventory
requests
dispatches
returns
```

### Receiving supplies

- {doc}`donations` - Receive an incoming donation, inspect items, and stock them

### Managing stock

- {doc}`manage_inventory` - View stock levels, expiry dates, movement history, and add products
- {doc}`dashboard` - Monitor warehouse health and alerts at a glance

### Requesting and delivering supplies

- {doc}`requests` - Submit a request (field officers) or allocate and dispatch one (coordinators)
- {doc}`dispatches` - Pick, pack, ship, and confirm delivery (warehouse staff)
- {doc}`returns` - Handle items returned from distribution points

## Are you stuck?

**Can't find the DRIMS menu?**

You may not have DRIMS access. Ask your administrator to assign you a DRIMS role.

**Don't see any warehouses or areas in the dropdown lists?**

Your administrator needs to assign you to specific warehouses or geographic areas.

**Something not covered here?**

Ask your supervisor or system administrator for help.
