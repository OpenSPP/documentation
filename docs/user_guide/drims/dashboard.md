---
openspp:
  doc_status: draft
  products: [drims]
  applies_to:
    - drims
---

# Understand the Dashboard

```{admonition} Applies to: DRIMS
:class: tip
This feature is available in OpenSPP deployments with the DRIMS module installed.
```

This guide is for **DRIMS users** who need to monitor disaster response operations, track inventory, and respond to alerts.

## What You'll Do

Learn how to read the DRIMS dashboard to understand the current status of your disaster response at a glance:

- **Incident cards** - See donations, requests, stock, and distributions for each disaster
- **Key Performance Indicators (KPIs)** - Track what's happening in real time
- **Warehouse health** - Identify warehouses that need attention
- **Alerts** - Get notified when action is needed (low stock, overdue requests, expiring items)

## Before You Start

- You need **DRIMS Viewer** or higher access to view the dashboard
- You need **DRIMS Warehouse Staff** or **Manager** access to acknowledge and resolve alerts
- At least one **hazard incident** must exist — every DRIMS operation (donation, request, dispatch) is linked to an incident, so the dashboard will be empty until one is created. Incidents are created by an implementer or administrator. See {doc}`/user_guide/hazards/index` for how to record and manage incidents.

## The Incident Dashboard

**Where to find it:** Click **DRIMS** in the sidebar, then select **Dashboard**.

![Click DRIMS in the sidebar, then select Dashboard](/_images/en-us/user_guide/drims/dashboard/01-click-drims-sidebar.png)

The dashboard displays each active incident as a card. Cards are organized by status (Alert, Active, Recovery, Closed) and show the most important information about each disaster response operation.

```{note}
New incidents default to **Active** status. The **Alert** status is for pre-disaster preparedness (e.g., a typhoon is approaching but hasn't hit yet) and can only be set by an administrator. The typical flow is: Active → Recovery → Closed.
```

![DRIMS Dashboard showing incident cards with KPIs for each disaster](/_images/en-us/user_guide/drims/dashboard/02-incident-cards-kpis.png)

Each incident card displays:

- **Incident name** - The disaster or emergency
- **Status badge** - Current state (Alert, Active, Recovery, Closed)
- **KPI row** - Key metrics at a glance
- **Alert indicators** - Warnings that need attention

## Reading Incident Cards

Each incident card shows key performance indicators (KPIs) that help you understand the response status.


### What the Numbers Mean

| KPI | What It Shows | Example |
|-----|---------------|---------|
| **Donations** | Number of donations received and their total value | "5 donations, $25,000" |
| **Requests** | Total requests and how many are pending approval | "12 requests, 3 pending" |
| **Stock** | Items currently on hand across warehouses assigned to this incident (not yet dispatched). Drops to zero once goods are sent out — does not reflect total received. | "176 units, 4 products" |
| **Distributed** | Total value of goods dispatched (unit price × quantity), not a cash payment. Shows zero if products have no unit price set. | "$15,000 distributed" |
| **Beneficiaries** | Number of beneficiaries served in the last 30 days from completed distributions | "234 beneficiaries (30d)" |
| **Returns** | Number of processed return dispatches | "1 return processed" |

```{note}
KPI numbers (stock, distributed value, beneficiaries) are cached for performance and may not reflect the latest changes immediately. If a number looks wrong — for example, stock shows zero when you know items exist — first check that the warehouse is linked to the incident under **Active Response** (DRIMS → Inventory → Warehouses). If the warehouse is correctly linked but the number is still wrong, contact your system administrator to refresh the cache.
```

### Understanding the Badges

- **Red badge** (⚠) - One or more critical priority alerts on this incident
- **Orange badge** (🔔) - Active alerts present, none critical
- **Orange "pending" indicator** on Requests - Requests waiting for approval

## Warehouse Health Indicators

Warehouses assigned to an incident display a health badge showing whether they need attention. For configuration details see {doc}`/config_guide/drims/warehouses`.

| Status | Color | What It Means |
|--------|-------|---------------|
| **Critical** | Red | 3 or more active alerts |
| **Warning** | Orange | 1–2 active alerts |
| **Good** | Green | No active alerts |

**Where to find it:** Click **DRIMS** in the sidebar, then **Inventory → Warehouses**.

