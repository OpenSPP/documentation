---
openspp:
  doc_status: draft
  products: [core]
---

# Document management

This guide is for **implementers** configuring file storage directories, document categories, and file type restrictions.

## Prerequisites

```{important}
The `spp_dms` module must be installed. See {doc}`/get_started/modules/index` for module installation instructions.
```

## What you'll find here

- **{doc}`overview`** - Directory structure, categories, file restrictions, and versioning

```{toctree}
:hidden:
:maxdepth: 1

overview
```

## Quick start

1. Navigate to the document management configuration
2. Create **Directories** for organizing documents (e.g., "Program Documents", "Registrant Files")
3. Define **Categories** with allowed file types and size limits
4. Upload documents and they are automatically versioned
