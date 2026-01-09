---
openspp:
  doc_status: draft
  products: [registry, programs]
---

# Step 6: Prepare and Distribute Entitlements

This tutorial is for **users** who want to learn how to generate benefit entitlements and prepare them for distribution to beneficiaries.

## What You'll Do

Generate entitlements for eligible families and prepare them for payment. You'll:
- Configure entitlement amounts
- Generate entitlement records
- Review and approve entitlements
- Understand the distribution process

## Before You Start

- You completed [Step 5: Run Cycle](05_run_cycle.md)
- Your January 2025 cycle is approved with 2 eligible families
- You need **Program Manager** or **Administrator** access
- Allow 5-10 minutes to complete this step

## The Scenario

You have 2 eligible families (Santos and Reyes). Now you'll:
1. Set each family to receive 3,000 PHP per month
2. Generate their entitlement records
3. Prepare the entitlements for payment

## Understanding Entitlements

An **entitlement** is a record that says "this family should receive this amount in this cycle." It's like an IOU that gets created after eligibility is confirmed.

The flow is:
1. **Generate** - Create entitlement records
2. **Review** - Check amounts and beneficiaries
3. **Approve** - Confirm they're ready for payment
4. **Distribute** - Pay out (via bank transfer, mobile money, etc.)

## Steps

### 1. Configure the Entitlement Manager

First, you need to tell the program how much each eligible family should receive. Open your **Cash Transfer for Vulnerable Families** program.

![Screenshot: Programs list with program highlighted](/_images/en-us/get_started/first_program/06_distribute_entitlements/01-programs-list-with-program-highlighted.png)

### 2. Go to Entitlement Manager Tab

Click the **Entitlement Manager** tab in the program form.

![Screenshot: Program form with Entitlement Manager tab highlighted](/_images/en-us/get_started/first_program/06_distribute_entitlements/02-program-form-with-entitlement-manager-tab-highligh.png)

### 3. Select Cash Entitlement Type

In the **Manager Type** field, select **Cash** from the dropdown. This indicates you're giving money, not in-kind goods.

![Screenshot: Manager Type dropdown with "Cash" selected](/_images/en-us/get_started/first_program/06_distribute_entitlements/03-manager-type-dropdown-with-cash-selected.png)

### 4. Set the Amount Per Beneficiary

In the **Amount Per Beneficiary** field, enter **3000**. This means each eligible family will receive 3,000 PHP.

![Screenshot: Amount Per Beneficiary field showing "3000"](/_images/en-us/get_started/first_program/06_distribute_entitlements/04-amount-per-beneficiary-field-showing-3000.png)

### 5. Configure Transfer Settings

Below the amount, you'll see transfer configuration options:

