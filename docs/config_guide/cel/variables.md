---
openspp:
  doc_status: draft
  products: [core]
---

# Variables

This guide is for **implementers** configuring CEL variables in OpenSPP.

Variables (`spp.cel.variable`) define named data points that can be reused across expressions and features. Define them once, use them everywhere.

## Why use variables?

| Benefit | Example |
|---------|---------|
| **Reusability** | Define "children under 5" once, use in multiple programs |
| **Maintainability** | Change threshold in one place |
| **Readability** | `poverty_line` is clearer than `10000` |
| **Performance** | Cached variables compute once |

## Variable anatomy

Every variable has:

| Field | Purpose | Example |
|-------|---------|---------|
| **Name** | Human-readable label | "Children Under 5 Count" |
| **CEL Accessor** | How it's referenced in expressions | `children_under_5_count` |
| **Applies To** | Context (individual, group, both) | Group/Household |
| **Source Type** | Where value comes from | Aggregate |

## Source types

### Model field

Maps directly to a model field.

| Field | Value |
|-------|-------|
| Source Type | Model Field |
| Field | `birthdate` |

### Constant/parameter

Fixed value, optionally program-overridable.

| Field | Value |
|-------|-------|
| Source Type | Constant |
| Value | `10000` |
| Program Override | Yes (optional) |

Use for thresholds like poverty lines that may vary by program.

### Computed (CEL)

Calculated from a CEL expression.

| Field | Value |
|-------|-------|
| Source Type | Computed |
| CEL Expression | `age_years(me.birthdate)` |

### Aggregate

Computes over related records (members, enrollments, entitlements, events).

| Field | Value |
|-------|-------|
| Source Type | Aggregate |
| Aggregate Target | Members |
| Aggregate Type | Count |
| Filter | `age_years(m.birthdate) < 5` |

Generates expressions like:
```cel
members.count(m, age_years(m.birthdate) < 5)
```

### External source

Value from external data provider.

### Scoring result

Value from a scoring run (typically cached).

### Vocabulary concept

Derived from vocabulary system.

## Aggregate variables

Aggregates are the most powerful variable type. They compute values across collections.

### Aggregate targets

| Target | Collection | Loop Variable |
|--------|------------|---------------|
| Members | Household members | `m` |
| Enrollments | Program memberships | `e` |
| Entitlements | Entitlement records | `ent` |
| Events | Event data records | `evt` |

### Aggregate types

| Type | Result | Example |
|------|--------|---------|
| Count | Number of matches | Children under 5 |
| Sum | Total of values | Sum of member incomes |
| Average | Mean of values | Average member age |
| Min | Minimum value | Youngest member age |
| Max | Maximum value | Highest member income |
| Exists | Boolean (any match) | Has disabled member |

### Examples

**Count children under 5:**
```cel
members.count(m, age_years(m.birthdate) < 5)
```

**Female head of household:**
```cel
members.exists(m, head(m) and m.gender == "female")
```

**Sum member income:**
```cel
members.sum(m.income, true)
```

**Any enrolled program:**
```cel
enrollments.exists(e, e.state == "enrolled")
```

## Event variables

When the event/CEL integration is installed, you can aggregate over events.

### Event functions

| Function | Purpose | Example |
|----------|---------|---------|
| `has_event(type)` | Check existence | `has_event("visit", within_days=90)` |
| `events_count(type)` | Count events | `events_count("visit", within_days=90)` |
| `events_sum(type, field)` | Sum field values | `events_sum("payment", "amount")` |
| `event(type, field)` | Get single value | `event("survey", "income", select="latest")` |

### Event function parameters

| Parameter | Purpose | Example |
|-----------|---------|---------|
| `within_days` | Recent events only | `within_days=90` |
| `within_months` | Recent events only | `within_months=12` |
| `period` | Specific period | `period=this_year()` |
| `select` | Which event | `select="latest"` |
| `default` | Fallback value | `default=0` |
| `states` | Filter by state | `states=["approved"]` |

### Finding event type codes

1. Go to **Studio → Event Types**
2. Click on your event type
3. Click **View Event Type**
4. Note the **Code** field (usually `x_evt_<slug>`)

### Finding field names

For Studio-created event types:
1. Open the event type in Studio
2. Note the **Technical Name** of each field
3. Use that name in `event()` calls

## Variable caching

For performance, variables can cache computed values.

### Cache strategies

| Strategy | Behavior | Use Case |
|----------|----------|----------|
| None | Always compute | Simple/fast variables |
| Session | Cache per request | Within batch operations |
| TTL | Persist with expiration | Expensive computations |
| Manual | Persist until refreshed | External/stable data |

### Cache configuration

| Field | Purpose |
|-------|---------|
| Cache TTL (seconds) | Expiration time for TTL strategy |
| Invalidate on Member Change | Recompute when members change |
| Invalidate on Field Change | Fields that trigger recompute |

### The unified value store

Cached values are stored in `spp.data.value`:
- Fast SQL lookups during eligibility
- Batch precomputation support
- Period-based historical values

## Period granularity

Variables can store historical values by period:

| Granularity | Period Key Format | Example |
|-------------|-------------------|---------|
| Current | None (latest only) | - |
| Daily | `YYYY-MM-DD` | `2024-12-18` |
| Monthly | `YYYY-MM` | `2024-12` |
| Quarterly | `YYYY-QN` | `2024-Q4` |
| Yearly | `YYYY` | `2024` |
| Snapshot | Point-in-time | At enrollment |

## How features use CEL

Different features use CEL in different ways:

| Feature | CEL Mode | Profile |
|---------|----------|---------|
| Registry search (CEL) | Compile-to-domain | `registry_*` |
| Program eligibility | Compile-to-domain | `registry_*` |
| Scoring indicators | Compile-to-domain | Registry or scoring |
| Entitlement amounts | Runtime evaluation | `me`, `base_amount` |
| GRM routing | Runtime evaluation | `ticket`, `r` |
| Approval conditions | Runtime evaluation | Target record |

## Creating a variable: step by step

### 1. Navigate

Go to **Studio → Variables** and click **Create**.

### 2. Basic Info

| Field | Action |
|-------|--------|
| Name | Enter descriptive name |
| CEL Accessor | Enter identifier (lowercase, underscores) |
| Applies To | Select context |

### 3. Source Configuration

Choose source type and configure:

**For Aggregate:**

| Field | Action |
|-------|--------|
| Aggregate Target | Select collection |
| Aggregate Type | Select operation |
| Filter | Enter predicate |

### 4. Caching (Optional)

| Field | Action |
|-------|--------|
| Cache Strategy | Select if needed |
| Cache TTL | Set expiration |
| Invalidation | Configure triggers |

### 5. Activate

1. Click **Save**
2. Click **Activate**

## Are you stuck?

**Variable not showing in autocomplete?**
- Verify it's **Active**
- Check **Applies To** matches your context
- Confirm you're using the **CEL Accessor** name

**Aggregate returning wrong count?**
- Verify filter predicate syntax
- Check if relations exclude inactive records
- Test with known data

**Cache not updating?**
- Check invalidation triggers
- Verify TTL hasn't cached stale value
- Try manual refresh

See {doc}`troubleshooting` for more debugging tips.
