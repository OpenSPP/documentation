---
openspp:
  doc_status: draft
---

# Model and Field Renames

This guide is for **developers** updating model and field references when migrating to OpenSPP V2.

## Overview

V2 renames all `g2p.*` models to `spp.*`. This affects:

- Model class names
- Database table names
- Field relations
- XML record references

## Core Model Renames

### Registry Models

| V1 Model | V2 Model | Description |
|----------|----------|-------------|
| `g2p.registrant` | `spp.registrant` | Base registrant (individual/group) |
| `g2p.reg.id` | `spp.reg.id` | Registrant ID numbers |
| `g2p.id.type` | `spp.id.type` | ID type configuration |
| `g2p.phone.number` | `spp.phone.number` | Phone numbers |
| `g2p.bank.details` | `spp.bank.details` | Banking information |

### Program Models

| V1 Model | V2 Model | Description |
|----------|----------|-------------|
| `g2p.program` | `spp.program` | Program definition |
| `g2p.program.cycle` | `spp.program.cycle` | Program cycle/period |
| `g2p.program.membership` | `spp.program.membership` | Beneficiary enrollment |
| `g2p.eligibility.manager` | `spp.eligibility.manager` | Eligibility configuration |
| `g2p.cycle.membership.manager` | `spp.cycle.membership.manager` | Enrollment manager |

### Entitlement Models

| V1 Model | V2 Model | Description |
|----------|----------|-------------|
| `g2p.entitlement` | `spp.entitlement` | Benefit entitlement |
| `g2p.entitlement.manager` | `spp.entitlement.manager` | Entitlement configuration |

### Payment Models

| V1 Model | V2 Model | Description |
|----------|----------|-------------|
| `g2p.payment` | `spp.payment` | Individual payment |
| `g2p.payment.batch` | `spp.payment.batch` | Payment batch |
| `g2p.payment.manager` | `spp.payment.manager` | Payment configuration |

## Update Model References

### In Python Model Definitions

```python
# Before (V1)
class CustomModel(models.Model):
    _name = "custom.model"

    registrant_id = fields.Many2one('g2p.registrant', string="Registrant")
    program_id = fields.Many2one('g2p.program', string="Program")
    entitlement_ids = fields.One2many('g2p.entitlement', 'partner_id')

# After (V2)
class CustomModel(models.Model):
    _name = "custom.model"

    registrant_id = fields.Many2one('spp.registrant', string="Registrant")
    program_id = fields.Many2one('spp.program', string="Program")
    entitlement_ids = fields.One2many('spp.entitlement', 'partner_id')
```

### In Python Code

```python
# Before (V1)
def create_program_membership(self):
    membership = self.env['g2p.program.membership'].create({
        'partner_id': self.registrant_id.id,
        'program_id': self.program_id.id,
    })
    return membership

# After (V2)
def create_program_membership(self):
    membership = self.env['spp.program.membership'].create({
        'partner_id': self.registrant_id.id,
        'program_id': self.program_id.id,
    })
    return membership
```

### In Domain Filters

```python
# Before (V1)
programs = self.env['g2p.program'].search([
    ('state', '=', 'active')
])

entitlements = self.env['g2p.entitlement'].search([
    ('partner_id', '=', partner.id),
    ('state', 'in', ['draft', 'approved'])
])

# After (V2)
programs = self.env['spp.program'].search([
    ('state', '=', 'active')
])

entitlements = self.env['spp.entitlement'].search([
    ('partner_id', '=', partner.id),
    ('state', 'in', ['draft', 'approved'])
])
```

## Update XML References

### In View Definitions

```xml
<!-- Before (V1) -->
<record id="view_g2p_program_form" model="ir.ui.view">
    <field name="name">g2p.program.form</field>
    <field name="model">g2p.program</field>
    <field name="arch" type="xml">
        <form>
            <field name="name"/>
            <field name="state"/>
        </form>
    </field>
</record>

<!-- After (V2) -->
<record id="view_spp_program_form" model="ir.ui.view">
    <field name="name">spp.program.form</field>
    <field name="model">spp.program</field>
    <field name="arch" type="xml">
        <form>
            <field name="name"/>
            <field name="state"/>
        </form>
    </field>
</record>
```

### In Action Definitions

```xml
<!-- Before (V1) -->
<record id="action_g2p_programs" model="ir.actions.act_window">
    <field name="name">Programs</field>
    <field name="res_model">g2p.program</field>
    <field name="view_mode">tree,form</field>
</record>

<!-- After (V2) -->
<record id="action_spp_programs" model="ir.actions.act_window">
    <field name="name">Programs</field>
    <field name="res_model">spp.program</field>
    <field name="view_mode">list,form</field>  <!-- Note: tree → list -->
</record>
```

### In Security Rules

```xml
<!-- Before (V1) -->
<record id="rule_g2p_program_user" model="ir.rule">
    <field name="name">Program User Access</field>
    <field name="model_id" ref="model_g2p_program"/>
    <field name="groups" eval="[(4, ref('group_g2p_user'))]"/>
    <field name="domain_force">[('state', '=', 'active')]</field>
</record>

<!-- After (V2) -->
<record id="rule_spp_program_user" model="ir.rule">
    <field name="name">Program User Access</field>
    <field name="model_id" ref="model_spp_program"/>
    <field name="groups" eval="[(4, ref('group_spp_user'))]"/>
    <field name="domain_force">[('state', '=', 'active')]</field>
</record>
```

