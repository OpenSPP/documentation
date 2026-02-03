---
openspp:
  doc_status: draft
---

# CEL Domain Query Builder


## Overview

The CEL Domain Query Builder (`spp_cel_domain`) enables users to write simple, human-readable expressions to filter records in OpenSPP. CEL (Common Expression Language) provides a more intuitive alternative to Odoo's native domain syntax, making it easier for implementers to define eligibility criteria, targeting rules, and data filters.

## Purpose

This module is designed to:

- **Simplify record filtering:** Write expressions like `age_years(r.birthdate) >= 18` instead of complex Odoo domains
- **Support variable resolution:** Reference pre-defined variables (e.g., `r.household_size`) that expand to their underlying expressions
- **Enable member aggregations:** Perform calculations across group members (count, sum, average, min, max)
- **Provide unified data storage:** Manage computed values and external data through the `spp.data.value` and `spp.data.provider` models

## Module Dependencies

| Dependency        | Description                                                                  |
| ----------------- | ---------------------------------------------------------------------------- |
| `base`            | Odoo core framework                                                          |
| `spp_base_common` | Common OpenSPP utilities and base models                                     |
| `spp_security`    | OpenSPP security groups and access control                                   |
| `spp_registry`    | Registry models for individuals and groups (required for member aggregation) |

## Key Features

### CEL Expression Syntax

CEL expressions support common operators and functions:

| Syntax      | Description                      | Example                             |
| ----------- | -------------------------------- | ----------------------------------- |
| Comparisons | `==`, `!=`, `<`, `<=`, `>`, `>=` | `r.age >= 18`                       |
| Logical     | `&&`, `\|\|`, `!`                | `r.age >= 18 && r.income < 5000`    |
| Membership  | `in`                             | `r.status in ["active", "pending"]` |
| Ternary     | `? :`                            | `r.age >= 65 ? "senior" : "adult"`  |

### Built-in Functions

| Function                 | Description                           | Example                             |
| ------------------------ | ------------------------------------- | ----------------------------------- |
| `age_years(date)`        | Calculate age in years from birthdate | `age_years(r.birthdate) >= 18`      |
| `today()`                | Current date                          | `r.registration_date < today()`     |
| `days_ago(n)`            | Date n days in the past               | `r.last_activity > days_ago(30)`    |
| `months_ago(n)`          | Date n months in the past             | `r.enrollment_date > months_ago(6)` |
| `years_ago(n)`           | Date n years in the past              | `r.birthdate < years_ago(65)`       |
| `between(val, min, max)` | Check if value is in range            | `between(r.income, 1000, 5000)`     |
| `size(list)`             | Get list length                       | `size(r.children) > 0`              |
| `has(obj, key)`          | Check if object has key               | `has(r, "phone")`                   |
| `matches(str, pattern)`  | Regex pattern matching                | `matches(r.id_number, "^[A-Z]")`    |

### Member Aggregations

For group/household records, aggregate across members:

| Function                        | Description                 | Example                                     |
| ------------------------------- | --------------------------- | ------------------------------------------- |
| `members.count(filter)`         | Count matching members      | `members.count(age_years(m.birthdate) < 5)` |
| `members.exists(filter)`        | Check if any member matches | `members.exists(m.is_disabled)`             |
| `members.sum(m, field, filter)` | Sum field values            | `members.sum(m, m.income, true)`            |
| `members.avg(m, field, filter)` | Average field values        | `members.avg(m, m.age, true)`               |
| `members.min(m, field, filter)` | Minimum field value         | `members.min(m, m.age, true)`               |
| `members.max(m, field, filter)` | Maximum field value         | `members.max(m, m.income, true)`            |

### Profile-Based Compilation

Expressions are compiled against profiles that define the context:

| Profile                | Target Model             | Use Case                           |
| ---------------------- | ------------------------ | ---------------------------------- |
| `registry_individuals` | `res.partner`            | Filter individual registrants      |
| `registry_groups`      | `res.partner`            | Filter group/household registrants |
| `program_memberships`  | `spp.program.membership` | Filter program enrollments         |
| `entitlements`         | `spp.entitlement`        | Filter entitlement records         |

### Data Providers and Values

The module includes a unified variable/value storage system:

- **Data Providers** (`spp.data.provider`): Define sources of computed or external data
- **Data Values** (`spp.data.value`): Store computed values for registrants

## Integration

### With Programs Module

When `spp_programs` is installed, CEL expressions can reference program-related data:

```
r.program_count > 0 && r.total_entitlements < 10000
```

### With Eligibility Criteria

Used by program managers to define who qualifies for programs:

```
age_years(r.birthdate) >= 18 && age_years(r.birthdate) <= 65 && r.monthly_income < 5000
```

### With Targeting Rules

Filter beneficiaries for specific interventions:

```
r.area_id.admin_level == 3 && members.count(age_years(m.birthdate) < 5) > 0
```

### CEL Service API

Other modules can use the CEL service facade:

```python
service = env["spp.cel.service"]

# Compile and execute expression
result = service.compile_expression(
    "age_years(r.birthdate) >= 18",
    profile="registry_individuals"
)
# result = {"domain": [...], "count": 123, "ids": [...], "valid": True}

# Validate without executing
validation = service.validate_expression(
    "r.income < 5000",
    profile="registry_individuals"
)
# validation = {"valid": True, "error": None, "explain": "..."}
```

## Are you stuck?

### Expression returns no results

**Symptom:** Your expression compiles successfully but returns 0 matching records.

**Cause:** The expression logic may be too restrictive, or the field references may not match actual data.

**Solution:**

1. Test with a simpler expression first (e.g., just `true`)
2. Check that field names match exactly (case-sensitive)
3. Verify data exists in the referenced fields

### Unknown symbol error

**Symptom:** Error message "Unknown symbol: fieldname"

**Cause:** The field or variable does not exist in the selected profile.

**Solution:**

1. Check the profile's available symbols
2. Verify the field exists on the target model
3. For variables, ensure they are defined in the variable configuration

### Syntax error in expression

**Symptom:** Error message "Syntax error: unexpected token"

**Cause:** The expression contains invalid CEL syntax.

**Solution:**

1. Check operator syntax (`&&` not `and`, `||` not `or`)
2. Ensure strings are quoted properly
3. Verify parentheses are balanced
4. Check function call syntax (parentheses required)
