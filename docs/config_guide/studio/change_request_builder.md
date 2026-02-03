---
openspp:
  doc_status: draft
  products: [core]
---

# Change Request Builder

This guide is for **implementers** creating change request types with approval workflows. You should be comfortable with forms and workflows like those in KoBoToolbox, but you don't need programming knowledge.

## What is Change Request Builder?

Change Request Builder lets you create new types of registry modification requests with approval workflows. Define which existing registry fields can be updated and who needs to approve the changes.

## When to use Change Request Builder

Use this tool when you need a formal process to update registry information:

| Use case | Example change request type |
|----------|----------------------------|
| Contact updates | "Update Phone Number" with supervisor approval |
| Address changes | "Update Address" requiring review |
| ID corrections | "Update ID Document" with verification |
| Data corrections | "Fix Registration Error" with review workflow |

## Mental model: change requests

Think of change requests as "update forms with approval":

| Without change requests | With change requests |
|------------------------|---------------------|
| Edit registry directly | Submit request → Approve → Apply |
| Changes immediate | Changes reviewed first |
| No audit trail | Full history of who requested what |
| Anyone can edit | Controlled permissions |

**When to use**:
- Updates need approval before taking effect
- You want audit history of all changes
- Multiple people might request changes to the same registrant

**When NOT to use**:
- Direct edits are acceptable
- Complex multi-record operations (add member, split household) - use built-in types

## Before you start

### Prerequisites

- **Studio Editor** or **Studio Manager** permissions
- Understanding of:
  - What registry fields can be updated
  - Who should approve changes

### What Studio can create

Studio handles simple field update requests (most common needs):

| ✓ Studio can create | ✗ Requires built-in types |
|---------------------|---------------------------|
| Update phone number | Add group member |
| Update address | Remove group member |
| Update ID information | Change head of household |
| Correct field values | Split household |
| Update contact info | Merge registrants |
|  | Exit registrant |

**Why the limitation?** Built-in types handle complex multi-record operations that require custom code.

### Planning your change request type

Decide:

1. **Name**: Clear purpose (e.g., "Update Phone Number")
2. **Applies to**: Individuals, Groups, or both
3. **Fields to update**: Which existing registry fields can be changed
4. **Approval**: Does it need approval before changes are applied?

## Creating a change request type

### Step 1: Open Change Request Builder

1. Click **Studio** in the main menu

![Studio Dashboard](/_images/en-us/config_guide/studio/change_request_builder/01-studio-dashboard.png)

2. Click **Change Requests** (under Forms & Fields)
3. Click the **New** button

![Change Request Types list view](/_images/en-us/config_guide/studio/change_request_builder/02-cr-types-list.png)

### Step 2: Enter basic information

![CR type form empty](/_images/en-us/config_guide/studio/change_request_builder/03-cr-type-form-empty.png)

| Field | What to enter | Example |
|-------|---------------|---------|
| **CR Type Name** | Descriptive name | "Update Phone Number" |
| **Technical Name** | Auto-generated code (read-only after save) | `x_cr_update_phone_number` |
| **Target Registry** | Who this applies to | Individual, Group/Household, or Both |
| **Description** | Optional explanation | "Request to update phone number for a registered beneficiary" |

### Step 3: Configure approval settings

| Field | What it does | Default |
|-------|--------------|---------|
| **Requires Approval** | If checked, requests need review before changes apply | Checked |
| **Who can approve** | Select user group authorized to approve | (select a group) |
| **Auto-apply when approved** | If checked, changes apply immediately after approval | Checked |

**Tip**: If approval is not required, changes can be applied immediately when the request is submitted.

![CR type form filled](/_images/en-us/config_guide/studio/change_request_builder/04-cr-type-form-filled.png)

### Step 4: Define field mappings

Click the **Field Mappings** tab to specify which registry fields can be updated.

![Field Mappings tab empty](/_images/en-us/config_guide/studio/change_request_builder/05-field-mappings-tab-empty.png)

Click **Add a line** to add each field:

![Add field mapping](/_images/en-us/config_guide/studio/change_request_builder/06-add-field-mapping.png)

| Setting | What to enter |
|---------|---------------|
| **Field** | Select from existing res.partner fields |
| **Label** | Display name in the request form |
| **Required** | Check if field must be filled |
| **Read-only** | Check if field is shown but cannot be edited |

#### How field mapping works

When you select a field, it automatically maps to that registry field:

| Field selected | Result when approved |
|----------------|---------------------|
| `phone` | Updates registrant's phone field |
| `street` | Updates registrant's street address |
| `email` | Updates registrant's email field |
| Custom fields (`x_*`) | Updates the custom field on registrant |

All fields map directly to their corresponding registry field. When a change request is approved, the values are copied to the registrant record.

#### Example field mapping

For an "Update Phone Number" change request:

| Field | Label | Required | Read-only |
|-------|-------|----------|-----------|
| `phone` | New Phone Number | Yes | No |

