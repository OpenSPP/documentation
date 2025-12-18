---
openspp:
  doc_status: draft
---

# Namespace Changes (g2p.* → spp.*)

This guide is for **developers** migrating code from the `g2p.*` namespace to `spp.*` namespace in OpenSPP V2.

## Overview

OpenSPP V2 renames all `g2p.*` modules and models to `spp.*` for clarity and ownership:

- **Module names**: `g2p_*` → `spp_*`
- **Model names**: `g2p.*` → `spp.*`
- **XML IDs**: `g2p_*` → `spp_*`

This change affects **all** G2P-derived modules in the OpenSPP codebase.

## Module Name Changes

### Core Registry Modules

| V1 Module | V2 Module | Notes |
|-----------|-----------|-------|
| `g2p_registry_base` | `spp_registry_base` | Consolidated from 4 modules |
| `g2p_registry_individual` | `spp_registry_base` | Merged into base |
| `g2p_registry_group` | `spp_registry_base` | Merged into base |
| `g2p_registry_membership` | `spp_registry_base` | Merged into base |

### Program Modules

| V1 Module | V2 Module | Notes |
|-----------|-----------|-------|
| `g2p_programs` | `spp_programs_base` | Renamed |
| `g2p_program_assessment` | `spp_program_assessment` | Namespace change only |
| `g2p_program_approval` | `spp_program_approval` | Namespace change only |
| `g2p_program_cycleless` | `spp_program_cycleless` | Namespace change only |

### Payment & Banking Modules

| V1 Module | V2 Module | Notes |
|-----------|-----------|-------|
| `g2p_bank` | `spp_banking` | Renamed |
| `g2p_payment_interop_layer` | `spp_payment_interop_layer` | Namespace change only |
| `g2p_payment_phee` | `spp_payment_phee` | Namespace change only |

### Security & Credentials

| V1 Module | V2 Module | Notes |
|-----------|-----------|-------|
| `g2p_encryption` | `spp_encryption` | Namespace change only |
| `g2p_openid_vci` | `spp_credentials` | Renamed for clarity |
| `g2p_openid_vci_rest_api` | `spp_credentials_rest_api` | Renamed |

### Other Modules

| V1 Module | V2 Module | Notes |
|-----------|-----------|-------|
| `g2p_entitlement_in_kind` | `spp_entitlement_in_kind` | Namespace change only |

## Update Module Dependencies

### In `__manifest__.py`

```python
# Before (V1)
{
    'name': 'Custom Farmer Module',
    'version': '17.0.1.0.0',
    'depends': [
        'g2p_registry_base',
        'g2p_registry_individual',
        'g2p_programs',
        'g2p_bank',
    ],
}

# After (V2)
{
    'name': 'Custom Farmer Module',
    'version': '19.0.1.0.0',  # Note Odoo version change
    'depends': [
        'spp_registry_base',  # Individual/group merged in
        'spp_programs_base',   # Note: _base suffix
        'spp_banking',         # Note: different name
    ],
}
```

### Consolidated Modules

Several registry modules were consolidated. Update dependencies:

```python
# Before (V1) - Multiple dependencies
'depends': [
    'g2p_registry_base',
    'g2p_registry_individual',
    'g2p_registry_group',
]

# After (V2) - Single dependency
'depends': [
    'spp_registry_base',  # Contains all registry functionality
]
```

## Update Import Statements

### Python Imports

No changes needed for Python imports - models are referenced by string name:

```python
# Both V1 and V2 use the same pattern
self.env['spp.program']  # Model string changes, not imports
```

### XML External IDs

Update all external ID references:

```python
# Before (V1)
<field name="ref" eval="ref('g2p_registry_base.group_g2p_admin')" />
<field name="model_id" ref="g2p_programs.model_g2p_program" />

# After (V2)
<field name="ref" eval="ref('spp_registry_base.group_spp_admin')" />
<field name="model_id" ref="spp_programs_base.model_spp_program" />
```

## Update Model References

### In Python Code

```python
# Before (V1)
registrant = self.env['g2p.registrant'].search([])
program = self.env['g2p.program'].browse(program_id)
entitlement = self.env['g2p.entitlement'].create(vals)

# After (V2)
registrant = self.env['spp.registrant'].search([])
program = self.env['spp.program'].browse(program_id)
entitlement = self.env['spp.entitlement'].create(vals)
```

### In XML Views

```xml
<!-- Before (V1) -->
<record id="view_g2p_program_form" model="ir.ui.view">
    <field name="model">g2p.program</field>
    <field name="arch" type="xml">
        <form>
            <!-- form content -->
        </form>
    </field>
</record>

<!-- After (V2) -->
<record id="view_spp_program_form" model="ir.ui.view">
    <field name="model">spp.program</field>
    <field name="arch" type="xml">
        <form>
            <!-- form content -->
        </form>
    </field>
</record>
```

### In Security Rules

