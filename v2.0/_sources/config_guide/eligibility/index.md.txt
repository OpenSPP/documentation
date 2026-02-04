---
openspp:
  doc_status: draft
  products: [core]
---

# Eligibility rules

This guide is for **implementers** configuring eligibility rules to determine which registrants qualify for programs and benefits.

## What is eligibility?

Eligibility rules define who qualifies for a program. They translate policy decisions (e.g., "elderly citizens over 65" or "households with children under 5") into criteria that OpenSPP evaluates automatically against registry data.

```{mermaid}
graph LR
    R[Registry] --> E[Eligibility Manager]
    E --> |Evaluate| M{Matches?}
    M --> |Yes| Q[Eligible]
    M --> |No| N[Not Eligible]
    Q --> P[Program Enrollment]
```

## How eligibility works in OpenSPP

Each program has an **Eligibility Manager** that controls how eligibility is determined. The manager uses **CEL expressions** (Common Expression Language) to define criteria.

| Component | Purpose |
|-----------|---------|
| **Eligibility Manager** | Container for eligibility configuration |
| **CEL Expression** | The rule that determines eligibility |
| **Geographic Targeting** | Optional area-based restrictions |
| **Templates** | Pre-built expressions for common criteria |

## Quick start

To configure eligibility for a program:

1. Go to **Programs → Programs** and open your program
2. Click the **Configuration** tab
3. Find the **Eligibility Manager** section
4. Write a CEL expression or select a template
5. Review the match count and save

```{image} /_images/en-us/config_guide/eligibility/01-eligibility-manager-overview.png
:alt: Eligibility Manager section in program configuration
:class: img-fluid
```

## What you'll find here

```{toctree}
:maxdepth: 1
:hidden:

cel_expressions
geographic_targeting
templates
testing
advanced
```

| Guide | Description |
|-------|-------------|
| {doc}`cel_expressions` | Write CEL expressions for eligibility criteria |
| {doc}`geographic_targeting` | Target registrants by administrative area |
| {doc}`templates` | Use and create expression templates |
| {doc}`testing` | Validate and test eligibility rules |
| {doc}`advanced` | Multiple managers, legacy options, performance |

## Common eligibility patterns

| Program type | Example expression |
|--------------|-------------------|
| Senior citizens (65+) | `age_years(r.birthdate) >= 65` |
| Households with young children | `members.count(m, age_years(m.birthdate) < 5) >= 1` |
| Female-headed households | `members.exists(m, head(m) and is_female(m.gender_id))` |
| Large households | `hh_size >= 4` |
| Adult women | `is_female(r.gender_id) and age_years(r.birthdate) >= 18` |

See {doc}`cel_expressions` for the full syntax reference.

## Are you stuck?

**No registrants match my criteria?**
Check that your expression uses the correct context (`r` for registrant, `m` for member iteration). Use the Preview Beneficiaries button to debug.

**Expression shows an error?**
CEL uses `and`/`or` (not `AND`/`OR`). Check parentheses and field names.

**Need help with complex rules?**
See the {doc}`templates` page for pre-built patterns, or {doc}`cel_expressions` for the full syntax reference.
