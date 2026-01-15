---
openspp:
  doc_status: draft
  products: [payments]
  applies_to:
    - sp_mis
---

# Process Disbursements

**Applies to:** SP-MIS

This guide is for **users** who need to understand and process payment disbursements to beneficiaries.

## What You Will Do

Learn how entitlements become payments and how to approve them for disbursement.

## Before You Start

- You need **Programs Manager** or **Entitlement Validator** access to approve entitlements
- A program cycle must have generated entitlements
- For Point of Sale disbursement, see {doc}`/tutorial/user_guides/point_of_sales`

## How Disbursement Works

Disbursement is the process of getting approved benefits to beneficiaries. In OpenSPP, this follows these stages:

```
Entitlement Created (Draft)
         |
         v
   Pending Validation
         |
         v
      Approved  -----> Disbursed at Service Point
         |
         v
     (or Rejected)
```

## Understanding Entitlement States

Each entitlement moves through several states:

| State | Meaning | What Happens Next |
|-------|---------|-------------------|
| **Draft** | Entitlement just created | Needs to be submitted for validation |
| **Pending Validation** | Waiting for approval | Manager reviews and approves or rejects |
| **Approved** | Ready for payment | Can be disbursed at service points |
| **Rejected** | Not approved for payment | Beneficiary will not receive this payment |
| **Cancelled** | Cancelled before payment | No longer active |

## Steps

### 1. Open Program Entitlements

Navigate to the program cycle to view entitlements.

1. Click **Programs** in the main menu
2. Select the program you want to manage
3. Click on the **Cycles** tab
4. Select the cycle with entitlements to process

![Navigate to program cycle](/_images/en-us/payments/process_disbursements/01-navigate-to-program-cycle-to-view-entitlements.png)

### 2. View Cycle Entitlements

Click **Entitlements** to see all entitlements in this cycle.

![View entitlements button](/_images/en-us/payments/process_disbursements/02-view-entitlements-button-on-cycle-form.png)

The list shows:

| Column | Description |
|--------|-------------|
| **Code** | Unique entitlement identifier |
| **Beneficiary** | Person or group receiving the payment |
| **Initial Amount** | Amount to be paid |
| **Valid From** | Start of payment validity period |
| **Valid Until** | End of payment validity period |
| **State** | Current status (Draft, Pending, Approved, etc.) |

![Entitlements list view](/_images/en-us/payments/process_disbursements/03-entitlements-list-view-showing-beneficiaries-amoun.png)

### 3. Set Entitlements to Pending Validation

Before entitlements can be approved, they must be set to pending validation.

1. From the cycle view, click **Set to Pending Validation**

![Set to pending validation button](/_images/en-us/payments/process_disbursements/04-set-to-pending-validation-button-on-cycle-form.png)

2. Confirm the action when prompted

This changes all draft entitlements to "Pending Validation" status.

```{note}
For cycles with many entitlements, this process runs in the background. You will see a message in the cycle's history when complete.
```

### 4. Approve Entitlements

Once entitlements are pending validation, they can be approved.

**To approve all entitlements in a cycle:**

1. From the cycle view, click **Validate Entitlements**

![Validate entitlements button](/_images/en-us/payments/process_disbursements/05-validate-entitlements-button-to-approve-all-entitl.png)

2. The system checks fund availability
3. Approved entitlements are ready for disbursement

```{important}
Approval requires sufficient program funds. If funds are insufficient, you will see an error message indicating the shortfall.
```

**To approve individual entitlements:**

1. Open the entitlement from the list
2. Click **Approve Entitlement**

![Approve single entitlement](/_images/en-us/payments/process_disbursements/06-approve-single-entitlement-button-on-entitlement-f.png)

### 5. Reject Entitlements (If Needed)

If an entitlement should not be paid, you can reject it.

1. Open the entitlement from the list
2. Click **Reject Entitlement**

![Reject entitlement button](/_images/en-us/payments/process_disbursements/07-reject-entitlement-button-on-entitlement-form.png)

3. Enter a reason for rejection
4. Click **Confirm**

![Reject reason dialog](/_images/en-us/payments/process_disbursements/08-reject-reason-dialog-requiring-explanation-for-rej.png)

**To reject multiple entitlements:**

1. Select entitlements from the list using checkboxes
2. Click **Action** and select **Reject**
3. Enter the rejection reason
4. Confirm

### 6. View Approved Entitlements

Filter the entitlements list to see only approved payments:

1. Click the filter dropdown
2. Select **Approved** under State filter

![Filter approved entitlements](/_images/en-us/payments/process_disbursements/09-filter-approved-entitlements-using-state-filter.png)

Approved entitlements show:
- The approval date
- The payment reference (disbursement ID)
- Transfer fee (if applicable)

### 7. Disburse at Service Points

Once entitlements are approved, payments can be disbursed at service points using the Point of Sale system.

1. Navigate to **Point of Sale**
2. Select the appropriate service point
3. Start a new session
4. Select the beneficiary
5. Process the entitlement payment

For detailed POS instructions, see {doc}`/tutorial/user_guides/point_of_sales`.

![POS disbursement flow](/_images/en-us/payments/process_disbursements/10-point-of-sale-disbursement-flow-for-service-point.png)

## Understanding Payment Status

After approval, you can track whether payments have been disbursed:

| Status | Meaning |
|--------|---------|
| **Approved** | Ready to disburse, not yet paid |
| **Disbursed** | Payment completed at service point |

## Handling Failed Payments

If a payment fails or needs to be corrected:

**Reset to Pending (for rejected entitlements):**

1. Open the rejected entitlement
2. Click **Reset to Pending**
3. The entitlement returns to pending validation status
4. It can then be approved again

![Reset to pending button](/_images/en-us/payments/process_disbursements/11-reset-to-pending-button-to-return-rejected-entitle.png)

**Process Refunds:**

If a payment was made in error at a service point, use the POS refund feature. See the Refunds section in {doc}`/tutorial/user_guides/point_of_sales`.

## Are You Stuck?

**Cannot see the Validate Entitlements button?**
You may not have validator permissions. Contact your administrator to request **Programs Validator** access.

**Approval fails with "insufficient funds" error?**
The program does not have enough allocated funds to cover all entitlements. Contact your program administrator to:
- Add more funds to the program
- Reduce the entitlement amounts
- Cancel some entitlements

**Entitlement stuck in Draft state?**
Run "Set to Pending Validation" from the cycle view first. Entitlements must be pending before they can be approved.

**Cannot reject an entitlement?**
Only entitlements in Draft or Pending Validation state can be rejected. Once approved, entitlements must be processed differently.

**Processing is taking a long time?**
For cycles with many entitlements (200+), processing runs in the background. Check the cycle's message history for completion notifications.

**Beneficiary says they did not receive payment?**
1. Check if the entitlement state is "Approved"
2. Check if it was disbursed in Point of Sale
3. Verify the correct service point was used
4. Review the transaction history in POS

## Next Steps

- {doc}`service_points` - Understand service point locations
- {doc}`/tutorial/user_guides/point_of_sales` - Complete POS disbursement guide
- {doc}`/user_guide/programs/index` - Managing programs and cycles
