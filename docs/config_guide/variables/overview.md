---
openspp:
  doc_status: draft
  products: [core]
---

# Variables Overview

This guide is for **implementers** configuring OpenSPP's variable system. You should be comfortable with CEL expressions but don't need to write code.

## What Are Variables?

Variables are named data points you can reference in CEL expressions. They provide a layer of abstraction between your business logic and the underlying data.

**Example:** Instead of writing `registrant.custom_field_income`, you reference `income` in your expressions.

| Without Variables | With Variables |
|-------------------|----------------|
| `registrant.x_custom_income > 5000` | `income > 5000` |
| Breaks if field renamed | Variable handles the mapping |
| No caching | Built-in caching support |
| No historical tracking | Period granularity options |

## Mental Model

Think of variables in three layers:

```
┌───────────────────────────────────────────────────────┐
│  1. SOURCE                                            │
│     Where data comes from:                            │
│     • Model field (res.partner.income)                │
│     • Computed CEL expression                         │
│     • Aggregate over members                          │
│     • External API                                    │
└───────────────────────────────────────────────────────┘
                         │
                         │ processed by
                         ▼
┌───────────────────────────────────────────────────────┐
│  2. VARIABLE                                          │
│     Configuration:                                    │
│     • Name: income                                    │
│     • Label: Household Income                         │
│     • Value Type: Money                               │
│     • Cache: TTL 1 hour                               │
└───────────────────────────────────────────────────────┘
                         │
                         │ referenced in
                         ▼
┌───────────────────────────────────────────────────────┐
│  3. CEL EXPRESSION                                    │
│     Usage:                                            │
│     income > poverty_line                             │
│     child_count >= 3                                  │
│     has_disability == true                            │
└───────────────────────────────────────────────────────┘
```

## Source Types

Variables can get their data from different sources:

| Source Type | Description | Example |
|-------------|-------------|---------|
| **Model Field** | Direct reference to a field on a model | `res.partner.income` → `income` |
| **Computed (CEL)** | Calculated from a CEL expression | `age_years(birthdate)` → `age` |
| **Aggregate** | Computed over household members | Count children under 5 → `child_under_5_count` |
| **External** | Fetched from external data provider | API lookup → `credit_score` |
| **Constant** | Fixed value, optionally program-configurable | Poverty line → `poverty_threshold` |
| **Vocabulary** | Value from a vocabulary concept group | Gender concept → `is_female` |
| **Scoring** | Result from a scoring/PMT calculation | PMT score → `pmt_score` |

## Value Types

Each variable has a value type that determines how it's used:

| Value Type | CEL Type | Example |
|------------|----------|---------|
| **Number** | double/int | `income`, `age`, `score` |
| **Yes/No** | bool | `is_disabled`, `has_id` |
| **Text** | string | `occupation`, `notes` |
| **Date** | timestamp | `enrollment_date` |
| **Money** | double | `benefit_amount` |
| **List** | list | `id_types`, `programs` |

## Applies To

Variables are scoped to specific registrant types:

| Scope | Use For |
|-------|---------|
| **Individual** | Person-level data (age, gender, disability) |
| **Group/Household** | Household-level data (size, income, location) |
| **Both** | Works for either context |

## Caching

Variables support different caching strategies for performance:

| Strategy | When Cached | Use Case |
|----------|-------------|----------|
| **No Caching** | Never | Frequently changing data, small datasets |
| **Session** | Per request/batch | Eligibility batch processing |
| **TTL-based** | For specified duration | Stable data, API rate limits |
| **Manual** | On explicit trigger | Data refreshed on schedule |

**TTL Example:**
```
Cache Strategy: TTL-based
Cache TTL: 3600 seconds (1 hour)
```

The variable value is computed once and reused for 1 hour before refreshing.

```{figure} /_images/en-us/config_guide/variables/10-caching-configuration.png
:alt: Variable form with Cache Strategy and TTL fields highlighted

Set the **Cache Strategy** and **Cache TTL** to control how long computed values are reused.
```

## Period Granularity

Variables can track values over time:

| Granularity | Description | Example |
|-------------|-------------|---------|
| **Current** | Always latest value | Current income |
| **Daily** | Value per day | Daily attendance |
| **Monthly** | Value per month | Monthly earnings |
| **Quarterly** | Value per quarter | Quarterly assessment score |
| **Yearly** | Value per year | Annual income |
| **Snapshot** | Point-in-time freeze | Income at enrollment |

```{figure} /_images/en-us/config_guide/variables/11-period-granularity.png
:alt: Variable form with Period Granularity field highlighted

Choose the **Period Granularity** to track variable values over time.
```

**Snapshot Example:** Capture household income at the moment of program enrollment, even if it changes later.

## Categories

Variables are organized into categories for easier management:

| Category | Typical Variables |
|----------|-------------------|
| Demographics | age, gender, marital_status |
| Household | hh_size, child_count, dependency_ratio |
| Economic | income, assets, employment_status |
| Health | disability_status, chronic_illness |
| Program | enrollment_date, benefit_amount |

## Variable Lifecycle

```
Draft → Active → Inactive
  ↑        │
  │        │ (can reactivate)
  └────────┘
```

| State | Description |
|-------|-------------|
| **Draft** | Being configured, not usable in expressions |
| **Active** | Available for use in CEL expressions |
| **Inactive** | Hidden from variable picker, existing references still work |

## Common Patterns

### Pattern 1: Field Reference

Map a model field to a simpler variable name.

| Setting | Value |
|---------|-------|
| Source Type | Model Field |
| Source Model | res.partner |
| Source Field | x_custom_income |
| Name | income |
| Label | Household Income |
| Value Type | Money |

**CEL Usage:** `income > 5000`

### Pattern 2: Age Calculation

Compute age from birthdate.

| Setting | Value |
|---------|-------|
| Source Type | Computed (CEL) |
| CEL Expression | `age_years(birthdate)` |
| Name | age |
| Label | Age in Years |
| Value Type | Number |

**CEL Usage:** `age >= 18 && age <= 65`

### Pattern 3: Household Member Count

Count members meeting criteria.

| Setting | Value |
|---------|-------|
| Source Type | Member Aggregate |
| Aggregate Type | Count |
| Aggregate Target | Household Members |
| Aggregate Filter | `age_years(m.birthdate) < 5` |
| Name | children_under_5 |

**CEL Usage:** `children_under_5 >= 1`

### Pattern 4: Program Constant

Define a threshold that programs can override.

| Setting | Value |
|---------|-------|
| Source Type | Constant/Parameter |
| Default Value | 5000 |
| Program Configurable | Yes |
| Name | poverty_line |
| Label | Poverty Line Threshold |

**CEL Usage:** `income < poverty_line`

## Navigation

Variables are configured in **Studio → Variables**.

```{figure} /_images/en-us/config_guide/variables/01-studio-variables-card.png
:alt: Studio Dashboard with the Variables card highlighted

Click **Open Variables** on the Studio Dashboard to manage variable definitions.
```

| Menu | Purpose |
|------|---------|
| **All Variables** | View, create, and manage variables |
| **Categories** | Create and organize variable categories |

```{figure} /_images/en-us/config_guide/variables/02-variables-list.png
:alt: Variables list view showing configured variables

The **Variables** list displays all defined variables with their status and source type.
```

## Are You Stuck?

**Variable not appearing in CEL autocomplete?**

Check that the variable state is "Active". Draft variables don't appear in the picker.

**Getting stale cached values?**

For TTL-based caching, wait for the TTL to expire or switch to "No Caching" for testing. For manual cache, trigger a refresh.

**Aggregate returning wrong count?**

Check the aggregate filter expression. Use `m.` prefix for member fields (e.g., `m.birthdate`, `m.gender`).

**What's the difference between Source Type and Value Type?**

Source Type is *where* the data comes from (field, computed, aggregate). Value Type is *what kind* of data it is (number, text, date).

## Next Steps

| To... | See... |
|-------|--------|
| Create a new variable | {doc}`creating_variables` |
| Understand different source types | {doc}`variable_types` |
| Use variables in expressions | {doc}`using_variables` |
| Learn CEL basics | {doc}`/config_guide/cel/index` |
