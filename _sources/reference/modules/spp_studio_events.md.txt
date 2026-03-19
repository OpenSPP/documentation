---
openspp:
  doc_status: draft
---

# Studio - Events

**Module:** `spp_studio_events`

## Overview

OpenSPP Studio - Events provides a user-friendly interface for creating custom event types without code. Event types define data collection forms that can be recorded against individuals or groups, enabling program staff to design surveys, assessments, and field data collection workflows.

## Purpose

This module is designed to:

- **Enable no-code event type design:** Create custom data collection forms through a visual wizard
- **Define custom fields:** Add text, numbers, dates, selections, and linked records to event forms
- **Configure target registrants:** Specify whether events apply to individuals, groups, or both
- **Organize fields into tabs:** Group related fields for better form organization
- **Integrate with external tools:** Optionally connect to Kobo forms for field data collection
- **Set up approval workflows:** Configure approval requirements for event data

## Module Dependencies

| Module             | Description                                   |
| ------------------ | --------------------------------------------- |
| **spp_studio**     | Core Studio interface and mixin functionality |
| **spp_event_data** | Event data infrastructure and storage         |

## Key Features

### Visual Event Type Builder

A three-step wizard for creating event types:

| Step             | Description                               |
| ---------------- | ----------------------------------------- |
| Basic Info       | Name, description, and target type        |
| Field Definition | Add and configure custom fields           |
| Options          | Approval settings and integration options |

### Supported Field Types

| Field Type   | Description              | Use Case                 |
| ------------ | ------------------------ | ------------------------ |
| Text         | Single-line text input   | Names, short answers     |
| Long Text    | Multi-line text area     | Comments, descriptions   |
| Integer      | Whole numbers            | Counts, quantities       |
| Decimal      | Numbers with decimals    | Measurements, amounts    |
| Date         | Date picker              | Event dates, deadlines   |
| Date & Time  | Date and time picker     | Appointments, timestamps |
| Yes/No       | Boolean toggle           | Binary questions         |
| Selection    | Single-choice dropdown   | Categories, status       |
| Multi-Select | Multiple choice          | Tags, multiple options   |
| Link         | Related record reference | Link to other models     |

### Field Configuration Options

Each field can be configured with:

| Option                 | Description                           |
| ---------------------- | ------------------------------------- |
| Required               | Field must be filled before saving    |
| Help Text              | Guidance shown to users               |
| Sequence               | Display order in the form             |
| Validation             | Range limits or pattern matching      |
| Conditional Visibility | Show/hide based on other field values |

### Field Groups (Tabs)

Organize fields into logical groups displayed as tabs:

- Create named groups (e.g., "Personal Info", "Medical History")
- Assign fields to groups
- Set group display sequence
- Ungrouped fields appear in a "General" tab

### Validation Rules

Configure field-level validation:

| Validation Type | Applicable To    | Description                 |
| --------------- | ---------------- | --------------------------- |
| Range           | Numbers          | Minimum and maximum values  |
| Pattern (Regex) | Text             | Regular expression matching |
| Selection       | Selection fields | Valid option enforcement    |

### Conditional Visibility

Show or hide fields based on other field values:

| Condition      | Description                            |
| -------------- | -------------------------------------- |
| Is Set         | Show when another field has a value    |
| Is Not Set     | Show when another field is empty       |
| Equals         | Show when another field equals a value |
| Does Not Equal | Show when another field differs        |

### Target Use Cases

| Use Case                  | Description                         |
| ------------------------- | ----------------------------------- |
| Health Screenings         | Medical assessments and vital signs |
| Household Visits          | Home inspection and verification    |
| Surveys                   | Questionnaires and assessments      |
| Field Inspections         | On-site verification activities     |
| Data Collection Campaigns | Bulk data gathering exercises       |

## Integration

### With Event Data Module

When activated, Studio event types create:

- `spp.event.type` record for the event definition
- `spp.event.field` records for each custom field
- Dynamic wizard fields on `spp.event.data.entry.wizard`
- Generated form view for the entry wizard

### With Kobo Integration

Optional connection to Kobo Toolbox:

- Store Kobo Form ID for reference
- Enable field data collection via Kobo
- Sync data back to OpenSPP events

### With Approval Module

Configure approval workflows for event data:

- Require approval before events become active
- Link to approval definition for workflow steps
- Events enter pending state until approved

### With Registry Module

Events are recorded against registrants:

- Individual-targeted events
- Group/household-targeted events
- Events applicable to both types

## Lifecycle Management

Event types follow a safe editing lifecycle:

| State    | Can Edit | Can Record Events |
| -------- | -------- | ----------------- |
| Draft    | Yes      | No                |
| Active   | No       | Yes               |
| Inactive | Yes      | No                |

When deactivating:

- Existing events are preserved
- Event type becomes hidden from new entry
- Can reactivate to resume data collection

## Auto-Generated Components

When a Studio event type is activated:

1. **spp.event.type** - The underlying event type record
2. **spp.event.field** - Field definitions for each custom field
3. **ir.model.fields** - Dynamic fields on the entry wizard
4. **ir.ui.view** - Custom form view for the entry wizard

## Related Modules

- {doc}`spp_studio` - Core Studio interface
- {doc}`spp_event_data` - Event data infrastructure
