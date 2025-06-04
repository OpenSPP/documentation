#!/usr/bin/env python3
"""Update all internal links in documentation files after refactoring."""

import re
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

# Map of old paths to new paths (without extensions)
path_mappings = {
    # Community and support
    "community_and_support/code_of_conduct": "community/code_of_conduct",
    "community_and_support/how_to_contribute_to_the_project": "community/contributing",
    "community_and_support/index": "community/index",
    "community_and_support/l3_support": "community/support",
    "community_and_support/license": "community/license",
    "community_and_support/security_report": "community/security_reporting",
    "community_and_support/i18n_l10n": "developer_guide/i18n_l10n",
    "community_and_support/module_lifecycle_development_status": "community/module_lifecycle_development_status",
    "community_and_support/module_lifecycle_maintainer_role": "community/module_lifecycle_maintainer_role",
    
    # Contributing
    "contributing/admins": "community/contributing",
    "contributing/authors": "community/contributing",
    "contributing/index": "community/contributing",
    "contributing/myst-reference": "community/contributing",
    "contributing/setup-build": "community/contributing",
    "contributing/sphinx-extensions": "community/contributing",
    
    # Explanation to overview/concepts
    "explanation/data_collection_validation": "overview/concepts/data_collection_validation",
    "explanation/data_protection": "overview/concepts/data_protection",
    "explanation/digital_public_infrastructure": "overview/concepts/digital_public_infrastructure",
    "explanation/farmer_registry": "overview/concepts/farmer_registry",
    "explanation/index": "overview/concepts/index",
    "explanation/integrated_beneficiary_registry": "overview/concepts/integrated_beneficiary_registry",
    "explanation/Registering_individuals_and_groups": "overview/concepts/registrant_concepts",
    "explanation/registry_key_concepts": "overview/concepts/registry_key_concepts",
    "explanation/security_archi": "reference/technical/security",
    "explanation/social_protection_management_information_systems": "overview/concepts/sp_mis",
    "explanation/social_registry": "overview/concepts/social_registry",
    "explanation/user_mgt": "overview/concepts/user_management",
    
    # Getting started
    "getting_started/creating_a_program": "user_guide/program_management/create_program",
    "getting_started/installation_guide": "getting_started/installation_docker",
    
    # Glossary
    "glossary": "reference/glossary",
    
    # Developer guides
    "howto/developer_guides/beneficiary_keycloak": "developer_guide/integrations/keycloak_beneficiary_portal",
    "howto/developer_guides/custom_areas": "developer_guide/customization/customizing_areas",
    "howto/developer_guides/custom_audit": "developer_guide/customization/customizing_audit",
    "howto/developer_guides/custom_cr": "developer_guide/customization/customizing_change_requests",
    "howto/developer_guides/custom_cycle": "developer_guide/customization/customizing_cycles",
    "howto/developer_guides/custom_entitlement": "developer_guide/customization/customizing_entitlements",
    "howto/developer_guides/custom_fields_indicators": "developer_guide/customization/customizing_fields",
    "howto/developer_guides/custom_program": "developer_guide/customization/customizing_programs",
    "howto/developer_guides/custom_registry_tab_fields": "developer_guide/customization/customizing_registry",
    "howto/developer_guides/custom_registry": "developer_guide/customization/customizing_registry",
    "howto/developer_guides/custom_service_points": "developer_guide/customization/customizing_service_points",
    "howto/developer_guides/dci": "developer_guide/integrations/dci",
    "howto/developer_guides/development_setup": "developer_guide/setup",
    "howto/developer_guides/esignet": "developer_guide/integrations/esignet",
    "howto/developer_guides/implmenting_pmt": "developer_guide/customization/implementing_pmt",
    "howto/developer_guides/indicators": "developer_guide/customization/customizing_indicators",
    "howto/developer_guides/module": "developer_guide/module_development",
    "howto/developer_guides/oidc": "developer_guide/integrations/oidc",
    "howto/developer_guides/rest_api": "developer_guide/api_usage/rest_api",
    "howto/developer_guides/setting_up_using_pypi": "getting_started/installation_pypi",
    "howto/developer_guides/troubleshooting": "developer_guide/troubleshooting",
    "howto/developer_mode": "developer_guide/developer_mode",
    "howto/index": "user_guide/index",
    "howto/translation": "community/contributing",
    
    # User guides
    "howto/user_guides/administrating_role_based_access": "user_guide/administration/user_access",
    "howto/user_guides/enroll_beneficiaries": "user_guide/program_management/enroll_beneficiaries",
    "howto/user_guides/export_registrant_data": "user_guide/registry_management/import_export_data",
    "howto/user_guides/implementing_pmt": "user_guide/program_management/implementing_pmt",
    "howto/user_guides/import_registrant_data": "user_guide/registry_management/import_export_data",
    "howto/user_guides/register_new_individual": "user_guide/registry_management/register_individual",
    "howto/user_guides/setting_up_farmer_registry": "user_guide/registry_management/setting_up_farmer_registry",
    "howto/user_guides/setting_up_service_points": "user_guide/administration/service_points",
    
    # Technical reference
    "technical_reference/apis": "developer_guide/api_usage/index",
    "technical_reference/architecture": "developer_guide/architecture",
    "technical_reference/audit_logs": "reference/technical/audit_logs",
    "technical_reference/backup": "reference/technical/backup",
    "technical_reference/code": "developer_guide/best_practices",
    "technical_reference/extensibility": "overview/concepts/extensibility",
    "technical_reference/external_api": "developer_guide/api_usage/external_api_xmlrpc",
    "technical_reference/g2p-connect": "developer_guide/integrations/g2p-connect",
    "technical_reference/index": "reference/index",
    "technical_reference/integrations": "overview/features/integrations_apis",
    "technical_reference/monitoring": "reference/technical/monitoring",
    "technical_reference/openg2p": "overview/concepts/openg2p",
    "technical_reference/performance_optimization": "reference/technical/performance",
    "technical_reference/programs/concepts": "developer_guide/architecture",
    "technical_reference/programs/cycle_manager": "reference/technical/cycle_manager",
    "technical_reference/programs/dashboards": "user_guide/reporting_dashboards",
    "technical_reference/programs/deduplication_manager": "reference/technical/deduplication_manager",
    "technical_reference/programs/eligibility_manager": "reference/technical/eligibility_manager",
    "technical_reference/programs/entitlement_manager": "reference/technical/entitlement_manager",
    "technical_reference/programs/index": "reference/technical/index",
    "technical_reference/programs/notification_manager": "reference/technical/notification_manager",
    "technical_reference/programs/program_manager": "reference/technical/program_manager",
    "technical_reference/release_management": "community/release_management",
    "technical_reference/security": "reference/technical/security",
    
    # Tutorial mappings
    "tutorial/access_management": "user_guide/administration/user_access",
    "tutorial/audit_log": "user_guide/administration/using_audit_logs",
    "tutorial/change_requests": "user_guide/registry_management/using_change_requests",
    "tutorial/consent_management": "user_guide/consent_management",
    "tutorial/custom_fields": "user_guide/administration/managing_custom_fields",
    "tutorial/dashboards_and_reports": "user_guide/reporting_dashboards",
    "tutorial/event_data": "user_guide/registry_management/using_event_data",
    "tutorial/geotargeting": "user_guide/program_management/using_geotargeting",
    "tutorial/grievance_redressal_management": "user_guide/grievance_management",
    "tutorial/hardware_integration": "user_guide/administration/hardware_integration",
    "tutorial/index": "user_guide/index",
    "tutorial/indicators": "user_guide/program_management/using_indicators",
    "tutorial/managing_social_protection_programs": "user_guide/program_management/index",
    "tutorial/programs/export_beneficiaries": "user_guide/program_management/export_beneficiaries",
    "tutorial/programs_and_cycles": "user_guide/program_management/programs_overview",
    "tutorial/proxy_means_test": "user_guide/program_management/using_pmt",
    "tutorial/user_guides/administrating_role_based_access": "user_guide/administration/user_access",
    "tutorial/user_guides/allocate_funds": "user_guide/program_management/allocate_funds",
    "tutorial/user_guides/configure_ID_generate_qr": "user_guide/registry_management/identity_management",
    "tutorial/user_guides/configure_cash_entitlements": "user_guide/program_management/configure_entitlements",
    "tutorial/user_guides/create_program_cycle_prepare_entitlements": "user_guide/program_management/create_cycle",
    "tutorial/user_guides/create_social_protection_program": "user_guide/program_management/create_program",
    "tutorial/user_guides/enroll_beneficiaries": "user_guide/program_management/enroll_beneficiaries",
    "tutorial/user_guides/export_registrant_data": "user_guide/registry_management/import_export_data",
    "tutorial/user_guides/import_areas": "user_guide/administration/import_areas",
    "tutorial/user_guides/import_registrant_data": "user_guide/registry_management/import_export_data",
    "tutorial/user_guides/point_of_sales": "user_guide/pos_usage",
    "tutorial/user_guides/register_new_individual": "user_guide/registry_management/register_individual",
    "tutorial/user_guides/setting_up_service_points": "user_guide/administration/service_points",
    "tutorial/vouchers": "user_guide/program_management/using_vouchers",
}

