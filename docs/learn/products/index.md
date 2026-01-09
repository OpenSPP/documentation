---
openspp:
  doc_status: draft
  products: [core]
---

# OpenSPP Products

OpenSPP offers flexible products tailored to different social protection needs. Each product builds on a common foundation, adding specialized capabilities for your use case.

**For:** Decision-makers evaluating OpenSPP, implementers planning deployments

## Choose Your Product

| Product | Description | Best For |
|---------|-------------|----------|
| {doc}`social_registry` | Registry for identifying and assessing vulnerable populations | National registries, humanitarian registration |
| {doc}`sp_mis` | Full program management with eligibility, enrollment, and payments | Cash transfers, social assistance programs |
| {doc}`farmer_registry` | Specialized registry for agricultural households with GIS integration | Agricultural support, rural development |
| {doc}`drims` | Disaster response inventory and distribution management | Humanitarian organizations, emergency response |

## Product Architecture

All OpenSPP products share a common foundation and can be combined:

```{mermaid}
graph TB
    subgraph "Specialized Products"
        FR[Farmer Registry]
        DRIMS[DRIMS]
    end

    subgraph "Core Products"
        MIS[SP-MIS]
        SR[Social Registry]
    end

    subgraph "Foundation"
        BASE[OpenSPP Base]
    end

    FR --> SR
    DRIMS --> BASE
    MIS --> SR
    SR --> BASE
```

- **Social Registry** - Core registration, eligibility assessment, and data management
- **SP-MIS** - Extends Social Registry with programs, payment cycles, and monitoring
- **Farmer Registry** - Extends Social Registry with agricultural data and GIS
- **DRIMS** - Standalone inventory and dispatch management for disaster response

## Getting Started

1. **Evaluate** - Install using {doc}`/get_started/installation/docker` with a demo module
2. **Learn** - Read the product page for your use case
3. **Configure** - Follow the configuration guides for your product
4. **Extend** - Build custom modules using the developer guides

```{toctree}
:maxdepth: 1
:hidden:

social_registry
sp_mis
farmer_registry
drims
```
