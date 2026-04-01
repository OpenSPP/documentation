---
openspp:
  doc_status: draft
  products: [core]
---

# Mixins

**For: developers**

OpenSPP provides several mixins that add common functionality to your models. Mixins are abstract models — you add them to your model's `_inherit` list to gain their fields and methods.

## Available mixins

| Mixin                               | Module                  | Purpose                                     |
| ----------------------------------- | ----------------------- | ------------------------------------------- |
| `spp.approval.mixin`                | `spp_approval`          | Multi-tier approval workflows               |
| `spp.mixin.source.tracking`         | `spp_source_tracking`   | Data provenance tracking                    |
| `spp.disable.edit.mixin`            | `spp_programs`          | Conditionally disable form editing          |
| `spp.job.relate.mixin`              | `spp_programs`          | Link records to background jobs             |
| `spp.versioned.mixin`               | `spp_versioning`        | Record versioning with scheduled activation |
| `spp.consent.mixin`                 | `spp_consent`           | Consent management for data sharing         |
| `spp.studio.mixin`                  | `spp_studio`            | Studio no-code configuration support        |
| `spp.data.cache.invalidation.mixin` | `spp_cel_domain`        | CEL cache invalidation triggers             |
| `spp.cr.conflict.mixin`             | `spp_change_request_v2` | Change request conflict detection           |

## Approval mixin

The most commonly used mixin. Adds a multi-tier approval workflow to any model.

### Usage

```python
class MyModel(models.Model):
    _name = "spp.my.feature"
    _inherit = ["mail.thread", "mail.activity.mixin", "spp.approval.mixin"]
```

```{important}
`spp.approval.mixin` requires `mail.thread` and `mail.activity.mixin` to be in the inherit list. The approval workflow uses mail activities to notify approvers.
```

### What it provides

- `approval_state` field (`pending`, `approved`, `rejected`)
- `approval_review_ids` — linked approval review records
- Methods for submitting, approving, and rejecting
- Integration with `spp.approval.definition` for configuring who can approve

### Adding to your module

1. Add `spp_approval` to your manifest's `depends`
2. Add the mixin to your model's `_inherit`
3. Add approval state fields to your form view
4. Configure an approval definition through the UI or data files

## Source tracking mixin

Tracks where data originated and how it was last updated. Useful for models that receive data from external sources (imports, APIs, field surveys).

### Usage

```python
class MyModel(models.Model):
    _name = "spp.my.feature"
    _inherit = ["spp.mixin.source.tracking"]
```

### What it provides

| Field                   | Type      | Description                                                               |
| ----------------------- | --------- | ------------------------------------------------------------------------- |
| `source_system`         | Char      | Original source (immutable after create)                                  |
| `source_reference`      | Char      | External reference ID (immutable after create)                            |
| `collection_method`     | Selection | How data was collected (`manual`, `import`, `api`, `survey`, `migration`) |
| `collection_date`       | Datetime  | When data was collected                                                   |
| `last_update_system`    | Char      | System that last updated the record                                       |
| `last_update_reference` | Char      | External reference of the update                                          |

The creation fields (`source_system`, `source_reference`) are set once on create and cannot be changed. Update fields (`last_update_system`, `last_update_reference`) are updated on each write.

## Disable edit mixin

Conditionally makes a form read-only based on a domain filter. Useful for preventing edits on records in certain states.

### Usage

```python
class MyModel(models.Model):
    _name = "spp.my.feature"
    _inherit = ["spp.disable.edit.mixin"]

    DISABLE_EDIT_DOMAIN = [("state", "=", "closed")]
```

When a record matches the `DISABLE_EDIT_DOMAIN`, the form view's edit button is hidden via injected CSS. This is a UI-level control, not a security mechanism — use record rules for actual access control.

## Versioned mixin

Adds record versioning with support for scheduled activation. Records can have future versions that automatically become active at a specified date.

### Usage

```python
class MyModel(models.Model):
    _name = "spp.my.feature"
    _inherit = ["spp.versioned.mixin"]
```

Add `spp_versioning` to your manifest's `depends`.

## Combining mixins

Mixins can be combined as needed:

```python
class MyModel(models.Model):
    _name = "spp.my.feature"
    _description = "My Feature"
    _inherit = [
        "mail.thread",
        "mail.activity.mixin",
        "spp.approval.mixin",
        "spp.mixin.source.tracking",
        "spp.disable.edit.mixin",
    ]

    DISABLE_EDIT_DOMAIN = [("approval_state", "=", "approved")]
```

When combining mixins, make sure to add all their parent modules to your manifest's `depends` list.
