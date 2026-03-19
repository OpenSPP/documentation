---
openspp:
  doc_status: draft
  products: [core]
---

# Formula library

This guide is for **implementers** using pre-built formulas and common patterns for entitlement calculations.

## Common formula patterns

This library provides copy-paste formulas for typical social protection scenarios.

## Fixed amounts

### Simple fixed amount

Every beneficiary receives the same amount.

| Field | Value |
|-------|-------|
| Amount | `500` |
| Formula | (leave empty) |

**Result:** $500 per beneficiary

### Fixed amount with formula

Using a formula for documentation clarity:

```cel
500
```

## Per-member calculations

### Per household member

Amount scales with household size.

| Field | Value |
|-------|-------|
| Amount | `100` |
| Multiplier Field | `z_ind_grp_num_individuals` |

**Or using formula:**

```cel
100 * me.z_ind_grp_num_individuals
```

**Example:** 5-member household = $500

### Per adult member

```cel
base_amount * me.z_ind_grp_num_adults
```

### Per child

```cel
base_amount * me.z_ind_grp_num_children
```

### Per elderly member

```cel
base_amount * me.z_ind_grp_num_elderly
```

## Capped calculations

### Maximum amount cap

Limit total regardless of household size:

```cel
min(base_amount * me.household_size, 1000)
```

**Example:**
- 8-member household × $150 = $1,200
- Capped to $1,000

### Minimum guarantee

Ensure a minimum amount:

```cel
max(base_amount * me.household_size, 200)
```

**Example:**
- 1-member household × $50 = $50
- Raised to minimum $200

### Bounded range

Both minimum and maximum:

```cel
max(min(base_amount * me.household_size, 1000), 200)
```

## Tiered calculations

### Household size tiers

Different rates for different sizes:

```cel
# Small (1-3): $300, Medium (4-6): $500, Large (7+): $700
me.household_size <= 3 ? 300 :
  me.household_size <= 6 ? 500 : 700
```

### Age-based tiers

```cel
# Under 18: $200, 18-59: $300, 60+: $400
age_years(me.birthdate) < 18 ? 200 :
  age_years(me.birthdate) < 60 ? 300 : 400
```

## Percentage adjustments

### Percentage increase

10% increase on base amount:

```cel
base_amount * 1.10
```

### Percentage decrease

20% reduction:

```cel
base_amount * 0.80
```

### Conditional percentage

```cel
# 50% increase for female-headed households
me.is_female_headed ? base_amount * 1.5 : base_amount
```

## Supplement patterns

### Base plus supplement

Base amount plus additional for specific criteria:

```cel
# Base $300 + $100 for disability
base_amount + (me.has_disability ? 100 : 0)
```

### Multiple supplements

```cel
# Base + elderly bonus + disability bonus
base_amount +
  (me.has_elderly_member ? 50 : 0) +
  (me.has_disabled_member ? 75 : 0)
```

### Per-category supplements

```cel
# $50 per child under 5 + $30 per school-age child
(me.children_under_5 * 50) + (me.school_age_children * 30)
```

## Conditional amounts

### Gender-based

```cel
# Different amount for female vs male headed
me.is_female_headed ? 550 : 500
```

### Location-based

```cel
# Urban vs rural rates
me.is_urban ? 600 : 450
```

### Program-specific attribute

```cel
# Based on PMT score category
me.pmt_category == 'extreme_poor' ? 600 :
  me.pmt_category == 'poor' ? 450 : 300
```

## Household composition formulas

### Base + per child under 5

```cel
300 + (me.children_under_5 * 50)
```

### Dependency ratio adjustment

```cel
# Higher amount for more dependents
base_amount * (1 + (me.dependency_ratio * 0.1))
```

### Complex household formula

```cel
# Base $200 + $50/child + $30/elderly + $100 if female-headed
200 +
  (me.num_children * 50) +
  (me.num_elderly * 30) +
  (me.is_female_headed ? 100 : 0)
```

## Seasonal/temporal formulas

### Lean season adjustment

```cel
# 20% increase during lean season (typically set via program config)
base_amount * (me.is_lean_season ? 1.2 : 1.0)
```

### First-time bonus

```cel
# Extra amount for first enrollment
base_amount + (me.is_first_enrollment ? 200 : 0)
```

## Currency and rounding

### Round to nearest 10

```cel
# Round $347 to $350
round(base_amount / 10) * 10
```

### Round down

```cel
floor(base_amount * me.household_size)
```

### Round up

```cel
ceil(base_amount * me.household_size / 100) * 100
```

## Null-safe patterns

### Handle missing data

```cel
# Default to 1 if household_size is missing
base_amount * (has(me, 'household_size') ? me.household_size : 1)
```

### Conditional with null check

```cel
# Only apply bonus if field exists and is true
base_amount + (has(me, 'is_vulnerable') && me.is_vulnerable ? 100 : 0)
```

## Complex real-world examples

### Cash transfer with multiple components

**Program:** Monthly cash transfer
- Base: $200
- Per child under 5: $40 (max 3 children)
- School attendance bonus: $30 per enrolled child
- Female-headed supplement: $50

```cel
200 +
  (min(me.children_under_5, 3) * 40) +
  (me.children_in_school * 30) +
  (me.is_female_headed ? 50 : 0)
```

### Emergency response calculation

**Program:** Disaster relief
- Base: $300
- Per affected household member: $50
- Special needs supplement: $100
- Maximum: $800

```cel
min(
  300 + (me.affected_members * 50) + (me.has_special_needs ? 100 : 0),
  800
)
```

### Agricultural support

**Program:** Farmer assistance
- Small farm (< 2 ha): $200
- Medium farm (2-5 ha): $350
- Large farm (> 5 ha): $500
- Crop loss supplement: +50%

```cel
(me.farm_size < 2 ? 200 : me.farm_size <= 5 ? 350 : 500) *
  (me.has_crop_loss ? 1.5 : 1.0)
```

## Formula testing

### Before deploying

1. Test with sample beneficiaries
2. Verify edge cases (0 children, max household size)
3. Check null handling
4. Confirm rounding behavior

### Test cases to consider

| Scenario | Expected behavior |
|----------|-------------------|
| Empty household_size | Should use default or skip |
| Maximum values | Should hit cap correctly |
| Minimum values | Should meet minimum guarantee |
| All conditions true | Should sum correctly |
| No conditions true | Should return base only |

## Are you stuck?

**Formula returns wrong amount?**
- Check operator precedence (use parentheses)
- Verify field names match exactly
- Test each component separately

**Null/missing data errors?**
- Use `has()` to check field existence
- Provide default values with ternary operators

**Rounding issues?**
- Use explicit `round()`, `floor()`, or `ceil()`
- Test with edge case amounts

## Next steps

- {doc}`cash_calculations` - Detailed configuration steps
- {doc}`dynamic_entitlements` - Household-based patterns
- {doc}`conditional_logic` - Complex conditional scenarios
