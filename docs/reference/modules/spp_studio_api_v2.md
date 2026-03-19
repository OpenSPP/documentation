---
openspp:
  doc_status: draft
---

# API v2 Integration

**Module:** `spp_studio_api_v2`

## Overview

Bridge Studio custom fields and variables with API v2

## Purpose

This module is designed to:

- **Expose Studio custom fields via API v2:** Automatically register Studio-defined fields in API v2 extensions so they appear in Individual and Group API responses and accept updates.
- **Provide Studio field discovery endpoints:** Allow API clients to list custom fields, retrieve their JSON Schema validation rules, and browse available CEL variables.
- **Support extension writes:** Parse incoming API extension data (CodeableConcept, date, numeric types) and convert them to Odoo field values for create/update operations.
- **Serve computed variable values:** Return cached CEL variable values for Individual and Group registrants via dedicated API endpoints.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `spp_api_v2` | OpenSPP API V2 - Standards-aligned, consent-respecting AP... |
| `spp_studio` | No-code customization interface for OpenSPP |
| `spp_cel_domain` | Write simple CEL-like expressions to filter records (Open... |

## Key Features

### Auto-Registration of Studio Fields

When a Studio field is activated, it is automatically added to the appropriate API v2 extension (Individual or Group). When deactivated, it is removed. An `api_exposed` flag on each Studio field controls whether it appears in API responses.

### Studio API Endpoints

All endpoints require the `studio:read` API scope.

| Endpoint | Method | Description |
| --- | --- | --- |
| `/Studio/fields` | GET | List all active Studio custom fields with filtering by target type and pagination |
| `/Studio/fields/{technical_name}/schema` | GET | Get JSON Schema for a specific field (type, constraints, enum values, visibility rules) |
| `/Studio/variables` | GET | List active CEL variables with filtering by context, source type, and category |
| `/Studio/variables/{resource_type}/{identifier}` | GET | Get cached variable values for a specific Individual or Group |

### Field Schema

The schema endpoint returns JSON Schema-compatible metadata for each Studio field:

| Schema Property | Description |
| --- | --- |
| type | JSON Schema type (string, number, boolean, object, array) |
| format | date, date-time, or reference for link fields |
| enum / enumDisplay | Allowed values and display labels for selection fields |
| minimum / maximum | Numeric constraints |
| maxLength | String length limits (255 for text, 65535 for long text) |
| linkModel / linkDomain | Target model and domain filter for link fields |
| visibilityField / Operator / Value | Conditional visibility rules |

### Extension Write Service

Handles reverse mapping from API format to Odoo field values:

| API Format | Odoo Conversion |
| --- | --- |
| camelCase field names | snake_case with `x_` prefix |
| CodeableConcept (`{coding: [{system, code}]}`) | Many2one vocabulary code lookup |
| Arrays of CodeableConcept | Many2many with `Command.set()` |
| ISO date strings | Passed through to Odoo date/datetime fields |
| String booleans (`"true"`, `"1"`) | Python bool |
| `namespace\|value` identifiers | Vocabulary code lookup by namespace_uri and code |

A model allowlist (`SAFE_LOOKUP_MODELS`) restricts display name lookups to safe reference models like `spp.vocabulary.code`, `res.country`, and `res.partner.category`. Sensitive models are explicitly blocked.

### Variable Value Service

Retrieves cached variable values from `spp.data.value` for API responses:

- Single subject queries by partner ID
- Bulk queries for multiple partners (up to 1,000 per batch)
- Period-based historical queries
- Optional stale value filtering
- On-demand computation for field-type variables on safe source models

### API Client Scope

Extends the API client scope model with a `studio` resource type, allowing fine-grained access control for Studio API endpoints.

## Integration

- **spp_api_v2:** Adds the Studio router to the API v2 FastAPI endpoint. Patches `IndividualService` and `GroupService` to handle extension data writes and include computed variable values in responses.
- **spp_studio:** Extends Studio field lifecycle hooks (`_post_activate`, `_post_deactivate`) to automatically register/unregister fields in API extensions.
- **spp_cel_domain:** CEL variables and their cached values are exposed through the variables API endpoints for external system consumption.
