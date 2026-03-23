---
openspp:
  doc_status: draft
---

# Targeting Simulation

**Module:** `spp_simulation`

## Overview

Simulate targeting scenarios, analyze fairness and distribution, and compare different targeting strategies before committing to criteria.

## Purpose

This module is designed to:

- **Simulate targeting scenarios:** Define "what if" targeting strategies using CEL expressions and evaluate their impact before committing to real program criteria.
- **Analyze fairness and distribution:** Compute equity scores, Gini coefficients, geographic breakdowns, and demographic parity metrics for each simulation run.
- **Compare targeting strategies:** Run side-by-side comparisons of different scenarios to identify the most effective and equitable approach.
- **Measure targeting accuracy:** Calculate leakage and undercoverage rates against an ideal target population.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `base` | Odoo core framework |
| `mail` | Communication and activity tracking |
| `spp_programs` | Manage cash and in-kind entitlements, integrate with inve... |
| `spp_cel_domain` | Write simple CEL-like expressions to filter records (Open... |
| `spp_cel_widget` | Reusable CEL expression editor with syntax highlighting a... |
| `spp_security` | Central security definitions for OpenSPP modules |
| `spp_analytics` | Query engine for indicators, simulations, and GIS analytics |
| `spp_metric` | Unified metric foundation for indicators and simulations |

## Key Features

### Simulation Scenarios

A scenario defines a targeting strategy to evaluate:

| Field | Description |
| --- | --- |
| Target Type | Group (household) or Individual |
| Targeting Expression | CEL expression defining who is eligible |
| Budget Amount / Strategy | Budget limit and handling strategy (no constraint, cap at total, or proportional reduction) |
| Entitlement Rules | Rules for calculating benefit amounts per beneficiary |
| Ideal Population Expression | CEL expression defining who *should* receive benefits (for accuracy measurement) |
| Custom Metrics | Additional metrics to compute during simulation |
| Reference Program | Optional program for comparison context |

Scenarios follow a Draft, Ready, Archived workflow. A targeting expression is required before marking a scenario as Ready. A live preview count shows how many registrants match the expression.

### Entitlement Rules

Each scenario can have multiple entitlement rules defining how benefit amounts are calculated:

| Amount Mode | Description |
| --- | --- |
| Fixed Amount | Same amount per beneficiary |
| Multiplier | Base amount multiplied by a registrant field value (e.g., household size), with optional maximum |
| CEL Expression | Amount computed by a CEL expression |

Rules can have optional condition expressions to apply only to a subset of targeted beneficiaries.

### Simulation Runs

Each run produces aggregated results that are preserved for audit compliance (runs cannot be deleted):

| Metric | Description |
| --- | --- |
| Beneficiary Count | Number of registrants who would receive benefits |
| Coverage Rate | Percentage of registry targeted |
| Total Cost | Sum of all entitlement amounts |
| Budget Utilization | Percentage of budget used |
| Gini Coefficient | Measures benefit inequality (0 = equal, 1 = maximum inequality) |
| Parity Score | 0-100 score measuring demographic coverage parity |
| Leakage Rate | Percentage of recipients not in the ideal population |
| Undercoverage Rate | Percentage of ideal population not targeted |

Runs also store detailed JSON data for distribution statistics, fairness breakdowns, geographic analysis, targeting efficiency (confusion matrix), and custom metric results. Natural language HTML summaries are auto-generated for each section.

### Scenario Templates

Pre-built templates help non-technical users create scenarios quickly:

| Field | Description |
| --- | --- |
| Category | Age-Based, Geographic, Vulnerability, Economic, or Categorical |
| Targeting Expression | Pre-written CEL expression |
| Default Amount / Mode | Suggested entitlement amount |
| Ideal Population Expression | Pre-written accuracy benchmark |

### Scenario Comparison

Compare multiple simulation runs side by side:

- Comparison of headline metrics (beneficiary count, cost, coverage, equity, leakage)
- Parameter comparison showing differences in targeting expressions, budgets, and entitlement rules
- Overlap analysis computing the Jaccard index between targeted populations
- Staleness warnings when runs were executed far apart

### Custom Metrics

Define additional evaluation metrics for simulation scenarios:

| Metric Type | Description |
| --- | --- |
| Aggregate | CEL expression aggregated via sum, avg, min, max, or count |
| Coverage | CEL expression computing a coverage percentage |
| Ratio | Numerator and denominator CEL expressions |

## Integration

- **spp_cel_domain / spp_cel_widget:** CEL expressions define targeting criteria, entitlement amounts, ideal population definitions, and custom metrics.
- **spp_programs:** Scenarios can reference programs for comparison and can be converted into real programs.
- **spp_analytics:** Provides the query engine for computing simulation analytics and geographic breakdowns.
- **spp_metric:** Custom simulation metrics inherit from the unified metric base model.
