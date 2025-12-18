---
openspp:
  doc_status: draft
---

# ODK/KoboToolbox Integration

This guide is for **implementers** connecting ODK Collect or KoboToolbox to OpenSPP for mobile data collection. You should be familiar with creating forms in ODK/Kobo but don't need programming knowledge.

## Mental Model

The integration has three layers:

```
Mobile Form (ODK/Kobo) → Sync Configuration (OpenSPP) → Event Data (OpenSPP)
```

| Layer | What It Does | Where You Configure |
|-------|--------------|---------------------|
| **Mobile Form** | Data collection questionnaire | ODK/KoboToolbox platform |
| **Sync Configuration** | Maps form fields to event fields | OpenSPP Studio |
| **Event Data** | Stores collected data | Automatic (created by sync) |

Think of it like:
- **Mobile form** = The questions you ask in the field
- **Sync configuration** = The translation rules
- **Event data** = The answers stored in OpenSPP

## Prerequisites

Before setting up integration:

1. **ODK/Kobo account** with form already created
2. **Event type** created in OpenSPP Studio (see {doc}`event_types`)
3. **API credentials** for your ODK/Kobo account
4. **Field mapping** - know which form questions map to which event fields

## Integration Options

OpenSPP V2 supports two integration approaches:

| Approach | When to Use | Direction |
|----------|-------------|-----------|
| **Pull Sync** | Periodic import from ODK/Kobo | ODK/Kobo → OpenSPP |
| **Push Sync** | Real-time submission to OpenSPP | ODK/Kobo → OpenSPP (immediate) |

**Most implementations use Pull Sync** (scheduled every 15-60 minutes).

## Setup: Pull Sync (Recommended)

### Step 1: Create Event Type in OpenSPP

First, create your event type in **Studio → Event Types** with fields matching your ODK/Kobo form.

**Example: Income Survey**

| Field Label | Technical Name | Type |
|-------------|---------------|------|
| Respondent ID | `respondent_id` | Text |
| Monthly Income | `monthly_income` | Decimal |
| Household Size | `household_size` | Integer |
| Has Employment | `has_employment` | Boolean |

See {doc}`event_types` and {doc}`field_definitions` for details.

### Step 2: Note Event Type Code

After activating the event type, note its **Code** (e.g., `income_survey`). You'll need this for the sync configuration.

### Step 3: Configure ODK/Kobo Connection

Go to **Studio → External Data Sources** → **Create**.

| Setting | Value | Example |
|---------|-------|---------|
| **Name** | Descriptive name | "KoboToolbox Income Survey" |
| **Source Type** | ODK Central / KoboToolbox | KoboToolbox |
| **API URL** | Your server URL | `https://kf.kobotoolbox.org` |
| **Username** | Your ODK/Kobo username | `datamanager@example.org` |
| **API Token** | Your API token | (from Kobo account settings) |

**Getting your Kobo API token:**
1. Log in to KoboToolbox
2. Go to **Account Settings**
3. Navigate to **Security**
4. Copy your **API Token**

### Step 4: Link Form to Event Type

In the External Data Source configuration:

| Setting | Value |
|---------|-------|
| **Form ID** | ODK/Kobo form identifier |
| **Event Type** | Select your event type |
| **Sync Schedule** | Every 15 minutes / Hourly / Custom |

**Finding your Kobo Form ID:**
1. Open your form in KoboToolbox
2. Go to **Settings**
3. Copy the **Form ID** (e.g., `aABcDeFg123`)

### Step 5: Configure Field Mapping

Map ODK/Kobo form questions to OpenSPP event fields:

| ODK/Kobo Field Name | OpenSPP Event Field | Transformation |
|---------------------|---------------------|----------------|
| `respondent_national_id` | `respondent_id` | Direct mapping |
| `monthly_income_usd` | `monthly_income` | Direct mapping |
| `household_size` | `household_size` | Direct mapping |
| `has_employment` | `has_employment` | Yes/No → True/False |

