---
openspp:
  doc_status: draft
---

# OpenSPP Change Request V2


## Overview

OpenSPP Change Request V2 is a configuration-driven change request system with UX improvements, conflict detection, and duplicate prevention. It provides a structured workflow for managing updates to registrant information, ensuring data quality through approval processes and validation rules.

## Purpose

This module is designed to:

- **Manage registrant updates:** Provide a governed process for modifying registry data
- **Enable flexible CR types:** Configure different change request types for various update scenarios
- **Detect conflicts:** Identify conflicting or duplicate change requests
- **Support approval workflows:** Integrate with approval processes for change governance
- **Apply changes automatically:** Auto-update registrant records when requests are approved
- **Track document uploads:** Attach supporting documents to change requests

## Module Dependencies

| Module              | Description                                |
| ------------------- | ------------------------------------------ |
| **spp_base_common** | Common utilities and base functionality    |
| **spp_registry**    | Core registry for individuals and groups   |
| **spp_security**    | Security groups and privileges             |
| **spp_approval**    | Approval workflow infrastructure           |
| **spp_event_data**  | Event data integration                     |
| **spp_dms**         | Document management for attachments        |
| **spp_vocabulary**  | Controlled vocabularies for document types |
| **mail**            | Messaging and activity tracking            |

## Key Features

### Change Request Types

Configuration-driven CR types with flexible options:

| Setting           | Description                                |
| ----------------- | ------------------------------------------ |
| Name/Code         | Unique identifier and display name         |
| Target Type       | Individual, Group, or Both                 |
| Detail Model      | Technical model for storing change details |
| Apply Strategy    | Field mapping, custom method, or manual    |
| Approval Workflow | Optional approval definition               |

### Apply Strategies

Three strategies for applying approved changes:

| Strategy      | Description                        | Use Case                |
| ------------- | ---------------------------------- | ----------------------- |
| Field Mapping | Map source fields to target fields | Simple field updates    |
| Custom        | Call custom Python method          | Complex transformations |
| Manual        | User applies changes manually      | Review-only scenarios   |

### Field Mapping Configuration

For field mapping strategy:

- Define source field (from detail model)
- Define target field (on registrant)
- Set field sequence for ordering
- Supports all standard field types

### Conflict Detection

Identify potentially conflicting change requests:

| Feature             | Description                              |
| ------------------- | ---------------------------------------- |
| Conflict Rules      | Define what constitutes a conflict       |
| Automatic Detection | Check on CR creation and submission      |
| Conflict Comparison | Side-by-side view of conflicting changes |
| Resolution Wizard   | Tools for resolving conflicts            |

### Duplicate Prevention

Prevent duplicate change requests:

- Configure duplicate detection rules
- Check against pending requests
- Warning or blocking modes
- Customizable matching criteria

### Document Requirements

Configure required supporting documents:

| Setting             | Description                         |
| ------------------- | ----------------------------------- |
| Available Documents | Document types that can be uploaded |
| Required Documents  | Subset that must be uploaded        |
| Validation Mode     | None, Warning, or Required          |

### Required Field Validation

Mark fields as required for submission:

- Select from available detail model fields
- Validate before submission
- Block submission if fields are empty

### Three-Tier Customization Model

CR types support different editability levels:

| Flag             | Description                          |
| ---------------- | ------------------------------------ |
| Studio Editable  | Can be modified via Studio UI        |
| Studio Cloneable | Can be cloned to create variants     |
| System Type      | Defined by module, cannot be deleted |

## Change Request Workflow

Standard change request lifecycle:

| State     | Description                     |
| --------- | ------------------------------- |
| Draft     | Initial creation, can be edited |
| Pending   | Submitted for approval          |
| Approved  | Approved, ready to apply        |
| Applied   | Changes applied to registrant   |
| Rejected  | Request denied                  |
| Cancelled | Request cancelled               |

## Built-in CR Types

The module provides infrastructure for CR types. Actual type definitions are provided by:

- **spp_cr_types_base** - Basic types (edit individual, edit group, update ID)
- **spp_cr_types_advanced** - Complex types (add member, change head of household)

## Integration

### With Registry Module

Change requests modify `res.partner` records:

- Link to target registrant
- Access registrant data for validation
- Apply changes to registry fields
- Track change history

### With Approval Module

Approval workflow integration:

- Link CR types to approval definitions
- Support multi-step approvals
- Batch approval capabilities
- Approval queue management

### With DMS Module

Document management integration:

- Dedicated directories for CR documents
- Document upload wizard
- Document type categorization
- Attachment tracking

### With Event Data Module

Event-based change request creation:

- Auto-create CRs from events
- Auto-approve from event data
- Link CRs to source events

## Security Groups

| Group        | Permissions                         |
| ------------ | ----------------------------------- |
| CR User      | Create and view own requests        |
| CR Validator | Review and approve requests         |
| CR Manager   | Full access including configuration |

## UX Improvements

Enhanced user experience features:

- Create wizard with registrant search
- Batch approval wizard
- Conflict comparison wizard
- Change preview before apply
- Queue views for workload management

## Related Modules

- {doc}`spp_cr_types_base` - Basic change request types
- {doc}`spp_studio_change_requests` - No-code CR type builder
- {doc}`spp_approval` - Approval workflow infrastructure
