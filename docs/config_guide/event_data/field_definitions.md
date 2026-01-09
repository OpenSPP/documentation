---
openspp:
  doc_status: draft
  products: [core]
---

# Defining Event Fields

This guide is for **implementers** configuring custom fields for event types in OpenSPP Studio. You should be comfortable with form builders like KoboToolbox, but you don't need to write code.

## Mental Model

Event fields work like form questions:

| Concept | Equivalent | Example |
|---------|-----------|---------|
| **Field Definition** | Form question | "What is your monthly income?" |
| **Field Type** | Answer type | Number, Text, Yes/No |
| **Validation** | Answer rules | "Must be between 0 and 100,000" |
| **Visibility** | Skip logic | "Show if employment_status = Employed" |

## Field Types

### Available Field Types

| Type | Data Format | When to Use | Example |
|------|-------------|-------------|---------|
| **Text** | Short text (up to 255 chars) | Names, IDs, short notes | "Employment type" |
| **Long Text** | Multi-line text | Comments, descriptions | "Assessment notes" |
| **Integer** | Whole numbers | Counts, ages | Household size: `5` |
| **Decimal** | Numbers with decimals | Money, measurements | Income: `4500.50` |
| **Date** | Calendar date (YYYY-MM-DD) | Birthdates, verification dates | `2024-03-15` |
| **DateTime** | Date + time | Timestamps | `2024-03-15 14:30:00` |
| **Boolean** | True/False | Yes/No questions | Is employed: `true` |
| **Selection** | Pick one from list | Categories, statuses | Employment: "Employed" |
| **Multi-Select** | Pick multiple from list | Multiple categories | Crops: ["Maize", "Beans"] |
| **Link** | Reference to another record | Link to location, organization | Area: → res.partner |

## Adding Fields to Event Type

### Step 1: Open Event Type

Go to **Studio → Event Types** and open your event type (must be in Draft state).

### Step 2: Add Field

Click **Add Field** in the Fields tab.

### Step 3: Configure Basic Properties

| Property | Description | Example |
|----------|-------------|---------|
| **Label** | User-facing question text | "Monthly Income (USD)" |
| **Technical Name** | Internal field name (no spaces) | `monthly_income` |
| **Type** | Field type from list above | Decimal |
| **Required** | Must be filled? | Yes |
| **Help Text** | Guidance for data collectors | "Enter total monthly income from all sources" |
| **Sequence** | Display order (10, 20, 30...) | 10 |

### Step 4: Configure Type-Specific Settings

#### For Selection/Multi-Select Fields

Add options (one per line):

```
Employed
Unemployed
Self-employed
Student
Retired
```

**In CEL expressions, use the exact option text:**
```cel
event('survey').employment_status == 'Employed'
```

#### For Link Fields

| Setting | Value |
|---------|-------|
| **Link To** | Model to link to (e.g., `res.partner`, `spp.area`) |
| **Link Domain** | Filter expression (e.g., `[('is_location', '=', True)]`) |

#### For Decimal/Integer Fields

Set validation ranges (see Validation section below).

## Field Validation

Validation rules ensure data quality before events are saved.

### Validation Types

#### Range Validation (Numbers and Dates)

**For Integer/Decimal fields:**

| Setting | Value | Effect |
|---------|-------|--------|
| **Validation** | Value Range | Enables min/max validation |
| **Minimum Value** | 0 | Income cannot be negative |
| **Maximum Value** | 100000 | Income cannot exceed 100,000 |
| **Error Message** | "Income must be between 0 and 100,000" | Shown on validation failure |

**For Date fields:**

| Setting | Value | Effect |
|---------|-------|--------|
| **Validation** | Value Range | Enables date range validation |
| **Minimum Value** | 2020-01-01 | No dates before 2020 |
| **Maximum Value** | today | No future dates |

#### Pattern Validation (Text)

**For Text fields:**

| Setting | Value | Effect |
|---------|-------|--------|
| **Validation** | Pattern Match | Enables regex validation |
| **Pattern** | `^[A-Z]{2}[0-9]{6}$` | Must match format (e.g., ID number) |
| **Error Message** | "ID must be 2 letters + 6 digits" | Shown on validation failure |

**Common Patterns:**

