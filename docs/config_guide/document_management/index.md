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

Your user account must have **Document Management** access rights. See {doc}`/user_guide/getting_started/administrating_role_based_access` for how to assign the appropriate group to a role.
```

## What you'll find here

- **{doc}`overview`** - Directory structure, categories, file restrictions, and versioning

```{toctree}
:hidden:
:maxdepth: 1

overview
```

## Quick start

1. From the main menu, click **DMS**
2. Navigate to the document management configuration
3. Create **Directories** for organizing documents (e.g., "Program Documents", "Registrant Files")
4. Define **Categories** with allowed file types and size limits
5. Upload documents and they are automatically versioned
