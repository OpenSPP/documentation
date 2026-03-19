---
openspp:
  doc_status: draft
---

# Studio - Change Requests

**Module:** `spp_studio_change_requests`

## Overview

OpenSPP Studio - Change Requests provides a user-friendly interface for creating custom change request types without code. It allows program staff to configure simple field-based change requests with approval workflows, enabling registrants to update their information through a governed process.

## Purpose

This module is designed to:

- **Enable no-code CR type creation:** Build custom change request types through a visual wizard
- **Configure field mappings:** Select which registry fields can be updated through each request type
- **Set up approval workflows:** Define who can approve changes and how
- **Manage CR type lifecycle:** Safely edit configurations through draft/active states
- **Auto-apply approved changes:** Automatically update registrant records when requests are approved

## Module Dependencies

| Module                    | Description                                   |
| ------------------------- | --------------------------------------------- |
| **spp_studio**            | Core Studio interface and mixin functionality |
| **spp_change_request_v2** | Change request infrastructure and processing  |
| **spp_registry**          | Registry models for field mapping             |
| **spp_audit**             | Audit trail logging                           |

## Key Features

### Visual CR Type Builder

A three-step wizard for creating change request types:

| Step              | Description                                 |
| ----------------- | ------------------------------------------- |
| Basic Info        | Name, description, and target registry type |
| Field Selection   | Choose which fields can be changed          |
| Approval Settings | Configure approval requirements             |

### Field Mapping Configuration

Define which registry fields can be updated:

- Map source fields (change request) to target fields (registrant)
- Mark fields as required or optional
- Set field-level validation rules
- Configure read-only display fields

### Lifecycle Management

CR types follow a safe editing lifecycle:

| State    | Can Edit | Can Use |
| -------- | -------- | ------- |
| Draft    | Yes      | No      |
| Active   | Limited  | Yes     |
| Inactive | Yes      | No      |

When active:

- Core settings (name, target type) are locked
- Field mappings can still be modified
- Changes sync automatically to the underlying CR type

### Auto-Generated Detail Models

When a Studio CR type is activated:

1. A detail model (`x_spp_cr_detail_*`) is dynamically created
2. Fields are added based on configured mappings
3. A form view is generated with proper field ordering
4. Access rights are configured for CR security groups

### Target Use Cases

| Use Case            | Description                                  |
| ------------------- | -------------------------------------------- |
| Address Update      | Allow registrants to request address changes |
| Phone Number Change | Update contact phone numbers                 |
| Bank Account Update | Modify payment account details               |
| Contact Information | General contact detail changes               |
| Simple Demographics | Basic demographic field updates              |

## Integration

### With Change Request V2 Module

Studio CR types create standard `spp.change.request.type` records:

- Uses field mapping apply strategy
- Inherits conflict detection capabilities
- Supports document requirements
- Integrates with approval workflows

### With Registry Module

Field mappings connect to `res.partner` fields:

- Individual-specific fields (given_name, birthdate, gender)
- Group-specific fields (group name)
- Shared fields (phone, email, address)

### With Approval Module

Approval configuration options:

- Require approval before applying changes
- Configure approval groups
- Auto-apply changes on approval
- Manual application option

### With Studio Module

Inherits Studio mixin functionality:

- Draft/Active/Inactive state management
- Deactivation impact warnings
- Activation hooks for setup
- Audit trail integration

## Security

Access rights for generated detail models:

| Group        | Read | Write | Create | Delete |
| ------------ | ---- | ----- | ------ | ------ |
| CR Manager   | Yes  | Yes   | Yes    | Yes    |
| CR Validator | Yes  | Yes   | No     | No     |
| CR User      | Yes  | Yes   | No     | No     |

Note: Detail records are created by the system (via sudo), so regular users do not need create permission.

## Related Modules

- {doc}`spp_change_request_v2` - Change request infrastructure
- {doc}`spp_studio` - Core Studio interface
- {doc}`spp_cr_types_base` - Pre-built change request types
