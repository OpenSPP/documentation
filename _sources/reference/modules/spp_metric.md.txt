---
openspp:
  doc_status: draft
---

# Metric

**Module:** `spp_metric`

## Overview

Unified metric foundation for indicators and simulations

## Purpose

This module is designed to:

- **Provide a shared metric foundation:** Define an abstract base model with common fields (identity, presentation, categorization) that concrete metric types inherit to avoid field duplication.
- **Manage metric categories:** Maintain a hierarchical category system for organizing all metric types in displays and reports.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `base` | Odoo core framework |

## Key Features

### Metric Base Model

An abstract model (`spp.metric.base`) that provides shared fields inherited by concrete metric types such as indicators and simulation metrics.

| Field | Description |
| --- | --- |
| Name | Technical identifier (e.g., `children_under_5`) |
| Label | Human-readable display label (translatable) |
| Description | Detailed description of what the metric measures |
| Unit | Unit of measurement (e.g., people, USD, %) |
| Decimal Places | Number of decimal places for display |
| Category | Link to a metric category for organization |
| Sequence | Display order within a category |
| Active | Toggle to hide inactive metrics |

Concrete models inherit this abstract model and add their own type-specific fields. For example, `spp.indicator` adds publication flags and privacy settings, while simulation metrics add CEL expressions and aggregation types.

### Metric Categories

A hierarchical categorization system for organizing metrics.

| Field | Description |
| --- | --- |
| Name | Display name (e.g., Demographics), translatable |
| Code | Unique technical identifier (e.g., `demographics`) |
| Description | Description of what metrics belong in this category |
| Parent Category | Optional parent for hierarchical organization |
| Sequence | Display order |

Categories enforce unique codes and prevent circular parent relationships.

## Integration

- **spp_indicator:** Inherits `spp.metric.base` for indicator identity, presentation, and categorization fields. Uses `spp.metric.category` for indicator grouping.
- **spp_metric_service:** Provides the category model used by metric computation services for organizing breakdown and distribution results.
- **spp_indicator_studio:** Exposes category management views within the Studio configuration interface.
