---
openspp:
  doc_status: draft
  products: [disability_registry]
---

# Disability Registry stories

The OpenSPP Disability Registry demo module includes ten fixed registrant stories covering all three assessment instruments, all three workflow states, diverse impairment profiles, and the full assistive device lifecycle. Each story is designed to let you explore a specific feature set without building your own test data.

## Before you start

- OpenSPP should be installed and running (see {doc}`../../installation/index`)
- OpenSPP Disability Registry Demo module should be installed and demo data loaded (see {doc}`install_data`)
- You need at minimum Disability Viewer access, or log in as `admin`

> **Locale note:** The reference data uses a Philippine (`fil_PH`) theme — Filipino names, Philippine locations, currency (₱), and regional area codes. The assessment logic, instrument types, and program structures are country-agnostic. Swap names, locations, and currency to match your deployment context.

## Assessment instruments

The demo covers all three standardized instruments. The system automatically selects the appropriate instrument based on the registrant's age at the time of assessment:

| Instrument | Age group | Proxy |
|-----------|-----------|-------|
| WG-SS | 18 and above | Optional |
| CFM 5–17 | 5–17 years | Mandatory (or self-report if configured) |
| CFM 2–4 | 2–4 years | Mandatory |

The WG standard threshold is **"a lot of difficulty" or "cannot do at all"** in any domain. CFM 5–17 uses the same scale, with the exception of anxiety and depression which use a frequency scale where **"daily"** is the threshold.

## Demo users

| Login | Password | Role | Used in scenarios |
|-------|----------|------|-------------------|
| `admin` | `admin` | System Administrator | Any — full access |
| `assessor` | `demo` | Disability Assessor | Draft creation, submit for review |
| `validator` | `demo` | Disability Validator | Pending → approve |
| `viewer` | `demo` | Disability Viewer | Read-only walkthroughs |

---

## Story 1: Maria Santos — Adult with approved multi-impairment assessment

**Demonstration purpose:** Complete approved WG-SS assessment with two classified impairment types, three domains above threshold, assistive device management, and an improvement-not-expected review schedule. Primary story for the end-to-end approved assessment lifecycle.

**Quick facts:**

| Field | Value |
|-------|-------|
| Registrant | Maria Santos |
| Date of birth | 1985-03-15 |
| Age at assessment | 39 |
| Sex | Female |
| Location | Quezon City, NCR |
| Instrument | WG-SS (adult) |
| Assessment date | 2025-01-10 |
| State | Approved |
| Has disability | Yes |
| Review category | MINE — Improvement Not Expected |
| Next review | 2031-01-10 (72 months) |

**WG-SS domain responses:**

| Domain | Response | Code | Above threshold |
|--------|----------|------|----------------|
| Seeing | A lot of difficulty | `a_lot` | Yes |
| Hearing | Some difficulty | `some` | No |
| Walking | Cannot do at all | `cannot` | Yes |
| Remembering | No difficulty | `none` | No |
| Self-care | A lot of difficulty | `a_lot` | Yes |
| Communicating | Some difficulty | `some` | No |

Three domains above threshold → `has_disability = True`

**Impairment classification:**

| Impairment type | Cause | Severity |
|----------------|-------|----------|
| Physical / Mobility Impairment | Injury/Accident | Severe |
| Sensory / Visual Impairment | Disease/Illness | Moderate |

Overall severity: **Severe** (highest across all classified impairment lines)

**Support needs:** Requires wheelchair for all mobility outside the home. Uses a screen reader and magnifier for vision tasks. Caregiver assists with daily self-care.

**Assistive devices:**

| Device | Status | Provider | Date |
|--------|--------|----------|------|
| Wheelchair | Provided | National Disability Council | 2024-06-15 |
| Magnifier | Needed | — | — |

`has_unmet_device_need = True` — Magnifier status is `needed`

**Programs enrolled:**

| Program | CEL eligibility |
|---------|----------------|
| PWD Cash Assistance Program | `has_disability(registrant) == True` |
| Severe Disability Supplement | `is_severe_disability(registrant) == True` |
| Assistive Device Support Grant | `has_disability(registrant) and registrant.has_unmet_device_need` |

