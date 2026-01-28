---
openspp:
  doc_status: draft
  products: [programs]
  applies_to:
    - sp_mis
---

# Enroll Beneficiaries

**Applies to:** SP-MIS

## What You Will Do

Learn how to add registrants to a program and verify their eligibility.

## Before You Start

- You need **Program manager**, **Program validator**, or **Administrator** roles assigned to your user account.
- Registrants must already exist in the Registry

## Understanding Enrollment

Enrollment adds registrants to a program as beneficiaries. There are three ways to enroll:

| Method | Best For | How It Works |
|--------|----------|--------------|
| **Import Eligible** | Large-scale enrollment | System finds all registrants matching eligibility rules |
| **Enroll Eligible** | Verifying and activating | Moves imported registrants from Draft to Enrolled |
| **Individual Enrollment** | Single registrants | Enroll one registrant from their profile |

```{note}
**Large-Scale Operations**: When importing or enrolling 1,000 or more beneficiaries, the system processes these operations in the background to ensure performance. The program will be temporarily locked during processing, and you'll receive notifications when operations start and complete.
```

## Enrollment States

Beneficiaries progress through these states:

| State | Meaning |
|-------|---------|
| **Draft** | Added to program but not yet verified |
| **Enrolled** | Actively enrolled and eligible for benefits |
| **Paused** | Temporarily suspended (still in program) |
| **Exited** | Permanently removed from program |
| **Not Eligible** | Does not meet eligibility criteria |
| **Duplicated** | Flagged as a duplicate record |

## Method 1: Import and Enroll Eligible Registrants

This is the standard workflow for enrolling multiple registrants.

### Step 1: Open the Program

1. Click **Programs** > **Programs** in the main menu.

2. Click on the program where you want to enroll beneficiaries.

### Step 2: Import Eligible Registrants

1. Click the **Import Eligible** button.

   ![Import eligible button](/_images/en-us/programs/enroll/01-import-eligible-button-highlighted-on-program-form.png)

2. Wait for the import to complete. A notification shows how many registrants were found.

   ![Import notification](/_images/en-us/programs/enroll/02-import-notification-showing-registrants-found.png)

   ```{note}
   **Large-Scale Imports**: If importing 1,000 or more beneficiaries, the system processes the import in the background. You'll see a warning notification saying "Started importing X beneficiaries" instead of an immediate success message. The program will be locked during the import process, and you'll receive a notification when the import completes.
   ```

3. The imported registrants appear in the **Beneficiaries** tab with **Draft** status.

   ![Draft beneficiaries](/_images/en-us/programs/enroll/03-beneficiaries-tab.png)

### Step 3: Enroll Eligible Registrants

1. Click the **Enroll Eligible** button.

   ![Enroll eligible button](/_images/en-us/programs/enroll/04-enroll-eligible-button-highlighted.png)

2. The system verifies each registrant against the eligibility rules.

3. A notification shows the enrollment results:

   - **Small batches** (< 1,000 beneficiaries): Immediate success notification showing "Enrolled Beneficiaries: X successfully and Y unsuccessfully"
   - **Large batches** (≥ 1,000 beneficiaries): Warning notification saying "Eligibility check of X beneficiaries started" - the process runs in the background

   ![Enrollment notification](/_images/en-us/programs/enroll/05-enrollment-notification.png)

   ```{important}
   **Background Processing**: For large-scale enrollment (1,000+ beneficiaries), the program will be locked during processing. You'll see a lock indicator and the reason "Eligibility check of beneficiaries". Wait for the process to complete - you'll receive a notification when finished.
   ```

4. Successfully enrolled registrants now show **Enrolled** status.

   ![Enrolled beneficiaries](/_images/en-us/programs/enroll/06-beneficiaries-tab-showing-enrolled-status.png)

### Step 4: Review Results

Check the **Beneficiaries** tab to see:

- **Enrolled** - Successfully enrolled and eligible
- **Not Eligible** - Did not meet eligibility criteria
- **Duplicated** - Flagged as potential duplicate

## Method 2: Enroll Individual Registrant

Enroll a single registrant directly from their profile.

### Step 1: Open the Registrant

1. Go to **Registry** and find the registrant you want to enroll.

2. Open their profile.

### Step 2: Click Enroll in Program

1. In the **Participation** section, click **Enroll in Program**.

   ![Enroll in program button](/_images/en-us/programs/enroll/07-enroll-in-program-button-on-registrant.png)

2. A wizard opens.

### Step 3: Select the Program

1. Select the program from the dropdown.

   ![Program selection](/_images/en-us/programs/enroll/08-program-selection-wizard-for-individual-enrollment.png)

   Only programs matching the registrant type (individual or group) are shown.