| Field | Value |
|-------|-------|
| Transfer Type | Cash |
| Auto-approve Entitlements | Unchecked (you'll approve manually) |

Keep these as default for now. Manual approval lets you review entitlements before they're finalized.

![Screenshot: Transfer settings showing Cash type and auto-approve unchecked](/_images/en-us/get_started/first_program/06_distribute_entitlements/05-transfer-settings-showing-cash-type-and-auto-appro.png)

### 6. Save the Program

Click **Save** to update the program with your entitlement configuration.

![Screenshot: Save button highlighted](/_images/en-us/get_started/first_program/06_distribute_entitlements/06-save-button-highlighted.png)

Success message: "Program updated successfully."

![Screenshot: Success notification](/_images/en-us/get_started/first_program/06_distribute_entitlements/07-success-notification.png)

### 7. Open the January 2025 Cycle

Go to the **Cycles** tab and click on **January 2025** to open the cycle.

![Screenshot: Cycles tab with January 2025 cycle highlighted](/_images/en-us/get_started/first_program/06_distribute_entitlements/08-cycles-tab-with-january-2025-cycle-highlighted.png)

### 8. Generate Entitlements

Now you're ready to create entitlement records. Click the **Prepare Entitlements** button.

![Screenshot: Cycle form with "Prepare Entitlements" button highlighted](/_images/en-us/get_started/first_program/06_distribute_entitlements/09-cycle-form-with-prepare-entitlements-button-highli.png)

The system will generate one entitlement for each eligible beneficiary. You should see a message: "2 entitlements generated."

![Screenshot: Success notification showing "2 entitlements generated"](/_images/en-us/get_started/first_program/06_distribute_entitlements/10-success-notification-showing-2-entitlements-genera.png)

### 9. View Generated Entitlements

Click the **Entitlements** tab in the cycle form to see the generated entitlements.

![Screenshot: Cycle form with Entitlements tab highlighted](/_images/en-us/get_started/first_program/06_distribute_entitlements/11-cycle-form-with-entitlements-tab-highlighted.png)

You should see 2 entitlement records:

| Beneficiary | Amount | Status |
|-------------|--------|--------|
| Santos Family | 3,000 PHP | Draft |
| Reyes Family | 3,000 PHP | Draft |

![Screenshot: Entitlements tab showing two entitlements with Draft status](/_images/en-us/get_started/first_program/06_distribute_entitlements/12-entitlements-tab-showing-two-entitlements-with-dra.png)

### 10. Review an Entitlement

Click on **Santos Family** entitlement to review the details.

![Screenshot: Santos Family entitlement in the list](/_images/en-us/get_started/first_program/06_distribute_entitlements/13-santos-family-entitlement-in-the-list.png)

The entitlement form shows:
- **Partner**: Santos Family (the beneficiary)
- **Cycle**: January 2025
- **Amount**: 3,000 PHP
- **State**: Draft
- **Disbursement Date**: (empty - will be set when distributed)

![Screenshot: Entitlement form showing all details for Santos Family](/_images/en-us/get_started/first_program/06_distribute_entitlements/14-entitlement-form-showing-all-details-for-santos-fa.png)

### 11. Approve Individual Entitlements

To approve this entitlement, click the **Approve** button at the top of the form.

![Screenshot: Entitlement form with "Approve" button highlighted](/_images/en-us/get_started/first_program/06_distribute_entitlements/15-entitlement-form-with-approve-button-highlighted.png)

The status changes from **Draft** to **Approved**.

![Screenshot: Entitlement status badge showing "Approved"](/_images/en-us/get_started/first_program/06_distribute_entitlements/16-entitlement-status-badge-showing-approved.png)

### 12. Approve All Entitlements

Go back to the cycle's Entitlements tab. You can approve entitlements individually (as you just did), or approve all at once.

To approve all remaining entitlements, select them using the checkboxes, then click **Action → Approve Entitlements**.

![Screenshot: Entitlements list with checkboxes selected and Action menu showing "Approve Entitlements"](/_images/en-us/get_started/first_program/06_distribute_entitlements/17-entitlements-list-with-checkboxes-selected-and-act.png)

All entitlements are now **Approved**.

![Screenshot: All entitlements showing Approved status](/_images/en-us/get_started/first_program/06_distribute_entitlements/18-all-entitlements-showing-approved-status.png)

### 13. Validate Entitlements

Before distribution, validate that the entitlements are ready. Click the **Validate Entitlements** button in the cycle.

![Screenshot: Cycle form with "Validate Entitlements" button highlighted](/_images/en-us/get_started/first_program/06_distribute_entitlements/19-cycle-form-with-validate-entitlements-button-highl.png)

The system checks that:
- All amounts are correct
- All beneficiaries are eligible
- All required information is present

You should see: "All entitlements validated successfully."

![Screenshot: Success notification for validation](/_images/en-us/get_started/first_program/06_distribute_entitlements/20-success-notification-for-validation.png)

### 14. View Cycle Summary

Go back to the main cycle form to see the summary:

- **Total Beneficiaries**: 2
- **Total Entitlements**: 2
- **Total Amount**: 6,000 PHP (2 families × 3,000 PHP)
- **Status**: Ready for Distribution

![Screenshot: Cycle summary showing totals and status](/_images/en-us/get_started/first_program/06_distribute_entitlements/21-cycle-summary-showing-totals-and-status.png)

### 15. Understanding Distribution

At this point, your entitlements are approved and ready for payment. The actual distribution (sending money to families) happens through integration with payment systems like:
- Bank transfers
- Mobile money (GCash, PayMaya, etc.)
- Cash distribution at service points

The specific distribution method depends on your OpenSPP configuration and payment integrations. This is typically handled by your finance or disbursement team.

![Screenshot: Distribution options or payment integration screen](/_images/en-us/get_started/first_program/06_distribute_entitlements/22-distribution-options-or-payment-integration-screen.png)

## What You Accomplished

Congratulations! You've successfully completed your first end-to-end program cycle:

✓ **Configured entitlements** - Set 3,000 PHP per family
✓ **Generated 2 entitlements** - One for each eligible family
✓ **Reviewed amounts** - Verified Santos and Reyes families will receive correct amounts
✓ **Approved entitlements** - Confirmed they're ready for payment
✓ **Validated the cycle** - Ensured everything is correct

**Total to distribute**: 6,000 PHP to 2 families

Your program is now ready for the distribution/payment phase!

## Summary of Your Complete Program

Let's recap what you built in this tutorial:

**Program**: Cash Transfer for Vulnerable Families
- **Target**: Groups (families/households)
- **Currency**: PHP

**Eligibility**:
- Household income < 10,000 PHP
- At least 1 child under 5 years old

**Entitlement**:
- 3,000 PHP per family per month

**January 2025 Results**:
- 5 families evaluated
- 2 eligible (Santos, Reyes)
- 6,000 PHP total entitlements

## Are You Stuck?

**Prepare Entitlements button is grayed out?**
Make sure:
- The cycle is approved
- You've configured the Entitlement Manager in the program
- There are eligible beneficiaries in the cycle

**No entitlements generated?**
Check that your cycle has eligible beneficiaries. Go to the Beneficiaries tab and verify at least one family shows as "Eligible."

**Wrong amount generated?**
Go back to the program's Entitlement Manager tab and verify the Amount Per Beneficiary field is set correctly. After changing it, you may need to delete existing entitlements and regenerate them.

**Can't approve entitlements?**
You need approval permissions. Check with your system administrator if you have the **Entitlement Approver** or **Program Manager** role.

**Want to cancel or modify an entitlement?**
If an entitlement is still in Draft status, you can delete it and regenerate. If it's Approved, you may need to use a "Reject" or "Cancel" action depending on your OpenSPP configuration.

**How do I actually pay the beneficiaries?**
The payment/distribution step depends on your payment provider integration. Common methods:
- Export entitlements to Excel and import to bank system
- Use built-in payment integration (if configured)
- Use service point distribution module
- Contact your system administrator for your organization's payment process

**Want to create a second cycle (February 2025)?**
Yes! Just go back to the Cycles tab and create a new cycle with February dates. You can re-run eligibility and generate new entitlements. This is how monthly programs work.

## Next Steps

You've completed the First Program Tutorial! You now know the complete flow:
1. Registry setup
2. Import data
3. Create program
4. Configure eligibility
5. Run cycles
6. Generate entitlements

### What to Learn Next

**For Users**:
- [Enroll Beneficiaries](../../tutorial/user_guides/enroll_beneficiaries.md) - Manual enrollment process
- [Point of Sales Distribution](../../tutorial/user_guides/point_of_sales.md) - In-person benefit distribution
- [Import Registrant Data](../../tutorial/user_guides/import_registrant_data.md) - Advanced import options

**For Implementers** (if you want to create more complex rules):
- Configure advanced eligibility with CEL expressions
- Set up conditional entitlements based on family size
- Create in-kind or basket entitlements

**For Administrators**:
- Set up role-based access control
- Configure payment integrations
- Set up approval workflows

### Tips for Your Real Program

1. **Start small**: Test with a small group before enrolling everyone
2. **Verify data quality**: Clean your registry data before running cycles
3. **Document your rules**: Write down why you chose your eligibility criteria
4. **Train your team**: Make sure everyone understands the cycle process
5. **Monitor and adjust**: Review results and refine eligibility rules as needed

### Need Help?

- Check the [User Guides](../../tutorial/user_guides/index.md) for specific tasks
- Review [Key Concepts](../../learn/concepts/index.md) for deeper understanding
- Contact your system administrator for technical issues
- Join the OpenSPP community for support

**Congratulations on completing your first program!**
