---
openspp:
  doc_status: draft
  products: [core]
---

# Overview

This guide is for **implementers** who need to configure change request types to match program requirements. You should be comfortable with logic builders like CommCare or Kobo, but you don't need to write Python code for basic configurations.

## What are change request types?

Change request types define the different kinds of modifications that can be made to registrant records through a controlled workflow. Instead of allowing direct edits, change requests ensure that:

- All changes go through an approval process
- An audit trail is maintained for compliance
- Data quality is preserved through validation rules
- Document requirements can be enforced

## Architecture

Change requests in OpenSPP V2 follow a configuration-driven architecture with three layers:

1. **Request Type** - Defines what kind of change can be made (e.g., "Add Member", "Edit Individual")
2. **Detail Model** - Stores the specific fields for this request type (real Odoo fields, not JSON)
3. **Apply Strategy** - Controls how approved changes are written to the registrant record

```
┌──────────────────────────────────────┐
│   Change Request Type Config         │
│   (spp.change.request.type)          │
├──────────────────────────────────────┤
│ • Name: "Edit Phone Number"          │
│ • Code: edit_phone                   │
│ • Target: Individual                 │
│ • Approval: Single-level             │
│ • Apply Strategy: Field Mapping      │
└──────────────────┬───────────────────┘
                   │
      ┌────────────┴────────────┐
      ▼                         ▼
┌─────────────────┐   ┌──────────────────┐
│ Detail Model    │   │ Apply Mappings   │
│ (real fields)   │   │                  │
├─────────────────┤   ├──────────────────┤
│ • new_phone     │   │ new_phone → phone│
│ • phone_type    │   │                  │
│ • is_primary    │   │                  │
└─────────────────┘   └──────────────────┘
```

## Available detail models

OpenSPP provides pre-built detail models for common change request scenarios:

### From spp_cr_types_base

| Model | Purpose |
|-------|---------|
| `spp.cr.detail.edit_individual` | Edit individual information |
| `spp.cr.detail.edit_group` | Edit group/household information |
| `spp.cr.detail.update_id` | Update ID document |

### From spp_cr_types_advanced

| Model | Purpose |
|-------|---------|
| `spp.cr.detail.add_member` | Add person to household |
| `spp.cr.detail.remove_member` | Remove person from household |
| `spp.cr.detail.change_hoh` | Change head of household |
| `spp.cr.detail.transfer_member` | Transfer member between groups |
| `spp.cr.detail.exit_registrant` | Deactivate registrant |
| `spp.cr.detail.create_group` | Create new group/household |
| `spp.cr.detail.split_household` | Split household into two |
| `spp.cr.detail.merge_registrants` | Merge duplicate records |

## Configuration workflow

The typical workflow for configuring a change request type:

1. **Create the request type** - Define basic info, target type, and code
2. **Link a detail model** - Select which fields will be collected
3. **Configure approval** - Set up the approval workflow
4. **Set up field mappings** - Define how fields are applied to the registrant
5. **Configure documents** - Set required supporting documents

See {doc}`creating_types` for step-by-step instructions.

## Next steps

- {doc}`creating_types` - Step-by-step guide to create a change request type
- {doc}`field_mappings` - Configure how changes are applied
- {doc}`patterns` - Common configuration patterns
- {doc}`custom_detail_models` - Create custom detail models for specialized needs
