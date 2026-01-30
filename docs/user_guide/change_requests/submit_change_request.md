---
openspp:
  doc_status: draft
  products: [core]
  applies_to:
    - social_registry
    - sp_mis
---

# Submit a change request

**Applies to:** Social Registry, SP-MIS

This guide is for **users** (program staff, registry officers) who need to submit change requests to update registrant information.

## What you will do

Create a change request to modify registrant information, such as updating personal details, adding household members, or correcting ID documents. Change requests go through an approval workflow before being applied to the registrant's record.

## Before you start

- You need **Change Request User** permissions
- Know which registrant needs the update
- Have any required documentation ready (ID documents, birth certificates, etc.).

## Steps

### Step 1. Open change requests

Click **Change Requests** in the main menu.

![Change Requests menu](/_images/en-us/change-requests/submit/01-change-requests-menu-in-main-navigation.png)

### Step 2. Start a new request

Click **New Request** in the sidebar menu.

![New Request menu item](/_images/en-us/change-requests/submit/02-new-request-menu-item-in-change-requests-sidebar.png)

This opens the create change request wizard.

### Step 3. Select the request type

Choose the type of change you need from the available options. Common request types include:

| Request type | Use when |
|--------------|----------|
| Edit individual information | Updating personal details (name, phone, address) |
| Edit group information | Updating household details |
| Add group member | Adding a new person to a household |
| Remove group member | Removing someone from a household |
| Update ID document | Adding or correcting ID numbers |
| Change head of household | Designating a new household head |

```{note}
**Available request types**: The system may have additional request types configured (such as transfer member, exit registrant, create new group, split household, merge registrants). See {doc}`change_request_types` for a complete reference of all available types.
```

![Request type selection](/_images/en-us/change-requests/submit/03-request-type-selection.png)

Click on the request type you need.

### Step 4. Select the registrant

In the **Registrant** field, search for the person or household you are updating.

Type part of their name or ID number to search.

![Registrant search](/_images/en-us/change-requests/submit/04-registrant-search-field-with-autocomplete-dropdown.png)

Select the correct registrant from the dropdown.

```{note}
Some request types only work with individuals, others only with groups. The system filters the registrant list based on your selected request type.
```

### Step 5. Click create

Click **Create** to create the change request.

![Create button](/_images/en-us/change-requests/submit/05-create-button-to-create-the-change-request.png)

The system creates the request and automatically opens the detail form for editing.

```{note}
**Automatic Detail Form**: After clicking Create, the detail form opens automatically. If you navigate back to the main change request form, you can use the **Edit Details** smart button or the **Continue Editing** button in the Details tab to return to editing.
```

### Step 6. Fill in the change details

The form shows fields specific to your request type. Fill in the information you want to change.

**For Edit Individual Information:**

| Field | What to enter |
|-------|---------------|
| Given Name | Person's first name |
| Family Name | Person's surname |
| Date of Birth | Use the calendar picker |
| Gender | Select from dropdown |
| Phone | Contact phone number |
| Email | Email address |
| Address | Street address, city, postal code |

![Edit Individual form](/_images/en-us/change-requests/submit/06-edit-individual-information.png)

**For Add Group Member:**

| Field | What to enter |
|-------|---------------|
| Given Name | New member's first name |
| Family Name | New member's surname |
| Date of Birth | Use the calendar picker |
| Gender | Select from dropdown |
| Relationship to Head | Their role in the household (child, spouse, etc.) |

![Add Member form](/_images/en-us/change-requests/submit/07-add-group-member.png)

### Step 7. Save the details

Click **Save** to save your changes to the detail form.

![Save button](/_images/en-us/change-requests/submit/08-save-button-to-save-changes-to-the-detail-form.png)

The detail form remains open after saving. To submit the change request, navigate to the main change request form using the breadcrumb navigation or by opening the change request from the list.

### Step 8. Upload documents (if required)

If your request type requires supporting documents:

1. On the change request form, click the **Documents** tab.

   ![Documents tab](/_images/en-us/change-requests/submit/09-documents-tab-for-uploading-supporting-documents.png)

2. Click **Upload Document**.

   ![Upload Document button](/_images/en-us/change-requests/submit/10-upload-document-button-in-documents-tab.png)

3. Select the document type and attach the file.

   ![Document upload form](/_images/en-us/change-requests/submit/11-document-upload-form-with-type-selection-and-file.png)

4. Click **Upload**.

### Step 9. Add notes (optional)

Click the **Notes** tab to add:

- **Description** - Explain why this change is needed.
- **Internal Notes** - Notes for reviewers (not visible to the registrant).

![Notes tab](/_images/en-us/change-requests/submit/12-notes-tab-with-description.png)

### Step 10. Review your changes

Before submitting, open the main change request form and review the **Details** tab to see a preview of the proposed changes.

The preview shows:
- **Current Data** - What the registrant record looks like now.
- **Proposed Changes** - What will change if approved.

```{note}
**Preview availability**: The preview is only visible in the main change request form, not in the detail form. Make sure you've saved the detail form and navigated to the main change request form to see the preview.
```

![Preview of changes](/_images/en-us/change-requests/submit/13-preview-of-changes.png)

### Step 11. Submit for approval

When everything is correct, click **Submit for Approval**.

![Submit for Approval button](/_images/en-us/change-requests/submit/14-submit-for-approval-button-to-send-request-for-rev.png)

The status changes from **Draft** to **Under Review** (also referred to as "Pending Approval" in some menus).

![Status changed to Under Review](/_images/en-us/change-requests/submit/15-status-changed-to-under-review-after-submission.png)

## What happens next?

After you submit:

1. The request appears in the **Pending Approval** (or "Under Review") queue for validators
2. A validator reviews your request
3. They may:
   - **Approve** it - Changes are approved and ready to be finalized (requires "Finalize & Record Changes" action to actually apply)
   - **Request Changes** - You will need to edit and resubmit
   - **Decline** it - The request is rejected
4. You can track the status in the **All Requests** view.

```{note}
**Approval vs. finalization**: When a validator approves your request, it moves to **Approved** status. However, the changes are not yet applied to the registrant's record. A separate "Finalize & Record Changes" action must be performed to actually record the changes. This provides an additional safety check before making permanent changes.
```

## Are you stuck?

**Cannot find the Change Requests menu?**
You may not have Change Request User permissions. Contact your administrator.

**Request type dropdown shows no options?**
No change request types have been configured. Contact your administrator.

**Cannot find the registrant?**
- Make sure they are already registered in the system.
- Check if you selected the right request type (some only work with individuals or groups).
- Try searching by ID number instead of name.

**Submit button is disabled?**
- Check that all required fields are filled (marked with *).
- Make sure you saved the detail form.
- The system checks that you have actually proposed changes - make sure you've entered information in the detail form that differs from the current registrant data.
- Some request types require documents before submission.

**Made a mistake after submitting?**
If a validator sends it back for changes (status: **Needs Changes**), you can edit and resubmit. Otherwise, you may need to ask a validator to decline it so you can start over.

**Need to cancel a draft request?**
Open the request and use the **Action** menu to delete it (only possible while in Draft status).

## Next steps

- {doc}`review_change_request` - Learn how validators review requests
- {doc}`change_request_types` - See all available request types
