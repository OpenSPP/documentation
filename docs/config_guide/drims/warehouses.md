---
openspp:
  doc_status: draft
---

# Configuring Warehouses

This guide is for **implementers** setting up warehouse infrastructure for a DRIMS deployment. You should be familiar with basic inventory concepts and disaster response coordination, but you don't need to know Python or Odoo internals.

## Mental Model

DRIMS organizes warehouses into a three-tier hierarchy that mirrors real-world disaster response operations:

```
┌─────────────────────────────────┐
│   Central Warehouse (Tier 1)    │  ← National stockpile
│   • High-capacity storage        │
│   • Receives bulk donations      │
│   • Supplies regional warehouses │
└─────────────────────────────────┘
           │ Distributes to
           ▼
┌─────────────────────────────────┐
│  Regional Warehouses (Tier 2)   │  ← Provincial/district hubs
│  • Medium-capacity storage       │
│  • Serves multiple districts     │
│  • Coordinates local distribution│
└─────────────────────────────────┘
           │ Distributes to
           ▼
┌─────────────────────────────────┐
│   Mobile Warehouses (Tier 3)    │  ← Field distribution points
│   • Temporary field locations    │
│   • Direct beneficiary access    │
│   • Rapid deployment capability  │
└─────────────────────────────────┘
```

**Key concepts:**

- **DRIMS-enabled warehouse**: Any Odoo warehouse marked for disaster response operations
- **Warehouse tier**: Classification that determines the warehouse's role in the distribution chain
- **Incident linkage**: Warehouses can be assigned to specific disasters to track incident-specific inventory
- **Area assignment**: Links warehouses to geographic locations for routing and reporting

## Enabling a Warehouse for DRIMS

Before a warehouse can be used for disaster response operations, it must be enabled in DRIMS.

### Steps

1. Navigate to **DRIMS → Inventory → Warehouses**

   ![Screenshot placeholder: DRIMS inventory menu](warehouses/nav_warehouses.png)

2. Select an existing warehouse or create a new one using the **New** button

3. In the warehouse form, check the **DRIMS Warehouse** checkbox

   ![Screenshot placeholder: DRIMS warehouse checkbox](warehouses/enable_drims.png)

4. Configure the DRIMS-specific fields (see next section)

5. Click **Save**

## Warehouse Configuration

Once a warehouse is DRIMS-enabled, configure these fields:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| **DRIMS Warehouse** | Checkbox | Yes | Enables the warehouse for DRIMS operations |
| **Warehouse Tier** | Selection | Yes | Role in distribution hierarchy (Central/Regional/Mobile) |
| **Area** | Dropdown | Recommended | Geographic location from the area hierarchy |
| **Linked Incidents** | Multi-select | Optional | Specific disasters this warehouse serves |

![Screenshot placeholder: DRIMS warehouse configuration form](warehouses/config_form.png)

### Field Details

**Warehouse Tier**

Choose based on the warehouse's role:

- `Central` - National or main stockpile that receives bulk donations
- `Regional` - Provincial/district hub serving multiple areas
- `Mobile` - Temporary field location for direct distribution

**Area**

Select the geographic area from your configured hierarchy (Province → District → Division). This determines:

- Which users can access the warehouse (based on area permissions)
- Routing decisions for automated dispatch suggestions
- Geographic filtering in reports and dashboards

**Linked Incidents**

Optional multi-select field to restrict the warehouse to specific disasters. When set:

- Only donations/requests for linked incidents can use this warehouse
- Dashboard metrics filter to show only linked incident data
- Useful for dedicated response warehouses (e.g., "Flood 2024 Response Center")

Leave empty to allow the warehouse to serve all incidents.

## Linking Warehouses to Incidents

You can associate warehouses with specific disaster incidents in two ways:

### Option 1: From the Warehouse Form

1. Open the warehouse in **DRIMS → Inventory → Warehouses**
2. Scroll to the **Linked Incidents** field
3. Click to select one or more incidents
4. Save the warehouse

### Option 2: From the Incident Dashboard

1. Open the incident in **DRIMS → Dashboard**
2. Navigate to the **Warehouses** tab
3. Click **Add** to link existing warehouses
4. Select warehouses from the list
5. Save the incident

![Screenshot placeholder: Incident warehouses tab](warehouses/incident_link.png)

**When to link warehouses to incidents:**

- Dedicated response: A warehouse is set up specifically for one disaster
- Resource isolation: Strict separation of inventory between concurrent disasters
- Security: Limit warehouse visibility to incident-specific teams

**When to leave warehouses unlinked:**

- Shared facilities: One warehouse serves multiple ongoing disasters
- Permanent infrastructure: Regional hubs that handle all disasters in their area
- Flexible allocation: You want to reassign warehouse capacity as incidents evolve

## Setting Up Warehouse Tiers

### Central Warehouse Setup

**Use case:** National or main stockpile receiving bulk donations from international agencies.

| Field | Recommended Value |
|-------|-------------------|
| Warehouse Tier | Central |
| Area | Leave empty or set to country level |
| Linked Incidents | Leave empty (serves all) |

**Typical configuration:**
- High storage capacity
- Located near international ports/airports
- Receives donations in large quantities
- Distributes to regional warehouses

### Regional Warehouse Setup

**Use case:** Provincial or district hub coordinating local distribution.

| Field | Recommended Value |
|-------|-------------------|
| Warehouse Tier | Regional |
| Area | Set to province or district |
| Linked Incidents | Leave empty or link to regional disasters |

