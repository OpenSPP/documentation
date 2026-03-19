---
openspp:
  doc_status: draft
---

# HXL Integration

**Module:** `spp_hxl`

## Overview

Humanitarian Exchange Language (HXL) support for data interoperability. Adds HXL hashtag mapping to variables and export profiles for humanitarian coordination.

## Purpose

This module is designed to:

- **Manage HXL hashtags:** Maintain a registry of HXL 1.1 standard and custom hashtags organized by category (geographic, population, indicator, etc.) with format validation.
- **Manage HXL attributes:** Maintain a registry of HXL attributes (e.g., `+f`, `+children`, `+code`) with category classification and format validation.
- **Configure export profiles:** Define reusable export templates that map Odoo model fields to HXL-tagged columns for humanitarian data exchange.
- **Map CEL variables to HXL tags:** Extend CEL variables with HXL hashtag and attribute mappings, controlling import and export behavior per variable.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `spp_security` | Central security definitions for OpenSPP modules |
| `spp_cel_domain` | Write simple CEL-like expressions to filter records (Open... |
| `spp_studio` | No-code customization interface for OpenSPP |
| `spp_vocabulary` | OpenSPP: Vocabulary |

## Key Features

### HXL Hashtag Registry

Stores HXL hashtags with metadata for data interoperability.

| Field | Description |
| --- | --- |
| Hashtag | HXL hashtag string (e.g., `#affected`), must start with `#` |
| Category | Classification such as Geographic, Population, Indicators, OpenSPP Custom |
| Data Type | Expected data type: Text, Number, Date, or Geographic |
| Is Standard | Whether the tag is part of the HXL 1.1 specification |

### HXL Attribute Registry

Stores HXL attributes that modify hashtags.

| Field | Description |
| --- | --- |
| Code | Attribute code (e.g., `+f`, `+children`), must start with `+` |
| Category | Classification such as Gender, Age Group, Data Type, Vocabulary Reference |
| Is Standard | Whether the attribute is part of the HXL 1.1 specification |

### Export Profiles

Pre-configured export templates that map model fields to HXL-tagged columns.

| Field | Description |
| --- | --- |
| Model | Target Odoo model for the export |
| Columns | Ordered list of column definitions with field paths and HXL tags |
| Include HXL Row | Whether to include the HXL hashtag row in exported files |
| Date Format | Python strftime format for date columns |

Each column can specify an HXL tag manually or build one by selecting a hashtag and combining it with attributes. The computed tag is stored for use during export.

### CEL Variable HXL Mapping

Extends CEL variables with HXL interoperability fields:

| Field | Description |
| --- | --- |
| HXL Hashtag | Primary HXL hashtag for the variable |
| HXL Attributes | Attribute string appended to the hashtag |
| HXL Import Action | How to handle during import: map to field, create event, store as variable, or skip |
| Include in HXL Export | Whether to include the variable in HXL-tagged exports |

## Integration

- **spp_cel_domain:** Extends CEL variables (`spp.cel.variable`) with HXL mapping fields for import/export behavior.
- **spp_studio:** Provides the configuration UI context for managing HXL tags and profiles.
- **spp_hxl_area:** This module's hashtag and attribute registries are used by `spp_hxl_area` for area-level HXL data import and aggregation.

```{toctree}
:maxdepth: 1
:hidden:

spp_hxl_area
```
