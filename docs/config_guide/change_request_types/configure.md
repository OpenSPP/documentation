---
openspp:
  doc_status: draft
  products: [core]
---

# Configure Change Request Types

This guide is for **implementers** who need to configure change request types to match program requirements. You should be comfortable with logic builders like CommCare or Kobo, but you don't need to write Python code for basic configurations.

## Mental Model

Change requests in OpenSPP V2 follow a configuration-driven architecture with three layers:

1. **Request Type** - Defines what kind of change can be made (e.g., "Add Member", "Edit Individual")
2. **Detail Model** - Stores the specific fields for this request type (real Odoo fields, not JSON)
3. **Apply Strategy** - Controls how approved changes are written to the registrant record

```
┌──────────────────────────────────────┐
│   Change Request Type Config         │
│   (spp.change.request.type)          │
├──────────────────────────────────────┤
│ • Name: "Edit Phone Number"          │
│ • Code: edit_phone                   │
│ • Target: Individual                 │
│ • Approval: Single-level             │
│ • Apply Strategy: Field Mapping      │
└──────────────────┬───────────────────┘
                   │
      ┌────────────┴────────────┐
      ▼                         ▼
┌─────────────────┐   ┌──────────────────┐
│ Detail Model    │   │ Apply Mappings   │
│ (real fields)   │   │                  │
├─────────────────┤   ├──────────────────┤
│ • new_phone     │   │ new_phone → phone│
│ • phone_type    │   │                  │
│ • is_primary    │   │                  │
└─────────────────┘   └──────────────────┘
```

## Basic Configuration (Using Existing Detail Models)

### Step 1: Create the Request Type

Navigate to **Change Requests → Configuration → Change Request Types** and click **New**.

**Header:**

Enter the type name in the header field (placeholder shows "Type Name").

**BASIC INFO section:**

| Field | Value | Notes |
|-------|-------|-------|
| Code | `edit_individual` | Unique identifier (lowercase, underscores only) |
| Sequence | 10 | Lower numbers appear first in menus |
| Icon | `fa-edit` | Font Awesome icon class |
| Color | (select) | Color picker for visual identification |

**TARGET section:**

| Field | Value | Notes |
|-------|-------|-------|
| Target Type | Individual | Individual, Group/Household, or Both |
| Is Requires Applicant? | No | If yes, forces separate "submitted by" field |

**Description** (at bottom of form): Enter a description to help users understand when to use this type.

### Step 2: Link to Detail Model

Navigate to the **Detail Model** tab.

| Field | Value | Notes |
|-------|-------|-------|
| Detail Model? | `spp.cr.detail.edit_individual` | Technical model name (pre-created, required) |
| Detail Form View? | (leave blank) | Auto-selects default view |

```{note}
For basic configurations, use existing detail models:
- `spp.cr.detail.edit_individual` - Edit person info
- `spp.cr.detail.edit_group` - Edit household info
- `spp.cr.detail.add_member` - Add person to household
- `spp.cr.detail.add_child` - Add child with specialized fields
```

### Step 3: Configure Approval Workflow

Navigate to the **Approval** tab.

| Field | Value | Notes |
|-------|-------|-------|
| Approval Workflow | Select from dropdown | Choose existing approval definition |
| Auto Approve From Event | No | If yes, requests from event data are auto-approved |

```{note}
The **Auto Apply On Approve** field is located in the **Apply Configuration** tab (see Step 4).
```

**Creating Approval Workflows:**

If you need a new workflow, go to **Studio → Approvals → Definitions** first.

Example: Two-level approval for sensitive changes

| Field | Value |
|-------|-------|
| Name | Change Request - Sensitive |
| Levels | 2 |
| Level 1 Approvers | Supervisor Group |
| Level 2 Approvers | Program Manager Group |
| Require All | No |

### Step 4: Configure Apply Strategy

Navigate to the **Apply Configuration** tab.

**For Simple Field Mapping:**

