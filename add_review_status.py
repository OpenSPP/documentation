#!/usr/bin/env python3
"""
Script to add review status frontmatter to all documentation pages.
"""

import os
import re
from pathlib import Path
from datetime import datetime

def get_review_status_for_file(file_path, docs_root):
    """
    Determine the initial review status based on file location and reorganization status.
    """
    rel_path = file_path.relative_to(docs_root)
    
    # Files that were newly created or significantly updated during reorganization
    newly_created_files = {
        'getting_started/installation_pypi.md',
        'overview/case_studies/index.md',
        'overview/features/index.md',
        'developer_guide/customization/index.md',
        'developer_guide/integrations/index.md',
        'developer_guide/api_usage/index.md',
        'reference/api/index.md',
        'reference/technical/index.md',
        'user_guide/registry_management/index.md',
        'user_guide/program_management/index.md',
        'user_guide/administration/index.md',
    }
    
    # Files that were just moved but content is likely still accurate
    simple_moves = {
        'community/',
        'reference/modules/',
        'reference/glossary.rst',
    }
    
    # Files that were merged or significantly restructured
    complex_restructures = {
        'user_guide/',
        'overview/concepts/',
        'developer_guide/customization/',
        'developer_guide/integrations/',
    }
    
    str_path = str(rel_path)
    
    # if str_path in newly_created_files:
    #     return 'approved'  # Newly created files are already reviewed
    # elif any(str_path.startswith(prefix) for prefix in simple_moves):
    #     return 'reviewed'  # Simple moves, content likely accurate
    # elif any(str_path.startswith(prefix) for prefix in complex_restructures):
    #     return 'needs-review'  # Complex changes need review
    # elif str_path.startswith('getting_started/'):
    #     return 'reviewed'  # Installation guides were just updated
    # else:
    return 'needs-review'  # Default: needs review

def has_frontmatter(content):
    """Check if file already has frontmatter."""
    return content.strip().startswith('---')

def add_frontmatter(file_path, docs_root):
    """Add review status frontmatter to a file."""
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return False
    
    # Skip if already has frontmatter
    if has_frontmatter(content):
        print(f"Skipping {file_path} - already has frontmatter")
        return False
    
    # Determine status
    status = get_review_status_for_file(file_path, docs_root)
    today = datetime.now().strftime('%Y-%m-%d')
    
    # Create frontmatter
    frontmatter = f"""---
review-status: {status}
review-date: {today}
reviewer: migration-script
migration-notes: "Added during 2025 documentation reorganization"
---

"""
    
    # Add frontmatter to content
    new_content = frontmatter + content
    
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Added frontmatter to {file_path} (status: {status})")
        return True
    except Exception as e:
        print(f"Error writing {file_path}: {e}")
        return False

def main():
    """Main function to process all documentation files."""
    docs_root = Path(__file__).parent / 'docs'
    
    if not docs_root.exists():
        print(f"Documentation directory not found: {docs_root}")
        return
    
    # Find all markdown and rst files
    md_files = list(docs_root.rglob('*.md'))
    rst_files = list(docs_root.rglob('*.rst'))
    all_files = md_files + rst_files
    
    # Filter out files in _static, _templates, and other system directories
    excluded_dirs = {'_static', '_templates', '_build'}
    
    documentation_files = []
    for file_path in all_files:
        # Check if any part of the path is in excluded directories
        if not any(part in excluded_dirs for part in file_path.parts):
            documentation_files.append(file_path)
    
    print(f"Found {len(documentation_files)} documentation files")
    
    # Statistics
    stats = {
        'processed': 0,
        'skipped': 0,
        'errors': 0,
        'status_counts': {
            'needs-review': 0,
            'reviewed': 0,
            'approved': 0
        }
    }
    
    # Process each file
    for file_path in sorted(documentation_files):
        try:
            # Get status before processing
            status = get_review_status_for_file(file_path, docs_root)
            
            if add_frontmatter(file_path, docs_root):
                stats['processed'] += 1
                stats['status_counts'][status] += 1
            else:
                stats['skipped'] += 1
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            stats['errors'] += 1
    
    # Print summary
    print("\n" + "="*50)
    print("SUMMARY")
    print("="*50)
    print(f"Files processed: {stats['processed']}")
    print(f"Files skipped: {stats['skipped']}")
    print(f"Errors: {stats['errors']}")
    print("\nStatus distribution:")
    for status, count in stats['status_counts'].items():
        print(f"  {status}: {count}")
    
    # Create status dashboard
    create_status_dashboard(docs_root, documentation_files)

def create_status_dashboard(docs_root, all_files):
    """Create a status dashboard page."""
    
    dashboard_content = """---
review-status: needs-review
review-date: {date}
reviewer: migration-script
---

# Documentation Review Status Dashboard

This page tracks the review status of all documentation pages after the 2025 reorganization.

## Status Definitions

- **🟢 Approved**: Content is up-to-date and accurate
- **🟡 Reviewed**: Content has been checked and is likely accurate
- **🔴 Needs Review**: Content needs to be reviewed for accuracy after reorganization
- **🟠 In Review**: Currently being reviewed by someone
- **⚪ Outdated**: Content is known to be outdated

## Review Progress

{progress_section}

## Files by Status

{files_by_status}

---

*Last updated: {date}*
""".format(
        date=datetime.now().strftime('%Y-%m-%d'),
        progress_section="",  # We'll fill this in when we have actual data
        files_by_status=""    # We'll fill this in when we have actual data
    )
    
    dashboard_path = docs_root / 'contributing' / 'review_status_dashboard.md'
    
    try:
        with open(dashboard_path, 'w', encoding='utf-8') as f:
            f.write(dashboard_content)
        print(f"\nCreated status dashboard at: {dashboard_path}")
    except Exception as e:
        print(f"Error creating dashboard: {e}")

if __name__ == '__main__':
    main()