![Field mapping filled](/_images/en-us/config_guide/studio/change_request_builder/07-field-mapping-filled.png)

#### Field mapping options (advanced)

Click on a field row to open detailed configuration:

| Option | Use for |
|--------|---------|
| **Help Text** | Additional guidance for users filling the form |
| **Validation Type** | None, Regular Expression, or Domain |
| **Validation Rule** | Regex pattern or domain expression (if validation enabled) |

### Step 5: Save as draft

Click **Save** to create the change request type in Draft state.

![Draft state with Activate button](/_images/en-us/config_guide/studio/change_request_builder/09-draft-state-activate-button.png)

## Change request type lifecycle

Change request types follow a three-state lifecycle:

```
Draft ──► Active ──► Inactive
  ▲                     │
  └─────────────────────┘
      (can reactivate)
```

| State | Can edit fields? | Can edit settings? | Can be used? | Actions available |
|-------|-----------------|-------------------|--------------|-------------------|
| **Draft** | Yes | Yes | No | Activate |
| **Active** | Yes (add/modify) | No | Yes | Deactivate, View Requests |
| **Inactive** | No | No | No | Reactivate |

**Note**: Unlike Event Types, active Change Request Types allow you to add or modify field mappings. Core settings (name, target, approval) remain locked while active.

### Activating a change request type

1. Open the change request type in Draft state
2. Click **Activate** (requires Studio Manager permission)
3. The type becomes available for submitting requests

### Deactivating a change request type

1. Open an Active change request type
2. Click **Deactivate**
3. Existing requests continue to process, but no new requests can be created

## Using change request types

### Submitting a change request

Once a change request type is active:

1. Go to **Registry** and open an individual or group record
2. Look for the **Change Requests** tab
3. Click to create a new request
4. Select the change request type
5. Fill in the new values
6. Submit the request

### Approving a change request

If approval is required:

1. Go to **GRM → Change Requests**
2. Find the pending request
3. Review the requested changes
4. Click **Approve** or **Reject**
5. If approved and auto-apply is enabled, changes are applied immediately

### Viewing audit history

From a change request type:
- Click **View Requests** to see all requests of this type
- The **Audit Trail** tab shows creation, activation, and modification history

![Audit Trail tab](/_images/en-us/config_guide/studio/change_request_builder/08-audit-trail-tab.png)

## Managing change request types

### View all change request types

**Studio → Change Requests** shows all types:

| Column | Shows |
|--------|-------|
| **Name** | Change request type name |
| **Technical Name** | Internal code |
| **Target Type** | Individual, Group/Household, or Both |
| **Fields** | Number of field mappings |
| **State** | Draft, Active, or Inactive |

![List view with data](/_images/en-us/config_guide/studio/change_request_builder/10-list-view-with-data.png)

### Filtering change request types

Use the search and filter options:
- **Filter by state**: Draft, Active, Inactive
- **Filter by target**: Individual, Group
- **Search by name**: Find specific types

## Common patterns

### Phone number update

```
Name: Update Phone Number
Applies to: Individuals
Requires Approval: Yes

Field Mappings:
  - phone → "New Phone Number" [Required]
```

### Address change

```
Name: Update Address
Applies to: Individuals and Groups
Requires Approval: Yes

Field Mappings:
  - street → "Street Address" [Required]
  - city → "City" [Required]
  - zip → "Postal Code" [Optional]
```

### Email update

```
Name: Update Email
Applies to: Individuals
Requires Approval: Yes

Field Mappings:
  - email → "New Email Address" [Required]
```

## Are you stuck?

**Can't see the Activate button?**
- You need Studio Manager permission
- The change request type must have at least one field mapping
- Check that you're viewing a Draft type

**Can't edit settings on an active type?**
- Active types have locked core settings (name, target, approval)
- You can still add or modify field mappings
- To change core settings: Deactivate first, then edit

**Field not appearing in the mapping dropdown?**
- Only stored fields from res.partner appear in the list
- System fields and computed fields are excluded
- Custom fields (x_*) should appear if they're stored

**Changes not applying after approval?**
- Check that "Auto-apply when approved" is enabled
- Verify the field mapping is correct
- Check that the mapped field is not read-only on the registrant

**Want to add documentation-only fields?**
This is not currently supported. All mapped fields will update the registry when approved. For documentation needs, consider using the notes/description fields on the change request itself.

**Can I create a change request for adding group members?**
No, use the built-in "Add Member" change request type. Studio cannot create multi-record operations.

**How do I track who approved what?**
All approvals are logged in the change request record. Go to the request detail view to see the approval history.

**What if the requester selects the wrong registrant?**
If the request is still pending, the submitter or approver can cancel it and create a new one.

## Next steps

- **Create event types for surveys**: {doc}`event_type_designer`
- **Add custom registry fields**: {doc}`registry_field_builder`
- **Define eligibility rules**: {doc}`/config_guide/cel/index`
- **Return to Studio overview**: {doc}`overview`
