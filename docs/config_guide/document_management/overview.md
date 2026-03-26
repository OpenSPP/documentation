---
openspp:
  doc_status: draft
  products: [core]
---

# Document management overview

This guide is for **implementers** setting up document storage in OpenSPP. You should understand your organization's document management needs but don't need programming knowledge.

## Mental model

Document management in OpenSPP has three layers:

| Layer | What it does | Example |
|-------|--------------|---------|
| **Directory** | Hierarchical folder structure | "Programs / Cash Transfer / Policies" |
| **Category** | Classification with file restrictions | "Official Documents - PDF only, max 10MB" |
| **File** | Individual document with versioning | "Enrollment Policy v3.pdf" |

Think of it like a filing cabinet: **directories** are the drawers and folders, **categories** are the labels that say what goes where and what's allowed, and **files** are the actual documents with a version history.

## Key concepts

### Directories

| Field | What it means |
|-------|---------------|
| **Name** | Folder name |
| **Parent** | Parent directory for hierarchy |
| **Category** | Default category for files in this directory |

Directories can be nested to any depth to organize documents logically.

### Categories

Categories restrict what files can be stored:

| Field | What it means |
|-------|---------------|
| **Name** | Category label (e.g., "Official Documents") |
| **Allowed Extensions** | File types allowed (e.g., pdf, docx, xlsx) |
| **Blocked Extensions** | File types blocked |
| **Allowed File Formats** | Additional file format restrictions |
| **Max Size (MB)** | Maximum file size |

### File versioning

When a file is re-uploaded, the system:
1. Keeps the previous version in the version history
2. Sets the new upload as the current version
3. Allows reverting to any previous version

## Setting up document management

### Step 1: Plan your directory structure

Common patterns:

| Directory | Purpose |
|-----------|---------|
| Program Documents | Policies, guidelines, reports per program |
| Registrant Files | ID documents, certificates, assessments |
| Operations | SOPs, training materials, forms |
| Audit | Audit reports, compliance documents |

### Step 2: Create categories

1. Navigate to document **Configuration > Categories**
2. Create categories with appropriate restrictions:

| Category | Allowed Types | Max Size |
|----------|--------------|----------|
| ID Documents | pdf, jpg, png | 5 MB |
| Reports | pdf, docx, xlsx | 20 MB |
| Photos | jpg, png, heic | 10 MB |
| Policies | pdf | 15 MB |

### Step 3: Create directories

1. Create top-level directories
2. Nest sub-directories as needed
3. Assign default categories to directories

## Are You Stuck?

**Upload fails with "file type not allowed"?**

Check the category's **Allowed Extensions**. The file type must be in the allowed list (or not in the blocked list).

**File too large?**

Check the category's **Max Size** setting. Increase it or compress the file before uploading.

**Can I recover a deleted file?**

Deleted files are not recoverable through the UI. Use database backups for recovery.

**How do I find a specific document?**

Use the search bar to filter by filename, category, directory, or upload date.

## Next steps

- {doc}`/config_guide/storage_backend/overview` - Configure where files are physically stored
- {doc}`/config_guide/audit/overview` - Track document access
