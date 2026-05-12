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
class DataValue(models.Model):
    _name = 'spp.data.value'

    # Variable reference
    variable_name = fields.Char(required=True, index=True)
    variable_id = fields.Many2one('spp.cel.variable', compute='_compute_variable_id')

    # Subject reference (generic - supports any model)
    subject_model = fields.Char(required=True, default='res.partner', index=True)
    subject_id = fields.Integer(required=True, index=True)

    # Time reference
    period_key = fields.Char(index=True)  # e.g., "current", "2024-12", "2024-Q4"
    as_of = fields.Datetime()  # Point-in-time for snapshots
    recorded_at = fields.Datetime(required=True, default=fields.Datetime.now)
    expires_at = fields.Datetime(index=True)  # TTL expiration

    # Value storage (JSON for flexibility)
    value_json = fields.Json()  # e.g., {"value": 42} or {"value": 45.2, "confidence": 0.95}
    value_type = fields.Selection([
        ('number', 'Number'),
        ('string', 'Text'),
        ('boolean', 'Yes/No'),
        ('json', 'Complex JSON'),
    ])

    # Source tracking
    source_type = fields.Selection([
        ('computed', 'Computed'),
        ('aggregate', 'Aggregate'),
        ('external', 'External API'),
        ('scoring', 'Scoring Model'),
        ('push', 'API Push'),
        ('snapshot', 'Manual Snapshot'),
    ])
    provider = fields.Char(index=True)  # e.g., 'edu_ministry'
    params_hash = fields.Char()  # For distinguishing values with different parameters

    # Quality metadata
    coverage = fields.Float()  # Data completeness (0.0 to 1.0)
    is_stale = fields.Boolean(compute='_compute_is_stale')
    error_code = fields.Char()
    error_message = fields.Text()

    # Audit
    company_id = fields.Many2one('res.company', required=True)
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
| `cache_ttl_seconds` | TTL expiration time (default: 86400) |
| `invalidate_on_member_change` | Recompute when members change |
| `invalidate_on_field_change` | Fields that trigger recompute |

## The `metric()` Function

When a variable uses persistent caching (`ttl` or `manual`), the variable resolver emits a `metric()` call instead of inlining the variable's CEL expression.

### How It Works

1. Expression references `children_under_5_count`
2. Variable has `cache_strategy = 'ttl'`
3. Resolver emits: `metric('children_under_5_count', me)`
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
def _precompute_cycle_cached_variables(self, cycle, beneficiaries):
    """Precompute all cached variables before eligibility check."""
    cache_mgr = self.env["spp.data.cache.manager"]
    result = cache_mgr.precompute_cached_variables(
        subject_ids=beneficiaries.mapped("partner_id.id"),
        period_key="current",
        program_id=cycle.program_id.id,
    )
```

### When to Precompute

| Scenario | Recommendation |
|----------|----------------|
| Small batch (< 100) | On-demand is fine |
| Medium batch (100-1000) | Consider precompute |
| Large batch (> 1000) | Always precompute |

## Cache Manager Methods

The `spp.data.cache.manager` service provides cache lifecycle operations:

### Precomputation

```python
cache_mgr = env["spp.data.cache.manager"]

# Precompute a single variable
result = cache_mgr.precompute_variable(
    variable_name="complex_score",
    subject_ids=[1, 2, 3, 4, 5],
    period_key="2024-12",
    program_id=program.id,  # Optional
)

# Precompute ALL cached variables
result = cache_mgr.precompute_cached_variables(
    subject_ids=[1, 2, 3, 4, 5],
    period_key="current",
    program_id=program.id,  # Optional
    variable_names=["var1", "var2"],  # Optional filter
)
```

### Refresh Operations

```python
# Refresh a specific variable for subjects
values = cache_mgr.refresh_variable(
    variable_name="pmt_score",
    subject_ids=[1, 2, 3],
    period_key="current",
)

# Refresh all cached variables for a single subject
values = cache_mgr.refresh_variables_for_subject(
    subject_id=123,
    variable_names=["var1", "var2"],  # Optional, None = all
    period_key="current",
)

# Refresh stale cache entries (for cron jobs)
result = cache_mgr.refresh_stale_cached_variables(
    max_age_hours=24,
    batch_size=1000,
)
```

### Cache Invalidation

```python
# Invalidate specific subjects
count = cache_mgr.invalidate_variable(
    variable_name="pmt_score",
    subject_ids=[1, 2, 3],
    period_key="current",  # Optional
)

# Invalidate ALL cache entries for a variable
count = cache_mgr.invalidate_variable("household_size")
```

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
cache_mgr = env["spp.data.cache.manager"]

# Refresh specific variable for subjects
cache_mgr.refresh_variable(
    variable_name="children_count",
    subject_ids=registrants.ids,
)

# Refresh all cached variables for a subject
cache_mgr.refresh_variables_for_subject(
    subject_id=123,
    variable_names=None,  # None = all cacheable variables
)
```

## Source Code References

| Component | Location |
|-----------|----------|
| Variable model | `spp_cel_domain/models/cel_variable.py` |
| Resolver (metric emission) | `spp_cel_domain/models/cel_variable_resolver.py` |
| Value store | `spp_cel_domain/models/data_value.py` |
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
