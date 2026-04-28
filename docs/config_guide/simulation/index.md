---
openspp:
  doc_status: draft
  products: [core]
---

# Simulation

This guide is for **implementers** configuring targeting simulations to model and compare program scenarios before rollout.

## Prerequisites

```{important}
The `spp_simulation` module must be installed. See {doc}`/get_started/modules/index` for module installation instructions.
```

## What you'll find here

- **{doc}`overview`** - Simulation concepts, scenario templates, comparison runs, and fairness metrics

```{toctree}
:hidden:
:maxdepth: 1

overview
```

## Quick start

1. Navigate to **Simulation > Simulation Scenario Templates**
2. Review or create **Scenario Templates** with CEL targeting expressions
3. Create a **Simulation Scenario** from a template
4. Run the scenario to see who would be targeted
5. Use **Simulation Comparison** to evaluate multiple scenarios side by side
