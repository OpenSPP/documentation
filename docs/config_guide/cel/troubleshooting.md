---
openspp:
  doc_status: draft
---

# CEL Troubleshooting

This guide is for **implementers** debugging CEL expressions that aren't working as expected.

## Quick Diagnosis

| Symptom | Likely Cause | Jump To |
|---------|--------------|---------|
| "Unknown symbol" error | Wrong profile/context | [Section 1](#1-unknown-symbol-or-field-not-found) |
| "Unknown variable" error | Variable not active | [Section 2](#2-unknown-variable) |
| Syntax error | Quoting or operator issue | [Section 3](#3-syntax-errors) |
| Validates but matches 0 | Wrong population or data | [Section 4](#4-validates-but-matches-0-records) |
| Slow performance | Complex expression | [Section 5](#5-performance-issues) |

## 1. "Unknown Symbol" or "Field Not Found"

This almost always means:
- You're in a different **profile/context** than expected
- The field name differs in your deployment

### Checklist

1. **Check the profile**
   - Open the symbol browser in the CEL editor
   - Verify you're in the expected profile (individual vs group)

2. **Use autocomplete**
   - Type `me.` and see available fields
   - Field names may differ from UI labels

3. **Check related records**
   - For group context: `members.` prefix
   - For enrollments: `enrollments.` prefix

### Common Mistakes

| You Wrote | Problem | Fix |
|-----------|---------|-----|
| `birthdate` | Missing context | `me.birthdate` |
| `me.gender` | Field might be `gender_id.name` | Check autocomplete |
| `members.age` | Age is computed | `age_years(m.birthdate)` |
| `income` | Field might be custom | Check actual field name |

### If Field Doesn't Exist

If you need a field that isn't available:
1. Add it as a custom field in Registry configuration
2. Create a variable that maps to it
3. Contact your administrator

## 2. "Unknown Variable"

The variable exists but can't be resolved.

### Checklist

1. **Is the variable Active?**
   - Go to Studio → Variables
   - Find your variable
   - Check the **Status** field

2. **Does Applies To match?**
   - Variable set to "Individual" won't work in group context
   - Variable set to "Group" won't work in individual context

3. **Are you using the right name?**
   - Use the **CEL Accessor** exactly
   - Not the Name field, not the Technical Name

### Example

| Field | Value |
|-------|-------|
| Name | Children Under 5 Count |
| CEL Accessor | `children_under_5_count` |
| Technical Name | `x_cel_var_children_u5` |

In expressions, use: `children_under_5_count` ✓

Not: `Children Under 5 Count` ✗
Not: `x_cel_var_children_u5` ✗

## 3. Syntax Errors

### Common Mistakes

| Mistake | Problem | Fix |
|---------|---------|-----|
| `enrolled` | Unquoted string | `"enrolled"` |
| `True` / `FALSE` | Wrong case | `true` / `false` |
| `AND` / `OR` | Wrong case | `and` / `or` |
| `me.status = "active"` | Single equals | `me.status == "active"` |

### String Quoting

Strings must be quoted:

```cel
# Wrong
me.status == active

# Right
me.status == "active"
```

### Boolean Values

Booleans are lowercase:

```cel
# Wrong
me.is_group == True

# Right
me.is_group == true
```

### Operator Case

Operators are lowercase:

```cel
# Wrong
a AND b OR c

# Right
a and b or c
```

### Parentheses for Precedence

When mixing `and`/`or`, use parentheses:

```cel
# Ambiguous
a and b or c

# Clear
(a and b) or c
a and (b or c)
```

## 4. Validates but Matches 0 Records

The expression is syntactically correct but finds no matches.

### Checklist

1. **Check the base population**
   - Are you filtering individuals or groups?
   - The profile applies a base domain automatically

2. **Verify data exists**
   - Do test records have the expected field values?
   - Are the values in the expected format?

3. **Check member relations**
   - `members` may exclude ended memberships by default
   - Verify test households have active members

4. **Check event data (if using events)**
   - Are there matching events for test registrants?
   - Are events in the expected state?

### Debugging Steps

1. **Simplify the expression**
   ```cel
   # Start with just
   true
   # Then add one condition at a time
   me.active == true
   # Then more
   me.active == true and has(me.birthdate)
   ```

2. **Check matching count**
   - The editor shows matching count for compile-to-domain
   - Watch how it changes as you add conditions

3. **Test with known records**
   - Find a record you know should match
   - Build expression to match just that record
   - Expand from there

## 5. Performance Issues

### Symptoms

- Expression takes long to validate
- Eligibility check times out
- "Python fallback" warnings

### Causes and Solutions

| Cause | Solution |
|-------|----------|
| Complex event queries | Simplify predicates, use caching |
| Large member aggregates | Use cached variables |
| Many nested conditions | Break into variables |
| Uncached expensive variables | Enable caching |

### Use Cached Variables

For expensive computations:

1. Go to Studio → Variables
2. Edit the variable
3. Set **Cache Strategy** to TTL or Manual
4. Configure invalidation triggers

### Simplify Event Queries

Instead of complex `where` predicates:

```cel
# May fall back to Python
events_count("visit", where="data->>'type' == 'home'", within_days=90)

# Prefer simpler form
events_count("home_visit", within_days=90)
```

### Precomputation

For batch eligibility checks:
- Enable variable precomputation
- Run precompute before eligibility assessment
- Contact administrator for setup

## Debugging Tools

### Symbol Browser

1. Open the CEL editor
2. Click the symbol browser icon
3. Browse available:
   - Profiles
   - Symbols and fields
   - Variables
   - Functions

### Validation Preview

The editor shows:
- Syntax errors with line/column
- Unknown symbol warnings
- Matching record count

### Test Cases

For expressions in Studio:

1. Go to the **Tests** tab
2. Add test cases with expected results
3. Run tests to verify behavior

## Getting More Help

If you're still stuck:

1. **Check the profile documentation**
   - Each feature documents its CEL context
   - See program, GRM, scoring documentation

2. **Review variable configuration**
   - Verify source type settings
   - Check aggregate filters

3. **Contact your administrator**
   - They can check server logs
   - They can verify module configuration

## Related Documentation

- {doc}`quick_start` - Basic concepts
- {doc}`syntax` - Complete syntax reference
- {doc}`variables` - Variable configuration
- {doc}`cookbook` - Working examples
