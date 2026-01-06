---
openspp:
  doc_status: draft
---

# Receive a Donation

## What You'll Do

Record and process incoming relief supplies from donors through inspection and add them to your warehouse inventory.

## Before You Start

- You need **Warehouse Staff** or **Warehouse Officer** access
- Know which disaster incident the donation is for
- Have the donor's delivery note or donation letter

## Steps

### 1. Open Donations

Click **DRIMS** in the sidebar, then select **Donations**.

![Donations menu](screenshots/drims_donations_menu.png)

You'll see a list of all donations for your warehouses.

![Donations list](screenshots/drims_donations_list.png)

### 2. Find the Announced Donation

Look for the donation that was announced earlier. Donations waiting to be received show **Announced** in the Status column.

Click on the donation row to open it.

![Open announced donation](screenshots/drims_donation_announced.png)

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

![Mark received button](screenshots/drims_donation_mark_received_button.png)

A form will appear for you to confirm receipt.

![Mark received form](screenshots/drims_donation_mark_received_form.png)

Fill in:

| Field | Instructions |
|-------|--------------|
| **Received Date** | Today's date (or actual arrival date) |
| **Actual Quantities** | Update quantities if different from what was pledged |
| **Notes** | Any observations about the delivery (optional) |

Click **Confirm** to save.

The donation status changes to **Received**.

![Donation received status](screenshots/drims_donation_received.png)

### 4. Inspect the Donation

Now check the quality and condition of the items. Click the **Inspect** button.

![Inspect button](screenshots/drims_donation_inspect_button.png)

A checklist appears for you to record your inspection.

![Inspection form](screenshots/drims_donation_inspection_form.png)

For each line item, check:

| What to Check | Record |
|---------------|--------|
| **Condition** | Good, Damaged, Expired |
| **Quantity Match** | Does it match what you counted? |
| **Quality** | Meets standards for distribution? |
| **Notes** | Any issues or concerns |

Click **Complete Inspection** when done.

The donation status changes to **Inspected**.

![Donation inspected status](screenshots/drims_donation_inspected.png)

### 5. Stock the Items

If items passed inspection, add them to inventory. Click the **Stock** button.

![Stock button](screenshots/drims_donation_stock_button.png)

The system creates a stock receipt and asks you to confirm.

![Stock receipt](screenshots/drims_donation_stock_receipt.png)

Review the items and quantities, then click **Validate**.

![Validate stock](screenshots/drims_donation_validate_stock.png)

For items that need tracking (like medicines with expiry dates or batch numbers), you'll see a screen to enter:

| Field | What It Means |
|-------|---------------|
| **Lot/Serial Number** | Batch number or unique identifier |
| **Expiry Date** | When the item expires (if applicable) |

Enter the information and click **Confirm**.

![Lot tracking](screenshots/drims_donation_lot_tracking.png)

The donation status changes to **Stocked** and items are now in your inventory.

![Donation stocked status](screenshots/drims_donation_stocked.png)

### 6. Verify Stock Added

To confirm items are in inventory, click **Inventory** in the sidebar, then **Products**.

![Inventory menu](screenshots/drims_inventory_menu.png)

Search for the donated items and check the **On Hand** quantity increased.

![Stock verification](screenshots/drims_stock_verification.png)

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
