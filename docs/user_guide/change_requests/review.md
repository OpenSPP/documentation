---
openspp:
  doc_status: draft
---

# Review and Approve Change Requests

This guide is for **users** (supervisors, program managers) who need to review and approve change requests submitted by staff.

## What You'll Do

Review change requests submitted by registry officers, verify the proposed changes, and approve or reject them. Approved requests automatically update the registrant's information.

## Before You Start

- You need **Change Request Approver** or **Administrator** permissions
- Understand your organization's approval policies
- Know what documentation is required for different types of changes

## Steps

### 1. Open Pending Requests

Click **Registry** in the sidebar, then select **Change Requests**.

The list automatically shows pending requests first.

![](review/1.png)

### 2. Filter by Status (Optional)

Use the **Filters** dropdown to view requests by status:
- **Pending Approval** - Waiting for your review
- **Revision Requested** - Sent back to the submitter
- **Approved** - Approved but not yet applied
- **Applied** - Changes completed
- **Rejected** - Denied requests

![](review/2.png)

### 3. Open a Request

Click on a request to open it and review the details.

![](review/3.png)

### 4. Review the Information

Check the following:

**Header Information:**
- **Request Type** - What kind of change is being requested
- **Registrant** - Who will be affected by this change
- **Applicant** - Who submitted the request (if different from registrant)
- **Created Date** - When the request was submitted

![](review/4.png)

**Change Details:**

Review the fields that will be changed. The exact fields depend on the request type.

For **Edit Individual Information**, you'll see proposed updates like:
- Name changes
- Phone number updates
- Address changes

For **Add Group Member**, you'll see details of the new member:
- Name
- Date of birth
- Gender
- Relationship to household head

![](review/5.png)

**Supporting Documents:**

Click the **Documents** tab to view any uploaded files (ID cards, birth certificates, etc.).

![](review/6.png)

**Notes:**

Check the **Description** and **Internal Notes** fields for context about why the change was requested.

![](review/7.png)

### 5. Check History (Optional)

Click the **History** tab to see:
- Who created the request
- Previous approvers (in multi-level workflows)
- State changes and timestamps

![](review/8.png)

### 6. Make Your Decision

You have three options:

#### Option A: Approve

If everything looks correct:

1. Click **Approve** at the top of the form
2. Add an optional comment explaining your approval
3. Click **Confirm**

The status changes to **Approved** and the changes are applied to the registrant's record.

![](review/9.png)

#### Option B: Request Revision

If you need the submitter to fix something:

1. Click **Request Revision**
2. **Required:** Add a comment explaining what needs to be changed
3. Click **Confirm**

The request goes back to the submitter with status **Revision Requested**.

![](review/10.png)

#### Option C: Reject

If the request should not be processed:

1. Click **Reject**
2. **Required:** Add a comment explaining why it was rejected
3. Click **Confirm**

The status changes to **Rejected** and no changes are applied.

![](review/11.png)

## Multi-Level Approvals

Some request types require multiple approvals:

### First-Level Approver

You'll see:
- Your approval level in the **Approval Sequence** section
- **Next Approvers** who will review after you

After you approve, the request moves to the next approver.

![](review/12.png)

### Final Approver

You'll see:
- Previous approvers and their decisions
- You have the final say

After you approve, the changes are applied immediately.

![](review/13.png)

## Checking Applied Changes

After approving a request:

### 1. View the Updated Record

Click on the **Registrant** name to open their record and verify the changes were applied correctly.

![](review/14.png)

### 2. Check the Audit Trail

In the registrant's record, look for the **Event Data** or **History** tab to see:
- When the change was applied
- Who approved it
- The change request reference

![](review/15.png)

## Bulk Actions

If you have many requests to review:

### 1. Select Multiple Requests

In the list view, check the boxes next to multiple requests.

![](review/16.png)

### 2. Use Action Menu

Click the **Action** dropdown and select:
- **Approve Selected** (if all are valid)
- **Reject Selected** (rarely used)

![](review/17.png)

### 3. Add Bulk Comment

Add a comment that applies to all selected requests, then click **Confirm**.

![](review/18.png)

## Are You Stuck?

**Don't see the Approve button?**
You may not have **Change Request Approver** permissions. Contact your administrator.

**Approve button is disabled?**
The request may require earlier approval levels first. Check the **Approval Sequence** section to see who needs to approve before you.

**Can't see pending requests?**
Check the filters - you may have a filter active that's hiding pending requests. Click **Clear Filters** to see all requests.

**Need to undo an approval?**
Once approved and applied, changes can't be undone through the change request. You'll need to create a new change request with the corrected information.

**Request is stuck in "Pending"?**
This can happen if:
- An earlier approver hasn't acted yet (check approval sequence)
- The approval workflow is misconfigured (contact your administrator)

**Applied changes don't match what I approved?**
Contact your administrator immediately. This could indicate a configuration issue with the apply strategy.

**Getting "Access Denied" error when approving?**
You may be assigned as an approver but don't have the security group permissions. Contact your administrator to add you to the **Change Request Approver** group.

**Don't see documents that were mentioned?**
Check:
- The **Documents** tab (not the main form)
- Your permissions - you may not have access to view certain document types
- Ask the submitter to re-upload if they're missing
