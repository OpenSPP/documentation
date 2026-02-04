---
openspp:
  doc_status: draft
---

# Studio

**Module:** `spp_studio`

## Overview

OpenSPP Studio is a no-code customization interface designed for semi-technical users at NGOs and UN agencies. It enables program staff to configure OpenSPP without developer involvement, providing tools for creating business logic, managing variables, and customizing data collection.

## Purpose

This module is designed to:

- **Empower program staff:** Allow M&E officers, data managers, and country coordinators to configure the system without coding
- **Create business logic:** Build eligibility criteria, benefit calculations, and scoring formulas using CEL expressions
- **Manage variables:** Discover and configure available variables through an integrated variable dictionary
- **Install pre-built formulas:** Deploy Logic Packs containing ready-to-use expressions for common social protection use cases
- **Add custom fields:** Extend Individual and Group registries with additional data fields
- **Test configurations:** Validate business logic with built-in test cases and personas

## Module Dependencies

| Module               | Description                                           |
| -------------------- | ----------------------------------------------------- |
| **spp_registry**     | Core registry for individuals and groups              |
| **spp_programs**     | Program management functionality                      |
| **spp_custom_field** | Foundation for custom field definitions               |
| **spp_cel_domain**   | Unified variable system and CEL expression evaluation |
| **spp_cel_widget**   | CEL expression editor widget                          |
| **spp_vocabulary**   | Controlled vocabularies for tags and categories       |
| **spp_approval**     | Approval workflow integration                         |
| **spp_versioning**   | Version history with scheduled activation             |
| **spp_audit**        | Audit trail logging                                   |
| **spp_security**     | Security group management                             |
| **spp_user_roles**   | User role definitions                                 |

## Key Features

### CEL Expression Editor

A full-featured expression editor for creating business logic:

- Syntax highlighting for CEL expressions
- Auto-completion for variables and functions
- Real-time expression validation
- Error messaging with line-level feedback

### Variable Dictionary

Integrated discovery of all available variables:

- Browse variables by category (demographics, economics, program data)
- View variable metadata (type, context, description)
- Insert variables directly into expressions
- Track variable usage across logic definitions

### Logic Packs

Pre-built formula bundles for common use cases:

| Pack Category         | Examples                                    |
| --------------------- | ------------------------------------------- |
| Cash Transfer         | Basic cash transfer eligibility and amounts |
| PMT Targeting         | Proxy means test scoring formulas           |
| Child Benefit         | Age-based child benefit calculations        |
| Social Pension        | Elderly pension eligibility                 |
| Disability Assistance | Disability support criteria                 |
| CCT Program           | Conditional cash transfer requirements      |
| Geographic Targeting  | Location-based eligibility                  |

### Business Logic Lifecycle

Logic definitions follow a governance workflow:

| State            | Description                                    |
| ---------------- | ---------------------------------------------- |
| Draft            | Initial creation, can be freely edited         |
| Pending Approval | Submitted for review (when governance enabled) |
| Published        | Active and in use, frozen for stability        |
| Archived         | Retired logic, preserved for history           |

### Testing Framework

Built-in test execution:

- Create test cases with expected inputs and outputs
- Use test personas representing typical beneficiaries
- Run individual or batch tests
- View pass/fail results with error details

## Integration

### With Programs Module

Studio logic can be attached to programs for:

- Eligibility determination
- Benefit amount calculation
- Validation rules
- Scoring and ranking

### With Registry Module

Custom fields created in Studio appear in:

- Individual registration forms
- Group/household forms
- Registry search and filters

### With Approval Module

When governance is enabled:

- Logic changes require approval before publishing
- Approval workflows follow configured definitions
- Audit trail tracks all approvals

### With Events Module

Logic can be used in event-triggered calculations:

- Post-event data processing
- Conditional event creation
- Event-based eligibility updates

## Target Users

| Role                  | Use Case                                         |
| --------------------- | ------------------------------------------------ |
| Program Data Managers | Create and test eligibility formulas             |
| M&E Officers          | Build monitoring indicators and validation rules |
| Country Coordinators  | Configure country-specific program rules         |

## Related Modules

- {doc}`spp_studio_events` - No-code event type designer
- {doc}`spp_studio_change_requests` - No-code change request type builder
- {doc}`spp_custom_field` - Foundation for custom fields
