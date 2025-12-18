---
openspp:
  doc_status: draft
---

# Proxy Means Test (PMT) Configuration

This guide is for **implementers** setting up Proxy Means Test scoring for poverty targeting. PMT uses observable household characteristics to estimate income or consumption levels without directly measuring them.

## What is PMT?

Proxy Means Test (PMT) is a poverty targeting method that:
- **Estimates** household poverty based on easily observable indicators (assets, housing, demographics)
- **Avoids** asking for sensitive income data (which is often unreliable)
- **Produces** a poverty probability score that classifies households into poverty levels
- **Is transparent** and replicable across assessments

PMT is widely used in conditional cash transfer programs, social safety nets, and poverty-targeted initiatives.

## When to Use PMT

| Use PMT When | Don't Use PMT When |
|--------------|-------------------|
| Targeting cash transfer programs | Emergency response (too slow) |
| National poverty registries | Small-scale pilot programs |
| Long-term program enrollment | Short-term crisis interventions |
| Verifiable, stable indicators available | Rapidly changing conditions |

## PMT Components

A complete PMT model in OpenSPP includes:

1. **Household indicators** - Observable characteristics (housing, assets, demographics)
2. **Indicator weights** - Coefficients derived from household surveys
3. **Value mappings** - How to score each indicator value
4. **Poverty thresholds** - Score ranges that define poverty levels

## Step-by-Step Configuration

### Step 1: Create the PMT Model

Go to **Scoring → Scoring Models** and create a new model:

| Field | Value |
|-------|-------|
| **Name** | 2024 PMT - Rural |
| **Code** | PMT_2024_RURAL |
| **Category** | poverty |
| **Calculation Method** | weighted_sum |
| **Active** | ☑ (after configuration complete) |
| **Effective Date** | 2024-01-01 |
| **Description** | PMT model for rural households based on 2023 HIES survey |

**Important:** Keep models inactive until fully configured and tested.

### Step 2: Add Housing Indicators

Housing quality is a strong poverty predictor. Add these indicators:

#### Roof Material

| Field | Value |
|-------|-------|
| Code | roof_material |
| Name | Roof Material |
| Field Path | household.roof_material |
| Weight | 0.15 |
| Calculation Type | mapped |
| Required | Yes |
| Sequence | 1 |

**Value Mappings:**

| Input Value | Output Score | Notes |
|-------------|--------------|-------|
| concrete | 0 | Strong, permanent material |
| metal_sheet | 2 | Durable, semi-permanent |
| tile | 1 | Good quality |
| wood | 6 | Light material |
| thatch | 8 | Temporary material |
| salvaged | 10 | Makeshift, poorest quality |

#### Wall Material

| Field | Value |
|-------|-------|
| Code | wall_material |
| Name | Wall Material |
| Field Path | household.wall_material |
| Weight | 0.15 |
| Calculation Type | mapped |
| Required | Yes |
| Sequence | 2 |

**Value Mappings:**

| Input Value | Output Score |
|-------------|--------------|
| concrete | 0 |
| brick | 1 |
| wood | 5 |
| bamboo | 7 |
| salvaged | 10 |

#### Floor Material

| Field | Value |
|-------|-------|
| Code | floor_material |
| Name | Floor Material |
| Field Path | household.floor_material |
| Weight | 0.10 |
| Calculation Type | mapped |
| Required | Yes |
| Sequence | 3 |

**Value Mappings:**

| Input Value | Output Score |
|-------------|--------------|
| tile | 0 |
| cement | 2 |
| wood | 5 |
| bamboo | 7 |
| earth | 10 |

### Step 3: Add Water & Sanitation Indicators

#### Water Source

| Field | Value |
|-------|-------|
| Code | water_source |
| Name | Primary Water Source |
| Field Path | household.water_source |
| Weight | 0.10 |
| Calculation Type | mapped |
| Required | Yes |
| Sequence | 4 |

**Value Mappings:**

| Input Value | Output Score | Notes |
|-------------|--------------|-------|
| piped_dwelling | 0 | Piped water in dwelling |
| piped_yard | 2 | Piped water in yard |
| public_tap | 4 | Public standpipe |
| protected_well | 6 | Protected well/spring |
| unprotected_well | 8 | Unprotected source |
| surface_water | 10 | River, lake, pond |

#### Toilet Facility

| Field | Value |
|-------|-------|
| Code | toilet_facility |
| Name | Toilet Facility Type |
| Field Path | household.toilet_type |
| Weight | 0.10 |
| Calculation Type | mapped |
| Required | Yes |
| Sequence | 5 |

**Value Mappings:**

| Input Value | Output Score |
|-------------|--------------|
| flush_sewer | 0 |
| flush_septic | 2 |
| ventilated_pit | 5 |
| pit_latrine | 7 |
| none | 10 |

### Step 4: Add Asset Indicators

