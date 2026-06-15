---
openspp:
  doc_status: draft
---

# OpenSPP Studio Change Requests - Programs

**Module:** `spp_studio_change_requests_programs`

## Overview

Program scoping for Studio change request types.

## Purpose

This module is designed to:

- **Scope change request types to programs:** restore the program-scoping field on the Studio change request type form.
- **Keep change requests program-free:** carry the program-scoping UI so `spp_studio_change_requests` can be installed without the Programs stack.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `spp_studio_change_requests` | No-code change request type builder |
| `spp_studio_programs` | Program scoping for OpenSPP Studio configurations. |

## Key Features

- **Programs field on the form:** injects the `program_ids` field back into the change request type form when programs are available.

## Integration

- Companion to `spp_studio_change_requests` and `spp_studio_programs`. Auto-installs when both are present.
