#!/usr/bin/env python3
"""
Add frontmatter to documentation files that are missing it

Infers product categorization based on file path and module names.
"""

from pathlib import Path
import re

# Module to product mapping
MODULE_TO_PRODUCTS = {
    # Registry modules
    'spp_area': ['registry'],
    'spp_area_gis': ['registry'],
    'spp_base': ['core'],
    'spp_base_api': ['core'],
    'spp_base_demo': ['core'],
    'spp_base_gis': ['registry'],
    'spp_base_gis_demo': ['registry'],
    'spp_base_gis_rest': ['registry'],
    'spp_base_setting': ['core'],
    'spp_change_request': ['registry'],
    'spp_change_request_add_children_demo': ['registry'],
    'spp_change_request_add_farmer': ['farmer_registry'],
    'spp_consent': ['core'],
    'spp_custom_field': ['core'],
    'spp_custom_field_custom_filter': ['core'],
    'spp_custom_field_recompute_daily': ['core'],
    'spp_custom_fields_ui': ['core'],
    'spp_custom_filter': ['core'],
    'spp_custom_filter_ui': ['core'],
    'spp_data_export': ['core'],
    'spp_demo': ['core'],
    'spp_dms': ['core'],
    'spp_encryption': ['core'],
    'spp_exclusion_filter': ['registry'],
    'spp_idpass': ['registry'],
    'spp_idqueue': ['registry'],
    'spp_import_match': ['registry'],
    'spp_oauth': ['core'],
    'spp_openid_vci': ['registry'],
    'spp_openid_vci_group': ['registry'],
    'spp_openid_vci_individual': ['registry'],
    'spp_registrant_import': ['registry'],
    'spp_registrant_tag': ['registry'],
    'spp_registry_data_source': ['registry'],
    'spp_registry_group_hierarchy': ['registry'],
    'spp_scan_id_document': ['registry'],
    'spp_starter': ['core'],
    'spp_user_roles': ['core'],

    # Program modules
    'spp_auto_update_entitlements': ['programs'],
    'spp_basic_cash_entitlement_spent': ['programs'],
    'spp_eligibility_sql': ['programs'],
    'spp_eligibility_tags': ['programs'],
    'spp_ent_trans': ['programs'],
    'spp_entitlement_basket': ['programs'],
    'spp_entitlement_cash': ['programs'],
    'spp_entitlement_in_kind': ['programs'],
    'spp_event_data': ['programs'],
    'spp_event_data_program_membership': ['programs'],
    'spp_event_demo': ['programs'],
    'spp_manual_entitlement': ['programs'],
    'spp_pmt': ['programs'],
    'spp_program_id': ['programs'],
    'spp_programs': ['programs'],
    'spp_programs_compliance_criteria': ['programs'],
    'spp_programs_sp': ['programs'],

    # DRIMS modules (inventory management)
    # Note: DRIMS modules will be prefixed with spp_drims_* when added

    # Payment modules
    'spp_pos': ['payments'],
    'spp_service_point_device': ['payments'],
    'spp_service_points': ['payments'],

    # Farmer registry modules
    'spp_farmer_registry_base': ['farmer_registry'],
    'spp_farmer_registry_dashboard': ['farmer_registry'],
    'spp_farmer_registry_demo': ['farmer_registry'],
    'spp_irrigation': ['farmer_registry'],
    'spp_land_record': ['farmer_registry'],

    # API and integration modules
    'spp_api': ['core'],
    'spp_api_records': ['core'],
    'spp_dci_api_server': ['core'],
    'spp_import_dci_api': ['core'],

    # Audit modules
    'spp_audit_config': ['core'],
    'spp_audit_log': ['core'],
    'spp_audit_post': ['core'],
}

