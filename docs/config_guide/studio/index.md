---
openspp:
  doc_status: draft
---

# OpenSPP Studio

**For: Implementers**

OpenSPP Studio is a no-code configuration tool that allows implementers to customize OpenSPP through a visual interface. If you can build a KoBoToolbox form, you can configure OpenSPP Studio.

## What is Studio?

Studio gives you the power to:

- **Add custom fields** to registrant and group records without developer help
- **Design event types** to collect field data from surveys and assessments
- **Build change request workflows** for updating registry information with approval
- **Create eligibility rules** visually without writing code expressions

## Who is Studio for?

This guide is for **implementers** - program staff and M&E teams who configure systems like KoBoToolbox, ODK Collect, or CommCare. You should be comfortable with:

- Building forms and defining fields
- Understanding data concepts (field types, validation, conditions)
- Working with spreadsheets and data

You do NOT need to know Python, SQL, or Odoo development.

## Quick Links

```{toctree}
:maxdepth: 1

overview
registry_field_builder
event_type_designer
change_request_builder
eligibility_rule_builder
```

## Getting Started

1. **Read the overview** to understand Studio's interface and capabilities
2. **Choose your task**:
   - Need to track program-specific data? → Registry Field Builder
   - Collecting survey data? → Event Type Designer
   - Need approval workflows for updates? → Change Request Builder
   - Setting program eligibility criteria? → Eligibility Rule Builder

## Common Use Cases

| I want to... | Use this tool |
|--------------|---------------|
| Track "Pantawid ID" for Philippines beneficiaries | Registry Field Builder |
| Import vulnerability assessments from Kobo | Event Type Designer |
| Create a phone number update request with approval | Change Request Builder |
| Select households with children under 5 and low income | Eligibility Rule Builder |

## Are You Stuck?

**Can't find the Studio menu?**
You need Studio Editor or Studio Manager permissions. Contact your system administrator.

**Not sure which tool to use?**
Read the {doc}`overview` for guidance on when to use each Studio component.

**Need to do something not covered here?**
Some advanced configurations require developer assistance. See the "What Requires Developers" section in the overview.
