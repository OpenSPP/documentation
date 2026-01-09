---
openspp:
  doc_status: draft
  products: [core]
---

# Eligibility Rule Builder

This guide is for **implementers** building program eligibility rules visually. You should be comfortable with logic like "if this AND that" from tools like KoBoToolbox skip logic, but you don't need to write code expressions.

## What is Eligibility Rule Builder?

Eligibility Rule Builder lets you create program eligibility criteria using visual tools instead of writing CEL (Common Expression Language) expressions. Combine conditions based on registry fields, event data, group membership, and location to define who qualifies for your program.

## When to Use Eligibility Rule Builder

Use this tool when you need to define program eligibility criteria:

| Use Case | Example Rule |
|----------|--------------|
| Income targeting | Households with monthly income below $500 |
| Age-based programs | Elderly individuals aged 65 or older |
| Conditional cash transfers | Households with children under 5 AND attending school |
| Vulnerability targeting | Individuals with vulnerability score above 70 |
| Geographic targeting | Families living in specific districts |
| Multi-criteria programs | Low income AND (has disability OR elderly head of household) |

## Mental Model: Eligibility Rules

Think of eligibility rules like KoBoToolbox's "relevant" (skip logic) but for selecting program beneficiaries:

| In KoBoToolbox | In OpenSPP Eligibility |
|----------------|------------------------|
| Show question if age >= 18 | Include registrant if age >= 18 |
| Relevant: ${has_children} = 'yes' | Condition: Has children = Yes |
| Multiple conditions with "and" | All conditions must be true (AND) |
| Calculation based on previous answers | Calculation based on registry fields |

**Key difference**: Instead of controlling form questions, you're selecting who gets into a program.

## Before You Start

### Prerequisites