# Path pattern to product mapping (for non-module files)
PATH_TO_PRODUCTS = {
    'config_guide/': ['core'],
    'developer_guide/': ['core'],
    'learn/': ['core'],
    'ops_guide/': ['core'],
    'reference/': ['core'],
    'get_started/first_program': ['registry', 'programs'],
    'get_started/': ['core'],
    'user_guide/administration': ['core'],
    'user_guide/dashboards': ['core'],
    'user_guide/entitlements': ['programs'],
}

def infer_products_from_path(file_path: Path) -> list[str]:
    """Infer products from file path"""
    path_str = str(file_path)

    # Check if it's a module documentation file
    if '/modules/' in path_str:
        # Extract module name (e.g., spp_api.md -> spp_api)
        module_name = file_path.stem
        if module_name in MODULE_TO_PRODUCTS:
            return MODULE_TO_PRODUCTS[module_name]
        else:
            # Unknown module - default to core
            return ['core']

    # Check path patterns (most specific first)
    for pattern, products in sorted(PATH_TO_PRODUCTS.items(), key=lambda x: -len(x[0])):
        if pattern in path_str:
            return products

    # Default to core
    return ['core']

def add_frontmatter_to_file(file_path: Path, products: list[str]) -> bool:
    """Add YAML frontmatter to a file"""
    content = file_path.read_text()

    # Skip if frontmatter already exists
    if content.startswith('---\n'):
        return False

    # Create frontmatter
    products_str = ', '.join(products)
    frontmatter = f"""---
openspp:
  doc_status: draft
  products: [{products_str}]
---

"""

    # Prepend frontmatter
    new_content = frontmatter + content
    file_path.write_text(new_content)

    return True

def main():
    """Add frontmatter to all files missing it"""
    docs_dir = Path('documentation/docs')

    if not docs_dir.exists():
        print(f"Error: {docs_dir} does not exist")
        print("Please run this script from the repository root")
        return 1

    # Get list of files missing frontmatter from audit
    # NOTE: Skipping modules/ folder - will be regenerated
    missing_frontmatter_files = [
        'config_guide/change_request_types/index.md',
        'config_guide/consent/index.md',
        'config_guide/eligibility/index.md',
        'config_guide/entitlement_formulas/index.md',
        'config_guide/index.md',
        'config_guide/variables/index.md',
        'developer_guide/architecture/index.md',
        'developer_guide/extending/index.md',
        'developer_guide/index.md',
        'developer_guide/integrations/index.md',
        'developer_guide/setup/index.md',
        'get_started/first_program/index.md',
        'get_started/index.md',
        'learn/concepts/index.md',
        'learn/index.md',
        'ops_guide/backup/index.md',
        'ops_guide/deployment/index.md',
        'ops_guide/index.md',
        'ops_guide/monitoring/index.md',
        'ops_guide/storage/index.md',
        'reference/api/index.md',
        'reference/index.md',
        'reference/modules/index.md',
        'user_guide/administration/index.md',
        'user_guide/dashboards/index.md',
        'user_guide/entitlements/index.md',
    ]

    updated_count = 0

    print(f"Processing {len(missing_frontmatter_files)} files...\n")

    for rel_path_str in missing_frontmatter_files:
        file_path = docs_dir / rel_path_str

        if not file_path.exists():
            print(f"⚠️  File not found: {rel_path_str}")
            continue

        products = infer_products_from_path(file_path)

        if add_frontmatter_to_file(file_path, products):
            print(f"✅ Added frontmatter to {rel_path_str} (products: {products})")
            updated_count += 1
        else:
            print(f"⏭️  Skipped {rel_path_str} (already has frontmatter)")

    print(f"\n{'='*80}")
    print(f"Updated {updated_count} files")
    print(f"{'='*80}\n")
    print("Next steps:")
    print("1. Review the changes: git diff documentation/docs/")
    print("2. Verify categorization: python documentation/scripts/audit_product_metadata.py")
    print("3. Build docs: cd documentation && make html")

    return 0

if __name__ == '__main__':
    exit(main())
