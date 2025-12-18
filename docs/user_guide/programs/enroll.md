---
openspp:
  doc_status: draft
---

# Enroll Beneficiaries

This guide is for **users** who need to enroll registrants into social protection programs.

## What You'll Learn

By the end of this guide, you will be able to:
- Import eligible registrants into a program
- Enroll beneficiaries in a program
- Verify enrollment status

## Prerequisites

- An existing program configured in OpenSPP
- Registrants in the system who match the program's eligibility criteria
- **Program Manager** or **Administrator** access

## Understanding Enrollment

Enrollment is a two-step process:

| Step | What Happens |
|------|--------------|
| **Import** | Finds registrants matching eligibility criteria and adds them as potential beneficiaries |
| **Enroll** | Confirms beneficiaries and authorizes them to receive benefits |

## Option 1: Automatic Enrollment During Program Setup

If you selected **Yes** to "Import and enroll beneficiaries" during program creation, enrollment happens automatically.

### Verify Automatic Enrollment

1. Navigate to your program
2. Check the **Beneficiaries** icon - it shows the count of enrolled beneficiaries

![Beneficiaries count](tutorial/user_guides/enroll_beneficiaries/2.png)

3. Click **Beneficiaries** to view the list
4. Verify the **Status** column shows "Enrolled"

![Enrolled beneficiaries](tutorial/user_guides/enroll_beneficiaries/3.png)

## Option 2: Manual Enrollment After Program Creation

If you selected **No** during program creation, follow these steps.

### Step 1: Import Eligible Registrants

1. Open your program
2. Click **Import Eligible Registrants**

![Import button](tutorial/user_guides/enroll_beneficiaries/4.png)

3. Wait for the import to complete:
   - **Under 1,000 beneficiaries**: Green popup confirms completion
   - **Over 1,000 beneficiaries**: Yellow notification appears - refresh the page until it disappears

![Import notification](tutorial/user_guides/enroll_beneficiaries/5.png)

```{important}
Do not proceed to enrollment until the import is complete. For large imports, this may take several minutes.
```

### Step 2: Enroll Beneficiaries

1. Once import is complete, click **Enroll Eligible Registrants**

![Enroll button](tutorial/user_guides/enroll_beneficiaries/6.png)

2. A notification appears indicating enrollment is in progress
3. Refresh the page until the notification disappears

### Step 3: Verify Enrollment

1. Check the **Beneficiaries** icon shows the expected count

![Final count](tutorial/user_guides/enroll_beneficiaries/7.png)

2. Click **Beneficiaries** to view the enrolled list
3. Verify the **Status** column shows "Enrolled"

![Enrolled list](tutorial/user_guides/enroll_beneficiaries/8.png)

## Enrollment Summary

| Scenario | Import Step | Enroll Step |
|----------|-------------|-------------|
| Automatic (Yes during setup) | Automatic | Automatic |
| Manual (No during setup) | Click "Import Eligible Registrants" | Click "Enroll Eligible Registrants" |

## Are You Stuck?

**No beneficiaries imported?**
- Check eligibility criteria - they may be too restrictive
- Verify registrants exist that match the criteria
- Check the program's target type (individuals vs groups)

**Import seems to hang?**
- Large imports take time - be patient
- Refresh the page to check status
- For very large imports (10,000+), consider importing in batches

**Beneficiaries show "Imported" but not "Enrolled"?**
- You need to click "Enroll Eligible Registrants" after importing
- Wait for import to fully complete before enrolling

**Wrong beneficiaries enrolled?**
- Review your eligibility criteria
- Check if the correct program is selected
- Beneficiaries can be manually removed if needed

## Next Steps

- {doc}`/user_guide/entitlements/index` - Create entitlements for enrolled beneficiaries
- {doc}`/tutorial/user_guides/create_program_cycle_prepare_entitlements` - Create program cycles
