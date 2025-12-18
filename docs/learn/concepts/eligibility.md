---
openspp:
  doc_status: draft
---

# Eligibility

Eligibility is the process of determining who qualifies to receive benefits from a social protection program. It answers the fundamental question: "Who should we serve?"

**For:** All audiences

## What is Eligibility?

In social protection, eligibility defines the criteria that individuals, families, or groups must meet to qualify for program enrollment and benefits. These criteria ensure that programs reach their intended beneficiaries and allocate limited resources to those who need them most.

For example, a cash transfer program for vulnerable families might require:
- Household income below a certain threshold
- Presence of children under a specific age
- Residence in a particular geographic area

Eligibility rules transform program policy into concrete, measurable conditions that the system can evaluate automatically.

## Why Eligibility Matters

Well-designed eligibility criteria are crucial for several reasons:

**Targeting Accuracy**: They help programs reach the intended population and minimize inclusion errors (enrolling those who don't qualify) and exclusion errors (missing those who do).

**Transparency**: Clear criteria make programs fair and predictable. Beneficiaries understand why they qualify or don't qualify.

**Efficiency**: Automated eligibility checking reduces manual review time and enables programs to scale.

**Accountability**: Documented criteria provide an audit trail and help demonstrate program integrity.

## Types of Eligibility Criteria

Social protection programs typically use one or more of these criteria types:

### Demographic Criteria

These criteria are based on personal characteristics:

- **Age**: Seniors over 60, children under 5, youth between 15-24
- **Gender**: Programs specifically targeting women or girls
- **Disability Status**: Support for persons with disabilities
- **Family Composition**: Single parents, orphaned children, large families

**Example**: "All individuals aged 60 years or older"

### Geographic Criteria

These criteria target specific locations:

- **Administrative Boundaries**: Provinces, districts, municipalities
- **Urban vs Rural**: Programs for rural smallholders or urban informal workers
- **Special Zones**: Conflict-affected areas, disaster zones, high-poverty regions

**Example**: "Households residing in the Northern Region"

### Economic Criteria

These criteria assess financial need:

- **Income Level**: Below poverty line, earning less than minimum wage
- **Asset Ownership**: Land size, livestock count, vehicle ownership
- **Employment Status**: Unemployed, informal workers, seasonal laborers
- **Vulnerability Scores**: Proxy means test (PMT), social welfare development index (SWDI)

**Example**: "Households with monthly income below 10,000 PHP"

### Categorical Criteria

These criteria are based on specific circumstances or affiliations:

- **Program Participation**: Already enrolled in another program, past beneficiaries
- **Household Events**: Recent births, deaths, illness, job loss
- **Registration Status**: Holders of specific IDs, registered with certain agencies
- **Special Categories**: Veterans, refugees, migrant workers

**Example**: "Families with at least one child born in the past 12 months"

## Combined Criteria

Most programs combine multiple criteria types using logical operators:

- **AND Logic**: Must meet all conditions (more restrictive)
  - Example: "Households in the Northern Region AND with income below 10,000 PHP"

- **OR Logic**: Must meet at least one condition (more inclusive)
  - Example: "Individuals over 60 OR persons with disabilities"

- **Complex Logic**: Nested conditions with multiple operators
  - Example: "(Households with children under 5 AND income below 10,000) OR (Elderly households with income below 15,000)"

## Eligibility in OpenSPP

OpenSPP implements eligibility through a flexible **Eligibility Manager** system that allows programs to define, test, and apply eligibility rules.

### The Eligibility Manager

Each program has an **Eligibility Manager** that controls how eligibility is determined. The manager:

1. **Defines the rules**: What conditions must registrants meet?
2. **Evaluates registrants**: Which individuals or groups match the criteria?
3. **Returns results**: A list of eligible registrants ready for enrollment
4. **Supports testing**: Preview who qualifies before enrolling

Think of the Eligibility Manager as the program's "admission criteria" - it's the gatekeeper that decides who gets in.

### Different Eligibility Methods

OpenSPP supports three main methods for defining eligibility, each suited to different use cases:

#### 1. Tag-Based Eligibility

**Best for**: Simple inclusion/exclusion using predefined categories

**How it works**: Registrants are tagged with labels (e.g., "Elderly," "Disabled," "Urban Poor"). The eligibility manager selects everyone with specific tags.

**Example**: "Enroll all registrants tagged as 'Vulnerable Household'"

**Advantages**:
- Very simple to set up
- Fast to evaluate
- Easy to understand

**Limitations**:
- Tags must be assigned beforehand
- Cannot evaluate complex conditions
- Limited flexibility

#### 2. SQL-Based Eligibility

**Best for**: Complex queries requiring direct database access

**How it works**: Write SQL queries that select eligible registrants from the database.

**Example**:
```sql
SELECT id FROM res_partner
WHERE household_income < 10000
AND id IN (SELECT parent_id FROM res_partner WHERE age < 5)
```

**Advantages**:
- Maximum flexibility
- Can express any logic
- Efficient for complex queries

**Limitations**:
- Requires SQL knowledge
- Less portable across deployments
- Harder to test and maintain

#### 3. CEL Expression-Based Eligibility (Default)

**Best for**: Most eligibility scenarios, especially when using Studio configuration

**How it works**: Write expressions using the Common Expression Language (CEL) that evaluate to true/false for each registrant.

**Example**: `household_income < 10000 && children_under_5 >= 1`

**Advantages**:
- Powerful yet accessible to implementers
- Can reference Studio variables
- Built-in validation and testing
- Portable across deployments

**Limitations**:
- Requires learning CEL syntax
- Very complex logic might need SQL instead

Most programs use CEL-based eligibility because it balances power and accessibility.

## How Eligibility Verification Works

### When Eligibility is Checked

Eligibility verification typically happens at these key moments:

**1. Program Enrollment**

When preparing a program cycle, the system evaluates all registrants against the eligibility criteria to determine who can be enrolled as beneficiaries.

**2. Manual Verification**

Administrators can manually trigger eligibility checks to preview who would qualify before creating a cycle.

**3. Re-verification**

Some programs periodically re-check eligibility to ensure beneficiaries still qualify. This might happen:
- At the start of each new cycle
- After a specific time period
- When registrant data changes

### The Evaluation Process

Here's what happens when OpenSPP evaluates eligibility:

1. **Load Criteria**: The system retrieves the eligibility rules from the program's Eligibility Manager

2. **Identify Target Population**: Determine which registrants to evaluate (individuals vs groups/households, geographic scope, etc.)

3. **Evaluate Each Registrant**: For each registrant, the system:
   - Loads their current data
   - Applies the eligibility expression or query
   - Determines if they meet the criteria (true/false)

4. **Return Eligible Set**: The system produces a list of eligible registrants

5. **Create Preview or Enrollment**: Depending on the action, the system either shows a preview or proceeds with enrollment

### Performance Considerations

For programs with millions of registrants, eligibility evaluation must be efficient. OpenSPP optimizes this through:

- **Database-level filtering**: Most criteria are converted to database queries that run directly on PostgreSQL
- **Indexed fields**: Common criteria fields (age, location, income) are indexed for fast lookup
- **Batch processing**: Large evaluations are processed in chunks
- **Caching**: Results can be cached when registrant data hasn't changed

## Common Eligibility Patterns

Here are real-world examples of eligibility criteria:

### Age-Based Programs

**Child Grant**: Children under 18 years
```cel
age_years(r.birthdate) < 18
```

**Old Age Pension**: Seniors 60 and above
```cel
age_years(r.birthdate) >= 60
```

**Youth Employment Program**: Ages 18-35
```cel
age_years(r.birthdate) >= 18 && age_years(r.birthdate) <= 35
```

### Household Composition Programs

**Single Parent Support**: Households with one adult and children
```cel
adult_count == 1 && children_count > 0
```

**Large Family Assistance**: Families with 4+ children
```cel
children_count >= 4
```

**Families with Young Children**: At least one child under 5
```cel
children_under_5 >= 1
```

### Economic Vulnerability Programs

**Below Poverty Line**: Income-based targeting
```cel
household_income < 10000
```

**Multidimensional Poverty**: Using a composite score
```cel
vulnerability_score >= 70
```

**Unemployed Heads of Household**
```cel
employment_status == "unemployed" && is_head_of_household
```

### Geographic Targeting

**Regional Program**: Specific administrative area
```cel
r.area_id.code in ["REGION_1", "REGION_2"]
```

**Rural Farmers**: Agricultural areas only
```cel
r.area_id.area_type == "rural" && occupation == "farmer"
```

**Urban Informal Sector**: City-based workers
```cel
r.area_id.area_type == "urban" && employment_type == "informal"
```

### Combined Criteria

**Comprehensive Vulnerability**: Multiple conditions
```cel
(household_income < 10000 && children_under_5 >= 1) ||
(elderly_count >= 1 && household_income < 15000) ||
(disabled_count >= 1)
```

## Eligibility vs Compliance

It's important to distinguish between two related concepts:

**Eligibility**: Determines who qualifies to **enter** the program
- Evaluated before enrollment
- Answers: "Who should be enrolled?"

**Compliance**: Determines who remains **compliant** within the program
- Evaluated during program cycles
- Answers: "Who should continue receiving benefits?"

Example: A program might require:
- **Eligibility**: Household income below 10,000 PHP (to enroll)
- **Compliance**: Attend monthly health check-ups (to remain in good standing)

Both use similar technical mechanisms (CEL expressions, SQL queries) but serve different purposes in the program lifecycle.

## Testing Eligibility Rules

Before deploying eligibility criteria to a live program, it's critical to test them:

### Preview Functionality

OpenSPP provides preview tools that show:
- How many registrants currently meet the criteria
- A sample list of who would be selected
- Which registrants are borderline cases

### Test Cases

Create test cases with known registrants:
- **Should qualify**: Registrants that clearly meet criteria
- **Should not qualify**: Registrants that clearly don't meet criteria
- **Edge cases**: Registrants on the boundary (just above/below threshold)

### Iterative Refinement

Testing often reveals issues:
- Criteria too strict (excludes intended beneficiaries)
- Criteria too loose (includes unintended beneficiaries)
- Data quality problems (missing or incorrect values)

Refine your criteria based on test results before going live.

## Best Practices

### Keep Criteria Clear and Documented

Document the policy intent behind each criterion. Future administrators need to understand not just what the rule is, but why it exists.

### Use Variables for Complex Calculations

Rather than embedding complex logic directly in eligibility expressions, create reusable variables in Studio that can be tested independently.

### Plan for Data Quality

Eligibility is only as good as your data. Ensure that:
- Required fields are collected during registration
- Data is validated at entry
- Regular data quality audits are conducted

### Consider the Beneficiary Experience

Clear criteria help beneficiaries understand:
- Why they were selected or not selected
- What would make them eligible in the future
- How to appeal incorrect determinations

### Balance Precision and Practicality

Highly complex criteria might be theoretically precise but difficult to implement, explain, or maintain. Sometimes simpler criteria with regular manual review work better than overly complex automated rules.

## Learn More

For hands-on guidance on configuring eligibility:

- **Configuration**: {doc}`/config_guide/eligibility/index` - Set up eligibility managers and rules
- **CEL Expressions**: {doc}`/config_guide/cel/index` - Write and test eligibility expressions
- **First Program Tutorial**: {doc}`/get_started/first_program/04_configure_eligibility` - Step-by-step eligibility setup
- **Technical Reference**: {doc}`/technical_reference/programs/eligibility_manager` - Developer API documentation

## Summary

Eligibility is the foundation of targeted social protection programs. It translates program policy into concrete criteria that determine who qualifies for benefits. OpenSPP provides flexible tools - tag-based, SQL-based, and CEL expression-based methods - to implement eligibility rules that range from simple to highly complex.

Well-designed eligibility criteria ensure programs reach their intended beneficiaries, operate efficiently, and maintain transparency and accountability. Testing and refining criteria before deployment, combined with good data quality, are essential for successful program implementation.
