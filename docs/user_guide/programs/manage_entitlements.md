---
openspp:
  doc_status: draft
  products: [programs]
  applies_to:
    - sp_mis
---

# Manage Entitlements

**Applies to:** SP-MIS

## What You Will Do

Learn how to view, understand, and manage entitlements in OpenSPP.

## Before You Start

- You need **Program Validator**, **Program Manager**, or **Administrator** access to approve entitlements
- **Program Officer** access allows viewing but not approving

## What is an Entitlement?

An **entitlement** represents the benefit a beneficiary will receive for a specific cycle. Each entitlement includes:

- The beneficiary receiving the benefit
- The amount or items they will receive
- The validity period
- The current approval status

There are two types of entitlements:

| Type | Description |
|------|-------------|
| **Cash entitlement** | Monetary benefit with an amount and currency |
| **In-kind entitlement** | Physical items with quantity and product details |

## Entitlement States

Entitlements progress through these states:

| State | Meaning | Who Can Change |
|-------|---------|----------------|
| **Draft** | Not yet submitted | Program Officer |
| **Pending Approval** | Waiting for validation | Program Validator |
| **Approved** | Ready for distribution | - |
| **Transferred to FSP** | Sent to payment provider | - |
| **Redeemed/Paid** | Beneficiary received benefit | - |
| **Rejected** | Declined (with reason) | - |
| **Cancelled** | Voided | Program Manager |
| **Expired** | Validity period ended | Automatic |

## View Entitlements

### From a Cycle

1. Open the program and click the **Cycles** smart button.

2. Select a cycle.

3. Click the **Entitlements** tab or the **Entitlements** smart button.

   ![Cycle entitlements](/_images/en-us/programs/entitlements/01-cycle-entitlements-view-showing-entitlements-tab.png)

### From the In-Kind Menu

For in-kind entitlements:

1. Click **Programs** > **In-Kind** > **Entitlements**.

   ![In-kind menu](/_images/en-us/programs/entitlements/02-in-kind-menu-under-programs.png)

2. The entitlements list shows all in-kind entitlements.

   ![In-kind list](/_images/en-us/programs/entitlements/03-in-kind-entitlements-list-view.png)

## Understand Entitlement Information

### Cash Entitlement Fields

| Field | Description |
|-------|-------------|
| **Code** | Unique reference number |
| **ERN** | Entitlement Reference Number (generated on approval) |
| **Registrant** | Beneficiary name |
| **Program** | Parent program |
| **Cycle** | Distribution cycle |
| **Initial Amount** | Benefit amount |
| **Currency** | Payment currency |
| **Valid From** | Start of validity |
| **Valid Until** | End of validity |
| **State** | Current status |

![Cash entitlement form](/_images/en-us/programs/entitlements/04-cash-entitlement-form-with-amount-and-details.png)

### In-Kind Entitlement Fields

| Field | Description |
|-------|-------------|
| **Code** | Unique reference number |
| **Registrant** | Beneficiary name |
| **Product** | Item being distributed |
| **Quantity** | Number of items |
| **Unit of Measure** | Units (kg, pieces, etc.) |
| **Service Point** | Distribution location |
| **Valid From** | Start of validity |
| **Valid Until** | End of validity |
| **State** | Current status |

![In-kind entitlement form](/_images/en-us/programs/entitlements/05-in-kind-entitlement-form-with-product-and-quantity.png)

## Filter and Search Entitlements

### Use Filters

From the entitlements list, use filters to find specific entitlements:

| Filter | Shows |
|--------|-------|
| **Draft** | Entitlements not yet submitted |
| **Pending Validation** | Awaiting approval |
| **Approved** | Ready for distribution |
| **Cancelled** | Voided entitlements |
| **Expired** | Past validity date |

![Entitlement filters](/_images/en-us/programs/entitlements/06-entitlement-filters-for-state-filtering.png)

