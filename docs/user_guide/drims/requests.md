---
openspp:
  doc_status: draft
  products: [drims]
  applies_to:
    - drims
---

# Submit a Relief Request

```{admonition} Applies to: DRIMS
:class: tip
This feature is available in OpenSPP deployments with the DRIMS module installed.
```

## What You'll Do

Create and submit a request for relief supplies to be delivered to a disaster-affected area.

## Before You Start

- You need **Field Officer** or **Officer** access
- Know which incident you're responding to
- Know the destination area where supplies are needed
- Have information about what items are needed and how many people are affected

## Steps

### 1. Open Requests

Click **DRIMS** in the sidebar, then select **Requests**.

![Screenshot: DRIMS menu with Requests highlighted](/_images/en-us/user_guide/drims/requests/1.png)

### 2. Create New Request

Click the **New** button in the top left.

![Screenshot: Requests list with New button highlighted](/_images/en-us/user_guide/drims/requests/2.png)

### 3. Select the Incident

In the **Incident** field, click the dropdown and choose the disaster incident you're responding to.

![Screenshot: Incident dropdown open](/_images/en-us/user_guide/drims/requests/3.png)

**What this means:** Every request must be linked to a disaster incident (like "Flood 2025" or "Earthquake North Region"). This helps track what supplies are for which emergency.

### 4. Choose Destination Area

In the **Destination Area** field, select where the supplies need to be delivered.

![Screenshot: Destination Area dropdown](/_images/en-us/user_guide/drims/requests/4.png)

**What this means:** This is the specific geographic area (city, district, or zone) where {term}`Beneficiary`(ies) will receive the supplies.

### 5. Set Priority Level

