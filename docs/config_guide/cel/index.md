---
openspp:
  doc_status: draft
---

# CEL Expressions

This guide is for **implementers** configuring OpenSPP rules and formulas.

OpenSPP uses CEL (Common Expression Language) as a shared logic layer for:
- Program eligibility and compliance rules
- Scoring formulas and indicators
- Entitlement amount calculations
- Workflow routing and escalation
- Data validation rules
- Event-based conditions

## Mental Model

CEL in OpenSPP has three key concepts:

| Concept | What It Is | Example |
|---------|-----------|---------|
| **Symbols** | Data available in context | `me`, `members`, `enrollments` |
| **Variables** | Named, reusable data points | `children_under_5_count`, `poverty_line` |
| **Expressions** | Reusable rules/formulas | `children_under_5_count >= 1 and household_income < poverty_line` |

## Where to Configure

In **Studio**, you configure:

| Location | What You Create |
|----------|-----------------|
| Studio → Variables | Named data points (`spp.cel.variable`) |
| Studio → Expressions | Reusable rules (`spp.cel.expression`) |
| Studio → Expressions → Tests | Test cases for expressions |

## How CEL Is Used

OpenSPP uses CEL in two modes:

| Mode | Purpose | Examples |
|------|---------|----------|
| **Compile-to-domain** | Select matching records | Eligibility rules, registry search |
| **Runtime evaluation** | Compute values at runtime | Entitlement amounts, workflow routing |

## Topics

```{toctree}
:maxdepth: 1

quick_start
syntax
variables
cookbook
troubleshooting
```

## Quick Reference

### Common Operators

| Operator | Example | Description |
|----------|---------|-------------|
| `and` / `&&` | `a and b` | Both must be true |
| `or` / `\|\|` | `a or b` | Either can be true |
| `not` / `!` | `not a` | Negation |
| `==` | `me.status == "active"` | Equality |
| `<`, `>`, `<=`, `>=` | `age_years(me.birthdate) >= 18` | Comparison |
| `? :` | `me.is_group ? 1 : 0` | Ternary (if/else) |

### Common Functions

| Function | Example | Description |
|----------|---------|-------------|
| `has()` | `has(me.birthdate)` | Check field exists |
| `age_years()` | `age_years(me.birthdate)` | Calculate age in years |
| `members.count()` | `members.count(age < 18)` | Count matching members |
| `members.exists()` | `members.exists(age < 5)` | Check if any match |
| `members.sum()` | `members.sum(m.income, true)` | Sum member values |

## Next Steps

- **New to CEL?** Start with {doc}`quick_start`
- **Need examples?** See {doc}`cookbook`
- **Something not working?** Check {doc}`troubleshooting`
