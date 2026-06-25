---
openspp:
  doc_status: draft
  products: [farmer_registry]
---

# Farmer Registry stories

The OpenSPP Farmer Registry demo module includes a number of fixed farms that show various farm situations. This will allow you to easily understand the available functionalities.

## Before you start

- OpenSPP should be installed and running (see {doc}`../../installation/index`)
- OpenSPP Farmer Registry Demo should be installed and demo data should be generated (see {doc}`install_data`)
- You need administrator access to OpenSPP

> **Locale note:** The reference data shipped with this demo is coded against `fil_PH`
> (Philippine names, currency, area codes, bank list, place names). The structure of the
> stories — roles, geographic dimension, program enrollments — is locale-agnostic and can
> be re-keyed to any country profile by swapping the persona names, area codes, GPS
> coordinates, and bank list referenced in the demo generator. Place names in the prose
> below ("Cabanatuan", "Cotabato City", etc.) are illustrative; the underlying steps
> apply to any equivalent regional centre/rural area pair.

## Demo users

The demo install seeds the following user accounts. All passwords are `demo` unless noted otherwise. Use these to exercise role-gated views, approval flows, and the CR validator chain.

| Login                | Password | Role(s)                         | Used in scenarios                              |
| -------------------- | -------- | ------------------------------- | ---------------------------------------------- |
| `admin`              | `admin`  | System Administrator (built-in) | Any — full access                              |
| `manager`            | `demo`   | Farm Manager + CR Requestor     | Program lifecycle, CR submission, dashboards   |
| `officer`            | `demo`   | Farm User + CR Requestor        | Farm data entry, CR submission                 |
| `supervisor`         | `demo`   | Farm Manager                    | Program manager view, approvals                |
| `viewer`             | `demo`   | Farm User                       | Read-only walkthroughs                         |
| `program_manager`    | `demo`   | Program Manager + Farm User     | Cycle + entitlement approval (Scenario 9)      |
| `cycle_approver`     | `demo`   | Cycle Approver                  | Cycle approval workflows                       |
| `cr_local_validator` | `demo`   | CR Local Validator (Tier-1)     | Local CR approval / revision-request scenarios |
| `cr_hq_validator`    | `demo`   | CR HQ Validator (Tier-2)        | HQ-tier CR approval scenarios                  |

> The `cycle_approver` account handles standard cycle approval workflows. The
> `program_manager` account additionally carries **queue-job manager** rights, which
> approving a cycle needs in order to enqueue the entitlement-validation job — use
> `program_manager` for the Scenario 9 approval walk where that job enqueue step is
> demonstrated.

## Farm stories

Each farm is identified by its family name. Programs
that target groups enroll the farm — not individual members. Multi-program enrollment is
allowed when the farm satisfies more than one program's CEL.

---

## Story 1: Santos Farm — Smallholder rice farmer, full lifecycle to graduation

**Demonstration purpose:** End-to-end Input Subsidy lifecycle — enrolled, paid through
three cycles, then graduated. Contrasts with Dela Cruz Farm which stays multi-enrolled and Garcia Farm which
continues active. Primary story for "graduation after target met".

**Program(s) the farm is enrolled in:**

| Program       | Reason for eligibility                        | Compliance                                           | Status                 |
| ------------- | --------------------------------------------- | ---------------------------------------------------- | ---------------------- |
| Input Subsidy | Smallholder (2.0 ha ≤ 5), has productive land | **Passed** each cycle — productive land share ≥ 50 % | **Exited** (graduated) |

**Farm journey:**

1. Enrolled in Input Subsidy 150 days ago (rice, 2.0 ha, Cabanatuan area)
2. Payment #1 (₱200) — paid 120 days ago
3. Payment #2 (₱200) — paid 90 days ago
4. Payment #3 (₱200) — paid 60 days ago
5. Compliance pass each cycle (productive land = 100 % of total)
6. **Graduated 30 days ago** — target met, exited program

**Existing change requests for the farm:**

- `update_farm_details` (approved) — Farm expanded to 3.0 ha after acquiring adjacent parcel

