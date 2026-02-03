---
openspp:
  doc_status: draft
  products: [core]
---

# Variable Types

This guide is for **implementers** who need to understand the different source types available for variables.

## Source Types Overview

| Source Type | Data Origin | Use Case |
|-------------|-------------|----------|
| Model Field | Odoo model field | Map existing fields to variables |
| Computed (CEL) | CEL expression | Calculate derived values |
| Member Aggregate | Household members | Count, sum, average over members |
| Constant/Parameter | Fixed value | Thresholds, configuration values |
| External Source | External API | Credit scores, external data |
| Vocabulary Concept | Concept group | Boolean from vocabulary membership |
| Scoring Result | PMT/scoring | Proxy means test scores |

## Model Field Variables

Reference an existing field on an Odoo model.

### When to Use

- Map a custom field to a simpler variable name
- Abstract field names from business logic
- Enable field renaming without breaking expressions

### Configuration

| Field | Value | Notes |
|-------|-------|-------|
| Source Type | Model Field | |
| Source Model | `res.partner` | The Odoo model name |
| Source Field | `x_custom_income` | The field name on the model |

### Example: Map Income Field

| Setting | Value |
|---------|-------|
| Name | `income` |
| Source Type | Model Field |
| Source Model | `res.partner` |
| Source Field | `x_studio_monthly_income` |
| Value Type | Money |

![Model Field source type configuration](/_images/en-us/config_guide/variables/05-source-type-field.png)

**CEL Usage:** `income > 5000`

### Field Status Indicator

The system shows whether the source field exists:

| Status | Meaning |
|--------|---------|
| Field Exists | Field found on model |
| Field Missing | Field not found (check spelling) |
| Unknown | Status not yet checked |
| Not Applicable | Not a field-based variable |

## Computed (CEL) Variables

Calculate values using CEL expressions.

### When to Use

- Derive values from other variables or fields
- Perform calculations (age from birthdate)
- Create conditional logic

### Configuration

| Field | Value | Notes |
|-------|-------|-------|
| Source Type | Computed (CEL) | |
| CEL Expression | `age_years(birthdate)` | The computation expression |

### Example: Calculate Age

| Setting | Value |
|---------|-------|
| Name | `age` |
| Source Type | Computed (CEL) |
| CEL Expression | `age_years(birthdate)` |
| Value Type | Number |
| Unit | years |

![Computed CEL source type configuration](/_images/en-us/config_guide/variables/08-source-type-computed.png)

**CEL Usage:** `age >= 18 && age <= 65`

### Example: Dependency Ratio

| Setting | Value |
|---------|-------|
| Name | `dependency_ratio` |
| Source Type | Computed (CEL) |
| CEL Expression | `(children_under_15 + elderly_over_65) / working_age_members` |
| Value Type | Number |

### Expression Guidelines

- Reference other variables by name: `income`, `hh_size`
- Use built-in functions: `age_years()`, `size()`, `sum()`
- Avoid circular references (A depends on B, B depends on A)

## Member Aggregate Variables

Compute values over household members, enrollments, entitlements, or events.

### When to Use

- Count members meeting criteria
- Sum values across members
- Check if any member matches condition

### Configuration

| Field | Value | Notes |
|-------|-------|-------|
| Source Type | Member Aggregate | |
| Aggregate Type | Count / Sum / Avg / Min / Max / Exists | |
| Aggregate Target | Household Members | What to aggregate over |
| Aggregate Filter | `age_years(m.birthdate) < 5` | Filter expression |
| Aggregate Field | `income` | For sum/avg/min/max only |

### Aggregate Types

| Type | Returns | Use For |
|------|---------|---------|
| **Count** | Number | How many members match |
| **Sum** | Number | Total of a field across members |
| **Average** | Number | Mean of a field across members |
| **Minimum** | Number | Smallest value |
| **Maximum** | Number | Largest value |
| **Exists** | Yes/No | True if any member matches |

![Aggregate types dropdown](/_images/en-us/config_guide/variables/07-aggregate-types-dropdown.png)

### Aggregate Targets

| Target | Aggregates Over |
|--------|-----------------|
| Household Members | Members of the household |
| Program Enrollments | Program membership records |
| Entitlements | Entitlement records |
| Events | Event data records |

### Example: Count Children

| Setting | Value |
|---------|-------|
| Name | `child_count` |
| Aggregate Type | Count |
| Aggregate Target | Household Members |
| Aggregate Filter | `age_years(m.birthdate) < 18` |
| Value Type | Number |

### Example: Total Member Income

| Setting | Value |
|---------|-------|
| Name | `total_member_income` |
| Aggregate Type | Sum |
| Aggregate Target | Household Members |
| Aggregate Field | `income` |
| Value Type | Money |

### Example: Has Elderly Member

| Setting | Value |
|---------|-------|
| Name | `has_elderly` |
| Aggregate Type | Exists |
| Aggregate Target | Household Members |
| Aggregate Filter | `age_years(m.birthdate) >= 65` |
| Value Type | Yes/No |

