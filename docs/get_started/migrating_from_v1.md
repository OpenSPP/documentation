---
openspp:
  doc_status: draft
---

# Quick Start: Migrating from V1 to V2

This guide is for **developers** getting started with migrating from OpenSPP V1 to V2.

## What You Need to Know

OpenSPP V2 includes major changes:

- **Odoo 19 upgrade** (from Odoo 17)
- **Namespace changes** (`g2p.*` → `spp.*`)
- **Module consolidation** (fewer modules, same functionality)
- **API v2** (OAuth 2.0, external IDs)

**Migration time:** Plan for 2-4 weeks depending on customization complexity.

## Before You Start

### 1. Check Your Customizations

```bash
# In your custom module directory
find . -name "*.py" -o -name "*.xml" | xargs grep -l "g2p\."

# This shows which files reference V1 code
```

### 2. Backup Everything

```bash
# Backup database
pg_dump openspp_production > openspp_v1_backup_$(date +%Y%m%d).sql

# Backup filestore
tar -czf filestore_backup_$(date +%Y%m%d).tar.gz /var/lib/odoo/filestore/

# Backup custom modules
tar -czf custom_modules_$(date +%Y%m%d).tar.gz /path/to/custom/modules/
```

### 3. Set Up Test Environment

**Do NOT migrate production first!**

```bash
# Clone production to test database
createdb openspp_test
psql openspp_test < openspp_v1_backup.sql

# Test migration on test database first
```

## Quick Migration Steps

### Step 1: Update Module Dependencies (5 minutes)

Edit your custom module's `__manifest__.py`:

```python
# Find this file: your_custom_module/__manifest__.py

{
    'name': 'My Custom Module',
    'version': '19.0.1.0.0',  # Update version
    'depends': [
        # OLD → NEW
        'g2p_registry_base',     # → 'spp_registry_base'
        'g2p_programs',          # → 'spp_programs_base'
        'g2p_bank',              # → 'spp_banking'
    ],
}
```

### Step 2: Fix View Files (15 minutes)

Replace `<tree>` with `<list>` in all XML view files:

```bash
cd your_custom_module/

# Automated fix
find . -name "*.xml" -exec sed -i 's/<tree/<list/g' {} \;
find . -name "*.xml" -exec sed -i 's/<\/tree>/<\/list>/g' {} \;
```

### Step 3: Update Model References (30 minutes)

Replace `g2p.*` with `spp.*` in Python and XML files:

```bash
# Python files
find . -name "*.py" -exec sed -i 's/g2p\.program/spp.program/g' {} \;
find . -name "*.py" -exec sed -i 's/g2p\.registrant/spp.registrant/g' {} \;
find . -name "*.py" -exec sed -i 's/g2p\.entitlement/spp.entitlement/g' {} \;

# XML files
find . -name "*.xml" -exec sed -i 's/g2p_registry/spp_registry/g' {} \;
find . -name "*.xml" -exec sed -i 's/g2p_programs/spp_programs_base/g' {} \;
```

### Step 4: Fix Security Files (10 minutes)

Remove deprecated fields from security XML:

```bash
# Remove category_id from res.groups
find . -name "*.xml" -exec sed -i '/<field name="category_id"/d' {} \;

# Remove users from res.groups
find . -name "*.xml" -exec sed -i '/<field name="users"/d' {} \;

# Remove groups from menuitem (manual review recommended)
# Check views/menus.xml and remove groups="..." from menuitems
```

### Step 5: Test Installation (1 hour)

```bash
# Start Odoo in test mode
./odoo-bin -d openspp_test -u your_custom_module --test-enable --stop-after-init

# Check for errors in output
```

## Common Issues and Quick Fixes

### Issue: "Invalid view type: 'tree'"

```xml
<!-- Find and replace in all XML files -->
<tree>  →  <list>
</tree>  →  </list>
```

### Issue: "Invalid field 'category_id'"

```xml
<!-- Remove this line from security/groups.xml -->
<field name="category_id" ref="..."/>  ← DELETE THIS LINE
```

### Issue: "Model 'g2p.program' does not exist"

```python
# Update in Python files
self.env['g2p.program']  →  self.env['spp.program']
```

### Issue: Module dependency not found

```python
# In __manifest__.py
'depends': [
    'g2p_programs',  →  'spp_programs_base',  # Note: _base suffix!
]
```

## Download Migration Script

Save this as `quick_migrate.py` in your module directory:

```python
#!/usr/bin/env python3
"""
Quick migration script for OpenSPP V1 to V2
Usage: python quick_migrate.py /path/to/your/module
"""

import re
from pathlib import Path

REPLACEMENTS = {
    # Module names
    'g2p_registry_base': 'spp_registry_base',
    'g2p_programs': 'spp_programs_base',
    'g2p_bank': 'spp_banking',

    # Model names
    'g2p.program': 'spp.program',
    'g2p.registrant': 'spp.registrant',
    'g2p.entitlement': 'spp.entitlement',
    'g2p.program.cycle': 'spp.program.cycle',
    'g2p.program.membership': 'spp.program.membership',
}

def migrate_file(file_path):
    """Apply replacements to a file"""
    try:
        content = file_path.read_text()
        original = content

        # Apply all replacements
        for old, new in REPLACEMENTS.items():
            content = content.replace(old, new)

        # Fix tree → list in XML
        if file_path.suffix == '.xml':
            content = re.sub(r'<tree(\s|>)', r'<list\1', content)
            content = re.sub(r'</tree>', r'</list>', content)

            # Remove deprecated fields
            content = re.sub(r'\s*<field name="category_id"[^>]*/>\n', '', content)
            content = re.sub(r'\s*<field name="users"[^>]*/>\n', '', content)

        if content != original:
            file_path.write_text(content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python quick_migrate.py /path/to/module")
        sys.exit(1)

    module_path = Path(sys.argv[1])
    if not module_path.exists():
        print(f"Error: {module_path} does not exist")
        sys.exit(1)

    # Process all Python and XML files
    files = list(module_path.rglob("*.py")) + list(module_path.rglob("*.xml"))

    changed = 0
    for file_path in files:
        if migrate_file(file_path):
            print(f"✓ {file_path.relative_to(module_path)}")
            changed += 1

    print(f"\nMigrated {changed} files")
    print("\nNext steps:")
    print("1. Review changes: git diff")
    print("2. Test installation: ./odoo-bin -d test_db -u your_module")
    print("3. Check for errors in the output")

if __name__ == "__main__":
    main()
```

Run it:

```bash
python quick_migrate.py /path/to/your/module
```

## Validation Checklist

After migration, verify:

- [ ] Module installs without errors
- [ ] All views load correctly
- [ ] Menu items appear
- [ ] Security rules work
- [ ] Custom functionality works
- [ ] Tests pass (if you have them)

## Testing Commands

```bash
# Install in test database
./odoo-bin -d openspp_test -i your_custom_module

# Update existing installation
./odoo-bin -d openspp_test -u your_custom_module

# Run with tests
./odoo-bin -d openspp_test -u your_custom_module --test-enable --stop-after-init
```

## When to Get Help

Stop and seek help if:

- Module won't install after following these steps
- Critical functionality broken
- Data loss or corruption
- Security issues
- Performance degradation

## Next Steps

Once basic migration works:

1. **Deep dive:** Read the {doc}`detailed migration guide </developer_guide/migration/index>`
2. **API updates:** If you use the API, see {doc}`API changes </developer_guide/migration/api_changes>`
3. **Breaking changes:** Review all {doc}`Odoo 19 breaking changes </developer_guide/migration/breaking_changes>`
4. **Testing:** Write comprehensive tests for your customizations

## Additional Resources

### Documentation

- {doc}`Complete Migration Guide </developer_guide/migration/index>` - Detailed migration information
- {doc}`Namespace Changes </developer_guide/migration/namespace_changes>` - All module renames
- {doc}`Model Renames </developer_guide/migration/model_renames>` - All model changes
- {doc}`Breaking Changes </developer_guide/migration/breaking_changes>` - Odoo 19 compatibility

### Community

- [OpenSPP Forums](https://github.com/OpenSPP/openspp/discussions) - Ask questions
- [GitHub Issues](https://github.com/OpenSPP/openspp/issues) - Report bugs
- [V2 Architecture Docs](https://github.com/OpenSPP/openspp-modules-v2) - Technical details

## FAQ

### How long does migration take?

- **Simple module** (no customizations): 1-2 days
- **Moderate customizations**: 1-2 weeks
- **Heavy customizations**: 2-4 weeks

### Can I migrate incrementally?

No - V2 is a major upgrade. You must migrate the entire system.

### Will my data be safe?

Yes, if you:
1. Backup first
2. Test on a copy
3. Follow migration procedures

### What if something goes wrong?

Restore from backup:

```bash
# Restore database
dropdb openspp_test
createdb openspp_test
psql openspp_test < openspp_v1_backup.sql

# Restore filestore
rm -rf /var/lib/odoo/filestore/openspp_test
tar -xzf filestore_backup.tar.gz -C /var/lib/odoo/filestore/
```

### Can I stay on V1?

V1 will receive security updates until Dec 2025. After that, you must upgrade.

## Troubleshooting

### Module won't install

```bash
# Check logs for specific error
tail -f /var/log/odoo/odoo-server.log

# Common issues:
# - Missing dependency (install missing spp_* modules)
# - Syntax error (check Python/XML files)
# - Database constraint (check for data issues)
```

### Views don't appear

```
# Check for view errors
SELECT name, arch_base FROM ir_ui_view WHERE name LIKE '%your_module%';

# Common issues:
# - Still using <tree> instead of <list>
# - Invalid XML syntax
# - Missing parent view
```

### Permission errors

```
# Check security rules
SELECT * FROM ir_model_access WHERE name LIKE '%your_module%';

# Common issues:
# - ir.model.access.csv not updated
# - Group references still use g2p_*
```

## Success Indicators

You've successfully migrated when:

✓ Module installs without errors
✓ All tests pass
✓ Views render correctly
✓ Security works as expected
✓ Data integrity maintained
✓ Performance acceptable
✓ Users can perform all tasks

## Get Started Now

1. **Backup everything**
2. **Run migration script** on test copy
3. **Test thoroughly**
4. **Fix issues** using detailed guides
5. **Repeat** until perfect
6. **Migrate production** (with scheduled downtime)

Good luck with your migration!
