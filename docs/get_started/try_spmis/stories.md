---
openspp:
  doc_status: draft
  products: [registry, programs]
---

# SP-MIS Stories

The OpenSPP SP-MIS demo module includes a number of fixed households that show various household situations. This will allow you to easily understand the available functionalities.

## Before you start

- OpenSPP should be installed and running (see {doc}`../installation/index`)
- OpenSPP SPMIS Demo should be installed and demo data should be generated (see {doc}`install_data`)
- You need administrator access to OpenSPP


## Story 1: Payment failure, recovery, and compliance pass

**Demonstration purpose:** Cash Transfer with a payment failure and successful
reprocessing. Also demonstrates compliance passing — household Dela Cruz (PH) / Mensah (TG) / Bandara (LK) remains compliant each cycle,
contrasting with household Santos (PH) / Koffi (TG) / Perera (LK) who fails compliance and graduates.

**Program(s) that the household is enrolled in:**

| Program       | Reason for eligibility                         | Compliance                                                | Status   |
| ------------- | ---------------------------------------------- | --------------------------------------------------------- | -------- |
| Cash Transfer | income 4,000 < poverty_line 5,000, size 4 >= 2 | **Passed** — per_capita_income 1,000 < poverty_line 5,000 | Enrolled |

**Household journey:**

1. Enrolled 100 days ago
2. Payment #1 ($150) — paid
3. Payment #2 ($150) — **failed** (bank issue)
4. Payment #3 ($150) — paid (reprocessed)
5. Compliance check passes each cycle (per_capita_income 1,000 < poverty_line 5,000)

**Existing change requests for the household:**

- `update_id` (approved) — Correct national ID number for Juan (PH) / Kofi (TG) / Nimal (LK) after data entry error

**Geographical location:** Calamba City (PH) / Tokoin (TG) / Moratuwa (LK)

---

## Story 2: Graduation and partial exit

**Demonstration purpose:** Complete program lifecycle — enrollment, payments, compliance
failure triggering graduation from one program while remaining in another. Shows that
exiting one program doesn't affect other enrollments. Primary story for demonstrating
the compliance manager.

**Program(s) that the household is enrolled in:**

| Program               | Reason for eligibility            | Compliance                                                                    | Status                 |
| --------------------- | --------------------------------- | ----------------------------------------------------------------------------- | ---------------------- |
| Cash Transfer         | income 3,500 < 5,000, size 5 >= 2 | **Failed** — per_capita_income exceeded poverty_line after income improvement | **Exited** (graduated) |
| Universal Child Grant | child_count 2 > 0                 | N/A (no compliance on this program)                                           | Enrolled               |

**Household journey:**

1. Enrolled in Cash Transfer 180 days ago (hh_total_income 3,500, per_capita 700)
2. Also enrolled in Universal Child Grant
3. 3 Cash Transfer payments of $150 (compliant — per_capita_income < poverty_line)
4. Income improved → **compliance check fails** in cycle 4
5. Marked `non_compliant` on cycle membership → no entitlement generated
6. Non-compliance triggers graduation review → exited from Cash Transfer 30 days ago
7. Still receiving Universal Child Grant (2 children x $50 = $100/month)

**Individual dual enrollment:**

| Member                                          | Program         | Reason for eligibility |
| ----------------------------------------------- | --------------- | ---------------------- |
| Maria Santos (PH) / Ama Koffi (TG) / Kumari Perera (LK) (42, F) | Food Assistance | active registrant      |

Maria Santos (PH) / Ama Koffi (TG) / Kumari Perera (LK) receives monthly food baskets individually. Continues after household Cash
Transfer graduation.

**Existing change requests for the household:**

- `edit_individual` (approved) — Maria Santos's (PH) / Ama Koffi's (TG) / Kumari Perera's (LK) phone/address update after moving
- `edit_individual` (pending x2) — Conflict detection: two overlapping CRs for Maria Santos (PH) / Ama Koffi (TG) / Kumari Perera (LK)

**Geographical location:** Santa Rosa City (PH) / Aflao Sagbado (TG) / Kolonnawa (LK)

---

## Story 3: Multi-generational household

**Demonstration purpose:** Demonstrates a large multi-generational household with three
generations living together — grandparents, parents, and children. Shows household
composition complexity and how multiple individuals within a household can qualify for
different individual-targeting programs (e.g., elderly members for pension).

**Program(s) that the household is enrolled in:**

Not enrolled in group programs via named stories. Volume-generated households with
similar composition are enrolled based on blueprint eligibility flags.

**Demo points:**

- Multi-generational household structure (grandparents + parents + children)
- Elderly head (72) and spouse (68) — both individually eligible for Elderly Social
  Pension
- child_count = 3 (under 18: Lucia Reyes (PH) / Dzidzor Lawson (TG) / Wasana Rathnayake (LK) - 14y, Antonio Reyes (PH) / Kokou Lawson (TG) / Ruwan Rathnayake (LK) - 10y, Isabella Reyes (PH) / Ewoenam Lawson (TG) / Nimali Rathnayake (LK) - 6y; Jose Jr Reyes (PH) / Dela Lawson (TG) / Pradeep Rathnayake (LK) - 18y excluded)
- Large household (8 members) for household composition analysis

