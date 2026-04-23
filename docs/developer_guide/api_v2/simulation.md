---
openspp:
  doc_status: draft
  products: [core]
---

# Simulation

**For: developers**

Run and analyze scenario-based program simulations through the API.

```{warning}
**Known issue:** The `simulation:write` scope is checked by every create/update/archive endpoint but cannot be granted — `write` is not a valid scope action in OpenSPP (the standard set is `read`, `search`, `create`, `update`, `delete`, `all`). Until the module is fixed, all create/update/archive operations on scenarios will return 403. Read-only operations (`simulation:read`) and execution (`simulation:execute`) work normally. Track this in the OpenSPP modules repo.
```

## Overview

The Simulation API (`spp_api_v2_simulation`) enables scenario-based testing of program designs before implementation. You can:

- **Design scenarios** with targeting criteria, budgets, and entitlement rules
- **Run simulations** against real registry data
- **Compare results** across multiple scenarios
- **Convert scenarios** into production programs

This is used for program design, impact analysis, and budget planning.

## Prerequisites

- Install `spp_api_v2_simulation` module
- API client with appropriate scopes:

| Scope | Permissions |
|-------|------------|
| `simulation:read` | View scenarios, runs, comparisons, templates |
| `simulation:write` | Create/update/archive scenarios |
| `simulation:execute` | Run simulations |
| `simulation:convert` | Convert scenarios to programs |

## Scenario Lifecycle

```
  ┌───────┐     ┌───────┐     ┌──────────────┐
  │ Draft │────►│ Ready │────►│ Run (N times) │
  └───────┘     └───────┘     └──────────────┘
                    │
                    └──► Convert to Program
```

## Templates

List pre-built scenario templates for common program designs.

```text
GET /api/v2/spp/simulation/templates
Authorization: Bearer TOKEN
```

## Scenario Management

### List Scenarios

```text
GET /api/v2/spp/simulation/scenarios?state=ready&limit=50
Authorization: Bearer TOKEN
```

**Query parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `state` | string | `draft`, `ready`, `archived` |
| `category` | string | Scenario category |
| `limit` | integer | Max results (default 100, max 500) |
| `offset` | integer | Skip N results (default 0) |

### Create Scenario

```text
POST /api/v2/spp/simulation/scenarios
Authorization: Bearer TOKEN
Content-Type: application/json

{
  "name": "CCT for Female Adults",
  "description": "Cash transfer targeting women aged 18+",
  "category": "poverty_reduction",
  "target_type": "individual",
  "targeting_expression": "age >= 18 AND gender == 'F'",
  "targeting_expression_explanation": "Female adults aged 18 and above",
  "budget_amount": 5000000,
  "budget_strategy": "per_beneficiary",
  "ideal_population_expression": "poverty_score > 0.7",
  "entitlement_rules": [
    {
      "amount_mode": "fixed",
      "amount": 5000,
      "multiplier_field": null,
      "max_multiplier": 1
    }
  ],
  "program_id": 5
}
```

**Key fields:**

| Field | Type | Description |
|-------|------|-------------|
| `targeting_expression` | string | CEL expression for eligibility |
| `budget_amount` | number | Total budget |
| `budget_strategy` | string | `per_beneficiary`, `total`, etc. |
| `ideal_population_expression` | string | CEL expression defining the "ideal" target (for equity scoring) |
| `entitlement_rules` | array | Benefit amount rules |

**Response (201 Created):** Scenario object with computed fields like `targeting_preview_count` and `equity_score`.

### Get Scenario

```text
GET /api/v2/spp/simulation/scenarios/{scenario_id}
Authorization: Bearer TOKEN
```

### Update Scenario

Only draft scenarios can be updated.

```text
PUT /api/v2/spp/simulation/scenarios/{scenario_id}
Authorization: Bearer TOKEN
Content-Type: application/json

{
  "budget_amount": 7500000,
  "entitlement_rules": [
    {"amount_mode": "fixed", "amount": 7500, "max_multiplier": 1}
  ]
}
```

### Archive Scenario

```text
DELETE /api/v2/spp/simulation/scenarios/{scenario_id}
Authorization: Bearer TOKEN
```

Returns 204 No Content. This is a soft delete (archive).

