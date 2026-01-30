---
openspp:
  doc_status: draft
  products: [core]
---

# Change Request Builder

This guide is for **implementers** creating change request types with approval workflows. You should be comfortable with forms and workflows like those in KoBoToolbox, but you don't need programming knowledge.

## What is Change Request Builder?

Change Request Builder lets you create new types of registry modification requests with approval workflows. Define what information to collect, how it maps to registry fields, and who needs to approve changes.

## When to Use Change Request Builder

Use this tool when you need a formal process to update registry information:

| Use Case | Example Change Request Type |
|----------|----------------------------|
| Contact updates | "Update Phone Number" with supervisor approval |
| Address changes | "Update Address" requiring documentation |
| ID corrections | "Update ID Document" with verification |
| Data corrections | "Fix Registration Error" with review workflow |

## Mental Model: Change Requests

Think of change requests as "update forms with approval":

| Without Change Requests | With Change Requests |
|------------------------|---------------------|
| Edit registry directly | Submit request → Approve → Apply |
| Changes immediate | Changes reviewed first |
| No audit trail | Full history of who requested what |
| No documentation | Attach supporting documents |
| Anyone can edit | Controlled permissions |

**When to use**:
- Updates need approval
- Changes need documentation
- You want audit history
- Multiple people might conflict

**When NOT to use**:
- Direct edits are fine
- Complex multi-record operations (add member, split household) - use built-in types

## Before You Start

### Prerequisites

- **Studio Editor** or **Studio Manager** permissions
- Understanding of:
  - What registry fields can be updated
  - Who should approve changes
  - What documentation is needed

### What Studio Can Create

Studio handles simple field update requests (80% of needs):

| ✓ Studio Can Create | ✗ Requires Built-in Types |
|---------------------|---------------------------|
| Update phone number | Add group member |
| Update address | Remove group member |
| Update ID documents | Change head of household |
| Correct field values | Split household |
| Update contact info | Merge registrants |
|  | Exit registrant |

**Why the limitation?** Built-in types handle complex multi-record operations that require custom code.

### Planning Your Change Request Type

Decide:

1. **Name**: Clear purpose (e.g., "Update Phone Number")
2. **Applies to**: Individuals, Groups, or both
3. **Fields to collect**: What information does requester provide?
4. **Registry mapping**: Which fields get updated when approved?
5. **Approval workflow**: Simple (one step) or two-level?
6. **Requirements**: Supporting documents? Conflict checks?

## Creating a Change Request Type

### Step 1: Open Change Request Builder

1. Click **Studio** in the main menu
2. Click **Change Requests**
3. Click **+ New CR Type** button

**Screenshot should show**: Studio Dashboard with Change Requests card highlighted, then Change Request Builder list view showing both custom CR types and built-in types (Add Member, Remove Member, etc.).

### Step 2: Enter Basic Information

| Field | What to Enter | Example |
|-------|---------------|---------|
| **Name** | Clear, action-oriented name | "Update Phone Number" |
| **Icon** | Visual identifier | 📱 (phone icon) |
| **Color** | UI color | Blue |
| **Applies to** | Individual, Group, or both | (•) Individuals only |
| **Description** | Shown to users submitting | "Use this form to request a phone number update for a registered beneficiary. Requires supervisor approval." |

**Screenshot should show**: Step 1 of CR type creation wizard with fields filled in as shown in example.

**Tips**:
- Name should be verb-based: "Update X", "Change Y"
- Description helps users understand when to use this CR type
- Icon and color help distinguish CR types visually

Click **Next →** when ready.

### Step 3: Define Fields to Collect

Configure what information the requester provides:

**Screenshot should show**: Step 2 of wizard showing fields table with columns: Field Label, Type, Maps to Registry, Required.

#### Adding Fields

Click **+ Add Field** for each piece of information needed.

**Example: Phone Number Update**

