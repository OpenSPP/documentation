---
openspp:
  doc_status: unverified
---

# Caching and `metric()`

OpenSPP’s variable system supports persistent caching for variables that are expensive to compute (or sourced externally).

## The unified value store (`spp.data.value`)

Cached variable values are stored in a dedicated model (`spp.data.value`). This enables:

- fast SQL-based lookups during eligibility compilation
- batch precomputation (warming the cache before running large filters)
- TTL expiration or manual refresh

## When `metric()` appears

When a variable is configured with a persistent cache strategy (`ttl` or `manual`), the variable resolver emits a `metric()` call instead of inlining the variable’s full CEL expression. This allows the engine to fetch a cached value from the unified value store.

## Precomputation in batch workflows

Some workflows (for example program cycle eligibility checks) can precompute cached variables for a set of beneficiaries before applying eligibility rules. This avoids expensive per-record computation and improves performance on large datasets.

```{note}
Developer reference (source code):
- Variable caching fields: `openspp-modules-v2/spp_cel_domain/models/cel_variable.py`
- Resolver emission of `metric(...)`: `openspp-modules-v2/spp_cel_domain/models/cel_variable_resolver.py`
- Cache lifecycle manager: `openspp-modules-v2/spp_cel_domain/models/data_evaluator.py` (`spp.data.cache.manager`)
- Cycle precompute hook: `openspp-modules-v2/spp_programs/models/managers/cycle_manager_base.py`
```

