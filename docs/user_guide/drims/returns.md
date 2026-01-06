---
openspp:
  doc_status: draft
---

# Handle Returns

## What You'll Do

Create and process returns for items sent back from distribution points to the warehouse.

## Before You Start

- You need **Warehouse Officer** or **Administrator** access
- The original dispatch must be recorded in DRIMS
- You should have documentation of why items are being returned

## Why Items Are Returned

Items come back to the warehouse for different reasons. The reason determines what happens to them next.

| Reason | When to Use | What Happens Next |
|--------|-------------|-------------------|
| **Excess** | More items delivered than needed | Usually restocked |
| **Damaged** | Items damaged during transit or storage | Inspected, may be disposed |
| **Expired** | Items past their expiration date | Disposed |
| **Wrong Item** | Incorrect items were sent | Restocked, correct items dispatched |
| **Cancelled** | Distribution was cancelled | Restocked |

## Creating a Return

### 1. Open Returns

Click **Warehouse** in the sidebar, then select **Returns**.

![Screenshot: Returns menu](returns/01_menu.png)

### 2. Create New Return

Click the **New** button in the top left.

![Screenshot: New return button](returns/02_new.png)

### 3. Fill in Return Details

Enter the following information:

| Field | What to Enter |
|-------|---------------|
| **Source Dispatch** | Select the original dispatch this return is for |
| **Warehouse** | The warehouse receiving the returned items (auto-fills from dispatch) |
| **Incident** | The disaster incident (auto-fills from dispatch) |
| **Return Reason** | Why items are being returned (see table above) |
| **Return Date** | When items are expected back |

![Screenshot: Return form header](returns/03_header.png)

### 4. Add Items Being Returned

In the **Items** tab, click **Add a line** for each item type being returned.

For each item, enter:
- **Product:** The item being returned
- **Quantity:** How many units are coming back
- **Notes:** Any details about the item's condition

![Screenshot: Adding return items](returns/04_items.png)

### 5. Save the Return

Click **Save** in the top left.

![Screenshot: Save button](returns/05_save.png)

The return is now in **Draft** status. It won't affect inventory until you confirm it.

## Processing the Return

Returns go through several steps to ensure items are properly tracked and handled.

### Step 1: Confirm the Return

When you've verified the return details, click **Confirm**.

![Screenshot: Confirm button](returns/06_confirm.png)

This authorizes the return and alerts warehouse staff to expect the items.

**Status:** Draft → **Confirmed**

### Step 2: Receive the Items

When the physical items arrive at the warehouse, click **Receive**.

![Screenshot: Receive button](returns/07_receive.png)

You may need to update quantities if the actual returned amount differs from what was expected.

**Status:** Confirmed → **Received**

### Step 3: Inspect the Items

Warehouse staff checks each item's condition. Click **Inspect**.

![Screenshot: Inspect button](returns/08_inspect.png)

For each line item, record:
- **Condition:** Good, Damaged, Expired
- **Inspection Notes:** Details about the item's state

![Screenshot: Inspection details](returns/09_inspection.png)

**Status:** Received → **Inspected**

### Step 4: Restock or Dispose

Based on the inspection, items are either returned to inventory or removed.

#### For Good Items: Click **Restock**

![Screenshot: Restock button](returns/10_restock.png)

This adds the items back to your warehouse inventory. They become available for future dispatches.

**Status:** Inspected → **Restocked**

#### For Damaged/Expired Items: Click **Dispose**

![Screenshot: Dispose button](returns/11_dispose.png)

This removes the items from inventory and records them as disposed.

**Status:** Inspected → **Disposed**

## What Happens to Returned Items

After inspection, the decision tree looks like this:

```
Inspected Items
    │
    ├─→ Good condition → Restock → Back in inventory
    │
    └─→ Damaged/Expired → Dispose → Removed from inventory
```

**Restocked items:**
- Added back to warehouse stock
- Available for allocation to new requests
- Tracked with same lot numbers (if applicable)

**Disposed items:**
- Removed from inventory
- Documented for audit trail
- May require disposal documentation per local regulations

## Are You Stuck?

**Can't find the original dispatch?**

Use the search filter at the top of the Source Dispatch field. Search by dispatch reference number or destination area.

**Return button is greyed out?**

You may not have warehouse permissions. Contact your administrator.

**Quantities don't match what was dispatched?**

This is normal. Only return what actually came back. The system tracks the difference.

**Don't know whether to restock or dispose?**

- **Excess items in good condition:** Restock
- **Items with original packaging intact:** Restock
- **Items past expiry date:** Dispose
- **Items with damaged packaging:** Inspect contents, then decide
- **Items exposed to contamination:** Dispose
- **When in doubt:** Ask your warehouse supervisor

**System says "Stock move already exists"?**

The return may have been partially processed. Check the **Inventory Moves** tab at the bottom of the form to see what's already been recorded.

**Need to cancel a return?**

While the return is in **Draft** status, click **Cancel**. Once confirmed, contact your administrator to reverse the return.
