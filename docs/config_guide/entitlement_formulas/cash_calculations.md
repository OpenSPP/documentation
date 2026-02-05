---
openspp:
  doc_status: draft
  products: [core]
---

# Cash calculations

This guide is for **implementers** configuring cash entitlement calculations including fixed amounts, multipliers, and maximum caps.

## Understanding cash entitlements

Cash entitlements are monetary payments calculated for each beneficiary. The calculation can be:

- **Fixed amount** - Same amount for all beneficiaries
- **Multiplied amount** - Amount multiplied by a beneficiary field
- **Formula-based** - Complex calculation using CEL expressions
- **Capped amount** - Maximum limit on total entitlement

## Cash entitlement manager configuration

### Accessing the configuration

1. Open your program's **Configuration** tab
2. Find the **Entitlement Manager** section
3. Click the gear icon on the cash entitlement manager

```{figure} /_images/en-us/config_guide/entitlement_formulas/02-cash-entitlement-manager-form.png
:alt: Cash entitlement manager configuration form

The Cash entitlement manager form showing **Evaluate one item**, **Maximum Amount**, and the **Entitlement Items** list.
```

### Manager-level settings

| Field | Description |
|-------|-------------|
| **Name** | Display name for this manager |
| **Maximum Amount** | Cap on total entitlement (0 = no cap) |
| **Entitlement Validation Group** | User group that can approve entitlements |
| **Entitlement Items** | List of calculation rules |

## Entitlement items

Each cash entitlement manager has one or more **items**. Items are evaluated in order, and amounts are summed.

### Adding an entitlement item

1. In the entitlement manager form, click **Add a line** in the Entitlement Items section
2. Configure the item fields
3. Save the configuration

```{figure} /_images/en-us/config_guide/entitlement_formulas/03-entitlement-item-form.png
:alt: Entitlement item configuration form

The entitlement item form with **Amount**, **Condition Domain**, **Multiplier**, and **Maximum number** fields.
```

### Item configuration fields

| Field | Description | Example |
|-------|-------------|---------|
| **Amount** | Base amount for this item | `500` |
| **Currency** | Payment currency | USD, PHP |
| **Multiplier Field** | Beneficiary field to multiply by | `household_size` |
| **Max Multiplier** | Maximum multiplier value (0 = no max) | `10` |
| **Condition** | CEL expression for who gets this item | `age_years(r.birthdate) >= 60` |
| **Formula** | CEL expression for complex calculation | `base_amount * 1.1` |

## Fixed amount configuration

For a simple fixed amount for all beneficiaries:

| Field | Value |
|-------|-------|
| Amount | `500` |
| Multiplier Field | (empty) |
| Condition | (empty) |

**Result:** Every beneficiary receives $500.

## Multiplier configuration

To scale the amount by a beneficiary field:

| Field | Value |
|-------|-------|
| Amount | `100` |
| Multiplier Field | `z_ind_grp_num_individuals` |
| Max Multiplier | `10` |

**Result:** $100 per household member, maximum 10 members = $1,000 max.

### Common multiplier fields

| Field | Description |
|-------|-------------|
| `z_ind_grp_num_individuals` | Total household members |
| `z_ind_grp_num_children` | Number of children |
| `z_ind_grp_num_adults` | Number of adults |
| `z_ind_grp_num_elderly` | Number of elderly members |

```{note}
Field names depend on your registry configuration. Check your registrant model for available fields.
```

## Maximum amount cap

To limit the total entitlement regardless of multipliers:

1. Set **Maximum Amount** at the manager level
2. This caps the sum of all entitlement items

| Configuration | Value |
|---------------|-------|
| Item 1 Amount | `100` |
| Multiplier | `household_size` |
| Maximum Amount (manager) | `800` |

**Example:** Household of 12 members
- Calculated: 12 × $100 = $1,200
- Capped at: $800

## Multiple entitlement items

Combine multiple items for complex calculations:

### Example: Base + per-child supplement

**Item 1: Base amount**

| Field | Value |
|-------|-------|
| Amount | `300` |
| Condition | (empty - all beneficiaries) |

**Item 2: Child supplement**

| Field | Value |
|-------|-------|
| Amount | `50` |
| Multiplier Field | `z_ind_grp_num_children_under_5` |
| Max Multiplier | `5` |

