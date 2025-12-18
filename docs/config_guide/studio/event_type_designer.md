---
openspp:
  doc_status: draft
---

# Event Type Designer

This guide is for **implementers** creating event types to capture field data and survey responses. You should be familiar with KoBoToolbox or ODK, but you don't need programming knowledge.

## What is Event Type Designer?

Event Type Designer lets you create new survey and assessment types for capturing time-based observations about registrants. Import field definitions directly from KoBoToolbox or ODK forms, or create event types from scratch.

## When to Use Event Type Designer

Use this tool when you collect data that changes over time or comes from field visits:

| Use Case | Example Event Type |
|----------|-------------------|
| Vulnerability assessments | "PMT Survey" with scoring fields |
| Field visits | "Monthly Household Visit" tracking |
| Verification surveys | "Household Verification" checklist |
| Program monitoring | "Compliance Check" for conditional programs |
| Health assessments | "Nutrition Survey" for mother-child programs |

## Mental Model: Events vs Registry Fields

| Registry Fields | Event Data |
|----------------|------------|
| Permanent characteristics | Time-based observations |
| Name, birthdate, gender | Survey responses, visit notes |
| Changes rarely | Changes regularly |
| One value at a time | Multiple records over time |
| Examples: "Date of Birth" | Examples: "Monthly Income Assessment" |

**Rule of thumb**: If you need to track history ("What was the value in June?"), use an event type. If you just need the current value, use a registry field.

## Before You Start

### Prerequisites

- **Studio Editor** or **Studio Manager** permissions
- For Kobo/ODK import:
  - Access to KoBoToolbox or ODK Central server
  - API token or credentials
  - Published form ready to import

### Planning Your Event Type

Decide:

1. **Name**: Clear, descriptive name (e.g., "Vulnerability Assessment")
2. **Category**: Survey, Field Visit, Data Sync, or Manual Entry
3. **Target**: Individuals, Groups, or both
4. **Data source**: Internal, Kobo, ODK, or API
5. **Fields**: What data to collect
6. **Lifecycle**: One active per registrant? Auto-expire? Requires approval?

## Creating an Event Type

### Step 1: Open Event Type Designer

1. Click **Studio** in the main menu
2. Click **Event Types**
3. Click **+ New Event Type** button

**Screenshot should show**: Studio Dashboard with Event Types card highlighted, then Event Type Designer list view with "+ New Event Type" button.

### Step 2: Enter Basic Information

| Field | What to Enter | Example |
|-------|---------------|---------|
| **Event Type Name** | Descriptive name | "Vulnerability Assessment" |
| **Code** | Auto-generated, used in reports | `vulnerability_assessment` |
| **Category** | Choose one (see below) | Survey / Assessment |
| **Applies to** | Individual, Group, or both | ☑ Individuals  ☑ Groups |

**Screenshot should show**: Step 1 of event type creation wizard with fields filled in.

#### Category Options

| Category | Use When |
|----------|----------|
| **Survey / Assessment** | Collecting structured survey data |
| **Field Visit** | Recording visit observations |
| **Data Sync** | Importing from external system automatically |
| **Manual Entry** | Staff enter data directly in OpenSPP |

Click **Next →** when ready.

### Step 3: Choose Data Source

You'll see four options:

**Screenshot should show**: Step 2 of wizard with four data source cards (Internal, KoBoToolbox, ODK Central, API).

| Source | Use When |
|--------|----------|
| **📱 Internal** | Data entered directly in OpenSPP |
| **🌐 KoBoToolbox** | Import from Kobo forms |
| **📋 ODK Central** | Import from ODK server |
| **🔌 API** | Custom API integration (advanced) |

Choose your data source and click **Next →**.

### Step 3b: Connect to KoBoToolbox (if selected)

If you chose KoBoToolbox as the source:

#### Select or Add Connection

**If you already have a Kobo connection**:
- Select existing connection (e.g., "UNHCR Kobo Server")

**If this is your first time**:
- Select "+ Add new connection..."
- See "Connecting to KoBoToolbox" section below

**Screenshot should show**: Connection selection screen with saved connections listed and "+ Add new connection..." option.

