#\!/usr/bin/env python3
"""Handle remaining files that weren't moved in the initial refactoring."""

import os
import shutil
from pathlib import Path

# Additional mappings for files that were missed
additional_mappings = [
    # Community and support files
    ("docs/community_and_support/i18n_l10n.md", "docs/developer_guide/i18n_l10n.md"),
    ("docs/community_and_support/module_lifecycle_development_status.rst", "docs/community/module_lifecycle_development_status.rst"),
    ("docs/community_and_support/module_lifecycle_maintainer_role.rst", "docs/community/module_lifecycle_maintainer_role.rst"),
    
    # Split installation guide
    ("docs/getting_started/installation_guide.md", "docs/getting_started/installation_pypi.md"),
    
    # Images directories - move them to their new locations
    ("docs/explanation/images/", "docs/overview/concepts/images/"),
    ("docs/technical_reference/images/", "docs/reference/technical/images/"),
    ("docs/technical_reference/programs/images/", "docs/reference/technical/images/programs/"),
    ("docs/technical_reference/external_api/", "docs/developer_guide/api_usage/external_api/"),
    
    # Howto images
    ("docs/howto/developer_guides/beneficiary_keycloak/", "docs/developer_guide/integrations/beneficiary_keycloak/"),
    ("docs/howto/developer_guides/custom_areas/", "docs/developer_guide/customization/custom_areas/"),
    ("docs/howto/developer_guides/custom_audit/", "docs/developer_guide/customization/custom_audit/"),
    ("docs/howto/developer_guides/custom_cr/", "docs/developer_guide/customization/custom_cr/"),
    ("docs/howto/developer_guides/custom_entitlement/", "docs/developer_guide/customization/custom_entitlement/"),
    ("docs/howto/developer_guides/custom_registry/", "docs/developer_guide/customization/custom_registry/"),
    ("docs/howto/developer_guides/custom_service_points/", "docs/developer_guide/customization/custom_service_points/"),
    ("docs/howto/developer_guides/esignet/", "docs/developer_guide/integrations/esignet/"),
    ("docs/howto/developer_guides/rest_api/", "docs/developer_guide/api_usage/rest_api/"),
    ("docs/howto/developer_guides/setting_up_using_pypi/", "docs/developer_guide/setting_up_using_pypi/"),
    ("docs/howto/developer_mode/", "docs/developer_guide/developer_mode/"),
    
    # User guides images
    ("docs/howto/user_guides/administrating_role_based_access/", "docs/user_guide/administration/administrating_role_based_access/"),
    ("docs/howto/user_guides/enroll_beneficiaries/", "docs/user_guide/program_management/enroll_beneficiaries/"),
    ("docs/howto/user_guides/export_registrant_data/", "docs/user_guide/registry_management/export_registrant_data/"),
    ("docs/howto/user_guides/import_registrant_data/", "docs/user_guide/registry_management/import_registrant_data/"),
    ("docs/howto/user_guides/register_new_individual/", "docs/user_guide/registry_management/register_new_individual/"),
    ("docs/howto/user_guides/setting_up_farmer_registry/", "docs/user_guide/registry_management/setting_up_farmer_registry/"),
    ("docs/howto/user_guides/setting_up_service_points/", "docs/user_guide/administration/setting_up_service_points/"),
    
    # Tutorial images
    ("docs/tutorial/access_management/", "docs/user_guide/administration/access_management/"),
    ("docs/tutorial/geotargeting/", "docs/user_guide/program_management/geotargeting/"),
    ("docs/tutorial/indicators/", "docs/user_guide/program_management/indicators/"),
    ("docs/tutorial/programs_and_cycles/", "docs/user_guide/program_management/programs_and_cycles/"),
    ("docs/tutorial/user_guides/administrating_role_based_access/", "docs/user_guide/administration/administrating_role_based_access/"),
    ("docs/tutorial/user_guides/allocate_funds/", "docs/user_guide/program_management/allocate_funds/"),
    ("docs/tutorial/user_guides/configure_ID_generate_qr/", "docs/user_guide/registry_management/configure_ID_generate_qr/"),
    ("docs/tutorial/user_guides/configure_cash_entitlements/", "docs/user_guide/program_management/configure_cash_entitlements/"),
    ("docs/tutorial/user_guides/create_program_cycle_prepare_entitlements/", "docs/user_guide/program_management/create_program_cycle_prepare_entitlements/"),
    ("docs/tutorial/user_guides/create_social_protection_program/", "docs/user_guide/program_management/create_social_protection_program/"),
    ("docs/tutorial/user_guides/enroll_beneficiaries/", "docs/user_guide/program_management/enroll_beneficiaries/"),
    ("docs/tutorial/user_guides/export_registrant_data/", "docs/user_guide/registry_management/export_registrant_data/"),
    ("docs/tutorial/user_guides/import_areas/", "docs/user_guide/administration/import_areas/"),
    ("docs/tutorial/user_guides/import_registrant_data/", "docs/user_guide/registry_management/import_registrant_data/"),
    ("docs/tutorial/user_guides/point_of_sales/", "docs/user_guide/point_of_sales/"),
    ("docs/tutorial/user_guides/register_new_individual/", "docs/user_guide/registry_management/register_new_individual/"),
    ("docs/tutorial/user_guides/setting_up_service_points/", "docs/user_guide/administration/setting_up_service_points/"),
]

# Process additional mappings
for src, dst in additional_mappings:
    src_path = Path(src)
    dst_path = Path(dst)
    
    if src_path.exists():
        if src.endswith("/"):
            # Directory
            if src_path.is_dir():
                dst_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(src_path), str(dst_path))
                print(f"Moved directory: {src_path} -> {dst_path}")
        else:
            # File
            dst_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src_path), str(dst_path))
            print(f"Moved file: {src_path} -> {dst_path}")

# Remove old empty directories
dirs_to_remove = [
    "docs/community_and_support",
    "docs/contributing", 
    "docs/explanation",
    "docs/howto/developer_guides",
    "docs/howto/user_guides",
    "docs/howto",
    "docs/technical_reference/programs",
    "docs/technical_reference",
    "docs/tutorial/user_guides",
    "docs/tutorial"
]

for dir_path in dirs_to_remove:
    try:
        if Path(dir_path).exists() and not any(Path(dir_path).iterdir()):
            os.rmdir(dir_path)
            print(f"Removed empty directory: {dir_path}")
    except:
        pass
