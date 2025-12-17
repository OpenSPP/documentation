---
myst:
  html_meta:
    "description": "Configure SWDI-style assessments in OpenSPP using scoring models"
    "property=og:title": "Social Welfare Development Index (SWDI)"
    "keywords": "OpenSPP, SWDI, assessment, scoring"
---

# Social Welfare Development Index (SWDI)

SWDI-style assessments score household welfare based on multiple dimensions (for example housing, education, health,
employment, assets) and typically categorize households to guide program decisions.

In OpenSPP, SWDI-style assessments are configured using the {doc}`scoring_framework` (the `spp_scoring` module).

## Recommended approach

1. Create a **Scoring Model** with:
   - **Category**: *Eligibility Scoring* or *Custom* (depending on how you use the result)
   - **Calculation Method**: *Weighted Sum*
2. Add indicators aligned to your SWDI questionnaire or assessment form.
3. Define thresholds for SWDI bands (for example `LEVEL_1`, `LEVEL_2`, `LEVEL_3`).
4. Activate the model and run scoring (batch scoring is common for periodic re-assessments).

## Tips

- Store the raw assessment answers as structured registrant data (fields or related records) so they can be referenced by
  indicator **Field Paths**.
- If your assessment is collected as events, consider transforming key answers into registry fields (or computed values)
  before scoring.

## Screenshot placeholders (recommended filenames)

- `tutorial/social_welfare_development_index/scoring_model_form.png`: SWDI scoring model configuration
- `tutorial/social_welfare_development_index/score_breakdown.png`: Example result breakdown for a household

