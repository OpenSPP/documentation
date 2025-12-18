---
openspp:
  doc_status: draft
---

# Creating Custom Scoring Formulas

This guide is for **implementers** building custom scoring models for program-specific needs. If PMT, vulnerability, or SWDI don't fit your requirements, you can create tailored scoring formulas using OpenSPP's flexible scoring framework.

## When to Create Custom Scores

Create custom scoring models when:
- **Program has unique targeting criteria** (e.g., youth employment readiness, farmer productivity)
- **Need to combine multiple methodologies** (e.g., 60% PMT + 40% vulnerability)
- **External requirements** mandate specific calculation methods
- **Piloting new approaches** before standardizing
- **Context-specific adaptations** of standard methods

## Custom Scoring Approaches

| Approach | When to Use | Complexity |
|----------|-------------|------------|
| **Weighted Sum with Custom Indicators** | Program-specific criteria, simple formula | Low |
| **CEL Formula Scoring** | Complex conditional logic, mathematical transformations | Medium |
| **Lookup Tables** | Direct mapping from characteristics to eligibility tiers | Low |
| **Composite Scores** | Combine multiple existing scores | Medium |
| **External Integration** | Fetch scores from third-party systems or ML models | High |

## Approach 1: Weighted Sum with Custom Indicators

Use OpenSPP's weighted sum method with indicators specific to your program.

### Example: Youth Employment Readiness Score

**Goal:** Score young people (18-24) for job training program eligibility.

#### Step 1: Create the Model

| Field | Value |
|-------|-------|
| **Name** | Youth Employment Readiness 2024 |
| **Code** | YER_2024 |
| **Category** | eligibility |
| **Calculation Method** | weighted_sum |
| **Active** | ☑ |
| **Description** | Scores youth based on education, work experience, motivation |

#### Step 2: Define Custom Indicators

**Education Level**

| Field | Value |
|-------|-------|
| Code | education_level |
| Name | Highest Education Completed |
| Field Path | individual.education_level |
| Weight | 0.25 |
| Calculation Type | mapped |
| Sequence | 1 |

**Value Mappings:**

| Input Value | Output Score | Reasoning |
|-------------|--------------|-----------|
| tertiary | 100 | Ready for advanced roles |
| vocational | 90 | Job-specific skills |
| secondary | 70 | Basic skills present |
| primary | 40 | Needs basic training |
| none | 0 | Intensive support needed |

**Previous Work Experience**

| Field | Value |
|-------|-------|
| Code | work_experience |
| Name | Months of Work Experience |
| Field Path | individual.work_experience_months |
| Weight | 0.20 |
| Calculation Type | range |
| Sequence | 2 |

**Value Mappings (Range):**

| Min | Max | Output Score |
|-----|-----|--------------|
| 24 | 999 | 100 |
| 12 | 23 | 75 |
| 6 | 11 | 50 |
| 1 | 5 | 25 |
| 0 | 0 | 0 |

**Digital Literacy**

| Field | Value |
|-------|-------|
| Code | digital_skills |
| Name | Digital Literacy Assessment |
| Field Path | individual.digital_literacy_score |
| Weight | 0.20 |
| Calculation Type | range |
| Sequence | 3 |

**Value Mappings (Range):**

| Min | Max | Output Score | Notes |
|-----|-----|--------------|-------|
| 80 | 100 | 100 | Advanced (can use office software) |
| 60 | 79 | 75 | Intermediate (basic computer use) |
| 40 | 59 | 50 | Basic (smartphone only) |
| 20 | 39 | 25 | Limited (minimal exposure) |
| 0 | 19 | 0 | None |

**Communication Skills**

| Field | Value |
|-------|-------|
| Code | communication |
| Name | Communication Skills Rating |
| Field Path | individual.communication_score |
| Weight | 0.15 |
| Calculation Type | range |
| Sequence | 4 |

**Value Mappings (Range):**

| Min | Max | Output Score |
|-----|-----|--------------|
| 8 | 10 | 100 |
| 6 | 7 | 70 |
| 4 | 5 | 40 |
| 0 | 3 | 0 |

**Motivation & Interest**

| Field | Value |
|-------|-------|
| Code | motivation |
| Name | Motivation Assessment |
| Field Path | individual.motivation_score |
| Weight | 0.10 |
| Calculation Type | range |
| Sequence | 5 |

**Value Mappings (Range):**

