---
openspp:
  doc_status: draft
---

# Step 5: Run a Program Cycle

This tutorial is for **users** who want to learn how to execute a program cycle and identify eligible beneficiaries.

## What You'll Do

Create and run your first program cycle. The cycle will:
- Evaluate all families in your registry against the eligibility rules
- Identify which families qualify for benefits
- Prepare them for entitlement generation

## Before You Start

- You completed [Step 4: Configure Eligibility](04_configure_eligibility.md)
- Your program has eligibility rules configured
- You need **Program Manager** or **Administrator** access
- Allow 5-10 minutes to complete this step

## The Scenario

A program cycle represents a period during which benefits are distributed. For your monthly Cash Transfer for Vulnerable Families program, each cycle is one month. In this step, you'll create and run your first cycle to identify which families are eligible.

## Understanding Cycles

Think of a cycle as one "round" of your program:
1. **Create the cycle** - Define the time period
2. **Run eligibility check** - Evaluate families against your rules
3. **Review results** - See who qualified
4. **Generate entitlements** - Create benefit records (next step)

## Steps

### 1. Open Your Program

Go to **Programs** and click on **Cash Transfer for Vulnerable Families**.

![Screenshot: Programs list with "Cash Transfer for Vulnerable Families" highlighted](/_images/en-us/get_started/first_program/05_run_cycle/1.png)

### 2. Navigate to the Cycles Tab

Click the **Cycles** tab in the program form. This shows all cycles for this program.

![Screenshot: Program form with Cycles tab highlighted, showing empty cycles list](/_images/en-us/get_started/first_program/05_run_cycle/2.png)

### 3. Create a New Cycle

Click **Add a line** to create a new cycle.

![Screenshot: Cycles tab with "Add a line" button highlighted](/_images/en-us/get_started/first_program/05_run_cycle/3.png)

### 4. Configure the Cycle

A quick create dialog appears. Fill in the following information:

| Field | Value |
|-------|-------|
| Cycle Name | January 2025 |
| Start Date | 2025-01-01 |
| End Date | 2025-01-31 |

These dates define when this benefit period begins and ends.

![Screenshot: Quick create dialog with Cycle Name "January 2025", Start Date "2025-01-01", End Date "2025-01-31"](/_images/en-us/get_started/first_program/05_run_cycle/4.png)

### 5. Save the Cycle

Click **Save & Close** in the dialog to create the cycle.

![Screenshot: Quick create dialog with "Save & Close" button highlighted](/_images/en-us/get_started/first_program/05_run_cycle/5.png)

The cycle now appears in the Cycles tab with status **Draft**.

![Screenshot: Cycles tab showing "January 2025" cycle with Draft status](/_images/en-us/get_started/first_program/05_run_cycle/6.png)

### 6. Open the Cycle

Click on **January 2025** in the cycles list to open the full cycle form.

![Screenshot: January 2025 cycle in list, clickable](/_images/en-us/get_started/first_program/05_run_cycle/7.png)

### 7. Enroll Beneficiaries

Before running the eligibility check, you need to import families into the cycle. Click the **Enroll Beneficiaries** button.

![Screenshot: Cycle form showing "Enroll Beneficiaries" button](/_images/en-us/get_started/first_program/05_run_cycle/8.png)

A dialog appears asking which registrants to import. Select **All Groups** to import all families from your registry.

![Screenshot: Enroll Beneficiaries dialog with "All Groups" radio button selected](/_images/en-us/get_started/first_program/05_run_cycle/9.png)

Click **Enroll** to import the families.

![Screenshot: Enroll button in dialog](/_images/en-us/get_started/first_program/05_run_cycle/10.png)

You should see a success message: "5 beneficiaries enrolled in cycle."

![Screenshot: Success notification showing "5 beneficiaries enrolled in cycle"](/_images/en-us/get_started/first_program/05_run_cycle/11.png)

### 8. View Enrolled Beneficiaries

Click the **Beneficiaries** tab to see all families enrolled in this cycle. You should see your 5 families:
- Garcia Family
- Santos Family
- Cruz Family
- Reyes Family
- Ramos Family

All should have status **Draft** (not evaluated yet).