**Typical configuration:**
- Medium storage capacity
- Strategically located within the region
- Receives stock from central warehouse
- Distributes to mobile units and distribution points

### Mobile Warehouse Setup

**Use case:** Temporary field location for rapid deployment and direct beneficiary access.

| Field | Recommended Value |
|-------|-------------------|
| Warehouse Tier | Mobile |
| Area | Set to district or division |
| Linked Incidents | Link to specific incident |

**Typical configuration:**
- Temporary/portable infrastructure
- Located close to affected populations
- Minimal storage capacity
- Direct distribution to beneficiaries

## Common Patterns

### Pattern 1: Single-Tier Deployment (Small-Scale)

For pilot programs or single-district responses:

```
Mobile Warehouse
├─ Area: Target District
├─ Tier: Mobile
└─ Incidents: Single active disaster
```

All donations received and distributed from one location.

### Pattern 2: Two-Tier Deployment (Provincial)

For province-wide disasters:

```
Regional Warehouse (Provincial Capital)
├─ Area: Province
├─ Tier: Regional
└─ Serves
    ├─ Mobile Warehouse (District A)
    ├─ Mobile Warehouse (District B)
    └─ Mobile Warehouse (District C)
```

Regional hub supplies multiple field locations.

### Pattern 3: Three-Tier Deployment (National)

For major national disasters:

```
Central Warehouse (Capital)
├─ Area: Country
├─ Tier: Central
└─ Serves
    ├─ Regional Warehouse (Province 1)
    │   └─ Mobile units in Districts 1A, 1B
    ├─ Regional Warehouse (Province 2)
    │   └─ Mobile units in Districts 2A, 2B
    └─ Regional Warehouse (Province 3)
        └─ Mobile units in Districts 3A, 3B
```

Full cascading distribution from national stockpile to field.

### Pattern 4: Multi-Incident Shared Infrastructure

For regions with concurrent disasters:

```
Regional Warehouse (Shared)
├─ Area: Province
├─ Tier: Regional
├─ Incidents: [Empty - serves all]
└─ Handles
    ├─ Flood 2024 (Incident A)
    ├─ Drought 2024 (Incident B)
    └─ Landslide 2024 (Incident C)
```

One warehouse tracks inventory separately per incident but shares physical space.

## Stock Health Indicators

DRIMS automatically calculates warehouse health based on alerts:

| Health Status | Indicator | Meaning |
|---------------|-----------|---------|
| **Good** | Green | No critical alerts, adequate stock levels |
| **Warning** | Yellow | Low stock alerts or items approaching expiry |
| **Critical** | Red | Stock-outs, expired items, or SLA violations |

Health status is computed automatically based on:
- Low stock alerts for essential items
- Expiry warnings
- Pending requests exceeding delivery deadlines

You cannot set health status manually - it reflects the current alert state.

## Are You Stuck?

### Can't see DRIMS Warehouse checkbox?

**Problem:** The DRIMS Warehouse field doesn't appear on the warehouse form.

**Solution:** Ensure the `spp_drims` module is installed. Go to **Apps → Update Apps List** and search for "DRIMS". Install if not already active.

### Warehouse doesn't appear in donation/request forms?

**Problem:** A DRIMS-enabled warehouse isn't showing up as an option when creating donations or requests.

**Possible causes:**

1. **Incident mismatch:** The warehouse is linked to specific incidents, but you're creating a donation/request for a different incident. Either unlink the warehouse from incidents (to make it available for all) or ensure you're working with a matching incident.

2. **Area permissions:** Your user account may not have access to the warehouse's assigned area. Contact your administrator to verify your area assignments in **Settings → Users → [Your User] → DRIMS Area Access**.

3. **Warehouse tier mismatch:** Some transaction types have tier restrictions. For example, bulk donations may be configured to only accept central warehouses.

### How do I know which tier to assign?

**Question:** I'm not sure whether to make this warehouse Central, Regional, or Mobile.

**Answer:** Ask these questions:

- **Where does it receive stock from?** If from international donors → Central. If from another warehouse in-country → Regional or Mobile.
- **What's its capacity?** High-capacity → Central. Medium → Regional. Temporary/low → Mobile.
- **How permanent is it?** Permanent infrastructure → Central or Regional. Temporary field deployment → Mobile.
- **Who does it serve?** Other warehouses → Central or Regional. Direct beneficiaries → Mobile.

If still uncertain, start with `Regional` - you can change it later without affecting historical data.

### Can I change warehouse tier after transactions exist?

**Yes.** The tier field can be changed at any time. Historical transactions (donations, requests, dispatches) are not affected. The tier only influences:

- How the warehouse appears in reports and organizational charts
- Default routing suggestions for new requests
- Dashboard grouping and metrics

Changing tier does not move or modify existing inventory.

### Should I create one warehouse per incident or share warehouses?

**It depends on your operating model:**

**Separate warehouses per incident when:**
- Funding sources require strict separation
- Different agencies lead different incidents (consortium model)
- Security/access control demands physical or logical isolation

**Share warehouses across incidents when:**
- You have limited physical infrastructure
- Operational efficiency benefits from consolidated inventory
- You trust DRIMS to track incident-specific stock within shared facilities

DRIMS tracks inventory per incident regardless of your choice. The difference is organizational and security-related, not technical.

## Next Steps

- {doc}`/config_guide/drims/vocabularies` - Configure donor types and item conditions
- {doc}`/config_guide/drims/alerts` - Set up stock monitoring and alerts
- {doc}`/user_guide/drims/donations` - Receive donations into warehouses
