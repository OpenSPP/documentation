---
openspp:
  doc_status: unverified
  products: [core]
---

# Entitlement amount formulas (CEL)

Cash entitlement managers can calculate amounts using CEL formulas instead of a fixed multiplier/indicator setup.

This is designed for implementers who want formulas like:

- fixed amount (e.g., `500`)
- per-household-size (if your beneficiary record has `household_size`)
- conditional adjustments based on beneficiary attributes

## Where to configure

1. Go to **Programs → Programs** and open your program.
2. Open the **Configuration** tab.
3. In **Entitlement Manager**, click the **gear** icon on your cash entitlement manager.
4. In the **Entitlement Items** list, add or edit an item and fill the **Formula**.

Screenshot placeholders:

- `tutorial/programs/entitlement_amount_formulas/program_config_entitlement_manager.png`
- `tutorial/programs/entitlement_amount_formulas/cash_entitlement_items_list.png`
- `tutorial/programs/entitlement_amount_formulas/cash_entitlement_item_form.png`

## The runtime context (what you can reference)

Amount formulas are evaluated at runtime (they are not compiled to a domain). The evaluation context includes:

- `me`: the beneficiary record (safe field access; no ORM writes)
- `base_amount`: the “Amount” column value for the item

Examples:

```text
500
```

```text
base_amount * 1.1
```

```text
base_amount if me.is_woman_headed else base_amount * 0.8
```

```{note}
Unlike eligibility rules, amount formulas do not run in a profile with `members/enrollments/entitlements` relations. If you need a household aggregate, you typically need that value available as a field on the beneficiary record.
```

## Built-in functions you can use

In amount formulas you can use common helpers and safe built-ins, such as:

- `age_years(date)`
- `has(value_or_obj, field_name?)`
- `min(...)`, `max(...)`, `abs(...)`, `sum(...)`

## Preview and validation

When you edit a formula, OpenSPP computes a preview:

- If the program has at least one enrolled beneficiary, it shows a **sample calculation**.
- Otherwise, it performs a syntax check.

Screenshot placeholders:

- `tutorial/programs/entitlement_amount_formulas/formula_preview_ok.png`
- `tutorial/programs/entitlement_amount_formulas/formula_error.png`

## Operational notes

- Formulas are evaluated during entitlement preparation. If a formula fails for a beneficiary, that beneficiary may be skipped for that item (so test formulas before running large batches).
- Keep formulas simple and reusable. If your formula becomes complex, consider creating the needed derived data as registry fields first (and then referencing those fields through `me.<field>`).

## Related reading

- CEL basics: {doc}`../cel_quickstart`
- CEL patterns: {doc}`../cel_cookbook`
- Technical reference (modes): {doc}`../../technical_reference/cel/usage_by_feature`

