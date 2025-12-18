---
openspp:
  doc_status: draft
---

# V1 to V2 Migration Guide

This guide is for **developers** upgrading custom modules and extensions from OpenSPP V1 to V2.

## What Changed in V2

OpenSPP V2 is a major architectural upgrade that includes:

1. **Odoo 19 Upgrade** - Platform upgrade from Odoo 17 to Odoo 19
2. **Namespace Migration** - All `g2p.*` models renamed to `spp.*`
3. **Module Consolidation** - Simplified module structure (e.g., 10 change request modules → 1)
4. **Breaking API Changes** - Odoo 19 compatibility changes

## Prerequisites

Before starting migration:

- Python 3.11+ development environment
- Understanding of Odoo module development
- Git for version control
- Database backup of your V1 instance

## Migration Path

```{toctree}
:maxdepth: 1

namespace_changes
model_renames
api_changes
breaking_changes
```

## Quick Overview

| Change Type | Impact | Effort |
|-------------|--------|--------|
| Namespace (`g2p.*` → `spp.*`) | HIGH | Medium (mostly automated) |
| Module renames | MEDIUM | Low (find/replace) |
| Odoo 19 breaking changes | HIGH | High (manual review required) |
| Change request consolidation | MEDIUM | Medium (API changed) |

## Migration Workflow

### 1. Assess Your Custom Code

Identify what you have:

```bash
# Find all g2p references in your custom modules
cd your_custom_module/
grep -r "g2p\." . --include="*.py" --include="*.xml"

# Count occurrences
grep -r "g2p\." . --include="*.py" --include="*.xml" | wc -l
```

### 2. Update Dependencies

Update your module's `__manifest__.py`:

```python
# Before (V1)
{
    'name': 'My Custom Module',
    'depends': [
        'g2p_registry_base',
        'g2p_programs',
    ],
}

# After (V2)
{
    'name': 'My Custom Module',
    'depends': [
        'spp_registry_base',
        'spp_programs_base',
    ],
}
```

### 3. Update Code References

Follow the detailed guides:

- {doc}`namespace_changes` - Update all model and module names
- {doc}`model_renames` - Update field references
- {doc}`api_changes` - Update API endpoints
- {doc}`breaking_changes` - Fix Odoo 19 compatibility issues

### 4. Test Migration

Create a test checklist:

```python
# tests/test_migration.py

from odoo.tests import TransactionCase

class TestV2Migration(TransactionCase):
    def test_module_installs(self):
        """Verify module installs without errors"""
        # Your test here

    def test_models_accessible(self):
        """Verify all models exist with new names"""
        partner = self.env['res.partner'].search([], limit=1)
        self.assertTrue(partner.exists())

    def test_data_integrity(self):
        """Verify data migrates correctly"""
        # Test critical data
```

## Migration Tools

### Automated Find-Replace Script

Use this script to automate basic replacements:

```python
#!/usr/bin/env python3
"""
Automated V1 to V2 migration helper
Usage: python migrate_to_v2.py /path/to/your/module
"""

import re
import sys
from pathlib import Path

# Model name replacements
MODEL_RENAMES = {
    'g2p.reg.id': 'spp.reg.id',
    'g2p.id.type': 'spp.id.type',
    'g2p.program': 'spp.program',
    'g2p.program.cycle': 'spp.program.cycle',
    'g2p.program.membership': 'spp.program.membership',
    'g2p.entitlement': 'spp.entitlement',
    'g2p.payment.batch': 'spp.payment.batch',
    # Add more from model_renames.md
}

# Module name replacements
MODULE_RENAMES = {
    'g2p_registry_base': 'spp_registry_base',
    'g2p_registry_individual': 'spp_registry_base',
    'g2p_registry_group': 'spp_registry_base',
    'g2p_programs': 'spp_programs_base',
    'g2p_bank': 'spp_banking',
    # Add more from namespace_changes.md
}

def migrate_file(file_path):
    """Migrate a single file"""
    content = file_path.read_text()
    original = content

    # Replace model names
    for old, new in MODEL_RENAMES.items():
        content = content.replace(old, new)

    # Replace module names
    for old, new in MODULE_RENAMES.items():
        content = content.replace(old, new)

    # Only write if changed
    if content != original:
        file_path.write_text(content)
        return True
    return False

def migrate_module(module_path):
    """Migrate entire module"""
    module_path = Path(module_path)

    if not module_path.exists():
        print(f"Error: {module_path} does not exist")
        sys.exit(1)

    # Find all Python and XML files
    files = list(module_path.rglob("*.py")) + list(module_path.rglob("*.xml"))

    changed_count = 0
    for file_path in files:
        if migrate_file(file_path):
            print(f"✓ {file_path.relative_to(module_path)}")
            changed_count += 1

    print(f"\nMigrated {changed_count} files")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python migrate_to_v2.py /path/to/your/module")
        sys.exit(1)

    migrate_module(sys.argv[1])
```

**Warning:** This script handles basic replacements only. You must still:
- Review all changes manually
- Fix Odoo 19 breaking changes (see {doc}`breaking_changes`)
- Update tests
- Verify functionality

## Database Migration

V2 includes automatic database migration scripts for core modules. For custom modules:

```python
# In your module: migrations/2.0.0/pre-migrate.py

def migrate(cr, version):
    """Migrate custom data from V1 to V2"""

    # Example: Rename custom table
    cr.execute("""
        ALTER TABLE custom_g2p_extension
        RENAME TO custom_spp_extension
    """)

    # Update foreign key references
    cr.execute("""
        UPDATE custom_spp_extension
        SET registrant_model = 'spp.registrant'
        WHERE registrant_model = 'g2p.registrant'
    """)
```

## Getting Help

If you encounter issues:

1. Check {doc}`breaking_changes` for common problems
2. Review the [V2 Architecture Documentation](https://github.com/OpenSPP/openspp-modules-v2)
3. Ask in [OpenSPP Community Forums](https://github.com/OpenSPP/openspp/discussions)
4. File a bug report with migration details

## See Also

- [Odoo 19 Migration Guide](https://www.odoo.com/documentation/19.0/developer/howtos/upgrade.html)
- [OpenSPP Module Development Guide](../development_setup.md)
