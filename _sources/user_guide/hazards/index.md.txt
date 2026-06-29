---
openspp:
  doc_status: draft
  products: [core]
---

# Hazards and incidents

This guide is for **users** — disaster response officers, program staff, and field personnel who record hazard events, assess impacts on registrants, and coordinate emergency responses in OpenSPP.

## What is hazard and incident management?

The hazard and incident module helps you record natural or human-made disasters, assess their impact on the registrants in your system, and link affected populations to emergency response programs. It provides:

- A structured record of disaster events (typhoons, floods, earthquakes, conflict, drought, and more)
- Tools to identify which registrants are in affected geographic areas
- An impact assessment workflow with damage level tracking and verification
- Integration with programs so emergency assistance reaches affected people quickly

## What you'll learn

This section covers:

1. **{doc}`manage_hazards`** — Record hazard incidents, identify affected areas and registrants, assess damage, and move an incident through its lifecycle

## Before you start

You need one of these access levels:

| Role | What you can do |
|------|----------------|
| **Hazard Viewer** | View incidents and impact records (read only) |
| **Hazard Officer** | Create incidents, add affected areas, and record impacts |
| **Hazard Manager** | Full access — create, edit, delete, and configure categories |

If you cannot see the **Hazard and Emergency** menu in the sidebar, contact your administrator to assign you a hazard role.

## Key concepts

| Term | What it means |
|------|---------------|
| **Incident** | A specific hazard event (e.g., "Typhoon Odette – December 2021") |
| **Hazard category** | The type of hazard, organized in a hierarchy (e.g., Natural > Storm > Typhoon) |
| **Severity** | How severe the incident is, rated 1 (minor) to 5 (catastrophic) |
| **Affected area** | A geographic area linked to an incident, with its own severity override |
| **Impact** | A record of how a specific registrant was affected by an incident |
| **Damage level** | The degree of harm to a registrant — Minimal, Moderate, Severe, Critical, Partially damaged, or Totally damaged |
| **Verification status** | Whether an impact record has been confirmed — Reported, Verified, Disputed, or Closed |

## Incident lifecycle

Incidents move through four stages:

```
Alert → Active → Recovery → Closed
```

| Stage | When to use |
|-------|-------------|
| **Alert** | The hazard has been identified but has not yet caused confirmed impacts |
| **Active** | The incident is ongoing and impacts are being assessed |
| **Recovery** | The acute phase has passed and recovery response is underway |
| **Closed** | The incident is fully documented and no further action is needed |

```{toctree}
:maxdepth: 2
:hidden:

manage_hazards
```

## Are you stuck?

**The Hazard and Emergency menu is missing.**
You do not have a hazard role. Ask your administrator to assign you at least Hazard Viewer access.

**I can see incidents but cannot create one.**
You need the Hazard Officer or Hazard Manager role to create incidents.

**I need to link an incident to a program.**
See the programs section of the guide — this requires the Emergency Response configuration on the program itself, which is set up by a program manager.