### Search by Beneficiary

Type a beneficiary name or ID in the search bar to find their entitlements.

### Group Results

Group entitlements by:

- **State** - See counts per status
- **Valid From** - Group by date
- **Company** - For multi-company setups

## Approve Entitlements

### Approve from a Cycle

To approve all entitlements in a cycle at once:

1. Open the cycle (must be in **To Approve** state).

2. Click **Validate Entitlements**.

   ![Validate entitlements button](/_images/en-us/programs/entitlements/07-validate-entitlements-button-on-cycle-form.png)

3. All pending entitlements in the cycle are approved.

4. Click **Approve Cycle** to complete the approval process.

### Approve Individual Entitlements

To approve a single entitlement:

1. Open the entitlement.

2. Click **Approve Entitlement**.

   ![Approve entitlement button](/_images/en-us/programs/entitlements/08-approve-entitlement-button-on-individual-entitleme.png)

3. The entitlement state changes to **Approved**.

### Batch Approve

To approve multiple entitlements at once:

1. From the entitlements list, select the entitlements to approve (use checkboxes).

2. Click **Action** > **Approve**.

   ![Batch approve](/_images/en-us/programs/entitlements/09-batch-approve-with-action-menu-and-selected-entitl.png)

3. Confirm the approval.

## Reject Entitlements

If an entitlement should not be paid:

1. Open the entitlement.

2. Click **Reject**.

3. Select a rejection reason:

   | Reason | When to Use |
   |--------|-------------|
   | Beneficiary did not want it | Beneficiary declined |
   | Account does not exist | Payment account is invalid |
   | Other reason | Any other issue |

4. The entitlement state changes to **Rejected**.

## Reset to Draft

If corrections are needed on a pending or rejected entitlement:

1. Open the entitlement.

2. Click **Reset to Draft** (if available).

3. Make corrections.

4. Submit for approval again.

{note}
Approved entitlements cannot be reset to draft. Contact a Program Manager if an approved entitlement needs to be cancelled.

## View Entitlement History

For each entitlement, you can track:

- When it was created
- Who submitted it for approval
- Who approved or rejected it
- Approval comments

This information is visible in the **Approval** tab (for cycles) or the form chatter.

![Entitlement history](/_images/en-us/programs/entitlements/10-entitlement-history-in-chatter-or-approval-tab.png)

## Check Payment Status

After entitlements are approved:

| Status | Meaning |
|--------|---------|
| **Not Paid** | Payment not yet processed |
| **Paid** | Beneficiary received payment |

The payment date shows when the payment was completed.

![Payment status](/_images/en-us/programs/entitlements/11-payment-status-on-approved-entitlement.png)

## Are You Stuck?

**Cannot see the Approve button?**
- Only Program Validators and Managers can approve entitlements
- The entitlement must be in Pending Approval state
- Contact your administrator if you need approval permissions

**Entitlement shows wrong amount?**
- Amounts are calculated by the entitlement manager
- Contact your Program Manager to verify the calculation rules
- For draft entitlements, the cycle may need to regenerate entitlements

**Entitlement is expired but should be valid?**
- Check the Valid Until date
- Expired entitlements cannot be reactivated
- A new entitlement must be created in the next cycle

**Cannot find an entitlement?**
- Check all states (including Cancelled and Expired)
- Search by beneficiary name or entitlement code
- Verify you are looking in the correct cycle

**Reject button is not visible?**
- The entitlement may already be approved or cancelled
- Only pending entitlements can be rejected

**Batch approve fails for some entitlements?**
- The error message shows which entitlements failed and why
- Usually caused by entitlements not in Pending Approval state
- Review and retry the individual entitlements

## Next Steps

- {doc}`program_cycles` - Learn about cycle workflows
- {doc}`enroll_beneficiaries` - Add more beneficiaries
- {doc}`/user_guide/payments/index` - Process payments for approved entitlements
