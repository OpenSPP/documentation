---
openspp:
  doc_status: draft
  products: [farmer_registry]
---

# Farmer Registry demo scenarios

You will here find a number of scenarios that can be used to demonstrate various functionality in OpenSPP.

## Before you start

- OpenSPP should be installed and running (see {doc}`../../installation/index`)
- OpenSPP Farmer Registry Demo should be installed and demo data should be generated (see {doc}`install_data`)
- You need administrator access to OpenSPP

---

## Scenario 1: New enrollment

Walk through enrolling a previously unregistered smallholder.

1. Open **Settings → Vocabularies → Manage Vocabularies** and confirm the FAO-aligned
   vocabularies are loaded: `urn:fao:icc:1.1` (crops), `urn:fao:livestock:2020`
   (livestock), `urn:fao:asfis:2024` (aquaculture). These back the species pickers used
   in step 5 below.
2. Open **Registry → Configuration → Seasons**. The list shows three points of the
   `spp.farm.season` state machine: a `closed` prior-year season, an `active`
   current-year season, and (optionally) a `draft` future season the user can transition
   by hand. Activities can only be entered against an active season.
3. Open **Registry → Browse All (Audit) → All Groups → New**. Give the farm a name and
   select **Farm** as the **Group Type**.
4. Open the **Farm Details** tab and fill in the **Farm Size** section: set **Total Farm
   Size (hectares)**, **Acreage Under Crops**, and **Years of Experience**. Open the
   **Participation** tab and add the head member in the **Group Members** section.
5. Add a crop activity for the new farm. The species picker is backed by the FAO ICC 1.1
   vocabulary — pick `0116` Rice, paddy (matching Santos Farm) or `0115` Maize, white (matching
   Mangudadatu Farm). For aquaculture, the picker uses FAO ASFIS — pick `TIL` Tilapia (matching Dela Cruz Fishpond).
6. From the new farm's form, open the **Participation** tab and click **Enroll in
   Program**. In the wizard, pick **Input Subsidy** and confirm. This creates a program
   membership record for the farm in `draft` state.
7. Open **Programs → Programs → Input Subsidy** and click **Enroll Eligible**. This
   evaluates the CEL expression against all `draft` and `not_eligible` memberships —
   farms whose facts match the eligibility criteria are moved to `enrolled`.
8. The new farm is now enrolled. Open the program's **Cycles** tab to see it listed for
   the next scheduled payment.

**Key messages:**

- Eligibility is data-driven; changing the farm's facts changes the verdict
- The CEL evaluates on demand (**Enroll Eligible** for draft memberships, **Verify Eligibility** to re-evaluate already-enrolled ones) and at every cycle creation
- Activity classification uses FAO standards (ICC 1.1 / livestock 2020 / ASFIS)
  end-to-end — no free-text species fields, no national-only codes

---

## Scenario 2: Multi-program coordination

Show how a single farm fans out into two programs.

1. Open the Dela Cruz Farm record (**Registry → Browse All (Audit) → All Groups → Dela Cruz Farm**) —
   scroll to the **Program Enrollments** section to see two memberships (Input Subsidy +
   Livestock Support).
2. Open **Programs → Programs → Input Subsidy** — click the **Cycles** smart button —
   open cycle 1 or cycle 2 — click the **Payments** smart button — search by beneficiary **Dela
   Cruz** to see the payment record.
3. Open **Programs → Programs → Livestock Support** — click the **Cycles** smart button
   — open cycle 1 — click the **Payments** smart button — search by beneficiary **Dela
   Cruz** to see a different payment amount.
4. Show that the two payment streams are independent (separate batches, separate
   journals).

**Key messages:**

- Multi-program is a property of _fact pattern_, not configuration
- Each program owns its own cycle/entitlement workflow

---

## Scenario 3: Graduation from a program

Show that a farm which has completed its program cycles exits with an `Exited` status.

1. Open **Programs → Programs → Input Subsidy** — **Configuration** tab — scroll to the
   **Compliance Criteria** section — open the linked manager record to show the CEL
   `has_productive_land == true and farm_size_hectares > 0`.
2. Open Santos Farm (**Registry → Browse All (Audit) → All Groups → Santos Farm**) — open
   the **Participation** tab — the **Program Enrollments** section shows the Input Subsidy
   Program with state `Exited` and latest cycle status `Enrolled`, meaning Santos Farm
   completed all cycles compliantly and has since exited the program.

**Key messages:**

- `Exited` is a terminal state set manually by a program officer — there is no automatic exit based on cycle count
- A farm that remains compliant throughout all cycles can be exited once the program is complete

---

## Scenario 4: Aquaculture targeting

Demonstrate that the system handles non-crop farming.

1. Open Dela Cruz Fishpond (**Registry → Browse All (Audit) → All Groups → Dela Cruz Fishpond**) — **Aquaculture Activities**
   tab — confirm Nile tilapia is listed as a commercial activity.
2. Open the **Farm Details** tab — in the **Acreage Breakdown** section, confirm
   **Acreage Under Aquaculture** is 0.5 ha.
