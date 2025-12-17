---
openspp:
  doc_status: unverified
---

# CEL quickstart (for implementers)

This quickstart is for people configuring OpenSPP (for example M&E teams, program implementers, and technical staff) who are comfortable with “logic builders” (CommCare/Kobo-style configuration), but are not writing Python modules.

OpenSPP uses CEL to define reusable **variables** and **expressions** that power rules across the system (program eligibility, scoring formulas, workflow routing, validations, event-based conditions, and more).

## Mental model (3 things)

1. **Symbols**: “what data exists in this screen’s context” (the current record, and related records).
2. **Variables**: named data points you define once and reuse (constants, computed formulas, aggregates, external values).
3. **Expressions**: reusable rules you define once and reuse (boolean rules, numeric formulas, validations).

```{note}
Depending on the screen you may see `me` or `r` for the “current record”. Both can exist depending on configuration. In newer screens, prefer `me`.
```

## Where you configure it (Studio)

- **Studio → Variables**: create/manage variables
- **Studio → Expressions**: create/manage expressions
- **Studio → Expressions → Tests**: create test cases (recommended before publishing)

Screenshot placeholders:

- `tutorial/cel_quickstart/studio_variables_list.png`
- `tutorial/cel_quickstart/studio_variable_form.png`
- `tutorial/cel_quickstart/studio_expressions_list.png`
- `tutorial/cel_quickstart/studio_expression_editor.png`
- `tutorial/cel_quickstart/studio_expression_tests.png`

## Example A — “Children under 5” (household variable)

Goal: create a variable `children_under_5_count` that counts household members under 5.

1. Go to **Studio → Variables** and click **Create**.
2. Set:
   - **Applies To**: Group/Household
   - **Source Type**: Aggregate
   - **Aggregate Target**: Members
   - **Aggregate Type**: Count
   - **Filter**: `age_years(m.birthdate) < 5`
   - **CEL Accessor**: `children_under_5_count`
3. Activate the variable.

Now you can reference it (by accessor) in any expression in the same context:

```text
children_under_5_count >= 1
```

## Example B — “Priority household” (expression)

Goal: create an expression that flags priority households.

1. Go to **Studio → Expressions** and click **Create**.
2. Set:
   - **Type**: Eligibility (or “Other” depending on your use case)
   - **Context**: Group/Household
   - **Output Type**: Yes/No (Boolean)
3. Enter:

```text
children_under_5_count >= 1
```

4. Save and add **Tests** (recommended).

## How to know what data you can use

Most CEL-enabled screens use the CEL editor widget, which provides:

- autocomplete for available symbols and fields
- a symbol browser (profiles, variables, functions)
- validation errors with locations

See {doc}`../technical_reference/cel/widget_and_validation` and {doc}`../technical_reference/cel/profiles_and_symbols`.

## Next steps

- Common recipes: {doc}`cel_cookbook`
- Debugging and “why doesn’t this work”: {doc}`cel_troubleshooting`
- How OpenSPP uses CEL by feature: {doc}`../technical_reference/cel/usage_by_feature`

