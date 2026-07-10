---
openspp:
  doc_status: draft
  products: [disability_registry]
---

# Demo scenarios

These scenarios walk you through the key workflows in the OpenSPP Disability Registry using the pre-loaded demo data. Each scenario is self-contained — you can run them in any order.

## Before you start

- Demo data has been loaded (see {doc}`install_data`)
- Log in as `admin` unless the scenario specifies a different user

---

## Scenario 1: Browse and filter assessments

**What you'll learn:** How to use the assessment list view to locate registrants by state, instrument, review category, or disability outcome.

1. Navigate to **Disability Registry** > **Assessments**.

2. The list shows all ten story assessments plus volume records. Note the **State** column — Approved, Pending, and Draft records are all present.

3. Use **Filters** > **State = Approved** — six story records remain (Maria Santos, Roberto Dela Cruz, Danilo Mangudadatu, Elena Garcia, Grace Bautista, Sofia Pangandaman).

4. Change the filter to **State = Pending** — three records appear (Juan Cruz Jr, Liza Villanueva, Michael Torres).

5. Remove all filters and use **Group By** > **Instrument**:
   - **WG-SS** — the largest group, covering all adults
   - **CFM 5–17** — Juan Cruz Jr and Grace Bautista
   - **CFM 2–4** — Liza Villanueva only (the only toddler story)

6. Use the **Search** bar to type "Santos" — both Maria Santos and Elena Garcia's assessments are returned. Use "Mangudadatu" for an exact match.

**Key messages:**

- Disability status is computed automatically from domain responses — no manual entry required
- "Some difficulty" does not meet the WG threshold; only "a lot of difficulty" or "cannot do at all" trigger a positive result
- Only Approved assessments set the registrant's live disability status

---

## Scenario 2: Review a complete approved assessment

**What you'll learn:** How WG-SS domain responses, impairment lines, severity rollup, and assistive device records appear on a completed approved assessment.

**Registrant:** Maria Santos (Story 1)

1. Open Maria Santos's assessment from the list (state: Approved).

2. On the **Assessment** tab, review the WG-SS responses:
   - Three domains at threshold: seeing (`a_lot`), walking (`cannot`), self-care (`a_lot`)
   - **Has Disability** shows **Yes**

3. Switch to the **Impairments** tab:
   - Two impairment lines: Physical/Mobility Impairment (Injury/Accident, Severe) and Visual Impairment (Disease/Illness, Moderate)
   - **Overall Severity** shows **Severe** — automatically set to the highest severity across all lines

4. Switch to the **Support Needs** tab:
   - Free-text support description and the **Assistive Devices** section listing Wheelchair (Provided) and Magnifier (Needed)

5. Switch to the **Review** tab:
   - Category: **MINE — Improvement Not Expected**
   - Next review: **2031-01-10** (72 months from assessment date)

6. Navigate to Maria Santos's registrant record (click her name in the breadcrumb):
   - **Has Disability = True**, **Disability Severity = Severe**
   - **Has Unmet Device Need = True** (Magnifier is `needed`)
   - The **Assessments** and **Assistive Devices** smart buttons show counts

**Key messages:**

- Impairment classification, support needs, device requests, and review schedule are all managed within the same assessment record
- Overall severity derives automatically from the worst-case impairment line
- Device status (Needed → Requested → Provided) maps to real procurement and distribution stages

---

## Scenario 3: Approve a pending adult WG-SS assessment

**What you'll learn:** The approval workflow for a pending assessment and how approval updates the registrant record.

**Registrant:** Michael Torres (Story 9) **Log in as:** `validator` / `demo`

```{note}
An approval workflow must be configured in Settings before the Approve button appears. Go to **Settings → Disability Registry** and set the **Assessment approval workflow** field. Create an approval definition under **Approvals → Approval Definitions** with model **Disability Assessment** if one does not already exist.
```

1. Navigate to **Disability Registry** > **Assessments**, filter by **State = Pending**, and open **Michael Torres**'s assessment.

