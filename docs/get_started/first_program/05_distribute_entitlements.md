---
openspp:
  doc_status: draft
  products: [registry, programs]
---

# Step 5: Generate entitlements

This tutorial is for **users** who want to learn how to generate entitlements for distribution.

## What you'll learn

Understand how to configure generate benefit records for distribution.

## Before you start

- You completed [Step 4: Understanding program cycles](04_run_cycle.md)
- Your program has cycles with enrolled beneficiaries
- You need **Program Validator** access
- Allow 5-10 minutes to complete this step

## The scenario

A program has been configured, beneficiaries are enrolled and a cycle has been created. All that is left is now to generate the entitlements.


## Understanding entitlements

An **entitlement** is a record that specifies what benefits a registrant should receive in a cycle. Think of it as a benefit authorization that can be approved and paid.

The flow is:
1. **Configure** - Set benefit amounts in program configuration
2. **Generate** - Create entitlement records for cycle beneficiaries
3. **Review** - Check amounts and beneficiaries
4. **Approve** - Confirm they're ready for distribution

## Steps

### 1. X

Logged in as **Program Validator**, navigate to Programs and open the program **Cash transfer for vulnerable families**.

![Program Configuration tab](/_images/en-us/get_started/first_program/05_distribute_entitlements/01-program-configuration.png)

### 2. X

Click on the name of the cycle to enter it. Click on the tab **Entitlements** and note that they have the status **Pending Approval**

![Program Configuration tab](/_images/en-us/get_started/first_program/05_distribute_entitlements/01-program-configuration.png)

### 3. X

Click **Approve Entitlements**. A message is displayed informing that the entitlements have been approved.

![Program Configuration tab](/_images/en-us/get_started/first_program/05_distribute_entitlements/01-program-configuration.png)

### 4. X

Click on the tab **Entitlements** and note that they have the status **Approved**

![Program Configuration tab](/_images/en-us/get_started/first_program/05_distribute_entitlements/01-program-configuration.png)

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