**Farm assets:** 1 hand tractor (machinery, operational) attached to the main land parcel.

**Activity vocabulary:** Rice cultivation references the FAO ICC 1.1 crop code `0116`
(Rice, paddy) — the same standard used by national agricultural censuses.

**Geographical location:** Inland rice plains — Cabanatuan, Nueva Ecija

---

## Story 2: Dela Cruz Farm — Multi-program mixed farmer

**Demonstration purpose:** A farm that satisfies more than one program's CEL
simultaneously. Demonstrates concurrent enrollment, separate cycle/payment streams, and
multi-CR sequencing on the same farm. Primary story for "multi-program coordination".

**Program(s) the farm is enrolled in:**

| Program           | Reason for eligibility                                        | Compliance                                   | Status   |
| ----------------- | ------------------------------------------------------------- | -------------------------------------------- | -------- |
| Input Subsidy     | Smallholder (3.0 ha), has productive land (rice + vegetables) | **Passed** — productive land = 67 % of total | Enrolled |
| Livestock Support | `livestock_count` = 50 (chickens) > 0                        | N/A (no compliance on this program)          | Enrolled |

**Farm journey:**

1. Enrolled in Input Subsidy 100 days ago (mixed farm: 1.5 ha rice + 0.5 ha vegetables + 50 chickens)
2. Payment #1 — Input Subsidy ₱200 — paid 70 days ago
3. Payment #2 — Input Subsidy ₱200 — paid 40 days ago
4. Payment #3 — Input Subsidy ₱200 — paid in the current cycle
5. Enrolled in Livestock Support 80 days ago (chickens = 50 heads)
6. Payment #1 — Livestock Support ₱275 — paid 50 days ago
7. Payment #2 — Livestock Support ₱275 — paid 20 days ago
8. Payment #3 — Livestock Support ₱275 — paid in the current cycle
9. Both enrollments still active

**Existing change requests for the farm:**

- `update_farm_details` (applied) — Expanded to 4.0 ha, added livestock area
- `manage_farm_activity` (pending) — Register new chicken-rearing activity (50 heads, subsistence)

**Geographical location:** Inland mixed farming — San Pablo City, Laguna

---

## Story 3: Garcia Farm — Senior livestock farmer, gender + age diversity

**Demonstration purpose:** A senior female farmer whose primary income is livestock.
Demonstrates non-cash-crop targeting and the per-head benefit formula. Contrasts with
Santos Farm's flat per-hectare payment.

**Program(s) the farm is enrolled in:**

| Program           | Reason for eligibility           | Compliance                          | Status   |
| ----------------- | -------------------------------- | ----------------------------------- | -------- |
| Livestock Support | `livestock_count` = 20 (goats) > 0 | N/A (no compliance on this program) | Enrolled |

**Farm journey:**

1. Enrolled in Livestock Support 120 days ago (mixed farm: 0.5 ha crops + 20 goats, 1.0 ha total)
2. Payment #1 — ₱275 (livestock base 75 + 20 heads × ₱10) — paid 90 days ago
3. Payment #2 — ₱275 — paid 60 days ago
4. Payment #3 — ₱275 — paid 30 days ago
5. Active enrollment, not yet graduated

**Existing change requests for the farm:**

- `update_farm_details` (approved) — Land tenure transferred to owner after inheritance

**Geographical location:** Inland plateau, livestock area — Lipa City, Batangas

---

## Story 4: Mangudadatu Farm — Climate-vulnerable farmer with idle land

**Demonstration purpose:** A farmer whose declared idle land triggers Climate Resilience
eligibility. Demonstrates the program's targeting logic (`farm_size_idle > 0`) and BARMM
conflict-affected context. Contrasts with Santos Farm and Dela Cruz Farm which satisfy productive-land programs
only.

**Program(s) the farm is enrolled in:**

| Program            | Reason for eligibility                             | Compliance                          | Status   |
| ------------------ | -------------------------------------------------- | ----------------------------------- | -------- |
| Climate Resilience | Smallholder (4.0 ha), `farm_size_idle` = 1.0 ha > 0 | N/A (no compliance on this program) | Enrolled |

