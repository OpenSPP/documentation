---
openspp:
  doc_status: draft
  products: [core]
---

# CEL Syntax Reference

This guide is for **implementers** who need detailed syntax documentation.

## Expression Types

Expressions in OpenSPP are categorized by type:

| Type | Output | Use Case |
|------|--------|----------|
| Eligibility | Boolean | Program qualification rules |
| Compliance | Boolean | Ongoing requirement checks |
| Benefit | Number | Entitlement amount formulas |
| Scoring | Number | Scoring indicator formulas |
| Validation | Boolean | Data validation rules |
| Other | Any | Library/utility expressions |

## Basic Syntax

### Literals

| Type | Examples |
|------|----------|
| Boolean | `true`, `false` |
| Number | `42`, `3.14`, `-10` |
| String | `"enrolled"`, `"active"` |
| Null | `null` |

### Operators

#### Comparison

| Operator | Example | Description |
|----------|---------|-------------|
| `==` | `me.status == "active"` | Equal |
| `!=` | `me.status != "cancelled"` | Not equal |
| `<` | `me.age < 18` | Less than |
| `<=` | `me.age <= 65` | Less than or equal |
| `>` | `me.income > 10000` | Greater than |
| `>=` | `me.income >= 5000` | Greater than or equal |

#### Logical

| Operator | Alternative | Example |
|----------|-------------|---------|
| `and` | `&&` | `a and b` |
| `or` | `\|\|` | `a or b` |
| `not` | `!` | `not a` |

#### Arithmetic

| Operator | Example | Description |
|----------|---------|-------------|
| `+` | `a + b` | Addition |
| `-` | `a - b` | Subtraction |
| `*` | `a * b` | Multiplication |
| `/` | `a / b` | Division |
| `%` | `a % b` | Modulo |

### Ternary (Conditional)

```cel
condition ? value_if_true : value_if_false
```

Example:
```cel
me.is_group ? 1 : 0
```

### Safe Field Access

Use `has()` to check if a field exists before accessing:

```cel
has(me.birthdate) and age_years(me.birthdate) >= 18
```

## Built-in Functions

### Date/Time Functions

| Function | Example | Description |
|----------|---------|-------------|
| `age_years(date)` | `age_years(me.birthdate)` | Years since date |
| `age_months(date)` | `age_months(me.birthdate)` | Months since date |
| `age_days(date)` | `age_days(me.registration_date)` | Days since date |

### Math Functions

| Function | Example | Description |
|----------|---------|-------------|
| `min(a, b)` | `min(me.score, 100)` | Minimum value |
| `max(a, b)` | `max(me.score, 0)` | Maximum value |
| `abs(n)` | `abs(me.balance)` | Absolute value |

### String Functions

| Function | Example | Description |
|----------|---------|-------------|
| `startsWith(s, prefix)` | `me.id.startsWith("PH-")` | Check prefix |
| `endsWith(s, suffix)` | `me.id.endsWith("-2024")` | Check suffix |
| `contains(s, sub)` | `me.name.contains("Jr")` | Check substring |
| `size(s)` | `size(me.name)` | String length |

### Collection Functions

Used with relations like `members`, `enrollments`, `entitlements`:

| Function | Example | Description |
|----------|---------|-------------|
| `exists(predicate)` | `members.exists(age_years(m.birthdate) < 5)` | Any match |
| `all(predicate)` | `members.all(m.active == true)` | All match |
| `count(predicate)` | `members.count(age_years(m.birthdate) < 18)` | Count matches |
| `sum(expr, predicate)` | `members.sum(m.income, true)` | Sum values |
| `filter(predicate)` | `enrollments.filter(e.state == "enrolled")` | Filter list |

### Existence Check

| Function | Example | Description |
|----------|---------|-------------|
| `has(field)` | `has(me.birthdate)` | Field exists and not null |

## Collection Predicates

When using collection functions, predicates reference items with a loop variable:

```cel
members.count(m, age_years(m.birthdate) < 5)
members.exists(m, head(m) and m.gender == "female")
enrollments.exists(e, e.state == "enrolled")
```

The loop variable (`m`, `e`, etc.) represents each item in the collection.

```{note}
Newer syntax may omit the explicit loop variable:
`members.count(age_years(m.birthdate) < 5)`
Both forms are supported.
```

## Profiles and Symbols

### What Are Profiles?

Profiles define what data is available in a given context:
- The root model ("current record")
- Related collections
- Available functions

### Default Profiles

| Profile | Root Model | Available Relations |
|---------|-----------|---------------------|
| `registry_individuals` | `res.partner` (individual) | `groups`, `enrollments`, `entitlements`, `events` |
| `registry_groups` | `res.partner` (group) | `members`, `enrollments`, `entitlements`, `events` |
| `program_memberships` | `spp.program.membership` | - |
| `entitlements` | `spp.entitlement` | - |
| `grm_tickets` | `spp.grm.ticket` | - |

### Root Record Symbols

Most profiles provide access to the current record:

| Symbol | Usage |
|--------|-------|
| `me` | Preferred in newer screens |
| `r` | Used in older examples |

Example:
```cel
me.is_registrant == true and me.active == true
```

## CEL Editor Widget

The Studio CEL editor provides:

### Autocomplete

- Type `me.` to see available fields
- Type a function name to see signature

### Symbol Browser

Click the symbol icon to browse:
- Available profiles
- Symbols and fields
- Variables
- Functions

### Validation

Real-time validation shows:
- Syntax errors
- Unknown symbols
- Type mismatches
- Matching record count (for compile-to-domain)

### Validation API

For developers, the widget calls these endpoints:

| Endpoint | Purpose |
|----------|---------|
| `POST /spp_cel/profiles` | List available profiles |
| `POST /spp_cel/symbols/<profile>` | Get symbols for profile |
| `POST /spp_cel/validate` | Validate expression |

## CEL Execution Modes

### Compile-to-Domain

Used for record selection (eligibility, search):
- Supports profile symbols and relations
- Compiles to Odoo domain (SQL-optimized)
- Shows matching count in editor

### Runtime Evaluation

Used for value computation (amounts, routing):
- Works with provided context dictionary
- Supports arithmetic and comparisons
- No ORM access

| Feature | Compile-to-Domain | Runtime |
|---------|-------------------|---------|
| Profile symbols | ✓ | Limited |
| Relations (members) | ✓ | ✗ |
| Matching count | ✓ | ✗ |
| Arithmetic | ✓ | ✓ |
| Context variables | ✓ | ✓ |

## Are You Stuck?

**"Unknown symbol" error?**
- Check the profile matches your context (individual vs group)
- Use autocomplete to find the correct field name
- Verify variables are active

**Expression validates but matches 0 records?**
- Verify the base population (individuals vs groups)
- Check member relations exclude ended memberships
- Ensure event data exists if using event functions

**Need more help?**
- See {doc}`troubleshooting` for common issues
- See {doc}`variables` for variable configuration