| Min | Max | Output Score |
|-----|-----|--------------|
| 8 | 10 | 100 |
| 6 | 7 | 70 |
| 4 | 5 | 40 |
| 0 | 3 | 0 |

**Barrier Factors (Inverse Scoring)**

| Field | Value |
|-------|-------|
| Code | barriers |
| Name | Barriers to Employment Count |
| Field Path | individual.employment_barriers_count |
| Weight | 0.10 |
| Calculation Type | range |
| Sequence | 6 |

**Value Mappings (Range - Inverse):**

| Min | Max | Output Score | Notes |
|-----|-----|--------------|-------|
| 0 | 0 | 100 | No barriers |
| 1 | 1 | 70 | One barrier |
| 2 | 2 | 40 | Two barriers |
| 3 | 99 | 0 | Multiple barriers |

**Barriers include:** Transport issues, childcare needs, health limitations, etc.

#### Step 3: Set Thresholds

| Min Score | Max Score | Classification | Priority |
|-----------|-----------|----------------|----------|
| 0 | 40 | LOW_READINESS | 3 (needs intensive prep) |
| 40.01 | 65 | MODERATE_READINESS | 2 (needs basic training) |
| 65.01 | 100 | HIGH_READINESS | 1 (job-ready) |

#### Step 4: Use in Program Eligibility

In eligibility manager:

| Field | Value |
|-------|-------|
| Scoring Model | YER_2024 |
| Minimum Score | 40 |

Youth with scores ≥ 40 are eligible. Those with LOW_READINESS are referred to foundational skills training first.

## Approach 2: CEL Formula Scoring

Use Common Expression Language (CEL) for complex calculations.

### Example: Farmer Productivity Score

**Goal:** Score farmer households for agricultural support based on land, practices, and constraints.

#### Step 1: Create Model with CEL Formula

| Field | Value |
|-------|-------|
| **Name** | Farmer Productivity Index 2024 |
| **Code** | FPI_2024 |
| **Category** | eligibility |
| **Calculation Method** | cel_formula |
| **CEL Expression** | See below |

#### Step 2: Create Variables for Formula Components

Go to **Studio → Variables** and create:

**Land Size (hectares)**

| Field | Value |
|-------|-------|
| Name | Farm Land Size |
| CEL Accessor | farm_land_hectares |
| Field Path | household.farm_land_hectares |
| Applies To | Group/Household |

**Good Agricultural Practices Adoption**

| Field | Value |
|-------|-------|
| Name | GAP Adoption Score |
| CEL Accessor | gap_score |
| Field Path | household.gap_adoption_score |
| Applies To | Group/Household |

**Notes:** Score 0-10 based on practices like crop rotation, organic fertilizer, pest management.

**Market Access**

| Field | Value |
|-------|-------|
| Name | Market Distance |
| CEL Accessor | market_distance_km |
| Field Path | household.market_distance_km |
| Applies To | Group/Household |

**Irrigation Access**

| Field | Value |
|-------|-------|
| Name | Has Irrigation |
| CEL Accessor | has_irrigation |
| Field Path | household.has_irrigation |
| Applies To | Group/Household |

#### Step 3: Write CEL Formula

```cel
// Base score from land size (0-30 points)
(farm_land_hectares >= 5 ? 30 :
 farm_land_hectares >= 2 ? 20 :
 farm_land_hectares >= 1 ? 10 :
 farm_land_hectares >= 0.5 ? 5 : 0) +

// Good agricultural practices (0-25 points)
(gap_score * 2.5) +

// Market access (0-20 points, inverse distance)
(market_distance_km <= 5 ? 20 :
 market_distance_km <= 10 ? 15 :
 market_distance_km <= 20 ? 10 :
 market_distance_km <= 50 ? 5 : 0) +

// Irrigation (0-15 points)
(has_irrigation ? 15 : 0) +

// Household size adjustment (0-10 points, more workers = higher productivity potential)
(household.member_count >= 5 ? 10 :
 household.member_count >= 3 ? 7 :
 household.member_count >= 2 ? 4 : 0)
```

**Maximum possible score:** 30 + 25 + 20 + 15 + 10 = **100 points**

#### Step 4: Define Thresholds

| Min Score | Max Score | Classification | Support Package |
|-----------|-----------|----------------|-----------------|
| 0 | 30 | LOW_PRODUCTIVITY | Seeds + training + tools |
| 30.01 | 60 | MODERATE_PRODUCTIVITY | Training + credit access |
| 60.01 | 100 | HIGH_PRODUCTIVITY | Market linkage + bulk credit |

