---
review-status: needs-review
review-date: 2025-08-12
reviewer: migration-script
migration-notes: "Added during 2025 documentation reorganization"
---

# Customize Change Request

The OpenSPP platform provides a flexible and extensible Change Request (CR) framework. This allows developers
to create custom modules for specific data modification scenarios beyond the standard ones. This guide will
walk you through the process of creating a new Change Request Type module, using the
`spp_change_request_add_children_demo` module as a practical reference.

By the end of this guide, you will be able to:

- Structure a new Change Request module.
- Define a custom model to hold CR-specific data.
- Implement validation and data update logic.
- Create the necessary user interface (views and menus).
- Configure validation workflows and security.

## Prerequisites

- Solid understanding of Odoo 17 module development.
- Knowledge of Python, Odoo, XML, Xpaths.
- Familiarity with the OpenSPP core modules, especially `OpenSPP Change Request` (`spp_change_request`).
- To set up OpenSPP for development, please refer to the [Developer Guide](https://docs.openspp.org/howto/developer_guides/development_setup.html)

## Module Structure

A typical Change Request Type module follows the standard Odoo module structure. Here's the structure of our
reference module, `spp_change_request_add_children_demo`:

```
spp_change_request_add_children_demo/
├── __init__.py
├── __manifest__.py
├── data/
│   ├── spp_change_request_validation_sequence_data.xml
│   └── spp_dms_category_data.xml
├── models/
│   ├── __init__.py
│   └── change_request_add_children.py
├── security/
│   └── ir.model.access.csv
├── tests/
│   ├── __init__.py
│   └── test_create_cr.py
└── views/
    ├── change_request_add_children_views.xml
    └── menus.xml
```

---

## Step-by-Step Guide

### Step 1: Create the Module Scaffold

Start by creating a new directory for your module (e.g., `spp_change_request_custom_type`) and populate it
with the basic Odoo module files (`__init__.py`, `__manifest__.py`) and the directory structure shown above.

### Step 2: Define the Manifest (`__manifest__.py`)

The manifest file declares your module's metadata and dependencies. It's crucial to list all the modules your
CR type will interact with. For our "Add Child/Member" example, the dependencies are:

```python
# __manifest__.py
{
    "name": "OpenSPP Change Request Demo: Add Child/Member",
    "summary": "This module is a demo for creating a new change request type for adding children/members to a group.",
    "version": "17.0.1.0.0",
    "category": "OpenSPP/Change Request",
    "author": "OpenSPP",
    "website": "https://openspp.org",
    "license": "LGPL-3",
    "depends": [
        "spp_change_request",
        "g2p_registry_group",
        "g2p_registry_individual",
        "g2p_registry_membership",
        "spp_service_points",
        "phone_validation",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/spp_dms_category_data.xml",
        "data/spp_change_request_validation_sequence_data.xml",
        "views/change_request_add_children_views.xml",
        "views/menus.xml",
    ],
    "installable": True,
    "auto_install": False,
}
```

Your dependencies will vary based on the data you need to access and modify.

### Step 3: Create the Change Request Models

This is the heart of your module. You'll create a new model that holds the specific data for your change
request type.

1.  **Create the model file**: In your `models/` directory, create a Python file (e.g.,
    `models/change_request_custom.py`).

2.  **Define the model**:

    - The model name (`_name`) should be descriptive, like `spp.change.request.add.children`.
    - Inherit from `spp.change.request.source.mixin` and `spp.change.request.validation.sequence.mixin`. These
      mixins provide the core logic for state management, validation, and applying changes.
    - Define the fields required to capture the information for the change.

    ```python
    # From: spp_change_request_add_children_demo/models/change_request_add_children.py

    from odoo import _, api, fields, models from odoo.exceptions import ValidationError

    class ChangeRequestAddChildren(models.Model):
        _name = "spp.change.request.add.children"
        _inherit = [
            "spp.change.request.source.mixin",
            "spp.change.request.validation.sequence.mixin",
        ]
        _description = "Add Child/Member Change Request Type"

        # Constants for validation form and required documents
        VALIDATION_FORM = "spp_change_request_add_children_demo.view_change_request_add_children_validation_form"
        REQUIRED_DOCUMENT_TYPE = [
            "spp_change_request_add_children_demo.spp_dms_add_children",
        ]

        registrant_id = fields.Many2one(
            "res.partner",
            "Add to Group",
            domain=[("is_registrant", "=", True), ("is_group", "=", True)],
        )

        # Fields specific to this CR type
        family_name = fields.Char()
        given_name = fields.Char()
        birthdate = fields.Date("Date of Birth")
        gender = fields.Many2one("gender.type")
        # ... other fields
    ```

3.  **Implement `validate_data()`**: Override this method to add custom validation logic. This method is
    called before the request is submitted for approval. Raise a `ValidationError` if the data is invalid.

    ```python
    # From: spp_change_request_add_children_demo/models/change_request_add_children.py

    def validate_data(self):
        super().validate_data() # Checks for required documents
        error_message = []
        if not self.family_name:
            error_message.append(_("The Family Name is required!"))
        if not self.given_name:
            error_message.append(_("The First Name is required!"))
        # ... more checks
        if error_message:
            raise ValidationError("\n".join(error_message))
        return
    ```

4.  **Implement `update_live_data()`**: Override this method to define how the system's data should be
    modified once the CR is approved and applied. This is where you create or update records.

    ```python
    # From: spp_change_request_add_children_demo/models/change_request_add_children.py

    def update_live_data(self):
        self.ensure_one()
        # Create a new individual (res.partner)
        individual_id = self.env["res.partner"].create(
            {
                "is_registrant": True,
                "is_group": False,
                "name": self.full_name,
                "family_name": self.family_name,
                "given_name": self.given_name,
                # ... other fields from the CR form
            }
        )
        # Add the new individual to the group
        self.env["g2p.group.membership"].create(
            {
                "group": self.registrant_id.id,
                "individual": individual_id.id,
                # ... other membership details
            }
        )
    ```

5.  **Register the New Request Type**: You need to make the system aware of your new CR type. Inherit the base
    `spp.change.request` model and extend the `_selection_request_type_ref_id` method. This adds your new type
    to the dropdown list when creating a new CR.

    ```python
    # From: spp_change_request_add_children_demo/models/change_request_add_children.py

    class ChangeRequestTypeCustomAddChildren(models.Model):
        _inherit = "spp.change.request"

        # If the CR type applies only to a specific registrant type (e.g., Group),
        # you can override the domain.
        registrant_id = fields.Many2one(
            "res.partner",
            "Registrant",
            domain=[("is_registrant", "=", True), ("is_group", "=", True)],
        )

        @api.model
        def _selection_request_type_ref_id(self):
            selection = super()._selection_request_type_ref_id()
            new_request_type = ("spp.change.request.add.children", "Add Child/Member")
            if new_request_type not in selection:
                selection.append(new_request_type)
            return selection
    ```

### Step 4: Create the User Interface (Views)

Define the form view for your custom CR type.

1.  **Create the view file**: In your `views/` directory, create an XML file (e.g.,
    `views/change_request_custom_views.xml`).

2.  **Define the form view**: - The view record's `model` should be your new CR model
    (`spp.change.request.add.children`). - Structure the form with a `header` for status and buttons, and a
    `sheet` for the data fields. - Use Odoo's XML view syntax to lay out your fields.

    ```xml
    <!-- From: spp_change_request_add_children_demo/views/change_request_add_children_views.xml -->
    <record id="view_change_request_add_children_form" model="ir.ui.view">
        <field name="name">spp.change.request.add.children.form</field>
        <field name="model">spp.change.request.add.children</field>
        <field name="arch" type="xml">
            <form>
                <header>
                    <!-- Buttons for actions like submit, validate, apply -->
                    <!-- prettier-ignore-start -->
                    <button
                        name="action_submit"
                        string="Submit"
                        type="object"
                        class="oe_highlight"
                        data-hotkey="s"
                        invisible="state != 'draft'"
                    />
                    <button
                        name="action_validate"
                        string="Validate"
                        type="object"
                        class="oe_highlight"
                        data-hotkey="v"
                        invisible="state != 'pending'"
                    />
                    <!-- ... other buttons -->
                    <field
                        name="state"
                        widget="statusbar"
                        statusbar_visible="draft,pending,validated,applied"
                    />
                    <!-- prettier-ignore-end -->
                </header>
                <sheet>
                    <group>
                        <group>
                            <field name="registrant_id" />
                            <field name="applicant_id" />
                        </group>
                        <!-- ... other groups and fields -->
                    </group>
                    <notebook>
                        <page string="Child Information">
                            <group>
                                <field name="family_name" />
                                <field name="given_name" />
                                <field name="birthdate" />
                                <!-- ... -->
                            </group>
                        </page>
                        <!-- ... other pages for documents, etc. -->
                    </notebook>
                </sheet>
            </form>
        </field>
    </record>
    ```

3.  **Create Menu Items**: Add a menu item so users can create new instances of your CR type.

    ```xml
    <!-- From: spp_change_request_add_children_demo/views/menus.xml -->
    <record id="action_change_request_add_children" model="ir.actions.act_window">
        <field name="name">Add Child/Member</field>
        <field name="res_model">spp.change.request</field>
        <field name="view_mode">tree,form</field>
        <field name="context">{'default_request_type': 'spp.change.request.add.children'}</field>
        <field name="domain">[('request_type', '=', 'spp.change.request.add.children')]</field>
    </record>

    <menuitem
        id="menu_change_request_add_children"
        name="Add Child/Member"
        parent="spp_change_request.menu_change_request_root"
        action="action_change_request_add_children"
        sequence="10"/>
    ```

### Step 5: Define Data Files

Use XML data files to configure aspects of your CR type.

- **Validation Sequence**: In `data/spp_change_request_validation_sequence_data.xml`, define the approval
  steps. Each record links your `request_type`, a validation `stage_id`, and the `validation_group_id` (a
  `res.groups` record) responsible for that stage.

  ```xml
  <!-- From: spp_change_request_add_children_demo/data/spp_change_request_validation_sequence_data.xml -->
  <odoo>
      <data noupdate="1">
          <record id="add_children_validation_sequence_1" model="spp.change.request.validation.sequence">
              <field name="sequence">1</field>
              <field name="request_type">spp.change.request.add.children</field>
              <field name="stage_id" ref="spp_change_request.validation_stage_local" />
              <field
          name="validation_group_id"
          ref="spp_change_request.group_spp_change_request_local_validator"
        />
          </record>
          <record id="add_children_validation_sequence_2" model="spp.change.request.validation.sequence">
              <field name="sequence">2</field>
              <field name="request_type">spp.change.request.add.children</field>
              <field name="stage_id" ref="spp_change_request.validation_stage_hq" />
              <field
          name="validation_group_id"
          ref="spp_change_request.group_spp_change_request_hq_validator"
        />
          </record>
      </data>
  </odoo>
  ```

- **DMS Categories**: In `data/spp_dms_category_data.xml`, define any specific document categories required
  for your CR.

  ```xml
  <!-- From: spp_change_request_add_children_demo/data/spp_dms_category_data.xml -->
  <odoo>
      <data noupdate="1">
          <record id="spp_dms_add_children" model="spp.dms.category">
              <field name="name">Add Children Request Form</field>
          </record>
      </data>
  </odoo>
  ```

### Step 6: Set Up Security

Grant users access to your new model in security/ir.model.access.csv. At a minimum, you need to provide access
to the base user group.

```csv
# From: spp_change_request_add_children_demo/security/ir.model.access.csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_spp_change_request_add_children_user,spp.change.request.add.children.user,model_spp_change_request_add_children,base.group_user,1,1,1,1
```

### Step 7: Install and Test

1. Install or upgrade the module through the Apps menu.
2. Create a new change request.
3. Check if the new change request type is in the selection field.

## Best Practices

- Always start with a clear definition of the data you need to collect and the system changes that need to occur upon approval.

For more detailed guidelines, refer to the [Best Practices](../best_practices.md) page.

## References

For more information on extending Odoo models and views, refer to:
- [Odoo 17 Developer Documentation](https://www.odoo.com/documentation/17.0/developer/)
- [OpenSPP Development Guidelines](https://docs.openspp.org/)
- [Change Request Module Source](https://github.com/OpenSPP/openspp-modules/tree/17.0/spp_change_request)
