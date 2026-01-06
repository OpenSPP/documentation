---
openspp:
  doc_status: draft
---

# Configuring Vocabularies

This guide is for **implementers** customizing DRIMS controlled vocabularies. If you configure logic in tools like Kobo or CommCare, you have the skills to manage DRIMS vocabularies. You don't need Python knowledge.

## Mental Model

**Vocabularies** in DRIMS are controlled lists of standardized codes that ensure consistency across the system. Think of them like dropdown lists, but managed centrally and reusable across different forms and reports.

Each vocabulary has:

1. **Namespace URI** - A unique identifier (e.g., `urn:openspp:vocab:drims:priority-levels`)
2. **Codes** - Individual values within the vocabulary (e.g., `critical`, `high`, `medium`, `low`)
3. **Display Names** - Human-readable labels that can be translated
4. **System Flag** - Whether the vocabulary is protected from deletion

### Why Vocabularies Matter

Vocabularies prevent data quality issues:

- **Consistency** - Everyone uses the same codes for "high priority"
- **Reporting** - You can aggregate data reliably across incidents
- **Integration** - External systems can reference standard codes
- **Validation** - Invalid values are rejected automatically

```{note}
DRIMS uses international standards where possible. For example, the humanitarian {term}`Cluster` codes come directly from UN {term}`OCHA` guidelines.
```

## DRIMS Vocabularies

DRIMS defines 15+ vocabularies for different classification needs:

| Namespace URI | Purpose | Used In |
|---------------|---------|---------|
| `urn:openspp:vocab:drims:priority-levels` | Request urgency levels | Requests |
| `urn:openspp:vocab:drims:donor-types` | Donor classification | Donations |
| `urn:openspp:vocab:drims:item-conditions` | Item quality states | Donation inspection |
| `urn:openspp:vocab:drims:transport-modes` | Shipping methods | Dispatches |
| `urn:openspp:vocab:drims:request-states` | Request fulfillment status | Requests |
| `urn:openspp:vocab:drims:donation-states` | Donation processing status | Donations |
| `urn:openspp:vocab:drims:drims-types` | Transaction types | Stock movements |
| `urn:openspp:vocab:drims:alert-types` | Alert classifications | Alerts |
| `urn:openspp:vocab:drims:coordination-modes` | Multi-agency coordination models | Incidents |
| `urn:ocha:iasc:clusters` | UN humanitarian sectors | Requests, Personnel |
| `urn:openspp:vocab:drims:personnel-roles` | Staff role types | Personnel |
| `urn:openspp:vocab:drims:return-reasons` | Why items are returned | Returns |
| `urn:openspp:vocab:drims:warehouse-tiers` | Warehouse classification | Warehouses |
| `urn:openspp:vocab:drims:organization-roles` | Partner agency roles | Organizations |

```{important}
System vocabularies (marked with the system flag) include codes required by DRIMS workflows. You can add custom codes to these vocabularies, but you cannot delete the predefined codes.
```

## OCHA Humanitarian Clusters

The **humanitarian {term}`Cluster` system** is a standardized UN framework for coordinating disaster response by sector. DRIMS implements the official {term}`OCHA`/{term}`IASC` definitions.

### Cluster Reference

| Code | Cluster Name | Lead Agency | Focus Area |
|------|--------------|-------------|------------|
| `food_security` | Food Security | WFP / FAO | Food distribution, agricultural inputs, livelihood support |
| `health` | Health | WHO | Medical services, disease surveillance, health facility support |
| `nutrition` | Nutrition | UNICEF | Treatment of malnutrition, supplementary feeding, infant care |
| `wash` | WASH | UNICEF | Water supply, sanitation facilities, hygiene promotion |
| `shelter` | Shelter | UNHCR / IFRC | Emergency shelter, non-food items, housing reconstruction |
| `protection` | Protection | UNHCR | Safety, human rights, GBV prevention, child protection |
| `education` | Education | UNICEF / Save the Children | Learning continuity, temporary schools, supplies |
| `early_recovery` | Early Recovery | UNDP | Livelihoods restoration, debris removal, infrastructure |
| `logistics` | Logistics | WFP | Supply chain, warehousing, transport coordination |
| `emergency_telecom` | Emergency Telecommunications | WFP | Communications infrastructure, connectivity |
| `camp_coordination` | Camp Coordination & Management | UNHCR / IOM | Displaced persons camps, site management |

### How Clusters Are Used

**In Requests:**
Tag relief requests with the appropriate humanitarian sector to enable:
- Filtering requests by sector
- Reporting to cluster leads
- Identifying sector-specific gaps

**Example:**
```
Request: REQ-2025-0042
Cluster: WASH
Items: Water purification tablets (5000), Jerry cans (200)
```

