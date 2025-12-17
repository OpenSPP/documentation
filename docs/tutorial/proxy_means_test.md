# Proxy Means Test (PMT)

This tutorial explains how to configure a Proxy Means Test (PMT) using the **Scoring** framework (`spp_scoring`).

A PMT estimates poverty or welfare status based on observable indicators (for example housing quality, assets, education,
household composition) and then classifies registrants into categories used for targeting.

## Prerequisites

- The **Scoring** app/module is installed (`spp_scoring`).
- You have a Scoring privilege that allows configuration:
  - **Manager** (recommended for creating/activating models and editing thresholds/indicators), or
  - **Officer** (for running batch scoring).
- The registry has the fields you want to score on (PMT is only as good as the data available in your deployment).

```{note}
PMT is typically household-level. In OpenSPP, households are often represented as **group registrants**. You can apply the
same scoring model to individuals or groups depending on how your deployment models registrants.
```

## Step 1 — Create a scoring model for PMT

1. Go to **Scoring → Scoring Models** and click **Create**.
2. Set:
   - **Category**: *Poverty Assessment*
   - **Calculation Method**: *Weighted Sum* (recommended for most PMT models)
   - **Expected Total Weight**: usually `1.0` (so weights are easy to validate)
   - **Strict Mode**: enable only if missing data should make scoring “incomplete”

3. Save the model (do not activate yet).

### Screenshot placeholder

- `tutorial/proxy_means_test/scoring_model_form.png`: Scoring Model form (Basic Information + Calculation)

## Step 2 — Add PMT indicators

Indicators are the components of the PMT. Each indicator reads a value from registrant data and converts it into an
indicator score.

In the Scoring Model form, open the **Indicators** tab and add the indicators you need.

### How indicator configuration works

- **Field Path** uses dot notation (for example `income`, `occupation_id.code`, `group_membership_ids`, etc.).
- **Source Model** defaults to `res.partner` (the registrant record). This works for both individuals and groups, since
  OpenSPP registrants extend `res.partner`.
- **Calculation Type** controls how the field value becomes a score:
  - **Direct Value**: use the numeric value directly
  - **Value Mapping**: map discrete values to scores
  - **Range Mapping**: map numeric ranges to scores
  - **CEL Formula**: compute the indicator score using a CEL expression (advanced)

```{note}
For relational fields (for example Many2one), prefer mapping on a primitive attribute like `.code` or `.name`
(for example `occupation_id.code`) rather than the record itself.
```

### Example indicator patterns (adapt to your deployment)

1. **Income / consumption** (range mapping)
   - Field Path: `income`
   - Calculation Type: *Range Mapping*
   - Value Mappings (examples):
     - `0 → 100` → score `5`
     - `101 → 300` → score `3`
     - `301 → 999999` → score `0`

2. **Housing material** (value mapping)
   - Field Path: `<your_housing_field>`
   - Calculation Type: *Value Mapping*
   - Map each code/value to the appropriate score.

3. **Household size** (direct value or range mapping)
   - Field Path: `<your_household_size_field>`
   - Calculation Type: *Direct Value* (if already normalized), or *Range Mapping*

### Screenshot placeholders

- `tutorial/proxy_means_test/indicators_tab.png`: Indicators tab on a Scoring Model
- `tutorial/proxy_means_test/indicator_form_mapped.png`: Indicator form showing Value Mappings
- `tutorial/proxy_means_test/indicator_form_range.png`: Indicator form showing Range Mappings

## Step 3 — Define PMT classifications (thresholds)

Thresholds map the final score into a classification (for example *EXTREME_POOR*, *POOR*, *NEAR_POOR*, *NON_POOR*).

1. In the Scoring Model form, open the **Thresholds** tab.
2. Add thresholds that cover the expected score range (avoid gaps).

```{note}
When you activate a scoring model, OpenSPP validates that thresholds do not have gaps (for example a gap between the end
of one range and the start of the next).
```

### Screenshot placeholder

- `tutorial/proxy_means_test/thresholds_tab.png`: Thresholds tab showing PMT classifications

## Step 4 — Activate the PMT model

Click **Activate** on the Scoring Model.

Activation validates:

- At least one indicator and one threshold exist
- Indicator field paths are valid
- Threshold ranges have no gaps
- (If set) the total indicator weight matches **Expected Total Weight**

## Step 5 — Run scoring (batch scoring)

To score a population:

1. Go to **Scoring → Batch Scoring**.
2. Select your PMT scoring model.
3. Choose who to score:
   - **Specific Registrants** (manual selection), or
   - **Registrant Filter** (an Odoo domain string)

Example domain to score group registrants (households):

```text
[('is_registrant', '=', True), ('is_group', '=', True)]
```

### Screenshot placeholder

- `tutorial/proxy_means_test/batch_scoring_wizard.png`: Batch Scoring wizard (model + domain)

## Step 6 — Review results and score breakdown

1. Go to **Scoring → Scoring Results**.
2. Open a result to see:
   - score and classification
   - **Score Breakdown** (indicator-by-indicator contributions)

### Screenshot placeholder

- `tutorial/proxy_means_test/scoring_result_breakdown.png`: Scoring Result form showing Score Breakdown

## (Optional) Use PMT to enforce program eligibility

If your deployment uses OpenSPP Programs, scoring can be used as an eligibility rule via the scoring-programs bridge
module (`spp_scoring_programs`, auto-installed when both scoring and programs are installed).

1. Open a Program and go to the **Scoring** tab.
2. Set:
   - **Scoring Model**
   - Enable **Use Scoring for Eligibility**
   - Configure one of:
     - **Required Classifications** (comma-separated codes), or
     - **Minimum Score / Maximum Score**

### Screenshot placeholder

- `tutorial/proxy_means_test/program_scoring_tab.png`: Program form → Scoring tab (eligibility settings)