In the **Priority** field, choose the urgency level. See [Understanding Priority Levels](#understanding-priority-levels) below for guidance.

![Screenshot: Priority dropdown](/_images/en-us/user_guide/drims/requests/5.png)

### 6. Select Cluster (Optional)

If your organization uses humanitarian {term}`Cluster`s, select the relevant cluster (like Health, Shelter, Food Security).

![Screenshot: Cluster dropdown](/_images/en-us/user_guide/drims/requests/6.png)

**What this means:** Clusters are coordination groups for different types of relief. This is optional but helps coordinate with other organizations.

### 7. Set Date Needed

Click the **Date Needed** calendar and select when supplies must arrive.

![Screenshot: Date picker open](/_images/en-us/user_guide/drims/requests/7.png)

**Important:** Be realistic. The date you choose affects how your request is prioritized.

### 8. Add Justification

In the **Justification** field, explain why these supplies are needed. Be specific about the situation.

![Screenshot: Justification text field filled](/_images/en-us/user_guide/drims/requests/8.png)

**Example:** "Flash flooding has displaced 500 families. Temporary shelters need clean water and hygiene supplies. No clean water source available in evacuation center."

### 9. Enter Affected Population

In the **{term}`Affected Population`** field, enter the number of people who will benefit from these supplies.

![Screenshot: Affected Population field](/_images/en-us/user_guide/drims/requests/9.png)

### 10. Add Requested Items

In the **Requested Items** section, click **Add a line**.

![Screenshot: Add a line button in items section](/_images/en-us/user_guide/drims/requests/10.png)

For each item:
- **Product:** Select the item from the dropdown (like "Water Purification Tablets" or "Emergency Blankets")
- **Quantity:** Enter how many units you need
- **UoM:** Confirm the unit of measure (boxes, pieces, liters, etc.)

![Screenshot: Item line with product, quantity, and UoM filled](/_images/en-us/user_guide/drims/requests/11.png)

Repeat this step for each type of supply needed.

### 11. Mark as Life-Threatening (If Needed)

If this request involves a life-threatening situation, check the **Life-Threatening** box. See [Life-Threatening Requests](#life-threatening-requests) below.

![Screenshot: Life-Threatening checkbox](/_images/en-us/user_guide/drims/requests/12.png)

**Important:** Only use this for genuine emergencies. It bypasses normal approval workflows.

### 12. Save Draft

Click **Save** to save your request as a draft. You can come back and edit it later.

![Screenshot: Save button](/_images/en-us/user_guide/drims/requests/11.png)

### 13. Submit for Approval

When your request is ready, click **Submit** to send it for approval.

![Screenshot: Submit button](/_images/en-us/user_guide/drims/requests/11.png)

The request status will change to **Pending** and go to your supervisor or logistics coordinator for review.

![Screenshot: Status changed to Pending](/_images/en-us/user_guide/drims/requests/12.png)

## Understanding Priority Levels

Choose the right {term}`Priority Level` for your request:

| Priority | When to Use | Expected Response Time |
|----------|-------------|------------------------|
| **Critical** | Immediate threat to life, injuries, imminent danger | Within hours |
| **High** | Urgent needs, situation deteriorating rapidly | Within 24 hours |
| **Medium** | Standard relief needs, stable situation | Within 48-72 hours |
| **Low** | Non-urgent, supplementary supplies | When resources available |

**Example - Critical:** "50 people trapped in flooded area, need rescue equipment and medical supplies now."

**Example - High:** "Evacuation center has 200 people but no food. Supplies from yesterday running out."

**Example - Medium:** "Community center housing 80 families needs additional blankets and cooking supplies."

**Example - Low:** "Request recreational items for children in stable temporary housing."

## Life-Threatening Requests

The **{term}`Life-Threatening`** flag is for genuine emergencies where delays could result in loss of life.

**When to use it:**
- Medical emergencies requiring immediate supplies
- Rescue operations in progress
- Situations with injured or critically ill people
- Imminent danger to beneficiaries

**What happens:**
- Your request gets highest priority
- Approval workflows are expedited
- Notifications sent to emergency response team
- May bypass normal approval thresholds

**Important:** Misuse of this flag can delay genuine emergencies. Only check it when lives are truly at risk.

## After You Submit

Here's what happens to your request:

1. **Pending Approval** - Your supervisor or logistics coordinator reviews the request
2. **Approved** - If approved, warehouse staff begin preparing supplies
3. **Allocated** - A warehouse is assigned to fulfill your request
4. **Dispatched** - Supplies are picked, packed, and shipped
5. **Delivered** - You'll confirm receipt when supplies arrive

**You'll receive notifications** at each stage. Check the request status anytime by opening it from the Requests list.

**If changes are requested:** Your supervisor may return the request with notes asking for more information or adjustments. You'll receive a notification. Open the request, make the changes, and click **Re-submit**.

**If rejected:** You'll see the rejection reason. You can correct issues and reset the request to draft to try again, or create a new request.

## Are You Stuck?

**Can't find the incident in the dropdown?**

The incident may not be created yet. Contact your supervisor or DRIMS administrator to create the incident record first.

**Don't know which warehouse to request from?**

You don't choose the warehouse. After approval, the logistics team assigns the best warehouse based on stock availability and location.

**Can't find the product you need?**

The product might not be in the system catalog. Contact your DRIMS administrator to add it, or choose the closest alternative and explain in the justification field.

**Submit button is grayed out?**

Make sure you've filled in all required fields:
- Incident
- Destination Area
- Priority
- Date Needed
- At least one requested item

**Request stuck in Pending for days?**

Contact your supervisor or logistics coordinator. They may not have seen the approval notification.

**Need to cancel a submitted request?**

You can't cancel a pending request yourself. Contact the person reviewing it and ask them to reject it, or create a new request with updated information.

**How do I track my request after submission?**

Open the request from the Requests list. The status field shows where it is in the process. You can also see notes from reviewers in the chatter (message section at the bottom).

## Next Steps

- {doc}`dispatches` - Learn how dispatches are processed for your requests
- {doc}`returns` - Learn how to handle returned items
- {doc}`dashboard` - Monitor the status of your requests
