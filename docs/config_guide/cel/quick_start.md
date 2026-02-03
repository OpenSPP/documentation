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
2. Click **Rules** in the sidebar
3. Click **Variables**

![Studio Dashboard showing Variables card](/_images/en-us/config_guide/cel/quick_start/01-studio-dashboard.png)

### Step 2: Create a new variable

1. Click **New** to create a new variable

![Variables list view](/_images/en-us/config_guide/cel/quick_start/02-variables-list.png)

### Step 3: Configure the variable

Fill in the basic information:

| Field | Value |
|-------|-------|
| **Name** | Children Under 5 Count |
| **CEL Accessor** | `children_under_5_count` |
| **Applies To** | Group/Household |
| **Value Type** | Number |

![Variable form - basic info](/_images/en-us/config_guide/cel/quick_start/03-variable-form-basic.png)

### Step 4: Configure the source

Select **Aggregate** as the Source Type, then configure:

| Field | Value |
|-------|-------|
| **Source Type** | Aggregate |
| **Aggregate Target** | Members |
| **Aggregate Type** | Count |
| **Aggregate Filter** | `age_years(m.birthdate) < 5` |

![Variable form - aggregate configuration](/_images/en-us/config_guide/cel/quick_start/04-variable-aggregate-config.png)

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
2. Click **Rules** in the sidebar
3. Click **Expressions**

### Step 2: Create a new expression

1. Click **New** to create a new expression

![Expressions list view](/_images/en-us/config_guide/cel/quick_start/05-expressions-list.png)

### Step 3: Configure the expression

Fill in the basic information:

| Field | Value |
|-------|-------|
| **Name** | Priority Household |
| **Expression Type** | Filter |
| **Context Type** | Group/Household |
| **Output Type** | Boolean |

![Expression form - basic info](/_images/en-us/config_guide/cel/quick_start/06-expression-form-basic.png)

### Step 4: Enter the CEL expression

In the CEL editor, enter:

```cel
children_under_5_count >= 1
```

![CEL editor with expression](/_images/en-us/config_guide/cel/quick_start/07-cel-editor.png)

The editor provides:
- **Autocomplete**: Type `children` and press Ctrl+Space to see matching variables
- **Validation**: Errors appear as red underlines with explanations
- **Matching count**: Shows how many records match your expression

### Step 5: Test your expression (recommended)

1. Click the **Tests** tab
2. Click **Add a line** to add a test case
3. Select a test household from the registry
4. Set the expected result (True or False)
5. Click **Run Tests** to verify

![Expression test tab](/_images/en-us/config_guide/cel/quick_start/08-expression-tests.png)

### Step 6: Save and activate

1. Click **Save** to create the expression in Draft state
2. Click **Activate** to make it available for use

## How to know what data is available

The CEL editor provides tools to discover available data:

### Autocomplete

Type in the editor and press **Ctrl+Space** to see suggestions:
- Type `r.` to see fields on the current record
- Type a variable name to see matching variables
- Type a function name to see its signature

![CEL editor autocomplete](/_images/en-us/config_guide/cel/quick_start/09-autocomplete.png)

### Symbol browser

Click the **symbol browser icon** (sidebar button) to browse:
- Available symbols and their fields
- Active variables you can use
- Built-in functions with descriptions

![Symbol browser panel](/_images/en-us/config_guide/cel/quick_start/10-symbol-browser.png)

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
- Make sure the variable is **Active**, not Draft
- Check that **Applies To** matches your context (Individual vs Group)
- Verify you're using the **CEL Accessor** name, not the display name

**Expression validates but matches 0 records?**
- Check that you're testing against the correct registry type (Individual vs Group)
- Verify test data exists with the expected field values
- Try simplifying the expression to `true` first, then add conditions one at a time

**"Unknown symbol" error?**
- Use autocomplete (Ctrl+Space) to see available symbols
- Check that referenced variables are Active
- Verify the context matches (individual vs group profiles have different symbols)

**Can't activate a variable or expression?**
- You need **Studio Manager** permission to activate
- Check that all required fields are filled
- For aggregates, verify the filter expression is valid

## Next steps

- **Common patterns**: {doc}`cookbook`
- **Full syntax reference**: {doc}`syntax`
- **Debugging tips**: {doc}`troubleshooting`
- **Variable system details**: {doc}`variables`
