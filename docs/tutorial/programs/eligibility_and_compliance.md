---
openspp:
  doc_status: unverified
---

# Program eligibility and compliance rules (CEL)

OpenSPP programs use managers to decide:

- **Eligibility**: who qualifies to be enrolled.
- **Compliance**: who remains compliant (used in cycles to mark beneficiaries as non-compliant).

Both are configured using CEL expressions that compile to an Odoo domain (“compile-to-domain”), which means they can be validated and previewed before you apply them.

## Where to configure

1. Go to **Programs → Programs** and open your program.
2. Open the **Configuration** tab.
3. In **Eligibility Manager**, click the **gear** icon on the manager you want to configure (usually “Default Eligibility”).

Screenshot placeholders:

- `tutorial/programs/eligibility_and_compliance/program_config_eligibility_manager.png`
- `tutorial/programs/eligibility_and_compliance/eligibility_manager_form.png`

## Eligibility criteria

In the manager form, the **Eligibility Criteria** section contains a CEL editor:

- it validates the expression
- it shows how many beneficiaries match
- it can preview the list of matching registrants

### Writing the expression

The expression is evaluated against:

- **Individuals**: profile `registry_individuals`
- **Groups/Households**: profile `registry_groups`

You can use:

- `me` or `r` for the current registrant (depends on configuration; newer screens prefer `me`)
- relations like `members`, `enrollments`, `entitlements` where available
- functions like `age_years()`
- Studio variables by accessor (when defined as `spp.cel.variable`)

Examples:

```text
age_years(me.birthdate) >= 60
```

```text
members.exists(head(m) and age_years(m.birthdate) >= 60)
```

```{note}
The embedded editor may show symbols for a default profile even when your program targets groups/households. If you are targeting groups and the symbol browser looks “wrong”, use **Advanced Builder** and switch **Target Type** to Groups/Households.
```

Screenshot placeholders:

- `tutorial/programs/eligibility_and_compliance/eligibility_cel_editor.png`
- `tutorial/programs/eligibility_and_compliance/eligibility_advanced_builder.png`
- `tutorial/programs/eligibility_and_compliance/eligibility_preview_beneficiaries.png`

### Geographic targeting (“Target Areas”)

The manager form also contains **Target Areas**.

Current behavior to be aware of:

- If your CEL expression is **empty**, OpenSPP can still apply the geographic targeting filter.
- If you enter a CEL expression, you should treat geographic targeting as part of the expression (or validate that your deployment combines them as you expect).

If you need to mix “Target Areas” with other rules, prefer expressing the full rule as CEL so it is explicit and testable.

## Compliance criteria

The same manager form includes **Compliance Criteria (CEL)**.

Compliance criteria are used at the **cycle** level to mark beneficiaries as compliant vs non-compliant.

### How it is used in cycles

On a cycle (typically in **Draft** or **To Approve**), OpenSPP can apply the configured compliance criteria via the **Compliance Criteria** button. Beneficiaries who do not satisfy the criteria are marked **non-compliant** for that cycle.

Screenshot placeholders:

- `tutorial/programs/eligibility_and_compliance/compliance_cel_editor.png`
- `tutorial/programs/eligibility_and_compliance/cycle_compliance_button.png`
- `tutorial/programs/eligibility_and_compliance/cycle_members_non_compliant.png`

## Related reading

- CEL basics: {doc}`../cel_quickstart`
- CEL patterns: {doc}`../cel_cookbook`
- CEL debugging: {doc}`../cel_troubleshooting`
- Technical reference: {doc}`../../technical_reference/cel/index`

