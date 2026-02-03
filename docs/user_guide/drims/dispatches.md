---
openspp:
  doc_status: draft
  products: [drims]
  applies_to:
    - drims
---

# Process a Dispatch

```{admonition} Applies to: DRIMS
:class: tip
This feature is available in OpenSPP deployments with the DRIMS module installed.
```

This guide is for **warehouse staff** who pick, pack, and ship relief supplies to distribution points.

## What You'll Do

Process a dispatch from an approved request through packing, shipping, and {term}`Proof of Delivery` confirmation.

## Before You Start

- You need **Warehouse Officer** or **DRIMS Manager** access
- The dispatch must be created from an approved request
- Relief items must be in stock at your warehouse

## Creating a Dispatch from a Request

Dispatches are automatically created when a DRIMS coordinator allocates an approved request to your warehouse.

You'll receive dispatches in the **Draft** state, ready to be processed.

### To Find Your Dispatches

1. Click **DRIMS** in the sidebar
2. Select **Dispatches**
3. Filter by **My Warehouse** to see only dispatches assigned to you

<!-- TODO: Add screenshot: DRIMS menu with Dispatches option highlighted -->
<!-- ![Screenshot: DRIMS menu with Dispatches option highlighted](/_images/en-us/drims/dispatches/find_dispatches.png) -->

## Processing the Dispatch

Dispatches move through these states as you process them:

| State | What It Means | What You Do |
|-------|---------------|-------------|
| **Draft** | Just created, not confirmed | Review items and confirm |
| **Confirmed** | Ready to pick, waiting for stock | Reserve items from inventory |
| **Assigned** | Stock reserved, ready to pack | Pick and pack items, validate |
| **Done** | Items packed and validated | Record departure when truck leaves |
| **Departed** | Shipment left warehouse | Wait for delivery confirmation |
| **Arrived** | Shipment reached destination | Complete POD |
| **POD Confirmed** | Delivery confirmed | (Finished) |

### 1. Review and Confirm the Dispatch

Open the dispatch and review the items requested.

**Click Confirm** to move the dispatch to the next stage.

<!-- TODO: Add screenshot: Dispatch form in Draft state with Confirm button -->
<!-- ![Screenshot: Dispatch form in Draft state with Confirm button](/_images/en-us/drims/dispatches/confirm_dispatch.png) -->

### 2. Reserve Stock

After confirming, click **Check Availability** to reserve the items from your warehouse inventory.

If items are available, the dispatch moves to the **Assigned** state.

<!-- TODO: Add screenshot: Dispatch showing Check Availability button -->
<!-- ![Screenshot: Dispatch showing Check Availability button](/_images/en-us/drims/dispatches/check_availability.png) -->

### 3. Pick and Pack Items

Now you're ready to physically pick the items:

1. Print the picking list by clicking **Print → Picking List**
2. Go to your warehouse and collect the items on the list
3. Check quantities match what's on the list
4. Pack items securely for transport

<!-- TODO: Add screenshot: Picking list with items and quantities -->
<!-- ![Screenshot: Picking list with items and quantities](/_images/en-us/drims/dispatches/picking_list.png) -->

### 4. Validate the Dispatch

After packing, return to the dispatch and click **Validate**.

This confirms you've physically picked the items and updates your inventory. The dispatch moves to the **Done** state.

<!-- TODO: Add screenshot: Dispatch form with Validate button -->
<!-- ![Screenshot: Dispatch form with Validate button](/_images/en-us/drims/dispatches/validate_dispatch.png) -->

## Recording Departure

When the truck or vehicle leaves your warehouse with the shipment:

1. Open the dispatch
2. Click **Record Departure**
3. Enter the **Date and Time** the shipment left
4. Click **Confirm**

The dispatch moves to the **Departed** state.

<!-- TODO: Add screenshot: Record Departure dialog with date/time fields -->
<!-- ![Screenshot: Record Departure dialog with date/time fields](/_images/en-us/drims/dispatches/record_departure.png) -->

## Printing the Waybill

The {term}`Waybill` is the official shipping document that travels with the goods.

### To Print the Waybill

1. Open the dispatch
2. Click **Print → Waybill**
3. Give the printed waybill to the driver

The waybill includes:
- Dispatch reference number
- Source warehouse details
- Destination and contact information
- Complete item list with quantities
- Signature blocks for driver and receiver

<!-- TODO: Add screenshot: Waybill print preview -->
<!-- ![Screenshot: Waybill print preview](/_images/en-us/drims/dispatches/print_waybill.png) -->

```{important}
The driver must get the waybill signed by the person receiving the goods at the destination.
```

## Confirming Delivery (Proof of Delivery)

After the shipment arrives at the destination, the field staff or receiver will record proof of delivery.

```{note}
Usually field staff or the destination contact records this information, not warehouse staff. But you may need to enter it if they call or email you the details.
```

### To Record Proof of Delivery

1. Open the dispatch
2. Click **Record Arrival** to log when the shipment reached the destination
3. Scroll to the **Proof of Delivery** section
4. Fill in the following fields:

| Field | What to Enter |
|-------|---------------|
| **Received By** | Full name of the person who received the goods |
| **Receiver Title** | Their position or role (e.g., "Camp Coordinator", "Distribution Officer") |
| **Receiver Phone** | Contact phone number |
| **Signature** | Digital signature (if using tablet at destination) |
| **Delivery Notes** | Any notes about condition, shortages, or issues |

5. Click **Confirm POD** to complete the delivery

<!-- TODO: Add screenshot: Proof of Delivery section with fields filled in -->
<!-- ![Screenshot: Proof of Delivery section with fields filled in](/_images/en-us/drims/dispatches/proof_of_delivery.png) -->

The dispatch moves to the **POD Confirmed** state and the request is marked as delivered.

```{important}
**About Signatures:** If the receiver signs a paper waybill, you can either:
- Scan the signed waybill and attach it to the dispatch
- Take a photo with your phone and upload it
- Enter the receiver's details and note "Paper waybill on file"
```

## Are You Stuck?

**Can't find the Confirm button?**

You may not have Warehouse Officer permissions. Contact your DRIMS administrator.

**Check Availability button says "No Stock"?**

The requested items aren't available in your warehouse. Contact your DRIMS coordinator to either:
- Allocate the request to a different warehouse
- Wait for new donations or transfers

**Validate button is grayed out?**

Make sure you clicked **Check Availability** first to reserve the stock.

**Don't have all the quantities requested?**

You can do a partial delivery:
1. In the picking lines, change the **Done** quantity to what you actually have
2. Click **Validate**
3. The system will ask if you want to create a backorder for the remaining items

**Receiver didn't sign the waybill?**

This shouldn't happen, but if it does:
1. Record the arrival and receiver details anyway
2. In **Delivery Notes**, explain why there's no signature
3. Follow up with your DRIMS coordinator

**Shipment was damaged or items are missing?**

1. In **Delivery Notes**, describe what happened
2. Record the actual quantities received (not what was sent)
3. Your DRIMS coordinator will handle the discrepancy report

**Need to cancel a dispatch?**

If the dispatch is still in **Draft** or **Confirmed** state, you can click **Cancel**. If it's already **Assigned** or later, contact your DRIMS coordinator before canceling.

## Next Steps

- {doc}`returns` - Learn how to handle returned items
- {doc}`manage_inventory` - Learn how to check stock levels
- {doc}`dashboard` - Monitor alerts and KPIs