| Pattern | Matches | Example |
|---------|---------|---------|
| `^[A-Z]{2}[0-9]{6}$` | 2 uppercase letters + 6 digits | AB123456 |
| `^\d{10}$` | Exactly 10 digits | 0123456789 |
| `^[0-9]{3}-[0-9]{3}-[0-9]{4}$` | Phone format (XXX-XXX-XXXX) | 555-123-4567 |
| `^[a-zA-Z\s]+$` | Letters and spaces only | John Doe |

## Conditional Visibility

Show or hide fields based on other field values (like skip logic in surveys).

### Step 1: Enable Conditional Visibility

| Setting | Value |
|---------|-------|
| **Visibility** | Conditional |

### Step 2: Configure Condition

| Setting | Value | Description |
|---------|-------|-------------|
| **Show When Field** | Select another field in this event type | The field to check |
| **Condition** | Is Set / Not Set / Equals / Not Equals | How to check the field |
| **Value** | (depends on condition) | Value to compare (for Equals/Not Equals) |

### Examples

#### Example 1: Show Income Source if Employed

**Field:** `income_source` (Text)

| Setting | Value |
|---------|-------|
| **Visibility** | Conditional |
| **Show When Field** | `employment_status` |
| **Condition** | Equals |
| **Value** | Employed |

**Result:** The "Income Source" field only appears if "Employment Status" = "Employed"

#### Example 2: Show Disability Details if Has Disability

**Field:** `disability_type` (Selection)

| Setting | Value |
|---------|-------|
| **Visibility** | Conditional |
| **Show When Field** | `has_disability` |
| **Condition** | Equals |
| **Value** | true |

#### Example 3: Show Rejection Reason if Assessment Failed

**Field:** `rejection_reason` (Long Text)

| Setting | Value |
|---------|-------|
| **Visibility** | Conditional |
| **Show When Field** | `assessment_result` |
| **Condition** | Equals |
| **Value** | Failed |

## Field Configuration Examples

### Example 1: Income Assessment Fields

| Label | Technical Name | Type | Required | Validation |
|-------|---------------|------|----------|------------|
| Monthly Income (USD) | `monthly_income` | Decimal | Yes | Range: 0 - 100,000 |
| Household Size | `household_size` | Integer | Yes | Range: 1 - 50 |
| Employment Status | `employment_status` | Selection | Yes | Employed / Unemployed / Self-employed |
| Income Source | `income_source` | Text | No | Visible if employed |
| Verification Date | `verification_date` | Date | Yes | Range: 2020-01-01 to today |

### Example 2: Disability Assessment Fields

| Label | Technical Name | Type | Required | Validation |
|-------|---------------|------|----------|------------|
| Has Disability | `has_disability` | Boolean | Yes | - |
| Disability Type | `disability_type` | Multi-Select | Conditional | Visible if has_disability |
| Severity Level | `severity_level` | Selection | Conditional | Low / Medium / High / Severe |
| Support Needed | `support_needed` | Long Text | No | - |
| Assessment Score | `assessment_score` | Integer | Yes | Range: 0 - 100 |

Disability Type options:
```
Physical
Visual
Hearing
Cognitive
Psychosocial
Multiple
```

### Example 3: Farm Visit Fields

| Label | Technical Name | Type | Required | Validation |
|-------|---------------|------|----------|------------|
| Farm Size (hectares) | `hectares` | Decimal | Yes | Range: 0.1 - 1000 |
| Certified Farmer | `certified` | Boolean | Yes | - |
| Crops Grown | `crops` | Multi-Select | Yes | Maize / Rice / Beans / Vegetables |
| Livestock Count | `livestock_count` | Integer | No | Range: 0 - 10000 |
| Pest Infestation | `pest_infestation` | Boolean | Yes | - |
| Inspector Notes | `inspector_notes` | Long Text | No | - |

## Field Naming Best Practices

### Technical Names

**Good:**
- `monthly_income`
- `household_size`
- `has_disability`
- `assessment_date`

**Bad:**
- `Monthly Income` (has spaces)
- `income$` (special characters)
- `1_income` (starts with number)
- `class` (reserved word)

**Rules:**
- Use lowercase letters
- Use underscores instead of spaces
- Start with a letter
- No special characters
- Keep it descriptive but concise

