---
openspp:
  doc_status: draft
  products: [core]
---

# CEL quick start

This guide is for **implementers** who want to start writing CEL expressions in OpenSPP.

You should be comfortable with "logic builders" (like CommCare or Kobo configuration) but you don't need Python experience.

## What you'll learn

By the end of this guide, you will:
- Understand the three core concepts (symbols, variables, expressions)
- Create your first variable
- Create your first expression
- Know how to discover what data is available

## Prerequisites

- Access to OpenSPP with **Studio Editor** or **Studio Manager** permissions
- The CEL modules installed (standard in OpenSPP V2)

## The three core concepts

### 1. Symbols

Symbols are the data available in a given context. The most common symbols:

| Symbol | What it represents | Available in |
|--------|-------------------|--------------|
| `r` | Current record (registrant, ticket, etc.) | Most contexts |
| `members` | Household members | Group/household context |
| `enrollments` | Program memberships | Registry context |
| `entitlements` | Entitlement records | Registry context |
| `events` | Event data records | When event integration installed |

```{note}
The symbol `r` represents the current record. Inside aggregate functions (like counting members), use `m` to reference each member.
```

### 2. Variables

Variables are named data points you define once and reuse everywhere:

| Source type | Example | Use case |
|-------------|---------|----------|
| **Model Field** | `has_disability` | Maps directly to a registry field |
| **Constant** | `poverty_line = 10000` | Threshold values (can be program-specific) |
| **Computed** | `age = age_years(r.birthdate)` | Calculated from CEL expression |
| **Aggregate** | `children_under_5_count` | Computed over household members |
| **External** | `external_score` | From external data provider |
| **Vocabulary** | `disability_type` | From vocabulary concept |
| **Scoring** | `vulnerability_score` | From scoring model results |

### 3. Expressions

Expressions are reusable rules that combine variables and symbols:

```cel
children_under_5_count >= 1 and household_income < poverty_line
```

Expressions have different types based on their purpose:

| Expression type | Output | Use case |
|-----------------|--------|----------|
| **Filter** | Boolean | Select records (eligibility, search) |
| **Formula** | Number | Calculate amounts (entitlements) |
| **Scoring** | Number | Compute indicator scores |
| **Validation** | Boolean | Data validation rules |

## Example A: Create a variable

**Goal**: Create a variable that counts children under 5 in a household.

### Step 1: Navigate to variables

There are two ways to access Variables:

**Option A - From Dashboard:**
1. Click **Studio** in the main menu
2. Click the **Variables** card on the dashboard

**Option B - From Menu:**
1. Click **Studio** in the main menu
2. Click **Rules** in the top menu bar
3. Click **Variables**

### Step 2: Create a new variable

1. Click **New** to create a new variable

```{figure} ../../_images/en-us/config_guide/cel/quick_start/01-variables-list.png
:alt: Variables list view with New button highlighted

Click **New** to create a new variable.
```

### Step 3: Configure the variable

Fill in the basic information:

| Field | Value |
|-------|-------|
| **Variable Name** | Children Under 5 Count |
| **CEL Accessor** | `children_under_5_count` |

```{figure} ../../_images/en-us/config_guide/cel/quick_start/02-variable-form-basic.png
:alt: Variable form showing name and CEL accessor fields

Fill in the variable name and CEL accessor.
```

### Step 4: Configure the source

Select **Member Aggregate** as the Source Type, then configure:

| Field | Value |
|-------|-------|
| **Source Type** | Member Aggregate |
| **Aggregate Target** | Household Members |
| **Aggregate Type** | Count |
| **Filter (optional)** | `age_years(m.birthdate) < 5` |

```{figure} ../../_images/en-us/config_guide/cel/quick_start/03-variable-aggregate-config.png
:alt: Variable form showing aggregate configuration with filter

Configure the aggregate source type, target, and filter expression.
```

```{note}
In aggregate filters, use `m` to reference each member. The expression `age_years(m.birthdate) < 5` checks each member's age.
```

### Step 5: Save and activate

1. Click **Save** to create the variable in Draft state
2. Click **Activate** to make it available for use

Now you can use `children_under_5_count` in any expression that applies to groups/households.

## Example B: Create an expression

**Goal**: Create an expression that identifies "priority households" (those with children under 5).

### Step 1: Navigate to expressions

**Option A - From Dashboard:**
1. Click **Studio** in the main menu
2. Click the **Expressions** card on the dashboard

**Option B - From Menu:**
1. Click **Studio** in the main menu
2. Click **Rules** in the top menu bar
3. Click **Expressions**

### Step 2: Create a new expression

1. Click **New** to create a new expression

