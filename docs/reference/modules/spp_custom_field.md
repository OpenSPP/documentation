---
openspp:
  doc_status: draft
---

# OpenSPP Custom Fields


## Overview

OpenSPP Custom Fields enables administrators to define and add custom data fields directly to registrant profiles. This module supports tailoring data collection for specific social protection programs by allowing field differentiation by registrant type and providing dedicated sections for program-specific indicators.

## Purpose

This module is designed to:

- **Extend registrant profiles:** Add custom data fields beyond the standard registry fields
- **Differentiate by type:** Configure separate custom fields for individuals versus groups
- **Organize fields into groups:** Create logical groupings for better form organization
- **Support program-specific data:** Capture program indicators and specialized data points

## Module Dependencies

| Module           | Description                              |
| ---------------- | ---------------------------------------- |
| **base**         | Odoo core functionality                  |
| **spp_registry** | Core registry for individuals and groups |
| **spp_security** | Security group management                |

## Key Features

### Custom Field Groups

Organize custom fields into named groups:

| Field       | Description                                     |
| ----------- | ----------------------------------------------- |
| Group Name  | Display name for the field group (translatable) |
| Target Type | Individual or Group fields                      |
| Sequence    | Display order among groups                      |
| Description | Optional description of the group purpose       |
| Active      | Enable/disable the group                        |

### Target Type Configuration

Custom field groups are designated for specific registrant types:

| Target Type | Description                                  |
| ----------- | -------------------------------------------- |
| Individual  | Fields appear on individual registrant forms |
| Group       | Fields appear on group/household forms       |

### Field Group Ordering

Use sequence numbers to control display order:

- Lower sequence numbers appear first
- Groups with the same sequence are sorted by name
- Fields within groups follow their own sequence

## Integration

### With Registry Module

Custom field groups integrate with the registry:

- Groups appear as sections on registrant forms
- Fields are displayed within their designated groups
- Target type filtering ensures correct form display

### With Studio Module

The `spp_studio` module extends custom field capabilities:

- Visual field builder wizard
- CEL expression support for computed fields
- Enhanced field type options
- Logic-based field visibility

### With Programs Module

Custom fields can capture program-specific data:

- Program eligibility indicators
- Benefit calculation inputs
- Compliance tracking fields
- Monitoring and evaluation data

## Data Model

### spp.custom.field.group

| Field       | Type      | Description                                 |
| ----------- | --------- | ------------------------------------------- |
| name        | Char      | Group display name (required, translatable) |
| target_type | Selection | "grp" for Group, "indv" for Individual      |
| sequence    | Integer   | Display order (default: 10)                 |
| description | Text      | Optional description (translatable)         |
| active      | Boolean   | Enable/disable the group                    |

## Use Cases

### Program-Specific Data Collection

| Example               | Custom Fields                             |
| --------------------- | ----------------------------------------- |
| Cash Transfer Program | Bank account details, payment preferences |
| Health Program        | Medical conditions, vaccination status    |
| Education Program     | School enrollment, grade level            |
| Agriculture Program   | Land size, crop types, livestock count    |

### Localization Requirements

Different country deployments may need:

- National ID formats and fields
- Local administrative divisions
- Country-specific demographic data
- Regional program requirements

### Monitoring and Evaluation

Custom fields for M&E purposes:

- Baseline indicator values
- Follow-up assessment data
- Program outcome measurements
- Impact evaluation metrics

## Related Modules

- {doc}`spp_studio` - Visual custom field builder and logic integration
- {doc}`spp_registry` - Core registry functionality
