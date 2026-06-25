---
openspp:
  doc_status: draft
  products: [disability_registry]
---

# Disability Registry stories

The OpenSPP Disability Registry demo includes three fixed registrant records that demonstrate different assessment outcomes and workflow states.

## Before you start

- OpenSPP should be installed and running (see {doc}`../../installation/index`)
- OpenSPP Disability Registry demo data should be loaded (see {doc}`install_data`)
- You need at minimum Disability Viewer access, or log in as `admin`

## Assessment instruments

The demo uses the Washington Group Short Set (WG-SS) instrument across all three stories. The system automatically selects the appropriate instrument based on the registrant's age:

| Instrument | Age group | Respondent |
|-----------|-----------|------------|
| WG-SS | Adults 18 and over | Self-report (proxy optional) |
| CFM 5-17 | Children 5–17 | Proxy (parent/caregiver) |
| CFM 2-4 | Children 2–4 | Proxy (mandatory) |

The WG standard defines disability as **any domain reaching "a lot of difficulty" or "cannot do at all"**.

---

## Story 1: Maria Santos — Adult with approved multi-impairment assessment

**Demonstration purpose:** A complete approved assessment with multiple impairments, three domains above threshold, assistive device management, and an improvement-not-expected review schedule. Primary story for end-to-end approved assessment lifecycle.

**Assessment details:**

| Field | Value |
|-------|-------|
| Instrument | WG-SS (adult) |
| Assessment date | 2025-01-10 |
| State | Approved |
| Has disability | Yes |

**WG-SS domain responses:**

| Domain | Response | Above threshold |
|--------|----------|----------------|
| Seeing | A lot of difficulty | Yes |
| Hearing | Some difficulty | No |
| Walking | Cannot do at all | Yes |
| Remembering | No difficulty | No |
| Self-care | A lot of difficulty | Yes |
| Communicating | Some difficulty | No |

Three domains above threshold → `has_disability = True`

**Impairment classification:**

| Impairment type | Cause | Severity |
|----------------|-------|----------|
| Physical Impairment | Injury/Accident | Severe |
| Visual Impairment | Disease/Illness | Moderate |

Overall severity: **Severe** (highest across all classified impairment lines)

**Review schedule:**

| Category | Meaning | Next review |
|----------|---------|-------------|
| Improvement Not Expected (MINE) | No medical improvement expected | ~6 years from assessment date |

**Support needs:** Requires wheelchair and mobility assistance. Uses screen reader for vision support.

**Assistive devices:**

| Device | Status | Provider | Date |
|--------|--------|----------|------|
| Wheelchair | Provided | National Disability Council | 2024-06-15 |
| Magnifier | Requested | — | — |

---

## Story 2: Juan Cruz Jr — Child with pending assessment and unmet device need

**Demonstration purpose:** A child assessment answered by a proxy (parent), sitting in pending approval state with an unmet assistive device need. Demonstrates the proxy response workflow, hearing impairment classification, and the device `needed` status.

**Assessment details:**

| Field | Value |
|-------|-------|
| Instrument | WG-SS |
| Assessment date | 2025-01-12 |
| State | Pending approval |
| Proxy response | Yes — Parent |
| Has disability | Yes |

**Domain responses:**

| Domain | Response | Above threshold |
|--------|----------|----------------|
| Seeing | No difficulty | No |
| Hearing | A lot of difficulty | Yes |
| Walking | No difficulty | No |
| Remembering | Some difficulty | No |
| Self-care | No difficulty | No |
| Communicating | A lot of difficulty | Yes |

Two domains above threshold → `has_disability = True`

**Impairment classification:**

| Impairment type | Cause | Severity |
|----------------|-------|----------|
| Hearing Impairment | Congenital/Genetic | Moderate |

**Review schedule:**

| Category | Meaning | Next review |
|----------|---------|-------------|
| Improvement Possible (MIP) | Some chance of medical improvement | ~3 years from assessment date |

**Assistive devices:**

| Device | Status | Notes |
|--------|--------|-------|
| Hearing Aid | Needed | Child needs bilateral hearing aids for school participation |

The `needed` status sets `has_unmet_device_need = True` on the registrant record, which can be used in program eligibility targeting.

---

## Story 3: Ana Reyes — Adult with draft assessment, no disability

**Demonstration purpose:** An assessment still in draft state that will result in no disability finding. Demonstrates the draft workflow stage and how the system records assessments below the WG threshold.

**Assessment details:**

| Field | Value |
|-------|-------|
| Instrument | WG-SS (adult) |
| Assessment date | 2025-01-14 |
| State | Draft |
| Has disability | No |

**WG-SS domain responses:**

| Domain | Response | Above threshold |
|--------|----------|----------------|
| Seeing | No difficulty | No |
| Hearing | No difficulty | No |
| Walking | Some difficulty | No |
| Remembering | No difficulty | No |
| Self-care | No difficulty | No |
| Communicating | No difficulty | No |

Zero domains above threshold → `has_disability = False`

No impairments recorded. No assistive devices.

> The assessment is in draft state — it has not yet been submitted for approval. Until an assessment is approved, the registrant's `has_disability` field remains `False`. Submitting and approving this assessment confirms the no-disability outcome and creates a permanent audit record.
