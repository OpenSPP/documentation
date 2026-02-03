---
openspp:
  doc_status: draft
---

# OpenSPP Registry


## Overview

OpenSPP Registry is the consolidated registry management system for social protection programs. It provides comprehensive tools for managing individuals, groups (households, communities), and the relationships between them. This module is the foundation for beneficiary management across all OpenSPP functionality.

## Purpose

This module is designed to:

- **Manage registrants:** Create, update, and track individuals and groups participating in social protection programs.
- **Track identities:** Store and verify identity documents with multiple ID types per registrant.
- **Handle memberships:** Define group compositions with member roles, join dates, and relationship types.
- **Enable relationships:** Track family and social relationships between individuals.
- **Support flexible categorization:** Tag registrants for targeting, filtering, and reporting.

## Module Dependencies

| Dependency         | Purpose                                |
| ------------------ | -------------------------------------- |
| `base`             | Odoo core framework                    |
| `mail`             | Communication and activity tracking    |
| `contacts`         | Base contact model extension           |
| `web`              | Web interface components               |
| `portal`           | Portal access capabilities             |
| `phone_validation` | Phone number validation and formatting |
| `spp_security`     | Security groups and access control     |
| `spp_vocabulary`   | Vocabulary/lookup value management     |
| `muk_web_chatter`  | Enhanced chatter positioning           |

## Key Features

### Registrant Types

The registry supports two primary registrant types:

| Type           | Description                 | Use Cases                               |
| -------------- | --------------------------- | --------------------------------------- |
| **Individual** | A single person             | Direct beneficiaries, household members |
| **Group**      | A collection of individuals | Households, communities, cooperatives   |

### Individual Management

For each individual, the registry tracks:

| Category          | Data Points                                    |
| ----------------- | ---------------------------------------------- |
| **Profile**       | Name, birth date, gender, photo                |
| **Identity**      | ID documents with types, numbers, expiry dates |
| **Contact**       | Phone numbers, addresses                       |
| **Participation** | Group memberships, program enrollments         |
| **History**       | Timeline of changes and interactions           |

### Group Management

Groups represent collections of individuals with:

| Feature               | Description                                      |
| --------------------- | ------------------------------------------------ |
| **Membership roster** | List of members with roles and dates             |
| **Head of household** | Designated primary contact                       |
| **Aggregate data**    | Computed statistics (member count, demographics) |
| **Shared attributes** | Location, economic status                        |

### Group Membership

The membership model captures:

| Field      | Purpose                                   |
| ---------- | ----------------------------------------- |
| Member     | Reference to the individual               |
| Group      | Reference to the group                    |
| Role       | Member's role (Head, Spouse, Child, etc.) |
| Start Date | When membership began                     |
| End Date   | When membership ended (if applicable)     |

### Identity Documents

Track multiple identity documents per registrant:

| Field       | Description                                        |
| ----------- | -------------------------------------------------- |
| ID Type     | Category of document (National ID, Passport, etc.) |
| ID Number   | Document identifier                                |
| Issue Date  | When the document was issued                       |
| Expiry Date | When the document expires                          |
| Status      | Verification state                                 |

### Tagging System

Flexible tagging for categorization and targeting:

- Create custom tags for program-specific needs
- Apply multiple tags per registrant
- Use tags in eligibility criteria and filters
- Track tag assignment history

## Integration

### With Programs

The registry provides the beneficiary pool for program enrollment:

```
Registry (Individuals/Groups)
    ↓
Program Membership (enrolled beneficiaries)
    ↓
Cycle Membership (cycle participants)
    ↓
Entitlements (benefits)
```

### With Area Management

Registrants are linked to geographic areas for:

- Location-based program targeting
- Area-restricted data access
- Geographic reporting

### With Event Data

The registry integrates with event tracking for:

- Field visit records
- Survey responses
- Assessment data

### With Change Requests

Registry data can be modified through:

- Direct editing (for authorized users)
- Change request workflows (for controlled updates)

## Tab Structure

The registry UI organizes information into logical tabs:

| Tab               | Contents                               |
| ----------------- | -------------------------------------- |
| **Profile**       | Basic information, photo, status       |
| **Identity**      | ID documents, verification status      |
| **Participation** | Group memberships, program enrollments |
| **History**       | Activity log, change history           |

## Technical Details

| Property       | Value          |
| -------------- | -------------- |
| Technical Name | `spp_registry` |
| Category       | OpenSPP/Core   |
| Version        | 19.0.2.2.0     |
| License        | LGPL-3         |
| Application    | Yes            |

### External Dependencies

| Package        | Purpose                                  |
| -------------- | ---------------------------------------- |
| `python-magic` | File type detection for document uploads |

## Are you stuck?

### Cannot create new registrant

**Symptom:** "Access Denied" when trying to create an individual or group.

**Cause:** User does not have Registry Officer or higher permissions.

**Solution:** Assign the user to the Registry Officer or Registry Manager security group.

### Group membership not showing

**Symptom:** Individual added to group but does not appear in membership list.

**Cause:** Membership record may not have been saved properly, or user lacks permission to view.

**Solution:**

1. Verify the membership was saved (check for any validation errors)
2. Ensure user has at least Registry Viewer permissions

### ID document validation failing

**Symptom:** Cannot save ID document due to validation error.

**Cause:** ID number format may not match expected pattern for the selected ID type.

**Solution:** Check the ID type configuration for format requirements.

## See Also

- {doc}`spp_area` - Geographic area assignment for registrants
- {doc}`spp_programs` - Program enrollment and entitlements
- {doc}`spp_security` - Security groups for registry access
