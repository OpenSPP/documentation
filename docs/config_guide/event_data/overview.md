---
openspp:
  doc_status: draft
  products: [core]
---

# Event Data Overview

This guide is for **implementers** configuring event-based data collection in OpenSPP. You should be comfortable with logic builders like KoboToolbox or CommCare, but you don't need to write code.

## Mental Model

Event data in OpenSPP has three key differences from profile fields:

| Profile Fields | Event Data |
|----------------|------------|
| **One value** per registrant | **Many events** per registrant |
| **Overwrites** when updated | **Preserves history** (draft → active → superseded) |
| **No source tracking** | **Records who, when, and from where** |

Think of it like this:
- **Profile fields** are like a person's ID card - one current state
- **Event data** is like their medical records - dated observations over time

## What is Event Data?

Event data records **time-based observations** about registrants (individuals or groups) from external sources like:

- Mobile surveys (ODK, KoboToolbox)
- Field visits (assessments, verification)
- Partner system data (health records, education records)
- Periodic assessments (income verification, disability status)

Each event record contains:
- **Event Type** - What was collected (e.g., "Household Survey")
- **Registrant** - Who it's about (individual or group)
- **Collection Date** - When it was collected
- **Data Fields** - The actual values (income, household size, etc.)
- **Metadata** - Collector name, source system, verification status
- **Lifecycle State** - Draft, Active, Superseded, Expired

## Why Use Event Data?

Use event data instead of profile fields when:

| Situation | Why Event Data? |
|-----------|-----------------|
| **Data changes over time** | Track history instead of overwriting |
| **Multiple assessments** | Keep separate records for each assessment |
| **External data sources** | Maintain source information and sync status |
| **Approval workflows** | Move data through draft → approved → active states |
| **Temporal eligibility** | Check "income in last 12 months" or "recent visit" |
| **Data quality tracking** | Know who collected it, when, and verification status |

## Common Use Cases

### Use Case 1: Poverty Verification

**Goal:** Track household income assessments over time, use latest for eligibility.

**Setup:**
- Event Type: "Income Assessment"
- Fields: `monthly_income`, `household_size`, `employment_status`
- Configuration: One active event per household
- Collection: Field workers use KoboToolbox form

**In Eligibility Rule:**
```cel
event('income_assessment').monthly_income < 5000
```

### Use Case 2: School Attendance Tracking

**Goal:** Count attendance days for school feeding program.

**Setup:**
- Event Type: "Attendance"
- Fields: `attended` (yes/no), `reason_absent` (if applicable)
- Configuration: Multiple events allowed
- Collection: Daily from school management system

**In Eligibility Rule:**
```cel
events_count('attendance', period='2024', where='attended == true') >= 180
```

### Use Case 3: Disability Assessment

**Goal:** Record disability status with periodic reassessment.

**Setup:**
- Event Type: "Disability Assessment"
- Fields: `is_disabled`, `disability_type`, `support_needed`, `assessment_score`
- Configuration: One active event per person, expires after 24 months
- Collection: Health workers using mobile forms with photos

**In Eligibility Rule:**
```cel
has_event('disability_assessment', within_days=730)
and event('disability_assessment').is_disabled == true
```

### Use Case 4: Farm Certification

**Goal:** Track farm certification for agricultural support program.

**Setup:**
- Event Type: "Farm Visit"
- Fields: `hectares`, `certified`, `crops`, `pest_infestation`, `inspector_notes`
- Configuration: Keep all visits (historical record)
- Collection: Inspector tablet app

**In Eligibility Rule:**
```cel
event('farm_visit', select='latest').certified == true
and event('farm_visit').hectares >= 2
and event('farm_visit').hectares <= 10
```

## Event Lifecycle

Events move through states:

```
Draft → Pending Approval → Active → Superseded/Expired/Cancelled/Inactive
```

| State | Meaning | When Used |
|-------|---------|-----------|
| **Draft** | Captured but not final | Data entry in progress |
| **Pending Approval** | Awaiting review | When event type requires approval |
| **Active** | Current official data | After approval or direct activation |
| **Superseded** | Replaced by newer event | When new event activates (if "one active per registrant") |
| **Expired** | Past validity period | Auto-expired by scheduled job |
| **Cancelled** | Manually cancelled | User or system cancelled the event |
| **Inactive** | Deactivated | Event deactivated but preserved for history |

### Configuration Options

| Setting | Effect |
|---------|--------|
| **One Active Per Registrant** | New active event supersedes previous active one |
| **Allow Multiple Active** | Many active events can coexist |
| **Requires Approval** | New events start in "Pending Approval" |
| **Expiry Period** | Auto-expire active events after N days/months |

## When NOT to Use Event Data

Don't use event data when:

| Situation | Use Instead |
|-----------|-------------|
| Simple one-time registration data | Profile fields (name, birthdate, ID number) |
| Data that truly never changes | Profile fields (place of birth) |
| Calculated/derived values | Variables or computed fields |
| Real-time status flags | Profile fields with state machines |

## Event Data vs. Other Features

| Feature | When to Use |
|---------|-------------|
| **Profile Fields** | Stable registrant data (name, gender, birthdate) |
| **Event Data** | Time-based observations (surveys, visits, assessments) |
| **Variables** | Calculated values (from profile, members, or events) |
| **Change Requests** | Workflow for updating profile data |
| **Program Membership** | Enrollment status and dates |

## Next Steps

1. {doc}`event_types` - Create your first event type
2. {doc}`field_definitions` - Define custom fields with validation
3. {doc}`odk_kobo` - Connect ODK or KoboToolbox for mobile data collection

## Are You Stuck?

**Can't decide between profile field and event data?**

Ask yourself: "Do I need to know the history or just the current value?" If history matters, use event data.

**Event types vs. event records - what's the difference?**

Event *type* is the schema/template (like a form definition). Event *record* is an instance (like a filled form).

**How do I reference event data in eligibility rules?**

Use CEL functions: `event()`, `has_event()`, `events_count()`. See {doc}`../cel/variables` for full syntax.

**Should every survey become an event type?**

Only if you need the data in OpenSPP. If it's just for M&E dashboards elsewhere, keep it in your survey tool.
