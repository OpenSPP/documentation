---
openspp:
  doc_status: draft
  products: [core]
---

# Breaking Changes

This guide is for **developers** fixing Odoo 19 compatibility issues when migrating to OpenSPP V2.

## Overview

OpenSPP V2 upgrades from Odoo 17 to Odoo 19. This introduces **critical breaking changes** that require code updates.

## Critical: View Type Changes

### `<tree>` → `<list>` (BLOCKS MODULE INSTALLATION)

**Impact:** HIGH - Affects virtually every module
**Effort:** Medium - Automated replacement possible

**The Problem:**

```python
ParseError: Invalid view type: 'tree'.
Allowed types are: list, form, graph, pivot, calendar, kanban, search, qweb, activity
```

**Fix Required:**

```xml
<!-- Before (Odoo 17) -->
<record id="view_program_tree" model="ir.ui.view">
    <field name="model">spp.program</field>
    <field name="arch" type="xml">
        <tree string="Programs">
            <field name="name"/>
            <field name="state"/>
        </tree>
    </field>
</record>

<!-- After (Odoo 19) -->
<record id="view_program_list" model="ir.ui.view">
    <field name="model">spp.program</field>
    <field name="arch" type="xml">
        <list string="Programs">
            <field name="name"/>
            <field name="state"/>
        </list>
    </field>
</record>
```

**Automated Fix:**

```bash
# Replace all <tree> with <list> in XML files
find . -name "*.xml" -exec sed -i 's/<tree/<list/g' {} \;
find . -name "*.xml" -exec sed -i 's/<\/tree>/<\/list>/g' {} \;

# Also update in action view_mode
find . -name "*.xml" -exec sed -i 's/view_mode>tree,/view_mode>list,/g' {} \;
find . -name "*.xml" -exec sed -i 's/view_mode>tree</view_mode>list</g' {} \;
```

**Also update in Python:**

```python
# Before (Odoo 17)
return {
    'type': 'ir.actions.act_window',
    'res_model': 'spp.program',
    'view_mode': 'tree,form',
}

# After (Odoo 19)
return {
    'type': 'ir.actions.act_window',
    'res_model': 'spp.program',
    'view_mode': 'list,form',  # tree → list
}
```

## Critical: Security Group Changes

### `category_id` Removed from `res.groups`

**Impact:** HIGH - Blocks module installation
**Effort:** Low - Simple deletion

**The Problem:**

```python
ValueError: Invalid field 'category_id' in 'res.groups'
```

**Fix Required:**

```xml
<!-- Before (Odoo 17) -->
<record id="group_spp_admin" model="res.groups">
    <field name="name">Administrator</field>
    <field name="category_id" ref="module_category_openspp"/>  <!-- REMOVE THIS -->
</record>

<!-- After (Odoo 19) -->
<record id="group_spp_admin" model="res.groups">
    <field name="name">Administrator</field>
    <!-- category_id removed - not needed in Odoo 19 -->
</record>
```

**Automated Fix:**

```bash
# Remove all category_id lines from security XML
find . -name "*.xml" -exec sed -i '/<field name="category_id"/d' {} \;
```

### `users` Field Removed from `res.groups`

**Impact:** MEDIUM - Blocks some modules
**Effort:** Low - Remove field assignments

**The Problem:**

```python
ValueError: Invalid field 'users' in 'res.groups'
```

**Fix Required:**

```xml
<!-- Before (Odoo 17) -->
<record id="group_spp_admin" model="res.groups">
    <field name="name">Administrator</field>
    <field name="users" eval="[(4, ref('base.user_admin'))]"/>  <!-- REMOVE -->
</record>

<!-- After (Odoo 19) -->
<record id="group_spp_admin" model="res.groups">
    <field name="name">Administrator</field>
    <!-- Assign users via user records instead -->
</record>
```

**Assign users differently:**

```xml
<!-- Odoo 19 way: Update user records -->
<record id="base.user_admin" model="res.users">
    <field name="groups_id" eval="[(4, ref('group_spp_admin'))]"/>
</record>
```

## Critical: Menu Access Changes

### `groups_id` / `groups` Removed from `ir.ui.menu`

**Impact:** MEDIUM - Affects menu visibility
**Effort:** Medium - Requires rethinking access control

**The Problem:**

```python
ValueError: Invalid field 'groups_id' in 'ir.ui.menu'
# or
ValueError: Invalid field 'groups' in 'ir.ui.menu'
```

**Fix Required:**