| Field Label | Type | Maps to Registry | Required |
|-------------|------|------------------|----------|
| New Phone Number | Phone | → phone | Yes |
| Reason for Change | Selection | (don't apply) | Yes |
| Supporting Doc | File | (attachment) | No |

**Screenshot should show**: Fields table filled in with the phone number update example.

#### Field Configuration

For each field, configure:

| Setting | Options |
|---------|---------|
| **Field Label** | What users see |
| **Type** | Phone, Text, Selection, File, Date, Number, Yes/No |
| **Maps to Registry** | Which registry field to update (or "don't apply") |
| **Required** | Must be filled? |

#### Mapping to Registry

The "Maps to Registry" setting determines what happens when CR is approved:

| Mapping | Result When Approved |
|---------|---------------------|
| **→ phone** | Updates registrant's phone field |
| **→ address** | Updates registrant's address field |
| **(don't apply)** | Stored for documentation only |
| **(attachment)** | Attached to CR, not applied to registry |

**Common mappings**:

| CR Field | Maps To |
|----------|---------|
| New Phone Number | → phone |
| New Address | → address |
| New Email | → email |
| New ID Number | → x_cst_national_id (custom field) |
| Reason for Change | (don't apply) - documentation only |
| Supporting Document | (attachment) |

#### Selection Field Options

If you add a Selection field (like "Reason for Change"), define the options:

**Screenshot should show**: Selection options configuration for "Reason for Change".

| Value | Label |
|-------|-------|
| `lost_phone` | Lost Phone |
| `new_phone` | Got New Phone |
| `typo` | Correction of Typo |

Click **Next →** when fields are defined.

### Step 4: Configure Approval Settings

**Screenshot should show**: Step 3 of wizard showing approval workflow options.

#### Approval Workflow

Choose workflow type:

| Workflow | Steps | Use When |
|----------|-------|----------|
| **Simple** | Submit → Approve → Apply | Standard approval by supervisor |
| **Two-Level** | Submit → Review → Approve → Apply | Complex changes need multiple reviewers |
| **Custom** | Use existing approval definition | Reuse workflow from other system |

**Most common**: Simple approval

#### Auto-Apply Options

| Option | When to Use |
|--------|-------------|
| **Auto-apply when approved** | Changes apply immediately after approval (recommended) |
| Manual apply | Someone must manually apply after approval (rarely needed) |

#### Documentation Requirements

| Option | When to Use |
|--------|-------------|
| **Require supporting document before submission** | Always need proof (ID changes, address changes) |
| Optional documentation | Documents are nice to have but not required |

#### Conflict Detection

| Option | When to Use |
|--------|-------------|
| **Check for conflicting pending requests** | Prevent multiple simultaneous changes to same field |
| No conflict check | Multiple requests are fine |

**Screenshot should show**: Options checkboxes with "Auto-apply when approved" and "Require supporting document" checked.

#### Form Preview

The wizard shows a preview of what users will see:

```
┌─ Request Info ──────────────────────────────┐
│ Registrant: [Select beneficiary...]        │
└─────────────────────────────────────────────┘
┌─ New Information ───────────────────────────┐
│ New Phone Number: [______________] *        │
│ Reason: [Select...▼] *                      │
│ Supporting Doc: [Upload...]                 │
└─────────────────────────────────────────────┘
```

**Screenshot should show**: Form preview panel showing the rendered form.

Click **Save as Draft** to create the change request type.

## After Creating a Change Request Type

### Test Your CR Type

1. Go to **Registry → Individuals** (or Groups)
2. Open a registrant record
3. Click **Change Requests** tab
4. Click **+ New Request**
5. Select your new CR type
6. Fill in test data
7. Submit the request

**Screenshot should show**: Individual registry form with Change Requests tab open, showing "+ New Request" button and CR type selection.

8. Switch to **GRM → Change Requests**
9. Find your test request
10. Approve it
11. Verify the registry field was updated

**Screenshot should show**: Change Request list view showing the test request with "Pending Approval" status, then detail view with "Approve" button.

### Activate the CR Type

Once tested:

1. Return to **Studio → Change Requests**
2. Find your CR type
3. Click to open it
4. Click **Activate** (requires Studio Manager permission)

## Built-in Change Request Types

Studio shows built-in CR types that cannot be modified:

**Screenshot should show**: Built-in CR types section in CR Builder list view.

| Built-in Type | Purpose | Why Not in Studio |
|---------------|---------|-------------------|
| **Add Member** | Add person to group | Creates new membership record |
| **Remove Member** | Remove person from group | Modifies membership records |
| **Change Head of Household** | Update group head | Changes membership roles |
| **Split Household** | Divide group into two | Multi-record operation |
| **Merge Registrants** | Combine duplicate records | Complex data reconciliation |
| **Exit Registrant** | Mark person as exited | State change + archival |

**Use built-in types** for these operations - don't try to recreate them in Studio.

## Managing Change Request Types

### View All CR Types

**Studio → Change Requests** shows:
- Your custom CR types (editable)
- Built-in CR types (read-only)

**Screenshot should show**: CR type list view with both custom and built-in sections.

### Edit a CR Type

**For Draft CR types**:
- Click the name
- Make changes
- Save

**For Active CR types**:
- Cannot edit field mappings
- Can edit name, description, approval settings
- To change fields: Deactivate → Edit → Reactivate (be careful!)

### Deactivate a CR Type

**Warning**: Deactivating prevents new requests of this type. Existing requests continue to process.

1. Open the CR type
2. Click **Deactivate**
3. System shows impact: "Used by 15 pending requests"
4. Confirm deactivation

## Field Mapping Strategies

### Direct Field Mapping

Simple one-to-one updates:

```
CR Field: New Phone Number
Maps to: phone
When approved: registrant.phone = new_phone_number
```

### Multiple Field Updates

One CR can update multiple fields:

```
CR Type: Update Contact Info
Fields:
  - New Phone → phone
  - New Email → email
  - New Address → address
When approved: All three registry fields updated
```

### Documentation Fields

Fields for context, not applied:

```
CR Field: Reason for Change
Maps to: (don't apply)
Purpose: Stored in CR record for audit history
```

### Attachments

Supporting documents:

```
CR Field: ID Document Photo
Maps to: (attachment)
Purpose: Attached to CR, available for review
```

## Common Patterns

### Phone Number Update

```
Name: Update Phone Number
Applies to: Individuals
Icon: 📱  Color: Blue

Fields:
  - New Phone Number (Phone) → phone [Required]
  - Reason (Selection) → (don't apply) [Required]
    Options: Lost Phone, New Phone, Typo
  - Supporting Document (File) → (attachment) [Optional]

Approval: Simple
Auto-apply: Yes
Require document: No
```

### Address Change

```
Name: Update Address
Applies to: Individuals and Groups
Icon: 🏠  Color: Green

Fields:
  - New Street Address (Text) → address [Required]
  - New Area (Link to Area) → area_id [Required]
  - Reason (Selection) → (don't apply) [Required]
    Options: Moved, Correction, Other
  - Proof of Residence (File) → (attachment) [Required]

Approval: Simple
Auto-apply: Yes
Require document: Yes (proof of residence)
```

### ID Document Update

```
Name: Update ID Document
Applies to: Individuals
Icon: 🆔  Color: Orange

Fields:
  - New ID Number (Text) → x_cst_national_id [Required]
  - ID Type (Selection) → x_cst_id_type [Required]
    Options: National ID, Passport, Driver License
  - ID Expiry Date (Date) → x_cst_id_expiry [Optional]
  - ID Document Photo (File) → (attachment) [Required]
  - Reason (Selection) → (don't apply) [Required]
    Options: New ID Issued, Correction, Lost/Replaced

Approval: Two-Level (extra verification for ID changes)
Auto-apply: Yes
Require document: Yes
Check conflicts: Yes
```

### Household Data Correction

```
Name: Correct Household Info
Applies to: Groups only
Icon: 📝  Color: Purple

Fields:
  - Field to Correct (Selection) → (don't apply) [Required]
    Options: Size, Head of Household Name, Formation Date
  - Correct Value (Text) → (varies) [Required]
  - Evidence/Notes (Long Text) → (don't apply) [Required]
  - Supporting Document (File) → (attachment) [Optional]

Approval: Simple
Auto-apply: No (manual review of which field to update)
Require document: No
```

## Approval Workflow Details

### Simple Approval

```
┌─────────┐    ┌──────────┐    ┌─────────┐
│ Submit  │ →  │ Approve  │ →  │ Applied │
└─────────┘    └──────────┘    └─────────┘

Roles:
- Submit: Field staff, data officers
- Approve: Supervisors, managers
```

### Two-Level Approval

```
┌─────────┐    ┌────────┐    ┌──────────┐    ┌─────────┐
│ Submit  │ →  │ Review │ →  │ Approve  │ →  │ Applied │
└─────────┘    └────────┘    └──────────┘    └─────────┘

Roles:
- Submit: Field staff
- Review: Data quality team
- Approve: Senior management
```

### Auto-Apply vs Manual Apply

| Setting | When Changes Apply | Use When |
|---------|-------------------|----------|
| **Auto-apply** | Immediately after final approval | Standard use (90% of cases) |
| **Manual apply** | Someone clicks "Apply Changes" after approval | Need final manual verification |

## Are You Stuck?

**Can't map field to registry?**
- Make sure the registry field exists (check Registry Field Builder or existing fields)
- Custom fields need to be created first through Field Builder
- Some built-in fields may not be editable (e.g., registration_date)

**CR type created but can't submit requests?**
- Is the CR type **Active**?
- Do you have permission to submit change requests?
- Does the registrant exist in the registry?

**Approval not working?**
- Check that approver has correct permissions
- Verify approval workflow is configured
- Look for error messages in the CR detail view

**Fields not updating after approval?**
- Check that "Auto-apply when approved" is enabled
- Verify field mapping is correct
- Check that mapped field is not read-only

**Want to update multiple registrants at once?**
Studio CR types work one registrant at a time. For bulk updates, contact a developer.

**Can I create a CR for adding group members?**
No, use the built-in "Add Member" CR type. Studio cannot create multi-record operations.

**How do I track who approved what?**
All approvals are logged in the change request audit trail. Go to change request detail → Activity log.

**Can I customize the approval email notifications?**
This requires system configuration outside of Studio. Contact your administrator.

**What if requester enters wrong registrant?**
If the CR is still pending, the submitter or approver can cancel it and create a new one.

**Can I have different approvers for different areas/programs?**
Yes, but this requires approval workflow configuration outside of Studio. The basic Studio CR uses standard approval rules.

**Supporting documents not showing?**
- Check that file was uploaded successfully
- Verify attachments are enabled in your OpenSPP instance
- Large files may need admin to increase upload limits

**Can I make fields conditionally required?**
Not directly in Studio. All fields are either required or optional. For complex conditional logic, contact a developer.

## Next Steps

- **Define eligibility rules**: {doc}`/config_guide/cel/index`
- **Create event types for surveys**: {doc}`event_type_designer`
- **Add custom registry fields**: {doc}`registry_field_builder`
- **Return to Studio overview**: {doc}`overview`
