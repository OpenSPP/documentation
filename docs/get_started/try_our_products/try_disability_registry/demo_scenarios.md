---
openspp:
  doc_status: draft
  products: [disability_registry]
---

# Disability Registry demo scenarios

You will here find a number of scenarios that demonstrate key functionality in the OpenSPP Disability Registry.

## Before you start

- OpenSPP should be installed and running (see {doc}`../../installation/index`)
- OpenSPP Disability Registry demo data should be loaded (see {doc}`install_data`)
- You need administrator access to OpenSPP

---

## Scenario 1: Browse assessments and understand disability status

Get an overview of the assessment list and how disability status is determined.

1. Open **Disability → Assessments** — the list shows all three demo assessments with their state (Approved, Pending, Draft) and disability indicator.
2. Note the three distinct states: Maria Santos is **Approved**, Juan Cruz Jr is **Pending**, and Ana Reyes is **Draft**.
3. Open Maria Santos's assessment — open the **WG-SS Assessment** tab — see the six domain responses, with three domains reaching "a lot of difficulty" or "cannot do at all."
4. The **Has Disability** indicator at the top of the form is **Yes** because at least one domain meets the WG threshold.
5. Go back and open Ana Reyes's assessment — her highest response is "some difficulty" for walking, which is below the threshold — **Has Disability** is **No**.

**Key messages:**

- Disability status is computed automatically from WG domain responses — no manual entry required
- "Some difficulty" does not meet the WG threshold; only "a lot of difficulty" or "cannot do at all" trigger a positive result
- State controls whether the result is active on the registrant: only Approved assessments set the registrant's live disability status

---

## Scenario 2: Review a complete approved assessment

Walk through Maria Santos's approved assessment record end to end.

1. Open **Disability → Assessments** — open Maria Santos's assessment (state: Approved).
2. Open the **Impairment Classification** tab — two impairment lines are classified: Physical Impairment (Injury, Severe) and Visual Impairment (Disease, Moderate). The **Severity Level** shown on the assessment reflects the highest severity across all lines: **Severe**.
3. Open the **Support Needs** tab — see the free-text support description ("Requires wheelchair and mobility assistance. Uses screen reader for vision support.") and the **Assistive Device Requests** section.
4. Note the **Review Schedule** section — the category is **Improvement Not Expected (MINE)**, which automatically schedules the next review approximately 6 years from the assessment date.
5. Navigate to the registrant: click the registrant's name or the **View Registrant** button — on Maria Santos's registrant form, find the **Disability** section showing `has_disability = True`, her severity level, and the **Assistive Devices** smart button.
6. Click **Assistive Devices** — see the wheelchair (Provided, National Disability Council, 2024-06-15) and the magnifier (Requested).

**Key messages:**

- Impairment classification, support needs, device requests, and review schedule are all managed within the same assessment record
- The severity level on the assessment is derived automatically from the worst-case impairment line, not a manually entered field
- Device status workflow — Needed → Requested → Provided — maps to real-world procurement and distribution stages

---

## Scenario 3: Approve a pending assessment

Walk Juan Cruz Jr's pending assessment through the approval workflow.

```{note}
Before running this scenario, an approval workflow must be configured. Go to **Settings → Disability Registry** and set the **Assessment approval workflow** field to an approval definition. Create one under **Approvals → Approval Definitions** with model **Disability Assessment**. Until one is selected, the Submit button is hidden and assessments cannot be submitted.
```

1. Open **Disability → Assessments** — open Juan Cruz Jr's assessment (state: Pending).
2. Note the **Proxy Response** flag is set and the **Proxy Relationship** is **Parent** — the child's responses were provided by a caregiver.
3. Open the **Impairment Classification** tab — one impairment is classified: Hearing Impairment (Congenital, Moderate).
4. The **Review Schedule** shows **Improvement Possible (MIP)** — a 3-year review cycle.
5. With Disability Validator access (or as `admin`), click **Approve** — the assessment moves to **Approved** state. Juan Cruz Jr's registrant record now shows `has_disability = True`.
6. Navigate to Juan Cruz Jr's registrant record — click **Assistive Devices** — the Hearing Aid shows status **Needed**. This unmet need sets `has_unmet_device_need = True` on the registrant, which can be queried in program eligibility rules.