#### Select Form to Import

1. The system fetches all published forms from your Kobo server
2. Search or browse for your form
3. Select the form

**Screenshot should show**: Form selection screen showing list of Kobo forms with names and "Last submission" times.

| Form | Last Submission |
|------|----------------|
| (•) Vulnerability Assessment v3.2 | 2 days ago |
| ( ) Household Survey 2024 | 1 week ago |
| ( ) Rapid Needs Assessment | 3 weeks ago |

#### Configure Registrant Matching

Tell OpenSPP how to match survey submissions to registrants:

| Setting | What to Enter |
|---------|---------------|
| **Kobo field** | Which field contains the beneficiary ID | `beneficiary_id` |
| **ID Type** | What kind of ID it is | National ID, Phone Number, etc. |

**Screenshot should show**: Registrant matching configuration with dropdowns for Kobo field and ID type.

**Example**:
```
Your Kobo form has a field called "beneficiary_id" where
enumerators enter the person's National ID number.

Kobo field: [beneficiary_id ▼]
ID Type: [National ID ▼]
```

Click **Next →** when configured.

### Step 4: Define Fields

You'll see fields imported from your Kobo form (or an empty list for internal event types).

**Screenshot should show**: Step 3 of wizard showing imported fields table with checkboxes in Import column.

#### For Imported Fields (Kobo/ODK)

The system automatically maps Kobo question types to OpenSPP field types:

| Kobo Type | OpenSPP Type | Example |
|-----------|--------------|---------|
| text | Text | Short answer |
| integer | Number (whole) | Count |
| decimal | Number (decimal) | Amount |
| date | Date | Date picker |
| select_one | Selection | Dropdown |
| select_multiple | Text (array) | Multiple choices |
| geopoint | Text | GPS coordinates |

Review the imported fields:

| Column | What It Shows |
|--------|---------------|
| **Field Name** | Internal name from Kobo |
| **Type** | OpenSPP field type |
| **Required** | Whether field is mandatory |
| **Import?** | Uncheck to skip fields you don't need |

**Screenshot should show**: Fields table with several rows, some checked and some unchecked in Import column.

**Tips**:
- Uncheck fields you don't need (e.g., GPS coordinates, metadata)
- Required status is inherited from Kobo form
- You can edit field settings after import

#### For Internal Event Types

Click **+ Add Field** to create each field:

| Setting | What to Enter |
|---------|---------------|
| **Field Name** | Internal name (lowercase, no spaces) |
| **Label** | What users see |
| **Type** | Field type (text, number, date, etc.) |
| **Required** | Must be filled? |

Click **Next →** when fields are defined.

### Step 5: Configure Lifecycle Settings

Control how events behave over time:

**Screenshot should show**: Step 4 of wizard showing lifecycle options.

#### Event Lifecycle Options

| Option | Use When | Example |
|--------|----------|---------|
| **Only one active event per registrant** | Latest assessment supersedes previous ones | Vulnerability score (only most recent matters) |
| **Auto-expire after X days** | Event data becomes stale | Monthly visit (expires after 45 days) |
| **Require approval before activating** | Events need validation | Survey data needs QC review |

#### Change Request Integration

| Option | Use When |
|--------|----------|
| **Create change request when event data differs from registry** | Survey responses should update registry | Phone number in survey differs from registry → create CR |

If enabled, configure:
- Which CR type to create
- Which fields to compare

**Screenshot should show**: Change request integration checkbox checked with CR Type dropdown showing "Update Individual Info".

#### Preview

The wizard shows a summary of your settings:

```
Events of this type will:
• Replace previous active event (one per registrant)
• Be immediately active (no approval required)
• Never expire automatically
```

Click **Save as Draft** to create the event type.

## Connecting to KoBoToolbox

### Setting Up a Kobo Connection

1. In KoBoToolbox, generate an API token:
   - Log in to Kobo
   - Click your profile → Account Settings
   - Go to Security → API Token
   - Copy the token

**Screenshot should show**: KoBoToolbox interface showing Account Settings > Security > API Token.

