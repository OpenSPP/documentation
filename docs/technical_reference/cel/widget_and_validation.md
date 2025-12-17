---
openspp:
  doc_status: unverified
---

# Editor widget and validation

OpenSPP ships a CEL editor widget that provides:

- profile-aware autocomplete (symbols and fields)
- validation/linting with inline errors
- a symbol browser (variables, functions, library expressions)

The widget is used in Studio and other configuration screens that accept CEL.

## Validation APIs

The frontend calls JSON-RPC endpoints to fetch symbols and validate expressions:

- `POST /spp_cel/profiles` — list available profiles
- `POST /spp_cel/symbols/<profile>` — symbols/functions/variables for a profile
- `POST /spp_cel/validate` — validate expression + return structured errors and matching count

## What validation returns

Validation returns a structure like:

- `valid` (boolean)
- `errors` (list of `{message, line, col_start, col_end, severity, suggestion?}`)
- `matching_count` (when validation compiles the expression for a profile)
- `explain` (human-readable explanation, when available)

```{note}
Developer reference (source code):
- Controller routes: `openspp-modules-v2/spp_cel_widget/controllers/main.py`
- Symbol provider: `openspp-modules-v2/spp_cel_widget/models/cel_symbol_provider.py`
- Widget field + editor: `openspp-modules-v2/spp_cel_widget/static/src/js/cel_editor_field.js`, `openspp-modules-v2/spp_cel_widget/static/src/js/cel_editor.js`
```

