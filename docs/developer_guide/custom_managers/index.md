---
openspp:
  doc_status: draft
  products: [core]
---

# Custom program managers

**For: developers**

Learn how to build custom program managers for OpenSPP. The manager pattern is a core extension point that lets you implement custom logic for eligibility, entitlements, cycles, and payments.

Start with the {doc}`manager_pattern` page to understand how managers work, then refer to the specific manager type guides below.

## Topics covered

- **[Manager pattern](manager_pattern.md)**: How the strategy pattern works — wrapper/implementation models, base classes, and extension points
- **Eligibility managers**: Building custom eligibility criteria and rules
- **Entitlement managers**: Creating custom entitlement calculation logic (cash, in-kind)
- **Cycle managers**: Implementing custom program cycle workflows
- **Payment managers**: Building custom payment processing logic

```{toctree}
:maxdepth: 2
:hidden:

manager_pattern
```