3. Open **Programs → Programs → Aquaculture Support** — **Configuration** tab — scroll
   to the **Who Qualifies / Eligibility Method** block — CEL
   `r.is_group == true and aquaculture_count > 0`.
4. Back on the program form, click the **Cycles** smart button — Dela Cruz Fishpond appears
   in cycles 1 and 2 with payment ₱250 each.
5. Open Santos Farm — **Participation** tab — click **Enroll in Program**, select
   **Aquaculture Support** and confirm. The membership is created in `draft` state.
6. Open **Programs → Programs → Aquaculture Support** and click **Enroll Eligible**.
   The CEL evaluates all `draft` and `not_eligible` memberships — Santos Farm has
   `aquaculture_count == 0` so its membership moves to `not_eligible` instead of
   `enrolled`.

**Key messages:**

- Programs can target specific livelihood types via CEL
- The same farm record carries multiple livelihoods (mixed farms enroll into multiple
  programs, single-livelihood farms into one)

---

## Scenario 5: Climate Resilience for idle land

Show how `farm_size_idle` becomes a positive signal for climate-vulnerable households.

1. Open **Programs → Programs → Climate Resilience** — **Configuration** tab — scroll to
   the **Who Qualifies / Eligibility Method** block — CEL
   `r.is_group == true and is_smallholder and farm_size_idle > 0`.
2. Open Mangudadatu Farm (**Registry → Browse All (Audit) → All Groups → Mangudadatu Farm**) —
   **Farm Details** tab — confirm 3 ha under crops + 1 ha fallow/idle = 4 ha total —
   matches CEL.
3. Open **Programs → Programs → Climate Resilience** — click the **Cycles** smart button
   — open each cycle and click the **Payments** smart button to verify Mangudadatu Farm
   received ₱200 in each cycle.
4. Contrast with a large commercial farm: open **Registry → Browse All (Audit) → All
   Groups** — click the **Search bar → Add Custom Filter** — set field **Total Farm Size
   (hectares)**, operator **=**, value **50** — click **Search**. Open the matching farm
   and check its **Participation** tab — it has no Climate Resilience enrollment, because
   it fails `is_smallholder` even though its idle acreage is greater than 0.

**Key messages:**

- Idle land isn't always a negative — Climate Resilience treats it as a vulnerability signal
- The CEL requires both `is_smallholder` and `farm_size_idle > 0` — a large farm with idle land would still be excluded

---

## Scenario 6: Eligibility rejection paths

Show that two smallholder farms with the same size receive different program outcomes because
of a single CEL criterion — livelihood type.

1. Open **Programs → Programs → Livestock Support** — **Configuration** tab — scroll to the
   **Who Qualifies / Eligibility Method** block — CEL `r.is_group == true and livestock_count > 0`.
2. Open **Programs → Programs → Aquaculture Support** — **Configuration** tab — scroll to the
   **Who Qualifies / Eligibility Method** block — CEL `r.is_group == true and aquaculture_count > 0`.
3. Open Garcia Farm (**Registry → Browse All (Audit) → All Groups → Garcia Farm**) — **Participation**
   tab — **Program Enrollments** shows Livestock Support with state `enrolled`. Garcia Farm has no
   aquaculture activities, so it is not enrolled in Aquaculture Support.
4. To prove the exclusion live: click **Enroll in Program**, select **Aquaculture Support** and confirm
   — the membership is created in `draft` state. Open **Programs → Programs → Aquaculture Support**
   and click **Enroll Eligible** — Garcia Farm's membership moves to `not_eligible` because
   `aquaculture_count == 0`.
5. Open Dela Cruz Fishpond (**Registry → Browse All (Audit) → All Groups → Dela Cruz Fishpond**) —
   **Participation** tab — **Program Enrollments** shows Aquaculture Support with state `enrolled`.
   Dela Cruz Fishpond has no livestock, so it is not enrolled in Livestock Support.

**Key messages:**

- Rejecting one program does not reject all — each program's CEL is evaluated independently
- Two farms with the same total size can receive opposite outcomes; the deciding factor is what
  the farm actually produces, not its size or location
- No manual classification is needed — the CEL reads the farm's activity data directly

---

## Scenario 7: Cooperative as group of groups

Demonstrate the group-of-groups data model.

1. Open Nueva Ecija Rice Cooperative (**Registry → Browse All (Audit) → All
   Groups → Nueva Ecija Rice Cooperative**) — open the **Participation** tab — the
   **Group Members** section lists Santos Farm and Martinez Farm.
2. Notice the **Programs** smart button on the cooperative record shows **0** — the
   cooperative itself holds no program enrollments.
3. Open Santos Farm — the **Programs** smart button shows its own enrollments (Input
   Subsidy). Programs are carried by each member farm individually, not by the cooperative.

**Key messages:**

- Cooperatives are organizational records; programs target the underlying member farms
- The Programs smart button on the cooperative showing 0 is the visual proof — eligibility
  and payments belong to the farms, not the umbrella group
- Federations can pool farms from different provinces/regions; each member farm retains its own geographic and program data

---

## Scenario 8: Change request lifecycle

