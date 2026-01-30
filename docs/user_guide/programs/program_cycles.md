---
openspp:
  doc_status: draft
  products: [programs]
  applies_to:
    - sp_mis
---

# Work with program cycles

**Applies to:** SP-MIS

## What you will do

Learn how to navigate, understand, and manage program cycles in OpenSPP.

## Before you start

- You need **Program Validator**, **Program Manager**, **Program Cycle Approver**, or **Administrator** roles assigned to your user account
- The program must be in **Active** state
- At least one beneficiary must be enrolled in the program

## What is a cycle?

A **cycle** represents a distribution period within a program. For example:

- Monthly cash transfers have 12 cycles per year (one per month)
- Quarterly food assistance has 4 cycles per year
- One-time emergency payments have a single cycle

Each cycle:

- Has a start and end date
- Contains beneficiaries copied from the program
- Generates entitlements for each beneficiary
- Goes through an approval workflow before distribution

## Cycle states

Cycles progress through these states:

| State | Meaning | What happens next |
|-------|---------|-------------------|
| **Draft** | Cycle is being prepared | Copy beneficiaries, prepare entitlements |
| **To Approve** | Waiting for approval | Validator reviews and approves or rejects |
| **Approved** | Ready for distribution | Prepare and send payments |
| **Distributed** | Benefits have been sent | Mark as ended when complete |
| **Cancelled** | Cycle was rejected or cancelled | Can be reset to draft |
| **Ended** | Cycle is complete | Read-only |

![Cycle states progression](/_images/en-us/programs/cycles/01-cycle-form-showing-state-progression-badge.png)

## View program cycles

1. Click **Programs** > **Programs** in the main menu.

2. Click on a program to open it.

3. View cycles using either method:
   - **From the Overview tab**: The **Recent Cycles** section shows the most recent cycles.
   - **Using the smart button**: Click the **Cycles** smart button to see all cycles.

![Recent cycles in overview](/_images/en-us/programs/cycles/02-program-overview-tab-showing-recent-cycles-section.png)

![Cycles smart button](/_images/en-us/programs/cycles/03-cycles-smart-button-highlighted-on-program-form.png)

4. Click on a cycle row to open the cycle form.

![Open Cycle](/_images/en-us/programs/cycles/04-open-cycle-form.png)

## Understand the cycle form

### Overview tab

| Field | Description |
|-------|-------------|
| **Name** | Cycle name (e.g., "January 2025") |
| **Program** | Parent program |
| **Sequence** | Order of this cycle (1, 2, 3, etc.) |
| **Start Date** | When the cycle begins |
| **End Date** | When the cycle ends |
| **Total Amount** | Sum of all entitlements in this cycle |

![Cycle overview](/_images/en-us/programs/cycles/05-cycle-overview.png)

### Smart buttons

| Button | Shows |
|--------|-------|
| **Beneficiaries** | Enrolled beneficiaries in this cycle |
| **Entitlements** | Generated entitlements |
| **Payments** | Payment batches (if configured) |

## Create a new cycle

1. Open the program where you want to create a cycle.

2. Click the **New Cycle** button in the header.

![New cycle button](/_images/en-us/programs/cycles/07-new-cycle-button-in-program-header.png)

3. A notification confirms the new cycle was created.

![Cycle created notification](/_images/en-us/programs/cycles/08-notification-confirming-new-cycle-was-created.png)

4. Click the **Cycles** smart button and select the new cycle to open it.

## Cycle workflow

Cycles follow this workflow: Draft → To Approve → Approved → Distributed → Ended

### Step 1: Copy beneficiaries

When a cycle is first created, it automatically copies all currently enrolled beneficiaries from the program. 

**If new beneficiaries are enrolled after the cycle was created:**

1. Open the cycle (must be in **Draft** state).

2. Click **Copy Beneficiaries** to add the newly enrolled beneficiaries to the cycle.

   ![Copy beneficiaries button](/_images/en-us/programs/cycles/09-copy-beneficiaries-button-on-cycle-form.png)

```{note}
This function only adds newly enrolled beneficiaries. It does not remove beneficiaries who no longer meet eligibility criteria.
```

### Step 2: Prepare entitlements

Generate entitlements for all beneficiaries in the cycle:

1. Click **Prepare Entitlements**.

   ![Prepare entitlements button](/_images/en-us/programs/cycles/10-prepare-entitlements-button-on-cycle-form.png)

2. The system calculates benefit amounts based on the program rules.

3. View generated entitlements in the **Entitlements** tab.

### Step 3: Submit for approval

When entitlements are ready:

1. Review the **Total Amount** in the Overview tab to verify it is correct.

2. Click **Submit for Approval**.

   ![Submit for approval button](/_images/en-us/programs/cycles/11-submit-for-approval-button-on-cycle-form.png)

3. The cycle state changes to **To Approve**.

### Step 4: Approve the cycle

A user with the **Program Cycle Approver** role (configured during program setup) must approve the cycle.

1. Review the cycle and entitlements.

2. (Optional) Click **Validate Entitlements** to approve individual entitlements before approving the cycle. This requires the **Entitlement Approver** role.

3. Click **Approve Cycle** to approve the entire cycle.

   ![Approve cycle button](/_images/en-us/programs/cycles/12-approve-cycle-button.png)

4. The cycle state changes to **Approved** and is ready for distribution.

### Reject a cycle

If there are problems with the cycle during approval:

1. Click **Reject**.

2. Enter a reason for rejection.

3. The cycle state changes to **Cancelled** and can be reset to Draft if needed.


## Complete a cycle

After benefits are distributed:

1. Click **Mark as Distributed** when payments have been sent to beneficiaries. The cycle state changes to **Distributed**.

2. Click **End Cycle** when all distribution activities are complete and the cycle should be closed.

The cycle becomes read-only after ending and cannot be modified.

## Cancel a cycle

If a cycle should not proceed (before it reaches **To Approve** state):

1. Click **Cancel**.

2. The cycle and all its entitlements are cancelled. The cycle state changes to **Cancelled**.

```{note}
Use **Reject** if the cycle is already submitted for approval. Use **Cancel** if the cycle is still in Draft state.
```


## Are you stuck?

**Cannot find the New Cycle button?**
- Verify you have Program Manager, Validator or admin role assigned to your user account.
- Check that the program is in Active state
- Ensure at least one beneficiary is enrolled

**Copy Beneficiaries does nothing?**
- The program may have no newly enrolled beneficiaries since the cycle was created.
- This function only adds newly enrolled beneficiaries to the cycle. It does not remove beneficiaries who no longer meet the program's eligibility criteria.

**Prepare Entitlements fails?**
- Verify the cycle has beneficiaries (run Copy Beneficiaries first)
- Check that the program has an entitlement manager configured
- Contact your Program Manager if the problem persists

**Cannot approve the cycle?**
- Verify you have the **Program Cycle Approver** role assigned to your account.
- Confirm that a cycle approver role was selected during program configuration.

**Cycle dates show a validation error?**
- Start date cannot be in the past
- End date must be after start date

## Next steps

- {doc}`manage_entitlements` - View and manage individual entitlements
- {doc}`enroll_beneficiaries` - Add more beneficiaries to the program