### Mark Scenario as Ready

Transition from draft to ready (enables running simulations).

```text
POST /api/v2/spp/simulation/scenarios/{scenario_id}/ready
Authorization: Bearer TOKEN
```

## Running Simulations

### Execute Simulation

```text
POST /api/v2/spp/simulation/scenarios/{scenario_id}/run
Authorization: Bearer TOKEN
```

**Response:**

```json
{
  "run_id": 42,
  "scenario_id": 5,
  "state": "completed",
  "message": "Simulation completed: 12,500 beneficiaries, total cost PHP 62,500,000"
}
```

### List Runs

```text
GET /api/v2/spp/simulation/runs?scenario_id=5&state=completed
Authorization: Bearer TOKEN
```

**Query parameters:** `scenario_id`, `state`, `limit`, `offset`

### Get Run Results

```text
GET /api/v2/spp/simulation/runs/{run_id}?include_details=true
Authorization: Bearer TOKEN
```

**Response (with `include_details=true`):**

```json
{
  "run_id": 42,
  "scenario_id": 5,
  "state": "completed",
  "beneficiary_count": 12500,
  "total_cost": 62500000,
  "coverage_rate": 0.85,
  "equity_score": 0.72,
  "scenario_snapshot": {
    "targeting_expression": "age >= 18 AND gender == 'F'",
    "budget_amount": 5000000
  },
  "distribution_data": {
    "percentiles": {"p10": 5000, "p25": 5000, "p50": 5000, "p75": 5000, "p90": 5000},
    "gini_coefficient": 0.0,
    "standard_deviation": 0.0
  },
  "fairness_data": {
    "demographic_breakdown": {
      "gender": {"F": 12500}
    }
  },
  "targeting_efficiency_data": {
    "leakage_rate": 0.05,
    "undercoverage_rate": 0.15
  },
  "geographic_data": {
    "area_breakdowns": []
  }
}
```

## Comparisons

Compare results across multiple simulation runs.

### Create Comparison

```text
POST /api/v2/spp/simulation/comparisons
Authorization: Bearer TOKEN
Content-Type: application/json

{
  "name": "CCT: Fixed vs Variable Amount",
  "run_ids": [42, 43]
}
```

Minimum 2 runs required. Returns overlap data (Jaccard similarity between beneficiary sets).

### Get Comparison

```text
GET /api/v2/spp/simulation/comparisons/{comparison_id}
Authorization: Bearer TOKEN
```

## Convert to Program

Convert a ready scenario into a production program with CEL eligibility criteria and cash entitlement managers.

```text
POST /api/v2/spp/simulation/scenarios/{scenario_id}/convert-to-program
Authorization: Bearer TOKEN
Content-Type: application/json

{
  "name": "CCT for Female Adults 2024",
  "currency_code": "PHP",
  "is_one_time_distribution": false,
  "import_beneficiaries": true,
  "rrule_type": "monthly",
  "cycle_duration": 1,
  "day": 1,
  "month_by": "date"
}
```

**Response (201 Created):**

```json
{
  "program_id": 15,
  "program_name": "CCT for Female Adults 2024",
  "warnings": []
}
```

Requires `simulation:write` and `simulation:convert` scopes. Only ready scenarios with entitlement rules can be converted. Program name must be unique.

## Common mistakes

**Scenario won't transition to "ready"?**

The scenario must pass validation. Check that targeting expression, budget, and entitlement rules are all configured.

**Simulation run failed?**

Check the `state` and `message` fields in the run response. Common causes: invalid CEL expression, no matching beneficiaries, or database timeout.

**How are equity scores calculated?**

The equity score compares the actual targeted population against the `ideal_population_expression`. Higher scores mean better targeting accuracy.

**Can I re-run a simulation?**

Yes. You can run a ready scenario multiple times. Each run creates a separate result record.

**Convert-to-program fails?**

Check that the scenario is in "ready" state, has entitlement rules, and the program name is unique.

## What's next

- {doc}`resources` - Core program and membership resources
- {doc}`entitlements_cycles` - Entitlements created by programs
- {doc}`data_api` - Variable data for targeting expressions

## See also

- {doc}`overview` - API V2 design principles
- {doc}`authentication` - OAuth 2.0 setup and scopes
