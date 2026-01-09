---
openspp:
  doc_status: draft
  products: [programs]
  applies_to:
    - sp_mis
---

# Work with Program Cycles

**Applies to:** SP-MIS

## What You Will Do

Learn how to navigate, understand, and manage program cycles in OpenSPP.

## Before You Start

- You need **Program Officer**, **Program Manager**, or **Administrator** access
- The program must be in **Active** state
- At least one beneficiary must be enrolled in the program

## What is a Cycle?

A **cycle** represents a distribution period within a program. For example:

- Monthly cash transfers have 12 cycles per year (one per month)
- Quarterly food assistance has 4 cycles per year
- One-time emergency payments have a single cycle

Each cycle:

- Has a start and end date
- Contains beneficiaries copied from the program
- Generates entitlements for each beneficiary
- Goes through an approval workflow before distribution

## Cycle States

Cycles progress through these states:

| State | Meaning | What Happens Next |
|-------|---------|-------------------|
| **Draft** | Cycle is being prepared | Copy beneficiaries, prepare entitlements |
| **To Approve** | Waiting for approval | Validator reviews and approves or rejects |
| **Approved** | Ready for distribution | Prepare and send payments |
| **Distributed** | Benefits have been sent | Mark as ended when complete |
| **Cancelled** | Cycle was rejected or cancelled | Can be reset to draft |
| **Ended** | Cycle is complete | Read-only |

![Cycle states progression](/_images/en-us/programs/cycles/01-cycle-form-showing-state-progression-badge.png)

## View Program Cycles

### Step 1: Open the Program

1. Click **Programs** > **Programs** in the main menu.

2. Click on a program to open it.

### Step 2: View Cycles

There are two ways to view cycles:

**Option A: From the Overview tab**

The **Recent Cycles** section shows the most recent cycles.

![Recent cycles in overview](/_images/en-us/programs/cycles/02-program-overview-tab-showing-recent-cycles-section.png)

**Option B: Using the smart button**

Click the **Cycles** smart button to see all cycles.

![Cycles smart button](/_images/en-us/programs/cycles/03-cycles-smart-button-highlighted-on-program-form.png)

### Step 3: Open a Cycle

Click on a cycle row to open the cycle form.

![Cycle form](/_images/en-us/programs/cycles/04-cycle-form-with-overview-and-status-information.png)

## Understand the Cycle Form

### Overview Tab

| Field | Description |
|-------|-------------|
| **Name** | Cycle name (e.g., "January 2025") |
| **Program** | Parent program |
| **Sequence** | Order of this cycle (1, 2, 3, etc.) |
| **Start Date** | When the cycle begins |
| **End Date** | When the cycle ends |
| **Total Amount** | Sum of all entitlements in this cycle |

![Cycle overview](/_images/en-us/programs/cycles/05-cycle-overview-showing-name-program-dates-and-tota.png)

### Smart Buttons

| Button | Shows |
|--------|-------|
| **Beneficiaries** | Enrolled beneficiaries in this cycle |
| **Entitlements** | Generated entitlements |
| **Payments** | Payment batches (if configured) |

### Beneficiaries Tab

Shows all beneficiaries included in this cycle:

| Column | Description |
|--------|-------------|
| **Registrant** | Beneficiary name |
| **Enrollment Date** | When they were enrolled |
| **State** | Enrolled, Paused, Exited, or Non-compliant |

### Entitlements Tab

Shows all entitlements generated for this cycle:

| Column | Description |
|--------|-------------|
| **Code** | Unique entitlement reference |
| **Registrant** | Beneficiary name |
| **Initial Amount** | Benefit amount |
| **Valid From** | Start of validity period |
| **Valid Until** | End of validity period |
| **State** | Draft, Pending Approval, Approved, etc. |

![Cycle entitlements tab](/_images/en-us/programs/cycles/06-cycle-entitlements-tab-showing-generated-entitleme.png)

