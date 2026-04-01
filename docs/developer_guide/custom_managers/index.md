---
openspp:
  doc_status: draft
  products: [core]
---

# Custom program managers

**For: developers**

Learn how to build custom program managers for OpenSPP. The manager pattern is a core extension point that lets you implement custom logic for eligibility, entitlements, cycles, and payments.

## How to use this section

1. Read {doc}`manager_pattern` to understand how the strategy pattern works — wrapper models, implementation models, and how they connect to programs
2. Read {doc}`building_managers` for a step-by-step guide to creating a custom manager, with a complete eligibility manager example and method references for all manager types

## Topics covered

- **[Manager pattern](manager_pattern.md)**: How the strategy pattern works — wrapper/implementation models, base classes, and extension points
- **[Building a custom manager](building_managers.md)**: Step-by-step guide with a concrete example, registration pattern, and method reference for all manager types
- **[Example: CCT program managers](example_cct.md)**: Complete module with eligibility, entitlement, and cycle managers for a conditional cash transfer program

```{toctree}
:maxdepth: 2
:hidden:

manager_pattern
building_managers
example_cct
```
