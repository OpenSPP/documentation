#!/usr/bin/env python3
"""
Add product metadata to documentation files based on their path
"""

from pathlib import Path
import re

# Mapping from path patterns to products
PATH_TO_PRODUCTS = {
    'user_guide/registry': ['registry'],
    'user_guide/programs': ['programs'],
    'user_guide/drims': ['drims'],
    'user_guide/payments': ['payments'],
    'user_guide/grievances': ['grievances'],
    'config_guide/drims': ['drims'],
    'config_guide/registry': ['registry'],
    'config_guide/programs': ['programs'],
    'get_started': ['registry', 'programs'],  # Getting started uses both
    'technical_reference': ['core'],
    'developer_guide': ['core'],
    'ops_guide': ['core'],
    'howto/developer': ['core'],
    'modules/spp_farmer': ['farmer_registry'],
    'explanation': ['core'],
}

def infer_products(file_path: Path) -> list[str]:
    """Infer products from file path"""
    try:
        # Get relative path from docs directory
        docs_dir = Path('documentation/docs').resolve()
        path_str = str(file_path.resolve().relative_to(docs_dir))
    except ValueError:
        # If file is not under docs directory, use absolute path
        path_str = str(file_path)

    for pattern, products in PATH_TO_PRODUCTS.items():
        if pattern in path_str:
            return products

    return ['core']  # Default to core

def add_products_to_frontmatter(file_path: Path):
    """Add products field to YAML frontmatter"""
    content = file_path.read_text()

    # Check if frontmatter exists
    if not content.startswith('---\n'):
        return False

    # Check if products already exist
    if 'products:' in content:
        return False

    products = infer_products(file_path)

    # Find end of frontmatter
    lines = content.split('\n')
    try:
        end_idx = lines[1:].index('---') + 1
    except ValueError:
        # No closing ---, skip this file
        return False

    # Insert products after openspp: line
    inserted = False
    for i in range(1, end_idx):
        if lines[i].strip() == 'openspp:':
            # Find the next line after openspp: to determine indentation
            # Add products with proper indentation
            products_str = ', '.join(products)
            lines.insert(i + 2, f'  products: [{products_str}]')
            inserted = True
            break

    if not inserted:
        # No openspp: line found, skip
        return False

    file_path.write_text('\n'.join(lines))
    return True

# Run on all .md files
if __name__ == '__main__':
    docs_dir = Path('documentation/docs')

    if not docs_dir.exists():
        print(f"Error: {docs_dir} does not exist")
        print("Please run this script from the repository root")
        exit(1)

    updated = 0

    for md_file in sorted(docs_dir.rglob('*.md')):
        try:
            if add_products_to_frontmatter(md_file):
                print(f"Updated: {md_file}")
                updated += 1
        except Exception as e:
            print(f"Error processing {md_file}: {e}")

    print(f"\nUpdated {updated} files")
