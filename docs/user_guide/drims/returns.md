---
openspp:
  doc_status: draft
  products: [drims]
  applies_to:
    - drims
---

# Handle Returns

```{admonition} Applies to: DRIMS
:class: tip
This feature is available in OpenSPP deployments with the DRIMS module installed.
```

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

<!-- TODO: Add screenshot: Returns menu -->
<!-- ![Screenshot: Returns menu](/_images/en-us/drims/returns/01_menu.png) -->

### 2. Create New Return

Click the **New** button in the top left.

<!-- TODO: Add screenshot: New return button -->
<!-- ![Screenshot: New return button](/_images/en-us/drims/returns/02_new.png) -->

### 3. Fill in Return Details

Enter the following information:

| Field | What to Enter |
|-------|---------------|
| **Source Dispatch** | Select the original dispatch this return is for |
| **Warehouse** | The warehouse receiving the returned items (auto-fills from dispatch) |
| **Incident** | The disaster incident (auto-fills from dispatch) |
| **Return Reason** | Why items are being returned (see table above) |
| **Return Date** | When items are expected back |

<!-- TODO: Add screenshot: Return form header -->
<!-- ![Screenshot: Return form header](/_images/en-us/drims/returns/03_header.png) -->

### 4. Add Items Being Returned

In the **Items** tab, click **Add a line** for each item type being returned.

For each item, enter:
- **Product:** The item being returned
- **Quantity:** How many units are coming back
- **Notes:** Any details about the item's condition

<!-- TODO: Add screenshot: Adding return items -->
<!-- ![Screenshot: Adding return items](/_images/en-us/drims/returns/04_items.png) -->

### 5. Save the Return

Click **Save** in the top left.

<!-- TODO: Add screenshot: Save button -->
<!-- ![Screenshot: Save button](/_images/en-us/drims/returns/05_save.png) -->

The return is now in **Draft** status. It won't affect inventory until you confirm it.

## Processing the Return

Returns go through several steps to ensure items are properly tracked and handled.

### Step 1: Confirm the Return

When you've verified the return details, click **Confirm**.

<!-- TODO: Add screenshot: Confirm button -->
<!-- ![Screenshot: Confirm button](/_images/en-us/drims/returns/06_confirm.png) -->

This authorizes the return and alerts warehouse staff to expect the items.

**Status:** Draft → **Confirmed**

### Step 2: Receive the Items

When the physical items arrive at the warehouse, click **Receive**.

<!-- TODO: Add screenshot: Receive button -->
<!-- ![Screenshot: Receive button](/_images/en-us/drims/returns/07_receive.png) -->

You may need to update quantities if the actual returned amount differs from what was expected.

**Status:** Confirmed → **Received**

### Step 3: Inspect the Items

Warehouse staff checks each item's condition. Click **Inspect**.

<!-- TODO: Add screenshot: Inspect button -->
<!-- ![Screenshot: Inspect button](/_images/en-us/drims/returns/08_inspect.png) -->

For each line item, record:
- **Condition:** Good, Damaged, Expired
- **Inspection Notes:** Details about the item's state

<!-- TODO: Add screenshot: Inspection details -->
<!-- ![Screenshot: Inspection details](/_images/en-us/drims/returns/09_inspection.png) -->

**Status:** Received → **Inspected**

### Step 4: Restock or Dispose

Based on the inspection, items are either returned to inventory or removed.

#### For Good Items: Click **Restock**

<!-- TODO: Add screenshot: Restock button -->
<!-- ![Screenshot: Restock button](/_images/en-us/drims/returns/10_restock.png) -->

This adds the items back to your warehouse inventory. They become available for future dispatches.

**Status:** Inspected → **Restocked**

#### For Damaged/Expired Items: Click **Dispose**

<!-- TODO: Add screenshot: Dispose button -->
<!-- ![Screenshot: Dispose button](/_images/en-us/drims/returns/11_dispose.png) -->

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

## Next Steps

- {doc}`manage_inventory` - Learn how to check updated stock levels
- {doc}`dashboard` - Monitor warehouse health and alerts
- {doc}`donations` - Learn how to receive new donations
