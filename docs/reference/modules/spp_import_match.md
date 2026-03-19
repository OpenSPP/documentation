---
openspp:
  doc_status: draft
---

# Import Match

**Module:** `spp_import_match`

## Overview

OpenSPP Import Match enhances data import processes by intelligently matching incoming records against existing data, preventing duplication and ensuring registry integrity. It provides configurable matching logic and supports seamless updates to existing records during bulk data onboarding.

## Purpose

This module is designed to:

- **Define match rules:** Configure which fields to use for detecting duplicate records during data import, with support for relational sub-fields and conditional matching.
- **Prevent duplicate records:** Automatically find existing records that match incoming import rows, skipping or overwriting them based on configuration.
- **Support asynchronous imports:** Split large import files into chunks and process them via background jobs to avoid timeouts.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `base` | Odoo core framework |
| `spp_base_common` | The OpenSPP base module that provides the main menu, gene... |
| `base_import` | Data import framework |
| `job_worker` | Background job worker |
| `spp_security` | Central security definitions for OpenSPP modules |

## Key Features

### Import Match Rules

Configurable rules that define how to identify existing records during import.

| Field | Description |
| --- | --- |
| Model | The Odoo model to apply matching against |
| Fields | One or more fields to match on (combined as AND conditions) |
| Sub-Field | For relational fields, a sub-field to match (e.g., `id_type_id/name`) |
| Overwrite Match | When enabled, matched records are updated with imported values instead of skipped |
| Is Conditional | When enabled, the field match only applies if the imported value equals a specified condition value |

Multiple match rules can be defined per model. The system evaluates each rule in sequence order and returns the first single match found. If multiple records match a single rule, a validation error is raised.

### Duplicate Detection During Import

The module overrides the base `load()` method to intercept import operations:

1. Converts imported rows into Odoo field values
2. For each row, checks if an existing record matches using the configured rules
3. Based on the match result:
   - **No match:** Creates a new record
   - **Match found + overwrite disabled:** Skips the row
   - **Match found + overwrite enabled:** Updates the existing record
4. Returns counts of created, skipped, and overwritten records

### Asynchronous Import

For imports exceeding 100 rows, the module automatically:

1. Creates a CSV attachment from the parsed data
2. Splits the data into chunks on record boundaries
3. Queues each chunk as a separate background job with incremental priority
4. Each chunk is processed independently via the job queue

## Integration

- **base_import:** Extends the standard Odoo import wizard (`base_import.import`) to add match rule selection and asynchronous chunked processing.
- **job_worker:** Uses the job queue for processing large imports asynchronously, with each chunk running as a separate queued job.
- **All models:** The `base` model override applies matching logic to any model import when match rules are configured and selected via the import UI context.
