---
openspp:
  doc_status: unverified
---

# CEL (Common Expression Language)

OpenSPP uses a CEL-based engine for rules and computations across the platform. The same CEL building blocks are reused in multiple places (Studio logic, program eligibility, event data queries, workflow routing, approvals, and more).

## Two ways CEL is used

**1) Compile-to-domain (filtering / selection)**  
Some features compile a CEL expression into an Odoo domain to select matching records (for example “which registrants match this eligibility rule”). This path uses CEL **profiles** (symbols and relations) and supports optimized query execution.

**2) Evaluate-with-context (runtime evaluation)**  
Some features evaluate a CEL expression against an in-memory context dictionary (for example a workflow rule that checks a ticket’s fields, or a formula that computes an entitlement amount).

## Start here (recommended reading order)

- {doc}`usage_by_feature` — where CEL is used in OpenSPP and which mode applies (compile-to-domain vs runtime evaluation)
- {doc}`profiles_and_symbols` — which symbols exist in each context (registry individuals/groups, enrollments, entitlements, GRM tickets, …)
- {doc}`variables` — how `spp.cel.variable` works (source types, aggregates, accessors, and caching strategies)
- {doc}`expressions` — how `spp.cel.expression` works (types, context, publishing, testing)
- {doc}`events` — event functions and event aggregations (requires the event/CEL integration modules)
- {doc}`widget_and_validation` — editor widget, autocomplete, linting, and validation APIs
- {doc}`caching_and_metric` — cached variables and the unified value store (`spp.data.value`)

```{toctree}
:maxdepth: 2
:hidden: true

usage_by_feature
profiles_and_symbols
variables
expressions
events
widget_and_validation
caching_and_metric
```
