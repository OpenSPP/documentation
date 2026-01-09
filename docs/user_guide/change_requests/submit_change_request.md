---
openspp:
  doc_status: draft
  products: [core]
  applies_to:
    - social_registry
    - sp_mis
---

# Submit a Change Request

**Applies to:** Social Registry, SP-MIS

This guide is for **users** (program staff, registry officers) who need to submit change requests to update registrant information.

## What You Will Do

Create a change request to modify registrant information, such as updating personal details, adding household members, or correcting ID documents. Change requests go through an approval workflow before being applied to the registrant's record.

## Before You Start

- You need **Change Request User** permissions
- Know which registrant needs the update
- Have any required documentation ready (ID documents, birth certificates, etc.)

## Steps

### 1. Open Change Requests

Click **Change Requests** in the main menu.

![Change Requests menu](/_images/en-us/change-requests/submit/01-change-requests-menu-in-main-navigation.png)

### 2. Start a New Request

Click **New Request** in the sidebar menu.

![New Request menu item](/_images/en-us/change-requests/submit/02-new-request-menu-item-in-change-requests-sidebar.png)

This opens the Create Change Request wizard.

### 3. Select the Request Type

Choose the type of change you need from the available options:

| Request Type | Use When |
|--------------|----------|
| Edit Individual Information | Updating personal details (name, phone, address) |
| Edit Group Information | Updating household details |
| Add Group Member | Adding a new person to a household |
| Remove Group Member | Removing someone from a household |
| Update ID Document | Adding or correcting ID numbers |
| Change Head of Household | Designating a new household head |

![Request type selection](/_images/en-us/change-requests/submit/03-request-type-selection-showing-available-change-re.png)

Click on the request type you need.

### 4. Select the Registrant

In the **Registrant** field, search for the person or household you are updating.

Type part of their name or ID number to search.

![Registrant search](/_images/en-us/change-requests/submit/04-registrant-search-field-with-autocomplete-dropdown.png)

Select the correct registrant from the dropdown.

{note}
Some request types only work with individuals, others only with groups. The system filters the registrant list based on your selected request type.

### 5. Click Create

Click **Create** to create the change request.

![Create button](/_images/en-us/change-requests/submit/05-create-button-to-create-the-change-request.png)

The system creates the request and opens it for editing.

### 6. Edit the Change Details

Click **Continue Editing** or **Edit Details** to open the detail form.

![Edit Details button](/_images/en-us/change-requests/submit/06-edit-details-button-to-open-the-detail-form.png)

### 7. Fill in the Change Details

The form shows fields specific to your request type. Fill in the information you want to change.

**For Edit Individual Information:**

| Field | What to Enter |
|-------|---------------|
| Given Name | Person's first name |
| Family Name | Person's surname |
| Date of Birth | Use the calendar picker |
| Gender | Select from dropdown |
| Phone | Contact phone number |
| Email | Email address |
| Address | Street address, city, postal code |

![Edit Individual form](/_images/en-us/change-requests/submit/07-edit-individual-information-form-with-fields-for-p.png)

**For Add Group Member:**

| Field | What to Enter |
|-------|---------------|
| Given Name | New member's first name |
| Family Name | New member's surname |
| Date of Birth | Use the calendar picker |
| Gender | Select from dropdown |
| Relationship | Their role in the household (child, spouse, etc.) |

![Add Member form](/_images/en-us/change-requests/submit/08-add-group-member-form-with-fields-for-new-member-d.png)

### 8. Save the Details

Click **Save** to save your changes to the detail form.

![Save button](/_images/en-us/change-requests/submit/09-save-button-to-save-changes-to-the-detail-form.png)

You return to the main change request form.

### 9. Upload Documents (If Required)

If your request type requires supporting documents:

1. Click the **Documents** tab

   ![Documents tab](/_images/en-us/change-requests/submit/10-documents-tab-for-uploading-supporting-documents.png)

2. Click **Upload Document**

   ![Upload Document button](/_images/en-us/change-requests/submit/11-upload-document-button-in-documents-tab.png)

3. Select the document type and attach the file

   ![Document upload form](/_images/en-us/change-requests/submit/12-document-upload-form-with-type-selection-and-file.png)

4. Click **Upload**

### 10. Add Notes (Optional)

Click the **Notes** tab to add:

- **Description** - Explain why this change is needed
- **Internal Notes** - Notes for reviewers (not visible to the registrant)

![Notes tab](/_images/en-us/change-requests/submit/13-notes-tab-with-description-and-internal-notes-fiel.png)

### 11. Review Your Changes

Before submitting, review the **Details** tab to see a preview of the proposed changes.

The preview shows:
- **Current Data** - What the registrant record looks like now
- **Proposed Changes** - What will change if approved

![Preview of changes](/_images/en-us/change-requests/submit/14-preview-of-changes-showing-current-data-and-propos.png)

### 12. Submit for Approval

When everything is correct, click **Submit for Approval**.

![Submit for Approval button](/_images/en-us/change-requests/submit/15-submit-for-approval-button-to-send-request-for-rev.png)

The status changes from **Draft** to **Under Review**.

![Status changed to Under Review](/_images/en-us/change-requests/submit/16-status-changed-to-under-review-after-submission.png)

## What Happens Next?

After you submit:

1. The request appears in the **Pending Approval** queue for validators
2. A validator reviews your request
3. They may:
   - **Approve** it - Changes are recorded to the registrant
   - **Request Changes** - You will need to edit and resubmit
   - **Decline** it - The request is rejected
4. You can track the status in the **All Requests** view

## Are You Stuck?

**Cannot find the Change Requests menu?**
You may not have Change Request User permissions. Contact your administrator.

**Request type dropdown shows no options?**
No change request types have been configured. Contact your administrator.

**Cannot find the registrant?**
- Make sure they are already registered in the system
- Check if you selected the right request type (some only work with individuals or groups)
- Try searching by ID number instead of name

**Submit button is disabled?**
- Check that all required fields are filled (marked with *)
- Make sure you saved the detail form
- Some request types require documents before submission

**Made a mistake after submitting?**
If a validator sends it back for changes (status: **Needs Changes**), you can edit and resubmit. Otherwise, you may need to ask a validator to decline it so you can start over.

**Need to cancel a draft request?**
Open the request and use the **Action** menu to delete it (only possible while in Draft status).

## Next Steps

- {doc}`review_change_request` - Learn how validators review requests
- {doc}`change_request_types` - See all available request types
