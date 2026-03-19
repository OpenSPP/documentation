---
openspp:
  doc_status: draft
  products: [registry]
  applies_to:
    - social_registry
    - sp_mis
---

# Registry

**Applies to:** Social Registry, SP-MIS

This guide is for **users** (program staff, operators) who work with the OpenSPP registry.

## Overview

The Registry is the foundation of OpenSPP. It stores information about individuals and groups (households) who may receive benefits from social protection programs. Before someone can receive benefits, they must first be registered.

A **registrant** is any person or group recorded in OpenSPP. Registrants become **beneficiaries** only after they are enrolled in a program.

## What you can do

| Task | Description |
|------|-------------|
| Register individuals | Add new people to the registry |
| Register groups | Create households or other group types |
| Search and filter | Find registrants using various criteria |
| Import data | Bulk load registrants from CSV/Excel files |
| Export data | Download registrant data for analysis or backup |

## User roles

Your access to registry features depends on your role:

| Role | What you can Do |
|------|-----------------|
| **Viewer** | View registry records only |
| **Officer** | View and edit records, create new registrants |
| **Manager** | Full access including delete operations |
| **Administrator** | Full access plus configuration settings |

## Guides in this section

```{toctree}
:maxdepth: 2
:hidden:

register_individual
register_group
search_filter
import_data
export_data
```

### Registration

- {doc}`register_individual` - Add a new individual to the registry
- {doc}`register_group` - Create a household or group and add members

### Data management

- {doc}`search_filter` - Find and filter registrants
- {doc}`import_data` - Bulk import registrants from CSV/Excel
- {doc}`export_data` - Export registrant data

## Key concepts

### Individuals vs groups

| Type | Description | Example |
|------|-------------|---------|
| **Individual** | A single person | Maria Santos, age 35 |
| **Group** | A collection of related individuals | The Santos Household (4 members) |

Groups contain individuals as **members**. One member is typically designated as the **head** of the household.

### Registration vs enrollment

| Stage | Meaning |
|-------|---------|
| **Registered** | Person/group exists in the registry |
| **Enrolled** | Person/group is actively receiving benefits from a program |

You must register someone before you can enroll them in a program.

## Next steps

- {doc}`register_individual` - Start by registering your first individual
- {doc}`register_group` - Then create a group and add members
