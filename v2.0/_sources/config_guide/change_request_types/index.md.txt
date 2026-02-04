---
openspp:
  doc_status: draft
  products: [core]
---

# Change request types

This guide is for **implementers** configuring change request workflows for modifying registrant data.

## What you'll find here

Change request types define the controlled workflows for modifying registrant records. Instead of allowing direct edits, change requests ensure all modifications go through approval processes with full audit trails.

- **{doc}`overview`** - Architecture concepts and available detail models
- **{doc}`creating_types`** - Step-by-step guide to create a change request type
- **{doc}`field_mappings`** - Configure how changes are applied to registrants
- **{doc}`conflict_detection`** - Prevent conflicting or duplicate requests
- **{doc}`patterns`** - Common configuration patterns for different scenarios
- **{doc}`custom_detail_models`** - Create custom detail models for specialized needs
- **{doc}`troubleshooting`** - Testing, security, and common issues

## Quick start

To configure a basic change request type:

1. Navigate to **Change Requests → Configuration → Change Request Types**
2. Click **New** to create a new type
3. Enter name, code, and target type (Individual/Group)
4. Select a detail model in the **Detail Model** tab
5. Configure field mappings in the **Apply Configuration** tab
6. Set approval workflow in the **Approval** tab
7. Click **Save** then **Activate**

```{toctree}
:hidden:
:maxdepth: 1

overview
creating_types
field_mappings
conflict_detection
patterns
custom_detail_models
troubleshooting
```

## Related guides

- {doc}`../studio/change_request_builder` - Build change request types in Studio
- {doc}`../event_data/index` - Integrate with event data collection
