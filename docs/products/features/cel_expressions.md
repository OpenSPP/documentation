---
myst:
  html_meta:
    "title": "Common Expression Language (CEL)"
    "description": "OpenSPP's Common Expression Language (CEL) rules engine for eligibility, entitlement, and compliance logic"
    "keywords": "OpenSPP, CEL, Common Expression Language, rules engine, eligibility, entitlement, compliance, social protection"
---

# Common Expression Language (CEL)

OpenSPP's Common Expression Language (CEL) is a lightweight, purpose-built rules engine that powers eligibility criteria, entitlement formulas, compliance checks, and other configurable business logic across the platform, without requiring custom code for every rule.

## Configurable rules, safely and at scale

Social protection programs need business rules that change often — a new eligibility threshold, a revised benefit formula, an additional compliance condition — and that ideally don't require a developer and a deployment cycle every time. But letting non-developers write arbitrary expressions creates real risks if the engine isn't carefully built: a poorly sandboxed expression language can be exploited to reach outside its intended scope, and naive expression evaluation that loops through records one at a time in application code can grind to a halt against a registry with hundreds of thousands or millions of beneficiaries.

CEL addresses both problems by design. Its parser recognizes a small, readable set of operators and functions rather than a general-purpose scripting language, and it actively blocks access to the internal attributes and objects that a sandbox-escape attempt would rely on. For performance, expressions are compiled down to a query plan that pushes as much evaluation as possible into parameterized SQL, so eligibility and compliance rules can run efficiently across large registries rather than falling back to slow, record-by-record evaluation.

## CEL capabilities

* **Readable rule syntax**: Comparison, logical, and arithmetic operators, ternary conditionals, and list membership checks, combined with function calls for common patterns
* **Built-in date and household functions**: Functions like `age_years()` and `days_ago()`, plus household-aggregation helpers such as `members.exists()` and `members.count()`, cover common eligibility and compliance patterns out of the box
* **Reusable named variables**: Define variables backed by registry fields, constants, computed sub-expressions, household aggregates, external data sources, scoring models, or standardized vocabularies, then reference them by name across multiple rules
* **Security-hardened evaluation**: Blocks access to internal system attributes, limits expression recursion depth, and guards pattern-matching functions against runaway evaluation, so expressions written by non-developers can't be used to escape the sandbox
* **SQL-scale execution**: Expressions compile down to parameterized SQL where possible, designed to evaluate rules across large registries rather than looping through records one at a time
* **Caching for expensive variables**: Configurable caching avoids recomputing costly aggregates or external lookups on every evaluation
* **Rule preview and diagnostics**: Validate an expression, see its generated query and execution path, and preview which records currently match
* **Used throughout the platform**: Powers eligibility criteria, entitlement formulas, compliance checks, grievance routing, case triage, scoring models, and analytics indicators

## Technical implementation

CEL is delivered through the following modules:

* **[spp_cel_domain](/reference/modules/spp_cel_domain.md)**: Core CEL parser, query translator, executor, and variable/caching system
* **[spp_cel_widget](/reference/modules/spp_cel_widget.md)**: Syntax-highlighted expression editor with autocomplete
