---
openspp:
  doc_status: unverified
  products: [core]
---

# Variables and expressions (CEL) for developers

OpenSPP uses CEL-based **variables** and **expressions** as the primary way to implement reusable business logic (eligibility rules, validations, scoring formulas, workflow routing conditions, and more).

If you are coming from older “indicator-as-computed-field” patterns, treat variables/expressions as the preferred replacement for *most* derived values and rules.

## When to use variables vs custom code

- Use **variables** (`spp.cel.variable`) to define reusable data points once (constants, computed formulas, aggregates, external values).
- Use **expressions** (`spp.cel.expression`) to define reusable logic/rules that can be referenced from multiple configuration screens.
- Use **custom Odoo code** when you must change the data model, add complex UI, or implement a new compute path that cannot be expressed as CEL.

For the admin workflow (Studio screens), see {doc}`../../tutorial/variables_and_expressions`.
For the technical reference (profiles, symbols, caching, events), see {doc}`../../technical_reference/cel/index`.

## 1) Extending profiles and symbols (compile-to-domain)

Compile-to-domain features (like registry filtering and program eligibility) use **CEL profiles** to define what symbols and relations exist in a given context.

To extend a profile from your own module, provide a YAML file:

- `your_module/data/cel_profiles.yaml`

Example: extend the group registry profile with a new relation symbol:

```yaml
version: 1
presets:
  registry_groups:
    symbols:
      my_relation:
        relation: "many2one"
        field: "my_relation_id"
        model: "my.relation.model"
```

Profile configuration precedence is:

1. system parameters (deployment overrides)
2. module YAML (`data/cel_profiles.yaml` across installed modules)
3. built-in defaults

## 2) Adding runtime functions (evaluate-with-context)

Runtime evaluation screens call the CEL evaluator against a context dictionary (for example entitlement amount formulas). To add a runtime function, register it in the function registry:

```python
def is_even(n):
    try:
        return int(n) % 2 == 0
    except Exception:
        return False
```

Registering can be done from your module initialization (for example in a post-init hook):

```python
def post_init_hook(env):
    env["spp.cel.function.registry"].register("is_even", is_even)
```

```{note}
Runtime evaluation is designed to be safe: do not rely on ORM side effects, and avoid registering functions that perform writes or access privileged operations.
```

## 3) Adding compile-to-domain helpers (translator extensions)

If you need a new function that must work in **compile-to-domain** (record selection), implement it in the domain translator by inheriting `spp.cel.translator` and overriding `_to_plan`.

This is the same extension pattern used by the event data integration module.

## 4) Validating and debugging expressions

Use the CEL service facade:

- `env["spp.cel.service"].compile_expression(expr, profile)` for compile-to-domain validation and previews
- `env["spp.cel.service"].evaluate_expression(expr, context)` for runtime evaluation

Most UI screens also use the CEL editor widget, which exposes profile-aware symbol browsing and validation via JSON-RPC.

```{note}
Developer reference (source code):
- CEL service: `openspp-modules-v2/spp_cel_domain/models/cel_service.py`
- Profile registry: `openspp-modules-v2/spp_cel_domain/models/cel_registry.py`
- Function registry: `openspp-modules-v2/spp_cel_domain/models/cel_function_registry.py`
- Widget endpoints: `openspp-modules-v2/spp_cel_widget/controllers/main.py`
- Translator extension example (events): `openspp-modules-v2/spp_cel_event/models/cel_event_translator.py`
```