---

## Story 2: Juan Cruz Jr — Child with CFM 5–17 assessment, pending approval

**Demonstration purpose:** School-age child assessed using the Child Functioning Module (CFM 5–17). Proxy response by parent. Hearing and communication domains above threshold. Assessment submitted and waiting for validator approval. Primary story for the CFM 5–17 instrument and the pending approval state.

**Quick facts:**

| Field | Value |
|-------|-------|
| Registrant | Juan Cruz Jr |
| Date of birth | 2015-08-22 |
| Age at assessment | 9 |
| Sex | Male |
| Location | Cebu City, Cebu |
| Instrument | CFM 5–17 |
| Assessment date | 2025-01-12 |
| State | Pending approval |
| Proxy response | Yes — Mother (parent) |
| Has disability | Yes |
| Review category | MIP — Improvement Possible |
| Next review | 2028-01-12 (36 months) |

**CFM 5–17 domain responses:**

| Domain | Response | Code | Above threshold |
|--------|----------|------|----------------|
| Vision unaided | No difficulty | `none` | No |
| Hearing unaided | A lot of difficulty | `a_lot` | Yes |
| Walking 100 yds unaided | No difficulty | `none` | No |
| Walking 500 yds unaided | No difficulty | `none` | No |
| Self-care | No difficulty | `none` | No |
| Communicating inside household | A lot of difficulty | `a_lot` | Yes |
| Communicating outside household | A lot of difficulty | `a_lot` | Yes |
| Learning | Some difficulty | `some` | No |
| Remembering | No difficulty | `none` | No |
| Concentrating | No difficulty | `none` | No |
| Accepting change | Some difficulty | `some` | No |
| Behaviour | Some difficulty | `some` | No |
| Making friends | No difficulty | `none` | No |
| Anxiety | Never | `never` | No |
| Depression | Never | `never` | No |

Three CFM domains above threshold → `has_disability = True`

**Impairment classification:**

| Impairment type | Cause | Severity |
|----------------|-------|----------|
| Sensory / Hearing Impairment | Congenital/Genetic | Moderate |

**Assistive devices:**

| Device | Status | Notes |
|--------|--------|-------|
| Hearing Aid | Needed | Bilateral hearing aids recommended for school participation |

`has_unmet_device_need = True`

**Programs enrolled:**

| Program | CEL eligibility |
|---------|----------------|
| PWD Cash Assistance Program | `has_disability(registrant) == True` |
| Child Disability Benefit | `has_disability(registrant) and registrant.age < 18` |
| Assistive Device Support Grant | `has_disability(registrant) and registrant.has_unmet_device_need` |

---

## Story 3: Ana Reyes — Adult with draft assessment, below disability threshold

**Demonstration purpose:** Assessment in draft state. All WG-SS domains below threshold — the result will be a no-disability finding once submitted and approved. Shows the draft workflow stage and why recording below-threshold assessments matters for audit and re-evaluation.

**Quick facts:**

| Field | Value |
|-------|-------|
| Registrant | Ana Reyes |
| Date of birth | 1990-11-05 |
| Age at assessment | 34 |
| Sex | Female |
| Location | Davao City, Davao del Sur |
| Instrument | WG-SS (adult) |
| Assessment date | 2025-01-14 |
| State | Draft |
| Has disability | No |

**WG-SS domain responses:**

| Domain | Response | Code | Above threshold |
|--------|----------|------|----------------|
| Seeing | No difficulty | `none` | No |
| Hearing | No difficulty | `none` | No |
| Walking | Some difficulty | `some` | No |
| Remembering | No difficulty | `none` | No |
| Self-care | No difficulty | `none` | No |
| Communicating | No difficulty | `none` | No |

Zero domains above threshold → `has_disability = False`

No impairments recorded (`has_impairments_to_record = no`). No assistive devices. No program enrollments.

> The assessment has not been submitted. Until an approved assessment exists, `has_disability` stays `False` on the registrant record. Submitting and approving this assessment creates a permanent audit record confirming the no-disability outcome.

---

## Story 4: Roberto Dela Cruz — Adult with cognitive impairment, improvement expected

