---
openspp:
  doc_status: unverified
---

# Variables and expressions (CEL)

OpenSPP uses CEL-based **variables** and **expressions** as a shared logic layer:

- **Variables** represent reusable data points (field values, constants, aggregates, computed formulas, external values).
- **Expressions** represent reusable rules (eligibility, validation, scoring formulas, routing conditions, etc.).

This page focuses on how to **author and manage** variables and expressions with Studio. Feature-specific pages (Programs, GRM, Case, Approvals, Event Data, etc.) reference these building blocks.

For a “start from zero” guide and common recipes:

- {doc}`cel_quickstart`
- {doc}`cel_cookbook`
- {doc}`cel_troubleshooting`

## Where to configure (Studio)

- **Studio → Variables**: create and manage `spp.cel.variable`
- **Studio → Expressions**: create and manage `spp.cel.expression`
- **Studio → Expressions → Tests**: define test cases for expressions (recommended before publishing)

```{note}
Screenshot placeholders:
- `tutorial/variables_and_expressions/studio_variables_list.png`
- `tutorial/variables_and_expressions/studio_variable_form.png`
- `tutorial/variables_and_expressions/studio_expressions_list.png`
- `tutorial/variables_and_expressions/studio_expression_editor.png`
- `tutorial/variables_and_expressions/studio_expression_tests.png`
```

## Core syntax you’ll see in the UI

Depending on the screen, you may see either `me` or `r` used for the “current record”.

- `me.<field>` / `r.<field>`: field on the current record (for example the current registrant)
- `members.exists(<predicate>)` / `members.count(<predicate>)`: aggregate over household members (group context)
- `enrollments.exists(<predicate>)` / `enrollments.count(<predicate>)`: aggregate over program enrollments
- `entitlements.exists(<predicate>)` / `entitlements.count(<predicate>)`: aggregate over entitlements

Inside collection predicates, OpenSPP commonly uses:

- `m.<field>` for the “loop variable” (for example `age_years(m.birthdate) < 5`)
- `and` / `or` / `not` (you may also see `&&` / `||` / `!`)

Some older screens and examples use an explicit loop variable syntax (still supported in many places), for example:

```text
members.count(m, age_years(m.birthdate) < 5)
enrollments.exists(e, e.state == "enrolled")
```

## Create a variable

### Example: “children under 5” (household)

Goal: count children under 5 in a household.

1. Go to **Studio → Variables** and click **Create**.
2. Set:
   - **Applies To**: Group/Household
   - **Source Type**: Aggregate
   - **Aggregate Target**: Members
   - **Aggregate Type**: Count
   - **Filter**: `age_years(m.birthdate) < 5`
3. Set a stable **CEL Accessor** (for example `children_under_5_count`) and **Activate** the variable.

You can now reference the variable in expressions by its accessor (bare identifier):

```text
children_under_5_count >= 1
```

## Create an expression

### Example: “priority household” flag

Goal: flag households as “priority” when they have at least one child under 5.

1. Go to **Studio → Expressions** and click **Create**.
2. Set:
   - **Type**: Eligibility (or Validation/Other as appropriate)
   - **Context**: Group/Household
   - **Output Type**: Yes/No (Boolean)
3. Enter the expression:

```text
children_under_5_count >= 1
```

4. Save and run tests (recommended).
5. Publish when ready (if your deployment uses a publish workflow).

## How variables and expressions are used across OpenSPP

The same CEL building blocks are used in multiple features:

- **Programs**: eligibility and compliance criteria can compile CEL into record selection filters; some entitlement amounts can be computed by evaluating CEL formulas against a beneficiary record.
- **Event Data**: event functions and event aggregations allow conditions like “has a visit in last 90 days”.
- **GRM**: routing/escalation rules can evaluate CEL against ticket context.
- **Case management**: triage/assignment rules can evaluate CEL against case context.
- **Approvals**: approval definitions can use CEL conditions and CEL-based reviewer assignment.
- **Registry**: a “Registry (CEL)” search portal can filter registrants using CEL expressions.

For the technical model (profiles, symbols, validation, caching, event functions), see {doc}`../technical_reference/cel/index`.
