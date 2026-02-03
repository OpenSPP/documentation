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

## The Incident Dashboard

**Where to find it:** Click **DRIMS** in the sidebar, then select **Dashboard**.

The dashboard displays each active incident as a card. Cards are organized by status (Active, Pending, Closed) and show the most important information about each disaster response operation.

![Screenshot: DRIMS Dashboard showing incident cards](/_images/en-us/user_guide/drims/dashboard/1.png)

Each incident card displays:

- **Incident name** - The disaster or emergency
- **Status badge** - Current state (Active, Pending, Closed)
- **KPI row** - Key metrics at a glance
- **Alert indicators** - Warnings that need attention

## Reading Incident Cards

Each incident card shows key performance indicators (KPIs) that help you understand the response status.

![Screenshot: Single incident card with KPIs highlighted](/_images/en-us/user_guide/drims/dashboard/2.png)

### What the Numbers Mean

| KPI | What It Shows | Example |
|-----|---------------|---------|
| **Donations** | Number of donations received and their total value | "5 donations, $25,000" |
| **Requests** | Total requests and how many are pending approval | "12 requests, 3 pending" |
| **Stock** | Current inventory value and number of different items | "$18,500 in stock, 45 items" |
| **Distributed** | Value distributed and number of people helped (last 30 days) | "$15,000 distributed, 320 beneficiaries" |
| **Alerts** | Number of active alerts and critical alerts | "2 alerts, 1 critical" |

### Understanding the Icons

- **Orange border** - You have pending requests waiting for review
- **Red border** - You have critical alerts requiring immediate action
- **Orange badge** - Active alerts need attention
- **Gray text** - No stock currently available

## Warehouse Health Indicators

Each warehouse has a health status that tells you if it needs attention.

![Screenshot: Warehouse list showing health indicators](/_images/en-us/user_guide/drims/dashboard/3.png)

### Health Status Colors

| Status | Color | What It Means | What to Do |
|--------|-------|---------------|------------|
| **Critical** | Red | 3 or more active alerts, OR less than 10% stock capacity | Check alerts immediately, restock if needed |
| **Warning** | Orange | 1-2 active alerts, OR less than 30% stock capacity | Review alerts, plan restocking soon |
| **Good** | Green | No active alerts, adequate stock levels | No action needed |

**Where to find it:** Click **DRIMS** in the sidebar, then **Inventory → Warehouses**.

## Understanding Alerts

DRIMS automatically monitors your operations and creates alerts when something needs your attention. There are three types of alerts:

### Alert Types

| Alert Type | When It Appears | Priority | Example |
|------------|-----------------|----------|---------|
| **Low Stock** | Available stock is less than 50% of what pending requests need | Medium or High | "Rice stock (50 bags) below 50% of pending requests (120 bags)" |
| **SLA Breach** | A request is past its due date and hasn't been delivered | Critical or High | "Request #REQ-0045 is 3 days overdue" |
| **SLA Warning** | A request is due within 2 days | Medium or High | "Request #REQ-0052 due tomorrow" |
| **Expiry Warning** | Items in stock will expire soon (within 30 days) | Medium, High, or Critical | "Medical supplies lot #LOT-789 expires in 5 days" |

### Alert Priorities

| Priority | Color | When to Act |
|----------|-------|-------------|
| **Critical** | Red | Immediately - requires urgent action |
| **High** | Orange | Within hours - needs prompt attention |
| **Medium** | Yellow | Within 1-2 days - plan to address soon |
| **Low** | Blue | Informational - review when convenient |

### What Triggers Each Alert

**Low Stock Alerts:**
- Created every 4 hours
- Triggers when available quantity is less than 50% of pending request needs
- Priority is **High** if zero stock, **Medium** if some stock remains

**SLA Breach Alerts:**
- Created every 2 hours
- Triggers when a request passes its due date without being delivered
- Priority is **Critical** if more than 7 days overdue, **High** if 3-7 days, **Medium** if 1-3 days

**SLA Warning Alerts:**
- Created every 2 hours
- Triggers when a request is due within 2 days
- Priority is **High** if due today or tomorrow, **Medium** if due in 2 days

**Expiry Warning Alerts:**
- Created once daily
- Triggers when items will expire within 30 days
- Priority is **Critical** if expires within 7 days, **High** if within 14 days, **Medium** if within 30 days

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

1. Click **DRIMS** in the sidebar, then select **Operations → Alerts**

   ![Screenshot: Navigate to alerts menu](/_images/en-us/user_guide/drims/dashboard/4.png)

2. Click on the alert you want to acknowledge

   ![Screenshot: Alerts list](/_images/en-us/user_guide/drims/dashboard/5.png)

3. Click the **Acknowledge** button at the top of the form

   ![Screenshot: Acknowledge button](/_images/en-us/user_guide/drims/dashboard/6.png)

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

   ![Screenshot: Resolve button](/_images/en-us/user_guide/drims/dashboard/7.png)

The alert is marked resolved and no longer appears in active counts.

```{note}
DRIMS automatically checks for problems every few hours. If the problem still exists after you resolve an alert, a new alert will be created on the next check.
```

## Are You Stuck?

### I don't see the Dashboard menu

You may not have the right permissions. Contact your DRIMS administrator and ask for **DRIMS User** access.

### The KPI numbers look wrong

KPIs are updated automatically, but some values are cached for performance:

- **Donations, requests, stock items, beneficiaries** - Update in real time
- **Stock value, distributed value** - Update every 15-30 minutes

Wait a few minutes and refresh the page. If numbers still look wrong, contact your system administrator.

### I resolved an alert but it came back

DRIMS automatically rechecks for problems every few hours. If the underlying issue wasn't fully fixed, a new alert will be created. For example:

- **Low stock alert:** You need to receive enough stock to meet 50% of pending requests
- **SLA breach alert:** The request must be fully delivered, not just dispatched
- **Expiry warning:** Items must be distributed or marked as waste

### What does "pending" mean for requests?

Pending requests are waiting for approval. They haven't been rejected, but they haven't been approved for dispatch yet. Check with your warehouse manager or approval officer.

### Can I create alerts manually?

Yes. Go to **DRIMS → Operations → Alerts** and click **New**. This is useful when you notice a problem that DRIMS didn't automatically detect.

### How do I know which warehouse to restock?

Check the **Warehouse Health Indicators** (DRIMS → Inventory → Warehouses). Warehouses with red or orange status need attention. Click on a warehouse to see its active alerts.

### The alert says "SLA breach" but what does SLA mean?

SLA stands for "Service Level Agreement" - it's the due date or deadline for a request. An SLA breach means the request wasn't delivered by its due date.

## Next Steps

- {doc}`donations` - Learn how to receive and process donations
- {doc}`manage_inventory` - Learn how to view and manage stock levels
- {doc}`requests` - Learn how to submit relief requests
