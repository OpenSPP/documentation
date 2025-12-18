---
openspp:
  doc_status: draft
---

# Social Welfare Development Index (SWDI)

This guide is for **implementers** configuring the Social Welfare Development Index (SWDI), a multi-dimensional welfare assessment framework. SWDI evaluates household wellbeing across multiple domains rather than focusing solely on poverty or vulnerability.

## What is SWDI?

The Social Welfare Development Index (SWDI) is a composite scoring method that:
- **Measures** wellbeing across multiple dimensions (health, education, housing, economic security)
- **Aggregates** sub-indices into a total welfare score
- **Provides** a holistic view of household welfare beyond income
- **Identifies** specific areas where households need support

SWDI is similar to HDI (Human Development Index) but adapted for household-level social protection targeting.

## When to Use SWDI

| Use SWDI For | Don't Use SWDI For |
|-------------|-------------------|
| Comprehensive welfare programs | Emergency cash transfers (too slow) |
| Multi-sectoral interventions | Single-purpose programs |
| Long-term development tracking | Quick targeting decisions |
| Identifying service gaps | Simple eligibility screening |
| Monitoring program impacts | Administrative census only |

**SWDI is best when:** Your program can address multiple dimensions of wellbeing (health, education, housing, economic) and you want to track progress over time.

## SWDI Structure

A typical SWDI model has four main components:

| Component | Weight | What It Measures |
|-----------|--------|------------------|
| **Health Index** | 30% | Health status, access to care, nutrition |
| **Education Index** | 25% | School enrollment, educational attainment |
| **Economic Security Index** | 25% | Income, employment, assets |
| **Housing Index** | 20% | Housing quality, utilities, amenities |

Each component is calculated separately as a sub-index (0-100 scale), then weighted and combined.

## Step-by-Step Configuration

### Step 1: Create the SWDI Model

Go to **Scoring → Scoring Models** and create:

| Field | Value |
|-------|-------|
| **Name** | Social Welfare Development Index 2024 |
| **Code** | SWDI_2024 |
| **Category** | custom |
| **Calculation Method** | weighted_sum |
| **Active** | ☑ (after configuration) |
| **Effective Date** | 2024-01-01 |
| **Description** | Multi-dimensional welfare assessment across health, education, economic, and housing domains |

**Note:** We'll create the model in two stages:
1. First, configure sub-indices as separate scoring models
2. Then, create the main SWDI model that references them

Alternatively, use a single model with indicator grouping.

## Approach 1: Single Integrated Model

This approach uses one scoring model with organized indicators.

### Step 2A: Health Index Indicators (Weight: 0.30)

#### Health Facility Access

| Field | Value |
|-------|-------|
| Code | health_access |
| Name | Access to Health Facility |
| Field Path | household.health_facility_access |
| Weight | 0.10 |
| Calculation Type | mapped |
| Required | Yes |
| Sequence | 1 |

**Value Mappings:**

| Input Value | Output Score | Notes |
|-------------|--------------|-------|
| regular_access | 100 | Can access healthcare when needed |
| limited_access | 60 | Sometimes face barriers |
| no_access | 0 | Cannot access healthcare |

#### Household Illness Burden

| Field | Value |
|-------|-------|
| Code | chronic_illness |
| Name | Members with Chronic Illness |
| Field Path | household.chronic_illness_count |
| Weight | 0.08 |
| Calculation Type | range |
| Required | Yes |
| Sequence | 2 |

**Value Mappings (Range - Inverse Scoring):**

| Min | Max | Output Score | Notes |
|-----|-----|--------------|-------|
| 0 | 0 | 100 | No chronic illness |
| 1 | 1 | 60 | One member |
| 2 | 2 | 30 | Two members |
| 3 | 99 | 0 | Three or more |

#### Child Nutrition Status

| Field | Value |
|-------|-------|
| Code | child_nutrition |
| Name | Children Under 5 Well Nourished |
| Field Path | household.children_well_nourished |
| Weight | 0.07 |
| Calculation Type | mapped |
| Required | No |
| Default Value | True |
| Sequence | 3 |

**Value Mappings:**

| Input Value | Output Score | Notes |
|-------------|--------------|-------|
| True | 100 | All children U5 well nourished |
| False | 0 | At least one child malnourished |

**How to determine:** Based on growth monitoring, MUAC measurements, or self-reported assessment.

