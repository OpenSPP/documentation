---
openspp:
  doc_status: draft
  products: [core]
  applies_to:
    - social_registry
    - sp_mis
---

# Review a change request

**Applies to:** Social Registry, SP-MIS

This guide is for **validators** (local validators and HQ validators) who need to review and approve change requests submitted by staff.

## What you will do

Review change requests submitted by registry officers, verify the proposed changes against supporting documents, and approve, request changes, or decline them. Approved requests are then finalized and recorded to the registrant's profile.

## Before you start

- You need validator permissions. Your organization may configure this as either:
  - **One global validator role** - A single person with both **Validator** and **Validator HQ** roles, OR
  - **Two-tier system** - Separate **Validator** (local) and **Validator HQ** roles assigned to different people
- Understand your organization's approval policies
- Know what documentation is required for different types of changes

```{note}
**Single Validator Approval**: By default, change requests can be approved by a single validator. The approval system supports two configurations:
- **Default (Single Approver)**: Only one validator needs to approve the request
- **Multiple Approvers Required**: Your organization may configure certain request types to require multiple validators to approve. In this case, the system will track how many approvals are needed and who has already approved.

If you're unsure about your organization's approval requirements, check with your administrator or look at the approval status indicators on the request form.
```

## Steps

### Step 1. Open pending requests

Click **Change Requests** in the main menu, then click **Pending Approval** in the sidebar.

![Pending Approval menu](/_images/en-us/change-requests/review/01-pending-approval-menu-showing-requests-waiting-for.png)

This shows all requests waiting for review.

### Step 2. Open a request to review

Click on a request in the list to open it.

![Request list](/_images/en-us/change-requests/review/02-request-list-showing-pending-change-requests.png)

The request form opens with all details.

### Step 3. Review the request information

Check the header information:

| Field | What to check |
|-------|---------------|
| **Request Type** | What kind of change is requested |
| **Registrant** | Who will be affected by this change |
| **Submitted By** | Who created the request |
| **Submitted On** | When the request was submitted |

![Request header](/_images/en-us/change-requests/review/03-request-header.png)

### Step 4. Review the proposed changes

The **Details** tab shows a side-by-side comparison:

- **Left panel (Current Data)** - The registrant's current information.
- **Right panel (Proposed Changes)** - What will change if approved.

![Side-by-side comparison](/_images/en-us/change-requests/review/04-side-by-side-comparison.png)

Review each proposed change carefully.

### Step 5. Check supporting documents

Click the **Documents** tab to view uploaded files.

![Documents tab](/_images/en-us/change-requests/review/05-documents-tab-showing-uploaded-supporting-files.png)

Click on a document to view it.

Verify that:
- Required documents are present.
- Documents match the requested changes.
- Documents appear authentic.

### Step 6. Review notes

Click the **Notes** tab to see:

- **Description** - Why the change was requested.
- **Internal Notes** - Additional context from the submitter.

![Notes tab](/_images/en-us/change-requests/review/06-notes-tab-showing-description-and-internal-notes.png)

### Step 7. Check status history (optional)

Click the **Status History** tab to see:

- Who created the request.
- Previous review actions (for resubmitted requests).
- Timestamps for each status change.

![Status History tab](/_images/en-us/change-requests/review/07-status-history-tab.png)

### Step 8. Make your decision

You have three options:

#### Option A: Approve

If everything is correct and properly documented:

1. Click **Approve** in the header

![Approve button](/_images/en-us/change-requests/review/08-approve-button-location-in-request-header.png)

2. Confirm by clicking **OK** in the dialog.

![Confirmation dialog](/_images/en-us/change-requests/review/09-approval-confirmation-dialog.png)

The status changes to **Approved**.

```{note}
**Auto-Apply**: By default, most request types have auto-apply enabled. When you approve a request with auto-apply enabled, the changes are automatically recorded and the status becomes **Completed**. If auto-apply is disabled for the request type, you will need to manually click **Finalize & Record Changes** after approval.
```

If manual apply is required, click **Finalize & Record Changes** to complete the request.

![Finalize button](/_images/en-us/change-requests/review/10-finalize-and-record-changes-button.png)

#### Option B: Request changes

If the submitter needs to fix something:

1. Click **Request Changes** in the header

![Request Changes button](/_images/en-us/change-requests/review/11-request-changes-button-to-send-back-for-correction.png)

2. In the dialog, explain what needs to be corrected

![Request Changes dialog](/_images/en-us/change-requests/review/12-request-changes-dialog-with-explanation-field.png)

3. Click **Confirm**.