| Field | Value | Notes |
|-------|-------|-------|
| Apply Strategy | Field Mapping | Copies fields from detail to registrant |
| Auto Apply On Approve | Yes | If yes, changes apply immediately when approved |

**Field Mappings:**

In the **Field Mappings** section below, add your mappings:

| Source Field | Target Field | Transform |
|--------------|--------------|-----------|
| `given_name` | `given_name` | Direct Copy |
| `family_name` | `family_name` | Direct Copy |
| `phone` | `phone` | Direct Copy |
| `email` | `email` | Direct Copy |
| `birthdate` | `birthdate` | Direct Copy |
| `gender_id` | `gender` | Direct Copy |

**For Custom Logic:**

| Field | Value | Notes |
|-------|-------|-------|
| Apply Strategy | Custom Method | Uses Python code |
| Apply Model | `spp.cr.apply.add_member` | Pre-created custom strategy |
| Apply Method | `apply` | Method name (usually "apply") |

### Step 5: Configure Document Requirements

Navigate to the **Documents** tab.

| Field | Value | Notes |
|-------|-------|-------|
| Document Validation Mode | No Validation | No Validation / Warning if Missing / Block if Missing |
| Available Documents? | (select document types) | Document types that can be attached |
| Required Documents? | (select document types) | Use Ctrl/Cmd+Click for multiple |

**Document Validation Modes:**
- **No Validation** - Documents are optional
- **Warning if Missing** - Shows warning if missing, but allows submission
- **Block if Missing** - Blocks submission until all required documents are uploaded

## Advanced: Creating Custom Detail Models

For request types that need fields not in the default models, you can create custom detail models.

### Using Configurator V2 (Recommended)

1. **Navigate to Studio → Models → New**
2. **Configure the model:**

| Field | Value |
|-------|-------|
| Name | CR Detail: Update Phone |
| Technical Name | `spp.cr.detail.update_phone` |
| Inherit | `spp.cr.detail.base` |

3. **Add fields:**

| Field Name | Type | Widget | Required |
|------------|------|--------|----------|
| `new_phone` | Char | Phone | Yes |
| `phone_type` | Selection | Selection | No |
| `is_primary` | Boolean | Checkbox | No |
| `verification_code` | Char | Text | No |

4. **Add selection options for `phone_type`:**

| Value | Label |
|-------|-------|
| `mobile` | Mobile |
| `landline` | Landline |
| `work` | Work |

5. **Generate the form view** using Studio's view builder
6. **Activate the model**

### Using Code (For Developers)

Create a module `spp_cr_custom/details/update_phone.py`:

```python
from odoo import models, fields, api

class SPPCRDetailUpdatePhone(models.Model):
    _name = 'spp.cr.detail.update_phone'
    _description = 'CR Detail: Update Phone'
    _inherit = ['spp.cr.detail.base']

    new_phone = fields.Char(string='Phone Number', required=True)
    phone_type = fields.Selection([
        ('mobile', 'Mobile'),
        ('landline', 'Landline'),
        ('work', 'Work'),
    ], string='Phone Type')
    is_primary = fields.Boolean(string='Primary Number', default=True)
    verification_code = fields.Char(string='Verification Code')

    @api.onchange('new_phone')
    def _onchange_new_phone(self):
        """Validate phone format"""
        if self.new_phone and not self.new_phone.replace('+', '').replace(' ', '').isdigit():
            return {
                'warning': {
                    'title': 'Invalid Format',
                    'message': 'Phone number should contain only digits, spaces, and +'
                }
            }
```

Create the view in `spp_cr_custom/views/detail_update_phone_views.xml`:

