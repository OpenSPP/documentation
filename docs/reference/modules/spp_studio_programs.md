---
openspp:
  doc_status: draft
---

# OpenSPP Studio - Programs

**Module:** `spp_studio_programs`

## Overview

Program scoping for OpenSPP Studio configurations.

## Purpose

This module is designed to:

- **Scope Studio configs to programs:** add the optional program link used to restrict no-code configurations to specific programs.
- **Keep Studio program-free:** carry the program-scoping field and wizard option so `spp_studio` can be installed without the Programs stack.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `spp_studio` | No-code customization interface for OpenSPP |
| `spp_programs` | Manage programs, cycles, beneficiary enrollment, entitlem... |

## Key Features

- **Program scoping field:** adds `program_ids` to Studio configurations (`spp.studio.mixin`) so fields and logic variables can be limited to selected programs.
- **Pack install wizard option:** adds `program_id` to the Logic Pack install wizard for program-specific constant-value lookups.

## Integration

- Companion to `spp_studio`. Auto-installs when both `spp_studio` and `spp_programs` are present.