#### Health Insurance Coverage

| Field | Value |
|-------|-------|
| Code | health_insurance |
| Name | Household Has Health Insurance |
| Field Path | household.has_health_insurance |
| Weight | 0.05 |
| Calculation Type | mapped |
| Required | Yes |
| Sequence | 4 |

**Value Mappings:**

| Input Value | Output Score |
|-------------|--------------|
| True | 100 |
| False | 0 |

### Step 3A: Education Index Indicators (Weight: 0.25)

#### School-Age Children Enrolled

| Field | Value |
|-------|-------|
| Code | school_enrollment |
| Name | School-Age Children Enrolled |
| Field Path | household.school_enrollment_rate |
| Weight | 0.12 |
| Calculation Type | range |
| Required | Yes |
| Sequence | 5 |

**Value Mappings (Range):**

| Min | Max | Output Score | Notes |
|-----|-----|--------------|-------|
| 100 | 100 | 100 | All children enrolled |
| 75 | 99 | 70 | Most children enrolled |
| 50 | 74 | 40 | Half enrolled |
| 1 | 49 | 20 | Few enrolled |
| 0 | 0 | 0 | No enrollment |

**How to calculate:** (Enrolled children ÷ Total school-age children) × 100

Use CEL formula:
```cel
(household.children_enrolled / household.children_school_age) * 100
```

#### Adult Literacy

| Field | Value |
|-------|-------|
| Code | adult_literacy |
| Name | Adult Literacy Rate in Household |
| Field Path | household.adult_literacy_rate |
| Weight | 0.08 |
| Calculation Type | range |
| Required | Yes |
| Sequence | 6 |

**Value Mappings (Range):**

| Min | Max | Output Score |
|-----|-----|--------------|
| 100 | 100 | 100 |
| 75 | 99 | 75 |
| 50 | 74 | 50 |
| 25 | 49 | 25 |
| 0 | 24 | 0 |

**How to calculate:** (Literate adults ÷ Total adults) × 100

#### Highest Education in Household

| Field | Value |
|-------|-------|
| Code | max_education |
| Name | Highest Education Level in Household |
| Field Path | household.max_education_level |
| Weight | 0.05 |
| Calculation Type | mapped |
| Required | Yes |
| Sequence | 7 |

**Value Mappings:**

| Input Value | Output Score |
|-------------|--------------|
| tertiary | 100 |
| vocational | 80 |
| secondary | 60 |
| primary | 30 |
| none | 0 |

### Step 4A: Economic Security Index Indicators (Weight: 0.25)

#### Employment Status

| Field | Value |
|-------|-------|
| Code | employment_rate |
| Name | Working-Age Adults Employed |
| Field Path | household.employment_rate |
| Weight | 0.10 |
| Calculation Type | range |
| Required | Yes |
| Sequence | 8 |

**Value Mappings (Range):**

| Min | Max | Output Score | Notes |
|-----|-----|--------------|-------|
| 75 | 100 | 100 | Most/all adults working |
| 50 | 74 | 70 | Half employed |
| 25 | 49 | 40 | Few employed |
| 1 | 24 | 20 | Very low employment |
| 0 | 0 | 0 | No employment |

**How to calculate:** (Employed adults ÷ Working-age adults) × 100

#### Income Stability

| Field | Value |
|-------|-------|
| Code | income_stability |
| Name | Regular Income Sources |
| Field Path | household.has_regular_income |
| Weight | 0.08 |
| Calculation Type | mapped |
| Required | Yes |
| Sequence | 9 |

**Value Mappings:**

| Input Value | Output Score | Notes |
|-------------|--------------|-------|
| regular | 100 | Salary, pension, stable business |
| irregular | 50 | Casual labor, seasonal work |
| none | 0 | No regular income |

#### Asset Ownership

| Field | Value |
|-------|-------|
| Code | productive_assets |
| Name | Owns Productive Assets |
| Field Path | household.productive_asset_score |
| Weight | 0.07 |
| Calculation Type | range |
| Required | Yes |
| Sequence | 10 |

**Value Mappings (Range):**

| Min | Max | Output Score | Notes |
|-----|-----|--------------|-------|
| 8 | 10 | 100 | Multiple productive assets |
| 5 | 7 | 70 | Some productive assets |
| 2 | 4 | 40 | Few assets |
| 0 | 1 | 0 | No/minimal productive assets |

