---
openspp:
  doc_status: draft
---

# Programs

**Module:** `spp_studio_events_programs`

## Overview

Program scoping for Studio event types.

## Purpose

This module is designed to:

- **Scope event types to programs:** restore the program-scoping page on the Studio event type form.
- **Keep events program-free:** carry the program-scoping UI so `spp_studio_events` can be installed without the Programs stack.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `spp_studio_events` | No-code event type designer for data collection |
| `spp_studio_programs` | Program scoping for OpenSPP Studio configurations. |

## Key Features

- **Programs page on the form:** injects the Programs page (`program_ids`) back into the event type form when programs are available.

## Integration

- Companion to `spp_studio_events` and `spp_studio_programs`. Auto-installs when both are present.
