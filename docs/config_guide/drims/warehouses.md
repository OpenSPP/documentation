---
openspp:
  doc_status: draft
  products: [drims]
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
| **Area** | Dropdown | Recommended | Geographic location from the area hierarchy |
| **Storage Capacity (m³)** | Number | Optional | Maximum storage volume |
| **Active Incidents** | Multi-select | Optional | Hazard incidents this warehouse is responding to |

### Field Details

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

## Common Deployment Patterns

### Pattern 1: Single Warehouse (Small-Scale)

For pilot programs or single-district responses — one warehouse handles all donations and distribution.

### Pattern 2: Hub and Spoke (Provincial)

For province-wide disasters — a central hub in the provincial capital supplies field locations in affected districts.

### Pattern 3: Multi-Incident Shared Infrastructure

For regions with concurrent disasters — one warehouse serves multiple active incidents, tracking inventory per incident.

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

3. **Area permissions:** Verify the warehouse's area is accessible to your user account.

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