## Database Table Renames

V2 migration scripts automatically rename database tables:

```sql
-- Automatic migration (DO NOT run manually)
ALTER TABLE g2p_program RENAME TO spp_program;
ALTER TABLE g2p_program_cycle RENAME TO spp_program_cycle;
ALTER TABLE g2p_program_membership RENAME TO spp_program_membership;
-- ... etc
```

**Note:** You don't need to run these manually. The migration scripts handle this.

## Custom Module Migration

If you have custom modules that extend OpenSPP models:

### Inherited Models

```python
# Before (V1)
class CustomProgram(models.Model):
    _inherit = 'g2p.program'

    custom_field = fields.Char("Custom Field")

# After (V2)
class CustomProgram(models.Model):
    _inherit = 'spp.program'

    custom_field = fields.Char("Custom Field")
```

### Related Fields

```python
# Before (V1)
class CustomModel(models.Model):
    _name = "custom.model"

    program_id = fields.Many2one('g2p.program')
    program_state = fields.Selection(related='program_id.state')
    cycle_id = fields.Many2one('g2p.program.cycle')

# After (V2)
class CustomModel(models.Model):
    _name = "custom.model"

    program_id = fields.Many2one('spp.program')
    program_state = fields.Selection(related='program_id.state')
    cycle_id = fields.Many2one('spp.program.cycle')
```

## Automated Search-Replace Script

```python
#!/usr/bin/env python3
"""
Replace model names in Python and XML files
Usage: python replace_models.py /path/to/module
"""

import re
from pathlib import Path

# Complete model rename mapping
MODEL_RENAMES = {
    # Registry models
    'g2p.registrant': 'spp.registrant',
    'g2p.reg.id': 'spp.reg.id',
    'g2p.id.type': 'spp.id.type',
    'g2p.phone.number': 'spp.phone.number',
    'g2p.bank.details': 'spp.bank.details',

    # Program models
    'g2p.program': 'spp.program',
    'g2p.program.cycle': 'spp.program.cycle',
    'g2p.program.membership': 'spp.program.membership',
    'g2p.eligibility.manager': 'spp.eligibility.manager',
    'g2p.cycle.membership.manager': 'spp.cycle.membership.manager',

    # Entitlement models
    'g2p.entitlement': 'spp.entitlement',
    'g2p.entitlement.manager': 'spp.entitlement.manager',

    # Payment models
    'g2p.payment': 'spp.payment',
    'g2p.payment.batch': 'spp.payment.batch',
    'g2p.payment.manager': 'spp.payment.manager',
}

def replace_in_file(file_path, replacements):
    """Replace model names in a file"""
    content = file_path.read_text()
    original = content

    for old, new in replacements.items():
        content = content.replace(old, new)

    if content != original:
        file_path.write_text(content)
        return True
    return False

def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python replace_models.py /path/to/module")
        sys.exit(1)

    module_path = Path(sys.argv[1])
    files = list(module_path.rglob("*.py")) + list(module_path.rglob("*.xml"))

    changed = 0
    for file_path in files:
        if replace_in_file(file_path, MODEL_RENAMES):
            print(f"✓ {file_path.relative_to(module_path)}")
            changed += 1

    print(f"\nUpdated {changed} files")

if __name__ == "__main__":
    main()
```

## Verification Checklist

After renaming models, verify:

```python
# tests/test_model_renames.py

from odoo.tests import TransactionCase

class TestModelRenames(TransactionCase):
    def test_all_models_exist(self):
        """Verify renamed models are accessible"""
        models_to_check = [
            'spp.registrant',
            'spp.program',
            'spp.program.cycle',
            'spp.entitlement',
            'spp.payment',
        ]

        for model_name in models_to_check:
            with self.subTest(model=model_name):
                model = self.env[model_name]
                self.assertTrue(model, f"Model {model_name} should exist")

    def test_relations_work(self):
        """Verify model relationships still work"""
        # Create test program
        program = self.env['spp.program'].create({
            'name': 'Test Program',
        })

        # Create cycle
        cycle = self.env['spp.program.cycle'].create({
            'program_id': program.id,
            'name': 'Test Cycle',
        })

        # Verify relationship
        self.assertEqual(cycle.program_id.id, program.id)
```

## Common Issues

### Issue: Model Not Found

```
ValueError: The model spp.program does not exist
```

**Cause:** Module with new model not installed

**Solution:** Install `spp_programs_base` module

### Issue: Field Reference Error

```
KeyError: 'Field g2p.program.custom_field does not exist'
```

**Cause:** Field references old model name

**Solution:** Update field definition to use `spp.program`

### Issue: Inheritance Error

```
ValueError: Model to inherit g2p.program does not exist
```

**Cause:** `_inherit` still references old model

**Solution:** Update `_inherit` to `spp.program`

## See Also

- {doc}`namespace_changes` - Module name changes
- {doc}`api_changes` - API endpoint changes
- {doc}`breaking_changes` - Odoo 19 compatibility