### CEL Formula Patterns

**Conditional Scoring:**
```cel
condition ? score_if_true : score_if_false
```

**Nested Conditions:**
```cel
value >= 100 ? 10 :
value >= 50 ? 7 :
value >= 25 ? 4 : 0
```

**Combining Multiple Factors:**
```cel
(factor1_score * 0.4) + (factor2_score * 0.3) + (factor3_score * 0.3)
```

**Using Variables:**
```cel
children_under_5 >= 2 && household_income < 10000 ? 100 : 0
```

**Aggregations:**
```cel
household.members.filter(m, m.age < 18).size() * 5
```

**Safe Division (avoid divide by zero):**
```cel
working_adults > 0 ? (dependents / working_adults * 100) : 100
```

## Approach 3: Lookup Table Scoring

Map household characteristics directly to predefined scores.

### Example: Disaster Risk Classification

**Goal:** Classify households into risk tiers for disaster preparedness programs.

#### Step 1: Create Model

| Field | Value |
|-------|-------|
| **Name** | Disaster Risk Tier Assignment |
| **Code** | DISASTER_RISK_2024 |
| **Category** | triage |
| **Calculation Method** | lookup_table |

#### Step 2: Create Combination Lookup

Define a lookup indicator that considers multiple factors:

| Field | Value |
|-------|-------|
| Code | risk_tier |
| Name | Risk Tier Assignment |
| Field Path | household.disaster_risk_profile |
| Weight | 1.0 |
| Calculation Type | mapped |

**Value Mappings:**

| Input Value | Output Score | Notes |
|-------------|--------------|-------|
| coastal_wood_elderly | 100 | High risk: coastal, wood house, elderly |
| coastal_wood_family | 90 | High risk: coastal, wood house |
| coastal_concrete | 70 | Medium risk: coastal but strong house |
| inland_wood_flood | 80 | Medium-high: inland but flood zone |
| inland_concrete | 30 | Low risk: inland, strong house |
| highland_any | 10 | Very low risk: highland area |

**Note:** The `disaster_risk_profile` field should be calculated/assigned during registration based on location, housing type, and household composition.

#### Step 3: Set Thresholds

| Min Score | Max Score | Classification | Response Priority |
|-----------|-----------|----------------|-------------------|
| 0 | 30 | TIER_3 | Monitoring only |
| 30.01 | 70 | TIER_2 | Preparedness kit |
| 70.01 | 100 | TIER_1 | Priority evacuation plan |

## Approach 4: Composite Scores

Combine multiple existing scoring models.

### Example: Integrated Targeting Score

**Goal:** Combine poverty (PMT) and vulnerability for comprehensive targeting.

#### Step 1: Ensure Base Models Exist

- PMT_2024 (poverty scoring)
- VULN_2024 (vulnerability scoring)

#### Step 2: Create Composite Model

| Field | Value |
|-------|-------|
| **Name** | Integrated Targeting Index 2024 |
| **Code** | ITI_2024 |
| **Category** | eligibility |
| **Calculation Method** | cel_formula |
| **CEL Expression** | See below |

#### Step 3: Create Variables for Existing Scores

**PMT Score Variable**

| Field | Value |
|-------|-------|
| Name | Latest PMT Score |
| CEL Accessor | pmt_score |
| Source Type | Scoring Result |
| Scoring Model | PMT_2024 |
| Applies To | Group/Household |

**Vulnerability Score Variable**

| Field | Value |
|-------|-------|
| Name | Latest Vulnerability Score |
| CEL Accessor | vuln_score |
| Source Type | Scoring Result |
| Scoring Model | VULN_2024 |
| Applies To | Group/Household |

#### Step 4: Write Composite Formula

**Option 1: Weighted Average**
```cel
(pmt_score * 0.6) + (vuln_score * 0.4)
```

**Option 2: Maximum of Two**
```cel
pmt_score > vuln_score ? pmt_score : vuln_score
```

**Option 3: Conditional Combination**
```cel
// If extremely poor, use PMT score
// If extremely vulnerable, use vulnerability score
// Otherwise, use average
pmt_score >= 75 ? pmt_score :
vuln_score >= 75 ? vuln_score :
(pmt_score + vuln_score) / 2
```

**Option 4: Multiplicative (Both Must Be High)**
```cel
// Scale so households must score high on BOTH dimensions
((pmt_score / 100) * (vuln_score / 100)) * 100
```

#### Step 5: Define Thresholds