```{figure} ../../_images/en-us/config_guide/cel/quick_start/04-expressions-list.png
:alt: Expressions list view with New button highlighted

Click **New** to create a new expression.
```

### Step 3: Configure the expression

Fill in the basic information:

| Field | Value |
|-------|-------|
| **Name** | Priority Household |
| **Type** | Filter |
| **Context** | Group/Household |
| **Output Type** | Yes/No (Boolean) |

```{figure} ../../_images/en-us/config_guide/cel/quick_start/05-expression-form-basic.png
:alt: Expression form showing name, type, context, and output type fields

Fill in the expression name, type, context, and output type.
```

### Step 4: Enter the CEL expression

In the CEL editor, enter:

```cel
children_under_5_count >= 1
```

```{figure} ../../_images/en-us/config_guide/cel/quick_start/06-cel-editor.png
:alt: CEL editor with expression entered

Enter the CEL expression in the editor.
```

The editor provides:
- **Autocomplete**: Type `children` and press Ctrl+Space to see matching variables
- **Validation**: Errors appear as red underlines with explanations
- **Matching count**: Shows how many records match your expression

### Step 5: Test your expression (recommended)

1. Click the **Tests** tab
2. Click **Add a test case** to add a test case
3. Select a test household from the registry
4. Set the expected result (True or False)
5. Click **Run All Tests** to verify

```{figure} ../../_images/en-us/config_guide/cel/quick_start/07-expression-tests.png
:alt: Expression test tab showing test case configuration

Add test cases and click **Run All Tests** to verify your expression.
```

### Step 6: Save and publish

1. Click **Save** to create the expression in Draft state
2. Click **Submit for Approval** to request publication
3. Once approved, the expression will be **Published** and available for use

```{note}
Expressions follow a workflow: Draft → Pending Approval → Published → Archived. Only users with approval permissions can publish expressions.
```

## How to know what data is available

The CEL editor provides tools to discover available data:

### Autocomplete

Type in the editor and press **Ctrl+Space** to see suggestions:
- Type `r.` to see fields on the current record
- Type a variable name to see matching variables
- Type a function name to see its signature

```{figure} ../../_images/en-us/config_guide/cel/quick_start/08-autocomplete.png
:alt: CEL editor showing autocomplete suggestions

Type `r.` and press **Ctrl+Space** to see available fields.
```

### Symbol browser

Click the **Symbols** button above the CEL editor to browse:
- Available symbols and their fields
- Active variables you can use
- Built-in functions with descriptions

```{figure} ../../_images/en-us/config_guide/cel/quick_start/09-symbol-browser.png
:alt: Symbol browser panel showing available symbols and variables

Click **Symbols** to browse available fields, variables, and functions.
```

### Validation feedback

The editor shows real-time validation:
- **Red underlines**: Syntax errors or unknown symbols
- **Hover for details**: See error explanations
- **Matching count**: For filter expressions, shows how many records match

## Common mistakes

| Mistake | Problem | Fix |
|---------|---------|-----|
| `enrolled` | Unquoted string | `"enrolled"` |
| `True` | Wrong case | `true` |
| `AND` | Wrong case | `and` |
| `birthdate` | Missing context | `r.birthdate` or `m.birthdate` |
| `members.count(age < 5)` | Missing member reference | `members.count(age_years(m.birthdate) < 5)` |

## Are you stuck?

**Can't find the Variables or Expressions menu?**
- Check that you have **Studio Editor** or **Studio Manager** permissions
- Try accessing via the Studio Dashboard cards instead

**Variable not appearing in autocomplete?**
- Make sure the variable is **Active** (variables use Draft → Active workflow)
- Check that the variable's context matches your expression context (Individual vs Group)
- Verify you're using the **CEL Accessor** name, not the display name

**Expression validates but matches 0 records?**
- Check that you're testing against the correct registry type (Individual vs Group)
- Verify test data exists with the expected field values
- Try simplifying the expression to `true` first, then add conditions one at a time

**"Unknown symbol" error?**
- Use autocomplete (Ctrl+Space) to see available symbols
- Check that referenced variables are Active
- Verify the context matches (individual vs group profiles have different symbols)

**Can't activate a variable or publish an expression?**
- Variables: You need **Studio Manager** permission to activate
- Expressions: You need approval permissions to publish (expressions go through an approval workflow)
- Check that all required fields are filled
- For aggregates, verify the filter expression is valid

## Next steps

- **Common patterns**: {doc}`cookbook`
- **Full syntax reference**: {doc}`syntax`
- **Debugging tips**: {doc}`troubleshooting`
- **Variable system details**: {doc}`variables`
