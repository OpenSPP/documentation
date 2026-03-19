---
openspp:
  doc_status: draft
  products: [core]
---

# Using Variables in CEL

This guide is for **implementers** who need to use variables in CEL expressions for eligibility rules, targeting, and program logic.

## Referencing Variables

Variables are referenced by their **name** (CEL Accessor) in expressions.

### Basic Reference

```
income                    # Variable value
age                       # Variable value
has_disability            # Boolean variable
```

### In Comparisons

```
income > 5000             # Numeric comparison
age >= 18 && age <= 65    # Range check
has_disability == true    # Boolean check
```

### In Conditions

```
# If-else logic
income < poverty_line ? "eligible" : "not_eligible"

# Multiple conditions
income < poverty_line && child_count >= 2
```

## Variable Autocomplete

When using the CEL Expression Builder (**Studio → Expressions**):

1. Start typing a variable name
2. Autocomplete shows matching variables
3. Select to insert the variable
4. Hover for description and type info

Only **Active** variables appear in autocomplete.

## Type Compatibility

Match variable types with appropriate operators:

| Variable Type | Valid Operations |
|---------------|------------------|
| Number | `>`, `<`, `>=`, `<=`, `==`, `!=`, `+`, `-`, `*`, `/` |
| Money | Same as Number |
| Yes/No | `==`, `!=`, `&&`, `\|\|`, `!` |
| Text | `==`, `!=`, `contains()`, `startsWith()` |
| Date | `==`, `!=`, `>`, `<`, `before()`, `after()` |
| List | `in`, `size()`, `contains()` |

## Common Patterns

### Eligibility Check

```
# Basic income eligibility
income < poverty_line

# With household size consideration
income_per_capita < poverty_line

# Multiple criteria
income < poverty_line &&
child_count >= 1 &&
has_disabled_member == true
```

### Age-Based Targeting

```
# Working age
age >= 18 && age <= 65

# Children
age < 18

# Elderly
age >= 65

# Specific range
age >= 6 && age <= 14    # School age
```

### Household Composition

```
# Has children
child_count >= 1

# Large household
hh_size >= 5

# Single parent with children
is_single_parent == true && child_count >= 1

# Dependency ratio threshold
dependency_ratio > 0.5
```

### Vulnerability Scoring

```
# Combined score
pmt_score < threshold &&
(has_disabled_member == true || has_elderly == true)

# Weighted criteria
vulnerability_score >= 3

# Category-based
vulnerability_category == "extremely_poor"
```

### Program-Specific

```
# Already enrolled in another program
is_enrolled_in_4ps == false

# Recent beneficiary
months_since_last_benefit > 6

# Graduation criteria
consecutive_months_above_poverty >= 12
```

## Using Constants

Reference program-configurable constants:

```
# Poverty line (program can override)
income < poverty_line

# Age thresholds
age >= min_age && age <= max_age

# Benefit calculation
benefit_amount = base_benefit * household_multiplier
```

## Using Aggregates

Aggregate variables compute automatically:

```
# Child count (computed over members)
children_under_5 >= 1

# Has condition (exists aggregate)
has_pregnant_member == true

# Total value (sum aggregate)
total_household_income < threshold
```

## Period-Aware Variables

For variables with period granularity:

```
# Current value (default)
income > 5000

# Historical (if supported)
income_at_enrollment < poverty_line_at_enrollment
```

```{note}
Historical queries require the variable to have **Supports Historical** enabled.
```

## Combining Variables

### AND Logic

```
# All conditions must be true
income < poverty_line &&
age >= 18 &&
has_valid_id == true
```

### OR Logic

```
# Any condition can be true
has_disabled_member == true ||
has_elderly == true ||
has_pregnant == true
```

### Mixed Logic

```
# Use parentheses for clarity
(income < poverty_line || is_food_insecure == true) &&
has_children == true
```

## Null Handling

Variables may not have values for all registrants:

```
# Safe null check
income != null && income < poverty_line

# Default if null
(income ?? 0) < poverty_line

# Exists check
has(disability_status) && disability_status == "severe"
```

## Expression Examples by Use Case

### Cash Transfer Eligibility

```
# Pantawid Pamilya (4Ps style)
income_per_capita < poverty_line &&
child_count >= 1 &&
(has_child_under_18 == true || has_pregnant == true) &&
is_not_government_employee == true
```

### Emergency Assistance

```
# Disaster response
affected_by_disaster == true &&
damage_level >= 2 &&
income < 2 * poverty_line
```

### Scholarship Program

```
# Education support
age >= 16 && age <= 25 &&
is_enrolled_in_school == true &&
family_income < education_threshold &&
gpa >= minimum_gpa
```

### Livelihood Program

```
# Economic inclusion
age >= 18 && age <= 59 &&
is_unemployed == true &&
has_completed_training == false &&
months_in_poverty >= 6
```

### Senior Citizen Support

```
# Elderly assistance
age >= 65 &&
income < senior_poverty_line &&
is_receiving_pension == false
```

## Debugging Variables

### Check Variable Values

In the CEL Builder, you can test expressions with sample data:

1. Go to **Studio → Expressions**
2. Enter your expression
3. Select a test registrant
4. Click **Evaluate**
5. View variable values and result

### Common Issues

| Symptom | Likely Cause | Solution |
|---------|--------------|----------|
| Variable not found | Not active | Activate the variable |
| Returns null | No data for registrant | Add null check |
| Wrong value | Stale cache | Check cache settings |
| Type error | Wrong comparison | Match types correctly |

## Performance Tips

### Use Cached Variables

For frequently-used variables in batch operations:

| Scenario | Recommended Cache |
|----------|-------------------|
| Eligibility batch | Session cache |
| Daily reports | TTL (1 hour) |
| Real-time UI | No cache or short TTL |

### Minimize Aggregates

Aggregates are computed per evaluation. For better performance:

- Cache aggregate results
- Use simpler filters
- Avoid nested aggregates

### Keep Expressions Simple

```
# Good: Simple, readable
income < poverty_line && child_count >= 1

# Avoid: Complex nested logic
((income < poverty_line || (income < 1.5 * poverty_line &&
has_disabled_member == true)) && child_count >= 1) ||
(is_indigenous == true && income < 2 * poverty_line)
```

Break complex logic into multiple variables or eligibility rules.

## Are You Stuck?

**Variable shows as undefined?**

- Check variable is Active
- Verify the name spelling
- Ensure applies_to matches context (Individual vs Group)

**Expression returns unexpected results?**

- Test with specific registrant in CEL Builder
- Check null values
- Verify variable cache is current

**Type mismatch error?**

- Check value type of variable
- Use appropriate operators for type
- Convert types if needed: `int(string_var)`

**Aggregate seems wrong?**

- Verify filter expression
- Check aggregate target (members vs events)
- Test filter separately first

## Next Steps

| To... | See... |
|-------|--------|
| Create new variables | {doc}`creating_variables` |
| Understand source types | {doc}`variable_types` |
| Learn CEL basics | {doc}`/config_guide/cel/index` |
| Build eligibility rules | {doc}`/config_guide/cel/cookbook` |
