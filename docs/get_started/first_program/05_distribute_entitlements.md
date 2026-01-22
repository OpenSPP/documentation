---
openspp:
  doc_status: draft
  products: [registry, programs]
---

# Step 5: Configure and generate entitlements

This tutorial is for **users** who want to learn how to configure benefit amounts and generate entitlements for distribution.

## What you'll learn

Understand how to configure entitlement amounts and generate benefit records. You'll learn where to set benefit amounts and how to prepare entitlements for distribution.

## Before you start

- You completed [Step 4: Understanding program cycles](04_run_cycle.md)
- Your program has cycles with enrolled beneficiaries
- You need **Program Manager** or **System Administrator** access
- Allow 5-10 minutes to complete this step

## The scenario

Your **Cash Transfer for Vulnerable Families** program needs to distribute benefits to enrolled families. You'll configure how much each family receives and generate their entitlement records.

## Understanding entitlements

An **entitlement** is a record that specifies what benefits a registrant should receive in a cycle. Think of it as a benefit authorization that can be approved and paid.

The flow is:
1. **Configure** - Set benefit amounts in program configuration
2. **Generate** - Create entitlement records for cycle beneficiaries
3. **Review** - Check amounts and beneficiaries
4. **Approve** - Confirm they're ready for distribution

## Steps

### 1. Open the program Configuration tab

Navigate to Programs and open **Cash Transfer Program** (or your program name). Click the **Configuration** tab.

![Program Configuration tab](/_images/en-us/get_started/first_program/05_distribute_entitlements/01-program-configuration.png)

### 2. Find the "What Benefits?" section

Scroll down to the **What Benefits?** section. This section shows your program's **Entitlement Type** - in this case, **Default**.

![What Benefits section with Entitlement Type](/_images/en-us/get_started/first_program/05_distribute_entitlements/02-what-benefits-section.png)

### 3. Open entitlement configuration

Click the **gear icon** (⚙️) next to **Default** to configure the entitlement amounts.

![Gear icon next to Default entitlement type](/_images/en-us/get_started/first_program/05_distribute_entitlements/03-entitlement-config-gear.png)

### 4. Set the benefit amount

A dialog opens showing **BENEFIT AMOUNTS**. The **Amount per Cycle** field shows how much each beneficiary receives. In the demo data, this is set to **$150.00**.

![Entitlement configuration dialog showing Amount per Cycle](/_images/en-us/get_started/first_program/05_distribute_entitlements/04-entitlement-amount-dialog.png)

You can also configure:
- **Amount per Person (in group)** - Additional amount per family member
- **Transfer fees** - Percentage or fixed fees
- **Approval settings** - Validation groups

Click **Discard** to close the dialog (we're just viewing the configuration).

### 5. Open a cycle to prepare entitlements

Go back to the **Overview** tab and open an approved cycle from the Recent Cycles list. The cycle dialog shows a **Prepare Entitlements** button.

![Cycle dialog with Prepare Entitlements button](/_images/en-us/get_started/first_program/05_distribute_entitlements/05-cycle-prepare-entitlements.png)

Clicking this button generates one entitlement for each enrolled beneficiary, using the amount configured in the entitlement type.

### 6. View generated entitlements

Click the **Entitlements** tab to see the generated entitlements. Each row shows:
- **Code** - Entitlement reference number
- **Registrant** - Beneficiary name
- **Initial Amount** - Benefit amount
- **Valid From/Until** - Period dates
- **Status** - Draft, Approved, etc.

![Entitlements tab showing generated entitlements](/_images/en-us/get_started/first_program/05_distribute_entitlements/06-entitlements-tab.png)

### 7. Review individual entitlement

Click on an entitlement to open the form and review the details:
- Registrant information
- Cycle reference
- Amount and currency
- Valid period
- Status

![Individual entitlement form](/_images/en-us/get_started/first_program/05_distribute_entitlements/07-entitlement-form.png)

From this form, you can approve the entitlement by clicking the **Approve** button (if you have approval permissions).

### 8. View approved entitlements

After approval, entitlements show **Approved** status in the list. Approved entitlements are ready for the distribution/payment phase.

![Entitlements list with approved status](/_images/en-us/get_started/first_program/05_distribute_entitlements/08-entitlements-approved.png)

## What you accomplished

You now understand entitlement configuration:

- **Configuration tab** contains entitlement type settings
- **Gear icon** opens configuration dialog
- **Amount per Cycle** sets the benefit amount
- **Prepare Entitlements** generates records for beneficiaries
- **Status** tracks entitlement approval

## What's next

Entitlements and payments work together:
- **Entitlements** define what benefits each registrant receives
- **Payments** execute the actual distribution (bank transfer, mobile money, etc.)

The payment/distribution phase depends on your OpenSPP configuration and payment provider integrations. This is typically handled by your finance or disbursement team.

## Are you stuck?

**Can't find the Configuration tab?**
Make sure you're viewing the program form (not the programs list). Click on your program name to open it, then look for the Configuration tab at the top.

**Don't see the "What Benefits?" section?**
Scroll down in the Configuration tab. It may be below other configuration sections like "Who?" and "How?".

**Prepare Entitlements button is grayed out?**
Make sure:
- The cycle status is **Approved**
- You've configured the entitlement type (Amount per Cycle should not be $0)
- There are enrolled beneficiaries in the cycle (check Beneficiaries tab)

**No entitlements generated after clicking Prepare Entitlements?**
Check the cycle's Beneficiaries tab. If no beneficiaries are enrolled, no entitlements will be created. You may need to enroll beneficiaries first using the **Copy Beneficiaries** button or by importing eligible registrants.

**Wrong amount in generated entitlements?**
Go back to Configuration tab → "What Benefits?" → gear icon and verify the **Amount per Cycle** field. If you change it, you may need to delete existing entitlements and regenerate them.

**Can't approve entitlements?**
You need approval permissions. Check with your system administrator if you have the **Entitlement Approver** or **Program Manager** role.

**How do I actually pay the beneficiaries?**
The payment step depends on your OpenSPP payment integration:
- Bank transfers (export entitlements to Excel and import to bank system)
- Mobile money integration (GCash, M-Pesa, etc.)
- Service point distribution
- Contact your system administrator for your organization's payment process

## Next steps

Congratulations! You've completed the First Program tutorial series. You now understand:
1. Registry setup
2. Data import
3. Program creation
4. Eligibility configuration
5. Cycle management
6. Entitlement generation

### What to learn next

**For users**:
- Manual beneficiary enrollment
- Point of service distribution
- Advanced data import options

**For implementers**:
- Configure advanced eligibility rules
- Set up conditional entitlements
- Create in-kind or basket entitlements

**For administrators**:
- Role-based access control
- Payment integrations
- Approval workflows