**Result for household with 3 children under 5:**
- Base: $300
- Children: 3 × $50 = $150
- Total: $450

```{figure} /_images/en-us/config_guide/entitlement_formulas/04-multiple-entitlement-items.png
:alt: Multiple entitlement items configured in the Cash manager

Multiple entitlement items configured with different amounts, multipliers, and conditions for complex calculations.
```

## Formula-based calculations

For complex calculations, use CEL formulas instead of simple multipliers.

### Formula context

In amount formulas, you can reference:

| Variable | Description |
|----------|-------------|
| `base_amount` | The Amount field value for this item |
| `me` | The beneficiary record |

### Simple formula examples

```cel
# Fixed amount (same as leaving formula empty)
500

# Percentage increase
base_amount * 1.1

# Conditional adjustment
base_amount * 1.5 if me.is_female_headed else base_amount
```

### Using beneficiary fields

```cel
# Based on household size
base_amount * me.household_size

# With cap logic
min(base_amount * me.household_size, 1000)

# Conditional based on attribute
base_amount + (100 if me.has_disability else 0)
```

## Formula validation

When you enter a formula, OpenSPP validates it:

| Indicator | Meaning |
|-----------|---------|
| No error | Formula syntax is valid |
| Error message | Syntax error or invalid field |
| Sample calculation | Shows result for a sample beneficiary |

## Built-in functions

Available in amount formulas:

| Function | Description | Example |
|----------|-------------|---------|
| `age_years(date)` | Calculate age from date | `age_years(me.birthdate)` |
| `min(a, b, ...)` | Minimum value | `min(amount, 1000)` |
| `max(a, b, ...)` | Maximum value | `max(amount, 100)` |
| `abs(n)` | Absolute value | `abs(difference)` |
| `has(obj, field)` | Check if field exists | `has(me, 'disability_type')` |

## Calculation order

When preparing entitlements:

1. Each entitlement item is evaluated in order
2. Conditions are checked first
3. If condition passes, amount is calculated
4. Multiplier is applied (if configured)
5. Max multiplier caps the multiplier value
6. All item amounts are summed
7. Manager's maximum amount caps the total

```{mermaid}
graph TD
    I[Entitlement Item] --> C{Condition?}
    C --> |Pass| A[Calculate Amount]
    C --> |Fail| S[Skip Item]
    A --> M{Multiplier?}
    M --> |Yes| MV[Apply Multiplier]
    M --> |No| SUM
    MV --> CAP{Max Multiplier?}
    CAP --> |Yes| MC[Cap Multiplier]
    CAP --> |No| SUM
    MC --> SUM[Add to Total]
    SUM --> NEXT[Next Item]
    NEXT --> MAX{Max Amount?}
    MAX --> |Yes| FINAL[Cap Total]
    MAX --> |No| DONE[Final Amount]
    FINAL --> DONE
```

## Best practices

### Keep it simple

| Do | Don't |
|----|-------|
| Use multiplier fields for scaling | Write complex formulas for simple scaling |
| Use manager max amount for caps | Implement cap logic in every formula |
| Test with sample data first | Deploy without testing |

### Document your configuration

| Practice | Benefit |
|----------|---------|
| Name items descriptively | "Base + Child Supplement" |
| Add notes explaining logic | Future maintainability |
| Record policy rationale | Audit trail |

### Performance considerations

| Tip | Reason |
|-----|--------|
| Avoid complex formulas | Faster calculation |
| Use indexed fields for conditions | Faster filtering |
| Test with production data volumes | Verify performance |

## Are you stuck?

**Amount is always 0?**
- Check the Amount field has a value
- Verify the condition isn't excluding all beneficiaries
- Ensure multiplier field exists and has data

**Multiplier not working?**
- Verify the field name is correct
- Check the field has numeric values
- Look for typos in field name

**Formula error?**
- Check syntax (use `base_amount` not `amount`)
- Verify field names match your model
- Use the symbol browser for available fields

**Total exceeds expected?**
- Check Max Amount is set at manager level
- Verify Max Multiplier on items
- Review all items - amounts are summed

## Next steps

- {doc}`formula_library` - Pre-built formulas for common scenarios
- {doc}`dynamic_entitlements` - Household-based calculations
- {doc}`conditional_logic` - Different amounts for different groups
