---
openspp:
  doc_status: draft
---

# Manage hazard incidents

This guide is for **users** — hazard officers and managers who record disaster events, identify affected registrants, and track damage impacts in OpenSPP.

## What you will do

Record a hazard incident, define the geographic areas it affects, identify registrants in those areas, log their damage levels, verify impacts, and advance the incident through its lifecycle stages to closure.

## Before you start

You need one of these roles:

| Role | What you can do |
|------|----------------|
| **Hazard Officer** | Create incidents, add areas, and record impacts |
| **Hazard Manager** | Full access, including delete and category configuration |

If you cannot see the **Hazard and Emergency** menu, contact your administrator.

---

## Step 1. Create an incident

1. Go to **Hazard and Emergency > Incidents** and click **New**.
2. Fill in the incident form:

| Field | What to enter |
|-------|--------------|
| **Name** | A descriptive title, e.g., "Typhoon Odette – December 2021" |
| **Code** | A short reference code for the incident |
| **Category** | Select the hazard type (e.g., Natural > Storm > Typhoon) |
| **Start date** | When the incident began |
| **End date** | Leave blank if the incident is still ongoing |
| **Severity** | Rate 1 (minor) to 5 (catastrophic) |
| **Description** | A summary of the event |

3. Click **Save**. The incident is created in **Alert** status.

```{note}
The **Category** field uses a hierarchical structure. You can select a broad category (e.g., "Natural Disaster") or a specific sub-type (e.g., "Typhoon"). Use the most specific category that applies.
```

---

## Step 2. Add affected areas

Linking geographic areas to the incident lets OpenSPP identify which registrants live in the affected zone.

1. On the incident form, go to the **Affected Areas** tab.
2. Click **Add a line** and select an area from the list.
3. Optionally set a **Severity override** for that area if the local impact differs from the overall incident severity.
4. Add any area-specific **Notes** (e.g., "Coastal barangays only").
5. Repeat for each affected area.
6. Click **Save**.

| Field | What to enter |
|-------|--------------|
| **Area** | Geographic area from your configured area list |
| **Severity override** | Local severity (1–5), or leave blank to inherit incident severity |
| **Affected population estimate** | Estimated number of people in the area |
| **Notes** | Area-specific notes |

---

## Step 3. Activate the incident

Once the incident is confirmed and active, advance it from Alert to Active status.

1. On the incident form, click **Set Active**.
2. The status changes to **Active** and the incident appears in active incident dashboards.

```{tip}
Keep the incident in **Alert** status while you are still gathering information. Move to **Active** once you have confirmed areas and are beginning impact assessments.
```

---

## Step 4. Identify affected registrants

OpenSPP can automatically find registrants whose recorded address falls within the incident's affected areas.

1. On the incident form, click the **Affected Registrants** smart button at the top.
2. The system displays a list of registrants linked to the affected geographic areas.
3. Review the list to confirm which registrants require impact assessment.

```{note}
This list is based on the geographic areas recorded in the registry. Registrants whose area is not recorded, or who live in a border area, may not appear. Field officers should also report impacts manually (see Step 5).
```

---

## Step 5. Record registrant impacts

For each registrant affected by the incident, create an impact record.

### Option A: Record impacts one at a time

1. Open a registrant's record in the **Registry**.
2. Go to the **Hazard Impacts** tab.
3. Click **Add a line** and fill in the impact details:

| Field | What to enter |
|-------|--------------|
| **Incident** | Select the incident this impact relates to |
| **Impact type** | The type of harm (Physical, Economic, Health, Social) |
| **Damage level** | How severe the damage is (see damage levels below) |
| **Impact date** | When the impact was assessed |
| **Notes** | Observations from the field |

4. Click **Save**.

### Option B: Bulk create impacts for an area

For large-scale events, you can create impact records for all registrants in an affected area at once.

