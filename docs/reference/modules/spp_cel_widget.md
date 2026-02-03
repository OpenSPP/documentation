---
openspp:
  doc_status: draft
---

# CEL Expression Widget


## Overview

The CEL Expression Widget (`spp_cel_widget`) provides a reusable, rich text editor component for writing CEL expressions in the OpenSPP user interface. It features syntax highlighting, autocomplete suggestions, and real-time validation to help users write correct expressions efficiently.

## Purpose

This module is designed to:

- **Enhance expression editing:** Provide a code editor experience with CEL-specific syntax highlighting
- **Accelerate expression writing:** Offer autocomplete for available fields, functions, and variables
- **Prevent errors:** Real-time linting highlights syntax issues before saving
- **Improve discoverability:** Symbol browser shows all available options in context

## Module Dependencies

| Dependency       | Description                                   |
| ---------------- | --------------------------------------------- |
| `web`            | Odoo web framework for frontend components    |
| `spp_cel_domain` | CEL expression parsing and compilation engine |

## Key Features

### Syntax Highlighting

The editor uses CodeMirror with custom CEL language support:

| Element   | Highlighting                                |
| --------- | ------------------------------------------- |
| Keywords  | `true`, `false`, `in`, `&&`, `\|\|`         |
| Functions | `age_years()`, `today()`, `members.count()` |
| Strings   | Quoted text in different color              |
| Numbers   | Numeric literals                            |
| Operators | Comparison and logical operators            |
| Variables | `r.field`, `m.field` references             |

### Autocomplete

As you type, the widget suggests:

- **Fields:** Available fields from the current profile context
- **Functions:** Built-in CEL functions with parameter hints
- **Variables:** Pre-defined variables from `spp.cel.variable`
- **Operators:** Logical and comparison operators

Trigger autocomplete by typing or pressing `Ctrl+Space`.

### Real-time Linting

The editor validates expressions as you type:

| Issue Type     | Indicator                           |
| -------------- | ----------------------------------- |
| Syntax error   | Red underline with error message    |
| Unknown symbol | Warning indicator with suggestions  |
| Type mismatch  | Orange underline with expected type |

### Symbol Browser

A sidebar panel displays all available symbols organized by category:

- **Record Fields:** Fields available on the target model
- **Functions:** Built-in and custom CEL functions
- **Variables:** Pre-defined variables with their expressions
- **Constants:** System-defined constant values

Click any symbol to insert it at the cursor position.

## Integration

### Form Field Usage

Add the CEL editor widget to any text field:

```xml
<field name="expression" widget="cel_editor" options="{'profile': 'registry_individuals'}"/>
```

### Widget Options

| Option         | Type    | Description                                                               |
| -------------- | ------- | ------------------------------------------------------------------------- |
| `profile`      | string  | CEL profile for context (`registry_individuals`, `registry_groups`, etc.) |
| `show_preview` | boolean | Show live preview of matching records (default: false)                    |
| `show_browser` | boolean | Show symbol browser sidebar (default: true)                               |
| `height`       | string  | Editor height in CSS units (default: `200px`)                             |

### JavaScript API

For custom integrations:

```javascript
// Access the editor instance
const editor = this.refs.celEditor;

// Get current expression
const expression = editor.getValue();

// Set expression programmatically
editor.setValue("age_years(r.birthdate) >= 18");

// Trigger validation
const result = await editor.validate();
```

## Are you stuck?

### Autocomplete not showing

**Symptom:** Pressing `Ctrl+Space` does nothing, or suggestions don't appear.

**Cause:** The widget may not have loaded the symbol definitions yet, or the profile context is missing.

**Solution:**

1. Ensure the `profile` option is set in the widget configuration
2. Wait for the page to fully load before using autocomplete
3. Check browser console for JavaScript errors

### Highlighting looks wrong

**Symptom:** Colors don't match expected syntax categories.

**Cause:** The CEL language mode may not be properly loaded.

**Solution:**

1. Clear browser cache and reload
2. Check that `spp_cel_widget` module is installed
3. Verify no JavaScript errors in browser console

### Validation not working

**Symptom:** Invalid expressions don't show error indicators.

**Cause:** The linting service may not be connected to the backend.

**Solution:**

1. Check network tab for failed API calls
2. Verify user has access to the CEL service
3. Ensure the `spp_cel_domain` module is installed
