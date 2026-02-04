---
openspp:
  doc_status: draft
---

# CR Types - Base

**Module:** `spp_cr_types_base`

## Overview

OpenSPP CR Types - Base provides the foundational change request types using the field mapping strategy. These pre-built types cover common registry update scenarios and serve as templates for creating customized change request workflows.

## Purpose

This module is designed to:

- **Provide ready-to-use CR types:** Pre-configured types for common update scenarios
- **Demonstrate field mapping:** Show how to use the field mapping apply strategy
- **Enable Studio customization:** Types are editable and cloneable via Studio
- **Serve as templates:** Base types can be cloned to create variants

## Module Dependencies

| Module                    | Description                                  |
| ------------------------- | -------------------------------------------- |
| **spp_change_request_v2** | Change request infrastructure and processing |

## Included Change Request Types

### Edit Individual Information

Update personal information for individual registrants.

| Setting        | Value             |
| -------------- | ----------------- |
| Code           | `edit_individual` |
| Target Type    | Individual        |
| Apply Strategy | Field Mapping     |
| Icon           | fa-user-edit      |

**Mapped Fields:**

| Source Field  | Target Field | Description        |
| ------------- | ------------ | ------------------ |
| given_name    | given_name   | First name         |
| family_name   | family_name  | Last name          |
| birthdate     | birthdate    | Date of birth      |
| gender_id     | gender_id    | Gender             |
| phone         | phone        | Phone number       |
| email         | email        | Email address      |
| address_line1 | street       | Street address     |
| address_line2 | street2      | Additional address |
| city          | city         | City               |
| postal_code   | zip          | Postal/ZIP code    |

### Edit Group Information

Update information for group/household registrants.

| Setting        | Value           |
| -------------- | --------------- |
| Code           | `edit_group`    |
| Target Type    | Group/Household |
| Apply Strategy | Field Mapping   |
| Icon           | fa-users-cog    |

**Mapped Fields:**

| Source Field  | Target Field | Description        |
| ------------- | ------------ | ------------------ |
| group_name    | name         | Group name         |
| phone         | phone        | Phone number       |
| email         | email        | Email address      |
| address_line1 | street       | Street address     |
| address_line2 | street2      | Additional address |
| city          | city         | City               |
| postal_code   | zip          | Postal/ZIP code    |

### Update ID Document

Add, update, or remove identification documents.

| Setting        | Value                       |
| -------------- | --------------------------- |
| Code           | `update_id`                 |
| Target Type    | Both (Individual and Group) |
| Apply Strategy | Custom                      |
| Apply Model    | spp.cr.apply.update_id      |
| Icon           | fa-id-card                  |

This type uses a custom apply strategy because ID document updates involve:

- Adding new ID records
- Updating existing ID records
- Removing ID records
- Handling ID type relationships

## Editability Configuration

All base types are configured for Studio customization:

| Flag             | Value             | Meaning                              |
| ---------------- | ----------------- | ------------------------------------ |
| Studio Editable  | True              | Can modify field mappings via Studio |
| Studio Cloneable | True              | Can clone to create new variants     |
| System Type      | True              | Installed by module, cannot delete   |
| Source Module    | spp_cr_types_base | Origin tracking                      |

## Integration

### With Change Request V2 Module

These types use the infrastructure provided by `spp_change_request_v2`:

- Detail models are defined in the parent module
- Form views are provided for each detail model
- Apply strategies are implemented in the parent module

### With Studio Module

Types can be extended via `spp_studio_change_requests`:

- Clone existing types to create variants
- Modify field mappings on cloned types
- Add custom fields to detail forms

## Customization Patterns

### Clone and Modify

To create a variant of an existing type:

1. Navigate to Studio > Change Requests
2. Select the base type to clone
3. Click "Clone" button
4. Modify name, fields, and mappings
5. Activate the cloned type

### Add Custom Fields

To add fields to a base type:

1. Use Studio to edit the type
2. Add new field mappings
3. Map to existing registry fields
4. Or create custom registry fields first

### Restrict Available Fields

To limit which fields can be changed:

1. Clone the base type
2. Remove unwanted field mappings
3. Rename for clarity (e.g., "Address Update Only")
4. Activate the restricted type

## Use Cases

| Scenario            | Recommended Type               |
| ------------------- | ------------------------------ |
| Update contact info | Edit Individual/Group          |
| Change address      | Clone with address fields only |
| Update demographics | Edit Individual                |
| New ID document     | Update ID Document             |
| Change phone number | Clone with phone field only    |

## Related Modules

- {doc}`spp_change_request_v2` - Change request infrastructure
- {doc}`spp_studio_change_requests` - No-code CR type builder