**Key messages:**

- The approval gate ensures a reviewer confirms the assessment before it becomes the registrant's active disability status
- Proxy response is tracked with the respondent type and their relationship to the child
- Approving an assessment automatically propagates the disability status to the registrant record

---

## Scenario 4: Submit a draft assessment for review

Show how a draft assessment moves through submission to approval.

1. Open **Disability → Assessments** — open Ana Reyes's assessment (state: Draft).
2. The WG-SS tab shows all six responses entered, with "some difficulty" for walking as the highest — below the disability threshold. **Has Disability** is **No**.
3. Once the approval workflow is configured (see Scenario 3 note), click **Submit for Approval** — the assessment moves to **Pending** state.
4. A Disability Validator can then open the assessment and click **Approve** — it becomes **Approved** with a confirmed no-disability outcome on the record.
5. Navigate to Ana Reyes's registrant record — `has_disability` remains **No**, confirming the assessment correctly recorded a no-disability outcome.

**Key messages:**

- Draft assessments do not affect the registrant's active disability status — only Approved assessments count
- The system handles no-disability outcomes explicitly; registrants do not need a positive disability finding to have an assessment record
- Every assessment creates a permanent audit record regardless of the outcome, supporting accountability and historical review

---

## Scenario 5: Assistive device status lifecycle

Demonstrate the three-state device workflow across both registrants.

1. Open **Disability → Assistive Devices** — the list shows all three demo devices: Wheelchair (Provided), Magnifier (Requested), Hearing Aid (Needed).
2. Open the Hearing Aid record for Juan Cruz Jr — status is **Needed**. The notes field reads "Child needs bilateral hearing aids for school participation."
3. Change the status to **Requested** to simulate a procurement request being raised — save the record.
4. Open the Wheelchair record for Maria Santos — status is **Provided**, with provision date 2024-06-15 and provider "National Disability Council."
5. Navigate to Juan Cruz Jr's registrant record — with the Hearing Aid now in **Requested** status, note that `has_unmet_device_need` changes to **False** because no device remains in **Needed** status.

**Key messages:**

- Needed → Requested → Provided maps to the real procurement lifecycle from identification through distribution
- `has_unmet_device_need` on the registrant is True only when at least one device remains in **Needed** status — a single field a program eligibility rule can query directly
- Provision date and provider are recorded on transition to Provided, creating an accountability trail

---

## Scenario 6: Disability CEL functions in program eligibility

Show how disability data flows into program eligibility rules via built-in CEL functions.

1. Open a program's eligibility rule configuration (or open **Studio → Logic Packs** to view the disability function pack).
2. In the expression editor for an individual-registrant rule, type `has_disability` — the function returns `True` when the registrant has an approved assessment with at least one WG domain above the threshold.
3. For severity-based targeting, use `is_severe_disability` — this returns `True` when the registrant's severity level belongs to the **Severe Disability** concept group (Severe or Profound per ICF).
4. For household-level targeting, use `household_has_pwd` on a group/household rule — it returns `True` if any member of the household has a disability.
5. For reassessment-driven rules, use `needs_reassessment` — it returns `True` when the registrant's `next_review_date` is today or in the past, allowing programs to require periodic re-certification for continued enrollment.

Available CEL functions:

| Function | Input | Returns | Use case |
|----------|-------|---------|----------|
| `has_disability` | Individual | Boolean | Target any registrant with approved disability |
| `disability_severity` | Individual | Severity code | Filter by specific severity code |
| `is_severe_disability` | Individual | Boolean | Enhanced benefit eligibility (Severe or Profound) |
| `household_has_pwd` | Group/household | Boolean | Household-level disability targeting |
| `household_pwd_count` | Group/household | Integer | Threshold-based household rules |
| `needs_reassessment` | Individual | Boolean | Flag registrants with overdue review dates |

**Key messages:**

- CEL functions bridge assessment records to program eligibility without any custom code
- Severity-based and household-level targeting are first-class functions, not workarounds
- `needs_reassessment` enables compliance gates: programs can require periodic re-certification to maintain enrollment, closing the loop between assessment scheduling and program participation