![Screenshot: Beneficiaries tab showing 5 families listed with Draft status](/_images/en-us/get_started/first_program/05_run_cycle/12.png)

### 9. Run Eligibility Check

Now you're ready to evaluate which families are eligible. Click the **Check Eligibility** button at the top of the cycle form.

![Screenshot: Cycle form with "Check Eligibility" button highlighted](/_images/en-us/get_started/first_program/05_run_cycle/13.png)

The system will process each family against your eligibility rules. This may take a few moments.

![Screenshot: Processing indicator or loading message](/_images/en-us/get_started/first_program/05_run_cycle/14.png)

When complete, you'll see a message: "Eligibility check complete. 2 beneficiaries eligible, 3 ineligible."

![Screenshot: Success notification showing eligibility check results](/_images/en-us/get_started/first_program/05_run_cycle/15.png)

### 10. Review Eligibility Results

Go to the **Beneficiaries** tab again. Notice the status has changed for each family:

**Eligible (2 families)**:
- Santos Family ✓ (income: 8,000, has child born 2021)
- Reyes Family ✓ (income: 6,000, has child born 2023)

**Ineligible (3 families)**:
- Garcia Family ✗ (income too high: 15,000)
- Cruz Family ✗ (income too high: 12,000, no children under 5)
- Ramos Family ✗ (income too high: 18,000, child too old)

![Screenshot: Beneficiaries tab showing families with Eligible/Ineligible status](/_images/en-us/get_started/first_program/05_run_cycle/16.png)

### 11. View Eligibility Details

Click on **Santos Family** to see why they qualified. You should see an eligibility summary showing:
- ✓ Household Income (8,000) is less than 10,000
- ✓ Has 1 child under 5

![Screenshot: Santos Family record showing eligibility criteria met with checkmarks](/_images/en-us/get_started/first_program/05_run_cycle/17.png)

### 12. Approve the Cycle

Now that eligibility is determined, you're ready to approve the cycle. Go back to the cycle form and click **Approve Cycle**.

![Screenshot: Cycle form with "Approve Cycle" button highlighted](/_images/en-us/get_started/first_program/05_run_cycle/18.png)

Confirm the approval when prompted.

![Screenshot: Confirmation dialog asking "Are you sure you want to approve this cycle?"](/_images/en-us/get_started/first_program/05_run_cycle/19.png)

The cycle status changes from **Draft** to **Approved**.

![Screenshot: Cycle status badge showing "Approved"](/_images/en-us/get_started/first_program/05_run_cycle/20.png)

## What You Accomplished

You've successfully completed your first program cycle:

- **Created a cycle** for January 2025
- **Enrolled 5 families** from your registry
- **Ran eligibility check** using your income and children rules
- **Identified 2 eligible families** (Santos and Reyes)
- **Approved the cycle** to move forward

Your program now knows which families should receive benefits. The next step is to generate entitlements (the actual benefit amounts).

## Are You Stuck?

**Can't find the Cycles tab?**
Make sure you're on the program form for "Cash Transfer for Vulnerable Families," not in the programs list view.

**Enroll Beneficiaries button is grayed out?**
The cycle may already be approved or completed. Only Draft cycles can enroll beneficiaries. If you need to change it, use the **Set to Draft** button first.

**Check Eligibility button doesn't work?**
Make sure you've enrolled beneficiaries first. You can't check eligibility on an empty cycle.

**All families showing as Eligible or all as Ineligible?**
Double-check your eligibility rules in the program's Eligibility tab. Make sure:
- Both rules are configured correctly
- Filter Mode is set to "All"
- Field names match your registry data

**Eligibility check takes a very long time?**
For 5 families, it should be nearly instant. If it's slow, there may be a system issue. Check with your administrator or try refreshing the page.

**Don't see eligibility details for a family?**
Click on the family name in the Beneficiaries tab, then look for an "Eligibility" or "Evaluation" section in their record.

**Want to re-run eligibility after changing rules?**
You can! Go back to the program's Eligibility tab, modify the rules, save, then return to the cycle and click **Check Eligibility** again. The system will re-evaluate all families.

## Next Step

Now that you know which families are eligible, you're ready to generate entitlements (benefit amounts). Continue to [Step 6: Distribute Entitlements](06_distribute_entitlements.md).
