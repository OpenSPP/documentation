---
openspp:
  doc_status: draft
  products: [core]
---

# Import matching

This guide is for **implementers** configuring deduplication rules that prevent duplicate records during bulk data imports.

## What you'll find here

- **{doc}`overview`** - Import matching concepts, rules, field selection, and conditional logic

```{toctree}
:hidden:
:maxdepth: 1

overview
```

## Quick start

1. Navigate to **Configuration > Import Match**
2. Create a **Matching Rule** for the target model (e.g., registrants)
3. Select the **Fields** to match on (e.g., national ID, phone number)
4. Optionally add **Conditional Logic** (e.g., only match if status = active)
5. Set **Overwrite** behavior for matched records
