---
openspp:
  doc_status: draft
  products: [core]
---

# Hazard management overview

This guide is for **implementers** configuring hazard and disaster management in OpenSPP. You should understand your emergency response framework but don't need programming knowledge.

## Mental model

Hazard management in OpenSPP has four layers:

| Layer | What it does | Example |
|-------|--------------|---------|
| **Category** | Classifies the type of hazard | Natural → Storm → Typhoon |
| **Incident** | Records a specific disaster event | "Typhoon Rai - Dec 2025" |
| **Impact** | Tracks how individuals are affected | "Household displaced, property damaged" |
| **Geofence** | Defines the geographic response area | Affected municipalities |

Think of it like a disaster response playbook: **categories** are the hazard types you prepare for, **incidents** are the events that actually happen, **impacts** are the damage assessments, and **geofences** are the response zones.

## Key concepts

### Hazard categories

Categories form a hierarchy for classifying hazard types:

| Field | What it means |
|-------|---------------|
| **Name** | Category label (e.g., "Typhoon") |
| **Code** | Unique identifier |
| **Parent** | Parent category in the hierarchy |

Example hierarchy:

```
Natural Hazards
├── Geological
│   ├── Earthquake
│   └── Volcanic Eruption
├── Hydrometeorological
│   ├── Flood
│   ├── Typhoon
│   └── Drought
└── Biological
    ├── Epidemic
    └── Pest Infestation
```

### Hazard incidents

An incident records a specific disaster event:

| Field | What it means |
|-------|---------------|
| **Name** | Incident label (e.g., "Typhoon Rai - Visayas") |
| **Category** | Type of hazard |
| **Start Date** | When the event began |
| **End Date** | When the event ended (if applicable) |
| **Status** | Current phase of response |
| **Severity** | Impact level (1-5 scale) |
| **Affected Areas** | Geographic areas impacted |

#### Incident status lifecycle

```
Alert → Active → Recovery → Closed
```

| Status | Meaning |
|--------|---------|
| **Alert** | Hazard warning issued, preparing response |
| **Active** | Disaster is ongoing, response in progress |
| **Recovery** | Immediate threat passed, recovery operations |
| **Closed** | Response completed |

#### Severity levels

| Level | Label | Description |
|-------|-------|-------------|
| 1 | Minor | Localized damage, few affected |
| 2 | Moderate | Significant damage, hundreds affected |
| 3 | Significant | Widespread damage, thousands affected |
| 4 | Severe | Regional impact, tens of thousands affected |
| 5 | Catastrophic | National impact, mass displacement |

### Impact types

Impact types categorize how registrants are affected. OpenSPP includes 14 pre-configured types across four domains:

| Domain | Impact Types |
|--------|-------------|
| **Physical** | Displacement, Property Damage, Injury, Death |
| **Economic** | Livelihood Loss, Asset Destruction, Crop Loss, Livestock Loss |
| **Health** | Illness, Disability, Psychological Impact |
| **Social** | Family Separation, Community Disruption, Education Disruption |

### Impact records

For each affected registrant:

| Field | What it means |
|-------|---------------|
| **Registrant** | Who is affected |
| **Incident** | Which disaster |
| **Impact Types** | What kinds of damage |
| **Severity** | Individual impact level |
| **Notes** | Additional details |

## Navigation

| Menu | Purpose |
|------|---------|
| **Hazard Categories** | Define hazard classification hierarchy |
| **Hazard Incidents** | Create and manage disaster events |
| **Hazard Impacts** | View individual impact records |
| **Geofences** | Define geographic response areas |

```{figure} /_images/en-us/config_guide/hazard_management/01-hazard-categories.png
:alt: Hazard categories showing hierarchical classification
Hazard categories showing hierarchical classification.
```

```{figure} /_images/en-us/config_guide/hazard_management/02-hazard-incidents.png
:alt: Hazard incidents list showing status and severity
Hazard incidents list showing status and severity.
```

## Common use cases

### Use case 1: Typhoon response

**Goal:** Set up tracking for a typhoon emergency.

**Setup:**
1. Create a Hazard Incident with category = Typhoon, severity = 4
2. Set affected areas (provinces/municipalities)
3. As assessments come in, create impact records for affected households
4. Link emergency cash transfer programs (see {doc}`program_linking`)

### Use case 2: Drought early warning

**Goal:** Track a developing drought for proactive response.

**Setup:**
1. Create a Hazard Incident with category = Drought, status = Alert
2. Set affected agricultural areas
3. Record crop loss impacts as reports come in
4. Escalate to Active when thresholds are met

## Are You Stuck?

**Where do I configure hazard categories?**

Look for **Hazard Categories** in the configuration menu. If you don't see it, ask your administrator to install the **Hazard Management** module.

**Can I modify the pre-configured impact types?**

Yes. Impact types are standard records that can be edited, deactivated, or extended with new types.

**How do I track the same registrant across multiple incidents?**

Each impact record links a registrant to a specific incident. A registrant can have impact records from multiple incidents, allowing you to track cumulative disaster exposure.

**Severity levels - can I customize the scale?**

The 1-5 scale is fixed, but you can define what each level means for your context through operational guidelines.

## Next steps

- {doc}`program_linking` - Link programs to hazard incidents
- {doc}`/config_guide/area_management/overview` - Configure areas for incident mapping
- {doc}`/config_guide/gis/overview` - Visualize incidents on maps