**Farm journey:**

1. Enrolled in Climate Resilience 55 days ago (vulnerability: very_high; 3.0 ha rice + 1.0 ha idle/fallow)
2. Payment #1 — ₱200 — paid 50 days ago
3. Payment #2 — ₱200 — paid 35 days ago
4. Active enrollment

**Existing change requests for the farm:**

- `update_farm_details` (rejected) — Request to reclassify productive area (1.5 ha crops, 2.5 ha idle); rejected pending field verification

**Irrigation infrastructure** (anchors Scenario 10):

| Asset                         | Type      | Capacity              | Status                                | Network role                         |
| ----------------------------- | --------- | --------------------- | ------------------------------------- | ------------------------------------ |
| Cotabato Irrigation Reservoir | Reservoir | 5,000 m³ effective    | Reduced (design ~15,000 m³, silted)   | Source for the canal branch          |
| Cotabato Main Canal Branch    | Canal     | 300 m³ flow capacity  | Carrying reduced flow                 | Sourced by the reservoir; serves Mangudadatu Farm |

The reduced upstream capacity explains Mangudadatu Farm's 1 ha of idle/fallow land — it is the
downstream consequence of a degraded irrigation network, not random non-cultivation.

**Land parcel:** A polygon (~4 ha total area, of which 1 ha idle) is plotted at
Cotabato City and exportable as GeoJSON via `spp.land.record.get_geojson()`.

**Geographical location:** Inland BARMM — Cotabato City, Maguindanao

---

## Story 5: Martinez Farm — Young female farmer, organic transition

**Demonstration purpose:** Young female farmer in the highlands transitioning toward
organic agriculture. Demonstrates the diversity dimension and Logic Pack-driven
eligibility for early-career smallholders.

**Program(s) the farm is enrolled in:**

| Program       | Reason for eligibility                    | Compliance                                    | Status   |
| ------------- | ----------------------------------------- | --------------------------------------------- | -------- |
| Input Subsidy | Smallholder (2.0 ha), has productive land | **Passed** — productive land = 100 % of total | Enrolled |

**Farm journey:**

1. Enrolled in Input Subsidy 70 days ago (vegetables + maize, 2.0 ha)
2. Payment #1 — ₱200 — paid 45 days ago
3. Payment #2 — ₱200 — paid in the current cycle
4. Payment #3 — ₱200 — paid in the current cycle
5. Active enrollment

**Existing change requests for the farm:**

- `manage_farm_activity` (draft) — Register organic vegetable cultivation (commercial, 0.5 ha)

**Geographical location:** Mountain valley highlands — La Trinidad, Benguet

---

## Story 6: Dela Cruz Fishpond — Aquaculture, non-crop farming

**Demonstration purpose:** Demonstrates that the registry handles non-crop farming. The
farm is enrolled in Aquaculture Support — a program that targets a single field
(`aquaculture_count > 0`) ignored by every other program.

**Program(s) the farm is enrolled in:**

| Program             | Reason for eligibility          | Compliance                          | Status   |
| ------------------- | ------------------------------- | ----------------------------------- | -------- |
| Aquaculture Support | `aquaculture_count` > 0 (tilapia) | N/A (no compliance on this program) | Enrolled |

**Farm journey:**

1. Enrolled in Aquaculture Support 90 days ago (0.5 ha tilapia fishpond)
2. Payment #1 — ₱250 — paid 60 days ago
3. Payment #2 — ₱250 — paid 30 days ago
4. Active enrollment

**Existing change requests for the farm:**

- `manage_farm_activity` (pending) — Update tilapia production (3,500 kg current, 4,000 kg expected)

**Geographical location:** Inland fishpond area — Dagupan, Pangasinan

---

## Story 7: Pangandaman Farm — Equipment Grant + Input Subsidy stack

**Demonstration purpose:** Young but experienced female farmer in BARMM. Qualifies for
both Input Subsidy and Equipment Grant (12 years' experience clears the
`experience_years >= 2` threshold). Demonstrates BARMM women in agriculture.

