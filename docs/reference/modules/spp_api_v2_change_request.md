---
openspp:
  doc_status: draft
---

# Change Request

**Module:** `spp_api_v2_change_request`

## Overview

REST API endpoints for Change Request V2.

## Purpose

This module is designed to:

- **Expose change request operations via REST API:** Allow external systems to create, read, update, and search change requests through authenticated HTTP endpoints.
- **Manage approval workflow via API:** Support the full change request lifecycle (submit, approve, reject, request revision, apply, reset) through dedicated action endpoints.
- **Provide type discovery:** Let API consumers discover available change request types and their field schemas before creating requests.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `spp_api_v2` | OpenSPP API V2 - Standards-aligned, consent-respecting AP... |
| `spp_change_request_v2` | Configuration-driven change request system with UX improv... |

## Key Features

### CRUD Endpoints

| Method | Path | Description |
| --- | --- | --- |
| POST | `/ChangeRequest` | Create a new change request in draft status |
| GET | `/ChangeRequest/{ref}` | Read a change request by its reference (e.g., CR/2026/00001) |
| PUT | `/ChangeRequest/{ref}` | Update detail data on a draft change request |
| GET | `/ChangeRequest` | Search change requests with filters and pagination |

The reference uses a three-segment path (`{p1}/{p2}/{p3}`) to handle slashes in identifiers like `CR/2026/00001`.

Search supports filtering by registrant identifier, request type, status, and date range. Results are paginated with configurable count and offset.

### Workflow Actions

| Action | Path | Description |
| --- | --- | --- |
| Submit | `POST /{ref}/$submit` | Submit a draft change request for approval |
| Approve | `POST /{ref}/$approve` | Approve a pending change request (optional comment) |
| Reject | `POST /{ref}/$reject` | Reject with a required reason |
| Request Revision | `POST /{ref}/$request-revision` | Send back for revision with notes |
| Apply | `POST /{ref}/$apply` | Execute approved changes on the registrant |
| Reset | `POST /{ref}/$reset` | Reset rejected/revision CR back to draft |

### Type Schema Discovery

| Method | Path | Description |
| --- | --- | --- |
| GET | `/ChangeRequest/$types` | List all active change request types with code, name, and target type |
| GET | `/ChangeRequest/$types/{code}` | Get field definitions and document requirements for a specific type |

### Optimistic Locking

The PUT endpoint supports optimistic locking via the `If-Match` header. The ETag is based on the record's `write_date` timestamp, and a 409 Conflict is returned if the resource was modified by another request.

### Scope-Based Authorization

All endpoints check API client scopes before processing:

| Scope | Operations |
| --- | --- |
| `change_request:create` | Create |
| `change_request:read` | Read, search, list types |
| `change_request:update` | Update, submit, reset |
| `change_request:approve` | Approve, reject, request revision |
| `change_request:apply` | Apply |

## Integration

- **spp_api_v2:** Provides the FastAPI framework, OAuth authentication middleware, and search result pagination schemas.
- **spp_change_request_v2:** Supplies the underlying change request models, approval workflow logic, and type configuration. The API module delegates all business logic to a `ChangeRequestService` that wraps these models.
- **Auto-install:** This module auto-installs when both `spp_api_v2` and `spp_change_request_v2` are present.
