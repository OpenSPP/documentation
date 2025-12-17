---
openspp:
  doc_status: unverified
---

# Expressions

Expressions (`spp.cel.expression`) define reusable business logic as CEL strings. They can represent:

- eligibility and compliance rules
- scoring formulas
- validation rules
- “library” logic that can be reused across configuration screens

Studio layers additional governance features on top of the base model (for example publish workflows, versioning, and tests).

## Classification

Expressions are typically categorized by:

- **Type** (eligibility, benefit, compliance, scoring, validation, …)
- **Context** (individual, group/household, or shared)
- **Output type** (boolean, number, string, money)

The base model defines these main types:

- `eligibility`, `benefit`, `compliance`, `scoring`, `validation`, `other`

## Lifecycle and dependencies

Expressions have a lifecycle state (for example draft vs active/published depending on installed Studio features).

The core model can also compute which variables are referenced by an expression (used for impact analysis and UI display).

## Authoring and governance (Studio)

Studio provides:

- a CEL editor with autocomplete and validation
- a test panel to validate behavior before publishing
- optional publishing workflow (for example draft → pending → published)

See {doc}`../../tutorial/variables_and_expressions` for an admin-focused walkthrough.

```{note}
Developer reference (source code): `openspp-modules-v2/spp_cel_domain/models/cel_expression.py`
```
