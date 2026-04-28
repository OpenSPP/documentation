---
openspp:
  doc_status: draft
  products: [core]
---

# Case management

This guide is for **implementers** configuring case management workflows for social protection, child welfare, disability support, and other individual-level interventions.

## Prerequisites

```{important}
The `spp_case_base` module must be installed. See {doc}`/get_started/modules/index` for module installation instructions.
```

## What you'll find here

- **{doc}`overview`** - Case concepts, types, domains, and navigation
- **{doc}`stages`** - Case lifecycle stages, phase requirements, and closure reasons
- **{doc}`teams`** - Team configuration, caseloads, risk factors, and vulnerability categories

```{toctree}
:hidden:
:maxdepth: 1

overview
stages
teams
```

## Quick start

1. From the menu, click **Case Management**, then click **Configuration**, then click **Case Types**
2. Create a **Case Type** for each program domain (e.g., "Child Protection", "Disability")
3. Define **Case Stages** for the lifecycle (e.g., Intake → Assessment → Planning → Closure)
4. Create **Case Teams** and assign team members
5. Configure **Risk Factors** and **Vulnerabilities** for assessment frameworks