```xml
<record id="spp_cr_detail_update_phone_form" model="ir.ui.view">
    <field name="name">spp.cr.detail.update_phone.form</field>
    <field name="model">spp.cr.detail.update_phone</field>
    <field name="arch" type="xml">
        <form>
            <header>
                <button name="action_submit_for_approval"
                        string="Submit for Approval"
                        type="object"
                        class="btn-primary"
                        invisible="approval_state != 'draft'"/>
                <field name="approval_state" widget="statusbar"/>
            </header>
            <sheet>
                <div class="oe_title">
                    <h1>Update Phone Number</h1>
                </div>

                <group string="Individual">
                    <field name="registrant_id" readonly="1"/>
                </group>

                <group string="New Phone Information">
                    <group>
                        <field name="new_phone" widget="phone"/>
                        <field name="phone_type"/>
                    </group>
                    <group>
                        <field name="is_primary"/>
                        <field name="verification_code"/>
                    </group>
                </group>
            </sheet>
        </form>
    </field>
</record>
```

## Common Configuration Patterns

### Pattern 1: Auto-Approved Simple Changes

For low-risk changes that don't need manual review:

| Field | Value |
|-------|-------|
| Approval Workflow | (select "Auto-Approve") |
| Auto Apply on Approve | Yes |
| Document Validation | None |

**Use cases:** Phone updates, email changes, address corrections

### Pattern 2: Two-Level Sensitive Changes

For changes requiring verification:

| Field | Value |
|-------|-------|
| Approval Workflow | (select "Two-Level Approval") |
| Auto Apply on Approve | Yes |
| Document Validation | Required |
| Required Documents | National ID, Supporting Document |

**Use cases:** Name changes, birth date corrections, gender updates

### Pattern 3: Manual Application

For changes needing technical review before applying:

| Field | Value |
|-------|-------|
| Approval Workflow | (select "Single Approver") |
| Auto Apply on Approve | **No** |
| Apply Strategy | Manual |

**Use cases:** Complex group restructuring, data migrations, bulk corrections

### Pattern 4: Event-Sourced Auto-Creation

For change requests created automatically from event data:

| Field | Value |
|-------|-------|
| Auto Approve from Event | Yes |
| Auto Apply on Approve | Yes |
| Apply Strategy | Field Mapping |

**Use cases:** Field survey updates, mobile app submissions, API integrations

## Field Mapping Configuration

### Basic Mapping

When source and target field names match exactly:

| Source Field | Target Field | Transform |
|--------------|--------------|-----------|
| `phone` | `phone` | Direct Copy |
| `email` | `email` | Direct Copy |

### Relational Field Mapping

For Many2one fields, map the ID:

| Source Field | Target Field | Transform |
|--------------|--------------|-----------|
| `gender_id` | `gender` | Direct Copy |
| `area_id` | `area_id` | Direct Copy |

```{note}
The system automatically handles `.id` extraction for relational fields.
```

### Expression-Based Mapping

For complex transformations, use safe expressions:

| Source Field | Target Field | Transform | Expression |
|--------------|--------------|-----------|------------|
| `given_name` | `name` | Expression | `(value or '') + ' ' + (detail.family_name or '')` |
| `birthdate` | `age_years` | Expression | `(datetime.now().date() - value).days // 365 if value else 0` |

**Available variables in expressions:**
- `value` - The source field value
- `detail` - The entire detail record
- `registrant` - The target registrant record
- `env` - Odoo environment
- `datetime` - Python datetime module
- `date` - Python date module

### Conditional Mapping

Only apply mapping if a condition is met:

| Source Field | Target Field | Transform | Expression |
|--------------|--------------|-----------|------------|
| `is_primary` | `phone` | Expression | `detail.new_phone if value else registrant.phone` |

## Security Configuration

### Access Groups

Change request types respect standard Odoo security:

**Group: Change Request Officer**
- Create change requests
- Submit for approval
- Edit draft requests

**Group: Change Request Approver**
- View pending requests
- Approve/reject/request revision
- View approval history

**Group: Change Request Administrator**
- Configure request types
- View all requests
- Manually apply requests
- Override approval workflows

### Record Rules

Configure record rules to restrict which requests users can see:

**Rule: Own Requests Only**
```python
[('create_uid', '=', user.id)]
```

**Rule: Requests for My Area**
```python
[('registrant_id.area_id', 'in', user.allowed_area_ids.ids)]
```

