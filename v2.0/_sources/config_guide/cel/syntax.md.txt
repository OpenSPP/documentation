---
openspp:
  doc_status: draft
  products: [core]
---

# CEL syntax reference

This guide is for **implementers** who need detailed syntax documentation.

## Expression types

Expressions in OpenSPP are categorized by type:

| Type | Output | Use case |
|------|--------|----------|
| Filter | Boolean | Select records (eligibility, search, compliance) |
| Formula | Number | Calculate amounts (entitlements, benefits) |
| Scoring | Number | Scoring indicator formulas |
| Data Validation | Boolean | Data validation rules |
| Other | Any | Library/utility expressions |

## Basic syntax

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
| `==` | `r.status == "active"` | Equal |
| `!=` | `r.status != "cancelled"` | Not equal |
| `<` | `r.age < 18` | Less than |
| `<=` | `r.age <= 65` | Less than or equal |
| `>` | `r.income > 10000` | Greater than |
| `>=` | `r.income >= 5000` | Greater than or equal |

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

### Ternary (conditional)

```cel
condition ? value_if_true : value_if_false
```

Example:
```cel
r.is_group ? 1 : 0
```

### Safe field access

Use `has()` to check if a field exists before accessing:

```cel
has(r.birthdate) and age_years(r.birthdate) >= 18
```

## Built-in functions

### Date/time functions

| Function | Example | Description |
|----------|---------|-------------|
| `age_years(date)` | `age_years(r.birthdate)` | Years since date |
| `days_ago(n)` | `days_ago(30)` | Date n days ago |
| `months_ago(n)` | `months_ago(6)` | Date n months ago |
| `years_ago(n)` | `years_ago(1)` | Date n years ago |
| `today()` | `today()` | Current date |
| `now()` | `now()` | Current datetime |

### Math functions

| Function | Example | Description |
|----------|---------|-------------|
| `min(a, b)` | `min(r.score, 100)` | Minimum value |
| `max(a, b)` | `max(r.score, 0)` | Maximum value |
| `abs(n)` | `abs(r.balance)` | Absolute value |

### String functions

| Function | Example | Description |
|----------|---------|-------------|
| `startswith(field, prefix)` | `startswith(r.id, "PH-")` | Check prefix |
| `contains(field, text)` | `contains(r.name, "Jr")` | Check substring |
| `matches(field, pattern)` | `matches(r.id, "^PH-[0-9]+$")` | Regex match |
| `size(s)` | `size(r.name)` | String/collection length |

### Utility functions

| Function | Example | Description |
|----------|---------|-------------|
| `between(value, min, max)` | `between(r.age, 18, 65)` | Check if value is in range |

### Collection functions

Used with relations like `members`, `enrollments`, `entitlements`:

| Function | Example | Description |
|----------|---------|-------------|
| `exists(var, predicate)` | `members.exists(m, age_years(m.birthdate) < 5)` | Any match |
| `all(var, predicate)` | `members.all(m, m.active == true)` | All match |
| `count(var, predicate)` | `members.count(m, age_years(m.birthdate) < 18)` | Count matches |
| `sum(expr, predicate)` | `members.sum(m.income, true)` | Sum values |
| `filter(var, predicate)` | `enrollments.filter(e, e.state == "enrolled")` | Filter list |
| `head(var)` | `members.exists(m, head(m))` | Check if member is head of household |

### Existence check

| Function | Example | Description |
|----------|---------|-------------|
| `has(field)` | `has(r.birthdate)` | Field exists and not null |

## Collection predicates

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

## Profiles and symbols

### What are profiles?

Profiles define what data is available in a given context:
- The root model ("current record")
- Related collections
- Available functions

### Default profiles

| Profile | Root Model | Available Relations |
|---------|-----------|---------------------|
| `registry_individuals` | `res.partner` (individual) | `groups`, `enrollments`, `entitlements`, `events` |
| `registry_groups` | `res.partner` (group) | `members`, `enrollments`, `entitlements`, `events` |
| `program_memberships` | `spp.program.membership` | - |
| `entitlements` | `spp.entitlement` | - |
| `grm_tickets` | `spp.grm.ticket` | - |

### Root record symbol

All profiles provide access to the current record via the `r` symbol:

| Symbol | Description |
|--------|-------------|
| `r` | Current record (registrant, ticket, entitlement, etc.) |

Example:
```cel
r.is_registrant == true and r.active == true
```

```{note}
The symbol `r` represents the current record in all contexts. Inside aggregate functions (like counting members), use `m` to reference each member.
```

## CEL editor widget

The Studio CEL editor provides:

### Autocomplete

- Type `r.` to see available fields on the current record
- Type a function name to see its signature
- Press **Ctrl+Space** to trigger suggestions

See {doc}`quick_start` for a screenshot of the autocomplete feature.

### Symbol browser

Click the **Symbols** button to browse:
- Available profiles
- Symbols and fields
- Variables
- Functions

See {doc}`quick_start` for a screenshot of the symbol browser.

### Validation

Real-time validation shows:
- Syntax errors (red underlines)
- Unknown symbols
- Type mismatches
- Matching record count (for compile-to-domain expressions)

### Validation API

For developers, the widget calls these endpoints:

| Endpoint | Purpose |
|----------|---------|
| `POST /spp_cel/profiles` | List available profiles |
| `POST /spp_cel/symbols/<profile>` | Get symbols for profile |
| `POST /spp_cel/validate` | Validate expression |

## CEL execution modes

### Compile-to-domain

Used for record selection (eligibility, search):
- Supports profile symbols and relations
- Compiles to Odoo domain (SQL-optimized)
- Shows matching count in editor

### Runtime evaluation

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

## Are you stuck?

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