```csv
# Before (V1) - ir.model.access.csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_g2p_program_user,access_g2p_program_user,model_g2p_program,group_g2p_user,1,0,0,0

# After (V2) - ir.model.access.csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_spp_program_user,access_spp_program_user,model_spp_program,group_spp_user,1,0,0,0
```

## Automated Migration Script

Use this script to update module dependencies:

```python
#!/usr/bin/env python3
"""
Update module dependencies from g2p to spp
Usage: python update_manifest.py /path/to/module
"""

import ast
import sys
from pathlib import Path

# Module renames (comprehensive list)
MODULE_RENAMES = {
    'g2p_registry_base': 'spp_registry_base',
    'g2p_registry_individual': 'spp_registry_base',
    'g2p_registry_group': 'spp_registry_base',
    'g2p_registry_membership': 'spp_registry_base',
    'g2p_programs': 'spp_programs_base',
    'g2p_bank': 'spp_banking',
    'g2p_encryption': 'spp_encryption',
    'g2p_openid_vci': 'spp_credentials',
    'g2p_openid_vci_rest_api': 'spp_credentials_rest_api',
    'g2p_payment_interop_layer': 'spp_payment_interop_layer',
    'g2p_payment_phee': 'spp_payment_phee',
    'g2p_program_assessment': 'spp_program_assessment',
    'g2p_program_approval': 'spp_program_approval',
    'g2p_program_cycleless': 'spp_program_cycleless',
    'g2p_entitlement_in_kind': 'spp_entitlement_in_kind',
}

def update_manifest(manifest_path):
    """Update __manifest__.py with new module names"""
    content = manifest_path.read_text()

    # Simple string replacement
    for old, new in MODULE_RENAMES.items():
        content = content.replace(f"'{old}'", f"'{new}'")
        content = content.replace(f'"{old}"', f'"{new}"')

    manifest_path.write_text(content)
    print(f"✓ Updated {manifest_path}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python update_manifest.py /path/to/module")
        sys.exit(1)

    module_path = Path(sys.argv[1])
    manifest_path = module_path / '__manifest__.py'

    if not manifest_path.exists():
        print(f"Error: {manifest_path} not found")
        sys.exit(1)

    update_manifest(manifest_path)

if __name__ == "__main__":
    main()
```

## Search and Replace Patterns

### For Module Names in `__manifest__.py`

```bash
# In your custom module directory
sed -i "s/'g2p_registry_base'/'spp_registry_base'/g" __manifest__.py
sed -i "s/'g2p_programs'/'spp_programs_base'/g" __manifest__.py
sed -i "s/'g2p_bank'/'spp_banking'/g" __manifest__.py
```

### For Model Names in Python Files

```bash
# Replace in all Python files
find . -name "*.py" -exec sed -i 's/g2p\.registrant/spp.registrant/g' {} \;
find . -name "*.py" -exec sed -i 's/g2p\.program/spp.program/g' {} \;
find . -name "*.py" -exec sed -i 's/g2p\.entitlement/spp.entitlement/g' {} \;
```

### For XML IDs in XML Files

```bash
# Replace in all XML files
find . -name "*.xml" -exec sed -i 's/g2p_registry_base\./spp_registry_base./g' {} \;
find . -name "*.xml" -exec sed -i 's/g2p_programs\./spp_programs_base./g' {} \;
```

## Testing After Migration

After updating namespace references, verify:

```python
# tests/test_namespace_migration.py

from odoo.tests import TransactionCase

class TestNamespaceMigration(TransactionCase):
    def test_models_exist(self):
        """Verify all spp.* models are accessible"""
        # Test your commonly used models
        self.assertTrue(self.env['spp.registrant'])
        self.assertTrue(self.env['spp.program'])

    def test_external_ids_work(self):
        """Verify external IDs resolve correctly"""
        group = self.env.ref('spp_registry_base.group_spp_admin')
        self.assertTrue(group.exists())

    def test_module_installed(self):
        """Verify dependencies are installed"""
        module = self.env['ir.module.module'].search([
            ('name', '=', 'spp_registry_base'),
            ('state', '=', 'installed')
        ])
        self.assertTrue(module.exists())
```

## Common Migration Issues

### Issue: Module Not Found

```
ModuleNotFoundError: No module named 'g2p_registry_base'
```

**Solution:** Update dependency in `__manifest__.py` from `g2p_*` to `spp_*`

### Issue: Model Does Not Exist

```
ValueError: Model 'g2p.program' does not exist
```

**Solution:** Update model string from `g2p.*` to `spp.*` in your code

### Issue: External ID Not Found

```
ValueError: External ID not found: g2p_registry_base.group_g2p_admin
```

**Solution:** Update external ID reference from `g2p_*.*` to `spp_*.*`

## See Also

- {doc}`model_renames` - Complete list of model renames
- {doc}`breaking_changes` - Odoo 19 compatibility issues
- [ADR-001: Namespace Migration](https://github.com/OpenSPP/openspp-modules-v2/blob/main/docs/architecture/decisions/ADR-001-namespace-migration.md)