## Create a New Cycle

### Step 1: Open the Program

Navigate to the program where you want to create a cycle.

### Step 2: Click New Cycle

Click the **New Cycle** button in the header.

![New cycle button](/_images/en-us/programs/cycles/07-new-cycle-button-in-program-header.png)

### Step 3: Confirm

A notification confirms the new cycle was created.

![Cycle created notification](/_images/en-us/programs/cycles/08-notification-confirming-new-cycle-was-created.png)

### Step 4: Open the Cycle

Click the **Cycles** smart button and select the new cycle.

## Cycle Workflow

### Copy Beneficiaries

When a cycle is first created, it has no beneficiaries. Copy them from the program:

1. Open the cycle (must be in **Draft** state).

2. Click **Copy Beneficiaries**.

   ![Copy beneficiaries button](/_images/en-us/programs/cycles/09-copy-beneficiaries-button-on-cycle-form.png)

3. Beneficiaries are copied from the program enrollment list.

### Prepare Entitlements

After beneficiaries are copied, generate their entitlements:

1. Click **Prepare Entitlements**.

   ![Prepare entitlements button](/_images/en-us/programs/cycles/10-prepare-entitlements-button-on-cycle-form.png)

2. The system calculates benefit amounts based on the program rules.

3. View generated entitlements in the **Entitlements** tab.

### Submit for Approval

When entitlements are ready:

1. Review the **Total Amount** to verify it is correct.

2. Click **Submit for Approval**.

   ![Submit for approval button](/_images/en-us/programs/cycles/11-submit-for-approval-button-on-cycle-form.png)

3. The cycle state changes to **To Approve**.

### Approve the Cycle

A Program Validator or Manager must approve the cycle:

1. Review the cycle and entitlements.

2. Optionally click **Validate Entitlements** to approve individual entitlements.

3. Click **Approve Cycle** to approve the entire cycle.

   ![Approve cycle button](/_images/en-us/programs/cycles/12-approve-cycle-button-for-validators.png)

4. The cycle state changes to **Approved**.

### Reject a Cycle

If there are problems with the cycle:

1. Click **Reject**.

2. Enter a reason for rejection.

3. The cycle state changes to **Cancelled**.

4. The submitter can reset to draft and make corrections.

### Reset to Draft

To make changes to a rejected or pending cycle:

1. Click **Reset to Draft**.

   ![Reset to draft button](/_images/en-us/programs/cycles/13-reset-to-draft-button-for-corrections.png)

2. Make necessary corrections.

3. Submit for approval again.

## Complete a Cycle

After benefits are distributed:

1. Click **Mark as Distributed** when payments are sent.

2. Click **End Cycle** when the cycle is complete.

The cycle becomes read-only after ending.

## Cancel a Cycle

If a cycle should not proceed:

1. Click **Cancel**.

2. The cycle and all its entitlements are cancelled.

3. You can reset to draft if needed, or leave it cancelled.

## Are You Stuck?

**Cannot find the New Cycle button?**
- Verify you have Program Officer or higher access
- Check that the program is in Active state
- Ensure at least one beneficiary is enrolled

**Copy Beneficiaries does nothing?**
- The program may have no enrolled beneficiaries
- Check the program's Beneficiaries tab

**Prepare Entitlements fails?**
- Verify the cycle has beneficiaries (run Copy Beneficiaries first)
- Check that the program has an entitlement manager configured
- Contact your Program Manager if the problem persists

**Cannot approve the cycle?**
- Only Program Validators and Managers can approve cycles
- Entitlements may need to be validated first
- Check if the **Validate Entitlements** button is visible

**Cycle dates show a validation error?**
- Start date cannot be in the past
- End date must be after start date

## Next Steps

- {doc}`manage_entitlements` - View and manage individual entitlements
- {doc}`enroll_beneficiaries` - Add more beneficiaries to the program