The status changes to **Needs Changes**. The submitter will see your feedback and can edit and resubmit the request.

```{note}
**When the Request Changes button appears**: The **Request Changes** button is only visible when:
- The request status is **Under Review** (pending approval)
- You have **Validator** or **Validator HQ** permissions
- You have permission to approve this specific request

If you don't see the button, check the troubleshooting section below.
```

#### Option C: Decline

If the request should not be processed:

1. Click **Reject** in the header

![Reject button](/_images/en-us/change-requests/review/13-reject-button-to-decline-the-request.png)

2. In the dialog, explain why the request was declined

![Reject dialog](/_images/en-us/change-requests/review/14-reject-dialog-with-reason-field.png)

3. Click **Confirm**.

The status changes to **Declined**. The changes are not applied.

## Using the All Requests View

To see all requests (not just pending):

1. Click **All Requests** in the sidebar

2. Use filters to narrow the list:

   | Filter | Shows |
   |--------|-------|
   | **Draft** | Requests being created |
   | **Under Review** | Waiting for approval |
   | **Needs Changes** | Sent back for corrections |
   | **Approved** | Approved, waiting to be finalized |
   | **Completed** | Changes have been recorded |
   | **Declined** | Rejected requests |

![Filter options](/_images/en-us/change-requests/review/16-filter-options-for-request-status.png)

3. Use **Group By** to organize by Type, Status, or Creator.

![Group By options](/_images/en-us/change-requests/review/17-group-by-options-for-organizing-requests.png)

## Reviewing multiple requests

For efficient batch processing:

1. Use the kanban view (click the kanban icon)

![Kanban view](/_images/en-us/change-requests/review/18-kanban-view-showing-requests-grouped-by-status.png)

2. Requests are grouped by status.
3. Click a card to open the full request.
4. Use keyboard shortcuts for faster review (when viewing a pending change request form):
   - **A** - Approve
   - **R** - Request Changes
   - **D** - Decline

```{note}
**Keyboard Shortcuts**: These shortcuts work when you have a pending change request form open. They are not available in the kanban view itself - you need to open the request first.
```

## Verifying applied changes

After approving and finalizing a request:

1. Click **View Registrant** in the button box

![View Registrant button](/_images/en-us/change-requests/review/19-view-registrant-button-to-verify-applied-changes.png)

2. Verify the changes appear correctly in the registrant's profile.

3. The change request is linked in the registrant's audit trail.

## Are you stuck?

**Cannot see the Approve button?**
You may not have **Validator** or **Validator HQ** permissions. Contact your administrator.

**Approve button is disabled?**
- The request may not be in **Under Review** status.
- For multi-tier approvals, an earlier tier may need to be completed first.
- For requests requiring multiple approvers, the required number of approvals may not yet be met (check the approval status on the request).
- You may not have **Validator** or **Validator HQ** permissions to approve this request.

**Cannot see any pending requests?**
- Check that you have the **Pending Approval** view selected
- Make sure no filters are hiding requests
- Click **Clear Filters** to reset the view

**Request shows "Unable to Complete Request" error?**
- The error message explains what went wrong.
- This could be a data conflict or validation issue.
- Check the error message displayed in the red alert box on the request form.
- Contact your administrator if the error persists.

**Need to undo an approval?**
Once changes are recorded to a registrant (status: **Completed**), they cannot be undone through the change request system. Create a new change request with the correct information instead.

**Approved request but changes not applied?**
- Check if auto-apply is enabled for this request type. If not, you need to manually click **Finalize & Record Changes**.
- The request must be in **Approved** status (not just pending) before you can finalize it.

**Submitter keeps resubmitting incorrect request?**
Use **Reject** instead of **Request Changes** if the request should not be processed at all. Include a clear explanation in the rejection reason.

**Documents tab is empty but submitter says they uploaded files?**
- Check if the submitter has permission to upload documents.
- The documents may be in a different format than expected.
- Ask the submitter to re-upload using the Document Upload wizard.

**Cannot see the Request Changes button?**
- The request must be in **Under Review** status. If it's in Draft, Approved, or another status, the button won't appear.
- You must have **Validator** or **Validator HQ** permissions. Contact your administrator if you need these permissions.
- For multi-tier approvals, you may need to wait for your tier to become active before the button appears.
- The button appears alongside **Approve** and **Reject** in the header. If you can see those buttons but not **Request Changes**, refresh the page or check with your administrator.

## Next Steps

- {doc}`submit_change_request` - Learn how staff submit requests
- {doc}`change_request_types` - See all available request types
