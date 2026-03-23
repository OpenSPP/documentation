---
openspp:
  doc_status: draft
---

# Storage Backend

**Module:** `spp_storage_backend`

## Overview

Pluggable storage backend configuration for OpenSPP file storage

## Purpose

This module is designed to:

- **Configure pluggable file storage:** Define multiple storage backends (Odoo default, S3, Azure Blob, external filesystem) and switch between them without code changes.
- **Store and retrieve files:** Provide a unified API for storing, retrieving, and deleting files across different storage providers.
- **Generate temporary access URLs:** Create presigned/SAS URLs for secure, time-limited file access on S3 and Azure backends.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `base` | Odoo core framework |
| `spp_security` | Central security definitions for OpenSPP modules |

## Key Features

### Supported Backend Types

| Backend Type | Description | Required Configuration |
| --- | --- | --- |
| Odoo Default | Standard Odoo filestore/database storage | None |
| Amazon S3 / S3-Compatible | S3 or MinIO object storage | Bucket, Access Key, Secret Key, Region, optional Endpoint URL |
| Azure Blob Storage | Microsoft Azure Blob containers | Connection String, Container Name |
| External Filesystem | File storage on a mounted directory | Absolute base path |

### Storage Operations

Each backend provides a consistent interface:

| Operation | Description |
| --- | --- |
| `store(binary_data, path)` | Store binary data and return a storage reference |
| `retrieve(reference)` | Retrieve binary data by its storage reference |
| `delete(reference)` | Delete a file by its storage reference |
| `get_public_url(reference, expires_in)` | Generate a time-limited public URL (S3 and Azure only) |
| `test_connection()` | Verify the backend is accessible and properly configured |

### Default Backend

One backend can be designated as the default. The `get_default_backend()` method returns the default active backend, falling back to the first active Odoo backend, then any active backend.

### Security

- Only one backend can be marked as default (enforced by database constraint).
- S3, Azure, and filesystem backends validate required configuration fields before saving.
- Filesystem backend validates that the base path is absolute and prevents path traversal attacks.
- Connection testing is available via a UI button to verify backend accessibility before use.

## Integration

- **spp_security:** Uses OpenSPP security groups for access control to storage backend configuration.
- Other OpenSPP modules can use `spp.storage.backend` to store and retrieve files (e.g., attachments, exports, scan results) through the unified storage API.
