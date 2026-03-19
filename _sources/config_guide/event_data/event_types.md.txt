---
openspp:
  doc_status: draft
  products: [core]
---

# Configuring Event Types

This guide is for **implementers** creating event type schemas in OpenSPP Studio. You should understand your program's data collection needs but don't need programming knowledge.

## Mental model

Event types work in three layers:

1. **Studio Event Type** (Designer) - Where you configure fields, validation, and lifecycle
2. **Event Type** (System) - The activated schema used by the system
3. **Event Data Records** (Runtime) - Individual event instances collected from registrants

Think of it like this:
- **Studio Event Type** = Form template you're designing
- **Event Type** = Published form available for use
- **Event Data** = Completed forms

## Creating an event type

### Step 1: Navigate to event types

Go to **Studio → Forms & Fields → Event Types**.

```{tip}
For step-by-step screenshots of this process, see {doc}`/config_guide/studio/event_type_designer`.
```

### Step 2: Create event type

Click **New** and configure:

| Field | Value | Notes |
|-------|-------|-------|
| **Event Type Name** | Household Income Survey | User-facing name |
| **Target Type** | Group/Household | Individual, Group, or Both |
| **Description** | Quarterly income verification for cash transfer program | Helps users understand when to use this event type |

```{note}
A **Code** (technical identifier used in CEL expressions) is auto-generated when you activate the event type. The code is based on the name, e.g., "Household Income Survey" becomes `household_income_survey`.
```

### Step 3: Configure approval

| Setting | Options | When to Use |
|---------|---------|-------------|
| **Requires Approval** | Yes / No | **Yes**: New events start in "Pending Approval" state<br>**No**: Events activate immediately |
| **Approval Workflow** | Select workflow | Choose the approval workflow for events requiring approval |

```{note}
Additional lifecycle settings (**One Active Per Registrant**, **Auto Expire Days**) are configured on the activated event type record, not in the Studio form. These settings control how events behave at runtime.
```

**Example configurations:**

| Event Type | Requires Approval | Use Case |
|------------|-------------------|----------|
| Income Assessment | Yes | Needs review before eligibility changes |
| Attendance | No | High volume, immediate activation |
| Disability Status | Yes | Sensitive data requires verification |
| Farm Visit | Yes | Inspector findings need approval |

### Step 4: Add fields

Click the **Fields** tab and add your data fields. See {doc}`field_definitions` for detailed field configuration.

The form also includes:
- **Field Groups** tab - Organize fields into logical sections
- **Audit Trail** tab - View change history

Quick field setup:

| Field Name | Type | Required | Example |
|------------|------|----------|---------|
| Monthly Income | Decimal | Yes | 4500.00 |
| Household Size | Integer | Yes | 5 |
| Employment Status | Selection | Yes | Employed / Unemployed / Self-employed |
| Income Source | Text | No | Farming |

### Step 5: Configure programs (optional)

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

## Event type settings reference

### Basic configuration

| Field | Description | Example |
|-------|-------------|---------|
| **Event Type Name** | Display name for users | "Household Survey" |
| **Target Type** | Individual / Group/Household / Both | Individual |
| **Description** | Help text for data collectors | "Monthly income verification" |

After activation, the system generates a **Code** (technical identifier for CEL expressions) based on the name, e.g., `household_survey`.

### Lifecycle configuration

These settings are configured on the activated event type (not in Studio form):

| Setting | Description | Impact |
|---------|-------------|--------|
| **Is One Active Per Registrant** | Only one active event allowed | New activation supersedes previous active event |
| **Is Requires Approval** | Approval workflow enabled | New events start in "Pending Approval" |
| **Auto Expire Days** | Days until auto-expiry (0 = never) | Scheduled job expires events after N days |

In the Studio form, you configure:

| Setting | Description | Impact |
|---------|-------------|--------|
| **Requires Approval** | Enable approval workflow | New events need approval before activation |
| **Approval Workflow** | Select approval definition | Defines approvers and levels |

### Program association

| Setting | Description | Effect |
|---------|-------------|--------|
| **Programs** | Linked programs | If set, only these programs see this event type |
| **Empty** | No program restriction | All programs can use this event type |

## Using event type templates

OpenSPP V2 includes reusable field templates for common assessment types. Templates are managed in **Studio → Settings → Event Templates**.

### Available templates

| Template | Category | Use Case |
|----------|----------|----------|
| **Income Assessment** | Economic | Cash transfer programs |
| **Health Screening** | Health | Health programs |
| **Field Visit** | Visit | Inspector assessments |
| **Vulnerability Assessment** | Survey | Social protection targeting |

### Applying a template

Templates can be applied when creating event types through the Event Type Builder wizard or by configuring field mappings manually.

## Event type states

After creation, event types have states:

| State | Description | Available Actions |
|-------|-------------|-------------------|
| **Draft** | Being configured | Edit, Delete, Activate |
| **Active** | In use by system | Edit (limited), Deactivate, View Records |
| **Inactive** | Deactivated | Reactivate, Delete (if no data) |

**Note:** You can't delete an active event type that has data records.

## Common patterns

### Pattern 1: Periodic assessment (one active)

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

### Pattern 2: Repeated events (multiple active)

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

### Pattern 3: Verified external data (approval flow)

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

## Integration with data collection

### ODK/KoboToolbox

If integrating with mobile data collection:

1. Create event type in Studio
2. Note the **Code** (used in integration mapping)
3. Configure ODK/Kobo form with matching field names
4. Set up integration in {doc}`odk_kobo`

### Manual entry

For manual data entry:

1. Create event type
2. Activate it
3. Users can create events from:
   - Registrant record → **Event Data** button
   - Studio → Event Types → **Enter Event**

### API import

For programmatic import:

1. Create event type
2. Note the event type code
3. Use API endpoint: `POST /api/v2/events/`
4. Include event type code in payload

## Editing active event types

You can edit active event types with limitations:

| Can Edit | Cannot Edit |
|----------|-------------|
| Name, Description | Code (breaks CEL references) |
| Add new fields | Delete fields with data |
| Field labels, help text | Field technical names |
| Programs | Target type |
| Lifecycle settings | - |

**Best Practice:** Test event types in development before activating in production.

## Testing your event type

Before rolling out to data collectors:

1. **Activate** the event type in a test environment
2. **Create test events** with sample data
3. **Test eligibility rules** that reference this event type
4. **Verify lifecycle** - test superseding/expiry if configured
5. **Check integrations** - test ODK/Kobo sync if applicable

## Next steps

1. {doc}`field_definitions` - Configure field validation and visibility
2. {doc}`odk_kobo` - Connect to mobile data collection
3. {doc}`../cel/variables` - Use event data in eligibility rules

## Are you stuck?

**Where is the Code field?**

The code is auto-generated when you activate the event type. You don't enter it manually - it's derived from the name (e.g., "Household Survey" → `household_survey`).

**Can't activate - says "incomplete configuration"?**

Check that you have at least one field defined and all required fields are filled.

**Event type activated but not appearing in dropdown?**

Check:
- Is it linked to specific programs? (You might not be in that program context)
- Is target type correct? (Individual events don't show for groups)
- Refresh your browser

**How do I rename an event type?**

You can change the **Event Type Name** but not the **Code**. The code is permanent once the event type is activated (used in CEL expressions and integrations).

**How do I configure "One Active Per Registrant" or "Auto Expire Days"?**

These settings are on the activated event type record, not in the Studio form. After activation, an administrator can configure these settings on the `spp.event.type` record.

**What happens to old events if I change field definitions?**

Existing events keep their original data. New events use the new field definitions. This can cause mismatches - test carefully in development.
