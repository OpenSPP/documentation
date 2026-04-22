---
openspp:
  doc_status: draft
  products: [core]
---

# CEL (Common Expression Language)

**For: developers**

OpenSPP uses Common Expression Language (CEL) as its core expression system for eligibility rules, scoring, dynamic domain queries, and member aggregates. This page covers the parts developers extend — evaluating expressions from code, registering custom functions, and defining new variables.

## How to use this section

1. Read this page for architecture, entry points, and extension patterns
2. Read {doc}`internals` when you need to understand the caching system, batch precomputation, or period-key semantics
3. Check `doc-principles` and the Config Guide pages for CEL if you are writing expressions as an implementer (not extending the engine)

## Prerequisites

- Python and Odoo model basics
- Familiarity with Odoo domain syntax (CEL compiles to Odoo domains for filtering)
- General understanding of expression evaluation (CEL is similar in spirit to Google's CEL, but OpenSPP ships its own custom parser)

## When do you need this?

| Requirement | Approach |
|-------------|----------|
| Write an eligibility rule or a scoring formula | Use the UI — create a variable or expression record |
| Call CEL from Python code | Use `env["spp.cel.service"]` entry points |
| Add a new built-in function (e.g., `distance_km()`) | Register via `spp.cel.function.registry` |
| Define a new data-source variable | Create `spp.cel.variable` records in your module's XML data |
| Aggregate over events (visits, interactions) | Use `spp_cel_event` with `spp.cel.variable.event.agg` |
| Look up vocabulary codes in expressions | Use `spp_cel_vocabulary`'s `code()` and `in_group()` |
| Render a CEL editor in a form view | Use the `cel_expression` widget from `spp_cel_widget` |

## The CEL modules

These modules are all under `openspp-modules-v2/`:

| Module | Purpose |
|--------|---------|
| `spp_cel_domain` | Core CEL parser, evaluator, variable system, cache manager (`spp.data.value`), function registry |
| `spp_cel_event` | Event-data aggregation variables — count/sum events filtered by type and date window |
| `spp_cel_vocabulary` | Vocabulary-aware functions: `code()` (URI or alias lookup), `in_group()` (concept-group membership) |
| `spp_cel_registry_search` | Registry search powered by CEL expressions (UI + backend) |
| `spp_cel_widget` | OWL + CodeMirror editor with autocomplete and linting; HTTP endpoints for symbols/validation |

```{note}
OpenSPP ships its **own CEL parser** (`spp_cel_domain/services/cel_parser.py`), not an external library like `cel-python` or `celpy`. This is deliberate — it lets us enforce security (blocked attribute access, sandboxed evaluation) and compile expressions to Odoo domains for fast SQL filtering.
```

## Entry points

The main public API is the `spp.cel.service` AbstractModel (`spp_cel_domain/models/cel_service.py`).

### Evaluate an expression directly

```python
service = env["spp.cel.service"]

# Evaluate against a subject record (the "me" variable)
result = service.evaluate_expression(
    "age_years(me.birthdate) >= 18 && me.gender_id.code == 'female'",
    profile_or_context="individual",  # or a context dict
    context={"me": partner},
)
```

Returns the evaluated result (`bool`, `int`, `float`, `str`, or a recordset for collection expressions).

### Compile an expression to an Odoo domain

Used by eligibility and search features that need to filter records efficiently:

```python
result = service.compile_expression(
    expression="age_years(me.birthdate) >= 18",
    profile="individual",
    base_domain=[("is_registrant", "=", True)],
    limit=100,
)
# result = {
#     "domain": [...],        # Odoo domain ready for search()
#     "count": int,
#     "ids": [...],
#     "preview_records": [...],
#     "valid": bool,
#     "error": str | None,
#     "explain": str,          # Human-readable summary
#     "path": str,             # Compilation strategy taken
# }
```

### Evaluate with variable expansion

When your expression references named variables (e.g., `children_count >= 2`), use `evaluate_with_variables`. The resolver looks up each variable's definition from `spp.cel.variable`, recursively expands its CEL expression (or emits a `metric()` call if the variable is cached), and evaluates the result:

```python
result = service.evaluate_with_variables(
    expression="children_count >= 2 && household_income < 50000",
    context={"me": group},
    program_id=program.id,
    context_type="group",
)
```

### Member aggregates

Evaluate an expression over each member of a group and aggregate the result:

```python
count = service.evaluate_member_aggregate(
    group=household,
    expression="age_years(m.birthdate) < 18",
)
```

Inside the expression, `m` is each member. The return type depends on the aggregate form — `count`, `sum`, `avg`, etc. are controlled by the variable definition when called via `evaluate_with_variables`.

## Built-in functions

All of the functions below are defined in `spp_cel_domain/services/cel_functions.py` and available in every CEL evaluation. They reach expressions through two different paths:

- **Via `spp.cel.function.registry`** (appear in `registry.list_functions()`): `age_years`, `years_ago`, `between`
- **Injected directly into the evaluator context** (not in the registry): `today`, `now`, `days_ago`, `months_ago`, `size`, `has`, `matches`

Both paths work identically inside expressions — the distinction only matters if you introspect the registry programmatically.

| Function | Signature | Purpose |
|----------|-----------|---------|
| `age_years(date)` | `date` → `int` | Age in years from a date (typically `birthdate`); returns `None` for null input |
| `today()` | `() → date` | Current date |
| `now()` | `() → datetime` | Current datetime |
| `days_ago(n)` | `int → date` | Date `n` days in the past |
| `months_ago(n)` | `int → date` | Date `n` months in the past |
| `years_ago(n)` | `int → date` | Date `n` years in the past |
| `between(x, a, b)` | `(num, num, num) → bool` | True if `a ≤ x ≤ b` |
| `size(collection)` | `collection → int` | Size of a collection (list, recordset, string) |
| `has(obj, field=None)` | `(obj, str?) → bool` | True if `obj.field` has a non-empty value (or `obj` itself if `field` omitted) |
| `matches(string, pattern)` | `(str, regex) → bool` | Regex match |

Additional functions from `spp_cel_vocabulary`:

| Function | Signature | Purpose |
|----------|-----------|---------|
| `code(identifier)` | `str → spp.vocabulary.code` | Resolve a vocabulary code by URN or alias |
| `in_group(code_value, group_name)` | `(str, str) → bool` | Whether a code belongs to a concept group |

## Registering a custom CEL function

Register your function(s) via `spp.cel.function.registry`. Because the registry lives in process memory, registration must run on **every server start** — not just at install time. The cleanest pattern is an `_register_hook` classmethod on a tiny `AbstractModel`.

### `your_module/services/cel_functions.py`

```python
import math


def distance_km(lat1, lon1, lat2, lon2):
    """Great-circle distance in kilometers between two lat/lon pairs."""
    r = 6371.0
    lat1, lat2 = map(math.radians, (lat1, lat2))
    dlat = lat2 - lat1
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    return 2 * r * math.asin(math.sqrt(a))


def is_in_buffer_zone(partner, zone_name, radius_km):
    """True if the partner's location is within radius_km of the zone centroid."""
    zone = partner.env["spp.buffer.zone"].search([("name", "=", zone_name)], limit=1)
    if not zone or not partner.latitude or not partner.longitude:
        return False
    return distance_km(partner.latitude, partner.longitude, zone.lat, zone.lon) <= radius_km
```

### `your_module/models/cel_functions.py`

```python
from odoo import api, models

from ..services.cel_functions import distance_km, is_in_buffer_zone


class YourModuleCelFunctions(models.AbstractModel):
    _name = "your_module.cel.functions"
    _description = "Custom CEL function registrations for your_module"

    @api.model
    def _register_hook(self):
        # Called by Odoo on every server start / worker spawn.
        registry = self.env["spp.cel.function.registry"]
        registry.register("distance_km", distance_km)
        registry.register("is_in_buffer_zone", is_in_buffer_zone)
        return super()._register_hook()
```

### `your_module/__manifest__.py`

```python
{
    # ...
    "depends": ["spp_cel_domain"],
}
```

Functions receive plain Python arguments already unwrapped from CEL; returning primitives, recordsets, or vocabulary codes is fine. The registry is per-process; you do not need to persist anything to the database.

## Testing custom CEL functions

Tests should cover three things: the function's own logic, that it actually ends up in the registry after `_register_hook` runs, and that it works inside a real CEL expression.

### `your_module/tests/test_cel_functions.py`

```python
"""Tests for custom CEL functions."""

from odoo.tests import TransactionCase, tagged

from odoo.addons.spp_cel_domain.services import cel_parser as P

from ..services.cel_functions import distance_km, is_in_buffer_zone


@tagged("post_install", "-at_install")
class TestDistanceFunction(TransactionCase):

    # Unit tests: call the function directly, no CEL involved.

    def test_distance_km_same_point(self):
        """Distance between identical points is zero."""
        self.assertAlmostEqual(distance_km(14.6, 121.0, 14.6, 121.0), 0.0, places=3)

    def test_distance_km_known_values(self):
        """Manila to Cebu is roughly 570 km."""
        result = distance_km(14.5995, 120.9842, 10.3157, 123.8854)
        self.assertGreater(result, 560)
        self.assertLess(result, 580)

    # Registry test: confirm _register_hook actually ran.

    def test_distance_km_registered(self):
        """The function is registered on spp.cel.function.registry."""
        registry = self.env["spp.cel.function.registry"]
        self.assertTrue(registry.is_registered("distance_km"))
        self.assertTrue(registry.is_registered("is_in_buffer_zone"))

    # Integration test: use the function inside a CEL expression.

    def test_distance_km_in_expression(self):
        """distance_km can be called from a CEL expression."""
        context = {
            "distance_km": distance_km,
            "home_lat": 14.5995,
            "home_lon": 120.9842,
            "office_lat": 14.5547,
            "office_lon": 121.0244,
        }
        ast = P.parse("distance_km(home_lat, home_lon, office_lat, office_lon) < 10")
        self.assertTrue(P.evaluate(ast, context))
```

### What each test covers

- **Unit tests** verify the function's internal logic in isolation. They do not depend on Odoo state and are fast.
- **Registry tests** confirm your `_register_hook` actually registered the function. This catches the common bug where a developer adds a function but forgets to add an `AbstractModel` for it, so `_register_hook` never runs and the function is silently missing from the registry after a server restart.
- **Integration tests** verify the function works end-to-end inside a CEL expression using `cel_parser.parse()` and `cel_parser.evaluate()`. The test injects the function into the evaluator context the same way `spp.cel.service` does at runtime.

## Registering a variable

Variables are records on `spp.cel.variable`. You can create them through the UI, but modules usually ship them as XML data.

### Field-source variable (direct model field)

```xml
<record id="var_income" model="spp.cel.variable">
    <field name="name">Monthly Income</field>
    <field name="cel_accessor">income</field>
    <field name="source_type">field</field>
    <field name="source_model">res.partner</field>
    <field name="source_field">income</field>
    <field name="value_type">money</field>
    <field name="cache_strategy">none</field>
</record>
```

### Aggregate variable (count/sum over group members)

```xml
<record id="var_children_count" model="spp.cel.variable">
    <field name="name">Children Under 18</field>
    <field name="cel_accessor">children_count</field>
    <field name="source_type">aggregate</field>
    <field name="aggregate_type">count</field>
    <field name="aggregate_target">members</field>
    <field name="aggregate_filter">age_years(m.birthdate) &lt; 18</field>
    <field name="cache_strategy">ttl</field>
    <field name="cache_ttl_seconds">86400</field>
    <field name="invalidate_on_member_change" eval="True" />
</record>
```

For aggregates, always set `invalidate_on_member_change=True` so the cache refreshes when group composition changes.

### Computed variable (custom CEL expression)

```xml
<record id="var_pmt_score" model="spp.cel.variable">
    <field name="name">PMT Score</field>
    <field name="cel_accessor">pmt_score</field>
    <field name="source_type">computed</field>
    <field name="cel_expression">
        0.3 * income_normalized + 0.4 * children_count + 0.3 * education_level_score
    </field>
    <field name="cache_strategy">ttl</field>
    <field name="cache_ttl_seconds">86400</field>
</record>
```

For the full list of variable fields, source types, and caching behavior, see {doc}`internals`.

## HTTP endpoints (for the editor widget)

The CEL widget communicates with the backend via three JSON-RPC endpoints:

| Endpoint | Purpose |
|----------|---------|
| `POST /spp_cel/symbols/<profile>` | Return available variables, functions, and operators for a profile (for autocomplete) |
| `POST /spp_cel/validate` | Validate an expression without evaluating it |
| `POST /spp_cel/profiles` | List available profiles |

These endpoints are internal to the widget — CEL evaluation itself has no public REST endpoint. Evaluation is backend-only through `env["spp.cel.service"]`.

## Exception types

When an expression fails, `spp.cel.service` raises one of the typed errors from `spp_cel_domain/exceptions.py`:

| Exception | Meaning |
|-----------|---------|
| `CELSyntaxError` | Malformed expression (parse failure) |
| `CELSymbolError` | Unknown field or variable reference |
| `CELTypeError` | Type mismatch (e.g., comparing string to int) |
| `CELFunctionError` | Invalid function call (wrong arity, unknown name) |
| `CELExecutionError` | Runtime evaluation failure |
| `CELMetricsUnavailableError` | Expression calls `metric()` but the metrics infrastructure isn't installed |
| `CELProfileError` | Profile configuration invalid or missing |
| `CELValidationError` | Violates scalability or security constraints |

All inherit from `CELError`, so you can catch the base class to handle any CEL failure uniformly.

## Common mistakes

**Forgetting to re-register functions on every server start.** The CEL function registry is stored on the Odoo registry (per-process memory), not in the database — so every new Python process starts with an empty registry. Registering only in `post_init_hook` (which fires on install/upgrade) leaves your function missing after a plain server restart. The correct pattern is to also define an `_register_hook()` classmethod on an `AbstractModel` — Odoo calls `_register_hook` every time the registry is built (server start, worker spawn, module update). This is exactly how `spp.cel.function.registry` registers its own core functions; inherit the pattern for your own.

**Using `cache_strategy="ttl"` without setting `invalidate_on_member_change`.** For group aggregates, the cache doesn't know to refresh when members come and go. The result: yesterday's member count on a household that had a new baby this morning.

**Filtering vocabulary by `vocabulary_id.name` in Many2one domains.** Names are translated. Use `namespace_uri` (stored on the code record) instead — locale-safe and stable.

**Calling `metric()` directly in a user-written expression.** `metric()` is an internal compile-time construct emitted by the variable resolver for cached variables. Users should reference the variable by name — the resolver decides whether to inline the expression or emit a `metric()` call based on `cache_strategy`.

**Assuming evaluation is async.** CEL evaluation is synchronous and runs inside the request transaction. For expensive computations, move work into cached variables (`cache_strategy="ttl"` or `"manual"`) and precompute via `spp.data.cache.manager`.

**Period-key mismatches.** If a variable has `period_granularity="monthly"`, passing `period_key="2024"` (yearly format) returns nothing. Match the period-key format to the granularity.

## See also

- {doc}`internals` — caching, unified value store, batch precomputation, performance tuning
- {doc}`/developer_guide/custom_modules/index` — registering modules that ship CEL functions or variables
- {doc}`/developer_guide/change_request_types/approval_hooks` — dynamic approval uses CEL conditions to route approvals

```{toctree}
:maxdepth: 2
:hidden:

internals
```
