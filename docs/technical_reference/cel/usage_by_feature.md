---
openspp:
  doc_status: unverified
---

# How OpenSPP uses CEL

OpenSPP uses CEL in multiple features, but not all CEL-enabled screens behave the same way.

There are two main execution modes:

- **Compile-to-domain**: CEL is translated into an Odoo domain (and optionally into SQL for scale) to *select records*.
- **Runtime evaluation**: CEL is evaluated against an in-memory context dictionary to *compute a value* or *decide a rule outcome*.

This page maps common OpenSPP features to the CEL mode they use and the symbols you can expect.

## Feature map

| Feature / screen | What you author | CEL mode | Profile / context root |
| --- | --- | --- | --- |
| Studio → Variables | Variable definitions (`spp.cel.variable`) | N/A (inputs to both modes) | N/A |
| Studio → Expressions | Expression library (`spp.cel.expression`) | N/A (used by features) | Context depends on consumer |
| Registry search (CEL) | Filter expression | Compile-to-domain | `registry_individuals` or `registry_groups` (root: `me`/`r`) |
| Program eligibility / compliance rules | Selection criteria | Compile-to-domain | Usually registry profiles (root: `me`/`r`) |
| Scoring “CEL Formula” indicators | Formula expression | Compile-to-domain (validation) + scoring execution | Profile set on scoring model (default often registry) |
| Event data queries (when installed) | `has_event(...)`, `events_count(...)`, `event(...)` | Compile-to-domain | Registry profiles extended with `events` |
| Entitlement amount formulas | Amount formula | Runtime evaluation | Context includes `me` (beneficiary record) and `base_amount` |
| GRM routing / escalation rules | Rule conditions | Runtime evaluation | Context typically includes `ticket` and `r` (ticket) |
| Case triage / assignment rules | Rule conditions | Runtime evaluation | Context depends on case module (record + helper values) |
| Approvals (conditions / reviewer assignment) | Rule conditions | Runtime evaluation | Context includes the approval target record and workflow data |
| Data classification patterns | Classification predicates | Runtime evaluation | Context depends on classification integration |
| Verifiable credential claims | Claim expressions | Runtime evaluation | Context depends on credential integration |

```{important}
The available symbols and functions are **mode-dependent**:

- Compile-to-domain supports profile symbols, relations (members/enrollments/entitlements/events), and domain-specific helpers.
- Runtime evaluation supports arithmetic, comparisons, ternary, safe builtins, and registered runtime functions — but it does not have access to ORM search and should be treated as a pure function over a provided context.
```

## How to discover symbols for compile-to-domain screens

For screens that use the CEL editor widget, use the symbol browser / autocomplete to see:

- which **profile** is in use
- which **symbols** exist in that profile (root record, relations, fields)
- which **variables** and **library expressions** are available in that context

See {doc}`widget_and_validation` and {doc}`profiles_and_symbols`.

## Notes for runtime evaluation screens

Runtime evaluation screens often provide only a small set of context variables (for example `me`, `base_amount`).

If a screen does **not** use the CEL editor widget, the most reliable way to confirm the available context is to read the implementation and the field help text for that screen.

```{note}
Developer reference (source code, examples):
- CEL service facade: `openspp-modules-v2/spp_cel_domain/models/cel_service.py`
- Profiles and merge rules: `openspp-modules-v2/spp_cel_domain/models/cel_registry.py`
- Widget symbol APIs: `openspp-modules-v2/spp_cel_widget/controllers/main.py`
- Program eligibility/compliance: `openspp-modules-v2/spp_programs/models/cel/eligibility_cel.py`, `openspp-modules-v2/spp_programs/models/cel/compliance_cel.py`
- Entitlement amount formulas: `openspp-modules-v2/spp_programs/models/cel/entitlement_amount_cel.py`
- Scoring indicator validation: `openspp-modules-v2/spp_scoring/models/scoring_indicator.py`
- Event/CEL integration: `openspp-modules-v2/spp_cel_event/models/cel_event_translator.py`
```

