---
openspp:
  doc_status: draft
---

# Simulation API

**Module:** `spp_api_v2_simulation`

## Overview

REST API for simulation scenario management.

## Purpose

This module is designed to:

- **Manage simulation scenarios via REST API:** Create, read, update, list, and archive simulation scenarios through authenticated endpoints.
- **Execute simulations via API:** Trigger simulation runs and retrieve results including beneficiary counts and equity scores.
- **Compare simulation runs:** Create side-by-side comparisons of multiple simulation runs with overlap analysis.
- **Convert scenarios to programs:** Transform validated simulation scenarios into real programs with CEL eligibility and cash entitlement managers.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `spp_api_v2` | OpenSPP API V2 - Standards-aligned, consent-respecting AP... |
| `spp_simulation` | Simulate targeting scenarios, analyze fairness and distri... |
| `spp_analytics` | Query engine for indicators, simulations, and GIS analytics |

## Key Features

### Scenario Management

| Method | Path | Description |
| --- | --- | --- |
| GET | `/simulation/scenarios` | List scenarios with optional state/category filters and pagination |
| POST | `/simulation/scenarios` | Create a new scenario with entitlement rules |
| GET | `/simulation/scenarios/{id}` | Get scenario details including rules, preview counts, and latest results |
| PUT | `/simulation/scenarios/{id}` | Update a draft scenario |
| DELETE | `/simulation/scenarios/{id}` | Archive a scenario (soft delete) |

Scenarios include targeting expressions, budget configuration, entitlement rules, and state management (draft -> ready -> archived).

### Scenario Lifecycle Actions

| Method | Path | Description |
| --- | --- | --- |
| POST | `/simulation/scenarios/{id}/ready` | Transition scenario from draft to ready state |
| POST | `/simulation/scenarios/{id}/run` | Execute the simulation (requires `simulation:execute` scope) |
| POST | `/simulation/scenarios/{id}/convert-to-program` | Convert a ready scenario into a real program (requires `simulation:convert` scope) |

### Simulation Runs

| Method | Path | Description |
| --- | --- | --- |
| GET | `/simulation/runs` | List simulation runs with optional scenario/state filters |
| GET | `/simulation/runs/{id}` | Get run details with beneficiary counts and entitlement totals |

### Run Comparisons

| Method | Path | Description |
| --- | --- | --- |
| POST | `/simulation/comparisons` | Create a comparison of 2+ simulation runs |
| GET | `/simulation/comparisons/{id}` | Get comparison results with per-run metrics and overlap data |

### Templates

| Method | Path | Description |
| --- | --- | --- |
| GET | `/simulation/templates` | List active pre-built scenario templates |

### Analytics Endpoints

The module also exposes analytics endpoints for querying aggregated statistics:

| Method | Path | Description |
| --- | --- | --- |
| POST | `/simulation/analytics/query` | Compute aggregation with scope, statistics, and group-by dimensions |
| GET | `/simulation/analytics/statistics` | List available statistics for discovery |

### Scope-Based Authorization

| Scope | Operations |
| --- | --- |
| `simulation:read` | List/read scenarios, runs, comparisons, templates, analytics |
| `simulation:write` | Create/update/archive scenarios, create comparisons |
| `simulation:execute` | Run simulations |
| `simulation:convert` | Convert scenarios to programs |

## Integration

- **spp_simulation:** All scenario, run, and comparison business logic is delegated to the simulation models and service layer. The API module provides HTTP transport.
- **spp_analytics:** Analytics query endpoints delegate to the `spp.analytics.service` for unified statistics computation with access control and caching.
- **spp_api_v2:** Provides the FastAPI framework, OAuth authentication, and scope-based authorization middleware.
