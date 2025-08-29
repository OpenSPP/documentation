---
review-status: needs-review
review-date: 2025-06-04
reviewer: migration-script
migration-notes: "Added during 2025 documentation reorganization"
---

# Audit Logs

This article explains how the audit modules work in OpenSPP and how to customize them, using a practical example and a working sample module. The audit stack consists of `spp_audit_log` (core models and UI), `spp_audit_post` (optional chatter posting), and `spp_audit_config` (preconfigured rules).

**Core Models**

The audit stack provides core logging and optional posting with the following key components:
- `spp.audit.rule`: Configures what to log per model. Fields include `model_id`, `field_to_log_ids`, and toggles for `log_create`, `log_write`, `log_unlink`, plus `view_logs` to add a context action.
- `spp.audit.log`: Stores individual change entries including `audit_rule_id`, `user_id`, `model_id`, `res_id`, `method`, and formatted `data_html`.
- (From `spp_audit_post`) `spp.audit.rule` adds parent linking (`parent_id`, `child_ids`, `field_id`) and `spp.audit.log` adds `parent_model_id`, `parent_res_ids_str`, and `parent_data_html` for posting to parent records.

**Key Features**
- Dynamic method decoration on target models (`create`, `write`, `_write`, `unlink`) when a rule is created or updated
- Field-level selection via `field_to_log_ids` and automatic formatting for selections, relational fields, and datetime values
- Optional action menu "View logs" bound to the target model when `view_logs` is enabled
- Optional posting of audit messages to the target record or its parent model chatter (`spp_audit_post`)
- Preconfigured default rules installed via `spp_audit_config` (`data/audit_rule_data.xml`)

## Prerequisites

- Solid understanding of Odoo 17 module development, including Python, XML, and XPath.
- Ensure the following modules are installed: **SPP Audit Config**, **SPP Audit Log**, **SPP Audit Post** (optional).
- To set up OpenSPP for development, please refer to the {doc}`Development Setup Guide <../setup>`.

## Module Structure

A typical audit customization module follows the standard Odoo module structure. Here’s the structure for the example module, `spp_audit_log_custom`:

```
spp_audit_log_custom/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── spp_audit_rule.py
├── views/
│   └── spp_audit_rule_views.xml
├── security/
│   └── ir.model.access.csv
└── data/
    └── audit_rule_data.xml
```

## Step-by-Step Guide

In this example, we customize the audit rule to include an `active` flag, allowing rules to be enabled or disabled without deletion.

A working sample module is available at [this link](https://github.com/OpenSPP/documentation_code/tree/main/howto/developer_guides/customizations/spp_audit_log_custom).

### Create the Module Scaffold

Start by creating a new directory for your module (e.g., `spp_audit_log_custom`) and populate it
with the basic Odoo module files (`__init__.py`, `__manifest__.py`) and the directory structure shown above.

### Define Module Manifest

Create a manifest file with the correct dependencies and data files:

```python
{
    "name": "OpenSPP Audit Customizations",
    "summary": "Custom extensions for OpenSPP Audit",
    "category": "OpenSPP",
    "version": "17.0.1.0.0",
    "author": "Your Organization",
    "website": "https://your-website.com",
    "license": "LGPL-3",
    "depends": [
        "spp_audit_log",
        # "spp_audit_post",  # include if you extend or rely on chatter posting
    ],
    "data": [
        "views/spp_audit_rule_views.xml",
        # "security/ir.model.access.csv",  # not needed if you do not add new models
        # "data/audit_rule_data.xml",      # optional preconfigured rules
    ],
    "application": False,
    "installable": True,
    "auto_install": False,
}
```

### Extend the Audit Rule Model

Create `models/spp_audit_rule.py` and update `models/__init__.py`:

```python
from odoo import fields, models

class CustomAuditRule(models.Model):
    _inherit = "spp.audit.rule"

    active = fields.Boolean(
        default=True,
        help="If unchecked, the rule can be treated as inactive in your custom logic",
    )
```

### Create View Extensions

Create `views/spp_audit_rule_views.xml` and add it to the manifest:

```xml
<odoo>
    <record id="view_custom_audit_log_form" model="ir.ui.view">
        <field name="name">view_custom_audit_log_form</field>
        <field name="model">spp.audit.rule</field>
        <field name="inherit_id" ref="spp_audit_log.spp_audit_rule_form" />
        <field name="arch" type="xml">
            <xpath expr="//field[@name='name']" position="before">
                <field name="active" />
            </xpath>
        </field>
    </record>
</odoo>
```

### Add Security Access (Optional)

If you introduce new models, add access rights. For simple field additions, this is not required. Example:

```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_custom_spp_audit_rule,custom.spp.audit.rule,spp_audit_log.model_spp_audit_rule,base.group_system,1,1,1,0
```

- Group ID: **`g2p_registry_base.group_g2p_registrar`** for Registrar Access
- Group ID: **`g2p_registry_base.group_g2p_admin`** for Admin Access.

### Add Preconfigured Rules (Optional)

Seed rules using `data/audit_rule_data.xml` and the `spp.audit.rule.create_rules` helper:

```xml
<odoo>
    <data noupdate="1">
        <function model="spp.audit.rule" name="create_rules">
            <value name="rule_name">My Registry Rule</value>
            <value name="model">res.partner</value>
            <value name="fields_to_log" eval="['name', 'gender', 'birthdate']" />
            <value name="view_logs" eval="True" />
        </function>
    </data>
</odoo>
```

For parent/child rules (requires `spp_audit_post`), also pass `parent_rule_name` and `connecting_field_name`.

### Install and Test

1. Install or upgrade the module through the Apps menu.
2. Create or update records in the configured models (e.g., Individual or Group Registry).
3. Open **Audit Log → Audit → Log** to review entries.
4. On a specific record, use **Action → View logs** (if enabled) to see related entries.


## Best Practices

**Use Targeted Field Lists**: Keep `field_to_log_ids` focused on business-critical fields.

## References

For more information on extending OpenSPP modules, refer to:
- [Odoo 17 Developer Documentation](https://www.odoo.com/documentation/17.0/developer/)
- Audit module sources:
  - [`spp_audit_log`](https://github.com/OpenSPP/openspp-modules/tree/17.0/spp_audit_log)
  - [`spp_audit_post`](https://github.com/OpenSPP/openspp-modules/tree/17.0/spp_audit_post)