**Geographical location:** San Pablo City (PH) / Kpalime (TG) / Kandy Four Gravets (LK)

---

## Story 4: Emergency relief and transition

**Demonstration purpose:** Emergency response with fast-track enrollment, then
transition to longer-term Cash Transfer support after stabilization. Shows how displaced
families move through the system.

**Program(s) that the household is enrolled in:**

| Program          | Reason for eligibility                                 | Status   |
| ---------------- | ------------------------------------------------------ | -------- |
| Emergency Relief | dependency_ratio 5/2 = 2.5, displaced                  | Enrolled |
| Cash Transfer    | income 2,000 < 5,000, size 7 >= 2 (post-stabilization) | Enrolled |

**Household journey:**

1. Typhoon displaces family → emergency registration 60 days ago
2. Vulnerability assessment: very_high (displaced, lost assets, score 85)
3. Emergency Relief enrolled (fast-track 15-day cycles)
4. 2 emergency payments of $400 (Tier 2)
5. 30 days later: stabilized, enrolled in Cash Transfer for longer-term support
6. 1 Cash Transfer payment of $150

**Individual dual enrollment:**

| Member                                                   | Program         | Reason for eligibility |
| -------------------------------------------------------- | --------------- | ---------------------- |
| Ramon Gutierrez (PH) / Kosi Deku (TG) / Asanka Kumara (LK) (50, M) | Food Assistance | active registrant      |

Ramon Gutierrez (PH) / Kosi Deku (TG) / Asanka Kumara (LK) receives food baskets individually during the emergency period.

**Existing change requests for the household:**

- `edit_individual` (approved) — Ramon Gutierrez's (PH) / Kosi Deku's (TG) / Asanka Kumara's (LK) address update after relocation to temporary
  shelter

**Geographical location:** Antipolo City (PH) / Sokode (TG) / Galle Four Gravets (LK) — displacement zone

---

## Story 5: Disability support

**Demonstration purpose:** Disability-focused support with per-member benefit
calculation. Demonstrates disability assessment and the pending reassessment workflow.

**Program(s) that the household is enrolled in:**

| Program            | Reason for eligibility                         | Status   |
| ------------------ | ---------------------------------------------- | -------- |
| Disability Support | has_disabled_member = true, disabled_count = 1 | Enrolled |

**Household journey:**

1. Enrolled 100 days ago
2. Disability assessment completed for Miguel Martinez (PH) / Kofi Koudawo (TG) / Charitha Wickramasinghe (LK)
3. 3 monthly payments of $175 each (base $100 + 1 disabled member x $75)

**Existing change requests for the household:**

- `edit_individual` (pending) — Disability reassessment for Miguel Martinez (PH) / Kofi Koudawo (TG) / Charitha Wickramasinghe (LK) (updated medical
  documentation)

**Geographical location:** Makati City (PH) / Lome Commune (TG) / Dehiwala Mount Lavinia (LK)

---

## Story 6: Elder living alone

**Demonstration purpose:** Individual-only enrollment with no household. Multi-program
beneficiary receiving both cash (pension) and in-kind (food).

**Profile:** 72-year-old widow, lives alone, high vulnerability.

**Name:** Rosa Garcia (PH) / Adzo Amegah (TG) / Malini Silva (LK)

**Eligibility:**

| Program                | Why Eligible                |
| ---------------------- | --------------------------- |
| Elderly Social Pension | age 72 >= retirement_age 65 |
| Food Assistance        | active registrant           |

**Journey:**

1. Registered 200 days ago
2. Vulnerability assessment: high (elderly, alone, low income)
3. Enrolled in Elderly Social Pension 180 days ago
4. 4 monthly pension payments of $100
5. Enrolled in Food Assistance 175 days ago — receives monthly food baskets

**Change request:**

- `exit_registrant` (pending) — Graduated from food assistance program (pending
  approval)

**Geographical location:** Quezon City (PH) / Be (TG) / Fort (LK)

---

## Story 7: Age rejection

**Name:** Lorna Pascual (PH) / Ablavi Gbeassor (TG) / Priyanka Mendis (LK)

- 55-year-old woman
- Applied for Elderly Social Pension → **rejected** (age 55 < retirement_age 65)
- The only named story with an explicit rejection status in STORY_ENROLLMENTS

**Geographical location:** Pasig City (PH) / Nyekonakpoe (TG) / Pettah (LK)

---

## Story 8: Dual enrollment (from Story 2)

**Name:** Maria Santos (PH) / Ama Koffi (TG) / Kumari Perera (LK)

- Head of household Santos (PH) / Koffi (TG) / Perera (LK) (enrolled in Cash Transfer graduated + Universal Child Grant)
- Individually enrolled in Food Assistance 120 days ago
- **Demo point:** Same person visible in both individual and household program contexts

## Story 9: Dual enrollment (from Story 4)

**Name:** Ramon Gutierrez (PH) / Kosi Deku (TG) / Asanka Kumara (LK)

- Head of household Gutierrez (PH) / Deku (TG) / Kumara (LK) (enrolled in Emergency Relief + Cash Transfer)
- Individually enrolled in Food Assistance 50 days ago
- **Demo point:** Displaced person receiving household emergency aid + individual food
  support

---
