---
openspp:
  doc_status: draft
---

# Source Tracking


## Overview

The OpenSPP Source Tracking module provides data provenance capabilities for registrants and related records. It tracks where data originated, how it was collected, and maintains an audit trail through record merges and updates.

## Purpose

This module is designed to:

- **Track data origins:** Record the source system and method for every piece of data
- **Maintain provenance:** Preserve original source information even through updates
- **Support auditing:** Enable compliance audits by tracking data lineage
- **Handle merges:** Preserve source tracking when records are merged

## Module Dependencies

| Dependency       | Description                                |
| ---------------- | ------------------------------------------ |
| **base**         | Core Odoo framework                        |
| **spp_security** | OpenSPP security framework                 |
| **spp_registry** | OpenSPP registry for registrant management |
| **spp_programs** | Program management                         |

## Key Features

### Source Tracking Mixin

The `spp.mixin.source.tracking` abstract model can be inherited by any model requiring provenance tracking.

#### Creation Provenance (Immutable)

| Field             | Description                        |
| ----------------- | ---------------------------------- |
| Source System     | System that created the record     |
| Source Reference  | Original ID in the source system   |
| Collection Method | How data was collected             |
| Collection Date   | When data was originally collected |

#### Update Provenance

| Field                 | Description                                        |
| --------------------- | -------------------------------------------------- |
| Last Update System    | System that made the most recent update            |
| Last Update Reference | Reference for the update (request ID, batch, etc.) |

### Collection Methods

| Method                 | Description                             |
| ---------------------- | --------------------------------------- |
| **Manual Entry**       | Data entered through the UI             |
| **Bulk Import**        | Data loaded via import files            |
| **API**                | Data received through external API      |
| **Mobile App**         | Data collected via mobile application   |
| **Data Migration**     | Data from legacy system migration       |
| **Created from Merge** | Record created during a merge operation |

### Source System Detection

The module automatically detects the source system:

1. Check for explicit `source_system` in context
2. Check for `X-Source-System` HTTP header (external APIs)
3. Detect Odoo web client routes (`/web/`, `/jsonrpc`)
4. Default to `odoo-ui` for standard interactions

### Merge Provenance

When records are merged, the `spp.merge.provenance` model preserves:

| Field         | Description                                |
| ------------- | ------------------------------------------ |
| Survivor ID   | The record that absorbed the merged record |
| Merged ID     | Original database ID of merged record      |
| Merge Date    | When the merge occurred                    |
| Merged By     | User who performed the merge               |
| Merge Reason  | Explanation for the merge                  |
| Data Snapshot | Key fields preserved from merged record    |

Plus all original provenance fields from the merged record.

## Integration

### With spp_registry

The module extends `res.partner` to track:

- Where each registrant's data came from
- How data was collected (survey, import, API, etc.)
- Updates from different systems over time

### With spp_programs

Program membership records can track:

- Source of enrollment data
- System that processed the enrollment
- Original enrollment reference

### API Integration

External systems can set source tracking via:

**HTTP Headers:**

```
X-Source-System: external-mpi
```

**Context Variables:**

```python
self.with_context(
    source_system='kobo',
    source_reference='submission-12345',
    collection_method='mobile'
)
```

## Configuration

### Using the Mixin

To add source tracking to a model:

```python
class MyModel(models.Model):
    _name = "my.model"
    _inherit = ["my.model", "spp.mixin.source.tracking"]
```

### Context Variables

| Variable               | Description                          |
| ---------------------- | ------------------------------------ |
| `source_system`        | Override detected source system      |
| `source_reference`     | Reference ID in source system        |
| `collection_method`    | Override collection method detection |
| `skip_source_tracking` | Skip updating last_update fields     |
| `import_file`          | Automatically detected for imports   |

## Audit Use Cases

### Tracing Data Origins

Query records by source:

- Find all registrants from a specific import batch
- Identify data collected via mobile app
- Track records from legacy migration

### Merge History

The merge provenance enables:

- Reconstructing merged record state
- Auditing merge decisions
- Understanding data consolidation

### Compliance Reporting

Source tracking supports:

- Data lineage documentation
- Collection method verification
- System integration auditing

## Technical Details

### Protected Fields

Original provenance fields are immutable after creation:

- `source_system`
- `source_reference`
- `collection_method`
- `collection_date`

These cannot be modified by `write()` operations.

### Update Tracking

Update provenance is automatically set on every write (unless `skip_source_tracking` context is set).

### Migration Support

The module includes post-migration scripts to:

- Backfill source tracking on existing records
- Handle schema changes during upgrades