- **Studio Editor** or **Studio Manager** permissions
- Program already created (you'll link rules to programs)
- Understanding of:
  - What makes someone eligible for your program
  - Which registry fields contain relevant data
  - What event data (surveys) you collect

### Planning Your Rule

Decide:

1. **Program**: Which program is this for?
2. **Name**: Descriptive rule name
3. **Conditions**: What must be true? (income, age, location, events, etc.)
4. **Logic**: Must ALL conditions be true (AND logic)?
5. **Test criteria**: How many registrants should match?

### What Studio Can Build

Eligibility Rule Builder handles most common scenarios:

| ✓ Studio Can Build | ✗ Requires Developer |
|--------------------|---------------------|
| Registry field comparisons | Very complex nested OR/AND groups |
| Event data checks | Custom functions not in visual builder |
| Group membership rules | Performance-optimized rules for millions of records |
| Geographic targeting | Complex calculations across multiple records |
| Age calculations | Integration with external scoring systems |
| Score-based rules | |

## Creating an Eligibility Rule

### Step 1: Open Eligibility Rule Builder

1. Click **Studio** in the main menu
2. Click **Eligibility Rules**
3. Select a program from the dropdown (or click **+ New Rule**)

**Screenshot should show**: Studio Dashboard with Eligibility Rules card highlighted, then Eligibility Rule Builder view with program selector dropdown and rules list.

### Step 2: Create New Rule

Click **+ New Rule**

Enter rule details:

| Field | What to Enter | Example |
|-------|---------------|---------|
| **Rule Name** | Descriptive name | "Low Income Households with Children" |
| **Program** | Program this rule applies to | Cash Transfer Program 2024 |

**Screenshot should show**: New rule dialog with fields filled in.

### Step 3: Build Conditions

The rule builder shows:
- List of conditions
- "ALL of these conditions must be true" header
- Add Condition button
- Generated rule preview
- Test button

**Screenshot should show**: Rule builder interface as shown in spec with condition blocks.

#### Adding Your First Condition

Click **+ Add Condition**

Choose condition type:

| Condition Type | Use When | Example |
|----------------|----------|---------|
| **Registry Field** | Check registrant's data | Income < 500, Age >= 65 |
| **Event Data** | Check if event exists | Has Vulnerability Assessment in last year |
| **Event Value** | Check event field value | Vulnerability score > 70 |
| **Group Membership** | Check household status | Is member of household |
| **Location** | Check geographic area | Lives in District A or B |

**Screenshot should show**: Condition type selector showing the five options.

### Building Registry Field Conditions

**Example: Monthly Income Below 500**

1. Select **Registry Field** condition type
2. Configure:

| Setting | Select/Enter |
|---------|--------------|
| **Field** | Monthly Income |
| **Operator** | is less than |
| **Value** | 500 |

**Screenshot should show**: Registry field condition builder with dropdowns populated.

#### Available Operators

| Operator | Works With | Example |
|----------|------------|---------|
| **equals** | All types | Gender equals "Female" |
| **does not equal** | All types | Status does not equal "Exited" |
| **is greater than** | Numbers, dates | Age > 65 |
| **is less than** | Numbers, dates | Income < 500 |
| **is greater than or equal to** | Numbers, dates | Score >= 70 |
| **is less than or equal to** | Numbers, dates | Children <= 5 |
| **is empty** | All types | Phone number is empty |
| **is not empty** | All types | Email is not empty |
| **contains** | Text | Address contains "Manila" |
| **does not contain** | Text | Name does not contain "Test" |
| **is one of** | Selection | District is one of [A, B, C] |
| **is not one of** | Selection | Status is not one of [Exited, Suspended] |

### Building Event Data Conditions

**Example: Has Vulnerability Assessment in Last Year**

1. Select **Event Data** condition type
2. Configure:

| Setting | Select/Enter |
|---------|--------------|
| **Event Type** | Vulnerability Assessment |
| **Requirement** | (•) Has this event recorded |
| **Time Filter** | (•) In the last 365 days |

**Screenshot should show**: Event data condition builder with options selected.

#### Time Filter Options

| Filter | Use When | Example |
|--------|----------|---------|
| **In the last X days** | Recent events matter | Last 365 days, Last 30 days |
| **Ever (any time)** | Any historical event counts | Ever completed training |
| **In specific period** | Date range | Between Jan 1 - Dec 31, 2024 |

### Building Event Value Conditions

**Example: Vulnerability Score Greater Than 70**

1. Select **Event Value** condition type
2. Configure:

| Setting | Select/Enter |
|---------|--------------|
| **Event Type** | Vulnerability Assessment |
| **Field in event** | vulnerability_score |
| **Operator** | is greater than |
| **Value** | 70 |
| **Time Filter** | In the last 365 days |

**Screenshot should show**: Event value condition builder.

**Note**: This checks the field value within the most recent event of that type.

### Building Group Membership Conditions

**For Individual registrants**, check their household status:

| Condition | Use When |
|-----------|----------|
| **Is member of a group** | Person must be in a household |
| **Is head of household** | Person must be household head |
| **Group has at least X members** | Household must have minimum size |
| **Group has member matching...** | Complex: Someone in household matches criteria |

**Screenshot should show**: Group condition builder with options.

**Example: Is Head of Household**

```
Group Type: Household
Condition: (•) Is head of household
```

### Building Location Conditions

**Example: Lives in Specific Districts**

1. Select **Location** condition type
2. Configure:

| Setting | Select/Enter |
|---------|--------------|
| **Area Level** | District |
| **Operator** | is one of |
| **Areas** | [District A ×] [District B ×] [+ Add] |

**Screenshot should show**: Location condition builder with area tags.

## Combining Multiple Conditions

### Adding More Conditions

Click **+ Add Condition** for each additional criteria.

**Example Rule: Low Income Families with Children**

```
Rule: Low Income Households with Children
ALL of these conditions must be true:

┌─ Condition 1 ────────────────────────┐
│ Registry Field                       │
│ Monthly Income < 500                 │
└──────────────────────────────────────┘

┌─ Condition 2 ────────────────────────┐
│ Registry Field                       │
│ Number of Children > 0               │
└──────────────────────────────────────┘

┌─ Condition 3 ────────────────────────┐
│ Event Data                           │
│ Has Vulnerability Assessment         │
│ in last 365 days                     │
└──────────────────────────────────────┘
```

**Screenshot should show**: Rule builder with three conditions as shown above.

### Generated Rule Preview

As you build conditions, the system generates the actual CEL expression:

```
registrant.income < 500 &&
registrant.x_cst_num_children > 0 &&
has_event('vulnerability_assessment', within_days=365)
```

**Screenshot should show**: Generated rule panel showing CEL expression (read-only).

**You don't need to understand this code** - it's generated automatically from your visual conditions.

## Testing Your Rule

### Before Activating

Always test your rule:

1. Click **Test Rule**
2. System counts how many registrants match
3. Shows result: "Matches: 1,247 registrants"

**Screenshot should show**: Test results showing match count.

### Interpreting Results

| Result | What It Means | Action |
|--------|---------------|--------|
| **0 matches** | No one qualifies | Rules may be too strict - review conditions |
| **Expected number** | Rule works correctly | Proceed to activate |
| **Too many matches** | Rules may be too loose | Add more conditions |
| **Unexpected number** | Logic may be wrong | Review each condition carefully |

### Reviewing Sample Matches

Click **View Sample** to see registrants who match:

**Screenshot should show**: Sample matches list showing 10-20 registrants with key fields.

Check:
- Are these the right people?
- Do they meet all criteria?
- Any unexpected matches?

## Activating and Using Rules

### Activate the Rule

1. Review conditions and test results
2. Click **Save**
3. Click **Activate** (requires Studio Manager permission)

**Screenshot should show**: Rule detail view with "Activate" button.

### Link to Program

Rules are automatically linked to the program you selected when creating them.

To use the rule:

1. Go to **Programs → [Your Program]**
2. Go to **Eligibility** tab
3. Your rule appears in the eligibility manager
4. Configure when/how to apply the rule

**Screenshot should show**: Program detail view, Eligibility tab, showing the rule listed.

## Common Eligibility Patterns

### Low Income Households

```
Rule: Low Income Families
Program: Cash Transfer Program

Conditions:
1. Registry Field: Monthly Income <= 500
2. Registry Field: Is Active = Yes

Matches: 3,456 households
```

### Elderly Support Program

```
Rule: Elderly Individuals
Program: Senior Citizen Pension

Conditions:
1. Registry Field: Age >= 65
2. Registry Field: Receives Other Pension = No
3. Location: Lives in [Rural Districts]

Matches: 892 individuals
```

### Conditional Cash Transfer (Education)

```
Rule: Families with School-Age Children
Program: Education Conditional Transfer

Conditions:
1. Registry Field: Number of Children Ages 6-18 >= 1
2. Event Value: School Attendance Rate >= 80%
   (from "Monthly Compliance Check" event, last 90 days)
3. Registry Field: Monthly Income < 600

Matches: 2,145 households
```

### Vulnerability-Based Targeting

```
Rule: High Vulnerability Households
Program: Emergency Response

Conditions:
1. Event Value: Vulnerability Score >= 70
   (from "Vulnerability Assessment" event, last 365 days)
2. Group Membership: Is member of a household
3. Registry Field: Has Disability = Yes OR Number of Elderly >= 1

Matches: 1,523 households
```

**Note**: The last condition uses OR logic between disability and elderly. For complex OR logic, you may need developer help or create separate rules.

### Geographic Targeting

```
Rule: Flood-Affected Areas
Program: Disaster Relief

Conditions:
1. Location: Area is one of [District 5, District 7, District 12]
2. Event Data: Has "Damage Assessment" event in last 30 days
3. Registry Field: Housing Type = "Temporary Shelter" OR "Damaged"

Matches: 678 households
```

### Disability Inclusion

```
Rule: Persons with Disabilities
Program: Disability Support Grant

Conditions:
1. Registry Field: Has Disability = Yes
2. Registry Field: Disability Type is one of [Physical, Visual, Hearing]
3. Registry Field: Age >= 18
4. Event Data: Has "Disability Assessment" event ever

Matches: 234 individuals
```

## Managing Eligibility Rules

### View All Rules

**Studio → Eligibility Rules** shows all rules:

**Screenshot should show**: Eligibility rules list grouped by program.

| Column | Shows |
|--------|-------|
| **Name** | Rule name |
| **Conditions** | Number of conditions |
| **Status** | Draft or Active |
| **Matches** | Last test count (if tested) |

### Filter by Program

Use the program dropdown to see rules for specific programs.

### Edit a Rule

**For Draft rules**:
- Click the rule name
- Modify conditions
- Re-test
- Save

**For Active rules**:
- Cannot edit directly (program may be using it)
- Options:
  1. Deactivate → Edit → Test → Reactivate
  2. Create new version → Test → Activate → Deactivate old version

### Deactivate a Rule

**Warning**: Deactivating may affect program enrollment.

1. Open the rule
2. Click **Deactivate**
3. Confirm

**Impact**: Program will no longer use this rule for eligibility. Existing beneficiaries remain enrolled.

## Advanced Topics

### Complex OR Logic

Studio's default is AND logic (all conditions must be true).

For OR logic (any condition can be true):

**Simple OR - Use multiple rules**:
```
Rule 1: Elderly (Age >= 65)
Rule 2: Disabled (Has Disability = Yes)
Program uses: Rule 1 OR Rule 2
```

**Complex OR - Requires developer**:
```
(Income < 500 AND Children > 0) OR (Age >= 65 AND Lives Alone)
```

This level of complexity needs CEL expression written by developer.

### Calculated Fields

If you need to calculate values (like "total household income" from member incomes), you need:

1. Developer to create calculated field or variable
2. Then use that field in eligibility rules

### Dynamic Scoring

For PMT (Proxy Means Test) or complex scoring:

1. Use Event Type to collect assessment data
2. Calculate score in KoBoToolbox or external tool
3. Import score as event field
4. Use Event Value condition: Score >= threshold

### Time-Based Eligibility

Eligibility that changes over time:

```
Condition: Event Data
  Event Type: Monthly Compliance Check
  Time Filter: In the last 30 days

Result: Only registrants with recent compliance check are eligible
```

Run eligibility check monthly to update based on new events.

## Are You Stuck?

**Rule matches 0 registrants but should match many?**
- Check each condition individually - which one fails?
- Verify field names are correct
- Check that data actually exists (e.g., do registrants have income values?)
- Test with simpler conditions first, then add complexity

**Can't find a registry field in the condition builder?**
- Field must exist in the registry
- Custom fields must be Active (not Draft)
- Field must be searchable (check Field Builder settings)

**Event data conditions not working?**
- Verify event type is Active
- Check that registrants actually have events of that type
- Verify time filter (events may be older than filter allows)

**Need to check "this OR that"?**
- For simple OR: Create multiple rules
- For complex OR: Contact developer for CEL expression

**Rule matches wrong people?**
- Review each condition carefully
- Use "View Sample" to see who matched
- Check for missing conditions (e.g., forgot to exclude exited registrants)

**Getting errors about undefined fields?**
- Field may have been deleted or renamed
- Check that field names in conditions still exist
- Recreate the condition with current field

**Can't activate rule?**
- Need Studio Manager permission
- Make sure all conditions are valid
- Test the rule first

**Want to copy a rule to another program?**
Studio doesn't support copying rules directly. Create a new rule and manually rebuild conditions.

**How often should I run eligibility checks?**
This is configured in the program, not in the rule. Typically:
- One-time enrollment: Run once during enrollment period
- Conditional programs: Run monthly or quarterly
- Dynamic targeting: Run before each payment cycle

**Can eligibility rules automatically enroll people?**
No, rules select who is eligible. Enrollment is a separate process configured in the program.

**What happens to existing beneficiaries when I change a rule?**
Depends on program configuration:
- Re-run eligibility: Some may become ineligible
- One-time check: Rule change doesn't affect enrolled beneficiaries
- Ask administrator how your program handles this

**Can I test rules without affecting real data?**
Yes! Test Rule only counts matches - it doesn't enroll anyone or change any data.

## Field Reference

### Registry Fields You Can Use

**Standard Individual Fields**:
- age (calculated from birthdate)
- gender
- phone, email, address
- area_id (location)
- is_group (for checking if household)

**Standard Group Fields**:
- z_cst_num_members (household size)
- is_partial_group
- area_id

**Custom Fields**:
- Any fields created via Registry Field Builder
- Named like: x_cst_field_name

**To see all available fields**: Registry → Individuals → Click any record → See available fields

### Event Types You Can Use

- Any active event type from Event Type Designer
- Built-in event types from your system
- Check: Studio → Event Types for list

### Locations

- Areas defined in: Configuration → Locations → Areas
- Use the area hierarchy (Country → Region → District → etc.)

## Next Steps

- **Create event types for assessments**: {doc}`event_type_designer`
- **Add custom fields for targeting**: {doc}`registry_field_builder`
- **Build change request workflows**: {doc}`change_request_builder`
- **Return to Studio overview**: {doc}`overview`

## Further Learning

**Understanding CEL Expressions**: While Studio generates CEL automatically, understanding the basics can help:
- See {doc}`../cel/index` for CEL documentation
- Generated expressions are standard CEL - developers can enhance them
- Visual builder covers 80% of cases; CEL covers the remaining 20%

**Program Configuration**: Eligibility rules are just one part of program setup:
- See program configuration guides for enrollment, cycles, and entitlements
- Rules determine "who qualifies" - programs determine "what they receive"