![Click Inventory then Warehouses to check warehouse health](/_images/en-us/user_guide/drims/dashboard/03-click-inventory-warehouses.png)

![DRIMS Warehouses list showing health status indicators for each warehouse](/_images/en-us/user_guide/drims/dashboard/04-warehouse-health-status.png)

## Understanding Alerts

DRIMS automatically monitors your operations and creates alerts when something needs attention. For full configuration and threshold details see {doc}`/config_guide/drims/alerts`.

| Alert Type | What It Means |
|------------|---------------|
| **Low Stock** | Available stock has dropped below 50% of pending request quantities |
| **SLA Warning** | A request is approaching its due date (within 2 days) |
| **SLA Breach** | A request is past its due date and has not been delivered |
| **Expiry Warning** | Items in a DRIMS warehouse are approaching their expiration date |

Alerts are assigned **Critical**, **High**, or **Medium** priority depending on how urgent the situation is. Check **DRIMS → Monitoring → Alerts** to see all active alerts filtered by priority, type, or warehouse.

## Acknowledging and Resolving Alerts

Alerts have three states that show whether they've been addressed:

| State | Badge | What It Means |
|-------|-------|---------------|
| **Active** | Red | New alert that hasn't been reviewed yet |
| **Acknowledged** | Orange | Someone is working on it |
| **Resolved** | Green | Issue has been fixed |

### How to Acknowledge an Alert

Acknowledge an alert when you've seen it and are taking action.

**Steps:**

1. Click **DRIMS** in the sidebar, then select **Monitoring → Alerts**

2. Click on the alert you want to acknowledge

![Click on an alert to see its details](/_images/en-us/user_guide/drims/dashboard/05-alert-detail-view.png)

3. Click the **Acknowledge** button at the top of the form

![Use Acknowledge and Resolve buttons to manage the alert status](/_images/en-us/user_guide/drims/dashboard/06-acknowledge-resolve-alert.png)

The alert badge changes to orange, showing others that someone is handling it.

### How to Resolve an Alert

Resolve an alert after you've fixed the underlying problem.

**Steps:**

1. Fix the issue:
   - **Low stock:** Receive new donations or transfers
   - **SLA breach/warning:** Complete the dispatch and delivery
   - **Expiry warning:** Distribute items before they expire, or record wastage if expired

2. Open the alert (see steps above)

3. Click the **Resolve** button at the top of the form


The alert is marked resolved and no longer appears in active counts.

```{note}
DRIMS automatically checks for problems every few hours. If the problem still exists after you resolve an alert, a new alert will be created on the next check.
```

## Are You Stuck?

### I don't see the Dashboard menu

You may not have the right permissions. Contact your DRIMS administrator and ask for **DRIMS User** access.

### The KPI numbers look wrong

KPIs are updated automatically, but stock, distributed value, and beneficiary counts are cached for performance and may lag behind recent changes. Wait a few minutes and refresh the page. If numbers still look wrong, check that the warehouse is linked to the incident — see the note in the KPI table above. If the issue persists, contact your system administrator.

### I resolved an alert but it came back

DRIMS automatically rechecks for problems every few hours. If the underlying issue wasn't fully fixed, a new alert will be created. For example:

- **Low stock alert:** You need to receive enough stock to meet 50% of pending requests
- **SLA breach alert:** The request must be fully delivered, not just dispatched
- **Expiry warning:** Items must be distributed or marked as waste

### What does "pending" mean for requests?

Pending requests are waiting for approval. They haven't been rejected, but they haven't been approved for dispatch yet. Check with your warehouse manager or approval officer.

### Can I create alerts manually?

Yes. Go to **DRIMS → Monitoring → Alerts** and click **New**. This is useful when you notice a problem that DRIMS didn't automatically detect.

### How do I know which warehouse to restock?

Check the **Warehouse Health Indicators** (DRIMS → Inventory → Warehouses). Warehouses with red or orange status need attention. Click on a warehouse to see its active alerts.

### The alert says "SLA breach" but what does SLA mean?

SLA stands for "Service Level Agreement" - it's the due date or deadline for a request. An SLA breach means the request wasn't delivered by its due date.

## Next Steps

- {doc}`donations` - Learn how to receive and process donations
- {doc}`manage_inventory` - Learn how to view and manage stock levels
- {doc}`requests` - Learn how to submit relief requests