| Min Score | Max Score | Classification | Action |
|-----------|-----------|----------------|--------|
| 0 | 40 | LOW_PRIORITY | No assistance |
| 40.01 | 60 | MEDIUM_PRIORITY | Monitoring |
| 60.01 | 80 | HIGH_PRIORITY | Standard package |
| 80.01 | 100 | URGENT | Priority enrollment |

## Approach 5: External Integration

Connect to external scoring services or machine learning models.

### Example: ML-Based Poverty Model

**Goal:** Use a machine learning model trained on consumption data to predict poverty.

#### Step 1: Set Up External Service

Your ML model is deployed as a REST API:
```
POST https://ml.example.org/api/v1/predict-poverty
Body: {"household_id": "HH12345", "features": {...}}
Response: {"poverty_score": 72.5, "confidence": 0.89}
```

#### Step 2: Create Model Configuration

| Field | Value |
|-------|-------|
| **Name** | ML Poverty Prediction Model |
| **Code** | ML_PMT_2024 |
| **Category** | poverty |
| **Calculation Method** | external |
| **External Endpoint** | https://ml.example.org/api/v1/predict-poverty |
| **External Adapter** | (developer provides custom adapter code) |

#### Step 3: Configure Adapter

**Note:** This requires developer support. The adapter code:
1. Collects household features from OpenSPP
2. Formats API request
3. Calls external service
4. Parses response
5. Returns score to OpenSPP

#### Step 4: Use Like Any Other Model

Once configured, the external model works transparently:
- Calculate scores through UI or batch jobs
- Results stored in OpenSPP
- Use in eligibility criteria

**Advantages:**
- Leverage advanced ML models
- Model updates don't require OpenSPP changes
- Integration with existing government systems

**Considerations:**
- Requires stable API connectivity
- Implement caching for performance
- Have fallback if external service is down

## Advanced Patterns

### Pattern 1: Time-Decay Scoring

**Use case:** Recent shocks matter more than old shocks.

```cel
// Calculate weighted shock score with time decay
(recent_shock_3mo ? 10 : 0) * 1.0 +   // Last 3 months: full weight
(recent_shock_6mo ? 10 : 0) * 0.7 +   // 3-6 months: 70% weight
(recent_shock_12mo ? 10 : 0) * 0.4    // 6-12 months: 40% weight
```

### Pattern 2: Threshold-Based Bonus

**Use case:** Extra points if household meets multiple criteria.

```cel
// Base score
base_score +
// Bonus if BOTH conditions met
((poverty_score >= 75 && vulnerability_score >= 75) ? 20 : 0)
```

### Pattern 3: Categorical Multipliers

**Use case:** Score differently for different household types.

```cel
// Adjust score based on household type
household.type == 'female_headed' ? base_score * 1.2 :
household.type == 'disabled_member' ? base_score * 1.15 :
base_score
```

### Pattern 4: Progressive Scoring

**Use case:** Steeper penalties at extremes.

```cel
// Non-linear scoring for overcrowding
persons_per_room <= 2 ? 0 :
persons_per_room <= 3 ? 10 :
persons_per_room <= 4 ? 25 :
persons_per_room <= 5 ? 50 : 100
```

### Pattern 5: Multi-Criteria Must-Pass

**Use case:** Household must meet minimum thresholds on multiple dimensions.

```cel
// All three conditions must be met (AND logic)
(poverty_score >= 50 ? 33 : 0) +
(vulnerability_score >= 50 ? 33 : 0) +
(need_score >= 50 ? 34 : 0)
// Result: 100 if all three pass, < 100 otherwise
```

## Testing Custom Formulas

### Test Checklist

Before activating your custom model:

1. **Edge Cases**
   - [ ] Tested with all fields at minimum values
   - [ ] Tested with all fields at maximum values
   - [ ] Tested with missing optional fields
   - [ ] Tested with unusual combinations

2. **Expected Outcomes**
   - [ ] Poorest household scores high
   - [ ] Wealthiest household scores low
   - [ ] Middle-range households score in middle
   - [ ] Classifications align with targeting goals

3. **Formula Validation**
   - [ ] CEL expressions parse without errors
   - [ ] All variables resolve correctly
   - [ ] Weights sum as expected
   - [ ] Score range matches thresholds (0-100 if thresholds use that scale)

4. **Performance**
   - [ ] Single calculation completes in < 2 seconds
   - [ ] Batch scoring 1000 households completes in < 5 minutes
   - [ ] External APIs respond within timeout

