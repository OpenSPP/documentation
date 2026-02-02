---
openspp:
  doc_status: draft
  products: [core]
---

# Variables & Indicators

**For: Implementers**

Variables (called "Logic Variables" in the system) provide a unified way to define, cache, and reference data points in CEL expressions. They replace the previous separate indicators module with a more flexible approach supporting different data sources, caching strategies, and period granularities.

## What You'll Learn

This guide shows you how to create variables from different data sources, configure caching for performance, set up time-period tracking, and use variables in eligibility rules and program logic.

```{toctree}
:maxdepth: 1

overview
creating_variables
variable_types
using_variables
```

## Quick Links

| Topic | When to Use |
|-------|-------------|
| {doc}`overview` | Understand variable concepts, source types, and caching |
| {doc}`creating_variables` | Create and configure new variables in Studio |
| {doc}`variable_types` | Learn about different source types (field, computed, aggregate) |
| {doc}`using_variables` | Reference variables in CEL expressions |

## Prerequisites

Before configuring variables, you should:

- Have **Studio** access in OpenSPP
- Understand CEL expression basics (see {doc}`/config_guide/cel/index`)
- Know what data points your program logic needs
- Understand your caching and performance requirements

## What's New in V2

OpenSPP V2 introduces a unified variable system:

- **Multiple Source Types** - Field references, computed expressions, aggregates, external data
- **Smart Caching** - Session, TTL-based, or manual cache strategies
- **Period Granularity** - Daily, monthly, quarterly, yearly, or snapshot tracking
- **Member Aggregates** - Count, sum, average over household members or enrollments
- **Event Aggregates** - Aggregate event data with time-range filtering
- **Categories** - Organize variables into logical groups
- **Program Scoping** - Variables can be global or program-specific

## Navigation

Variables are configured in **Studio → Rules → Variables**.

| Menu | Purpose |
|------|---------|
| All Variables | View and manage all logic variables |
| Categories | Organize variables into groups |

---

*This documentation covers OpenSPP V2 variable configuration for implementers.*