```xml
<!-- Before (Odoo 17) -->
<menuitem
    id="menu_programs"
    name="Programs"
    action="action_programs"
    groups="group_spp_user,group_spp_admin"/>  <!-- REMOVE -->

<!-- After (Odoo 19) -->
<menuitem
    id="menu_programs"
    name="Programs"
    action="action_programs"/>
    <!-- Access control via action/model rules instead -->
```

**Alternative:** Control access via action security:

```xml
<!-- Use ir.rule or ir.model.access instead -->
<record id="rule_program_user" model="ir.rule">
    <field name="name">Program User Access</field>
    <field name="model_id" ref="model_spp_program"/>
    <field name="groups" eval="[(4, ref('group_spp_user'))]"/>
    <field name="domain_force">[(1, '=', 1)]</field>
</record>
```

## Python Import Changes

### `odoo.osv` Deprecated

**Impact:** MEDIUM - Produces warnings
**Effort:** Low - Simple import change

**The Problem:**

```python
DeprecationWarning: Since 19.0, odoo.osv is deprecated use odoo.fields.Domain
```

**Fix Required:**

```python
# Before (Odoo 17)
from odoo.osv.expression import OR, AND

domain = OR([domain1, domain2])

# After (Odoo 19)
from odoo.osv import expression  # Keep for expression functions

domain = expression.OR([domain1, domain2])

# OR use tools
from odoo.tools import domain as domain_tools
domain = domain_tools.OR([domain1, domain2])
```

## Command API Changes

### Many2many Command Format

**Impact:** LOW - Only if using old format
**Effort:** Low - Update to Command class

**Updated approach (Odoo 19):**

```python
# Before (Odoo 17) - Numeric tuples still work but deprecated
vals = {
    'group_ids': [(4, group_id), (4, another_id)]
}

# After (Odoo 19) - Use Command class (preferred)
from odoo import Command

vals = {
    'group_ids': [
        Command.link(group_id),
        Command.link(another_id)
    ]
}

# Other Command operations
Command.create(vals_dict)  # (0, 0, vals)
Command.update(id, vals)   # (1, id, vals)
Command.delete(id)         # (2, id)
Command.unlink(id)         # (3, id)
Command.link(id)           # (4, id)
Command.clear()            # (5,)
Command.set(ids_list)      # (6, 0, ids)
```

## Constraint Changes

### SQL Constraints Must Have Unique Names

**Impact:** LOW - Only affects modules with duplicate constraint names
**Effort:** Low - Rename constraints

**The Problem:**

```python
psycopg2.errors.DuplicateObject: constraint "unique_name" already exists
```

**Fix Required:**

```python
# Before (Odoo 17) - Same name in multiple models
class Model1(models.Model):
    _name = "model.one"
    _sql_constraints = [
        ('unique_name', 'unique(name)', 'Name must be unique')
    ]

class Model2(models.Model):
    _name = "model.two"
    _sql_constraints = [
        ('unique_name', 'unique(name)', 'Name must be unique')  # Duplicate!
    ]

# After (Odoo 19) - Unique names per model
class Model1(models.Model):
    _name = "model.one"
    _sql_constraints = [
        ('model_one_unique_name', 'unique(name)', 'Name must be unique')
    ]

class Model2(models.Model):
    _name = "model.two"
    _sql_constraints = [
        ('model_two_unique_name', 'unique(name)', 'Name must be unique')
    ]
```

## XML Data Changes

### `eval` Attribute Changes

**Impact:** LOW - Only specific eval patterns
**Effort:** Low - Update eval expressions

**Some eval patterns changed:**

```xml
<!-- Before (Odoo 17) -->
<field name="date" eval="datetime.now()"/>

<!-- After (Odoo 19) - Use time module -->
<field name="date" eval="time.strftime('%Y-%m-%d')"/>
```

## Testing Changes

### Test Decorators

**No major changes, but best practices updated:**

```python
# Odoo 19 best practices
from odoo.tests import TransactionCase, tagged

@tagged('post_install', '-at_install')
class TestProgram(TransactionCase):
    def test_program_creation(self):
        program = self.env['spp.program'].create({
            'name': 'Test Program'
        })
        self.assertTrue(program.exists())
```

## Migration Checklist

After updating code, verify:

### 1. XML Views

```bash
# Check for remaining <tree> tags
grep -r "<tree" --include="*.xml" .

# Should return no results in view definitions
```

### 2. Security Files

```bash
# Check for category_id
grep -r "category_id" --include="*.xml" .

# Check for users in groups
grep -r '<field name="users"' --include="*.xml" .

# Check for groups in menus
grep -r 'menuitem.*groups=' --include="*.xml" .
```

### 3. Python Imports

```bash
# Check for old osv imports
grep -r "from odoo.osv.expression import" --include="*.py" .
```

