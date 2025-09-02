#!/usr/bin/env python3
"""
Update module documentation titles based on __manifest__.py files.

This script:
1. Scans all submodule directories for modules with __manifest__.py files
2. Extracts the "name" field from each manifest
3. Removes prefixes like "G2P", "SPP", "OpenG2P", "OpenSPP" from titles
4. Updates the corresponding documentation files with clean titles
"""

import ast
import os
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple


def clean_module_name(name: str) -> str:
    """Clean module name by removing OpenSPP and SPP prefixes only."""
    prefixes = ["OpenSPP ", "SPP "]  # Keep G2P and OpenG2P prefixes
    for prefix in prefixes:
        if name.startswith(prefix):
            name = name[len(prefix):]
    return name.strip()


def extract_name_from_manifest(manifest_path: Path) -> Optional[str]:
    """Extract the 'name' field from a module's __manifest__.py file."""
    try:
        with open(manifest_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Parse the manifest dictionary
        parsed = ast.literal_eval(content)
        if isinstance(parsed, dict) and 'name' in parsed:
            return clean_module_name(parsed['name'])
    except Exception as e:
        print(f"Error reading {manifest_path}: {e}")
    return None


def find_all_modules(submodules_dir: Path) -> Dict[str, str]:
    """Find all modules in submodules directories and extract their names."""
    modules = {}
    
    # Search through all submodule directories
    for submodule_path in submodules_dir.iterdir():
        if not submodule_path.is_dir():
            continue
            
        # Look for modules in this submodule directory
        for item in submodule_path.iterdir():
            if not item.is_dir():
                continue
                
            manifest_path = item / "__manifest__.py"
            if manifest_path.exists():
                module_name = item.name
                display_name = extract_name_from_manifest(manifest_path)
                if display_name:
                    modules[module_name] = display_name
                    print(f"Found module: {module_name} -> {display_name}")
    
    return modules


def update_module_doc(doc_path: Path, clean_title: str) -> bool:
    """Update the title in a module documentation file."""
    if not doc_path.exists():
        print(f"Documentation file not found: {doc_path}")
        return False
    
    try:
        with open(doc_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file already has MyST frontmatter
        if content.startswith('---\n'):
            # Update existing frontmatter title
            lines = content.split('\n')
            updated = False
            in_frontmatter = False
            
            for i, line in enumerate(lines):
                if i == 0 and line == '---':
                    in_frontmatter = True
                elif in_frontmatter and line == '---':
                    in_frontmatter = False
                elif in_frontmatter and '"title":' in line:
                    # Update title line
                    lines[i] = f'    "title": "{clean_title}"'
                    updated = True
                    break
            
            if updated:
                new_content = '\n'.join(lines)
                with open(doc_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated title in {doc_path.name}")
                return True
        
        # Check for H1 heading to update
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if line.startswith('# '):
                # Update the H1 heading
                lines[i] = f"# {clean_title}"
                new_content = '\n'.join(lines)
                with open(doc_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated H1 title in {doc_path.name}")
                return True
        
        print(f"No title found to update in {doc_path.name}")
        return False
        
    except Exception as e:
        print(f"Error updating {doc_path}: {e}")
        return False


def main():
    """Main function to update all module documentation titles."""
    # Get project root directory
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    # Define paths
    submodules_dir = project_root / "submodules"
    docs_modules_dir = project_root / "docs" / "reference" / "modules"
    
    if not submodules_dir.exists():
        print(f"Submodules directory not found: {submodules_dir}")
        return
    
    if not docs_modules_dir.exists():
        print(f"Module docs directory not found: {docs_modules_dir}")
        return
    
    print("Finding all modules in submodules...")
    modules = find_all_modules(submodules_dir)
    
    if not modules:
        print("No modules found!")
        return
    
    print(f"\nFound {len(modules)} modules. Updating documentation...")
    updated_count = 0
    
    for module_name, clean_title in modules.items():
        doc_path = docs_modules_dir / f"{module_name}.md"
        if update_module_doc(doc_path, clean_title):
            updated_count += 1
    
    print(f"\nUpdated {updated_count} module documentation files.")


if __name__ == "__main__":
    main()