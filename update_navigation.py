#!/usr/bin/env python3
"""Update navigation menus (toctree) in index files after refactoring."""

import os
from pathlib import Path

# Define the content for each index file
index_files = {
    "docs/user_guide/program_management/index.md": {
        "title": "Program Management",
        "description": "This section contains guides for creating and managing social protection programs.",
        "files": [
            "create_program",
            "enroll_beneficiaries", 
            "create_cycle",
            "configure_entitlements",
            "allocate_funds",
            "implementing_pmt",
            "using_pmt",
            "using_geotargeting",
            "using_indicators",
            "using_vouchers",
            "export_beneficiaries",
            "programs_overview"
        ]
    },
    
    "docs/user_guide/administration/index.md": {
        "title": "Administration",
        "description": "This section contains administrative tasks and system management guides.",
        "files": [
            "user_access",
            "service_points", 
            "managing_custom_fields",
            "using_audit_logs",
            "import_areas",
            "hardware_integration"
        ]
    },
    
    "docs/developer_guide/index.md": {
        "title": "Developer Guide", 
        "description": "This section provides technical information and instructions for developers who need to customize, extend, integrate with, or contribute to OpenSPP.",
        "files": [
            "setup",
            "architecture",
            "module_development",
            "best_practices",
            "troubleshooting",
            "developer_mode",
            "i18n_l10n",
            "customization/index",
            "integrations/index", 
            "api_usage/index"
        ]
    },
    
    "docs/developer_guide/customization/index.md": {
        "title": "Customization",
        "description": "This section contains guides for customizing OpenSPP functionality.",
        "files": [
            "customizing_areas",
            "customizing_audit",
            "customizing_change_requests", 
            "customizing_cycles",
            "customizing_entitlements",
            "customizing_fields",
            "customizing_programs",
            "customizing_registry",
            "customizing_service_points",
            "customizing_indicators",
            "implementing_pmt"
        ]
    },
    
    "docs/developer_guide/integrations/index.md": {
        "title": "Integrations",
        "description": "This section contains guides for integrating OpenSPP with external systems.",
        "files": [
            "dci",
            "esignet",
            "oidc", 
            "keycloak_beneficiary_portal",
            "g2p-connect"
        ]
    },
    
    "docs/developer_guide/api_usage/index.md": {
        "title": "API Usage",
        "description": "This section contains guides for using OpenSPP APIs.",
        "files": [
            "rest_api",
            "external_api_xmlrpc"
        ]
    },
    
    "docs/reference/index.md": {
        "title": "Reference",
        "description": "This section provides detailed reference material about OpenSPP components.",
        "files": [
            "modules/index",
            "technical/index", 
            "api/index",
            "glossary"
        ]
    },
    
    "docs/reference/technical/index.md": {
        "title": "Technical Reference", 
        "description": "This section contains detailed technical specifications and references.",
        "files": [
            "security",
            "backup",
            "performance",
            "monitoring",
            "audit_logs",
            "cycle_manager",
            "deduplication_manager", 
            "eligibility_manager",
            "entitlement_manager",
            "notification_manager",
            "program_manager"
        ]
    },
    
    "docs/community/index.md": {
        "title": "Community",
        "description": "This section contains information about the OpenSPP project, community interaction, contribution processes, and legal information.",
        "files": [
            "contributing",
            "code_of_conduct",
            "license",
            "security_reporting",
            "support",
            "release_management",
            "module_lifecycle_development_status",
            "module_lifecycle_maintainer_role"
        ]
    },
    
    "docs/overview/features/index.md": {
        "title": "Features",
        "description": "This section provides an overview of OpenSPP features organized by functional area.",
        "files": [
            "registry_data_management",
            "integrations_apis"
        ]
    },
    
    "docs/overview/use_cases/index.md": {
        "title": "Use Cases", 
        "description": "This section provides entry points for OpenSPP's main use cases.",
        "files": [
            "social_registry",
            "farmer_registry",
            "humanitarian",
            "social-protection-management-information-system"
        ]
    },
    
    "docs/overview/case_studies/index.md": {
        "title": "Case Studies",
        "description": "This section contains examples of OpenSPP implementations and use cases.",
        "files": []
    }
}

def create_index_content(title, description, files):
    """Create content for an index file."""
    content = f"# {title}\n\n{description}\n\n"
    
    if files:
        content += "```{toctree}\n:maxdepth: 2\n:caption: Contents\n\n"
        for file in files:
            content += f"{file}\n"
        content += "```\n"
    else:
        content += "```{toctree}\n:maxdepth: 2\n:caption: Contents\n\n```\n"
    
    return content

def main():
    """Update all index files."""
    for file_path, config in index_files.items():
        path = Path(file_path)
        
        # Create directory if it doesn't exist
        path.parent.mkdir(parents=True, exist_ok=True)
        
        # Create content
        content = create_index_content(
            config["title"],
            config["description"], 
            config["files"]
        )
        
        # Write file
        with open(path, 'w') as f:
            f.write(content)
        
        print(f"Updated: {file_path}")

if __name__ == "__main__":
    main()