2. Click **Enroll**.

### Step 4: Verify Enrollment

1. A notification confirms the enrollment.

   ![Enrollment confirmation](/_images/en-us/programs/enroll/09-individual-enrollment-confirmation-notification.png)

2. The enrollment appears in the registrant's **Program Enrollments** section.

## Verify Eligibility

Re-check eligibility for beneficiaries who are currently **Enrolled** or **Not Eligible** (useful when registry data changes or eligibility rules are updated):

1. Open the program.

2. Click **Verify Eligibility**.

   ![Verify eligibility button](/_images/en-us/programs/enroll/10-verify-eligibility-button-highlighted.png)

3. The system re-evaluates beneficiaries in **Enrolled** and **Not Eligible** states against the current eligibility rules.

4. Beneficiaries who no longer qualify are marked as **Not Eligible**. Beneficiaries who now qualify (previously marked as Not Eligible) are moved to **Enrolled** status.

   ```{note}
   **Large-Scale Verification**: If verifying 1,000 or more beneficiaries, the process runs in the background. The program will be locked during verification, and you'll receive a notification when complete.
   ```

## View Beneficiary Details

### From the Program

1. Open the program.

2. Click the **Beneficiaries** tab or the **Beneficiaries** smart button.

3. Click on a beneficiary row to see their details.

   ![Beneficiaries view](/_images/en-us/programs/enroll/11-beneficiaries-view-from-smart-button-or-tab.png)

### Beneficiary Information

| Field | Description |
|-------|-------------|
| **Registrant** | Link to the registrant's profile |
| **Program** | The program they are enrolled in |
| **State** | Current enrollment status |
| **Enrollment Date** | When they were enrolled |
| **Exit Date** | When they exited (if applicable) |

   ![Beneficiaries view](/_images/en-us/programs/enroll/16-beneficiary-details.png)

## Manage Beneficiary Status

### Pause a Beneficiary

Temporarily suspend a beneficiary without removing them:

1. Open the beneficiary record.

2. Click **Pause**.

   ![Pause button](/_images/en-us/programs/enroll/12-pause-button-on-beneficiary-record.png)

3. The status changes to **Paused**. They will not receive benefits until resumed.

### Resume a Beneficiary

Reactivate a paused beneficiary:

1. Open the beneficiary record.

2. Click **Resume**.

3. The status changes back to **Enrolled**.

### Exit a Beneficiary

Permanently remove a beneficiary from the program:

1. Open the beneficiary record.

2. Click **Exit**.

   ![Exit button](/_images/en-us/programs/enroll/13-exit-button-on-beneficiary-record.png)

3. The status changes to **Exited** and the exit date is recorded.

4. Exited beneficiaries cannot be resumed. To re-enroll, create a new enrollment.

## Deduplicate Beneficiaries

Find and flag potential duplicate enrollments:

1. Open the program.

2. Click **Deduplicate**.

   ![Deduplicate button](/_images/en-us/programs/enroll/14-deduplicate-button-on-program-form.png)

3. The system checks for duplicates based on configured rules.

4. A notification shows how many duplicates were found.

5. View duplicates using the **Duplicates** smart button.

   ![Duplicates button](/_images/en-us/programs/enroll/15-duplicates-smart-button-for-viewing-duplicate.png)

## Are You Stuck?

**Import Eligible button does nothing?**
- The program may not have an eligibility manager configured
- Contact your Program Manager to verify the configuration

**No registrants found during import?**
- Check that registrants exist in the Registry
- Verify the program's target type matches (individual vs. group)
- Review the eligibility criteria with your Program Manager

**Program is locked and I can't make changes?**
- The program is currently processing a large-scale import or enrollment operation
- Wait for the background process to complete - you'll see a notification when finished
- Check the program's chatter/messages for status updates
- The lock will automatically release when the operation completes

**Registrant shows "Not Eligible" after enrollment?**
- The registrant's data may not meet the eligibility criteria
- Open their profile and verify their information is complete
- Check with your Program Manager about the specific eligibility rules

**Cannot pause or exit a beneficiary?**
- You may not have the required permissions
- The beneficiary may already be in the state you are trying to set

**"Already enrolled in this program" error?**
- A registrant can only be enrolled once per program
- Check the program's beneficiary list for existing enrollment
- If they were exited, you may need to create a new enrollment

**Individual enrollment shows no programs?**
- Check that active programs exist for the registrant's type
- Individual registrants can only enroll in individual-targeted programs
- Group registrants can only enroll in group-targeted programs

## Next Steps

- {doc}`program_cycles` - Create cycles to distribute benefits
- {doc}`manage_entitlements` - View entitlements for enrolled beneficiaries
