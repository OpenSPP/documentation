---
openspp:
  doc_status: draft
  products: [core]
---

# CEL Cookbook

This guide is for **implementers** who need ready-to-use CEL patterns.

Copy, paste, and adapt these patterns for your use case.

```{note}
Which symbols are available depends on the screen and profile. Use the editor's symbol browser to confirm what exists in your context.
```

## Basic Patterns

### Boolean Logic

```cel
me.is_registrant == true and me.active == true
```

Equivalent with operators:
```cel
me.is_registrant && me.active
```

### Handle Missing Values

Always check existence before accessing optional fields:

```cel
has(me.birthdate) and age_years(me.birthdate) >= 18
```

### Ternary (If/Else)

```cel
me.is_group ? 1 : 0
```

More complex:
```cel
me.income < 5000 ? "low" : (me.income < 15000 ? "medium" : "high")
```

### String Comparisons

```cel
me.status == "active"
me.region != "excluded_region"
```

## Household Composition

### Any Child Under 5

```cel
members.exists(m, age_years(m.birthdate) < 5)
```

Or newer syntax:
```cel
members.exists(age_years(m.birthdate) < 5)
```

### Count Children Under 18

```cel
members.count(m, age_years(m.birthdate) < 18)
```

### Count Children in Age Range

Children aged 6-12:
```cel
members.count(m, age_years(m.birthdate) >= 6 and age_years(m.birthdate) <= 12)
```

### Female Head of Household

```cel
members.exists(m, head(m) and m.gender == "female")
```

```{note}
The exact gender field/value depends on your data model. Use autocomplete to find the right field (e.g., `gender`, `gender_id.name`, `gender_id.code`).
```

### Elderly Member Present

Person over 65:
```cel
members.exists(m, age_years(m.birthdate) >= 65)
```

### Disabled Member Present

```cel
members.exists(m, m.has_disability == true)
```

### Household Size

```cel
members.count(m, true) >= 3
```

### Sum Member Income

```cel
members.sum(m.income, true)
```

With threshold:
```cel
members.sum(m.income, true) < 10000
```

## Program Enrollments

### Any Active Enrollment

```cel
enrollments.exists(e, e.state == "enrolled")
```

### Enrolled in Specific Program

```cel
enrollments.exists(e, e.state == "enrolled" and e.program_id.name == "4Ps")
```

### Not Currently Enrolled

```cel
not enrollments.exists(e, e.state == "enrolled")
```

### Count Active Enrollments

```cel
enrollments.count(e, e.state == "enrolled")
```

## Entitlements

### Has Approved Entitlement

```cel
entitlements.exists(ent, ent.state == "approved")
```

### Total Entitlement Amount

```cel
entitlements.sum(ent.amount, ent.state == "approved")
```

### Entitlements This Year

```cel
entitlements.exists(ent, ent.state == "approved" and ent.date_approved >= "2024-01-01")
```

## Event Data

Requires event/CEL integration modules.

### Has Recent Visit

Visit in last 90 days:
```cel
has_event("visit", within_days=90)
```

### Count Visits This Year

```cel
events_count("visit", period=this_year())
```

### Total Payments Received

```cel
events_sum("payment", "amount", period=this_year())
```

### Latest Survey Income

```cel
event("survey", "income", select="latest", within_months=12, default=0)
```

### Income Below Threshold

```cel
event("survey", "income", select="latest", within_months=12, default=0) < 500
```

### Completed Health Check

```cel
has_event("health_check", within_months=6)
```

## Eligibility Rules

### Income-Based

Household income under threshold:
```cel
household_income < poverty_line
```

Or with literal:
```cel
household_income < 10000
```

### Demographic Targeting

Children under 5 in low-income household:
```cel
children_under_5_count >= 1 and household_income < poverty_line
```

### Geographic Targeting

In target region:
```cel
me.area_id.name == "Region IV-A"
```

### Multi-Criteria

```cel
household_income < poverty_line
and children_under_5_count >= 1
and not enrollments.exists(e, e.state == "enrolled" and e.program_id.name == "Other Program")
```

### Vulnerability Score

```cel
vulnerability_score >= 50
```

## Entitlement Amount Formulas

These are evaluated at runtime with a small context (typically `me` and `base_amount`).

### Fixed Amount

```cel
500
```

### Scaled by Base

```cel
base_amount * 1.1
```

### Per Child Bonus

```cel
base_amount + (children_under_5_count * 200)
```

### Capped Amount

```cel
min(base_amount + (children_count * 100), 2000)
```

### Tiered by Household Size

```cel
members.count(m, true) <= 3 ? 500 : (members.count(m, true) <= 5 ? 750 : 1000)
```

## Scoring Formulas

### Simple Indicator

```cel
me.has_disability ? 10 : 0
```

### Age-Based Score

```cel
age_years(me.birthdate) >= 65 ? 5 : 0
```

### Household Composition Score

```cel
children_under_5_count * 3 + elderly_count * 2
```

### Normalized Score

```cel
min(vulnerability_score / 10, 10)
```

## Validation Rules

### Required Field

```cel
has(me.birthdate)
```

### Age Validation

```cel
has(me.birthdate) and age_years(me.birthdate) >= 0 and age_years(me.birthdate) <= 120
```

### Format Check

```cel
me.phone.startsWith("+63")
```

### Cross-Field Validation

Head of household must be adult:
```cel
not head(me) or age_years(me.birthdate) >= 18
```

## Workflow Routing

These are runtime evaluated with ticket/case context.

### Priority Based on Age

```cel
r.registrant_id.age >= 65 ? "priority" : "standard"
```

### Escalate High Value

```cel
r.amount > 10000 ? "manager_review" : "standard"
```

### Route by Region

```cel
r.area_id.name == "NCR" ? "ncr_team" : "regional_team"
```

## Tips for Adapting Patterns

1. **Check field names**: Use autocomplete to find exact field paths
2. **Verify context**: Individual vs group expressions need different symbols
3. **Test incrementally**: Start simple, add complexity
4. **Use variables**: Extract repeated logic into variables
5. **Add tests**: Create test cases in Studio before publishing

## Are You Stuck?

See {doc}`troubleshooting` for common issues and debugging tips.