**Field mapping configuration:**

```
ODK/Kobo Question Name: monthly_income_usd
  → OpenSPP Field: monthly_income
  → Type: Decimal
  → Required: Yes

ODK/Kobo Question Name: has_employment
  → OpenSPP Field: has_employment
  → Type: Boolean
  → Transform: "Yes" → true, "No" → false
```

### Step 6: Map Registrant Identifier

**Critical:** Tell OpenSPP which form field identifies the registrant.

| Setting | Value | Notes |
|---------|-------|-------|
| **Registrant ID Field** | `respondent_national_id` | Form field containing national ID |
| **ID Type** | National ID / Passport / Custom | How to match registrant |
| **Create if Not Found** | Yes / No | Auto-create registrant if no match? |

**Matching logic:**
- System searches for registrant with matching ID number
- If found, creates event for that registrant
- If not found and "Create if Not Found" = No, submission is rejected
- If not found and "Create if Not Found" = Yes, new registrant is created

### Step 7: Test Connection

Click **Test Connection** to verify:
- API credentials are correct
- Form is accessible
- Field mappings are valid

### Step 8: Activate Sync

Click **Activate** to start automatic syncing.

**What happens:**
- Scheduled job runs every N minutes (based on sync schedule)
- Fetches new submissions from ODK/Kobo
- Creates draft event records in OpenSPP
- If "Requires Approval" is enabled on event type, events await approval
- Otherwise, events are automatically activated

## Field Mapping Details

### Direct Mappings

Most fields map directly:

| ODK/Kobo Type | OpenSPP Type | Notes |
|---------------|--------------|-------|
| **text** | Text | Direct mapping |
| **integer** | Integer | Direct mapping |
| **decimal** | Decimal | Direct mapping |
| **date** | Date | Format: YYYY-MM-DD |
| **datetime** | DateTime | ISO 8601 format |

### Boolean Transformations

| ODK/Kobo Value | OpenSPP Value |
|----------------|---------------|
| "Yes" | `true` |
| "No" | `false` |
| "1" | `true` |
| "0" | `false` |

### Selection Transformations

ODK/Kobo select_one → OpenSPP Selection

**Ensure option values match exactly** (case-sensitive):

| ODK/Kobo Options | OpenSPP Options |
|------------------|-----------------|
| `employed` | Employed |
| `unemployed` | Unemployed |
| `self_employed` | Self-employed |

**Transformation rule:**
```
employed → Employed (capitalize)
unemployed → Unemployed
self_employed → Self-employed (replace underscore with space, capitalize)
```

### Multi-Select Transformations

ODK/Kobo select_multiple → OpenSPP Multi-Select

**Example:**
```
ODK/Kobo: "maize beans rice" (space-separated)
OpenSPP: ["Maize", "Beans", "Rice"] (array)
```

### GPS Coordinates

ODK/Kobo geopoint → OpenSPP fields

| ODK/Kobo Field | OpenSPP Fields |
|----------------|----------------|
| `location` (geopoint) | `latitude` (Decimal) + `longitude` (Decimal) |

**Mapping:**
```
location: "1.2345 -36.7890 0 0"
  → latitude: 1.2345
  → longitude: -36.7890
```

## Common Integration Patterns

### Pattern 1: Simple Survey Import

**Use case:** Monthly income verification surveys

**ODK/Kobo form structure:**
```
- respondent_id (text)
- monthly_income (decimal)
- household_size (integer)
- survey_date (date)
```

**OpenSPP event type:**
- Code: `income_survey`
- Fields: Match ODK form
- One Active Per Registrant: Yes
- Requires Approval: Yes

