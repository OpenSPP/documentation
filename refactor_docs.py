#!/usr/bin/env python3
"""
OpenSPP Documentation Refactoring Script

This script refactors the OpenSPP documentation structure according to the 
migration mapping provided in review_work/refactor_pages.md.

Usage:
    python refactor_docs.py --dry-run  # Test mode - shows what would be done
    python refactor_docs.py           # Execute the refactoring
"""

import os
import re
import shutil
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import argparse
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

class DocumentationRefactorer:
    def __init__(self, docs_root: str, dry_run: bool = True):
        self.docs_root = Path(docs_root)
        self.dry_run = dry_run
        self.file_mappings = {}
        self.redirects = {}
        self.merged_files = {}
        self.split_files = {}
        self.new_directories = set()
        
    def load_mappings(self):
        """Load the file mappings from the refactor_pages.md document."""
        # File mappings based on the refactor_pages.md content
        mappings = [
            # Community and support mappings
            ("docs/community_and_support/code_of_conduct.md", "docs/community/code_of_conduct.md"),
            ("docs/community_and_support/how_to_contribute_to_the_project.md", "docs/community/contributing.md"),
            ("docs/community_and_support/index.md", "docs/community/index.md"),
            ("docs/community_and_support/l3_support.md", "docs/community/support.md"),
            ("docs/community_and_support/license.md", "docs/community/license.md"),
            ("docs/community_and_support/security_report.md", "docs/community/security_reporting.md"),
            
            # Contributing mappings (merge into community)
            ("docs/contributing/admins.md", "docs/community/contributing.md", "merge"),
            ("docs/contributing/authors.md", "docs/community/contributing.md", "merge"),
            ("docs/contributing/index.md", "docs/community/contributing.md", "merge"),
            ("docs/contributing/myst-reference.md", "docs/community/contributing.md", "merge"),
            ("docs/contributing/setup-build.md", "docs/community/contributing.md", "merge"),
            ("docs/contributing/sphinx-extensions.md", "docs/community/contributing.md", "merge"),
            
            # Explanation to overview/concepts mappings
            ("docs/explanation/data_collection_validation.md", "docs/overview/concepts/data_collection_validation.md"),
            ("docs/explanation/data_protection.md", "docs/overview/concepts/data_protection.md"),
            ("docs/explanation/digital_public_infrastructure.md", "docs/overview/concepts/digital_public_infrastructure.md"),
            ("docs/explanation/farmer_registry.md", "docs/overview/concepts/farmer_registry.md"),
            ("docs/explanation/index.md", "docs/overview/concepts/index.md"),
            ("docs/explanation/integrated_beneficiary_registry.md", "docs/overview/concepts/integrated_beneficiary_registry.md"),
            ("docs/explanation/Registering_individuals_and_groups.md", "docs/overview/concepts/registrant_concepts.md"),
            ("docs/explanation/registry_key_concepts.md", "docs/overview/concepts/registry_key_concepts.md"),
            ("docs/explanation/security_archi.md", "docs/reference/technical/security.md", "merge"),
            ("docs/explanation/social_protection_management_information_systems.md", "docs/overview/concepts/sp_mis.md"),
            ("docs/explanation/social_registry.md", "docs/overview/concepts/social_registry.md"),
            ("docs/explanation/user_mgt.md", "docs/overview/concepts/user_management.md"),
            
            # Getting started mappings
            ("docs/getting_started/creating_a_program.md", "docs/user_guide/program_management/create_program.md"),
            ("docs/getting_started/index.md", "docs/getting_started/index.md"),
            ("docs/getting_started/installation_guide.md", "docs/getting_started/installation_docker.md", "split"),
            ("docs/getting_started/poc_and_pilot.md", "docs/getting_started/poc_and_pilot.md"),
            
            # Developer guides mappings
            ("docs/howto/developer_guides/beneficiary_keycloak.md", "docs/developer_guide/integrations/keycloak_beneficiary_portal.md"),
            ("docs/howto/developer_guides/custom_areas.md", "docs/developer_guide/customization/customizing_areas.md"),
            ("docs/howto/developer_guides/custom_audit.md", "docs/developer_guide/customization/customizing_audit.md"),
            ("docs/howto/developer_guides/custom_cr.md", "docs/developer_guide/customization/customizing_change_requests.md"),
            ("docs/howto/developer_guides/custom_cycle.md", "docs/developer_guide/customization/customizing_cycles.md"),
            ("docs/howto/developer_guides/custom_entitlement.md", "docs/developer_guide/customization/customizing_entitlements.md"),
            ("docs/howto/developer_guides/custom_fields_indicators.md", "docs/developer_guide/customization/customizing_fields.md"),
            ("docs/howto/developer_guides/custom_program.md", "docs/developer_guide/customization/customizing_programs.md"),
            ("docs/howto/developer_guides/custom_registry_tab_fields.md", "docs/developer_guide/customization/customizing_registry.md", "merge"),
            ("docs/howto/developer_guides/custom_registry.md", "docs/developer_guide/customization/customizing_registry.md"),
            ("docs/howto/developer_guides/custom_service_points.md", "docs/developer_guide/customization/customizing_service_points.md"),
            ("docs/howto/developer_guides/dci.md", "docs/developer_guide/integrations/dci.md"),
            ("docs/howto/developer_guides/development_setup.md", "docs/developer_guide/setup.md"),
            ("docs/howto/developer_guides/esignet.md", "docs/developer_guide/integrations/esignet.md"),
            ("docs/howto/developer_guides/implmenting_pmt.md", "docs/developer_guide/customization/implementing_pmt.md"),
            ("docs/howto/developer_guides/indicators.md", "docs/developer_guide/customization/customizing_indicators.md"),
            ("docs/howto/developer_guides/module.md", "docs/developer_guide/module_development.md"),
            ("docs/howto/developer_guides/oidc.md", "docs/developer_guide/integrations/oidc.md"),
            ("docs/howto/developer_guides/rest_api.md", "docs/developer_guide/api_usage/rest_api.md"),
            ("docs/howto/developer_guides/setting_up_using_pypi.md", "docs/getting_started/installation_pypi.md"),
            ("docs/howto/developer_guides/troubleshooting.md", "docs/developer_guide/troubleshooting.md"),
            
            # User guides mappings
            ("docs/howto/user_guides/administrating_role_based_access.md", "docs/user_guide/administration/user_access.md"),
            ("docs/howto/user_guides/enroll_beneficiaries.md", "docs/user_guide/program_management/enroll_beneficiaries.md"),
            ("docs/howto/user_guides/export_registrant_data.md", "docs/user_guide/registry_management/import_export_data.md", "merge"),
            ("docs/howto/user_guides/implementing_pmt.md", "docs/user_guide/program_management/implementing_pmt.md"),
            ("docs/howto/user_guides/import_registrant_data.md", "docs/user_guide/registry_management/import_export_data.md", "merge"),
            ("docs/howto/user_guides/register_new_individual.md", "docs/user_guide/registry_management/register_individual.md"),
            ("docs/howto/user_guides/setting_up_farmer_registry.md", "docs/user_guide/registry_management/setting_up_farmer_registry.md"),
            ("docs/howto/user_guides/setting_up_service_points.md", "docs/user_guide/administration/service_points.md"),
            
            # Other howto mappings
            ("docs/howto/developer_mode.md", "docs/developer_guide/developer_mode.md"),
            ("docs/howto/index.md", "docs/user_guide/index.md", "split"),
            ("docs/howto/translation.md", "docs/community/contributing.md", "merge"),
            
            # Best practices
            ("docs/best_practices/index.md", "docs/developer_guide/best_practices.md"),
            
            # Modules - all go to reference/modules
            ("docs/modules/", "docs/reference/modules/"),  # Directory mapping
            
            # Technical reference mappings
            ("docs/technical_reference/programs/concepts.md", "docs/developer_guide/architecture.md", "merge"),
            ("docs/technical_reference/programs/cycle_manager.rst", "docs/reference/technical/cycle_manager.rst"),
            ("docs/technical_reference/programs/dashboards.md", "docs/user_guide/reporting_dashboards.md"),
            ("docs/technical_reference/programs/deduplication_manager.md", "docs/reference/technical/deduplication_manager.md"),
            ("docs/technical_reference/programs/eligibility_manager.rst", "docs/reference/technical/eligibility_manager.rst"),
            ("docs/technical_reference/programs/entitlement_manager.rst", "docs/reference/technical/entitlement_manager.rst"),
            ("docs/technical_reference/programs/index.md", "docs/reference/technical/index.md"),
            ("docs/technical_reference/programs/notification_manager.rst", "docs/reference/technical/notification_manager.rst"),
            ("docs/technical_reference/programs/program_manager.rst", "docs/reference/technical/program_manager.rst"),
            ("docs/technical_reference/architecture.md", "docs/developer_guide/architecture.md"),
            ("docs/technical_reference/audit_logs.md", "docs/reference/technical/audit_logs.md"),
            ("docs/technical_reference/backup.md", "docs/reference/technical/backup.md"),
            ("docs/technical_reference/code.md", "docs/developer_guide/best_practices.md", "merge"),
            ("docs/technical_reference/extensibility.md", "docs/overview/concepts/extensibility.md"),
            ("docs/technical_reference/external_api.rst", "docs/developer_guide/api_usage/external_api_xmlrpc.md"),
            ("docs/technical_reference/index.md", "docs/reference/index.md", "merge"),
            ("docs/technical_reference/integrations.md", "docs/overview/features/integrations_apis.md"),
            ("docs/technical_reference/monitoring.md", "docs/reference/technical/monitoring.md"),
            ("docs/technical_reference/performance_optimization.md", "docs/reference/technical/performance.md"),
            ("docs/technical_reference/release_management.md", "docs/community/release_management.md"),
            ("docs/technical_reference/security.md", "docs/reference/technical/security.md"),
            ("docs/technical_reference/apis.md", "docs/developer_guide/api_usage/index.md"),
            ("docs/technical_reference/g2p-connect.md", "docs/developer_guide/integrations/g2p-connect.md"),
            ("docs/technical_reference/openg2p.md", "docs/overview/concepts/openg2p.md"),
            
            # Tutorial mappings
            ("docs/tutorial/user_guides/administrating_role_based_access.md", "docs/user_guide/administration/user_access.md", "merge"),
            ("docs/tutorial/user_guides/allocate_funds.md", "docs/user_guide/program_management/allocate_funds.md"),
            ("docs/tutorial/user_guides/configure_cash_entitlements.md", "docs/user_guide/program_management/configure_entitlements.md", "merge"),
            ("docs/tutorial/user_guides/configure_ID_generate_qr.md", "docs/user_guide/registry_management/identity_management.md"),
            ("docs/tutorial/user_guides/create_program_cycle_prepare_entitlements.md", "docs/user_guide/program_management/create_cycle.md", "split"),
            ("docs/tutorial/user_guides/create_social_protection_program.md", "docs/user_guide/program_management/create_program.md", "merge"),
            ("docs/tutorial/user_guides/enroll_beneficiaries.md", "docs/user_guide/program_management/enroll_beneficiaries.md", "merge"),
            ("docs/tutorial/user_guides/export_registrant_data.md", "docs/user_guide/registry_management/import_export_data.md", "merge"),
            ("docs/tutorial/user_guides/import_areas.md", "docs/user_guide/administration/import_areas.md"),
            ("docs/tutorial/user_guides/import_registrant_data.md", "docs/user_guide/registry_management/import_export_data.md", "merge"),
            ("docs/tutorial/user_guides/point_of_sales.md", "docs/user_guide/pos_usage.md"),
            ("docs/tutorial/user_guides/register_new_individual.md", "docs/user_guide/registry_management/register_individual.md", "merge"),
            ("docs/tutorial/user_guides/setting_up_service_points.md", "docs/user_guide/administration/service_points.md", "merge"),
            ("docs/tutorial/access_management.md", "docs/user_guide/administration/user_access.md", "merge"),
            ("docs/tutorial/audit_log.md", "docs/user_guide/administration/using_audit_logs.md"),
            ("docs/tutorial/change_requests.md", "docs/user_guide/registry_management/using_change_requests.md"),
            ("docs/tutorial/consent_management.md", "docs/user_guide/consent_management.md"),
            ("docs/tutorial/custom_fields.md", "docs/user_guide/administration/managing_custom_fields.md"),
            ("docs/tutorial/dashboards_and_reports.md", "docs/user_guide/reporting_dashboards.md", "merge"),
            ("docs/tutorial/event_data.md", "docs/user_guide/registry_management/using_event_data.md"),
            ("docs/tutorial/geotargeting.md", "docs/user_guide/program_management/using_geotargeting.md"),
            ("docs/tutorial/grievance_redressal_management.md", "docs/user_guide/grievance_management.md"),
            ("docs/tutorial/hardware_integration.md", "docs/user_guide/administration/hardware_integration.md"),
            ("docs/tutorial/index.md", "docs/user_guide/index.md", "merge"),
            ("docs/tutorial/indicators.md", "docs/user_guide/program_management/using_indicators.md"),
            ("docs/tutorial/managing_social_protection_programs.md", "docs/user_guide/program_management/index.md", "split"),
            ("docs/tutorial/programs_and_cycles.md", "docs/user_guide/program_management/programs_overview.md", "split"),
            ("docs/tutorial/proxy_means_test.md", "docs/user_guide/program_management/using_pmt.md"),
            ("docs/tutorial/vouchers.md", "docs/user_guide/program_management/using_vouchers.md"),
            ("docs/tutorial/programs/export_beneficiaries.md", "docs/user_guide/program_management/export_beneficiaries.md"),
            
            # Other root level files
            ("docs/glossary.rst", "docs/reference/glossary.rst"),
        ]
        
        # Process mappings
        for mapping in mappings:
            if len(mapping) == 2:
                src, dst = mapping
                action = "move"
            else:
                src, dst, action = mapping
            
            self.file_mappings[src] = (dst, action)
            
            # Generate redirect
            src_path = src.replace("docs/", "")
            dst_path = dst.replace("docs/", "").replace(".md", ".html").replace(".rst", ".html")
            self.redirects[src_path] = dst_path
            
            # Track new directories
            dst_dir = str(Path(dst).parent)
            if dst_dir != "docs":
                self.new_directories.add(dst_dir)

    def create_directories(self):
        """Create all necessary directories."""
        for directory in sorted(self.new_directories):
            dir_path = self.docs_root / directory.replace("docs/", "")
            if not dir_path.exists():
                if self.dry_run:
                    logger.info(f"[DRY RUN] Would create directory: {dir_path}")
                else:
                    dir_path.mkdir(parents=True, exist_ok=True)
                    logger.info(f"Created directory: {dir_path}")

    def move_files(self):
        """Move files according to the mappings."""
        # Sort mappings to process regular moves before merges
        sorted_mappings = sorted(self.file_mappings.items(), 
                                key=lambda x: (x[1][1] == "merge", x[0]))
        
        for src, (dst, action) in sorted_mappings:
            src_path = self.docs_root / src.replace("docs/", "")
            dst_path = self.docs_root / dst.replace("docs/", "")
            
            # Handle directory mappings
            if src.endswith("/"):
                if src_path.exists() and src_path.is_dir():
                    if self.dry_run:
                        logger.info(f"[DRY RUN] Would move directory: {src_path} -> {dst_path}")
                    else:
                        # Move all files in the directory
                        for file in src_path.glob("**/*.md"):
                            rel_path = file.relative_to(src_path)
                            new_file = dst_path / rel_path
                            new_file.parent.mkdir(parents=True, exist_ok=True)
                            shutil.move(str(file), str(new_file))
                            logger.info(f"Moved: {file} -> {new_file}")
                        
                        for file in src_path.glob("**/*.rst"):
                            rel_path = file.relative_to(src_path)
                            new_file = dst_path / rel_path
                            new_file.parent.mkdir(parents=True, exist_ok=True)
                            shutil.move(str(file), str(new_file))
                            logger.info(f"Moved: {file} -> {new_file}")
                continue
            
            # Handle file mappings
            if not src_path.exists():
                logger.warning(f"Source file not found: {src_path}")
                continue
            
            if action == "move":
                if self.dry_run:
                    logger.info(f"[DRY RUN] Would move: {src_path} -> {dst_path}")
                else:
                    dst_path.parent.mkdir(parents=True, exist_ok=True)
                    shutil.move(str(src_path), str(dst_path))
                    logger.info(f"Moved: {src_path} -> {dst_path}")
                    
            elif action == "merge":
                if dst not in self.merged_files:
                    self.merged_files[dst] = []
                self.merged_files[dst].append(src)
                
                if self.dry_run:
                    logger.info(f"[DRY RUN] Would merge: {src_path} into {dst_path}")
                else:
                    # For merge, we'll append content (implement actual merge logic as needed)
                    logger.info(f"Marked for merge: {src_path} -> {dst_path}")
                    
            elif action == "split":
                if src not in self.split_files:
                    self.split_files[src] = []
                self.split_files[src].append(dst)
                
                if self.dry_run:
                    logger.info(f"[DRY RUN] Would split: {src_path} -> {dst_path}")
                else:
                    # For split, copy to first destination, mark others for manual handling
                    dst_path.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(str(src_path), str(dst_path))
                    logger.info(f"Split (copied): {src_path} -> {dst_path}")

    def handle_merged_files(self):
        """Handle files that need to be merged."""
        for dst, sources in self.merged_files.items():
            dst_path = self.docs_root / dst.replace("docs/", "")
            
            if self.dry_run:
                logger.info(f"[DRY RUN] Would merge {len(sources)} files into {dst_path}")
                for src in sources:
                    logger.info(f"  - {src}")
            else:
                # Create a merged file with content from all sources
                dst_path.parent.mkdir(parents=True, exist_ok=True)
                
                # If destination exists, append to it
                if dst_path.exists():
                    with open(dst_path, 'a') as f:
                        f.write("\n\n---\n\n")
                        f.write(f"## Merged Content\n\n")
                
                for src in sources:
                    src_path = self.docs_root / src.replace("docs/", "")
                    if src_path.exists():
                        with open(src_path, 'r') as f:
                            content = f.read()
                        
                        with open(dst_path, 'a') as f:
                            f.write(f"\n\n### Content from {src}\n\n")
                            f.write(content)
                        
                        # Remove source file after merging
                        src_path.unlink()
                        logger.info(f"Merged and removed: {src_path}")

    def generate_redirects_config(self):
        """Generate the redirects configuration for conf.py."""
        redirect_dict = "redirects = {\n"
        for old_path, new_path in sorted(self.redirects.items()):
            # Skip self-redirects and directory redirects
            if old_path == new_path.replace(".html", ".md"):
                continue
            if old_path.endswith("/"):
                continue
            redirect_dict += f'    "{old_path}": "{new_path}",\n'
        redirect_dict += "}\n"
        
        return redirect_dict

    def update_conf_py(self):
        """Update conf.py with the new redirects."""
        conf_path = self.docs_root / "conf.py"
        
        if not conf_path.exists():
            logger.error("conf.py not found!")
            return
        
        with open(conf_path, 'r') as f:
            content = f.read()
        
        # Find the redirects section
        redirect_pattern = r'redirects = \{[^}]*\}'
        new_redirects = self.generate_redirects_config()
        
        if re.search(redirect_pattern, content, re.DOTALL):
            # Replace existing redirects
            content = re.sub(redirect_pattern, new_redirects.strip(), content, flags=re.DOTALL)
        else:
            # Add redirects before the smartquotes setting
            content = content.replace('# If true, the Docutils Smart Quotes', 
                                    f'{new_redirects}\n# If true, the Docutils Smart Quotes')
        
        if self.dry_run:
            logger.info("[DRY RUN] Would update conf.py with new redirects")
            logger.info(f"Redirect count: {len(self.redirects)}")
        else:
            with open(conf_path, 'w') as f:
                f.write(content)
            logger.info(f"Updated conf.py with {len(self.redirects)} redirects")

    def update_internal_links(self):
        """Update internal links in all documentation files."""
        # Get all markdown and rst files
        all_files = list(self.docs_root.glob("**/*.md")) + list(self.docs_root.glob("**/*.rst"))
        
        # Create reverse mapping of new locations
        new_to_old = {}
        for old, (new, _) in self.file_mappings.items():
            if not old.endswith("/"):
                new_to_old[new.replace("docs/", "")] = old.replace("docs/", "")
        
        for file_path in all_files:
            if not file_path.is_file():
                continue
                
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                original_content = content
                
                # Update {doc} links
                doc_pattern = r'\{doc\}`([^`]+)`'
                
                def replace_doc_link(match):
                    old_link = match.group(1)
                    # Check if this link needs updating
                    for old_path, new_path in self.redirects.items():
                        if old_link.endswith(old_path.replace(".html", "")):
                            new_link = new_path.replace(".html", "")
                            return f'{{doc}}`{new_link}`'
                    return match.group(0)
                
                content = re.sub(doc_pattern, replace_doc_link, content)
                
                # Update markdown links
                md_link_pattern = r'\[([^\]]+)\]\(([^)]+\.md)\)'
                
                def replace_md_link(match):
                    link_text = match.group(1)
                    old_link = match.group(2)
                    
                    # Normalize the link
                    if old_link.startswith("/"):
                        old_link = old_link[1:]
                    
                    # Check if this link needs updating
                    for old_path, new_path in self.redirects.items():
                        if old_link.endswith(old_path):
                            new_link = "/" + new_path.replace(".html", ".md")
                            return f'[{link_text}]({new_link})'
                    return match.group(0)
                
                content = re.sub(md_link_pattern, replace_md_link, content)
                
                # Only write if content changed
                if content != original_content:
                    if self.dry_run:
                        logger.info(f"[DRY RUN] Would update links in: {file_path}")
                    else:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(content)
                        logger.info(f"Updated links in: {file_path}")
                        
            except Exception as e:
                logger.error(f"Error processing {file_path}: {e}")

    def create_index_files(self):
        """Create index files for new directories that need them."""
        index_files = [
            "docs/overview/index.md",
            "docs/overview/features/index.md",
            "docs/overview/use_cases/index.md",
            "docs/overview/case_studies/index.md",
            "docs/user_guide/registry_management/index.md",
            "docs/user_guide/program_management/index.md",
            "docs/user_guide/administration/index.md",
            "docs/developer_guide/index.md",
            "docs/developer_guide/customization/index.md",
            "docs/developer_guide/integrations/index.md",
            "docs/developer_guide/api_usage/index.md",
            "docs/reference/api/index.md",
            "docs/reference/technical/index.md",
        ]
        
        for index_file in index_files:
            index_path = self.docs_root / index_file.replace("docs/", "")
            
            if not index_path.exists():
                section_name = index_path.parent.name.replace("_", " ").title()
                content = f"""# {section_name}

This section contains documentation about {section_name.lower()}.

```{{toctree}}
:maxdepth: 2
:caption: Contents

```
"""
                if self.dry_run:
                    logger.info(f"[DRY RUN] Would create index: {index_path}")
                else:
                    index_path.parent.mkdir(parents=True, exist_ok=True)
                    with open(index_path, 'w') as f:
                        f.write(content)
                    logger.info(f"Created index: {index_path}")

    def run(self):
        """Execute the complete refactoring process."""
        logger.info("Starting OpenSPP documentation refactoring...")
        
        # Load mappings
        self.load_mappings()
        logger.info(f"Loaded {len(self.file_mappings)} file mappings")
        
        # Create directories
        self.create_directories()
        
        # Move files
        self.move_files()
        
        # Handle merged files
        if self.merged_files:
            self.handle_merged_files()
        
        # Create index files
        self.create_index_files()
        
        # Update internal links
        self.update_internal_links()
        
        # Update conf.py
        self.update_conf_py()
        
        logger.info("Refactoring complete!")
        
        # Report on manual actions needed
        if self.split_files:
            logger.warning("\nFiles that need manual splitting:")
            for src, destinations in self.split_files.items():
                logger.warning(f"  {src} -> {', '.join(destinations)}")
        
        if self.merged_files:
            logger.warning("\nFiles that were merged (review content):")
            for dst, sources in self.merged_files.items():
                logger.warning(f"  {dst} <- {', '.join(sources)}")

def main():
    parser = argparse.ArgumentParser(description="Refactor OpenSPP documentation structure")
    parser.add_argument("--dry-run", action="store_true", 
                      help="Show what would be done without making changes")
    parser.add_argument("--docs-root", default="docs", 
                      help="Path to the docs directory (default: docs)")
    
    args = parser.parse_args()
    
    refactorer = DocumentationRefactorer(args.docs_root, dry_run=args.dry_run)
    refactorer.run()

if __name__ == "__main__":
    main()