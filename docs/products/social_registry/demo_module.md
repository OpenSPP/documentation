---
orphan: true
openspp:
  doc_status: draft
---

# Demo module

```{note}
A dedicated Social Registry demo module is not yet available. The generic OpenSPP demo module (`spp_demo`) can populate the registry with sample registrants for basic exploration, but pre-configured programs, user stories, and approval workflows specific to a social registry use case have not been created yet.

See [Missing documentation](#missing-documentation) below for details.
```

## What `spp_demo` provides

The base demo module (`spp_demo`) can generate sample data for any OpenSPP product, including the Social Registry:

| Item | Description |
|------|-------------|
| Sample registrants | Individuals and households with locale-appropriate names and attributes |
| Configurable volume | Set the number of records to generate |
| Locale support | Generate culturally appropriate data for different countries |
| Geographic distribution | Assign registrants to administrative areas |

## Demo users

The base demo module includes pre-configured users for testing:

| Role | Purpose |
|------|---------|
| Administrator | Full system access |
| Global Registrar | Registry data entry across all areas |
| Local Registrar | Registry data entry in assigned area |
| Viewer | Read-only access for reporting |

## Missing documentation

The following items are not yet available and are planned for a future release:

- **Dedicated Social Registry demo module** — A product-specific demo (`spp_social_registry_demo`) with fixed household stories, pre-configured change request workflows, and realistic registry scenarios has not been developed.
- **Try Social Registry guide** — A step-by-step walkthrough for exploring the Social Registry demo data (equivalent to the {doc}`Try SP-MIS guide </get_started/try_our_products/try_spmis/index>`) does not yet exist.
