# Variables and expressions (replacing “indicators”)

OpenSPP previously relied on “indicator” computed fields for derived values such as:

- number of children in a household
- whether a household is female-headed
- whether a registrant meets a threshold

In current deployments, these derived values are modeled as **variables** and **expressions** using the CEL-based engine (from the `spp_cel_domain` project) and configured through **Studio**.

## Where to configure

- **Studio → Variables**: define reusable named variables (field-based, constants, aggregates, computed values, external data, scoring results, vocabulary concepts).
- **Studio → Expressions**: define reusable business logic as CEL expressions (eligibility rules, scoring formulas, validations, etc.).

## Create a variable (Studio)

Example goal: **count children under 5 in a household**.

1. Go to **Studio → Variables** and click **Create**.
2. Set:
   - **Applies To**: Group/Household
   - **Source Type**: Aggregate
   - **Aggregate Target**: Members
   - **Aggregate Type**: Count
   - **Filter** (CEL): `age_years(m.birthdate) < 5`
3. Activate the variable.

Notes:
- Inside member aggregates, use the `m.` prefix for member fields (for example `m.birthdate`).
- Record fields are referenced using `r.` (for example `r.birthdate`) in general CEL expressions.
- Variables are referenced by their **name/accessor as bare identifiers** (for example `child_under_5_count`) and expanded by the resolver.

Screenshot placeholders:
- `indicators/studio_variables_list.png`
- `indicators/studio_variable_form_aggregate_members.png`

## Create an expression (Studio)

Example goal: **flag a household as priority** if it has at least one child under 5.

1. Go to **Studio → Expressions** and click **Create**.
2. Choose:
   - **Context**: Group/Household
   - **Output Type**: Yes/No (Boolean)
3. Enter a CEL expression:
   - `child_under_5_count >= 1`
4. Publish (or activate) the expression according to your governance settings.

Screenshot placeholders:
- `indicators/studio_expressions_list.png`
- `indicators/studio_expression_editor.png`

## Event-based indicators (advanced)

If your deployment includes the event/CEL integration, Studio variables can aggregate over event data (for example count of “Household Visit” events in the last 90 days, or the max score recorded this year). This is configured as an **Aggregate** variable targeting **Events**.