**Program(s) the farm is enrolled in:**

| Program         | Reason for eligibility                    | Compliance                                                | Status   |
| --------------- | ----------------------------------------- | --------------------------------------------------------- | -------- |
| Input Subsidy   | Smallholder (1.5 ha), has productive land | **Passed** — productive land = 100 % of total             | Enrolled |
| Equipment Grant | Smallholder, `experience_years` 12 ≥ 2   | **Passed** — still smallholder, still has productive land | Enrolled |

**Farm journey:**

1. Enrolled in Input Subsidy 130 days ago (rice + vegetables, 1.5 ha)
2. Payment #1 — Input Subsidy ₱200 — paid 100 days ago
3. Payment #2 — Input Subsidy ₱200 — paid 70 days ago
4. Payment #3 — Input Subsidy ₱200 — paid in the current cycle
5. Enrolled in Equipment Grant 60 days ago
6. Payment #1 — Equipment Grant ₱500 — paid 30 days ago
7. Both enrollments active

**Existing change requests for the farm:**

- `manage_farm_activity` (approved) — Register new maize cultivation for dry season (commercial, 0.8 ha)

**Geographical location:** Inland BARMM — Marawi, Lanao del Sur

---

## Story 8: Villanueva Farm — Threshold edge case at the smallholder boundary

**Demonstration purpose:** Boundary-condition testing. The farm sits at the smallholder
threshold (5.0 ha) with deep diversification. Demonstrates that the eligibility CEL
evaluates correctly at the exact boundary and that highly experienced farmers (25 years)
still qualify when other criteria fit.

**Program(s) the farm is enrolled in:**

| Program           | Reason for eligibility                          | Compliance                          | Status   |
| ----------------- | ----------------------------------------------- | ----------------------------------- | -------- |
| Livestock Support | `livestock_count` = 45 (15 cattle + 30 goats) > 0 | N/A (no compliance on this program) | Enrolled |

**Farm journey:**

1. Enrolled in Livestock Support 180 days ago (3.0 ha crops + 2.0 ha livestock; 15 cattle + 30 goats)
2. Payment #1 — ₱275 — paid 150 days ago
3. Payment #2 — ₱275 — paid 120 days ago
4. Payment #3 — ₱275 — paid in the current cycle
5. Active enrollment, sitting exactly at smallholder boundary

**Existing change requests for the farm:**

- `update_farm_details` (revision) — Update experience years (claimed 20) and land breakdown; revision requested for supporting documents
- `manage_farm_asset` (pending) — Register additional water pump for irrigation expansion

**Farm assets:** 1 water pump (machinery, operational) attached to the main land parcel.

**Geographical location:** Inland highland plateau — Malaybalay, Bukidnon

---

## Cooperative stories

Cooperatives in the demo are _groups of farms_ — a true group-of-groups hierarchy. They
demonstrate that the registry supports federation structures and aggregated metrics over
member farms.

### Story 9: Nueva Ecija Rice Cooperative

**Demonstration purpose:** A two-farm rice cooperative spanning Central Luzon.
Aggregated farm size = 4.0 ha; combined eligibility behaves as the union of member-farm
CELs. Demonstrates the group-of-groups data model and cooperative-level reporting
(combined hectarage, member count).

**Member farms:** Santos Farm (Nueva Ecija) + Martinez Farm (Benguet).

**Geographical location:** Central Luzon (Nueva Ecija, Benguet).

---

### Story 10: BARMM Farmers Federation

**Demonstration purpose:** A regional federation pooling two BARMM smallholder farms.
Combined size 5.5 ha — _exceeds_ the smallholder threshold when viewed in aggregate.
Demonstrates that program eligibility is computed per _member_ farm, not on the
federation aggregate (so each member is still treated as a smallholder).

**Member farms:** Mangudadatu Farm (Maguindanao) + Pangandaman Farm (Lanao del Sur).

**Geographical location:** BARMM (Maguindanao, Lanao del Sur).
