---
openspp:
  doc_status: draft
  products: [core]
  applies_to:
    - social_registry
    - sp_mis
    - drims
---

# Geographic Areas

**Applies to:** Social Registry, SP-MIS, DRIMS

## What You'll Find Here

This reference guide explains how geographic areas work in OpenSPP. You'll learn how to:

- Understand the area hierarchy (country, region, district, etc.)
- Use area filters to find registrants
- Read area codes and complete names

## What Are Geographic Areas?

Geographic areas represent locations in a hierarchical structure. They help you:

- Record where beneficiaries live
- Filter registrants by location
- Target programs to specific regions

## Area Hierarchy

Areas are organized in a parent-child hierarchy, up to 10 levels deep. A typical structure looks like:

| Level | Example | Description |
|-------|---------|-------------|
| 0 | Country | Top-level area (no parent) |
| 1 | Region | First subdivision |
| 2 | Province | Second subdivision |
| 3 | District | Third subdivision |
| 4 | Municipality | Fourth subdivision |
| 5 | Barangay/Village | Fifth subdivision |

```{note}
Your OpenSPP system may use different names for each level depending on your country's administrative divisions.
```

## Understanding Area Names

Each area has several name fields:

| Field | Description | Example |
|-------|-------------|---------|
| Name | Area name with code | Quezon City (QC01) |
| Code | Unique identifier | QC01 |
| Complete Name | Full path showing hierarchy | Philippines > NCR > Quezon City (QC01) |
| Alternate Names | Other names for the area | QC, Quezon |

The **Complete Name** shows the full path from the top-level area down to the current area, separated by " > " symbols. This helps you identify exactly where an area is in the hierarchy.

## Area Types

Areas can be classified by type. Common types include:

| Type | Description |
|------|-------------|
| Admin Area | Standard administrative division |

Your administrator may define additional area types specific to your implementation.

## Area Tags

Tags provide additional classification for areas. Tags are used for:

- Identifying urban vs rural areas
- Marking priority zones
- Grouping areas for reporting

Common tags might include: Urban, Rural, Remote, Priority, Conflict-Affected.

## Viewing Areas in the System

To view the list of areas:

1. Click **Area** in the main menu
2. Click **Areas** > **Area**

The list shows:

| Column | Description |
|--------|-------------|
| Name | Area name |
| Code | Area code |
| Parent | Parent area |
| Complete Name | Full hierarchy path |
| Level | Depth in hierarchy (0 = top level) |
| Type | Area classification |

## Using Area Filters

When searching for registrants, you can filter by area:

1. Open the **Registry** (Individuals or Groups)
2. Click the search box
3. Select an area field filter
4. Choose the area from the dropdown

The area dropdown shows:

- The complete name (full path) to help you identify the correct area
- Areas are filtered based on your access permissions

## How Areas Appear in Forms

When registering a beneficiary, you select their area from a dropdown. The dropdown shows areas you have permission to access.

| Form Field | What to Select |
|------------|----------------|
| Area | The beneficiary's location (usually their residence) |

## Are You Stuck?

**Can't find an area in the dropdown?**

- You may not have permission to access that area. Contact your administrator.
- The area may not exist in the system. Ask your administrator to add it.
- Try searching by the area code instead of the name.

**Not sure which area to select?**

- Look at the complete name to see the full hierarchy path.
- Ask the beneficiary to confirm their administrative division.
- Check identity documents that show the address.

**Area shows wrong parent?**

- Contact your administrator. Area hierarchy is managed by system administrators.

## Related Topics

- Registering individuals (see User Guides)
- Filtering beneficiaries by location (see User Guides)