**Productive assets:** Land, livestock, business equipment, tools, vehicles for work

**How to score:** Create an asset index (0-10) based on asset value/count.

### Step 5A: Housing Index Indicators (Weight: 0.20)

#### Housing Structure Quality

| Field | Value |
|-------|-------|
| Code | housing_quality |
| Name | Housing Quality Index |
| Field Path | household.housing_quality_score |
| Weight | 0.08 |
| Calculation Type | range |
| Required | Yes |
| Sequence | 11 |

**Value Mappings (Range):**

| Min | Max | Output Score |
|-----|-----|--------------|
| 8 | 10 | 100 |
| 6 | 7 | 70 |
| 4 | 5 | 40 |
| 0 | 3 | 0 |

**Housing quality score:** Composite of roof, wall, floor materials (score each 0-10, average them)

#### Water & Sanitation

| Field | Value |
|-------|-------|
| Code | wash_access |
| Name | WASH Access Score |
| Field Path | household.wash_score |
| Weight | 0.07 |
| Calculation Type | range |
| Required | Yes |
| Sequence | 12 |

**Value Mappings (Range):**

| Min | Max | Output Score |
|-----|-----|--------------|
| 8 | 10 | 100 |
| 5 | 7 | 60 |
| 2 | 4 | 30 |
| 0 | 1 | 0 |

**WASH score:** Combine water source (0-5) + sanitation facility (0-5) = 0-10 total

#### Electricity Access

| Field | Value |
|-------|-------|
| Code | electricity |
| Name | Has Reliable Electricity |
| Field Path | household.has_electricity |
| Weight | 0.03 |
| Calculation Type | mapped |
| Required | Yes |
| Sequence | 13 |

**Value Mappings:**

| Input Value | Output Score | Notes |
|-------------|--------------|-------|
| grid_reliable | 100 | Connected to grid, reliable |
| grid_unreliable | 70 | Connected but frequent outages |
| off_grid | 40 | Solar, generator (limited) |
| none | 0 | No electricity |

#### Overcrowding

| Field | Value |
|-------|-------|
| Code | persons_per_room |
| Name | Persons Per Sleeping Room |
| Field Path | household.persons_per_room |
| Weight | 0.02 |
| Calculation Type | range |
| Required | Yes |
| Sequence | 14 |

**Value Mappings (Range - Inverse):**

| Min | Max | Output Score | Notes |
|-----|-----|--------------|-------|
| 0 | 2 | 100 | Not overcrowded |
| 2.01 | 3 | 70 | Slightly overcrowded |
| 3.01 | 4 | 40 | Overcrowded |
| 4.01 | 99 | 0 | Severely overcrowded |

**How to calculate:** Total household members ÷ Number of sleeping rooms

### Step 6A: Define SWDI Thresholds

SWDI total score (0-100) classifications:

| Min Score | Max Score | Classification Code | Classification Label | Color |
|-----------|-----------|---------------------|----------------------|-------|
| 0.0 | 30.0 | VERY_LOW_WELFARE | Very Low Welfare | red |
| 30.01 | 50.0 | LOW_WELFARE | Low Welfare | orange |
| 50.01 | 70.0 | MODERATE_WELFARE | Moderate Welfare | yellow |
| 70.01 | 85.0 | HIGH_WELFARE | High Welfare | light green |
| 85.01 | 100.0 | VERY_HIGH_WELFARE | Very High Welfare | dark green |

### Step 7A: Validate and Test

**Check weight distribution:**
- Health indicators: 0.10 + 0.08 + 0.07 + 0.05 = 0.30 ✓
- Education indicators: 0.12 + 0.08 + 0.05 = 0.25 ✓
- Economic indicators: 0.10 + 0.08 + 0.07 = 0.25 ✓
- Housing indicators: 0.08 + 0.07 + 0.03 + 0.02 = 0.20 ✓
- **Total: 1.00 ✓**

**Test with sample household:**

#### Test Case: Moderate Welfare Household

