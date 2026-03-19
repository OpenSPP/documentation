---
openspp:
  doc_status: draft
  products: [core]
---

# CEL expressions for eligibility

This guide is for **implementers** writing CEL (Common Expression Language) expressions to define eligibility criteria.

## Understanding CEL

CEL is a simple expression language that lets you write eligibility rules without programming. It compiles to database queries for fast evaluation at scale.

**Example:** Select individuals aged 60 or older:

```cel
age_years(r.birthdate) >= 60
```

## Context variables

The context depends on your program's target type:

| Target type | Context variable | Description |
|-------------|------------------|-------------|
| Individual | `r` | The individual registrant |
| Group/Household | `r` | The group/household record |
| Group/Household | `members` | Collection of household members |

```{note}
Some expressions use `me` instead of `r`. Both refer to the current registrant. Check your CEL editor's symbol browser for available variables.
```

## Basic syntax

### Comparison operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | Equals | `r.gender_id == 'female'` |
| `!=` | Not equals | `r.status != 'inactive'` |
| `>=` | Greater than or equal | `age_years(r.birthdate) >= 18` |
| `<=` | Less than or equal | `age_years(r.birthdate) <= 65` |
| `>` | Greater than | `hh_size > 3` |
| `<` | Less than | `age_years(r.birthdate) < 5` |

### Logical operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `and` | Both must be true | `age >= 18 and age <= 65` |
| `or` | Either can be true | `age < 18 or age >= 65` |
| `not` | Negation | `not r.disabled` |

```{warning}
Use lowercase `and`/`or`, not `AND`/`OR`. CEL is case-sensitive for operators.
```

### Grouping with parentheses

Use parentheses to control evaluation order:

```cel
(age_years(r.birthdate) >= 60) or (r.disabled and age_years(r.birthdate) >= 50)
```

## Built-in functions

### Age calculation

| Function | Description | Example |
|----------|-------------|---------|
| `age_years(date)` | Calculate age in years from date | `age_years(r.birthdate) >= 65` |

### Gender helpers

| Function | Description | Example |
|----------|-------------|---------|
| `is_female(gender_field)` | Check if female | `is_female(r.gender_id)` |
| `is_male(gender_field)` | Check if male | `is_male(r.gender_id)` |

### Household role

| Function | Description | Example |
|----------|-------------|---------|
| `head(member)` | Check if member is household head | `head(m)` |

## Working with household members

For group/household programs, use collection functions to evaluate members:

### Check if any member matches

```cel
members.exists(m, age_years(m.birthdate) < 5)
```

This returns `true` if any member is under 5 years old.

### Count matching members

```cel
members.count(m, age_years(m.birthdate) < 18) >= 2
```

This returns `true` if there are 2 or more members under 18.

### Filter members

```cel
members.filter(m, is_female(m.gender_id) and age_years(m.birthdate) >= 18)
```

This returns a collection of adult female members.

### Collection function syntax

| Function | Syntax | Description |
|----------|--------|-------------|
| `exists` | `collection.exists(var, condition)` | True if any item matches |
| `count` | `collection.count(var, condition)` | Number of matching items |
| `filter` | `collection.filter(var, condition)` | Items that match |
| `all` | `collection.all(var, condition)` | True if all items match |

The `var` (typically `m` for member) is the iteration variable used in the condition.

## Household variables

For group/household programs, these pre-computed variables are available:

| Variable | Description | Example |
|----------|-------------|---------|
| `hh_size` | Number of household members | `hh_size >= 4` |

## Common patterns

### Age-based criteria

```cel
# Adults (18+)
age_years(r.birthdate) >= 18

# Working age (18-64)
age_years(r.birthdate) >= 18 and age_years(r.birthdate) <= 64

# Senior citizens (65+)
age_years(r.birthdate) >= 65

# Children under 5
age_years(r.birthdate) < 5
```

### Gender-based criteria

```cel
# Adult women
is_female(r.gender_id) and age_years(r.birthdate) >= 18

# Women of reproductive age (15-49)
is_female(r.gender_id) and age_years(r.birthdate) >= 15 and age_years(r.birthdate) <= 49
```

### Household composition

```cel
# Large households (4+ members)
hh_size >= 4

# Households with children under 5
members.count(m, age_years(m.birthdate) < 5) >= 1

# Households with school-age children (6-18)
members.count(m, age_years(m.birthdate) >= 6 and age_years(m.birthdate) <= 18) >= 1

# Female-headed households
members.exists(m, head(m) and is_female(m.gender_id))

# Elderly-headed households (60+)
members.exists(m, head(m) and age_years(m.birthdate) >= 60)
```

### Vulnerability indicators

```cel
# High dependency ratio (3+ dependents)
members.count(m, age_years(m.birthdate) < 18 or age_years(m.birthdate) >= 60) >= 3
```

### Combined criteria

```cel
# Elderly women in rural areas (requires area targeting)
is_female(r.gender_id) and age_years(r.birthdate) >= 60

# Large poor households with children
hh_size >= 5 and members.exists(m, age_years(m.birthdate) < 5)
```

## Using the CEL editor

The eligibility manager includes a CEL editor with:

```{figure} ../../_images/en-us/config_guide/eligibility/02-cel-editor-with-expression.png
:alt: CEL editor showing expression with validation

The CEL expression editor with syntax highlighting and live validation.
```

| Feature | Description |
|---------|-------------|
| **Syntax highlighting** | Color-coded expressions for readability |
| **Live validation** | Errors shown as you type |
| **Match count** | Shows how many registrants match |
| **Symbol browser** | Lists available variables and functions |

### Validation feedback

The editor shows real-time feedback:

| Indicator | Meaning |
|-----------|---------|
| Green checkmark | Expression is valid |
| Match count | Number of matching beneficiaries |
| Red error | Syntax error with description |

```{figure} ../../_images/en-us/config_guide/eligibility/03-cel-validation-success.png
:alt: CEL validation showing success with match count

A valid expression shows a green checkmark and the number of matching registrants.
```

### Symbol browser

Click the symbol browser to see all available:

- Variables (registrant fields)
- Functions (age_years, is_female, etc.)
- Collection operations (exists, count, filter)

```{figure} ../../_images/en-us/config_guide/eligibility/04-cel-symbol-browser.png
:alt: Symbol browser showing available functions

Click **Symbols** to browse available variables, functions, and collection operations.
```

## Advanced builder

For complex expressions, use the **Advanced Builder** button:

```{figure} ../../_images/en-us/config_guide/eligibility/05-advanced-builder-wizard.png
:alt: Advanced CEL builder wizard

The advanced builder provides a larger editing area with target type selection and template insertion.
```

The advanced builder provides:

- Larger editing area
- Target type selection (Individual/Group)
- Template insertion
- Full syntax reference

## Are you stuck?

**Expression shows "invalid syntax"?**
- Check for lowercase `and`/`or` (not `AND`/`OR`)
- Verify parentheses are balanced
- Use the symbol browser to check field names

**No registrants match?**
- Check the target type matches your program (Individual vs Group)
- Verify the field contains the expected data
- Start with a simpler expression and add conditions incrementally

**Age calculation seems wrong?**
- Ensure the birthdate field is not null
- Check the date format in your data

**Member functions not working?**
- Member functions (`members.exists`, `members.count`) only work for Group/Household programs
- For individual programs, access fields directly on `r`

## Next steps

- {doc}`templates` - Use pre-built expression templates
- {doc}`testing` - Validate your expressions before deployment
- {doc}`geographic_targeting` - Combine with area-based targeting
