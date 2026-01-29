---
openspp:
  doc_status: draft
  products: [core]
---

# Eligibility

Eligibility determines who qualifies for a social protection program. It's the set of rules that filter the registry population down to those who should receive benefits.

**For:** All audiences

## What is eligibility?

Eligibility criteria define the conditions a registrant must meet to participate in a program. These criteria translate policy decisions into concrete rules that OpenSPP can evaluate automatically.

**Examples of eligibility criteria:**

| Program Type | Eligibility criteria |
|-------------|---------------------|
| Old age pension | Age 60 or older |
| Child grant | Households with children under 5 |
| Poverty assistance | PMT score below threshold |
| Disability support | Certified disability status |
| Geographic targeting | Residence in specific districts |

## Why eligibility matters

Proper eligibility determination ensures:

| Goal | How eligibility helps |
|------|----------------------|
| **Targeting accuracy** | Benefits reach intended populations |
| **Fairness** | Consistent rules applied to all |
| **Accountability** | Clear, auditable selection criteria |
| **Efficiency** | Automated filtering reduces manual work |
| **Budget control** | Predictable beneficiary counts |

## Types of eligibility criteria

### Demographic criteria

Based on individual or household characteristics:

| Criterion | Example rule |
|-----------|-------------|
| **Age** | `age >= 60` (elderly) or `age < 18` (children) |
| **Gender** | `gender == 'female'` for maternal programs |
| **Disability** | `has_disability == true` |
| **Household size** | `household_size >= 4` (large families) |
| **Dependency ratio** | `dependents / working_adults > 2` |

### Economic criteria

Based on income, assets, or poverty indicators:

| Criterion | Example rule |
|-----------|-------------|
| **Income** | `monthly_income < poverty_line` |
| **PMT score** | `pmt_score < 25` (proxy means test) |
| **Asset ownership** | `owns_land == false` |
| **Employment** | `employment_status == 'unemployed'` |

### Geographic criteria

Based on location:

| Criterion | Example rule |
|-----------|-------------|
| **Administrative area** | `area_id in target_districts` |
| **Rural/Urban** | `area_type == 'rural'` |
| **Disaster zone** | `area_id in affected_areas` |

### Categorical criteria

Based on specific conditions or status:

| Criterion | Example rule |
|-----------|-------------|
| **Orphan status** | `is_orphan == true` |
| **Refugee status** | `registration_type == 'refugee'` |
| **School enrollment** | `enrolled_in_school == true` |
| **Health condition** | `has_chronic_illness == true` |

### Composite criteria

Combining multiple conditions:

```
# Elderly women in rural areas
age >= 60 AND gender == 'female' AND area_type == 'rural'

# Large poor households with children
household_size >= 5 AND pmt_score < 20 AND has_children_under_5 == true

# Working-age adults without employment
age >= 18 AND age < 60 AND employment_status == 'unemployed'
```

## Eligibility in OpenSPP

### How it works

```{mermaid}
graph TD
    R[Registry Population] --> E[Eligibility Manager]
    E --> |Apply criteria| F[Filter registrants]
    F --> |Matching| Q[Qualified registrants]
    F --> |Not matching| NQ[Not qualified]
    Q --> P[Program enrollment]

    style R fill:#e3f2fd
    style E fill:#fff3e0
    style Q fill:#e8f5e9
    style NQ fill:#ffebee
```

1. **Registry data** provides the population to evaluate
2. **Eligibility Manager** applies configured criteria
3. **Matching registrants** become eligible for enrollment
4. **Non-matching registrants** are marked as not eligible

### Eligibility manager

The Eligibility Manager is a configurable component that controls how eligibility is determined. OpenSPP supports multiple eligibility approaches:

| Manager type | Description | Best for |
|-------------|-------------|----------|
| **Default (Domain-based)** | Uses Odoo domain filters | Simple criteria |
| **CEL Expression** | Uses Common Expression Language | Complex rules |
| **Area-based** | Targets specific administrative areas | Geographic targeting |
| **Custom** | Developer-defined logic | Specialized requirements |

### Domain-based eligibility

The default eligibility manager uses Odoo domain syntax:

```python
# Households in specific districts
[('area_id', 'in', [district_1_id, district_2_id])]

# Individuals over 60
[('birthdate', '<=', '1964-01-01')]

# Groups with more than 3 members
[('z_ind_grp_num_individuals', '>=', 3)]
```

**Advantages:**
- Simple to configure
- No coding required
- Fast evaluation

**Limitations:**
- Cannot access related records easily
- Limited to field comparisons
- No complex calculations

### CEL-based eligibility

For complex criteria, OpenSPP supports CEL (Common Expression Language):

```cel
# Age-based eligibility
age_years(me.birthdate) >= 60

# Gender and age combined
me.gender == 'female' and age_years(me.birthdate) >= 18

# Household composition check
members.exists(m, age_years(m.birthdate) < 5)

# Using computed metrics
metric('household.pmt_score') < 25

# Complex household criteria
members.filter(m, age_years(m.birthdate) < 18).size() >= 2
```

**CEL features:**

| Feature | Description | Example |
|---------|-------------|---------|
| **`me`** | Current registrant context | `me.gender == 'female'` |
| **`members`** | Household members (for groups) | `members.size() >= 3` |
| **`age_years()`** | Calculate age from date | `age_years(me.birthdate) >= 60` |
| **`metric()`** | Access computed variables | `metric('pmt_score') < 25` |
| **`exists()`** | Check if any member matches | `members.exists(m, m.has_disability)` |
| **`filter()`** | Get members matching condition | `members.filter(m, m.age < 18)` |