**Demonstration purpose:** Adult with a cognitive impairment following a neurological episode. Two domains above threshold. Review category set to MIE (Improvement Expected) — the 12-month schedule. This story is due for reassessment at the time of the demo, making `needs_reassessment(registrant)` return `True`.

**Quick facts:**

| Field | Value |
|-------|-------|
| Registrant | Roberto Dela Cruz |
| Date of birth | 1969-07-10 |
| Age at assessment | 55 |
| Sex | Male |
| Location | Batangas City, Batangas |
| Instrument | WG-SS (adult) |
| Assessment date | 2025-02-03 |
| State | Approved |
| Has disability | Yes |
| Review category | MIE — Improvement Expected |
| Next review | 2026-02-03 (12 months) |

**WG-SS domain responses:**

| Domain | Response | Code | Above threshold |
|--------|----------|------|----------------|
| Seeing | No difficulty | `none` | No |
| Hearing | Some difficulty | `some` | No |
| Walking | Some difficulty | `some` | No |
| Remembering | A lot of difficulty | `a_lot` | Yes |
| Self-care | No difficulty | `none` | No |
| Communicating | A lot of difficulty | `a_lot` | Yes |

Two domains above threshold → `has_disability = True`

**Impairment classification:**

| Impairment type | Cause | Severity |
|----------------|-------|----------|
| Cognitive / Intellectual Disability | Disease/Illness | Moderate |

Overall severity: **Moderate**

**Support needs:** Attends weekly cognitive rehabilitation sessions. Family caregiver assists with planning and communication tasks.

**Assistive devices:**

| Device | Status | Notes |
|--------|--------|-------|
| Cognitive Aid | Needed | Communication support tool recommended by occupational therapist |

`has_unmet_device_need = True`

**Programs enrolled:**

| Program | CEL eligibility |
|---------|----------------|
| PWD Cash Assistance Program | `has_disability(registrant) == True` |
| Assistive Device Support Grant | `has_disability(registrant) and registrant.has_unmet_device_need` |
| Annual Reassessment Service | `needs_reassessment(registrant) == True` — review due 2026-02-03 |

---

## Story 5: Liza Villanueva — Toddler with CFM 2–4, mandatory proxy response

**Demonstration purpose:** A 2-year-old child assessed using the CFM 2–4 instrument. Proxy response is mandatory for this age group. One vision domain above threshold. Primary story for the CFM 2–4 instrument and mandatory proxy workflow.

**Quick facts:**

| Field | Value |
|-------|-------|
| Registrant | Liza Villanueva |
| Date of birth | 2022-04-18 |
| Age at assessment | 2 |
| Sex | Female |
| Location | Cagayan de Oro City, Misamis Oriental |
| Instrument | CFM 2–4 |
| Assessment date | 2025-03-20 |
| State | Pending approval |
| Proxy response | Yes — Mother (parent) — mandatory |
| Has disability | Yes |
| Review category | MIP — Improvement Possible |
| Next review | 2028-03-20 (36 months) |

**CFM 2–4 domain responses:**

| Domain | Field | Response | Code | Above threshold |
|--------|-------|----------|------|----------------|
| Glasses gate | `cfm24_glasses` | No | — | — |
| Vision unaided | `cfm24_vision` | A lot of difficulty | `a_lot` | Yes |
| Hearing aid gate | `cfm24_hearing_aid` | No | — | — |
| Hearing unaided | `cfm24_hearing` | No difficulty | `none` | No |
| Walk equipment gate | `cfm24_walk_equipment` | No | — | — |
| Walk unaided | `cfm24_walk_unaided` | Some difficulty | `some` | No |
| Dexterity | `cfm24_dexterity` | No difficulty | `none` | No |
| Understanding child | `cfm24_understood` | Some difficulty | `some` | No |
| Understanding you | `cfm24_understand_you` | No difficulty | `none` | No |
| Learning | `cfm24_learning` | No difficulty | `none` | No |
| Playing | `cfm24_playing` | No difficulty | `none` | No |
| Behaviour | `cfm24_behavior` | Same as peers | `same_or_less` | No |

One domain above threshold → `has_disability = True`