2. Review the WG-SS responses — self-care (`a_lot`) and communicating (`a_lot`) are both above threshold.

3. Review the impairment line: Physical / Upper Limb Impairment, Injury/Accident, Severe.

4. Click **Approve** — the state changes to **Approved**.

5. Navigate to Michael Torres's registrant record:
   - **Has Disability = True**
   - **Disability Severity = Severe**
   - **Next Review Date = 2026-03-10** (MIE, 12 months)
   - **Has Unmet Device Need = True** (Orthotic Device is `needed`)

6. Log back in as `admin` and open the **PWD Cash Assistance Program** — Michael Torres should now appear as an eligible enrollee.

**Key messages:**

- The approval gate ensures a validator confirms the assessment before it becomes the registrant's active disability status
- Approving an assessment automatically propagates disability status, severity, and review dates to the registrant record

---

## Scenario 4: Explore CFM child assessments across age groups

**What you'll learn:** How the three assessment instruments differ in structure, and how proxy response is handled for children.

### CFM 5–17: Grace Bautista (Story 8)

1. Open Grace Bautista's assessment (state: Approved, instrument: CFM 5–17).

2. Note:
   - Instrument was auto-selected: Grace was 14 at assessment date
   - **Proxy Response = No** — Grace responded herself (self-report configured for ages 14+)

3. Scroll through the CFM 5–17 responses:
   - All physical domains (vision, hearing, walking, self-care): `none`
   - Learning: `a_lot` — above threshold
   - Concentrating: `a_lot` — above threshold
   - Accepting change: `a_lot` — above threshold
   - Anxiety: `daily` — above threshold (frequency scale; threshold is `daily`, not `a_lot`)
   - Depression: `weekly` — **below** threshold (weekly does not meet the daily cutoff)

4. Four domains above threshold → `has_disability = True`, despite no physical domains flagged.

### CFM 5–17: Juan Cruz Jr (Story 2)

1. Open Juan Cruz Jr's assessment (state: Pending, instrument: CFM 5–17).

2. Note **Proxy Response = Yes — Mother (parent)** — mandatory because the assessor's configuration does not allow self-report for age 9.

3. Hearing (`a_lot`) and both communication domains (`a_lot`) are above threshold.

### CFM 2–4: Liza Villanueva (Story 5)

1. Open Liza Villanueva's assessment (state: Pending, instrument: CFM 2–4).

2. Note:
   - Instrument: **CFM 2–4** — Liza was 2 at assessment date
   - **Proxy Response = Yes — mandatory** for this instrument regardless of configuration

3. Review the CFM 2–4 fields — the vision gate (`cfm24_glasses = No`) routes responses to the unaided vision path (`cfm24_vision = a_lot`), which is the only domain above threshold.

**Key messages:**

- Instrument selection is automatic based on age at assessment date — no manual choice required
- CFM 2–4 always requires proxy response; CFM 5–17 proxy is configurable by age
- The anxiety and depression domains in CFM 5–17 use a frequency scale (`daily`/`weekly`/`monthly`) rather than the standard difficulty scale

---

## Scenario 5: Track the assistive device lifecycle

**What you'll learn:** How to move a device from `needed` → `requested` → `provided` and how the `has_unmet_device_need` flag responds to each transition.

**Registrant:** Juan Cruz Jr (Story 2)

1. Navigate to **Disability Registry** > **Assistive Devices**.

2. Find the **Hearing Aid** record linked to Juan Cruz Jr — status is **Needed**.

3. Open the record. Check Juan Cruz Jr's registrant form — `has_unmet_device_need = True`.

4. Change status to **Requested** (a procurement request has been raised) and save.

5. Return to Juan Cruz Jr's registrant record — `has_unmet_device_need` is now **False** because no device remains at `needed` status.

6. Return to the device record and change status to **Provided**. Fill in:
   - **Provider:** Department of Social Welfare and Development
   - **Provision Date:** today's date

7. Save — the device lifecycle is complete.

