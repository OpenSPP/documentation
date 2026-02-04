---
openspp:
  doc_status: draft
  products: [core]
---

# OpenSPP Studio

This guide is for **implementers** who want to customize OpenSPP through a visual, no-code interface. If you can build a KoBoToolbox form, you can configure OpenSPP Studio.

## What you'll find here

- **Overview** - Studio interface and capabilities
- **Registry Field Builder** - Add custom fields to registrant records
- **Event Type Designer** - Design event types for surveys and assessments
- **Change Request Builder** - Build change workflows with approval

```{toctree}
:hidden:
:maxdepth: 1

overview
registry_field_builder
event_type_designer
change_request_builder
```

## Quick links

- {doc}`overview` - Understand Studio's interface and capabilities
- {doc}`registry_field_builder` - Track program-specific data on registrants
- {doc}`event_type_designer` - Collect survey data from field assessments
- {doc}`change_request_builder` - Create approval workflows for updates

## Getting started

1. **Read the overview** to understand Studio's interface and capabilities
2. **Choose your task**:
   - Need to track program-specific data? → Registry Field Builder
   - Collecting survey data? → Event Type Designer
   - Need approval workflows for updates? → Change Request Builder
   - Setting program eligibility criteria? → Use the Expression Editor under Rules menu

## Common use cases

| I want to... | Use this tool |
|--------------|---------------|
| Track "Pantawid ID" for Philippines beneficiaries | Registry Field Builder |
| Create a vulnerability assessment form | Event Type Designer |
| Create a phone number update request with approval | Change Request Builder |
| Select households with children under 5 and low income | Expression Editor (Rules menu) |

## Are you stuck?

**Can't find the Studio menu?**
You need Studio Editor or Studio Manager permissions. Contact your system administrator.

**Not sure which tool to use?**
Read the {doc}`overview` for guidance on when to use each Studio component.

**Need to do something not covered here?**
Some advanced configurations require developer assistance. See the "What Requires Developers" section in the overview.