Asset ownership indicates economic capacity. Use boolean indicators (owns or doesn't own).

#### Television

| Field | Value |
|-------|-------|
| Code | owns_tv |
| Name | Owns Television |
| Field Path | household.owns_tv |
| Weight | 0.12 |
| Calculation Type | mapped |
| Required | No |
| Default Value | False |
| Sequence | 6 |

**Value Mappings:**

| Input Value | Output Score |
|-------------|--------------|
| True | 0 |
| False | 10 |

#### Refrigerator

| Field | Value |
|-------|-------|
| Code | owns_refrigerator |
| Name | Owns Refrigerator |
| Field Path | household.owns_refrigerator |
| Weight | 0.15 |
| Calculation Type | mapped |
| Required | No |
| Default Value | False |
| Sequence | 7 |

**Value Mappings:**

| Input Value | Output Score |
|-------------|--------------|
| True | 0 |
| False | 10 |

#### Motorcycle/Scooter

| Field | Value |
|-------|-------|
| Code | owns_motorcycle |
| Name | Owns Motorcycle/Scooter |
| Field Path | household.owns_motorcycle |
| Weight | 0.08 |
| Calculation Type | mapped |
| Required | No |
| Default Value | False |
| Sequence | 8 |

**Value Mappings:**

| Input Value | Output Score |
|-------------|--------------|
| True | 0 |
| False | 10 |

### Step 5: Add Demographic Indicators

#### Household Size

| Field | Value |
|-------|-------|
| Code | household_size |
| Name | Number of Household Members |
| Field Path | household.member_count |
| Weight | 0.05 |
| Calculation Type | range |
| Required | Yes |
| Sequence | 9 |

**Value Mappings (Range-Based):**

| Min | Max | Output Score | Notes |
|-----|-----|--------------|-------|
| 1 | 3 | 0 | Small household |
| 4 | 6 | 3 | Medium household |
| 7 | 10 | 7 | Large household |
| 11 | 99 | 10 | Very large household |

### Step 6: Define Poverty Thresholds

Based on your national poverty lines, set thresholds that classify households:

| Min Score | Max Score | Classification Code | Classification Label | Color |
|-----------|-----------|---------------------|----------------------|-------|
| 0.0 | 25.0 | NON_POOR | Non-Poor | green |
| 25.01 | 50.0 | NEAR_POOR | Near Poor | yellow |
| 50.01 | 75.0 | POOR | Poor | orange |
| 75.01 | 100.0 | EXTREME_POOR | Extremely Poor | red |

**Note:** Adjust these thresholds based on:
- National poverty line
- Consumption survey data
- Program targeting requirements
- Available budget constraints

### Step 7: Validate the Model

Before activating, validate your configuration:

#### Check Weight Distribution

Total weight should make sense for your scoring scale. If using 0-100 scale and each indicator scores 0-10, the weighted sum should align with your thresholds.

**Example calculation:**
- If ALL indicators show maximum poverty (score 10 each)
- Weighted sum = (10 × 0.15) + (10 × 0.15) + ... = sum of all weights × 10
- Make sure this aligns with your "EXTREME_POOR" threshold (75-100)

#### Test with Sample Households

Create test cases before going live:

**Test Case 1: Extremely Poor Household**

| Indicator | Value | Score | Weight | Weighted Score |
|-----------|-------|-------|--------|----------------|
| Roof Material | salvaged | 10 | 0.15 | 1.5 |
| Wall Material | salvaged | 10 | 0.15 | 1.5 |
| Floor Material | earth | 10 | 0.10 | 1.0 |
| Water Source | surface_water | 10 | 0.10 | 1.0 |
| Toilet Facility | none | 10 | 0.10 | 1.0 |
| Owns TV | False | 10 | 0.12 | 1.2 |
| Owns Refrigerator | False | 10 | 0.15 | 1.5 |
| Owns Motorcycle | False | 10 | 0.08 | 0.8 |
| Household Size | 9 | 7 | 0.05 | 0.35 |
| **Total** | | | **1.0** | **9.85** |

**Final Score:** 9.85 × 10 = **98.5** → **EXTREME_POOR** ✓

**Test Case 2: Non-Poor Household**

| Indicator | Value | Score | Weight | Weighted Score |
|-----------|-------|-------|--------|----------------|
| Roof Material | concrete | 0 | 0.15 | 0 |
| Wall Material | concrete | 0 | 0.15 | 0 |
| Floor Material | tile | 0 | 0.10 | 0 |
| Water Source | piped_dwelling | 0 | 0.10 | 0 |
| Toilet Facility | flush_sewer | 0 | 0.10 | 0 |
| Owns TV | True | 0 | 0.12 | 0 |
| Owns Refrigerator | True | 0 | 0.15 | 0 |
| Owns Motorcycle | True | 0 | 0.08 | 0 |
| Household Size | 4 | 3 | 0.05 | 0.15 |
| **Total** | | | **1.0** | **0.15** |

**Final Score:** 0.15 × 10 = **1.5** → **NON_POOR** ✓

### Step 8: Activate and Score

Once validated:

1. **Set Active = True** on the scoring model
2. **Test on a few real households** to verify calculations
3. **Run batch scoring** for your full registry:
   - Go to **Scoring → Actions → Batch Calculate Scores**
   - Select your PMT model
   - Choose target population (e.g., all households)
   - Schedule or run immediately

## Urban vs. Rural Models

Different contexts need different indicators and weights:

| Indicator | Rural Weight | Urban Weight | Rationale |
|-----------|--------------|--------------|-----------|
| Land ownership | 0.20 | 0.05 | More relevant in rural areas |
| Vehicle ownership | 0.10 | 0.18 | More indicative in urban areas |
| Housing materials | 0.35 | 0.25 | Stronger predictor in rural |
| Utilities access | 0.20 | 0.35 | More variation in urban |

**Best practice:** Create separate models for urban and rural contexts if coefficients differ significantly.

## Updating PMT Models

When national consumption surveys are updated or poverty lines change:

1. **Create new model version** (e.g., "PMT_2025_RURAL")
2. **Update weights** based on new survey data
3. **Adjust thresholds** to match new poverty lines
4. **Test on sample** to compare with old model
5. **Activate new model** and deactivate old
6. **Re-score population** to get updated classifications

## Integration with Programs

Link PMT scores to program eligibility:

### Option 1: Classification-Based

In your eligibility manager:

| Field | Value |
|-------|-------|
| Scoring Model | PMT_2024_RURAL |
| Required Classifications | POOR, EXTREME_POOR |

Households classified as "Poor" or "Extremely Poor" are eligible.

### Option 2: Score-Based

In your eligibility manager:

| Field | Value |
|-------|-------|
| Scoring Model | PMT_2024_RURAL |
| Minimum Score | 50.0 |
| Maximum Score | 100.0 |

Households scoring 50 or above are eligible.

### Option 3: Tiered Benefits

Different benefit amounts based on poverty level:

| Classification | Monthly Benefit |
|----------------|-----------------|
| EXTREME_POOR | $150 |
| POOR | $100 |
| NEAR_POOR | $50 |
| NON_POOR | Not eligible |

Configure in entitlement manager using classification-based benefit tiers.

## Common Patterns

### Pattern 1: Philippines Listahanan-Style

- 8-12 indicators
- Focus on housing materials, assets, utilities
- Thresholds: Poor vs. Non-Poor (simple binary)
- Calculation: Weighted sum with survey-derived coefficients

### Pattern 2: World Bank Recommended

- 10-15 indicators
- Include education level of household head
- Include dependency ratio (calculated indicator)
- Thresholds: Multiple poverty levels aligned with national poverty line

### Pattern 3: Hybrid PMT + Community Validation

- Base PMT score (weighted 70%)
- Community validation score (weighted 30%)
- Combines quantitative and qualitative assessment

## Are You Stuck?

**Weights don't add up to 1.0?**
That's okay if you're using a 0-100 scale. Just make sure your thresholds align with the possible score range. Alternatively, normalize weights to sum to 1.0.

**Scores are too clustered in one range?**
Review your value mappings. Make sure high-poverty indicators use higher scores (e.g., salvaged materials = 10, not 1).

**Classifications don't match reality?**
Thresholds may need adjustment. Compare your score distribution to actual poverty rates in the population. Use histogram analysis to find natural cutoff points.

**Urban and rural households scoring incorrectly?**
Create separate models. Urban households may have better housing but face higher costs. Rural households may own land but lack cash income.

**Model validation failing?**
Check that all field paths are valid. Ensure test households have data for required indicators. Review calculation logs for errors.

**Need to recalculate scores?**
You can trigger batch recalculation from **Scoring → Actions**. Existing scores are archived, not deleted, so you can compare changes.

## Best Practices

1. **Use survey data:** Derive weights from household income/expenditure surveys when possible
2. **Test thoroughly:** Run calculations on diverse household types before going live
3. **Document assumptions:** Note why specific weights and thresholds were chosen
4. **Version models:** Track model versions and effective dates for auditing
5. **Monitor distribution:** After batch scoring, review the classification distribution
6. **Plan updates:** Schedule regular model reviews (e.g., every 2-3 years)
7. **Communicate transparently:** Make scoring methodology available to stakeholders

## Security Considerations

PMT scores reveal sensitive poverty information:

| Access Level | Can Do |
|--------------|--------|
| **Program Managers** | Create/modify models, view all scores |
| **Field Officers** | Calculate scores, view classifications |
| **Data Entry** | Input household data (no score access) |
| **Beneficiaries** | View their own classification (optional) |

Configure access rights in **Settings → Users & Groups → Scoring Permissions**.

## Next Steps

- **{doc}`vulnerability`** - Add vulnerability scoring for emergency response
- **{doc}`swdi`** - Implement multi-dimensional welfare index
- **{doc}`custom`** - Create custom scoring formulas for specific programs
- **{doc}`/config_guide/eligibility/index`** - Link PMT scores to program eligibility

---

**See also:**
- {doc}`overview` - Scoring fundamentals
- {doc}`/config_guide/variables/index` - Using CEL for complex formulas
