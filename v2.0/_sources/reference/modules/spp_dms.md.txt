---
openspp:
  doc_status: draft
---

# Document Management System

**Module:** `spp_dms`

## Overview

The OpenSPP Document Management System (DMS) module provides centralized management and organization of program-related documents within a structured directory tree. It enables efficient document storage, retrieval, categorization, and version control with automatic metadata capture.

## Purpose

This module is designed to:

- **Organize documents:** Store files in a hierarchical directory structure
- **Categorize content:** Apply categories with validation rules for file types and sizes
- **Track versions:** Maintain version history with restore capabilities
- **Capture metadata:** Automatically record file size, type, checksums, and thumbnails

## Module Dependencies

| Dependency       | Description                |
| ---------------- | -------------------------- |
| **base**         | Core Odoo framework        |
| **web**          | Web client assets          |
| **spp_security** | OpenSPP security framework |

### External Python Dependencies

| Package    | Description                               |
| ---------- | ----------------------------------------- |
| **Pillow** | Image processing for thumbnails (>=9.0.1) |

## Key Features

### Directory Structure

Directories form a hierarchical tree:

| Field             | Description                 |
| ----------------- | --------------------------- |
| Name              | Directory name              |
| Parent Directory  | Parent in hierarchy         |
| Is Root Directory | Marks top-level directories |
| Complete Name     | Full path (auto-computed)   |
| Active            | Archive toggle              |

Each directory tracks:

- Subdirectory count
- File count
- Total size (computed from all contained files)

### File Management

Files are stored with comprehensive metadata:

| Field      | Description                     |
| ---------- | ------------------------------- |
| Filename   | Display name of the file        |
| Directory  | Parent directory                |
| Category   | Optional categorization         |
| Content    | Binary file content             |
| Extension  | File extension (computed)       |
| MIME Type  | Content type (computed)         |
| Size       | File size in bytes              |
| Human Size | Formatted size (e.g., "2.5 MB") |
| Checksum   | SHA-512 hash for integrity      |
| Path       | Full directory path             |

### File Categories

Categories define rules for files:

| Rule                   | Description                  |
| ---------------------- | ---------------------------- |
| Allowed Extensions     | List of permitted file types |
| Max File Size          | Maximum file size limit      |
| MIME Type Restrictions | Content type validation      |

Files are validated against category rules on save.

### Version Control

When versioning is enabled for a file:

| Feature         | Description                             |
| --------------- | --------------------------------------- |
| Version History | Tracks all changes with version numbers |
| Current Version | Marks the active version                |
| Auto-Versioning | Creates version on content change       |
| Restore         | Revert to any previous version          |

Version records store:

- Version number
- Content snapshot
- Checksum and size
- MIME type
- Comment/description
- Is current flag

### Image Support

For image files, the module provides:

- Automatic thumbnail generation
- Image preview in the UI
- Support for common formats (JPEG, PNG, GIF, SVG)

### Path Navigation

Files and directories compute their full path:

- `path_names`: Human-readable path string
- `path_json`: Structured path for programmatic navigation

## Integration

### Web Assets

The module includes custom JavaScript for:

- Binary field preview
- Enhanced file viewing experience

### Security Framework

Integrates with `spp_security` for:

- Access control to directories and files
- Privilege-based permissions

## Operations

### Directory Operations

| Action                  | Description                           |
| ----------------------- | ------------------------------------- |
| View All Subdirectories | List all directories under this one   |
| View All Files          | List all files in this directory tree |
| Archive                 | Set inactive to hide without deletion |

### File Operations

| Action             | Description                        |
| ------------------ | ---------------------------------- |
| Enable Versioning  | Start tracking versions            |
| Disable Versioning | Stop tracking (versions preserved) |
| View Versions      | See version history                |
| Restore Version    | Revert to previous version         |

### Version Restoration

The restore process:

1. Creates a snapshot of current content (auto-save)
2. Restores content from selected version
3. Creates new version marked as "Restored from version X"

## Configuration

### Creating a Directory Structure

1. Create root directories (set "Is Root Directory" = True)
2. Add subdirectories with parent references
3. Organize by program, document type, or date

### Setting Up Categories

| Field              | Description                |
| ------------------ | -------------------------- |
| Name               | Category display name      |
| Allowed Extensions | e.g., `pdf, doc, docx`     |
| Max Size           | Maximum file size in bytes |

### Enabling File Versioning

1. Open the file record
2. Click "Enable Versioning"
3. Initial version is created automatically

## Technical Details

### Checksum Computation

Files use SHA-512 checksums for:

- Data integrity verification
- Duplicate detection
- Version comparison

### Concurrent Version Handling

Version creation uses atomic SQL operations with retry logic to handle race conditions when multiple users modify the same file.

### Storage

File content is stored as Odoo attachments (`content_file` field), allowing standard Odoo file storage configuration (database or filestore).