### Test Case Template

| Test Name | Input Values | Expected Score | Expected Classification | Actual Score | Pass/Fail |
|-----------|--------------|----------------|------------------------|--------------|-----------|
| Extreme case 1 | field1=X, field2=Y | 95 | HIGH | | |
| Typical case | field1=X, field2=Y | 60 | MODERATE | | |
| Edge case | field1=null | 0 | LOW | | |

## Validation Rules

Implement validation to prevent configuration errors:

### Weight Validation

If using weighted sum:
- Total weight should equal 1.0 (or your chosen scale)
- No negative weights
- No single indicator weighted > 0.5 (unless intentional)

### Threshold Validation

- Thresholds should be contiguous (no gaps)
- Min scores should be < max scores
- Thresholds should cover entire possible score range

### Field Path Validation

- All field paths must exist in the data model
- Field types must match calculation types (numeric for ranges, boolean for binary)

### Formula Validation

- CEL expressions must parse successfully
- All referenced variables must be defined
- No division by zero potential
- Output should be numeric

## Common Patterns by Sector

### Education Programs

**Score based on:**
- School enrollment status
- Academic performance
- Attendance rate
- Household support for education
- Distance to school

### Health Programs

**Score based on:**
- Health insurance coverage
- Access to health facilities
- Vaccination status (children)
- Chronic illness in household
- Maternal health indicators

### Livelihood Programs

**Score based on:**
- Employment status
- Income stability
- Asset ownership
- Skills and training
- Market access

### Social Services

**Score based on:**
- Service utilization history
- Social support networks
- Case worker assessments
- Self-reported needs
- Previous program outcomes

## Are You Stuck?

**CEL formula not evaluating?**
Test the formula in **Studio → CEL Expression Tester**. Check that all variables are defined and accessible.

**Scores all coming out the same?**
Review your indicator weights and value mappings. Ensure there's variation in the data and scoring ranges.

**Need to score based on data not in registry?**
Use Event Data to capture program-specific assessments, then reference those fields in scoring.

**Formula too complex?**
Break it into sub-components. Create intermediate variables for complex calculations, then reference them in the main formula.

**External integration not working?**
Check API connectivity, authentication, and timeout settings. Implement caching and fallback mechanisms.

**How to handle missing data?**
Mark indicators as not required and set sensible defaults. Or use CEL to check for null and substitute values:
```cel
field != null ? field : default_value
```

**Need different models for different regions?**
Create separate models (e.g., CUSTOM_URBAN_2024, CUSTOM_RURAL_2024) and use eligibility rules to apply the right model based on household location.

## Best Practices

1. **Start simple:** Begin with 5-8 indicators, add complexity as needed
2. **Document rationale:** Note why each indicator and weight was chosen
3. **Test thoroughly:** Use diverse test cases before going live
4. **Version models:** Track changes over time (MODEL_v1, MODEL_v2)
5. **Monitor outcomes:** After scoring, review classification distribution
6. **Iterate:** Adjust weights and thresholds based on field feedback
7. **Combine approaches:** Use multiple scoring models for different purposes
8. **Keep formulas readable:** Use meaningful variable names, add comments
9. **Plan for updates:** Design for easy adjustment as programs evolve
10. **Validate with stakeholders:** Ensure scoring logic aligns with program goals

## Security Considerations

Custom scoring may involve sensitive data:

| Risk | Mitigation |
|------|------------|
| **Formula exposure** | Restrict who can view/edit scoring models |
| **Data leakage** | Be careful with external API integrations |
| **Score manipulation** | Audit score calculations, log changes |
| **Unfair scoring** | Review for bias in indicators and weights |

## Next Steps

Ready to implement?

1. **Define objectives** - What are you trying to measure?
2. **Identify indicators** - What data points matter?
3. **Choose approach** - Weighted sum, CEL formula, or composite?
4. **Configure model** - Set up indicators, weights, thresholds
5. **Test thoroughly** - Use test cases to validate
6. **Activate and monitor** - Go live and track outcomes

**Need inspiration?**
- **{doc}`pmt`** - Study PMT indicator selection
- **{doc}`vulnerability`** - See vulnerability factor combinations
- **{doc}`swdi`** - Learn multi-dimensional aggregation

---

**See also:**
- {doc}`overview` - Scoring fundamentals
- {doc}`/config_guide/variables/index` - Creating CEL variables for formulas
- {doc}`/config_guide/eligibility/index` - Using scores in program eligibility
