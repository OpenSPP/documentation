---
openspp:
  doc_status: draft
  products: [core]
---

# Configuring Event Types

This guide is for **implementers** creating event type schemas in OpenSPP Studio. You should understand your program's data collection needs but don't need programming knowledge.

## Mental Model

Event types work in three layers:

1. **Studio Event Type** (Designer) - Where you configure fields, validation, and lifecycle
2. **Event Type** (System) - The activated schema used by the system
3. **Event Data Records** (Runtime) - Individual event instances collected from registrants

Think of it like this:
- **Studio Event Type** = Form template you're designing
- **Event Type** = Published form available for use
- **Event Data** = Completed forms

## Creating an Event Type

### Step 1: Navigate to Studio

Go to **Studio → Event Types** in the OpenSPP menu.

### Step 2: Create Event Type

Click **Create** and configure:

| Field | Value | Notes |
|-------|-------|-------|
| **Name** | Household Income Survey | User-facing name |
| **Code** | `household_income_survey` | Auto-generated from name, used in CEL expressions |
| **Target Type** | Group/Household | Individual, Group, or Both |
| **Description** | Quarterly income verification for cash transfer program | Helps users understand when to use this event type |

### Step 3: Configure Lifecycle

| Setting | Options | When to Use |
|---------|---------|-------------|
| **One Active Per Registrant** | Yes / No | **Yes**: Latest assessment replaces previous (e.g., disability status)<br>**No**: Keep all events (e.g., attendance records, field visits) |
| **Requires Approval** | Yes / No | **Yes**: New events start in "Pending Approval" state<br>**No**: Events activate immediately |
| **Auto Expiry** | None / Days / Months | Set expiry period (e.g., "Expire after 12 months" for annual assessments) |

**Example Configurations:**

| Event Type | One Active | Requires Approval | Expiry |
|------------|------------|-------------------|--------|
| Income Assessment | Yes | Yes | 12 months |
| Attendance | No | No | None |
| Disability Status | Yes | Yes | 24 months |
| Farm Visit | No | Yes | None |

### Step 4: Add Fields

Click the **Fields** tab and add your data fields. See {doc}`field_definitions` for detailed field configuration.

Quick field setup:

| Field Name | Type | Required | Example |
|------------|------|----------|---------|
| Monthly Income | Decimal | Yes | 4500.00 |
| Household Size | Integer | Yes | 5 |
| Employment Status | Selection | Yes | Employed / Unemployed / Self-employed |
| Income Source | Text | No | Farming |

### Step 5: Configure Programs (Optional)

If this event type is specific to certain programs:

1. Click **Programs** tab
2. Add programs that can use this event type
3. Leave empty if event type is global

### Step 6: Activate

Click **Activate** to make the event type available for use.

**What happens on activation:**
- System creates an `spp.event.type` record
- Event type appears in data entry wizards
- CEL expressions can reference it by code
- If using form builder, generates entry form view

## Event Type Settings Reference

### Basic Configuration

| Field | Description | Example |
|-------|-------------|---------|
| **Name** | Display name for users | "Household Survey" |
| **Code** | Technical identifier for CEL | `household_survey` |
| **Target Type** | Individual / Group / Both | Individual |
| **Description** | Help text for data collectors | "Monthly income verification" |

### Lifecycle Configuration

| Setting | Description | Impact |
|---------|-------------|--------|
| **One Active Per Registrant** | Only one active event allowed | New activation supersedes previous active event |
| **Allow Multiple Active** | Multiple active events allowed | All events stay active until manually changed |
| **Requires Approval** | Approval workflow enabled | New events start in "Pending Approval" |
| **Auto Expiry** | Automatic expiration enabled | Scheduled job expires events after period |
| **Expiry Period** | Days or months until expiry | 365 days, 12 months, etc. |

### Program Association

| Setting | Description | Effect |
|---------|-------------|--------|
| **Programs** | Linked programs | If set, only these programs see this event type |
| **Empty** | No program restriction | All programs can use this event type |

## Using Event Type Templates

OpenSPP V2 includes reusable field templates for common assessment types.

### Applying a Template

1. Create a new event type
2. Click **Apply Template**
3. Select template category:
   - **Survey/Assessment** - Generic survey fields
   - **Health Screening** - Health assessment fields
   - **Economic Assessment** - Income, assets, employment
   - **Demographic** - Household composition