1. On the incident form, open the **Affected Areas** tab.
2. Select the area, then click **Bulk Create Impacts**.
3. Choose the impact type and default damage level.
4. Click **Confirm**. OpenSPP creates a Reported impact record for each registrant in that area.

```{tip}
Bulk creation uses **Reported** status, meaning the impacts still need field verification. Use bulk creation as a starting point, then update individual records as field data comes in.
```

### Damage levels

| Level | When to use |
|-------|------------|
| **Minimal** | Minor damage, household function not disrupted |
| **Moderate** | Significant damage, household partially affected |
| **Severe** | Serious damage, household severely disrupted |
| **Critical** | Household unable to function, urgent assistance needed |
| **Partially damaged** | Physical structure or assets partly destroyed |
| **Totally damaged** | Physical structure or assets fully destroyed |

---

## Step 6. Verify impacts

Impact records begin in **Reported** status. A hazard officer or manager must verify or dispute each record based on field evidence.

1. Open an impact record (from the incident's **Impacts** tab or the registrant's **Hazard Impacts** tab).
2. Review the damage level and notes.
3. Click one of the following:
   - **Verify** — Confirms the impact record as accurate. Status changes to **Verified**.
   - **Dispute** — Flags the record as contested. Status changes to **Disputed**.
4. Verified records can later be **Closed** once no further action is needed.

| Verification status | Meaning |
|--------------------|---------|
| **Reported** | Impact recorded but not yet reviewed |
| **Verified** | Confirmed accurate by an officer or manager |
| **Disputed** | Accuracy is contested, further review needed |
| **Closed** | Verified and no further action required |

```{note}
Only **Verified** impacts count toward emergency program eligibility. Disputed records are excluded until re-verified.
```

---

## Step 7. Move to recovery and close

Once the acute phase of the incident has passed, advance the incident through its final stages.

### Start recovery

1. On the incident form, click **Start Recovery**.
2. The status changes to **Recovery**. Ongoing response activities continue but the emergency phase is ending.

### Close the incident

1. On the incident form, click **Close**.
2. If no end date was set, the system records today's date as the end date.
3. The status changes to **Closed**. The incident becomes read-only.

---

## Viewing impacts on a registrant record

To see all hazard impacts for an individual registrant:

1. Go to **Registry > Individuals** (or **Groups**) and open the registrant's record.
2. Click the **Hazard Impacts** smart button at the top, or go to the **Hazard Impacts** tab.
3. The list shows all incidents affecting this registrant, with their damage level and verification status.

---

## Initial setup (managers only)

Before officers can use the hazard module, a manager must configure the following. Skip this section if setup is already complete.

### Hazard categories

1. Go to **Hazard and Emergency > Configuration > Hazard Categories**.
2. Click **New** and enter a category name and code.
3. To create a sub-category, set the **Parent Category** field.
4. Repeat to build out the hierarchy your organization uses.

### Impact types

1. Go to **Hazard and Emergency > Configuration > Impact Types**.
2. Click **New** and fill in:

| Field | What to enter |
|-------|--------------|
| **Name** | Descriptive label (e.g., "Livestock loss") |
| **Code** | Short reference code |
| **Category** | Physical, Economic, Health, or Social |
| **Description** | What this impact type covers |

---

## Are you stuck?

**I cannot find a registrant in the affected list.**
The registrant's area field may not be filled in, or their area may not be linked to the incident. Add the area manually or record the impact directly on the registrant's profile.

**The Bulk Create Impacts button is not visible.**
You may not have Hazard Officer or Manager access. Also check that at least one area is linked to the incident.

**I verified an impact by mistake.**
Contact a Hazard Manager to correct the record. Managers can revert a verified impact to Reported status.

**The incident cannot be closed.**
Check that all open impacts have been progressed beyond Reported status. Leaving impacts unreviewed may prevent closure depending on your organization's configuration.

**I need to link this incident to a program for emergency assistance.**
Open the incident and go to the **Response Programs** tab. A program manager must first configure the program's Emergency Response settings before it will appear here.
