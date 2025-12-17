---
myst:
  html_meta:
    "description": "Configure scoring models for targeting and assessments in OpenSPP"
    "property=og:title": "Scoring Framework"
    "keywords": "OpenSPP, scoring, targeting, assessment, PMT"
openspp:
  doc_status: unverified
---

# Scoring framework

OpenSPP provides a configurable **Scoring** framework (`spp_scoring`) that lets implementers compute a score and
classification for registrants using configurable indicators, weights, and thresholds.

This same mechanism can be used for multiple “algorithms”, for example:

- Proxy Means Test (PMT)
- Vulnerability scoring (crisis response)
- Social Welfare Development Index (SWDI)-style assessments
- Custom eligibility or prioritization scoring

## Roles and access

The Scoring app defines privileges under the **Scoring** category:

- **Viewer**: view models and results
- **Officer**: run scoring and view results
- **Manager**: configure and activate scoring models

## Core concepts

### Scoring model

A **Scoring Model** defines:

- how to calculate the total score (most commonly: **Weighted Sum**)
- which indicators contribute to the score
- how the final score maps to classifications (thresholds)

### Indicator

An **Indicator** reads one value from registrant data and turns it into an indicator score:

- The value is taken from a **Field Path** (dot notation) on the registrant.
- The indicator score is then calculated using one of:
  - **Direct Value** (numeric values)
  - **Value Mapping** (discrete values)
  - **Range Mapping** (numeric ranges)
  - **CEL Formula** (advanced)

```{note}
If you need an intermediate computation (for example “children under 5”), prefer defining it once as a **variable** in Studio and then reusing it across scoring and other features. See {doc}`variables_and_expressions`.
```

### Threshold

A **Threshold** maps a final score range to a classification (code, label, and display color).

## Typical workflow

1. **Create a scoring model**: **Scoring → Scoring Models**
2. **Add indicators**: configure field paths, weights, and mappings
3. **Add thresholds**: define the score-to-classification mapping
4. **Activate** the model (activation validates configuration)
5. **Run scoring** on a population: **Scoring → Batch Scoring**
6. **Review results**: **Scoring → Scoring Results** (includes a full score breakdown)

## Screenshot placeholders (recommended filenames)

Use these filenames when capturing screenshots so they can be dropped in without changing the docs later:

- `tutorial/scoring_framework/scoring_menu.png`: Scoring menu entries
- `tutorial/scoring_framework/scoring_model_form.png`: Scoring model form (before activation)
- `tutorial/scoring_framework/indicator_form.png`: Scoring indicator configuration
- `tutorial/scoring_framework/threshold_form.png`: Threshold configuration
- `tutorial/scoring_framework/batch_scoring_wizard.png`: Batch scoring wizard
- `tutorial/scoring_framework/scoring_result_breakdown.png`: Result “Score Breakdown” tab
