---
openspp:
  doc_status: draft
  products: [drims]
  applies_to:
    - drims
---

# Process a dispatch

```{admonition} Applies to: DRIMS
:class: tip
This feature is available in OpenSPP deployments with the DRIMS module installed.
```

This guide is for **warehouse staff** who pick, pack, and ship relief supplies to distribution points.

## What you'll do

Process a dispatch from an allocated request: confirm availability, pick and pack items, record departure, and confirm delivery with proof of delivery.

## Before you start

- You need **Warehouse Officer** or **DRIMS Manager** access
- The dispatch must have been created by a coordinator from an approved, allocated request
- Relief items must be in stock at your warehouse

## How dispatches are created

Dispatches are created automatically when a DRIMS coordinator allocates an approved request and clicks **Create Dispatch**. See {doc}`requests` for how coordinators do this.

A single request can have **multiple dispatches** — for example, if only part of the stock is available now and the rest arrives later. Each dispatch covers the not-yet-dispatched balance at the time it was created.

You'll receive dispatches in the **Draft** state, ready to be processed.

## Finding your dispatches

1. Click **DRIMS** in the sidebar
2. Select **Dispatches**
3. Use the **My Warehouse** filter to see only dispatches assigned to your warehouse

<!-- ![Dispatches list filtered to My Warehouse showing Draft dispatches](/_images/en-us/user_guide/drims/dispatches/01-dispatches-list.png) -->

## Dispatch states

| State | What it means | What you do |
|-------|---------------|-------------|
| **Draft** | Created, not yet confirmed | Review items and confirm |
| **Confirmed** | Ready to pick, waiting for stock reservation | Reserve items |
| **Assigned** | Stock reserved, ready to pack | Pick and pack items |
| **Done** | Items picked and validated | Record departure |
| **Departed** | Shipment left the warehouse | Wait for delivery confirmation |
| **Arrived** | Shipment reached destination | Complete proof of delivery |
| **POD Confirmed** | Delivery confirmed | Finished |

## Processing a dispatch

### 1. Review and confirm

Open the dispatch and check that the item list matches what you expect.

Click **Confirm** to move it forward.

<!-- ![Dispatch form with Confirm button and list of items](/_images/en-us/user_guide/drims/dispatches/02-confirm-dispatch.png) -->

### 2. Reserve stock

After confirming, click **Check Availability** to reserve items from your warehouse inventory.

If items are available, the dispatch moves to **Assigned**.

<!-- ![Check Availability button on a confirmed dispatch](/_images/en-us/user_guide/drims/dispatches/03-check-availability.png) -->

### 3. Pick and pack items

1. Print the picking list: click **Print → Picking List**
2. Go to your warehouse and collect the items on the list
3. Verify quantities match the list
4. Pack items securely for transport

### 4. Validate the dispatch

After packing, return to the dispatch and click **Validate**.

This confirms that the items have been physically picked and updates your inventory. The dispatch moves to **Done**.

<!-- ![Validate button on an assigned dispatch](/_images/en-us/user_guide/drims/dispatches/04-validate-dispatch.png) -->

```{note}
If a validation error appears directing you to the **DRIMS tab**, open the dispatch form's DRIMS tab to see the specific issue — for example, a mismatch between allocated quantities and what was picked.
```

## Partial quantities

If you don't have all the requested quantities available:

1. In the picking lines, change the **Done** quantity to what you physically have
2. Click **Validate**
3. The system asks whether to create a backorder for the remaining items
4. Select **Create Backorder** — this creates a second dispatch for the outstanding balance

The coordinator can then allocate additional stock and dispatch the backorder when it becomes available.

## Recording departure

When the vehicle leaves your warehouse with the shipment:

1. Open the dispatch (now in **Done** state)
2. Click **Record Departure**
3. Enter the date and time the shipment left
4. Click **Confirm**

The dispatch moves to **Departed**.

<!-- ![Record Departure button on a Done dispatch](/_images/en-us/user_guide/drims/dispatches/05-record-departure.png) -->

## Printing the waybill

The {term}`Waybill` is the official shipping document that travels with the goods.

1. Open the dispatch
2. Click **Print → Waybill**
3. Give the printed waybill to the driver

The waybill includes the dispatch reference, source and destination details, the full item list with quantities, and signature blocks for the driver and receiver.

```{important}
The driver must get the waybill signed by the person receiving the goods at the destination.
```

## Confirming delivery (proof of delivery)

After the shipment arrives, record proof of delivery (POD).

```{note}
Field staff at the destination usually record this. But if they contact you with the details, you can enter it on their behalf.
```

### 1. Record arrival

When the shipment reaches the destination, open the dispatch and click **Record Arrival** to log the arrival date and time.

The dispatch moves to **Arrived**.

<!-- ![Record Arrival button on a Departed dispatch](/_images/en-us/user_guide/drims/dispatches/06-record-arrival.png) -->

### 2. Complete the proof of delivery

Scroll to the **Proof of Delivery** section and fill in:

| Field | What to enter |
|-------|---------------|
| **Received by** | Full name of the person who received the goods |
| **Receiver title** | Their position (e.g., "Camp Coordinator", "Distribution Officer") |
| **Receiver phone** | Contact phone number |
| **Signature** | Digital signature if using a tablet at destination |
| **Delivery notes** | Any notes about condition, shortages, or issues |

Click **Confirm POD**.

<!-- ![Proof of Delivery section with receiver fields and Confirm POD button](/_images/en-us/user_guide/drims/dispatches/07-confirm-pod.png) -->

The dispatch moves to **POD Confirmed** and the linked request line is marked as delivered.

```{important}
**If the receiver signed a paper waybill instead**, you can either scan/photograph it and attach it to the dispatch, or enter the receiver's details and note "Paper waybill on file" in **Delivery Notes**.
```

## Are you stuck?

**Can't find the Confirm button?**

You may not have Warehouse Officer permissions. Contact your DRIMS administrator.

**Check Availability says no stock?**

The items aren't available at your warehouse. Contact your DRIMS coordinator to either allocate from a different warehouse or wait for new stock.

**Validate button is grayed out?**

Click **Check Availability** first to reserve the stock before validating.

**A validation error mentions the DRIMS tab?**

Open the **DRIMS** tab on the dispatch form. It will show the specific reason the validation failed — usually a quantity mismatch between what was allocated and what was picked.

**Shipment was damaged or items are missing?**

In **Delivery Notes**, describe what happened and record the actual quantities received. Your DRIMS coordinator will handle the discrepancy follow-up.

**Receiver didn't sign the waybill?**

Record the arrival and enter the receiver's details. In **Delivery Notes**, explain why there's no signature and follow up with your coordinator.

**Need to cancel a dispatch?**

Dispatches in **Draft** or **Confirmed** state can be cancelled with the **Cancel** button. If the dispatch is already **Assigned** or later, contact your DRIMS coordinator before cancelling.

## Next steps

- {doc}`returns` - Handle items returned from the field
- {doc}`manage_inventory` - Check updated stock levels after dispatch
- {doc}`dashboard` - Monitor warehouse alerts and KPIs