| Indicator | Value | Score | Weight | Weighted |
|-----------|-------|-------|--------|----------|
| **Health (0.30)** |
| Health Access | limited_access | 60 | 0.10 | 6.0 |
| Chronic Illness | 1 member | 60 | 0.08 | 4.8 |
| Child Nutrition | True | 100 | 0.07 | 7.0 |
| Health Insurance | False | 0 | 0.05 | 0.0 |
| **Education (0.25)** |
| School Enrollment | 100% | 100 | 0.12 | 12.0 |
| Adult Literacy | 75% | 75 | 0.08 | 6.0 |
| Max Education | secondary | 60 | 0.05 | 3.0 |
| **Economic (0.25)** |
| Employment Rate | 60% | 70 | 0.10 | 7.0 |
| Income Stability | irregular | 50 | 0.08 | 4.0 |
| Productive Assets | 3 assets | 40 | 0.07 | 2.8 |
| **Housing (0.20)** |
| Housing Quality | 7/10 | 70 | 0.08 | 5.6 |
| WASH Access | 6/10 | 60 | 0.07 | 4.2 |
| Electricity | grid_unreliable | 70 | 0.03 | 2.1 |
| Persons Per Room | 2.5 | 70 | 0.02 | 1.4 |
| **Total** | | | **1.00** | **65.9** |

**Final Score: 65.9 → MODERATE_WELFARE** ✓

## Approach 2: Modular Sub-Index Models

For more flexibility, create separate scoring models for each domain, then combine them.

### Step 2B: Create Sub-Index Models

Create four separate scoring models:
1. Health Index (SWDI_HEALTH_2024)
2. Education Index (SWDI_EDU_2024)
3. Economic Index (SWDI_ECON_2024)
4. Housing Index (SWDI_HOUSING_2024)

Each sub-index model:
- Has its own indicators
- Produces a 0-100 score
- Can be updated independently

### Step 3B: Create Composite SWDI Model

Use CEL formula to combine sub-indices:

| Field | Value |
|-------|-------|
| **Name** | SWDI Composite 2024 |
| **Code** | SWDI_2024 |
| **Calculation Method** | cel_formula |
| **CEL Expression** | See below |

**CEL Formula:**
```cel
(health_score.score * 0.30) +
(education_score.score * 0.25) +
(economic_score.score * 0.25) +
(housing_score.score * 0.20)
```

**Variables needed:**
- `health_score` → Latest score from SWDI_HEALTH_2024 model
- `education_score` → Latest score from SWDI_EDU_2024 model
- `economic_score` → Latest score from SWDI_ECON_2024 model
- `housing_score` → Latest score from SWDI_HOUSING_2024 model

**Advantage:** You can update education indicators without re-configuring health, economic, or housing components.

## Using SWDI Results

### Comprehensive Program Targeting

Target households with low SWDI scores for multi-sectoral support:

| SWDI Score | Intervention Package |
|------------|---------------------|
| 0-30 | Intensive case management + cash + services |
| 30-50 | Cash transfer + service referrals |
| 50-70 | Service access support |
| 70+ | Monitoring only (graduated) |

### Domain-Specific Interventions

Use sub-index scores to identify specific needs:

**Example:** Household with:
- Health Index: 40 (low) → Refer to health services, insurance enrollment
- Education Index: 85 (high) → No education intervention needed
- Economic Index: 50 (moderate) → Livelihood support
- Housing Index: 30 (low) → Housing upgrade assistance

### Progress Monitoring

Re-score households annually to track welfare changes:

| Year | SWDI Score | Classification | Change |
|------|-----------|----------------|--------|
| 2024 | 45 | Low Welfare | Baseline |
| 2025 | 58 | Moderate Welfare | +13 (improved) |
| 2026 | 72 | High Welfare | +14 (graduated) |

### Graduation Criteria

Set graduation thresholds:
- **Graduate when:** SWDI ≥ 70 for two consecutive years
- **Reduce support when:** SWDI 50-70
- **Intensive support when:** SWDI < 50

## Adapting SWDI to Your Context

SWDI is highly customizable:

### Adjust Domain Weights

**Example 1: Education-Focused Program**
- Health: 20%
- Education: 40% (increased)
- Economic: 20%
- Housing: 20%

**Example 2: Post-Disaster Context**
- Health: 35% (increased)
- Education: 15% (decreased)
- Economic: 30%
- Housing: 20%

### Add Custom Domains

Consider adding:
- **Social Cohesion Index** (10-15%) - Community participation, social support
- **Security Index** (10-15%) - Safety, protection concerns
- **Environmental Index** (5-10%) - Climate resilience, natural resource access

### Simplified SWDI

