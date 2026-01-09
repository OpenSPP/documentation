#!/usr/bin/env python3
"""
Audit documentation files for product metadata

Checks which files are missing the 'products' field in their frontmatter
and reports categorization status.
"""

from pathlib import Path
import re
from collections import defaultdict

def extract_frontmatter(file_path: Path) -> dict:
    """Extract YAML frontmatter from a markdown file"""
    content = file_path.read_text()

    if not content.startswith('---\n'):
        return {'has_frontmatter': False}

    try:
        end_idx = content.find('\n---\n', 4)
        if end_idx == -1:
            return {'has_frontmatter': False}

        frontmatter_text = content[4:end_idx]

        # Simple YAML parsing for our specific structure
        result = {'has_frontmatter': True}

        # Check for openspp section
        if 'openspp:' in frontmatter_text:
            result['has_openspp'] = True

            # Check for products field
            products_match = re.search(r'products:\s*\[(.*?)\]', frontmatter_text)
            if products_match:
                products_str = products_match.group(1)
                if products_str.strip():
                    products = [p.strip() for p in products_str.split(',')]
                    result['products'] = products
                else:
                    result['products'] = []
            else:
                result['has_openspp'] = True
                result['products'] = None
        else:
            result['has_openspp'] = False

        return result
    except Exception as e:
        return {'error': str(e)}

