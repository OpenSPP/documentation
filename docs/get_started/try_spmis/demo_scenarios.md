---
openspp:
  doc_status: draft
  products: [registry, programs]
---

# SP-MIS Demo scenarios

You will here find a number of scenarios that can be used to demonstrate various functionality in OpenSPP.

## Before you start

- OpenSPP should be installed and running (see {doc}`../installation/index`)
- OpenSPP SPMIS Demo should be installed and demo data should be generated (see {doc}`install_data`)
- You need administrator access to OpenSPP

## Scenario 1: Payment failure and recovery

Show Dela Cruz (PH) / Mensah (TG) / Bandara (LK) household payment failure and recovery.

1. Open Dela Cruz (PH) / Mensah (TG) / Bandara (LK) household -> 4 members
2. Show Cash Transfer enrollment
3. Show payment history: paid -> **failed** -> paid (reprocessed)
4. Show successful reprocessing of failed payment

## Scenario 2: Program graduation via compliance failure

Show Santos (PH) / Koffi (TG) / Perera (LK) household graduating from Cash Transfer after compliance failure.

1. Open Santos (PH) / Koffi (TG) / Perera (LK) household -> 5 members
2. Cash Transfer program -> show compliance manager (`per_capita_income < poverty_line`)
3. Show cycle history: 3 cycles compliant, cycle 4 **non_compliant** (income improved)
4. Show cycle 4 membership state: `non_compliant` — no entitlement generated
5. Cash Transfer: **exited** (graduation triggered by compliance failure)
6. Universal Child Grant: still **enrolled** (2 children x $50) — unaffected
7. Open Maria Santos (PH) / Ama Koffi (TG) / Kumari Perera (LK) individually -> Food Assistance (dual enrollment continues)

## Scenario 3: Multi-generational household

Show Reyes (PH) / Lawson (TG) / Rathnayake (LK) household as a large multi-generational family.

1. Open Reyes (PH) / Lawson (TG) / Rathnayake (LK) household -> 8 members (3 generations)
2. Show household composition: grandparents (72, 68), parents (45, 42), children (18,
   14, 10, 6)
3. Show elderly members individually eligible for Elderly Social Pension
4. Demonstrate household composition analysis

## Scenario 4: Emergency to long-term support

Show Gutierrez (PH) / Deku (TG) / Kumara (LK) displaced family transitioning from emergency to cash transfer.

1. Open Gutierrez (PH) / Deku (TG) / Kumara (LK) household -> 7 members, displaced
2. Show Emergency Relief enrollment (fast-track 15-day cycles)
3. Show vulnerability assessment (score: very_high)
4. Show $400 Tier 2 payments
5. Show transition to Cash Transfer (30-day cycles, $150)
6. Open Ramon Gutierrez (PH) / Kosi Deku (TG) / Asanka Kumara (LK) individually -> Food Assistance

## Scenario 5: Disability support

Show Martinez (PH) / Koudawo (TG) / Wickramasinghe (LK) family with disabled child and pending reassessment.

1. Open Martinez (PH) / Koudawo (TG) / Wickramasinghe (LK) household -> 3 members
2. Show Miguel Martinez's (PH) / Kofi Koudawo's (TG) / Charitha Wickramasinghe's (LK) disability status
3. Show Disability Support Grant: $175 (base $100 + 1 member x $75)
4. Show 3 payment records
5. Show pending disability reassessment CR

## Scenario 6: Eligibility enforcement

Show rejections working correctly.

1. Lorna Pascual (PH) / Ablavi Gbeassor (TG) / Priyanka Mendis (LK) -> rejected for Elderly Pension (age 55 < 65)
2. Castillo (PH) / Agbodjan (TG) / Weerasinghe (LK) household -> rejected for Cash Transfer (income 12,000 > 5,000)
3. Navarro (PH) / Gbeho (TG) / Amarasinghe (LK) household -> rejected for Child Grant (0 children)

## Scenario 7: Dual enrollment

Show same person in individual + household programs.

1. Open Maria Santos (PH) / Ama Koffi (TG) / Kumari Perera (LK) individual -> enrolled in Food Assistance
2. Open Santos (PH) / Koffi (TG) / Perera (LK) household -> enrolled in Universal Child Grant, graduated from Cash Transfer
3. Show both visible from Maria Santos's (PH) / Ama Koffi's (TG) / Kumari Perera's (LK) profile

## Scenario 8: Change request lifecycle

Show different CR types and states across 13 change requests.

1. Approved: Juan Dela Cruz (PH) / Kofi Mensah (TG) / Nimal Bandara (LK) `update_id` — corrected national ID
2. Approved: Maria Santos (PH) / Ama Koffi (TG) / Kumari Perera (LK) `edit_individual` — phone/address update
3. Pending (conflict): Maria Santos (PH) / Ama Koffi (TG) / Kumari Perera (LK) — two overlapping CRs
4. Draft: Aquino (PH) / Tetteh (TG) / Herath (LK) `edit_group` — UI workflow demo
5. Pending: Rosa Garcia (PH) / Adzo Amegah (TG) / Malini Silva (LK) `exit_registrant` — food assistance graduation (pending approval)
6. Approved: Morales (PH) / Agbeko (TG) / Fernando (LK) `add_member` — newborn added
7. Pending: Morales (PH) / Agbeko (TG) / Fernando (LK) `remove_member` — adult child moving out
8. Pending: Bautista (PH) / Akakpo (TG) / Gunasekara (LK) `transfer_member` — child to elderly relatives
9. Approved: Navarro (PH) / Gbeho (TG) / Amarasinghe (LK) `change_hoh` — set new head of household
10. Draft: IND1 `create_group` — register new household
11. Rejected: Bautista (PH) / Akakpo (TG) / Gunasekara (LK) `split_household` — incomplete documentation
12. Revision: IND2 `merge_registrants` — duplicate data quality

## Scenario 9: Compliance manager overview

Show how compliance criteria work on Cash Transfer — contrasting a failure (Santos (PH) / Koffi (TG) / Perera (LK)) with a
pass (Dela Cruz (PH) / Mensah (TG) / Bandara (LK)) on the same program.

1. Open Cash Transfer program -> show compliance manager config
2. Show CEL expression: `per_capita_income < poverty_line`
3. Open Santos (PH) / Koffi (TG) / Perera (LK) cycle membership -> state: `non_compliant` (income improved)
4. Contrast with Dela Cruz (PH) / Mensah (TG) / Bandara (LK) cycle membership -> state: `enrolled` (compliant, per_capita 1,000
   < 5,000)
5. Show Conditional Child Grant -> also has compliance manager
   (`per_capita_income < income_threshold`)
6. **Key point:** Eligibility gates enrollment; compliance gates each cycle's payment