**Impairment classification:**

| Impairment type | Cause | Severity |
|----------------|-------|----------|
| Sensory / Visual Impairment | Congenital/Genetic | Moderate |

**Assistive devices:**

| Device | Status | Provider | Date |
|--------|--------|----------|------|
| Corrective Glasses | Provided | Local Eye Clinic | 2025-04-10 |

`has_unmet_device_need = False` — glasses have been provided

**Programs enrolled:**

| Program | CEL eligibility |
|---------|----------------|
| PWD Cash Assistance Program | `has_disability(registrant) == True` |
| Child Disability Benefit | `has_disability(registrant) and registrant.age < 18` |

---

## Story 6: Danilo Mangudadatu — Adult with conflict-related multi-impairment

**Demonstration purpose:** Adult with permanent physical and communication disabilities caused by a conflict-related injury. Two domains above threshold. Both impairments share the same cause (Conflict/Violence) — useful for demonstrating multi-cause classification and cause-based reporting. MINE review with 72-month schedule.

**Quick facts:**

| Field | Value |
|-------|-------|
| Registrant | Danilo Mangudadatu |
| Date of birth | 1982-05-25 |
| Age at assessment | 42 |
| Sex | Male |
| Location | Cotabato City, Maguindanao del Norte |
| Instrument | WG-SS (adult) |
| Assessment date | 2025-02-15 |
| State | Approved |
| Has disability | Yes |
| Review category | MINE — Improvement Not Expected |
| Next review | 2031-02-15 (72 months) |

**WG-SS domain responses:**

| Domain | Response | Code | Above threshold |
|--------|----------|------|----------------|
| Seeing | No difficulty | `none` | No |
| Hearing | No difficulty | `none` | No |
| Walking | Cannot do at all | `cannot` | Yes |
| Remembering | A lot of difficulty | `a_lot` | Yes |
| Self-care | Some difficulty | `some` | No |
| Communicating | No difficulty | `none` | No |

Two domains above threshold → `has_disability = True`

**Impairment classification:**

| Impairment type | Cause | Severity |
|----------------|-------|----------|
| Physical / Mobility Impairment | Conflict/Violence | Severe |
| Communication / Speech Impairment | Conflict/Violence | Moderate |

Overall severity: **Severe**

**Support needs:** Uses a walker for all outdoor movement. Augmentative communication device prescribed for speech support in community settings.

**Assistive devices:**

| Device | Status | Provider | Date |
|--------|--------|----------|------|
| Walker/Rollator | Provided | DSWD Regional Office | 2024-09-20 |
| AAC Device | Requested | — | — |

`has_unmet_device_need = False` — both devices are past "needed" status (one provided, one requested)

**Programs enrolled:**

| Program | CEL eligibility |
|---------|----------------|
| PWD Cash Assistance Program | `has_disability(registrant) == True` |
| Severe Disability Supplement | `is_severe_disability(registrant) == True` |

---

## Story 7: Elena Garcia — Elderly adult with age-related multi-impairment

**Demonstration purpose:** Elderly registrant with three age-related impairments across sensory and physical domains. Three domains above threshold. Three impairments at different severity levels — demonstrates how overall severity is set to the highest severity across all impairment lines.

**Quick facts:**

| Field | Value |
|-------|-------|
| Registrant | Elena Garcia |
| Date of birth | 1952-02-14 |
| Age at assessment | 72 |
| Sex | Female |
| Location | Iloilo City, Iloilo |
| Instrument | WG-SS (adult) |
| Assessment date | 2025-01-20 |
| State | Approved |
| Has disability | Yes |
| Review category | MINE — Improvement Not Expected |
| Next review | 2031-01-20 (72 months) |

**WG-SS domain responses:**

| Domain | Response | Code | Above threshold |
|--------|----------|------|----------------|
| Seeing | A lot of difficulty | `a_lot` | Yes |
| Hearing | A lot of difficulty | `a_lot` | Yes |
| Walking | A lot of difficulty | `a_lot` | Yes |
| Remembering | Some difficulty | `some` | No |
| Self-care | No difficulty | `none` | No |
| Communicating | No difficulty | `none` | No |

