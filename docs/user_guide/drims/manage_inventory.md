---
openspp:
  doc_status: draft
  products: [drims]
  applies_to:
    - drims
---

# Manage Inventory

```{admonition} Applies to: DRIMS
:class: tip
This feature is available in OpenSPP deployments with the DRIMS module installed.
```

This guide is for **warehouse staff** and **managers** who need to monitor and manage stock levels in DRIMS warehouses.

## What You'll Do

Learn how to view and manage relief supply inventory across your warehouses:

- View current stock levels and quantities on hand
- Understand stock status (available, reserved, expired)
- Find items by product, warehouse, or lot number
- Check expiry dates and lot tracking information
- Review stock movements and history

## Before You Start

- You need **DRIMS Warehouse Staff** or **Manager** access to view inventory
- You need **Warehouse Officer** or higher to make stock adjustments

## View Current Stock Levels

### 1. Open the Inventory View

Click **DRIMS** in the sidebar, then select **Inventory** and **Stock**.

<!-- TODO: Add screenshot: Navigate to inventory -->
<!-- ![Screenshot: Navigate to inventory](/_images/en-us/drims/manage_inventory/navigate_inventory.png) -->

### 2. Understand the Stock List

The stock list shows all items currently in your warehouses:

<!-- TODO: Add screenshot: Stock list overview -->
<!-- ![Screenshot: Stock list overview](/_images/en-us/drims/manage_inventory/stock_list.png) -->

| Column | What It Shows |
|--------|---------------|
| **Product** | Name of the relief item |
| **Warehouse** | Which warehouse holds the stock |
| **Location** | Specific storage location within the warehouse |
| **On Hand** | Total quantity physically in the warehouse |
| **Reserved** | Quantity set aside for approved requests |
| **Available** | Quantity that can be allocated to new requests (On Hand minus Reserved) |

### 3. Filter by Warehouse

To see stock for a specific warehouse, click the **Filters** button and select your warehouse.

<!-- TODO: Add screenshot: Filter by warehouse -->
<!-- ![Screenshot: Filter by warehouse](/_images/en-us/drims/manage_inventory/filter_warehouse.png) -->

### 4. Search for Specific Products

Use the search bar to find specific items. You can search by:

- Product name (e.g., "blankets" or "rice")
- Product code (e.g., "NFI-001")
- Category (e.g., "Medical Supplies")

<!-- TODO: Add screenshot: Search for products -->
<!-- ![Screenshot: Search for products](/_images/en-us/drims/manage_inventory/search_products.png) -->

## Understanding Stock Status

Items in your warehouse can have different status indicators:

### Stock Availability

| Status | Color | What It Means |
|--------|-------|---------------|
| **Available** | Green | Ready to allocate to new requests |
| **Reserved** | Orange | Allocated to approved requests, awaiting dispatch |
| **Unavailable** | Gray | Out of stock, cannot fulfill requests |

### Quality Status

Some items may have quality flags based on inspection or expiry:

| Status | Icon | What It Means | Action Needed |
|--------|------|---------------|---------------|
| **Good** | Green checkmark | Passed inspection, safe to distribute | None |
| **Expiring Soon** | Yellow warning | Will expire within 30 days | Prioritize for dispatch |
| **Expired** | Red X | Past expiry date | Remove from inventory |
| **Damaged** | Red exclamation | Failed inspection | Review for disposal |

## Check Expiry Dates

For items with shelf life tracking (like medical supplies, food items), you can view expiry information.

### 1. Open Lot/Serial Number View

Click **DRIMS** in the sidebar, then select **Inventory** and **Lots/Serial Numbers**.

<!-- TODO: Add screenshot: Navigate to lots -->
<!-- ![Screenshot: Navigate to lots](/_images/en-us/drims/manage_inventory/navigate_lots.png) -->

### 2. View Expiry Information

The lot list shows tracking details for each batch of items:

<!-- TODO: Add screenshot: Lot list with expiry dates -->
<!-- ![Screenshot: Lot list with expiry dates](/_images/en-us/drims/manage_inventory/lot_list.png) -->

| Column | What It Shows |
|--------|---------------|
| **Lot/Serial Number** | Batch identifier from the manufacturer or donor |
| **Product** | Name of the item |
| **Expiry Date** | When the item expires |
| **On Hand Quantity** | How many units remain from this batch |
| **Status** | Current quality status |

### 3. Filter Expiring Items

To find items expiring soon:

1. Click **Filters**
2. Select **Expiring in 30 days** or set a custom date range
3. Review the list and plan dispatches

<!-- TODO: Add screenshot: Filter expiring items -->
<!-- ![Screenshot: Filter expiring items](/_images/en-us/drims/manage_inventory/filter_expiring.png) -->

```{warning}
Items with red expiry warnings should not be dispatched. Mark them for disposal through the appropriate inventory adjustment process.
```

## View Stock Movements

Track how stock has moved in and out of your warehouses.

### 1. Open Stock Moves

Click **DRIMS** in the sidebar, then select **Inventory** and **Stock Moves**.

<!-- TODO: Add screenshot: Navigate to stock moves -->
<!-- ![Screenshot: Navigate to stock moves](/_images/en-us/drims/manage_inventory/navigate_moves.png) -->

### 2. Understand Movement Types

