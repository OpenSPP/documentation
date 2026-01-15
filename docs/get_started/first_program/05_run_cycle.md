---
openspp:
  doc_status: draft
  products: [registry, programs]
---

# Step 5: Understanding program cycles

This tutorial is for **users** who want to learn how program cycles organize benefit distribution.

## What you'll learn

Understand what program cycles are and how they organize benefit distribution into time periods. You'll learn how to create cycles and view their basic information.

## Before you start

- You completed [Step 4: Import and enroll beneficiaries](04_enroll_beneficiaries.md)
- Your program has eligibility rules configured
- You need **Program Manager** or **System Administrator** access
- Allow 5-10 minutes to complete this step

## The scenario

Your **Cash Transfer for Vulnerable Families** program needs to distribute benefits on a regular schedule. Cycles organize this into manageable periods (for example, monthly distributions).

## Understanding cycles

A **program cycle** represents one period during which benefits are distributed. Think of it as one "round" of your program.

For example:
- **January 2025 cycle**: Distribute benefits for January
- **February 2025 cycle**: Distribute benefits for February

Each cycle has:
- **Start and end dates**: The period covered
- **Status**: Draft → To Approve → Approved → Distributed → Ended
- **Beneficiaries**: Families enrolled in this cycle
- **Entitlements**: Benefits generated for each family

## Steps

### 1. Open the Programs menu

Click **Programs** in the sidebar to view all programs.

![Programs list showing Cash Transfer Program](/_images/en-us/get_started/first_program/05_run_cycle/cle7_1.png)

### 2. View your program

Click on **Cash transfer for vulnerable families** to open your previously created program. You'll see the program Overview tab with a **Recent Cycles** section.

![Program overview showing Recent Cycles section](/_images/en-us/get_started/first_program/05_run_cycle/cle7_2.png)

### 3. Create a new cycle

Click the **New Cycle** button at the top of the program form. This instantly creates a new cycle with:
- Auto-generated name (for example, "Cycle 2")
- Auto-calculated start and end dates
- **Draft** status

![New Cycle button at top of program form](/_images/en-us/get_started/first_program/05_run_cycle/cle7_4.png)

The new cycle appears in the Recent Cycles list:

![New cycle appears in Recent Cycles with Draft status](/_images/en-us/get_started/first_program/05_run_cycle/cle7_3.png)

### 4. Open the cycle details

Click on the cycle name in the Recent Cycles list to open the cycle dialog. You'll see:
- Program name
- Cycle sequence number
- Start and end dates
- Financial summary (total amount, currency)

![Cycle dialog showing Overview tab with cycle details](/_images/en-us/get_started/first_program/05_run_cycle/cle7_5.png)

### 5. View enrolled beneficiaries

Click the **Beneficiaries** tab to see which families are enrolled in this cycle. Each beneficiary shows:
- Registrant name
- Enrollment date
- State (for example, Enrolled)

![Beneficiaries tab showing enrolled registrants](/_images/en-us/get_started/first_program/05_run_cycle/cle7_6.png)

### 6. Understand cycle status progression

Look at the status badges at the top of the cycle dialog. A cycle progresses through these statuses:

1. **Draft**: Cycle is being set up
2. **To Approve**: Cycle is ready for approval
3. **Approved**: Cycle is approved and entitlements can be generated
4. **Distributed**: Benefits have been distributed
5. **Ended**: Cycle is complete

![Status badges showing Draft → To Approve → Approved → Distributed → Ended](/_images/en-us/get_started/first_program/05_run_cycle/cle7_7.png)

### 7. See an approved cycle example

Here's what an approved cycle looks like (from demo data):

![Example of an approved cycle](/_images/en-us/get_started/first_program/05_run_cycle/cle7_8.png)

## What you accomplished

You now understand program cycles:

- **Cycles organize distribution** into time periods
- **New Cycle button** creates cycles instantly with auto-generated names and dates
- **Beneficiaries tab** shows which families are enrolled
- **Status progression** tracks the cycle from Draft to Ended

## What's next

Cycles and entitlements work together:
- **Cycles** define when benefits are distributed
- **Entitlements** define what benefits each family receives

In the next step, you'll learn how to configure benefit amounts and generate entitlements.

## Are you stuck?

**Can't find the New Cycle button?**
Make sure you're viewing the program form (not the programs list). The New Cycle button is at the top of the program form, next to Import Eligible and Enroll Eligible buttons.

**New cycle has weird dates?**
Cycles use auto-calculated dates based on your program schedule. You can edit the cycle dates later if needed by opening the cycle and clicking Edit.

**Don't see any beneficiaries in the Beneficiaries tab?**
This is normal for a new cycle. Beneficiaries are enrolled either:
- Automatically when they meet eligibility criteria
- Manually using the "Copy Beneficiaries" button
- By importing from the registry

**What's the difference between Draft and To Approve?**
- **Draft**: Cycle is still being set up, beneficiaries may still be added
- **To Approve**: Cycle is ready for review and approval by a supervisor

**Can I delete a cycle?**
Yes, you can delete Draft cycles. Once a cycle is Approved or has entitlements generated, it cannot be deleted (to preserve financial records).

## Next step

Continue to [Step 6: Configure and generate entitlements](06_distribute_entitlements.md).
