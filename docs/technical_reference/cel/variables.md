---
openspp:
  doc_status: unverified
---

# Variables

Variables (`spp.cel.variable`) define named data points that can be reused across expressions and features. Each variable has a **CEL accessor** (how it’s referenced in expressions) and a **source type** (where the value comes from).

## Referencing a variable

In CEL expressions, variables are typically referenced by their **accessor as a bare identifier**, for example:

```text
poverty_line
children_under_5_count
has_disability
```

The CEL engine expands variable references before compilation/evaluation.

## Source types

Core source types include:

- **Model field** (`field`): maps to a model field
- **Constant/parameter** (`constant`): fixed value (optionally program-overridable)
- **Computed (CEL)** (`computed`): calculated from a CEL expression
- **Member aggregate** (`aggregate`): aggregation over members/enrollments/entitlements (and events if installed)
- **External source** (`external`): provided by a data provider
- **Scoring result** (`scoring`): provided by a scoring run (and typically cached)
- **Vocabulary concept** (`vocabulary`): derived from vocabularies

Availability of some source types depends on which OpenSPP modules are installed (for example scoring, vocabulary, external providers).

```{note}
Developer reference (source code): `openspp-modules-v2/spp_cel_domain/models/cel_variable.py`
```

## Aggregates

Aggregates let you compute values like:

- “number of children under 18”
- “sum of entitlements in the current year”
- “whether any enrollment exists”

In Studio, aggregate variables generate CEL expressions for you. Typical generated expressions look like:

```text
members.count(m, age_years(m.birthdate) < 18)
members.exists(m, head(m) and m.gender == "female")
members.sum(m.income, true)
```

```{note}
You usually do not need to write aggregate expressions by hand: reference the variable accessor instead.
```

## Program-configurable constants

Constant/parameter variables can optionally be overridden per program (when the programs integration is installed). This is commonly used for values like poverty lines, cutoffs, or thresholds that differ by program.

## Caching and invalidation (unified variable system)

Variables can choose a caching strategy:

- `none`: always compute/fetch
- `session`: cache within the current request/batch operation
- `ttl`: persist cached values with expiration time
- `manual`: persist cached values until explicitly refreshed

For cached variables you may also configure:

- `cache_ttl_seconds` (TTL cache expiry)
- `invalidate_on_member_change` (for group aggregates)
- `invalidate_on_field_change` (comma-separated field names that trigger invalidation)

Cached values are stored in the unified value store (`spp.data.value`) and can be precomputed for performance in batch workflows (for example, before eligibility checks).

See {doc}`caching_and_metric`.

## Period granularity (historical values)

Variables can optionally support time-based values via **Period Granularity**:

- `current`: current value only (no history)
- `daily` / `monthly` / `quarterly` / `yearly`: values stored per period
- `snapshot`: point-in-time freezes (for example at enrollment)

When a variable supports historical values, queries and caches may use a `period_key` whose format depends on granularity (for example `2024-12` for monthly, `2024-Q4` for quarterly, `2024` for yearly).

```{note}
Period support is configured per variable (`period_granularity`) and validated against expected period key formats in the variable model.
```