**Sync configuration:**
- Schedule: Every hour
- Registrant ID: `respondent_id` (National ID)
- Create if Not Found: No (reject if registrant doesn't exist)

### Pattern 2: Repeated Attendance Tracking

**Use case:** Daily school attendance

**ODK/Kobo form structure:**
```
- student_id (text)
- attendance_date (date)
- attended (select_one: yes/no)
- reason_absent (text, relevant if attended=no)
```

**OpenSPP event type:**
- Code: `attendance`
- Fields: Match ODK form
- One Active Per Registrant: No (keep all records)
- Requires Approval: No (auto-activate)

**Sync configuration:**
- Schedule: Every 15 minutes
- Registrant ID: `student_id` (National ID)
- Create if Not Found: No

### Pattern 3: Field Verification with Photos

**Use case:** Farm certification visits with photos

**ODK/Kobo form structure:**
```
- farmer_id (text)
- visit_date (date)
- hectares (decimal)
- crops (select_multiple)
- certified (select_one: yes/no)
- farm_photo (image)
- inspector_notes (text)
```

**OpenSPP event type:**
- Code: `farm_visit`
- Fields: Match ODK form (plus `photo_url` for image)
- One Active Per Registrant: No
- Requires Approval: Yes

**Sync configuration:**
- Schedule: Every 30 minutes
- Registrant ID: `farmer_id` (National ID)
- Create if Not Found: No
- Photo Handling: Upload to filestore, store URL in `photo_url`

## Handling Attachments (Photos, Audio, Files)

ODK/Kobo forms can include media attachments.

### Configuration

| Setting | Value |
|---------|-------|
| **Download Attachments** | Yes / No |
| **Storage Location** | OpenSPP Filestore / External URL |
| **File Field Mapping** | Map to event field (stores URL/path) |

**Example:**
```
ODK/Kobo field: farm_photo (image)
  → Download: Yes
  → Store in: Filestore
  → OpenSPP field: photo_url (Text)
  → Value: "/filestore/events/farm_visit/12345_farm_photo.jpg"
```

## Error Handling

### Sync Errors

Common errors and solutions:

| Error | Cause | Solution |
|-------|-------|----------|
| **Registrant not found** | No matching ID in OpenSPP | Enable "Create if Not Found" or verify IDs |
| **Field mapping error** | ODK field missing or renamed | Update field mapping configuration |
| **Type mismatch** | Wrong data type (e.g., text in number field) | Fix ODK form or add transformation |
| **Required field missing** | ODK submission missing required field | Make field required in ODK form |
| **API authentication failed** | Invalid credentials or token expired | Update API token in configuration |

### Monitoring Sync Status

Check sync status in **Studio → External Data Sources**:

| Status | Meaning | Action |
|--------|---------|--------|
| **Active** | Syncing successfully | None |
| **Error** | Last sync failed | Check error log |
| **Paused** | Manually paused | Resume when ready |

**Error log shows:**
- Timestamp of failure
- Error message
- Affected submissions (by submission ID)
- Stack trace (for technical debugging)

## Testing Your Integration

### Step-by-Step Test

1. **Create test registrant** in OpenSPP with known ID
2. **Fill test form** in ODK/Kobo using that ID
3. **Submit form** from mobile device
4. **Wait for sync** (or trigger manual sync)
5. **Check OpenSPP** - Event Data should appear for registrant
6. **Verify data** - All fields mapped correctly
7. **Test approval workflow** (if enabled)

### Test Checklist

- [ ] All fields map correctly
- [ ] Registrant matching works (by ID)
- [ ] Boolean transformations correct (Yes/No → true/false)
- [ ] Selection options match exactly
- [ ] Multi-select fields parse correctly
- [ ] GPS coordinates split properly (if applicable)
- [ ] Photos/attachments download and link correctly
- [ ] Sync runs on schedule
- [ ] Errors are logged and visible
- [ ] Approval workflow works (if enabled)

## Sync Scheduling

### Recommended Schedules

| Use Case | Sync Frequency | Reason |
|----------|---------------|--------|
| **Attendance** | Every 15 minutes | Near real-time needed |
| **Surveys** | Every hour | Balance freshness and load |
| **Assessments** | Every 4 hours | Not time-critical |
| **Monthly reports** | Daily | Low urgency |

### Manual Sync

You can also trigger sync manually:

1. Go to **Studio → External Data Sources**
2. Open your data source
3. Click **Sync Now**

**Use manual sync for:**
- Testing new configurations
- Recovering from errors
- One-time imports

## Security Considerations

### API Token Security

**Best practices:**
- Store tokens securely (OpenSPP encrypts them)
- Use read-only tokens if possible (not supported by all ODK/Kobo servers)
- Rotate tokens periodically
- Revoke tokens immediately if compromised

### Data Privacy

**Configuration:**

| Setting | Recommendation |
|---------|---------------|
| **HTTPS only** | Always use HTTPS for API URLs |
| **Encryption** | Enable encryption for sensitive data in ODK/Kobo |
| **Access control** | Limit who can view/edit sync configuration |

### Registrant Matching

**Be careful with:**
- Auto-create registrant (could create duplicates)
- ID matching (ensure IDs are unique and consistent)

**Best practice:**
- Require exact ID match
- Use national ID or other official identifier
- Validate IDs in ODK form before submission

## Troubleshooting

### Problem: Submissions Not Appearing

**Check:**
1. Sync is active (not paused)
2. API credentials valid
3. Form ID correct
4. Submissions exist in ODK/Kobo
5. Sync schedule has run (check last sync time)

**Debug:**
- Trigger manual sync
- Check error log
- Verify API token not expired

### Problem: Registrant Not Matched

**Check:**
1. ID field mapping correct
2. ID values match exactly (no extra spaces, correct case)
3. Registrant exists in OpenSPP
4. ID type configuration matches registrant's ID type

**Debug:**
- Search for registrant manually in OpenSPP
- Compare ID from form with ID in OpenSPP
- Check for leading/trailing spaces

### Problem: Field Values Incorrect

**Check:**
1. Field mapping configuration
2. Data type transformations
3. Selection option spellings (case-sensitive)

**Debug:**
- View raw ODK submission data
- Compare with event data in OpenSPP
- Check transformation rules

### Problem: Photos Not Downloading

**Check:**
1. "Download Attachments" enabled
2. File field mapped correctly
3. Storage location configured
4. API has permission to access attachments

**Debug:**
- Check file size limits
- Verify network connectivity
- Check filestore permissions

## Advanced: Custom Transformations

For complex mappings, you can configure custom transformations.

**Example: Calculate age from birthdate**

```
ODK field: birthdate (date)
  → Transformation: age_years(birthdate)
  → OpenSPP field: age (Integer)
```

**Example: Concatenate fields**

```
ODK fields: first_name + last_name
  → Transformation: concat(first_name, " ", last_name)
  → OpenSPP field: full_name (Text)
```

**Note:** Custom transformations require technical configuration. Contact your OpenSPP administrator.

## Next Steps

1. {doc}`event_types` - Understand event type configuration
2. {doc}`field_definitions` - Configure event fields
3. {doc}`../cel/variables` - Use event data in eligibility rules

## Are You Stuck?

**Can't get API token from KoboToolbox?**

Go to your Kobo account → Settings → Security → API Token. If you don't see it, contact your Kobo administrator.

**Sync configuration saved but not syncing?**

Check:
- Sync is activated (not just saved)
- Schedule is configured
- Scheduled job is running (check with system administrator)

**All submissions being rejected?**

Most likely issue: Registrant ID matching. Check:
- ID field is mapped correctly
- IDs exist in OpenSPP
- "Create if Not Found" setting

**Getting "Form not found" error?**

Verify:
- Form ID is correct (check Kobo settings)
- Form is deployed (not draft)
- API credentials have access to the form

**How often should I sync?**

Balance between:
- Data freshness needed (near real-time vs. daily)
- Server load (more frequent = higher load)
- Number of submissions expected

**Can I sync multiple forms to one event type?**

Yes, create multiple External Data Source configurations pointing to the same event type. Useful for:
- Different languages of same form
- Staged rollout (different regions)
- Different versions (migrate from old to new)