Three domains above threshold → `has_disability = True`

**Impairment classification:**

| Impairment type | Cause | Severity |
|----------------|-------|----------|
| Sensory / Visual Impairment | Age-related | Mild |
| Sensory / Hearing Impairment | Age-related | Moderate |
| Physical / Mobility Impairment | Age-related | Moderate |

Overall severity: **Moderate** (highest across all three impairment lines)

**Support needs:** Uses walking cane and corrective glasses daily. Lives with family and is independent with daily self-care.

**Assistive devices:**

| Device | Status | Provider | Date |
|--------|--------|----------|------|
| Walking Cane | Provided | Family purchase | 2023-06-01 |
| Corrective Glasses | Provided | LGU Eyeglass Program | 2024-03-15 |
| Hearing Aid | Needed | — | — |

`has_unmet_device_need = True` — Hearing Aid status is `needed`

**Programs enrolled:**

| Program | CEL eligibility |
|---------|----------------|
| PWD Cash Assistance Program | `has_disability(registrant) == True` |
| Assistive Device Support Grant | `has_disability(registrant) and registrant.has_unmet_device_need` |

---

## Story 8: Grace Bautista — Adolescent with CFM 5–17 psychosocial domains

**Demonstration purpose:** School-age adolescent with psychosocial disability. Four CFM 5–17 domains above threshold, including the frequency-scale anxiety domain (daily). Shows how the anxiety/depression frequency scale differs from the standard difficulty scale and how psychosocial findings appear in CFM assessments.

**Quick facts:**

| Field | Value |
|-------|-------|
| Registrant | Grace Bautista |
| Date of birth | 2010-09-30 |
| Age at assessment | 14 |
| Sex | Female |
| Location | Angeles City, Pampanga |
| Instrument | CFM 5–17 |
| Assessment date | 2025-04-05 |
| State | Approved |
| Proxy response | No — self-report (configured for ages 14 and above) |
| Has disability | Yes |
| Review category | MIP — Improvement Possible |
| Next review | 2028-04-05 (36 months) |

**CFM 5–17 domain responses:**

| Domain | Response | Code | Scale | Above threshold |
|--------|----------|------|-------|----------------|
| Vision unaided | No difficulty | `none` | Standard | No |
| Hearing unaided | No difficulty | `none` | Standard | No |
| Walking 100 yds unaided | No difficulty | `none` | Standard | No |
| Walking 500 yds unaided | No difficulty | `none` | Standard | No |
| Self-care | No difficulty | `none` | Standard | No |
| Communicating inside | Some difficulty | `some` | Standard | No |
| Communicating outside | Some difficulty | `some` | Standard | No |
| Learning | A lot of difficulty | `a_lot` | Standard | Yes |
| Remembering | Some difficulty | `some` | Standard | No |
| Concentrating | A lot of difficulty | `a_lot` | Standard | Yes |
| Accepting change | A lot of difficulty | `a_lot` | Standard | Yes |
| Behaviour | Some difficulty | `some` | Standard | No |
| Making friends | Some difficulty | `some` | Standard | No |
| Anxiety | Daily | `daily` | Frequency | Yes |
| Depression | Weekly | `weekly` | Frequency | No |

Four domains above threshold → `has_disability = True`

**Impairment classification:**

| Impairment type | Cause | Severity |
|----------------|-------|----------|
| Psychosocial Disability | Birth Complications | Moderate |

**Assistive devices:** None

**Programs enrolled:**

| Program | CEL eligibility |
|---------|----------------|
| PWD Cash Assistance Program | `has_disability(registrant) == True` |
| Child Disability Benefit | `has_disability(registrant) and registrant.age < 18` |

---

## Story 9: Michael Torres — Young adult with pending WG-SS assessment

**Demonstration purpose:** Young adult with an upper limb injury. Assessment submitted and awaiting validator approval. Two WG-SS domains above threshold. MIE review category for the 12-month rehabilitation window. Primary story for "pending" state in the adult WG-SS pathway. This story pairs with Story 4 to show both MIE registrants due for reassessment.

**Quick facts:**