### Filter Expression Syntax

Use `m.` prefix for member fields:

```
# Age-based filters
age_years(m.birthdate) < 5        # Under 5
age_years(m.birthdate) >= 65      # 65 and older

# Field comparisons
m.gender == "female"              # Female members
m.is_disabled == true             # Disabled members

# Combined conditions
age_years(m.birthdate) < 18 && m.is_enrolled_in_school == true
```

## Event Aggregate Variables

Aggregate over event data with time filtering.

### Configuration

| Field | Value | Notes |
|-------|-------|-------|
| Source Type | Member Aggregate | |
| Aggregate Target | Events | |
| Event Type | (select event type) | Which event type |
| Time Range | This Year | Temporal filter |
| Event Field | `amount` | For sum/avg (JSON field in event) |

### Time Range Options

| Option | Description |
|--------|-------------|
| All Time | All events |
| This Year | Current calendar year |
| This Quarter | Current quarter |
| This Month | Current month |
| Within N Days | Last N days (specify N) |
| Within N Months | Last N months (specify N) |

### Example: Health Visits This Year

| Setting | Value |
|---------|-------|
| Name | `health_visits_year` |
| Aggregate Type | Count |
| Aggregate Target | Events |
| Event Type | Health Visit |
| Time Range | This Year |
| Value Type | Number |

### Example: Total Training Hours

| Setting | Value |
|---------|-------|
| Name | `training_hours` |
| Aggregate Type | Sum |
| Aggregate Target | Events |
| Event Type | Training Session |
| Time Range | All Time |
| Event Field | `duration_hours` |
| Value Type | Number |

## Constant/Parameter Variables

Fixed values that can optionally be overridden per program.

### When to Use

- Define thresholds (poverty line, age limits)
- Configuration values shared across expressions
- Values that programs can customize

### Configuration

| Field | Value | Notes |
|-------|-------|-------|
| Source Type | Constant/Parameter | |
| Default Value | `5000` | The base value |
| Program Configurable | Yes/No | Allow program overrides |

### Example: Poverty Line

| Setting | Value |
|---------|-------|
| Name | `poverty_line` |
| Source Type | Constant/Parameter |
| Default Value | `5000` |
| Program Configurable | Yes |
| Value Type | Money |
| Unit | USD |

![Constant source type configuration](/_images/en-us/config_guide/variables/09-source-type-constant.png)

**CEL Usage:** `income < poverty_line`

### Program Override

When **Program Configurable** is enabled:
1. Each program can set its own value
2. If not set, the default value is used
3. Allows same logic with different thresholds

## Vocabulary Concept Variables

Check membership in a vocabulary concept group.

### When to Use

- Boolean based on vocabulary code membership
- Check if value belongs to a concept group
- Abstract vocabulary logic

### Configuration

| Field | Value | Notes |
|-------|-------|-------|
| Source Type | Vocabulary Concept | |
| Source Concept Group | (select concept group) | The concept to check |

### Example: Is Female

| Setting | Value |
|---------|-------|
| Name | `is_female` |
| Source Type | Vocabulary Concept |
| Source Concept Group | Feminine Gender |
| Value Type | Yes/No |

**CEL Usage:** `is_female == true`

## External Source Variables

Fetch data from external providers.

### When to Use

- Credit scores from external bureau
- Data from government databases
- Third-party verification services

### Configuration

| Field | Value | Notes |
|-------|-------|-------|
| Source Type | External Source | |
| External Provider | (select provider) | Pre-configured data provider |

```{note}
External providers must be configured separately in **Settings → Data Providers**.
```

### Caching Recommendation

External sources should use caching to:
- Reduce API calls
- Handle rate limits
- Improve performance

| Setting | Recommended |
|---------|-------------|
| Cache Strategy | TTL-based |
| Cache TTL | 3600+ seconds |

## Scoring Result Variables

Output from PMT (Proxy Means Test) or scoring calculations.

### When to Use

- PMT scores for targeting
- Composite vulnerability indices
- Weighted scoring results

### Configuration

Scoring variables are typically created by the scoring module automatically.

## Are You Stuck?

**Which source type should I use?**

| If you need... | Use |
|----------------|-----|
| Existing field value | Model Field |
| Calculated value | Computed (CEL) |
| Count/sum over members | Member Aggregate |
| Fixed threshold | Constant/Parameter |
| External lookup | External Source |

**Aggregate filter not matching?**

- Use `m.` prefix for member fields
- Check field exists on member model
- Verify filter syntax in CEL builder first

**Computed expression causing errors?**

- Avoid circular references
- Check referenced variables exist and are active
- Test expression in CEL builder

## Next Steps

| To... | See... |
|-------|--------|
| Create a new variable | {doc}`creating_variables` |
| Use variables in expressions | {doc}`using_variables` |
| Understand caching | {doc}`overview` |