4. Choose template
5. Review and customize fields

### Available Templates

| Template | Fields Included | Use Case |
|----------|----------------|----------|
| **Basic Income Assessment** | Monthly income, employment status, income source | Cash transfer programs |
| **Household Composition** | Household size, children count, dependents | Family support programs |
| **Disability Screening** | Disability type, severity, support needs | Disability programs |
| **Farm Assessment** | Land size, crops, livestock, certification | Agricultural programs |
| **Health Screening** | Health status, chronic conditions, vaccinations | Health programs |

## Event Type States

After creation, event types have states:

| State | Description | Available Actions |
|-------|-------------|-------------------|
| **Draft** | Being configured | Edit, Delete, Activate |
| **Active** | In use by system | Edit (limited), Deactivate, View Records |
| **Inactive** | Deactivated | Reactivate, Delete (if no data) |

**Note:** You can't delete an active event type that has data records.

## Common Patterns

### Pattern 1: Periodic Assessment (One Active)

**Use for:** Income verification, disability status, farm certification

```
Configuration:
✓ One Active Per Registrant
✓ Requires Approval
✓ Auto Expiry: 12 months
```

**Behavior:**
- Only one active assessment at a time
- New approval supersedes old one
- Auto-expires after 12 months (triggers reassessment)

### Pattern 2: Repeated Events (Multiple Active)

**Use for:** Attendance, field visits, training sessions

```
Configuration:
✗ One Active Per Registrant
✗ Requires Approval
✗ Auto Expiry
```

**Behavior:**
- Unlimited active events
- Immediate activation
- Manual lifecycle management

### Pattern 3: Verified External Data (Approval Flow)

**Use for:** Partner system imports, high-stakes assessments

```
Configuration:
✓ One Active Per Registrant
✓ Requires Approval
✗ Auto Expiry
```

**Behavior:**
- Awaits review before activation
- Reviewer can reject/approve
- One verified record at a time

## Integration with Data Collection

### ODK/KoboToolbox

If integrating with mobile data collection:

1. Create event type in Studio
2. Note the **Code** (used in integration mapping)
3. Configure ODK/Kobo form with matching field names
4. Set up integration in {doc}`odk_kobo`

### Manual Entry

For manual data entry:

1. Create event type
2. Activate it
3. Users can create events from:
   - Registrant record → **Event Data** button
   - Studio → Event Types → **Enter Event**

### API Import

For programmatic import:

1. Create event type
2. Note the event type code
3. Use API endpoint: `POST /api/v2/events/`
4. Include event type code in payload

## Editing Active Event Types

You can edit active event types with limitations:

| Can Edit | Cannot Edit |
|----------|-------------|
| Name, Description | Code (breaks CEL references) |
| Add new fields | Delete fields with data |
| Field labels, help text | Field technical names |
| Programs | Target type |
| Lifecycle settings | - |

**Best Practice:** Test event types in development before activating in production.

## Testing Your Event Type

Before rolling out to data collectors:

1. **Activate** the event type in a test environment
2. **Create test events** with sample data
3. **Test eligibility rules** that reference this event type
4. **Verify lifecycle** - test superseding/expiry if configured
5. **Check integrations** - test ODK/Kobo sync if applicable

## Next Steps

1. {doc}`field_definitions` - Configure field validation and visibility
2. {doc}`odk_kobo` - Connect to mobile data collection
3. {doc}`../cel/variables` - Use event data in eligibility rules

## Are You Stuck?

**Event type code changed after I saved it?**

The code is auto-generated from the name on first save. It won't change after that. If you need a different code, create a new event type.

**Can't activate - says "incomplete configuration"?**

Check that you have at least one field defined and all required fields are filled.

**Event type activated but not appearing in dropdown?**

Check:
- Is it linked to specific programs? (You might not be in that program context)
- Is target type correct? (Individual events don't show for groups)
- Refresh your browser

**How do I rename an event type?**

You can change the **Name** but not the **Code**. The code is permanent once created (used in CEL expressions and integrations).

**Can I copy an event type?**

Yes - open the event type and click **Duplicate**. This creates a new draft copy with all fields.

**What happens to old events if I change field definitions?**

Existing events keep their original data. New events use the new field definitions. This can cause mismatches - test carefully in development.
