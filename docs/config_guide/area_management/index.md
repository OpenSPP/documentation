---
openspp:
  doc_status: draft
  products: [core]
---

# Area management

This guide is for **implementers** setting up geographic area hierarchies for program targeting, service delivery, and reporting.

## What you'll find here

- **{doc}`overview`** - Area concepts, hierarchy configuration, types, tags, and bulk import
- **{doc}`hdx_integration`** - Import administrative boundaries from the Humanitarian Data Exchange (HDX)

```{toctree}
:hidden:
:maxdepth: 1

overview
hdx_integration
```

## Quick start

1. Navigate to **Area > Areas > Area**
2. Create **Area Types** for each administrative level (e.g., Region, Province, Municipality, Barangay)
3. Create top-level areas and nest child areas under them to build the hierarchy
4. Optionally import boundaries in bulk using the **Area Import** tool or **HDX COD integration**
5. Tag areas with **Area Tags** for custom grouping (e.g., "urban", "conflict-affected")
