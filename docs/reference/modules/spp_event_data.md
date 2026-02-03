---
openspp:
  doc_status: draft
---

# Event Data


## Overview

The OpenSPP Event Data module records and tracks events related to individual and group registrants. It captures data from surveys, field visits, manual entries, and external systems like ODK Central and KoBoToolbox, providing a flexible framework for managing time-sensitive registrant information.

## Purpose

This module is designed to:

- **Record registrant events:** Capture surveys, assessments, field visits, and other data collection activities
- **Integrate external sources:** Pull data from ODK Central, KoBoToolbox, and other external systems
- **Manage event lifecycle:** Handle event states including approval workflows, expiration, and supersession
- **Support flexible data storage:** Store event data in JSON format, dedicated models, or custom fields

## Module Dependencies

| Dependency          | Description                                |
| ------------------- | ------------------------------------------ |
| **base**            | Core Odoo framework                        |
| **mail**            | Messaging and activity tracking            |
| **spp_registry**    | OpenSPP registry for registrant management |
| **spp_base_common** | Common OpenSPP utilities                   |
| **spp_security**    | OpenSPP security framework                 |
| **spp_approval**    | Approval workflow support                  |

## Key Features

### Event Types

Event types define the structure and behavior of events:

| Field       | Description                     |
| ----------- | ------------------------------- |
| Name        | Display name for the event type |
| Code        | Unique identifier code          |
| Category    | survey, visit, sync, or manual  |
| Target Type | individual, group, or both      |
| Source Type | internal, odk, kobo, or api     |

### Event Categories

| Category              | Description                             |
| --------------------- | --------------------------------------- |
| **Survey/Assessment** | Structured data collection forms        |
| **Field Visit**       | In-person visits and observations       |
| **External Sync**     | Data synchronized from external systems |
| **Manual Entry**      | Ad-hoc data entered by users            |

### Data Storage Modes

Event data can be stored in three ways:

| Mode                | Use Case          | Description                                  |
| ------------------- | ----------------- | -------------------------------------------- |
| **Dedicated Model** | Structured data   | Links to a specific Odoo model               |
| **JSON Storage**    | Flexible data     | Stores data as JSON in `data_json` field     |
| **Custom Fields**   | Configured fields | Uses field definitions from the Configurator |

### Event State Machine

| State          | Description                   |
| -------------- | ----------------------------- |
| **Draft**      | Initial state, not yet active |
| **Pending**    | Awaiting approval             |
| **Active**     | Current valid event           |
| **Superseded** | Replaced by a newer event     |
| **Expired**    | Past expiration date          |
| **Cancelled**  | Manually cancelled            |

### Lifecycle Rules

Event types can define automatic lifecycle behavior:

| Rule                      | Description                                               |
| ------------------------- | --------------------------------------------------------- |
| One Active Per Registrant | New events automatically supersede previous active events |
| Auto-Expire Days          | Events expire after N days (0 = never)                    |
| Requires Approval         | Events must go through approval workflow                  |

### External Source Configuration

For ODK/KoBoToolbox integration:

| Field               | Description                            |
| ------------------- | -------------------------------------- |
| Form ID             | External form identifier               |
| Server URL          | ODK/Kobo server address                |
| Project ID          | Project identifier                     |
| Registrant ID Field | Field containing registrant identifier |
| ID Type             | How to match registrant (ID type)      |

### Field Mapping

Map external fields to internal event data:

| Transform           | Description                 |
| ------------------- | --------------------------- |
| Direct Copy         | Use value as-is             |
| Parse Date          | Convert to date format      |
| Parse Datetime      | Convert to datetime format  |
| Parse Integer/Float | Convert to number           |
| Parse Boolean       | Convert to true/false       |
| Lookup Reference    | Find related record         |
| CEL Expression      | Apply custom transformation |

## Integration

### With spp_approval

Events requiring approval use the approval mixin:

1. Event type configures approval definition
2. New events are submitted for approval
3. Approved events are activated
4. Rejected events are cancelled

### With spp_change_request (optional)

When installed, events can automatically create change requests:

- Configure field mappings between event data and registrant fields
- Compare modes: always, different, or empty
- Change requests capture proposed updates for review

### With External Systems

The module provides connector interfaces for:

- ODK Central form submissions
- KoBoToolbox survey responses
- Generic API endpoints

## Event Data Record

Each event data record contains:

| Section        | Fields                                  |
| -------------- | --------------------------------------- |
| **Core**       | Event type, Registrant, Name            |
| **Collection** | Date, Collector (user or name)          |
| **State**      | Current state, Supersedes/Superseded by |
| **Data**       | JSON data, Data record reference        |
| **Source**     | Source type, Reference, URL, Raw data   |
| **Expiry**     | Expiry date, Is expired flag            |

### Data Display

Event data is rendered as formatted HTML in the UI:

- Nested JSON is displayed hierarchically
- Values are formatted by type (boolean badges, numbers highlighted)
- Labels are converted from `snake_case` to Title Case

## Configuration

### Creating an Event Type

| Field       | Required | Default  |
| ----------- | -------- | -------- |
| Name        | Yes      | -        |
| Code        | Yes      | -        |
| Category    | Yes      | survey   |
| Target Type | Yes      | both     |
| Source Type | Yes      | internal |

### Recording an Event

Use the "Create Event" wizard to record events:

1. Select the registrant
2. Choose the event type
3. Enter collection date and collector
4. Fill in event data
5. Save (goes to draft) or submit for approval

## Scheduled Actions

| Cron Job      | Description                                                |
| ------------- | ---------------------------------------------------------- |
| Expire Events | Automatically expires active events past their expiry date |

## Technical Details

### Hooks

The module provides installation hooks:

- `post_init_hook`: Runs after module installation
- `uninstall_hook`: Cleanup when module is removed