| Field | Value |
|-------|-------|
| Registrant | Michael Torres |
| Date of birth | 2005-11-08 |
| Age at assessment | 19 |
| Sex | Male |
| Location | Pasig City, Metro Manila |
| Instrument | WG-SS (adult) |
| Assessment date | 2025-03-10 |
| State | Pending approval |
| Has disability | Yes (pending confirmation) |
| Review category | MIE — Improvement Expected |
| Next review | 2026-03-10 (12 months) |

**WG-SS domain responses:**

| Domain | Response | Code | Above threshold |
|--------|----------|------|----------------|
| Seeing | No difficulty | `none` | No |
| Hearing | No difficulty | `none` | No |
| Walking | No difficulty | `none` | No |
| Remembering | No difficulty | `none` | No |
| Self-care | A lot of difficulty | `a_lot` | Yes |
| Communicating | A lot of difficulty | `a_lot` | Yes |

Two domains above threshold → `has_disability = True` (confirmed on approval)

**Impairment classification:**

| Impairment type | Cause | Severity |
|----------------|-------|----------|
| Physical / Upper Limb Impairment | Injury/Accident | Severe |

Overall severity: **Severe**

**Support needs:** Undergoing occupational therapy for dominant hand rehabilitation. Orthotic device prescribed for wrist and hand support.

**Assistive devices:**

| Device | Status | Notes |
|--------|--------|-------|
| Orthotic Device | Needed | Hand orthosis prescribed during OT sessions |

`has_unmet_device_need = True`

**Programs enrolled (evaluated on approval):**

| Program | CEL eligibility |
|---------|----------------|
| PWD Cash Assistance Program | `has_disability(registrant) == True` |
| Assistive Device Support Grant | `has_disability(registrant) and registrant.has_unmet_device_need` |
| Annual Reassessment Service | `needs_reassessment(registrant) == True` — review due 2026-03-10 |

---

## Story 10: Sofia Pangandaman — Adult with single-domain psychosocial disability

**Demonstration purpose:** Adult with exactly one WG-SS domain at threshold — the minimum for a positive disability finding. Shows that a single `a_lot` response is sufficient to set `has_disability = True`. Single moderate psychosocial impairment with unknown cause. MIP review category.

**Quick facts:**

| Field | Value |
|-------|-------|
| Registrant | Sofia Pangandaman |
| Date of birth | 1997-12-03 |
| Age at assessment | 27 |
| Sex | Female |
| Location | Marawi City, Lanao del Sur |
| Instrument | WG-SS (adult) |
| Assessment date | 2025-02-28 |
| State | Approved |
| Has disability | Yes |
| Review category | MIP — Improvement Possible |
| Next review | 2028-02-28 (36 months) |

**WG-SS domain responses:**

| Domain | Response | Code | Above threshold |
|--------|----------|------|----------------|
| Seeing | No difficulty | `none` | No |
| Hearing | No difficulty | `none` | No |
| Walking | No difficulty | `none` | No |
| Remembering | A lot of difficulty | `a_lot` | Yes |
| Self-care | No difficulty | `none` | No |
| Communicating | No difficulty | `none` | No |

One domain above threshold → `has_disability = True`

**Impairment classification:**

| Impairment type | Cause | Severity |
|----------------|-------|----------|
| Psychosocial Disability | Unknown/Undetermined | Moderate |

**Assistive devices:** None

**Programs enrolled:**

| Program | CEL eligibility |
|---------|----------------|
| PWD Cash Assistance Program | `has_disability(registrant) == True` |

---

## Volume registrants

In addition to the ten story registrants, the demo generator creates approximately 200 volume registrants from deterministic blueprints. These populate list views, search filters, and aggregate reports with realistic data. Volume records cover:

- Adults (WG-SS) with single-domain and multi-domain findings, distributed across all regions represented in the story data
- School-age children (CFM 5–17) and toddlers (CFM 2–4) with varied functioning profiles
- Elderly registrants (65+) with age-related impairments
- Mixed approval states: approximately 60 % approved, 25 % pending, 15 % draft
- Device records at all three statuses (needed, requested, provided)

Volume registrants do not have individual narratives. Use them to test list filtering, reporting, and bulk-action workflows.
