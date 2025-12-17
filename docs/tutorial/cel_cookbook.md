---
openspp:
  doc_status: unverified
---

# CEL cookbook (common patterns)

This page is a “copy/paste and adapt” list of common patterns. It’s written for implementers configuring OpenSPP.

```{note}
Which symbols are available depends on the screen/profile. Use the editor’s symbol browser/autocomplete to confirm what exists in your context.
```

## Basics

### Boolean logic

```text
me.is_registrant == true and me.active == true
```

You may also see `&&`, `||`, and `!` (equivalent to `and`, `or`, `not`).

### Handle missing values

```text
has(me.birthdate) and age_years(me.birthdate) >= 18
```

### Ternary (if/else)

```text
me.is_group ? 1 : 0
```

## Household composition

### Any child under 5

```text
members.exists(age_years(m.birthdate) < 5)
```

### Count children under 18

```text
members.count(age_years(m.birthdate) < 18)
```

### Female head of household

```text
members.exists(head(m) and m.gender == "female")
```

```{note}
Exact gender field/value depends on your data model. Use autocomplete to find the right field (for example `gender`, `gender_id.name`, `gender_id.code`, …).
```

### Sum member income (if your model has income per member)

```text
members.sum(m.income, true) >= 8000
```

## Program enrollments and entitlements (when available in profile)

### Any enrollment in enrolled state

```text
enrollments.exists(e.state == "enrolled")
```

### Any entitlement this cycle / period (example pattern)

```text
entitlements.exists(e.state == "approved")
```

```{note}
Enrollment/entitlement fields vary by deployment. Confirm field names in your environment.
```

## Event data (when event/CEL integration is installed)

### Has a visit in the last 90 days

```text
events_count("visit", within_days=90) >= 1
```

### Read latest survey value with a default

```text
event("survey", "income", select="latest", within_months=12, default=0) < 500
```

See {doc}`event_data` for how to create event types and enter events, and {doc}`../technical_reference/cel/events` for function details.

## Amount formulas (runtime evaluation contexts)

Some screens evaluate CEL as a formula with a small context dict (not a full profile). A common example is entitlement amount formulas where context includes:

- `me`: the beneficiary record (safe access to fields)
- `base_amount`: the configured base amount

Examples:

```text
500
```

```text
base_amount * 1.1
```

```text
min(me.children_count * 50, 500)
```

```{note}
Runtime contexts are feature-specific. See {doc}`../technical_reference/cel/usage_by_feature`.
```