**Rule: Requests for My Program**
```python
[('registrant_id.program_ids', 'in', user.program_ids.ids)]
```

## Testing Your Configuration

### Step 1: Create Test Request

1. Log in as a **Change Request Officer**
2. Navigate to **Registry → Change Requests → New**
3. Select your new request type
4. Fill in all fields
5. **Submit for Approval**

### Step 2: Test Approval

1. Log in as a **Change Request Approver**
2. Open the pending request
3. Review the information
4. **Approve** the request

### Step 3: Verify Application

1. Open the registrant record
2. Check that the fields were updated correctly
3. Check the **Event Data** tab for audit trail

### Step 4: Test Rejection Flow

1. Create another test request
2. As approver, **Reject** it
3. Verify the registrant record was **not** updated

## Troubleshooting

### Request Type Not Appearing

**Problem:** Users don't see the new request type in the dropdown.

**Checks:**
- Has the request type been activated? (Click **Activate** button to change from Draft status)
- Does the user have the **Change Request Officer** group?
- Is **Target Type** compatible with the selected registrant (Individual vs Group/Household)?
- Is there a domain filter on the request type field?

### Apply Fails After Approval

**Problem:** Request is approved but changes don't apply to the registrant.

**Checks:**
- Is **Auto Apply On Approve** enabled in the Apply Configuration tab?
- Are the field mappings correct? Check source/target field names.
- Check Odoo logs for errors: `/var/log/odoo/odoo.log`
- Do the fields exist on the target model (`res.partner`)?
- Does the apply strategy model exist?

### Approval Workflow Not Triggering

**Problem:** Request stays in "Draft" after submission.

**Checks:**
- Is an **Approval Workflow** selected on the request type?
- Is the approval definition active?
- Are there approvers assigned to the approval groups?
- Check the **Approval Reviews** tab on the change request

### Missing Fields in Form

**Problem:** Detail form doesn't show expected fields.

**Checks:**
- Is the **Detail Form View** specified correctly?
- Were the fields added to the detail model?
- Is the form view's `model` attribute correct?
- Try clearing browser cache
- Check Studio's form view editor

### Document Validation Not Working

**Problem:** Users can submit without required documents.

**Checks:**
- Is **Document Validation Mode** set to "Required"?
- Are the **Required Document Types** selected?
- Do the document types exist in the system?
- Is the document field visible in the form?

## Are You Stuck?

**Want to add a field that doesn't exist in the detail model?**
Use Configurator V2 to add the field to the detail model, or ask a developer to add it via code. Then add a new apply mapping for the field.

**Need to map to a custom field on res.partner?**
Ensure the custom field exists first (via Configurator or custom module). Then add the mapping as normal.

**Apply strategy is too simple for your needs?**
You'll need a **custom apply strategy**. This requires Python code - see the developer guide or ask a developer to create one.

**Need to validate data before approval?**
Add validation logic to the detail model using `@api.constrains` decorators, or create a custom approval workflow with validation steps.

**Want different approval workflows based on field values?**
Use **conditional approval definitions** - configure multiple approval workflows and use a computed field on the change request to select the right one based on the detail values.

**Need to create requests programmatically?**
Use the API V2 endpoints (`/ChangeRequest`) or create records directly:

```python
detail = env['spp.cr.detail.edit_individual'].create({
    'given_name': 'John',
    'family_name': 'Doe',
    'phone': '+1234567890',
})

cr = env['spp.change.request'].create({
    'request_type_id': env.ref('spp_change_request_v2.cr_type_edit_individual').id,
    'registrant_id': registrant.id,
    'detail_res_id': detail.id,
    'source_type': 'api',
})

cr.action_submit()  # Submit for approval
```

## See Also

- {doc}`/config_guide/event_data/index` - Integrate change requests with event data collection
- {doc}`/developer_guide/api_v2/index` - Create change requests via REST API
- {doc}`/config_guide/studio/index` - Use Configurator V2 to create custom models
