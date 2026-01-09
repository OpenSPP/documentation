---
openspp:
  doc_status: draft
  products: [core]
---

# CEL Internals

This guide is for **developers** who need to understand CEL caching, the unified value store, and performance optimization.

## Overview

OpenSPP's CEL system includes performance optimizations for production deployments:
- Cached variable values
- Batch precomputation
- SQL-optimized lookups

## The Unified Value Store

Cached variable values are stored in `spp.data.value`.

### Purpose

| Capability | Benefit |
|------------|---------|
| Fast SQL lookups | Eligibility compilation uses cached values |
| Batch precomputation | Warm cache before large operations |
| TTL expiration | Automatic refresh of stale values |
| Manual refresh | On-demand value updates |

### Model Structure

```python
class SppDataValue(models.Model):
    _name = 'spp.data.value'

    variable_id = fields.Many2one('spp.cel.variable')
    registrant_id = fields.Many2one('res.partner')
    period_key = fields.Char()  # e.g., "2024-12", "2024-Q4"
    value_float = fields.Float()
    value_char = fields.Char()
    value_bool = fields.Boolean()
    expires_at = fields.Datetime()
```

## Variable Caching

### Cache Strategies

| Strategy | Storage | Expiration | Use Case |
|----------|---------|------------|----------|
| `none` | No cache | N/A | Simple/fast variables |
| `session` | Request scope | End of request | Batch operations |
| `ttl` | `spp.data.value` | `cache_ttl_seconds` | Expensive computations |
| `manual` | `spp.data.value` | Explicit refresh | External/stable data |

### Configuration Fields

| Field | Purpose |
|-------|---------|
| `cache_strategy` | Which caching approach |
| `cache_ttl_seconds` | TTL expiration time |
| `invalidate_on_member_change` | Recompute when members change |
| `invalidate_on_field_change` | Fields that trigger recompute |

## The `metric()` Function

When a variable uses persistent caching (`ttl` or `manual`), the variable resolver emits a `metric()` call instead of inlining the variable's CEL expression.

### How It Works

1. Expression references `children_under_5_count`
2. Variable has `cache_strategy = 'ttl'`
3. Resolver emits: `metric("children_under_5_count")`
4. At compile time, CEL engine looks up cached value from `spp.data.value`

### Benefits

- Avoids recomputing expensive aggregates
- Enables SQL JOIN for eligibility filtering
- Supports historical/period values

## Batch Precomputation

Some workflows precompute cached variables before applying rules.

### Program Cycle Example

```python
# In cycle_manager_base.py
def prepare_eligibility_check(self, beneficiaries):
    # Precompute all cached variables for beneficiaries
    self.env['spp.data.cache.manager'].precompute_variables(
        variable_ids=self._get_eligibility_variables(),
        registrant_ids=beneficiaries.ids
    )
```

### When to Precompute

| Scenario | Recommendation |
|----------|----------------|
| Small batch (< 100) | On-demand is fine |
| Medium batch (100-1000) | Consider precompute |
| Large batch (> 1000) | Always precompute |

## Period Granularity

Variables can store historical values by period.

### Supported Granularities

| Granularity | Period Key Format | Example |
|-------------|-------------------|---------|
| `current` | None | Latest only |
| `daily` | `YYYY-MM-DD` | `2024-12-18` |
| `monthly` | `YYYY-MM` | `2024-12` |
| `quarterly` | `YYYY-QN` | `2024-Q4` |
| `yearly` | `YYYY` | `2024` |
| `snapshot` | Custom | At enrollment |

### Period Key Validation

```python
# In cel_variable.py
PERIOD_KEY_PATTERNS = {
    'daily': r'^\d{4}-\d{2}-\d{2}$',
    'monthly': r'^\d{4}-\d{2}$',
    'quarterly': r'^\d{4}-Q[1-4]$',
    'yearly': r'^\d{4}$',
}
```

## Cache Invalidation

### Automatic Triggers

Configure on the variable:
- `invalidate_on_member_change`: For group aggregates
- `invalidate_on_field_change`: Comma-separated field names

### Manual Refresh

```python
# Refresh specific variable for registrants
self.env['spp.data.cache.manager'].refresh_variable(
    variable_id=variable.id,
    registrant_ids=registrants.ids
)

# Refresh all cached variables for registrants
self.env['spp.data.cache.manager'].refresh_all(
    registrant_ids=registrants.ids
)
```

## Source Code References

| Component | Location |
|-----------|----------|
| Variable model | `spp_cel_domain/models/cel_variable.py` |
| Resolver (metric emission) | `spp_cel_domain/models/cel_variable_resolver.py` |
| Cache manager | `spp_cel_domain/models/data_evaluator.py` |
| Cycle precompute hook | `spp_programs/models/managers/cycle_manager_base.py` |

## Performance Tuning

### Identifying Slow Variables

1. Enable CEL query logging (see module settings)
2. Look for "Python fallback" warnings
3. Check query execution times

### Optimization Strategies

| Issue | Solution |
|-------|----------|
| Expensive aggregate | Enable caching |
| Many small lookups | Batch precompute |
| Complex event queries | Simplify predicates |
| Frequent recomputation | Adjust TTL or use manual |

### Monitoring

The cache manager tracks:
- Cache hit/miss rates
- Precomputation duration
- Stale value counts

## Related Documentation

For implementers:
- {doc}`/config_guide/cel/variables` - Configuring variables
- {doc}`/config_guide/cel/troubleshooting` - Debugging performance