def update_links_in_file(file_path: Path) -> bool:
    """Update links in a single file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Update markdown links [text](path.md)
        def replace_md_link(match):
            link_text = match.group(1)
            link_path = match.group(2)
            
            # Skip external links
            if link_path.startswith(('http://', 'https://', 'mailto:', '#')):
                return match.group(0)
            
            # Remove leading slash if present
            clean_path = link_path.lstrip('/')
            
            # Remove .md extension for comparison
            path_without_ext = clean_path.replace('.md', '').replace('.rst', '')
            
            # Check if this path needs updating
            for old_path, new_path in path_mappings.items():
                if path_without_ext.endswith(old_path):
                    # Calculate the relative path from current file to new location
                    current_depth = len(file_path.parts) - 2  # -2 for 'docs' and filename
                    new_depth = len(new_path.split('/'))
                    
                    # Build relative path
                    if current_depth > 0:
                        prefix = '/'.join(['..'] * current_depth) + '/'
                    else:
                        prefix = ''
                    
                    # Determine extension
                    if '.rst' in link_path:
                        ext = '.rst'
                    else:
                        ext = '.md'
                    
                    new_link = f"{prefix}{new_path}{ext}"
                    return f'[{link_text}]({new_link})'
            
            return match.group(0)
        
        # Pattern for markdown links
        md_link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
        content = re.sub(md_link_pattern, replace_md_link, content)
        
        # Update RST doc references :doc:`path`
        def replace_rst_doc(match):
            doc_path = match.group(1)
            
            # Remove leading slash if present
            clean_path = doc_path.lstrip('/')
            
            # Check if this path needs updating
            for old_path, new_path in path_mappings.items():
                if clean_path.endswith(old_path):
                    # Calculate the relative path
                    current_depth = len(file_path.parts) - 2
                    
                    if current_depth > 0:
                        prefix = '/'.join(['..'] * current_depth) + '/'
                    else:
                        prefix = ''
                    
                    new_doc = f"{prefix}{new_path}"
                    return f':doc:`{new_doc}`'
            
            return match.group(0)
        
        # Pattern for RST doc references
        rst_doc_pattern = r':doc:`([^`]+)`'
        content = re.sub(rst_doc_pattern, replace_rst_doc, content)
        
        # Update image paths
        content = content.replace('](/explanation/images/', '](/overview/concepts/images/')
        content = content.replace('](/technical_reference/images/', '](/reference/technical/images/')
        content = content.replace('](/howto/developer_guides/', '](/developer_guide/')
        content = content.replace('](/howto/user_guides/', '](/user_guide/')
        content = content.replace('](/tutorial/user_guides/', '](/user_guide/')
        
        # Write back if changed
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        
        return False
        
    except Exception as e:
        logger.error(f"Error processing {file_path}: {e}")
        return False

def main():
    """Update links in all documentation files."""
    docs_path = Path('docs')
    
    # Get all markdown and RST files
    all_files = list(docs_path.glob('**/*.md')) + list(docs_path.glob('**/*.rst'))
    
    updated_count = 0
    for file_path in all_files:
        if update_links_in_file(file_path):
            logger.info(f"Updated links in: {file_path}")
            updated_count += 1
    
    logger.info(f"Updated links in {updated_count} files")

if __name__ == "__main__":
    main()