**For a mixed-status example:** Open Elena Garcia (Story 7) — she has a Walking Cane (Provided), Corrective Glasses (Provided), and a Hearing Aid (Needed). Her `has_unmet_device_need` remains **True** as long as the Hearing Aid stays at `needed`.

**Key messages:**

- `has_unmet_device_need` on the registrant is `True` only when at least one device has `needed` status — a single Boolean that program eligibility rules can query directly
- Provision date and provider are captured on transition to `provided`, creating an accountability trail
- A registrant with multiple devices can have mixed statuses; the flag reflects the worst-case device

---

## Scenario 6: Disability CEL functions in program eligibility

**What you'll learn:** How the built-in disability CEL functions connect assessment records to program eligibility rules.

1. Navigate to **Programs** and open the **PWD Cash Assistance Program**.

2. Review the eligibility rule — it uses `has_disability(registrant) == True`. All registrants with an approved disability assessment qualify (Stories 1, 4, 6, 7, 8, 10 immediately; Stories 2, 9 on approval).

3. Open the **Severe Disability Supplement**:
   - Eligibility: `is_severe_disability(registrant) == True`
   - Only Maria Santos and Danilo Mangudadatu qualify — both have a Severe overall severity rating

4. Open the **Assistive Device Support Grant**:
   - Eligibility: `has_disability(registrant) and registrant.has_unmet_device_need`
   - Qualifies: Maria Santos, Juan Cruz Jr, Roberto Dela Cruz, Elena Garcia, Michael Torres

5. Open the **Child Disability Benefit**:
   - Eligibility: `has_disability(registrant) and registrant.age < 18`
   - Qualifies: Juan Cruz Jr, Liza Villanueva, Grace Bautista

6. Open the **Annual Reassessment Service**:
   - Eligibility: `needs_reassessment(registrant) == True`
   - Qualifies: Roberto Dela Cruz (next review 2026-02-03) and Michael Torres (next review 2026-03-10) — both dates are already past at demo time

Available CEL functions:

| Function | Input | Returns | Use case |
|----------|-------|---------|----------|
| `has_disability` | Individual | Boolean | Target any registrant with approved disability |
| `disability_severity` | Individual | Severity code | Filter or compare by specific severity code |
| `is_severe_disability` | Individual | Boolean | Enhanced benefit eligibility (Severe or Profound) |
| `household_has_pwd` | Group/household | Boolean | Household-level disability targeting |
| `household_pwd_count` | Group/household | Integer | Threshold-based household rules (e.g., 2+ members) |
| `needs_reassessment` | Individual | Boolean | Flag registrants with overdue review dates |

**Key messages:**

- CEL functions bridge assessment records to program eligibility without custom code
- `needs_reassessment` enables compliance gates — programs can require periodic re-certification for continued enrollment
- Household-level functions (`household_has_pwd`, `household_pwd_count`) target entire households based on any member's disability status

---

## Scenario 7: Search and filter volume registrants

**What you'll learn:** How the ~200 volume registrants support realistic search, filtering, and aggregate reporting.

1. Navigate to **Registry** > **Individuals**.

2. Use **Filters** > **Has Disability = Yes** to narrow to all registrants with an approved positive assessment.

3. Use **Group By** > **Disability Severity** — you will see groups for Mild, Moderate, Severe, and Profound.

4. Remove the severity grouping. Add filter **Disability Review Category = MINE** to find registrants who will not need a scheduled reassessment.

5. Add a second filter: **Has Unmet Device Need = Yes** — this combination identifies MINE registrants who still need a device, a common gap-analysis report in device distribution programs.

6. Use the **Search** bar with **Assessment Instrument = CFM 2-4** to find all toddler assessments in the population.

7. If GIS is configured, switch to **Map View** — volume registrants are distributed across the regions represented in the story data.

**Key messages:**

- Volume records make list filtering, aggregate counts, and map views meaningful rather than showing only ten rows
- Combined filters (e.g., MINE + unmet device need) produce the kind of gap-analysis reports programs use to prioritize outreach
