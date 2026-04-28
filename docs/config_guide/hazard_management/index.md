---
openspp:
  doc_status: draft
  products: [core]
---

# Hazard management

This guide is for **implementers** configuring disaster and hazard classification, incident tracking, and impact assessment for emergency response programs.

## Prerequisites

```{important}
The `spp_hazard` module must be installed. See {doc}`/get_started/modules/index` for module installation instructions.
```

## What you'll find here

- **{doc}`overview`** - Hazard categories, incident lifecycle, impact types, and severity levels
- **{doc}`program_linking`** - Linking emergency programs to hazard incidents

```{toctree}
:hidden:
:maxdepth: 1

overview
program_linking
```

## Quick start

1. Define **Hazard Categories** in a hierarchy (e.g., Natural → Storm → Typhoon)
2. When a disaster occurs, create a **Hazard Incident** with severity and affected areas
3. Record **Impacts** on affected registrants
4. Link emergency **Programs** to the incident for targeted response