2. In OpenSPP Studio:
   - Studio → External Sources → + Connect KoBoToolbox
   - Or during event type creation → + Add new connection

3. Fill in connection details:

| Field | What to Enter | Example |
|-------|---------------|---------|
| **Connection Name** | Memorable name for this server | "UNHCR Kobo Server" |
| **Server URL** | Kobo server address | `https://kf.kobotoolbox.org` |
| **API Token** | Token from step 1 | `••••••••••••••••` |

**Screenshot should show**: Kobo connection form with fields filled in.

4. Click **Test Connection**
   - System verifies credentials
   - Shows number of forms found
   - ✓ "Connected successfully! Found 47 forms."

5. Click **Save**

**Security note**: API tokens are stored encrypted and only visible to Studio Managers.

## Connecting to ODK Central

Similar to Kobo, but using ODK credentials:

1. In ODK Central, create an App User:
   - Open your project
   - Go to App Users
   - Create new app user
   - Copy the credentials

2. In OpenSPP:
   - Studio → External Sources → + Connect ODK Central

3. Fill in connection details:

| Field | What to Enter |
|-------|---------------|
| **Connection Name** | Memorable name |
| **Server URL** | ODK Central URL |
| **Email** | App user email |
| **Password** | App user password |
| **Project** | Select project from dropdown |

## After Creating an Event Type

### Test Your Event Type

1. Go to **Registry → Individuals** (or Groups)
2. Open a registrant record
3. Go to **Events** tab
4. Click **+ Add Event**
5. Select your new event type
6. Enter test data
7. Save

**Screenshot should show**: Individual registry form with Events tab open, showing "+ Add Event" button and event type selection.

### Activate the Event Type

Once tested:

1. Return to **Studio → Event Types**
2. Find your event type
3. Click to open it
4. Click **Activate** (requires Studio Manager permission)

**Screenshot should show**: Event type detail view with "Activate" button.

## Fetching Data from Kobo/ODK

### Manual Fetch (Phase 1)

For event types connected to Kobo/ODK:

1. Open the event type
2. Click **Actions → Fetch Latest Submissions**
3. System fetches new submissions since last sync
4. Shows summary:
   - "Fetched 45 submissions"
   - "Created 42 events"
   - "3 unmatched" (couldn't find registrant)

**Screenshot should show**: Fetch results dialog showing summary statistics.

### Unmatched Submissions

If submissions can't be matched to registrants:

1. Click **View Unmatched**
2. Shows list of submissions with the ID that couldn't be matched
3. Options:
   - Register the person first, then retry
   - Ignore if submission is invalid
   - Contact field team if IDs are incorrect

### Automatic Sync (Phase 2 - Future)

Future capabilities:
- Webhook receiver for real-time push from Kobo/ODK
- Scheduled automatic fetch (daily, hourly, etc.)
- Automatic event creation on submission

## Managing Event Types

### View All Event Types

**Studio → Event Types** shows all event types:

**Screenshot should show**: Event Type list view with columns.

| Column | Shows |
|--------|-------|
| **Name** | Event type name |
| **Category** | Survey, Visit, Sync, Manual |
| **Source** | Internal, Kobo, ODK, API |
| **Fields** | Number of fields |
| **Status** | Draft or Active |

### Edit an Event Type

**For Draft event types**:
- Click the name
- Make changes
- Save

**For Active event types**:
- Cannot edit structure (fields, source)
- Can edit name, category, lifecycle settings
- To change fields: Create new version, migrate data (requires developer)

### Deactivate an Event Type

**Warning**: Deactivating prevents new events of this type, but existing events remain.

1. Open the event type
2. Click **Deactivate**
3. System shows impact: "Used by 1,247 event records"
4. Confirm deactivation

## Field Type Mapping Reference

### From Kobo to OpenSPP

| Kobo Type | OpenSPP Type | Storage | Notes |
|-----------|--------------|---------|-------|
| text | char | Text | Up to 256 characters |
| integer | integer | Number | Whole numbers |
| decimal | float | Number | Decimal numbers |
| date | date | Date | Calendar picker |
| datetime | datetime | DateTime | Date and time |
| select_one | selection | Selection | Dropdown (imports choices) |
| select_multiple | json | Text | Multiple selections stored as array |
| geopoint | char | Text | Stored as "lat,lng" |
| image | binary | Attachment | File attachment |
| note | - | - | Skipped (display only in Kobo) |
| calculate | - | - | Skipped (Kobo internal) |
| begin_group | - | - | Skipped (structural) |

### Supported Field Types for Internal Events

| Type | Use For |
|------|---------|
| **Text** | Short answers, names, codes |
| **Long Text** | Notes, descriptions |
| **Number** | Counts, scores, amounts |
| **Date** | Assessment dates, visit dates |
| **Yes/No** | Checklists, true/false |
| **Selection** | Dropdown choices |
| **Multi-Select** | Multiple choice questions |

## Common Patterns

### Vulnerability Assessment from Kobo

```
Event Type: Vulnerability Assessment
Category: Survey / Assessment
Source: KoBoToolbox
Form: "PMT Survey v2.1"
Applies to: Groups (households)
Lifecycle: One active per household
Registrant Matching:
  - Kobo field: household_id
  - ID Type: National ID (head of household)
Fields: (imported from Kobo)
  - housing_material
  - water_source
  - toilet_type
  - electricity_access
  - vulnerability_score (calculated in Kobo)
```

### Monthly Household Visit

```
Event Type: Monthly Household Visit
Category: Field Visit
Source: Internal
Applies to: Groups (households)
Lifecycle:
  - Multiple events allowed
  - Auto-expire: No
  - Require approval: No
Fields:
  - visit_date (Date, Required)
  - household_present (Yes/No, Required)
  - compliance_status (Selection: Compliant/Non-compliant/Pending)
  - notes (Long Text)
```

### Health Check (from ODK)

```
Event Type: Child Health Check
Category: Survey / Assessment
Source: ODK Central
Form: "Nutrition Survey 2024"
Applies to: Individuals only
Lifecycle:
  - Multiple events allowed (track over time)
  - No expiration
Registrant Matching:
  - ODK field: child_id
  - ID Type: Health Card Number
Change Request Integration:
  - Enabled
  - CR Type: Update Individual Info
  - Compare fields: weight, height
```

## Are You Stuck?

**Can't see my Kobo forms?**
- Verify API token is correct
- Check that forms are published in Kobo
- Ensure you're connected to the right server (kf.kobotoolbox.org vs kobo.humanitarianresponse.info)
- Click "Test Connection" to verify

**Event type created but no events appear?**
- For Kobo/ODK: Have you clicked "Fetch Latest Submissions"?
- Check that submissions contain valid registrant IDs
- View unmatched submissions to see which IDs failed

**Fields imported incorrectly from Kobo?**
- Some Kobo field types don't map perfectly (groups, calculate fields are skipped)
- Edit field definitions after import if needed
- For complex mappings, contact a developer

**Getting "registrant not found" errors?**
- Verify the ID type matches what's in your registry
- Check that field team is entering correct ID format
- Ensure registrants are enrolled before submitting surveys

**Can't activate event type?**
- You need Studio Manager permission
- Make sure event type is fully configured (all required settings)
- Check that event type name is unique

**Want to change fields after activation?**
This is difficult because existing events use the old structure. Options:
- Deactivate old type, create new type (existing data remains separate)
- Contact developer for data migration

**Event data not appearing in registry?**
- Check the Events tab on registrant record
- Verify event is Active (not Draft or Superseded)
- Refresh the page

**How do I export event data?**
Event data export is not part of Studio. Contact administrator for reports or data exports.

**Can I use the same Kobo form for multiple event types?**
Yes, but not recommended. Each event type should have its own Kobo form for clarity.

**What if registrants have multiple active events?**
Depends on lifecycle settings:
- "One active per registrant" → Latest supersedes previous
- Multiple allowed → All events remain active and visible

## Next Steps

- **Build approval workflows for updates**: {doc}`change_request_builder`
- **Define eligibility rules using event data**: {doc}`eligibility_rule_builder`
- **Add custom registry fields**: {doc}`registry_field_builder`
- **Return to Studio overview**: {doc}`overview`
