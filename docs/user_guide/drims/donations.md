---
openspp:
  doc_status: draft
  products: [drims]
  applies_to:
    - drims
---

# Receive a Donation

```{admonition} Applies to: DRIMS
:class: tip
This feature is available in OpenSPP deployments with the DRIMS module installed.
```

## What You'll Do

Record and process incoming relief supplies from donors through inspection and add them to your warehouse inventory.

## Before You Start

- You need **Warehouse Staff** or **Warehouse Officer** access
- Know which disaster incident the donation is for
- Have the donor's delivery note or donation letter

## Steps

### 1. Open Donations

Click **DRIMS** in the sidebar, then select **Donations**.

![Donations menu](/_images/en-us/user_guide/drims/donations/1.png)

You'll see a list of all donations for your warehouses.

![Donations list](/_images/en-us/user_guide/drims/donations/2.png)

### 2. Find the Announced Donation

Look for the donation that was announced earlier. Donations waiting to be received show **Announced** in the Status column.

Click on the donation row to open it.

![Open announced donation](/_images/en-us/user_guide/drims/donations/3.png)

You'll see the donation details including:

| Field | What It Means |
|-------|---------------|
| **Incident** | The disaster or emergency this donation supports |
| **Warehouse** | Your warehouse where items will be stored |
| **Donor** | Organization or person donating the items |
| **Source Type** | Type of donor (UN Agency, NGO, Private, Government) |
| **Restriction** | Any limits on how items can be used |

### 3. Mark as Received

When the physical goods arrive at your warehouse, click the **Mark Received** button.

![Mark received button](/_images/en-us/user_guide/drims/donations/4.png)

A form will appear for you to confirm receipt.

![Mark received form](/_images/en-us/user_guide/drims/donations/5.png)

Fill in:

| Field | Instructions |
|-------|--------------|
| **Received Date** | Today's date (or actual arrival date) |
| **Actual Quantities** | Update quantities if different from what was pledged |
| **Notes** | Any observations about the delivery (optional) |

Click **Confirm** to save.

The donation status changes to **Received**.

![Donation received status](/_images/en-us/user_guide/drims/donations/6.png)

### 4. Inspect the Donation

Now check the quality and condition of the items. Click the **Inspect** button.

![Inspect button](/_images/en-us/user_guide/drims/donations/7.png)

A checklist appears for you to record your inspection.

![Inspection form](/_images/en-us/user_guide/drims/donations/8.png)

For each line item, check:

| What to Check | Record |
|---------------|--------|
| **Condition** | Good, Damaged, Expired |
| **Quantity Match** | Does it match what you counted? |
| **Quality** | Meets standards for distribution? |
| **Notes** | Any issues or concerns |

Click **Complete Inspection** when done.

The donation status changes to **Inspected**.

![Donation inspected status](/_images/en-us/user_guide/drims/donations/9.png)

### 5. Stock the Items

If items passed inspection, add them to inventory. Click the **Stock** button.

![Stock button](/_images/en-us/user_guide/drims/donations/10.png)

The system creates a stock receipt and asks you to confirm.

![Stock receipt](/_images/en-us/user_guide/drims/donations/11.png)

Review the items and quantities, then click **Validate**.

![Validate stock](/_images/en-us/user_guide/drims/donations/12.png)

For items that need tracking (like medicines with expiry dates or batch numbers), you'll see a screen to enter:

| Field | What It Means |
|-------|---------------|
| **Lot/Serial Number** | Batch number or unique identifier |
| **Expiry Date** | When the item expires (if applicable) |

Enter the information and click **Confirm**.

![Lot tracking](/_images/en-us/user_guide/drims/donations/13.png)

The donation status changes to **Stocked** and items are now in your inventory.

![Donation stocked status](/_images/en-us/user_guide/drims/donations/14.png)

### 6. Verify Stock Added

To confirm items are in inventory, click **Inventory** in the sidebar, then **Products**.

![Inventory menu](/_images/en-us/user_guide/drims/donations/15.png)

Search for the donated items and check the **On Hand** quantity increased.

![Stock verification](/_images/en-us/user_guide/drims/donations/16.png)

## What If Items Are Damaged?

If items fail inspection and cannot be used:

1. After clicking **Inspect**, mark items as damaged or rejected
2. Instead of **Stock**, click **Reject** button
3. Enter rejection reason and disposal instructions
4. Items will not be added to inventory

The donation status becomes **Rejected** and the incident is closed.

## Are You Stuck?

**Can't find the donation?**

Check the filter at the top. Make sure "My Warehouse" is selected, or change it to "All Warehouses" if the donation is for a different location.

**Mark Received button is grayed out?**

The donation may already be received or cancelled. Check the Status field. If it says anything other than "Announced", someone else already processed it.

**Don't see the Inspect button?**

You may not have Warehouse Officer permissions. Contact your supervisor to get the right access level.

**Stock button doesn't work?**

Make sure you completed the inspection first. You cannot stock items until they've been inspected.

**Item needs a lot number but you don't have it?**

Look on the physical package for batch numbers, manufacturing codes, or expiry dates. If the item truly has no tracking information, check with your supervisor about how to record it.

**Quantities don't match the pledge?**

That's normal. Donors sometimes send more or less than announced. Enter the actual quantity you received in the "Actual Quantities" field during the Mark Received step.

**Need to cancel a donation?**

If goods never arrived or the donation is cancelled, click the **Cancel** button while the donation is in Announced or Received status. Add a cancellation note explaining why.

## Next Steps

- {doc}`manage_inventory` - Learn how to view and manage stock levels
- {doc}`requests` - Learn how to submit relief requests
- {doc}`dispatches` - Learn how to process dispatches
