---
openspp:
  doc_status: draft
---

# API V2 — Programs

**Module:** `spp_api_v2_programs`

## Overview

REST API endpoints for Programs and Program Memberships.

## Purpose

This module is designed to:

- **Expose program data over the API:** serve Program and Program Membership resources through the OpenSPP REST API v2.
- **Keep the core API program-free:** carry the program-specific API surface so `spp_api_v2` can be installed without the Programs stack.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `spp_api_v2` | OpenSPP API V2 - Standards-aligned, consent-respecting AP... |
| `spp_programs` | Manage programs, cycles, beneficiary enrollment, entitlem... |

## Key Features

- **Program and Program Membership endpoints:** routers, services and schemas for both resources, including filter/search endpoints.
- **Same security model:** reuses the API's scope enforcement and consent filtering, so program endpoints behave like the rest of the API.

## Integration

- Companion to `spp_api_v2`. Auto-installs when both `spp_api_v2` and `spp_programs` are present.
- Appends its routers to the FastAPI application through the `_get_fastapi_routers` hook on `fastapi.endpoint`.