### Geographic targeting

The area-based eligibility manager simplifies geographic targeting:

| Configuration | Description |
|--------------|-------------|
| **Admin areas** | Select target districts, villages, etc. |
| **Area types** | Target by area classification |
| **Nested areas** | Include child areas automatically |

## Eligibility workflow

### At program level

```{mermaid}
stateDiagram-v2
    direction LR
    [*] --> Import: Import eligible registrants
    Import --> Draft: Create draft memberships
    Draft --> Verify: Verify eligibility
    Verify --> Enrolled: Passes criteria
    Verify --> NotEligible: Fails criteria
    Enrolled --> [*]
    NotEligible --> Draft: Re-evaluate
```

1. **Import** - Find registrants matching criteria from registry
2. **Draft** - Create draft program memberships
3. **Verify** - Run eligibility check against current data
4. **Enrolled/Not eligible** - Update status based on result

### At cycle level

Each cycle can also verify eligibility:

1. **Copy from program** - Bring enrolled members into cycle
2. **Verify cycle eligibility** - Re-check against current data
3. **Prepare entitlements** - Only for eligible cycle members

This allows for:
- Removing members who no longer qualify
- Adding newly eligible members
- Updating status based on changed circumstances

## Multiple eligibility managers

A program can have multiple eligibility managers that work together:

```{mermaid}
graph LR
    R[Registrants] --> E1[Manager 1:<br/>Age filter]
    E1 --> E2[Manager 2:<br/>Area filter]
    E2 --> E3[Manager 3:<br/>PMT filter]
    E3 --> Q[Qualified]

    style E1 fill:#e3f2fd
    style E2 fill:#fff3e0
    style E3 fill:#f3e5f5
```

Managers are applied in sequence—a registrant must pass all managers to qualify.

**Use cases for multiple managers:**

| Scenario | Manager setup |
|----------|--------------|
| **Layered targeting** | Area → PMT score → Household composition |
| **Phased rollout** | Core criteria → Additional filters per phase |
| **Complex programs** | Different criteria for different benefit components |

## Eligibility verification

### When to verify

| Timing | Purpose |
|--------|---------|
| **Initial enrollment** | Determine who qualifies |
| **Each cycle** | Confirm continued eligibility |
| **After data updates** | Reflect changed circumstances |
| **On demand** | Manual re-verification |

### Verification results

| Result | Meaning | Next Steps |
|--------|---------|------------|
| **Passes** | Meets all criteria | Proceed with enrollment/benefits |
| **Fails** | Doesn't meet criteria | Mark as not eligible |
| **Pending** | Awaiting data | Request missing information |

## Best practices

### Designing eligibility criteria

1. **Start simple** - Begin with core targeting criteria
2. **Be specific** - Clear rules are easier to audit
3. **Consider data availability** - Only use data you have
4. **Plan for updates** - Circumstances change over time
5. **Document rationale** - Record why criteria were chosen

### Configuration tips

| Tip | Reason |
|-----|--------|
| **Test with sample data** | Verify criteria work as expected |
| **Preview counts** | CEL manager shows matching count |
| **Use progressive refinement** | Add criteria incrementally |
| **Monitor exclusion rates** | High exclusion may indicate issues |

### Common pitfalls

| Pitfall | Solution |
|---------|----------|
| **Missing data causes exclusion** | Handle null values explicitly |
| **Overly complex criteria** | Simplify or split into multiple managers |
| **Criteria not updated** | Schedule periodic reviews |
| **No audit trail** | Log eligibility decisions |

## Are you stuck?

### Why are no registrants matching my criteria?

**Check:**
- Are the field names correct?
- Does your data contain the expected values?
- Are you targeting the right type (individual vs. group)?
- Is the domain syntax valid?

**Debug steps:**
1. Start with a minimal criterion
2. Add conditions one at a time
3. Use CEL preview to see match counts
4. Check sample registrant data

### How do I target households with specific member characteristics?

Use CEL expressions with the `members` context:

```cel
# Households with children under 5
members.exists(m, age_years(m.birthdate) < 5)

# Households with 2+ elderly members
members.filter(m, age_years(m.birthdate) >= 60).size() >= 2

# Female-headed households
members.exists(m, m.is_head == true and m.gender == 'female')
```

### Can I combine multiple criteria with OR logic?

Yes, with CEL:

```cel
# Elderly OR disabled
age_years(me.birthdate) >= 60 or me.has_disability == true
```

With domain syntax, you need to use `|` operator:

```python
['|', ('age', '>=', 60), ('has_disability', '=', True)]
```

### How do I handle missing data?

In CEL, use null checks:

```cel
# Only check PMT if it exists
me.pmt_score == null or me.pmt_score < 25
```

In domain syntax:

```python
['|', ('pmt_score', '=', False), ('pmt_score', '<', 25)]
```

## Next steps

**Learn more about concepts:**
- {doc}`programs` - How eligibility connects to programs
- {doc}`cycles` - Cycle-level eligibility verification
- {doc}`entitlements` - What happens after eligibility is confirmed

**For configuration:**
- See the Configuration Guide for setting up eligibility managers

**For developers:**
- See the Developer Guide for creating custom eligibility managers
