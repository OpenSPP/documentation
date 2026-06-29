---
openspp:
  doc_status: draft
---

# Source Tracking — Programs

**Module:** `spp_source_tracking_programs`

## Overview

Source tracking for program memberships.

## Purpose

This module is designed to:

- **Track provenance on enrollments:** add data-provenance / source-tracking fields to program memberships.
- **Keep core source tracking program-free:** carry the program-membership extension so `spp_source_tracking` can be installed without the Programs stack.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `spp_source_tracking` | Track data provenance and source information for registrants |
| `spp_programs` | Manage programs, cycles, beneficiary enrollment, entitlem... |

## Key Features

- **Source tracking on memberships:** applies the source-tracking mixin to `spp.program.membership`, recording origin and collection method.

## Integration

- Companion to `spp_source_tracking`. Auto-installs when both `spp_source_tracking` and `spp_programs` are present.