### Labels (User-Facing)

**Good:**
- "Monthly Income (USD)"
- "Does the household have access to clean water?"
- "Number of children under 5"

**Bad:**
- "income" (too terse)
- "monthly_income" (technical name, not friendly)
- "Enter the total monthly income from all sources including employment, farming, and transfers" (too verbose - put this in help text)

## Common Patterns

### Pattern 1: Yes/No with Conditional Follow-Up

```
Field 1:
  Label: Has disability
  Type: Boolean
  Required: Yes

Field 2:
  Label: Disability type
  Type: Multi-Select
  Required: No
  Visibility: Conditional on has_disability = true
```

### Pattern 2: Numeric Range with Validation

```
Field:
  Label: Household size
  Type: Integer
  Required: Yes
  Validation: Range (1 to 50)
  Error: "Household size must be between 1 and 50"
```

### Pattern 3: Categorical with Other Option

```
Field 1:
  Label: Employment status
  Type: Selection
  Options: Employed / Unemployed / Self-employed / Other
  Required: Yes

Field 2:
  Label: Please specify
  Type: Text
  Required: No
  Visibility: Conditional on employment_status = 'Other'
```

### Pattern 4: ID Number with Format Validation

```
Field:
  Label: National ID Number
  Type: Text
  Required: Yes
  Validation: Pattern Match
  Pattern: ^[A-Z]{2}[0-9]{6}$
  Error: "ID must be 2 uppercase letters followed by 6 digits"
```

## Reordering Fields

Fields are displayed in **sequence order** (lowest to highest).

To reorder:
1. Edit each field's **Sequence** value
2. Use increments of 10 (10, 20, 30...) to allow inserting fields later
3. Save changes

## Deleting Fields

**Before activation:**
- You can delete any field

**After activation:**
- You can only delete fields that have no data
- System prevents deletion if any event records contain data for this field

**Workaround:**
- Instead of deleting, mark field as **not required** and remove from entry forms

## Field Defaults

Some fields can have default values:

| Type | Default Options |
|------|----------------|
| **Date** | Today, Custom date |
| **Boolean** | True, False |
| **Integer/Decimal** | Numeric value |
| **Selection** | One of the options |

**Set default in:**
- Field configuration → Default Value

## Copying Fields from Templates

Instead of creating fields manually, you can use templates:

1. Click **Apply Template** when creating an event type
2. Select template category (Survey, Health, Economic, etc.)
3. Choose specific template
4. Review and customize fields

See {doc}`event_types` for available templates.

## Testing Field Configuration

Before deploying to production:

1. **Create test event** with sample data
2. **Test validation** - try invalid values (should be rejected)
3. **Test visibility** - check conditional fields show/hide correctly
4. **Test in mobile app** if using ODK/Kobo integration
5. **Test in CEL** - verify field data is accessible in expressions

## Next Steps

1. {doc}`event_types` - Configure event type lifecycle and settings
2. {doc}`odk_kobo` - Map fields to ODK/KoboToolbox forms
3. {doc}`../cel/variables` - Reference event fields in eligibility rules

## Are You Stuck?

**Field not appearing in entry form?**

Check:
- Is the field marked as required but has no default?
- Is it conditionally visible but the condition isn't met?
- Did you save the field configuration?
- Did you activate the event type after adding the field?

**Validation not working?**

Make sure:
- Validation type is set (not "None")
- Min/max or pattern is configured
- Error message is set
- Event type is re-activated after changes

**Conditional visibility not working?**

Check:
- Both fields are in the same event type
- The "Show When Field" is filled before the conditional field in sequence
- The condition value matches exactly (case-sensitive for selections)
- Event type is activated after adding visibility rules

**Can't use special characters in technical name?**

Technical names must be valid field names (letters, numbers, underscores only). Use the **Label** for special characters and spaces.

**How do I make a field show only for specific programs?**

Field visibility is per-event-type, not per-program. If you need program-specific fields, create separate event types and link them to specific programs.

**Pattern validation keeps rejecting valid values?**

Test your regex pattern in a regex tester (regex101.com) first. Remember:
- Use `^` for start of string and `$` for end
- Escape special regex characters with `\`
- Test with sample valid and invalid values
