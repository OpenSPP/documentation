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

| Dependency | Purpose |
| --- | --- |
| `base` | Odoo core framework |
| `mail` | Communication and activity tracking |
| `spp_audit` | Comprehensively tracks all data modifications and user ac... |
| `spp_security` | Central security definitions for OpenSPP modules |
| `spp_registry` | Consolidated registry management for individuals, groups,... |
| `spp_base_common` | The OpenSPP base module that provides the main menu, gene... |
| `spp_programs` | Manage cash and in-kind entitlements, integrate with inve... |
| `spp_user_roles` | The OpenSPP User Roles module defines and manages distinc... |
| `spp_custom_field` | The module enables administrators to define and add custo... |
| `spp_cel_domain` | Write simple CEL-like expressions to filter records (Open... |
| `spp_cel_widget` | Reusable CEL expression editor with syntax highlighting a... |
| `spp_vocabulary` | OpenSPP: Vocabulary |
| `spp_approval` | Standardized approval workflows with multi-tier sequencin... |
| `spp_versioning` | Artifact versioning with scheduled activation |

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

```{toctree}
:maxdepth: 1
:hidden:

spp_studio_api_v2
spp_studio_change_requests
spp_studio_events
```
