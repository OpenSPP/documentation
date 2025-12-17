---
openspp:
  doc_status: unverified
---

# CEL troubleshooting

This page is a practical checklist for when an expression “should work” but doesn’t.

## 1) “Unknown symbol” or “field not found”

This almost always means one of these:

- You are in a different **profile/context** than you think (household vs individual, ticket vs registrant, etc.).
- The field name differs in your deployment (custom fields, different vocabulary fields, etc.).

What to do:

1. Open the CEL editor’s **symbol browser** and confirm the profile and available symbols.
2. Use autocomplete to find the correct field path.
3. If you need a field that doesn’t exist, add it (Studio field or custom module), then create a variable for it.

See {doc}`../technical_reference/cel/widget_and_validation` and {doc}`../technical_reference/cel/profiles_and_symbols`.

## 2) “Unknown variable”

Common causes:

- The variable exists but is not **Active**.
- The variable’s **Applies To** doesn’t match the screen context (individual vs group/household).
- You referenced the wrong name: variables are referenced by **CEL Accessor** (recommended) or sometimes by technical name depending on configuration.

Checklist:

- Confirm the variable is Active.
- Confirm Applies To includes your context.
- Confirm you are using the CEL Accessor exactly.

## 3) Syntax errors (quoting, booleans, operators)

Common mistakes:

- Strings must be quoted: `"enrolled"` not `enrolled`
- Booleans are `true` / `false` (lowercase)
- Use `and` / `or` / `not` (or `&&` / `||` / `!` if supported in your screen)

Example:

```text
has(me.birthdate) and age_years(me.birthdate) >= 18
```

## 4) “It validates but matches 0 records”

For compile-to-domain screens (filters/eligibility):

- Confirm you are filtering the right population (individual registrants vs groups/households). Many profiles apply a base domain automatically.
- For household member rules, confirm whether the `members` relation excludes ended memberships by default.
- If you rely on event data, confirm you have matching active events for the registrants you are testing.

See {doc}`../technical_reference/cel/usage_by_feature` and {doc}`../technical_reference/cel/events`.

## 5) Performance: slow evaluation / Python fallback

Some constructs can cause a slower execution path (depending on feature/module):

- Event aggregates with complex `where` predicates may fall back to Python execution.
- Heavy logic over large datasets may benefit from caching.

What to do:

- Prefer reusable variables and, where appropriate, enable caching (`ttl` or `manual`) for expensive variables.
- If you use caching, ensure you understand invalidation rules and precomputation options.

See {doc}`../technical_reference/cel/caching_and_metric`.

## Screenshot placeholders (optional)

- `tutorial/cel_troubleshooting/symbol_browser.png`
- `tutorial/cel_troubleshooting/validation_error_example.png`
- `tutorial/cel_troubleshooting/explain_preview.png`

