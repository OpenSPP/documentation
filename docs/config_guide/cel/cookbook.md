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

## Basic patterns

### Boolean logic

```cel
r.is_registrant == true and r.active == true
```

Equivalent with operators:
```cel
r.is_registrant && r.active
```

### Handle missing values

Always check existence before accessing optional fields:

```cel
has(r.birthdate) and age_years(r.birthdate) >= 18
```

### Ternary (if/else)

```cel
r.is_group ? 1 : 0
```

More complex:
```cel
r.income < 5000 ? "low" : (r.income < 15000 ? "medium" : "high")
```

### String comparisons

```cel
r.status == "active"
r.region != "excluded_region"
```

## Household composition

### Any child under 5

```cel
members.exists(m, age_years(m.birthdate) < 5)
```

Or newer syntax:
```cel
members.exists(age_years(m.birthdate) < 5)
```

### Count children under 18

```cel
members.count(m, age_years(m.birthdate) < 18)
```

### Count children in age range

Children aged 6-12:
```cel
members.count(m, age_years(m.birthdate) >= 6 and age_years(m.birthdate) <= 12)
```

### Female head of household

```cel
members.exists(m, head(m) and m.gender == "female")
```

```{note}
The exact gender field/value depends on your data model. Use autocomplete to find the right field (e.g., `gender`, `gender_id.name`, `gender_id.code`).
```

### Elderly member present

Person over 65:
```cel
members.exists(m, age_years(m.birthdate) >= 65)
```

### Disabled member present

```cel
members.exists(m, m.has_disability == true)
```

### Household size

```cel
members.count(m, true) >= 3
```

### Sum member income

```cel
members.sum(m.income, true)
```

With threshold:
```cel
members.sum(m.income, true) < 10000
```

## Program enrollments

### Any active enrollment

```cel
enrollments.exists(e, e.state == "enrolled")
```

### Enrolled in specific program

```cel
enrollments.exists(e, e.state == "enrolled" and e.program_id.name == "4Ps")
```

### Not currently enrolled

```cel
not enrollments.exists(e, e.state == "enrolled")
```

### Count active enrollments

```cel
enrollments.count(e, e.state == "enrolled")
```

## Entitlements

### Has approved entitlement

```cel
entitlements.exists(ent, ent.state == "approved")
```

### Total entitlement amount

```cel
entitlements.sum(ent.amount, ent.state == "approved")
```

### Entitlements this year

```cel
entitlements.exists(ent, ent.state == "approved" and ent.date_approved >= "2024-01-01")
```

## Event data

Requires event/CEL integration modules.

### Has recent visit

Visit in last 90 days:
```cel
has_event("visit", within_days=90)
```

### Count visits this year

```cel
events_count("visit", period=this_year())
```

### Total payments received

```cel
events_sum("payment", "amount", period=this_year())
```

### Latest survey income

```cel
event("survey", "income", select="latest", within_months=12, default=0)
```

### Income below threshold

```cel
event("survey", "income", select="latest", within_months=12, default=0) < 500
```

### Completed health check

```cel
has_event("health_check", within_months=6)
```

## Eligibility rules

### Income-based

Household income under threshold:
```cel
household_income < poverty_line
```

Or with literal:
```cel
household_income < 10000
```

### Demographic targeting

Children under 5 in low-income household:
```cel
children_under_5_count >= 1 and household_income < poverty_line
```

### Geographic targeting

In target region:
```cel
r.area_id.name == "Region IV-A"
```

### Multi-criteria

```cel
household_income < poverty_line
and children_under_5_count >= 1
and not enrollments.exists(e, e.state == "enrolled" and e.program_id.name == "Other Program")
```

### Vulnerability score

```cel
vulnerability_score >= 50
```

## Entitlement amount formulas

These are evaluated at runtime with a small context (typically `me` and `base_amount`).

### Fixed amount

```cel
500
```

### Scaled by base

```cel
base_amount * 1.1
```

### Per child bonus

```cel
base_amount + (children_under_5_count * 200)
```

### Capped amount

```cel
min(base_amount + (children_count * 100), 2000)
```

### Tiered by household size

```cel
members.count(m, true) <= 3 ? 500 : (members.count(m, true) <= 5 ? 750 : 1000)
```

## Scoring formulas

### Simple indicator

```cel
r.has_disability ? 10 : 0
```

### Age-based score

```cel
age_years(r.birthdate) >= 65 ? 5 : 0
```

### Household composition score

```cel
children_under_5_count * 3 + elderly_count * 2
```

### Normalized score

```cel
min(vulnerability_score / 10, 10)
```

## Validation rules

### Required field

```cel
has(r.birthdate)
```

### Age validation

```cel
has(r.birthdate) and age_years(r.birthdate) >= 0 and age_years(r.birthdate) <= 120
```

### Format check

```cel
startswith(r.phone, "+63")
```

### Cross-field validation

Head of household must be adult:
```cel
not head(r) or age_years(r.birthdate) >= 18
```

## Workflow routing

These are runtime evaluated with ticket/case context.

### Priority based on age

```cel
r.registrant_id.age >= 65 ? "priority" : "standard"
```

### Escalate high value

```cel
r.amount > 10000 ? "manager_review" : "standard"
```

### Route by region

```cel
r.area_id.name == "NCR" ? "ncr_team" : "regional_team"
```

## Tips for adapting patterns

1. **Check field names**: Use autocomplete to find exact field paths
2. **Verify context**: Individual vs group expressions need different symbols
3. **Test incrementally**: Start simple, add complexity
4. **Use variables**: Extract repeated logic into variables
5. **Add tests**: Create test cases in Studio before publishing

## Are you stuck?

See {doc}`troubleshooting` for common issues and debugging tips.