## Automated Migration Script

Complete script to fix all breaking changes:

```python
#!/usr/bin/env python3
"""
Fix Odoo 19 breaking changes
Usage: python fix_odoo19.py /path/to/module
"""

import re
from pathlib import Path

def fix_tree_to_list(content):
    """Replace <tree> with <list>"""
    content = re.sub(r'<tree(\s|>)', r'<list\1', content)
    content = re.sub(r'</tree>', r'</list>', content)
    content = re.sub(r"view_mode>tree,", r"view_mode>list,", content)
    content = re.sub(r"view_mode>tree<", r"view_mode>list<", content)
    return content

def fix_security_groups(content):
    """Remove category_id and users from groups"""
    # Remove category_id lines
    content = re.sub(r'\s*<field name="category_id"[^>]*/>.*\n', '', content)

    # Remove users field lines
    content = re.sub(r'\s*<field name="users"[^>]*/>.*\n', '', content)

    return content

def fix_menu_groups(content):
    """Remove groups from menuitem"""
    content = re.sub(r'\s+groups="[^"]*"', '', content, flags=re.MULTILINE)
    return content

def fix_osv_imports(content):
    """Update osv imports"""
    # Replace direct OR/AND imports
    content = re.sub(
        r'from odoo\.osv\.expression import (OR|AND)',
        r'from odoo.osv import expression',
        content
    )

    # Update usage if simple OR/AND
    content = re.sub(r'\bOR\(', r'expression.OR(', content)
    content = re.sub(r'\bAND\(', r'expression.AND(', content)

    return content

def process_xml_file(file_path):
    """Process XML file"""
    content = file_path.read_text()
    original = content

    content = fix_tree_to_list(content)
    content = fix_security_groups(content)
    content = fix_menu_groups(content)

    if content != original:
        file_path.write_text(content)
        return True
    return False

def process_py_file(file_path):
    """Process Python file"""
    content = file_path.read_text()
    original = content

    content = fix_osv_imports(content)

    if content != original:
        file_path.write_text(content)
        return True
    return False

def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python fix_odoo19.py /path/to/module")
        sys.exit(1)

    module_path = Path(sys.argv[1])

    # Process XML files
    xml_changed = 0
    for xml_file in module_path.rglob("*.xml"):
        if process_xml_file(xml_file):
            print(f"✓ XML: {xml_file.relative_to(module_path)}")
            xml_changed += 1

    # Process Python files
    py_changed = 0
    for py_file in module_path.rglob("*.py"):
        if process_py_file(py_file):
            print(f"✓ PY:  {py_file.relative_to(module_path)}")
            py_changed += 1

    print(f"\nFixed {xml_changed} XML files and {py_changed} Python files")

if __name__ == "__main__":
    main()
```

## Common Error Messages

### Error: Invalid view type 'tree'

```
ParseError: Invalid view type: 'tree'
```

**Solution:** Replace `<tree>` with `<list>` in view definitions

### Error: Invalid field 'category_id'

```
ValueError: Invalid field 'category_id' in 'res.groups'
```

**Solution:** Remove `<field name="category_id"/>` from group records

### Error: Invalid field 'groups'

```
ValueError: Invalid field 'groups' in 'ir.ui.menu'
```

**Solution:** Remove `groups=` attribute from menuitem tags

### Warning: odoo.osv deprecated

```
DeprecationWarning: Since 19.0, odoo.osv is deprecated
```

**Solution:** Update imports to use `odoo.osv.expression` or `odoo.tools.domain`

## Testing After Fixes

```python
# tests/test_odoo19_compat.py

from odoo.tests import TransactionCase

class TestOdoo19Compatibility(TransactionCase):
    def test_module_installs(self):
        """Verify module installs without errors"""
        # Your module should install cleanly
        pass

    def test_views_load(self):
        """Verify all views load correctly"""
        views = self.env['ir.ui.view'].search([
            ('model', 'like', 'spp.%')
        ])
        for view in views:
            # Should not raise ParseError
            view._check_xml()

    def test_no_tree_views(self):
        """Verify no tree views remain"""
        tree_views = self.env['ir.ui.view'].search([
            ('type', '=', 'tree')
        ])
        self.assertEqual(len(tree_views), 0, "All tree views should be list views")
```

## See Also

- {doc}`namespace_changes` - g2p to spp migration
- {doc}`model_renames` - Model reference updates
- [Odoo 19 Official Migration Guide](https://www.odoo.com/documentation/19.0/developer/howtos/upgrade.html)
- [Odoo 19 Release Notes](https://www.odoo.com/odoo-19)