Walk through the 9 demo CRs to show every CR state. Open them from **Change Requests →
All Requests**, then use the search filter to narrow by registrant (e.g. type the farm's
name in the search bar) to see per-farm CRs.

1. Approved: Santos Farm `update_farm_details` — farm expanded after acquisition
2. Applied: Dela Cruz Farm `update_farm_details` — added livestock area, applied automatically
3. Pending: Dela Cruz Farm `manage_farm_activity` — register chicken activity (awaiting validator)
4. Approved: Garcia Farm `update_farm_details` — land tenure transfer
5. Draft: Martinez Farm `manage_farm_activity` — register organic crop (UI workflow stage)
6. Pending: Dela Cruz Fishpond `manage_farm_activity` — update tilapia yield
7. Rejected: Mangudadatu Farm `update_farm_details` — reclassify idle land, rejected pending verification
8. Approved: Pangandaman Farm `manage_farm_activity` — register dry-season maize
9. Revision: Villanueva Farm `update_farm_details` — experience claim flagged for documentation

**Key messages:**

- The demo covers all 6 CR states: Draft, Pending, Approved, Applied, Rejected, and Revision
- Two CR types are demonstrated: `update_farm_details` for farm profile changes and
  `manage_farm_activity` for adding or updating agricultural activities

---

## Scenario 9: Approval workflow on cycles

Demonstrate that a program can require human sign-off before a cycle is finalized.

```{note}
This scenario requires one configuration step before starting: open the program's
**Program Schedule** manager, set the **Approval Definition** field to
**Farmer: Cycle Approval - Cycle Approver**, and save.
```

1. Open **Programs → Programs → Input Subsidy** — click **New Cycle** in the header —
   the cycle is created in `draft` state.
2. Open the new cycle — click **Prepare Entitlements** — entitlements are generated for
   all enrolled beneficiaries.
3. Click **Apply Compliance Criteria** — the system evaluates each beneficiary against
   the program's compliance rules; non-compliant farms are marked and excluded from
   this cycle's payments.
4. Click **Submit for Approval** — the cycle moves to `to_approve`.
5. Log out and log in as `cycle_approver` (password: `demo`) — navigate to
   **Programs → Cycles** — find the pending cycle — click **Approve** — the cycle moves
   to `approved`.
6. Log back in as admin — return to Input Subsidy — the approved cycle is now ready
   for payment processing.

**Key messages:**

- Cycle approval is opt-in per program — set via the **Approval Definition** field on
  the Program Schedule manager
- Compliance criteria run inside the cycle, after entitlements are prepared — a farm
  can be enrolled but still excluded from a specific cycle if it fails compliance at
  that point in time
- The approval gate separates cycle creation from cycle execution, allowing a supervisor
  to review the compliant beneficiary list and amounts before funds are committed

---

## Scenario 10: GIS and irrigation walk for Mangudadatu Farm

Anchor the GIS, land-record, and irrigation modules in a single coherent flow. The
narrative hook: Mangudadatu Farm's 1 ha of idle/fallow land is the **downstream consequence of
reduced reservoir capacity**, not random non-cultivation.

```{note}
**Prerequisite — MapTiler API key:** The GIS map widget requires a MapTiler API key
configured in **Settings → General Settings → Map Provider**. Without it, the map panel
is blank; GPS coordinates and land parcel data are still stored and visible in the form
fields, but the visual map will not render. Set up MapTiler before running this scenario.
```

1. Open Mangudadatu Farm (**Registry → Browse All (Audit) → All Groups → Mangudadatu Farm**) —
   **Profile** tab — **Location** section — the GIS map shows the farm pinned near
   Cotabato City, Maguindanao.
2. Click the **Land Parcels** smart button in the header — the single land parcel record
   confirms the farm's total area of 4 ha, of which 1 ha is fallow/idle.
3. Open the **Irrigation** tab — two assets are linked to this farm:
   - **Cotabato Irrigation Reservoir** — type: Reservoir, capacity 5,000 m³,
     destination: Cotabato Main Canal Branch
   - **Cotabato Main Canal Branch** — type: Canal, capacity 300 m³,
     source: Cotabato Irrigation Reservoir
4. The inline list already shows the source-to-destination network — the reservoir feeds
   the canal, and the canal is what serves Mangudadatu Farm's fields. The reduced
   reservoir capacity explains why 1 ha of the farm sits idle.
5. Go back to **Registry → Browse All (Audit) → All Groups** — click **Filters →
   Add Custom Filter** — set field **Acreage Fallow/Idle**, operator **greater than**,
   value **0** — click **Search**. Mangudadatu Farm appears alongside other idle-land
   farms. This is the list a ministry planner would use to target a climate or
   irrigation rehabilitation intervention.

**Key messages:**

- The registry stores more than beneficiary data — farm location, land parcels, and
  irrigation infrastructure are all linked to the same farm record
- Idle land is not just a classification field — it can be traced to a physical cause
  (degraded reservoir) visible in the same system
- The filter on fallow/idle acreage is the tool a ministry planner uses to build a
  targeted intervention list without any external GIS software
