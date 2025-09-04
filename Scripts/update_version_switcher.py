#!/usr/bin/env python3
"""
ABOUTME: Script to update version switcher JSON for multi-version documentation
ABOUTME: Manages version list for sphinx-book-theme version switcher dropdown
"""

import json
import sys
import argparse
import tempfile
import shutil
import os
import re
from pathlib import Path


def get_secure_switcher_path():
    """Get the switcher.json path with security validation.
    
    Returns:
        Path object for switcher.json
        
    Raises:
        ValueError: If path validation fails
    """
    base_path = Path(__file__).parent.parent
    switcher_path = base_path / "docs" / "_static" / "switcher.json"
    
    # Ensure path is within expected directory (prevent directory traversal)
    try:
        switcher_path.resolve().relative_to(base_path.resolve())
    except ValueError:
        raise ValueError("Invalid path: potential directory traversal detected")
    
    return switcher_path


def validate_inputs(version=None, name=None, url=None):
    """Validate input parameters for security.
    
    Args:
        version: Version identifier to validate
        name: Display name to validate  
        url: URL to validate
        
    Returns:
        True if all inputs are valid
        
    Raises:
        ValueError: If any input is invalid
    """
    if version and not re.match(r'^[a-zA-Z0-9._-]+$', version):
        raise ValueError(f"Invalid version format: {version}")
    
    if url:
        if not url.startswith(('http://', 'https://')):
            raise ValueError(f"Invalid URL format: {url}")
        # Basic URL validation to prevent injection
        if any(char in url for char in ['"', "'", '<', '>', '\n', '\r']):
            raise ValueError(f"Invalid characters in URL: {url}")
    
    if name:
        # Prevent script injection in display names
        if any(char in name for char in ['<', '>', '"', "'"]):
            raise ValueError(f"Invalid characters in name: {name}")
    
    return True


def atomic_json_write(path, data):
    """Write JSON data atomically to prevent corruption.
    
    Args:
        path: Path object for target file
        data: Data to write as JSON
    """
    # Create temp file in same directory for atomic rename
    temp_fd, temp_path = tempfile.mkstemp(
        dir=path.parent,
        prefix='.tmp_',
        suffix='.json'
    )
    
    try:
        with os.fdopen(temp_fd, 'w') as tmp:
            json.dump(data, tmp, indent=2)
            tmp.flush()
            os.fsync(tmp.fileno())
        
        # Atomic rename
        shutil.move(temp_path, path)
    except Exception:
        # Clean up temp file on error
        if os.path.exists(temp_path):
            os.unlink(temp_path)
        raise


def update_version_switcher(action, version=None, name=None, url=None):
    """Update the version switcher JSON file.
    
    Args:
        action: 'add', 'remove', or 'list'
        version: Version identifier (e.g., 'stable', '1.1', 'feature-xyz')
        name: Display name for the version
        url: URL for the version documentation
    """
    switcher_path = get_secure_switcher_path()
    
    # Load existing versions
    if switcher_path.exists():
        with open(switcher_path, 'r') as f:
            versions = json.load(f)
    else:
        versions = []
    
    if action == 'list':
        print(json.dumps(versions, indent=2))
        return
    
    if action == 'add':
        if not all([version, name, url]):
            print("Error: version, name, and url are required for 'add' action")
            sys.exit(1)
        
        # Validate inputs for security
        try:
            validate_inputs(version, name, url)
        except ValueError as e:
            print(f"Error: {e}")
            sys.exit(1)
        
        # Remove existing entry with same version if exists
        versions = [v for v in versions if v['version'] != version]
        
        # Add new version entry
        new_entry = {
            "name": name,
            "version": version,
            "url": url
        }
        
        # Insert preview versions after stable but before releases
        if "preview" in url.lower():
            # Find position after stable version
            stable_index = 0
            for i, v in enumerate(versions):
                if v['version'] == 'stable':
                    stable_index = i + 1
                    break
            versions.insert(stable_index, new_entry)
        else:
            versions.append(new_entry)
    
    elif action == 'remove':
        if not version:
            print("Error: version is required for 'remove' action")
            sys.exit(1)
        
        # Validate version format
        try:
            validate_inputs(version=version)
        except ValueError as e:
            print(f"Error: {e}")
            sys.exit(1)
            
        versions = [v for v in versions if v['version'] != version]
    
    else:
        print(f"Error: Unknown action '{action}'")
        sys.exit(1)
    
    # Save updated versions using atomic write
    try:
        atomic_json_write(switcher_path, versions)
    except Exception as e:
        print(f"Error writing file: {e}")
        sys.exit(1)
    
    print(f"Updated version switcher: {action} {version if version else ''}")


def main():
    parser = argparse.ArgumentParser(description='Update version switcher for documentation')
    parser.add_argument('action', choices=['add', 'remove', 'list'],
                        help='Action to perform')
    parser.add_argument('--version', help='Version identifier')
    parser.add_argument('--name', help='Display name for the version')
    parser.add_argument('--url', help='URL for the version documentation')
    
    args = parser.parse_args()
    
    update_version_switcher(args.action, args.version, args.name, args.url)


if __name__ == '__main__':
    main()