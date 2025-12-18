---
openspp:
  doc_status: draft
---

# CEL Quick Start

This guide is for **implementers** who want to start writing CEL expressions in OpenSPP.

You should be comfortable with "logic builders" (like CommCare or Kobo configuration) but you don't need Python experience.

## What You'll Learn

By the end of this guide, you will:
- Understand the three core concepts (symbols, variables, expressions)
- Create your first variable
- Create your first expression
- Know how to discover what data is available

## Prerequisites

- Access to OpenSPP with **Implementer** or **Administrator** role
- The CEL modules installed (standard in OpenSPP V2)
- Allow 15 minutes

## The Three Core Concepts

### 1. Symbols

Symbols are the data available in a given context. The most common symbols:

| Symbol | What It Represents | Available In |
|--------|-------------------|--------------|
| `me` | Current record (registrant, ticket, etc.) | Most screens |
| `members` | Household members | Group/household context |
| `enrollments` | Program memberships | Registry context |
| `entitlements` | Entitlement records | Registry context |
| `events` | Event data records | When event integration installed |

```{note}
Some older examples use `r` instead of `me`. Both may work, but prefer `me` in new expressions.
```

### 2. Variables

Variables are named data points you define once and reuse everywhere:

| Variable Type | Example | Use Case |
|--------------|---------|----------|
| Constant | `poverty_line = 10000` | Threshold values |
| Aggregate | `children_under_5_count` | Computed from household |
| Field mapping | `has_disability` | Maps to model field |
| External | `external_score` | From external system |

### 3. Expressions

Expressions are reusable rules that combine variables and symbols:

```cel
children_under_5_count >= 1 and household_income < poverty_line
```

## Example A: Create a Variable

**Goal**: Create a variable that counts children under 5 in a household.

### Step 1: Navigate to Variables

1. Go to **Studio → Variables**
2. Click **Create**

### Step 2: Configure the Variable

| Field | Value |
|-------|-------|
| Name | Children Under 5 Count |
| CEL Accessor | `children_under_5_count` |
| Applies To | Group/Household |
| Source Type | Aggregate |
| Aggregate Target | Members |
| Aggregate Type | Count |
| Filter | `age_years(m.birthdate) < 5` |

### Step 3: Activate

1. Click **Save**
2. Click **Activate**

Now you can use `children_under_5_count` in any expression that applies to groups/households.

## Example B: Create an Expression

**Goal**: Create an expression that flags "priority households" (those with children under 5).

### Step 1: Navigate to Expressions

1. Go to **Studio → Expressions**
2. Click **Create**

### Step 2: Configure the Expression

| Field | Value |
|-------|-------|
| Name | Priority Household |
| Type | Eligibility |
| Context | Group/Household |
| Output Type | Yes/No (Boolean) |

### Step 3: Enter the Expression

In the CEL editor, enter:

```cel
children_under_5_count >= 1
```

### Step 4: Test (Recommended)

1. Click the **Tests** tab
2. Click **Add Test**
3. Select a test household
4. Set expected result
5. Run test to verify

### Step 5: Activate

1. Click **Save**
2. Click **Activate** (or follow your deployment's publish workflow)

## How to Know What Data Is Available

The CEL editor provides tools to discover available data:

### Autocomplete

Type `me.` and the editor suggests available fields.

### Symbol Browser

Click the symbol browser icon to see:
- Available profiles
- Symbols and their fields
- Available variables
- Built-in functions

### Validation

The editor shows errors inline:
- Unknown symbols highlighted
- Syntax errors explained
- Type mismatches flagged

## Common Mistakes

| Mistake | Problem | Fix |
|---------|---------|-----|
| `enrolled` | Unquoted string | `"enrolled"` |
| `True` | Wrong case | `true` |
| `AND` | Wrong case | `and` |
| `birthdate` | Missing context | `me.birthdate` or `m.birthdate` |

## Next Steps

- **Common patterns**: {doc}`cookbook`
- **Full syntax reference**: {doc}`syntax`
- **Debugging tips**: {doc}`troubleshooting`
- **Variable system details**: {doc}`variables`
