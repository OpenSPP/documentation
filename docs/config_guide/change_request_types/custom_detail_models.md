---
openspp:
  doc_status: draft
  products: [core]
---

# Custom detail models

When the pre-built detail models don't meet your requirements, you can create custom detail models to capture specific fields for your change request types.

## When to create custom models

Create a custom detail model when you need to:

- Capture fields not in existing models
- Add custom validation logic
- Create specialized forms for specific workflows
- Collect program-specific information

## Using Studio (recommended)

OpenSPP Studio provides a no-code interface for creating custom detail models.

![Studio Dashboard](/_images/en-us/config_guide/studio/change_request_builder/01-studio-dashboard.png)

### Step 1: Create the model

1. Navigate to **Studio → Models → New**
2. Configure the model:

| Field | Value |
|-------|-------|
| Name | CR Detail: Update Phone |
| Technical Name | `spp.cr.detail.update_phone` |
| Inherit | `spp.cr.detail.base` |

```{important}
Always inherit from `spp.cr.detail.base` to get required fields and functionality.
```

### Step 2: Add fields

Add the fields you need to collect:

| Field Name | Type | Widget | Required |
|------------|------|--------|----------|
| `new_phone` | Char | Phone | Yes |
| `phone_type` | Selection | Selection | No |
| `is_primary` | Boolean | Checkbox | No |
| `verification_code` | Char | Text | No |

### Step 3: Configure selection options

For selection fields like `phone_type`, add the options:

| Value | Label |
|-------|-------|
| `mobile` | Mobile |
| `landline` | Landline |
| `work` | Work |

### Step 4: Generate the form view

Use Studio's view builder to create a user-friendly form:

1. Click **Generate View**
2. Arrange fields in logical groups
3. Add labels and help text
4. Preview the form

### Step 5: Activate the model

Click **Activate** to make the model available for use in change request types.

![Draft state with Activate button](/_images/en-us/config_guide/studio/change_request_builder/09-draft-state-activate-button.png)

## Using code (for developers)

For more control or complex logic, create the detail model in Python code.

### Create the model

Create a file `spp_cr_custom/models/detail_update_phone.py`:

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

### Create the form view

Create `spp_cr_custom/views/detail_update_phone_views.xml`:

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

### Add security rules

Create `spp_cr_custom/security/ir.model.access.csv`:

```text
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_spp_cr_detail_update_phone_user,spp.cr.detail.update_phone.user,model_spp_cr_detail_update_phone,spp_change_request_v2.group_cr_user,1,1,1,0
access_spp_cr_detail_update_phone_manager,spp.cr.detail.update_phone.manager,model_spp_cr_detail_update_phone,spp_change_request_v2.group_cr_manager,1,1,1,1
```

### Update module files

Add the new files to your module's `__init__.py` and `__manifest__.py`.

## Base model fields

When inheriting from `spp.cr.detail.base`, your model automatically gets:

| Field | Type | Description |
|-------|------|-------------|
| `registrant_id` | Many2one | Link to the target registrant |
| `change_request_id` | Many2one | Link to the parent change request |
| `approval_state` | Selection | Current approval state |
| `create_uid` | Many2one | User who created the request |
| `create_date` | Datetime | When the request was created |

## Adding validation

### Using constraints

Add validation using `@api.constrains`:

```python
@api.constrains('new_phone')
def _check_phone_format(self):
    for rec in self:
        if rec.new_phone:
            # Remove formatting
            digits = rec.new_phone.replace('+', '').replace(' ', '').replace('-', '')
            if not digits.isdigit():
                raise ValidationError("Phone number must contain only digits")
            if len(digits) < 10:
                raise ValidationError("Phone number must be at least 10 digits")
```

### Using onchange

Add real-time validation using `@api.onchange`:

```python
@api.onchange('birthdate')
def _onchange_birthdate(self):
    if self.birthdate and self.birthdate > date.today():
        return {
            'warning': {
                'title': 'Invalid Date',
                'message': 'Birth date cannot be in the future'
            }
        }
```

## Linking to change request type

After creating your custom detail model:

1. Go to **Change Requests → Configuration → Change Request Types**
2. Create or edit a change request type
3. In the **Detail Model** tab, enter your model name (e.g., `spp.cr.detail.update_phone`)
4. Optionally select a specific form view
5. Configure field mappings in the **Apply Configuration** tab

## Best practices

1. **Follow naming conventions** - Use `spp.cr.detail.<purpose>` for model names
2. **Inherit the base** - Always inherit from `spp.cr.detail.base`
3. **Add validation** - Validate data before submission
4. **Create clear forms** - Group related fields, add help text
5. **Test thoroughly** - Test the full workflow before deploying

## See also

- {doc}`creating_types` - Basic configuration steps
- {doc}`field_mappings` - Configure how fields are applied
- {doc}`../studio/change_request_builder` - Studio interface for creating CR types