For rapid assessment, reduce indicators:
- 2-3 indicators per domain (8-12 total)
- Use observable indicators only (no calculated fields)
- Binary scoring where possible (0 or 100)

## Integration with Programs

### Eligibility Based on SWDI

In eligibility manager:

| Field | Value |
|-------|-------|
| Scoring Model | SWDI_2024 |
| Maximum Score | 50.0 |

Households with SWDI ≤ 50 are eligible.

### Combining SWDI with Other Scores

Use multiple scoring criteria:

```cel
(swdi_score.score <= 50) ||
(pmt_score.classification == 'POOR') ||
(vuln_score.classification == 'HIGH_VULN')
```

Households qualify if they meet ANY of these conditions.

### Benefit Levels by Domain Deficits

Customize benefit packages based on which domains are low:

| Domain Deficits | Benefit Package |
|-----------------|-----------------|
| Health only | Health insurance + service vouchers |
| Education only | School supplies + tutoring |
| Economic only | Cash grant + livelihood training |
| Housing only | Housing upgrade grant |
| Multiple domains | Comprehensive support package |

## Common Patterns

### Pattern 1: Development Program with Graduation

- **Entry criteria:** SWDI < 50
- **Support:** Multi-sectoral interventions over 2-3 years
- **Graduation:** SWDI ≥ 70 for 2 consecutive assessments
- **Re-assess:** Annually

### Pattern 2: Service Gap Identification

- **Calculate:** SWDI and sub-indices for entire registry
- **Analyze:** Which domains have lowest average scores?
- **Plan:** Invest in services for weakest domains
- **Monitor:** Track domain scores over time

### Pattern 3: Targeting with Flexibility

- **Primary criterion:** SWDI < 60
- **Secondary:** Allow case-by-case inclusion for households with specific vulnerabilities (e.g., disability, recent shock)
- **Appeals:** Use SWDI breakdown to review cases

## Are You Stuck?

**SWDI seems too complex?**
Start with a simplified version. Use 2-3 indicators per domain. You can add more sophistication later.

**How to weight domains?**
Base weights on your program objectives. If you're a health program, weight health more heavily. If comprehensive, use balanced weights (20-30% each).

**Sub-indices not calculating?**
Check that indicators within each domain have weights that make sense. Each sub-index should produce a 0-100 score.

**Scores don't match field observations?**
SWDI is multi-dimensional—a household can score high overall but have specific domain weaknesses. Review sub-index scores, not just total.

**How often to recalculate?**
SWDI components change slowly. Annual assessment is typical. More frequent (quarterly) if you're actively intervening.

**Should all indicators be weighted equally within domains?**
No. Weight indicators within each domain based on their importance. Health insurance might be less critical than health facility access, so use lower weight.

**Can I use SWDI with missing data?**
Mark non-critical indicators as not required. Calculate SWDI based on available indicators, but note that missing data affects comparability.

## Best Practices

1. **Align with program goals:** Weight domains based on what your program addresses
2. **Use existing data:** Where possible, map to data you already collect
3. **Validate with communities:** Do SWDI classifications match local perceptions?
4. **Track over time:** SWDI's strength is monitoring change
5. **Report by domain:** Don't just share total scores—show domain breakdowns
6. **Update periodically:** Review indicator relevance every 2-3 years
7. **Combine with qualitative data:** SWDI + case worker observations = best picture
8. **Set realistic targets:** Not all households will reach 100—what's "good enough"?

## Security Considerations

SWDI data is comprehensive and sensitive:

| Data Type | Risk | Mitigation |
|-----------|------|------------|
| Health information | Medical privacy | Limit access to health sub-index details |
| Housing details | Security risk (valuable assets) | Aggregate reporting, anonymize locations |
| Education data | Stigma (low education) | Present as household average, not individuals |
| Economic data | Targeting for exploitation | Encrypt, restrict export, audit access |

## Next Steps

- **{doc}`pmt`** - Add poverty scoring for economic domain detail
- **{doc}`vulnerability`** - Complement SWDI with vulnerability assessment
- **{doc}`custom`** - Create custom domain indices for your context
- **{doc}`/config_guide/eligibility/index`** - Link SWDI to program eligibility

---

**See also:**
- {doc}`overview` - Scoring fundamentals
- {doc}`/config_guide/variables/index` - CEL formulas for calculated indicators
- {doc}`/config_guide/event_data/index` - Track life events that affect SWDI