**In Personnel Records:**
Assign deployed staff to clusters for coordination and {term}`4W Report`ing ("Who does What, Where, When").

**Example:**
```
Personnel: Dilani Perera
Role: Field Coordinator
Cluster: Health
Incident: 2025 Southwest Monsoon Floods
```

![Cluster selection on request form](vocabularies/cluster_selection.png)

```{note}
The cluster codes follow UN OCHA standards and should not be modified. If your country uses different sector names, create custom translations in **Settings → Translations** rather than changing the codes.
```

## Priority Levels

Priority levels classify the urgency of relief requests. DRIMS includes four standard levels:

| Code | Display Name | Use Case |
|------|--------------|----------|
| `critical` | Critical | Life-threatening situations requiring immediate response (< 24 hours) |
| `high` | High | Urgent needs requiring response within 2-3 days |
| `medium` | Medium | Important needs requiring response within 1 week |
| `low` | Low | Non-urgent needs that can wait beyond 1 week |

### Priority in Workflows

Priority affects:
- **Dashboard sorting** - Critical requests appear first
- **Alert generation** - Overdue critical requests trigger automatic alerts
- **Approval routing** - Critical requests may bypass certain approval steps

![Priority field on request](vocabularies/priority_field.png)

```{tip}
You can add custom priority levels (e.g., `routine` for regular stock replenishment) by adding vocabulary codes. See "Adding Custom Vocabulary Codes" below.
```

## Item Conditions

Item condition codes track the quality state of donated goods during inspection:

| Code | Display Name | Description |
|------|--------------|-------------|
| `new` | New | Brand new, unopened items |
| `good` | Good | Used but fully functional, clean, no damage |
| `fair` | Fair | Functional with minor wear or cosmetic damage |
| `poor` | Poor | Functional but significant wear or damage |
| `damaged` | Damaged | Non-functional, broken, or unusable |
| `expired` | Expired | Past expiration or best-before date |

### Condition Tracking

Condition is recorded:
- **On donation receipt** - During warehouse inspection
- **On distribution** - When dispatching to beneficiaries
- **On return** - When items come back from field

![Item condition selection during inspection](vocabularies/condition_inspection.png)

```{warning}
Items marked `damaged` or `expired` should not be distributed. DRIMS can generate alerts when such items remain in inventory beyond a threshold period.
```

## Coordination Modes

Coordination modes define how multi-agency disaster response is organized:

| Code | Mode | Description |
|------|------|-------------|
| `lead_agency` | {term}`Lead Agency` | Single agency (usually government) coordinates all partners |
| `cluster` | Cluster System | UN-led sector coordination with designated cluster leads |
| `consortium` | Consortium | NGO-led coordination among partner organizations |
| `bilateral` | Bilateral | Direct government-to-government or agency-to-agency |

### Using Coordination Modes

Set the coordination mode on each **incident record** to indicate how the response is managed:

| Field | Value |
|-------|-------|
| Incident | 2025 Southwest Monsoon Floods |
| Coordination Mode | Cluster System |

This helps DRIMS:
- Generate appropriate reports (e.g., {term}`4W Report`s for cluster coordination)
- Route information to the right stakeholders
- Track agency roles correctly

![Coordination mode on incident](vocabularies/coordination_mode.png)

## Organization Roles

Partner agencies can be assigned roles in disaster response:

| Code | Role | Description |
|------|------|-------------|
| `lead` | {term}`Lead Agency` | Primary coordinating organization |
| `co_lead` | {term}`Co-Lead` | Shares coordination responsibility |
| `implementing` | {term}`Implementing Partner` | Delivers services on the ground |
| `funding` | {term}`Funding Partner` | Provides financial resources |
| `technical` | {term}`Technical Partner` | Provides expertise and guidance |

### Example

```
Organization: UNICEF
Role: Co-Lead
Incident: 2025 Southwest Monsoon Floods
Cluster: WASH
```

## Adding Custom Vocabulary Codes

You can extend vocabularies with country-specific or program-specific codes without writing Python.

### Step 1: Navigate to Vocabulary Management

Go to **DRIMS → Configuration → Vocabularies**.

![Vocabularies menu](vocabularies/menu_vocabularies.png)

### Step 2: Select the Vocabulary

Click on the vocabulary you want to extend (e.g., "Priority Levels").

![Select vocabulary](vocabularies/select_vocabulary.png)

### Step 3: Add a New Code

Click **Add a line** in the Codes section.

| Field | Value | Notes |
|-------|-------|-------|
| **Code** | `routine` | Lowercase, no spaces, use underscores |
| **Display Name (English)** | Routine | Human-readable label |
| **URI** | (auto-generated) | Leave blank - system generates |
| **Deprecated** | Unchecked | Check to hide from dropdowns |

