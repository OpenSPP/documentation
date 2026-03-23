---
openspp:
  doc_status: draft
---

# Programs Bridge

**Module:** `spp_scoring_programs`

## Overview

Integrates scoring with program eligibility and entitlements

## Purpose

This module is designed to:

- **Use scoring for program eligibility:** Determine whether registrants qualify for a program based on their score or classification from a scoring model.
- **Track scores on program membership:** Record the enrollment score and classification, and compute the latest score for each program member.
- **Auto-score on enrollment:** Optionally calculate scores automatically when registrants are enrolled in a program.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `spp_scoring` | Configurable scoring and assessment framework for benefic... |
| `spp_programs` | Manage cash and in-kind entitlements, integrate with inve... |

## Key Features

### Scoring-Based Eligibility

Extends `spp.program` with scoring eligibility settings:

| Field | Description |
| --- | --- |
| Scoring Model | Active scoring model used for eligibility checks |
| Use Scoring for Eligibility | Enable/disable scoring-based eligibility on the program |
| Minimum Score | Minimum score required for eligibility (inclusive) |
| Maximum Score | Maximum score allowed for eligibility (inclusive) |
| Required Classifications | Comma-separated classification codes that qualify (e.g., `POOR,EXTREME_POOR`) |
| Auto-Score on Enrollment | Automatically calculate score when a registrant is enrolled |
| Maximum Score Age (Days) | How old an existing score can be before recalculation (default: 180 days) |

Eligibility can be checked by score range or by classification code. The module hooks into pre-enrollment validation to reject ineligible registrants and post-enrollment to trigger automatic scoring.

### Program Membership Scoring

Extends `spp.program.membership` with:

| Field | Description |
| --- | --- |
| Enrollment Score | Score at the time of enrollment |
| Enrollment Classification | Classification at the time of enrollment |
| Latest Score | Computed field showing the most recent score |
| Latest Classification | Computed field showing the most recent classification |

### Scoring Model to Program Link

Extends `spp.scoring.model` with a many-to-many relationship to programs, allowing users to see which programs use each scoring model.

## Integration

- **spp_scoring:** Uses the scoring engine to calculate and retrieve scores. Reuses existing scores when they are within the configured maximum age.
- **spp_programs:** Extends program enrollment with pre/post hooks for eligibility checking and automatic score calculation. This module auto-installs when both `spp_scoring` and `spp_programs` are present.