The stock moves list shows all inventory transactions:

<!-- TODO: Add screenshot: Stock moves list -->
<!-- ![Screenshot: Stock moves list](/_images/en-us/drims/manage_inventory/moves_list.png) -->

| Move Type | Direction | What Triggered It |
|-----------|-----------|-------------------|
| **Donation Receipt** | In | Donation was stocked |
| **Request Dispatch** | Out | Items sent for a request |
| **Return Receipt** | In | Items returned from field |
| **Internal Transfer** | In/Out | Moved between warehouses |
| **Adjustment** | In/Out | Manual stock correction |
| **Disposal** | Out | Damaged/expired items removed |

### 3. Filter Movements

Filter by:

- **Date range** - See movements in a specific period
- **Move type** - See only dispatches or receipts
- **Product** - See all movements for a specific item
- **Warehouse** - See movements for your warehouse only

<!-- TODO: Add screenshot: Filter stock moves -->
<!-- ![Screenshot: Filter stock moves](/_images/en-us/drims/manage_inventory/filter_moves.png) -->

### 4. View Movement Details

Click on any movement to see full details:

<!-- TODO: Add screenshot: Movement details -->
<!-- ![Screenshot: Movement details](/_images/en-us/drims/manage_inventory/move_details.png) -->

| Field | What It Shows |
|-------|---------------|
| **Reference** | Linked document (donation, request, return) |
| **Date** | When the movement occurred |
| **Product** | Item that was moved |
| **Quantity** | How many units moved |
| **From Location** | Source location |
| **To Location** | Destination location |
| **Lot/Serial** | Tracking number if applicable |

## Check Stock by Incident

View inventory allocated to a specific disaster incident.

### 1. Open Incident Stock View

1. Click **DRIMS** in the sidebar
2. Select **Dashboard**
3. Click on the incident card
4. Select the **Stock** tab

<!-- TODO: Add screenshot: Incident stock tab -->
<!-- ![Screenshot: Incident stock tab](/_images/en-us/drims/manage_inventory/incident_stock.png) -->

### 2. Review Incident Inventory

This view shows:

- Total stock value for the incident
- Stock breakdown by product category
- Stock by warehouse serving the incident
- Recent stock movements for the incident

## Make Stock Adjustments

When physical counts don't match system records, you may need to adjust inventory.

```{note}
Stock adjustments require **Warehouse Officer** or **Manager** permissions. All adjustments are logged for audit purposes.
```

### 1. Start an Inventory Adjustment

1. Click **DRIMS** in the sidebar
2. Select **Inventory** and **Adjustments**
3. Click **New**

<!-- TODO: Add screenshot: New adjustment -->
<!-- ![Screenshot: New adjustment](/_images/en-us/drims/manage_inventory/new_adjustment.png) -->

### 2. Fill in Adjustment Details

| Field | What to Enter |
|-------|---------------|
| **Warehouse** | The warehouse being adjusted |
| **Reason** | Why the adjustment is needed (Physical Count, Damaged, Lost, etc.) |
| **Notes** | Detailed explanation of the discrepancy |

### 3. Add Adjustment Lines

For each item to adjust:

| Field | What to Enter |
|-------|---------------|
| **Product** | The item being adjusted |
| **Lot/Serial** | Specific batch if tracked |
| **Theoretical Quantity** | What the system shows |
| **Counted Quantity** | What you physically counted |

<!-- TODO: Add screenshot: Adjustment lines -->
<!-- ![Screenshot: Adjustment lines](/_images/en-us/drims/manage_inventory/adjustment_lines.png) -->

### 4. Validate the Adjustment

Click **Validate** to apply the adjustment. The system will automatically calculate the difference and update stock levels.

<!-- TODO: Add screenshot: Validate adjustment -->
<!-- ![Screenshot: Validate adjustment](/_images/en-us/drims/manage_inventory/validate_adjustment.png) -->

## Are You Stuck?

**Can't see inventory for a warehouse?**

You may not have access to that warehouse. Contact your administrator to verify your warehouse assignments in **Settings** and **Users** and **[Your User]** and **DRIMS Warehouse Access**.

**Stock numbers look wrong?**

Stock quantities are updated in real time for most operations. If numbers don't match:

1. Check for pending dispatches (reserved but not yet shipped)
2. Check for unprocessed donations (received but not yet stocked)
3. Perform a physical count and create an adjustment if needed

**Can't find a product?**

The product may be:
- Not in the catalog - Contact your administrator to add it
- In a different warehouse - Remove the warehouse filter to search all locations
- Using a different name - Try searching by product code instead

**Lot/serial number not showing?**

Not all products require lot tracking. Only items configured for tracking (like medical supplies with expiry dates) will show lot information.

**Can't make an adjustment?**

Stock adjustments require Warehouse Officer permissions. Contact your supervisor to get the appropriate access level, or ask them to make the adjustment on your behalf.

**Why is stock "Reserved" but nothing was dispatched?**

Stock is reserved as soon as a request is approved and allocated to your warehouse. It remains reserved until the dispatch is validated. Check the **Dispatches** list for pending dispatches that need processing.

## Next Steps

- {doc}`donations` - Learn how to receive new donations
- {doc}`dispatches` - Learn how to process dispatches
- {doc}`dashboard` - Monitor warehouse health and alerts