def audit_documentation(docs_dir: Path):
    """Audit all documentation files"""

    # Categories for reporting
    missing_frontmatter = []
    missing_openspp = []
    missing_products = []
    empty_products = []
    categorized = defaultdict(list)
    errors = []

    # Find all .md files
    md_files = sorted(docs_dir.rglob('*.md'))

    print(f"Auditing {len(md_files)} markdown files...\n")

    for md_file in md_files:
        rel_path = md_file.relative_to(docs_dir)

        # Skip certain directories
        if any(part.startswith('_') or part.startswith('.') for part in rel_path.parts):
            continue

        metadata = extract_frontmatter(md_file)

        if 'error' in metadata:
            errors.append((rel_path, metadata['error']))
        elif not metadata.get('has_frontmatter'):
            missing_frontmatter.append(rel_path)
        elif not metadata.get('has_openspp'):
            missing_openspp.append(rel_path)
        elif metadata.get('products') is None:
            missing_products.append(rel_path)
        elif metadata.get('products') == []:
            empty_products.append(rel_path)
        else:
            # Categorized correctly
            products = metadata['products']
            for product in products:
                categorized[product].append(rel_path)

    # Print results
    print("=" * 80)
    print("AUDIT RESULTS")
    print("=" * 80)
    print()

    # Summary
    total = len(md_files)
    issues = len(missing_frontmatter) + len(missing_openspp) + len(missing_products) + len(empty_products)
    good = total - issues - len(errors)

    print(f"Total files:           {total}")
    print(f"Correctly categorized: {good} ({good/total*100:.1f}%)")
    print(f"Need attention:        {issues} ({issues/total*100:.1f}%)")
    if errors:
        print(f"Errors:                {len(errors)}")
    print()

    # Issues breakdown
    if missing_frontmatter:
        print(f"❌ MISSING FRONTMATTER ({len(missing_frontmatter)} files)")
        print("   These files need a YAML frontmatter block added:")
        print()
        for path in missing_frontmatter[:10]:
            print(f"   - {path}")
        if len(missing_frontmatter) > 10:
            print(f"   ... and {len(missing_frontmatter) - 10} more")
        print()

    if missing_openspp:
        print(f"❌ MISSING OPENSPP SECTION ({len(missing_openspp)} files)")
        print("   These files have frontmatter but no 'openspp:' section:")
        print()
        for path in missing_openspp[:10]:
            print(f"   - {path}")
        if len(missing_openspp) > 10:
            print(f"   ... and {len(missing_openspp) - 10} more")
        print()

    if missing_products:
        print(f"❌ MISSING PRODUCTS FIELD ({len(missing_products)} files)")
        print("   These files have 'openspp:' but no 'products:' field:")
        print()
        for path in missing_products[:10]:
            print(f"   - {path}")
        if len(missing_products) > 10:
            print(f"   ... and {len(missing_products) - 10} more")
        print()

    if empty_products:
        print(f"⚠️  EMPTY PRODUCTS ({len(empty_products)} files)")
        print("   These files have 'products: []' - should be [core] or specific modules:")
        print()
        for path in empty_products[:10]:
            print(f"   - {path}")
        if len(empty_products) > 10:
            print(f"   ... and {len(empty_products) - 10} more")
        print()

    if errors:
        print(f"⚠️  PARSING ERRORS ({len(errors)} files)")
        for path, error in errors[:5]:
            print(f"   - {path}: {error}")
        if len(errors) > 5:
            print(f"   ... and {len(errors) - 5} more")
        print()

    # Categorization breakdown
    if categorized:
        print("✅ CATEGORIZED FILES BY PRODUCT")
        print()
        for product in sorted(categorized.keys()):
            count = len(categorized[product])
            print(f"   {product:20s} {count:4d} files")
        print()

    # Save detailed report
    report_path = docs_dir.parent / 'scripts' / 'audit_report.txt'
    with open(report_path, 'w') as f:
        f.write("DOCUMENTATION CATEGORIZATION AUDIT\n")
        f.write("=" * 80 + "\n\n")

        if missing_frontmatter:
            f.write(f"MISSING FRONTMATTER ({len(missing_frontmatter)} files)\n")
            f.write("-" * 80 + "\n")
            for path in missing_frontmatter:
                f.write(f"{path}\n")
            f.write("\n")

        if missing_openspp:
            f.write(f"MISSING OPENSPP SECTION ({len(missing_openspp)} files)\n")
            f.write("-" * 80 + "\n")
            for path in missing_openspp:
                f.write(f"{path}\n")
            f.write("\n")

        if missing_products:
            f.write(f"MISSING PRODUCTS FIELD ({len(missing_products)} files)\n")
            f.write("-" * 80 + "\n")
            for path in missing_products:
                f.write(f"{path}\n")
            f.write("\n")

        if empty_products:
            f.write(f"EMPTY PRODUCTS ({len(empty_products)} files)\n")
            f.write("-" * 80 + "\n")
            for path in empty_products:
                f.write(f"{path}\n")
            f.write("\n")

        if categorized:
            f.write("CATEGORIZED FILES\n")
            f.write("-" * 80 + "\n")
            for product in sorted(categorized.keys()):
                f.write(f"\n{product.upper()}\n")
                for path in sorted(categorized[product]):
                    f.write(f"  {path}\n")
            f.write("\n")

    print(f"📄 Detailed report saved to: {report_path}")
    print()

    # Action items
    if issues > 0:
        print("=" * 80)
        print("NEXT STEPS")
        print("=" * 80)
        print()
        print("1. Review the files listed above")
        print("2. Add 'products:' field to each file's frontmatter")
        print("3. Use these guidelines:")
        print()
        print("   products: [core]              - Platform-wide, ops, dev docs")
        print("   products: [registry]          - Registry-specific features")
        print("   products: [programs]          - Program management features")
        print("   products: [drims]             - DRIMS inventory features")
        print("   products: [payments]          - Payment processing")
        print("   products: [grievances]        - Grievance handling")
        print("   products: [registry, programs] - Cross-module workflows")
        print()
        print("4. Re-run this script to verify: python scripts/audit_product_metadata.py")
        print()

if __name__ == '__main__':
    docs_dir = Path('documentation/docs')

    if not docs_dir.exists():
        print(f"Error: {docs_dir} does not exist")
        print("Please run this script from the repository root")
        exit(1)

    audit_documentation(docs_dir)