![Add vocabulary code](vocabularies/add_code.png)

### Step 4: Save

Click **Save** to activate the new code.

### Step 5: Verify

Open a request form and check that the new priority level appears in the dropdown.

![New code in dropdown](vocabularies/verify_code.png)

```{important}
**Code naming rules:**
- Use lowercase letters
- Use underscores for spaces (e.g., `very_high` not `Very High`)
- Keep codes short and memorable
- Once saved, codes should not be changed (to preserve data integrity)
```

### Translating Vocabulary Codes

To add translations for vocabulary display names:

1. Go to **Settings → Translations → Translated Terms**
2. Search for your vocabulary code's display name
3. Add translations for each language

| Language | Translation |
|----------|-------------|
| English | Routine |
| French | De routine |
| Spanish | Rutina |

## Transport Modes

Transport modes classify how relief items are shipped:

| Code | Display Name | Typical Use |
|------|--------------|-------------|
| `road` | Road Transport | Trucks, vans for accessible areas |
| `air` | Air Transport | Helicopters, planes for remote or emergency deliveries |
| `water` | Water Transport | Boats for island or flood-affected areas |
| `rail` | Rail Transport | Trains for long-distance bulk shipments |
| `hand` | Hand Carry | Walking delivery for very remote locations |

Set transport mode on **dispatch records** for tracking and reporting.

## Alert Types

Alert types classify automated monitoring alerts:

| Code | Display Name | Triggers When |
|------|--------------|---------------|
| `stockout` | Stock Out | Product quantity reaches zero |
| `low_stock` | Low Stock | Product quantity below minimum threshold |
| `overstock` | Overstock | Product quantity above maximum threshold |
| `expiry_warning` | Expiring Soon | Product expiry date within warning period |
| `expired` | Expired | Product past expiration date |
| `request_overdue` | Request Overdue | Request not fulfilled by needed date |
| `dispatch_delayed` | Dispatch Delayed | Dispatch in transit beyond expected time |

```{note}
Alert thresholds can be configured per incident in **Incidents → Configuration → Alert Thresholds**.
```

## Transaction Types

Transaction types classify stock movements:

| Code | Display Name | Description |
|------|--------------|-------------|
| `donation_receipt` | Donation Receipt | Incoming donation to warehouse |
| `request_dispatch` | Request Dispatch | Outgoing shipment to fulfill request |
| `return_receipt` | Return Receipt | Items returned from distribution point |
| `adjustment` | Inventory Adjustment | Manual stock correction |
| `transfer` | Warehouse Transfer | Movement between warehouses |
| `write_off` | Write-off | Disposal of damaged/expired items |

## Viewing All Vocabularies

To see all vocabularies and their codes:

1. Go to **DRIMS → Configuration → Vocabularies**
2. Use the search and filters to find specific vocabularies
3. Click any vocabulary to view and edit its codes

![Vocabulary list](vocabularies/vocabulary_list.png)

## Are You Stuck?

### Can't find the Vocabularies menu?

You need **DRIMS Manager** or **Administrator** permissions. Contact your system administrator.

### New vocabulary code not appearing in dropdowns?

1. Check that you saved the vocabulary record
2. Refresh your browser (Ctrl+F5 or Cmd+Shift+R)
3. Verify the code is not marked as "Deprecated"

### Getting "duplicate code" error?

Code values must be unique within each vocabulary. Use a different code name.

### Want to remove a vocabulary code?

Instead of deleting (which can break historical data), mark the code as **Deprecated**. This hides it from dropdowns but preserves existing records.

### Need to change a code value?

Changing code values breaks historical data. Instead:
1. Mark the old code as deprecated
2. Create a new code with the correct value
3. Update active records to use the new code

### Cluster codes don't match our country's terminology?

Don't change the cluster codes (they follow UN standards). Instead, add translations in **Settings → Translations** to use your preferred terms.

### Want to add a completely new vocabulary?

New vocabularies require Python code and module development. Contact your developer or OpenSPP support for assistance. For most use cases, extending existing vocabularies with custom codes is sufficient.

## Related Documentation

- {doc}`/config_guide/drims/alerts` - Alert threshold configuration
- {doc}`/config_guide/drims/warehouses` - Warehouse configuration
- {doc}`/user_guide/drims/requests` - Creating relief requests
- {doc}`/user_guide/drims/donations` - Recording donations

## References

- [UN OCHA Cluster Coordination](https://www.humanitarianresponse.info/en/coordination/clusters)
- [IASC Cluster Reference Module](https://interagencystandingcommittee.org/iasc-transformative-agenda/iasc-reference-module-cluster-coordination-country-level-revised-july-2015)
