---
openspp:
  doc_status: draft
---

# Registry Group Hierarchy

**Module:** `spp_registry_group_hierarchy`

## Overview

The module introduces hierarchical relationships among OpenSPP registry groups, enabling the creation of nested structures where groups can contain both individuals and other sub-groups. It extends g2p_registry_group and g2p_registry_membership modules.

## Purpose

This module is designed to:

- **Enable group-of-groups structures:** Allow groups to contain both individuals and other groups as members, forming hierarchical relationships (e.g., cooperatives containing households).
- **Control membership types per group type:** Use vocabulary codes to define which group types allow mixed membership (individuals and sub-groups).

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `spp_security` | Central security definitions for OpenSPP modules |
| `base` | Odoo core framework |
| `spp_registry` | Consolidated registry management for individuals, groups,... |
| `spp_vocabulary` | OpenSPP: Vocabulary |

## Key Features

### Allow All Member Types

Adds an `allow_all_member_type` boolean to group type vocabulary codes (`spp.vocabulary.code`). When enabled on a group type, groups of that type can contain both individual registrants and other groups as members.

### Dynamic Membership Domain

Extends `spp.group.membership` with a computed domain that adjusts based on the group type:

| Group Type Setting | Allowed Members |
| --- | --- |
| `allow_all_member_type` = False | Individual registrants only |
| `allow_all_member_type` = True | Both individuals and groups (excluding the group itself) |

### Member Form Navigation

Provides an `open_member_form` action on membership records that opens the correct form view depending on whether the member is an individual or a group.

## Integration

- **spp_vocabulary:** Extends vocabulary codes with the `allow_all_member_type` flag to control which group types support hierarchical membership.
- **spp_registry:** Extends group membership to support dynamic filtering of allowed members based on the parent group's type configuration.
