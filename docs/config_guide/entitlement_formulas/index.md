---
openspp:
  doc_status: draft
  products: [core]
---

# Entitlement formulas

This guide is for **implementers** configuring entitlement formulas to calculate benefit amounts for qualified registrants.

## What are entitlement formulas?

Entitlement formulas define how much each beneficiary receives. They translate policy rules (e.g., "$50 base plus $10 per child") into calculations that OpenSPP applies automatically when preparing entitlements.

```{mermaid}
graph LR
    B[Beneficiary] --> E[Entitlement Manager]
    E --> |Apply formula| C[Calculate amount]
    C --> EN[Entitlement record]
    EN --> P[Payment/Distribution]
```

## How entitlements work in OpenSPP

Each program has an **Entitlement Manager** that controls how benefits are calculated. The manager can have multiple **entitlement items**, each with its own conditions and formulas.

| Component | Purpose |
|-----------|---------|
| **Entitlement Manager** | Container for entitlement configuration |
| **Entitlement Items** | Individual calculation rules |
| **Amount** | Base amount for the item |
| **Multiplier** | Field to multiply the amount by |
| **Condition** | CEL expression determining who gets this item |
| **Formula** | CEL expression for complex calculations |

## Quick start

To configure entitlements for a program:

1. Go to **Programs → Programs** and open your program
2. Click the **Configuration** tab
3. Find the **Entitlement Manager** section
4. Click the gear icon to configure
5. Add entitlement items with amounts and conditions
6. Save the configuration

```{image} /_images/en-us/config_guide/entitlement_formulas/01-entitlement-manager-overview.png
:alt: Entitlement Manager section in program configuration
:class: img-fluid
```

## What you'll find here

```{toctree}
:maxdepth: 1
:hidden:

cash_calculations
inkind_baskets
formula_library
dynamic_entitlements
conditional_logic
```

| Guide | Description |
|-------|-------------|
| {doc}`cash_calculations` | Configure cash entitlement amounts and multipliers |
| {doc}`inkind_baskets` | Set up in-kind products and baskets |
| {doc}`formula_library` | Pre-built formulas for common scenarios |
| {doc}`dynamic_entitlements` | Variable amounts based on household composition |
| {doc}`conditional_logic` | Different formulas for different beneficiary types |

## Entitlement types

OpenSPP supports different entitlement types:

| Type | Description | Use case |
|------|-------------|----------|
| **Cash** | Monetary payments | Cash transfer programs |
| **In-Kind** | Physical goods | Food distribution, supplies |
| **Basket** | Predefined product bundles | Standardized aid packages |

## Common calculation patterns

| Scenario | Configuration |
|----------|---------------|
| Fixed amount for all | Amount: `500`, No multiplier |
| Per household member | Amount: `100`, Multiplier: `household_size` |
| Base + per child | Item 1: `300` (all), Item 2: `50` per child under 5 |
| Maximum cap | Amount with multiplier, Max amount: `1000` |

See {doc}`cash_calculations` for detailed configuration.

## Are you stuck?

**Entitlements are $0?**
Check that entitlement items are configured and conditions match your beneficiaries.

**Formula shows an error?**
CEL formulas use `base_amount` for the item's amount value. Check syntax and field names.

**Need complex calculations?**
See {doc}`formula_library` for pre-built patterns or {doc}`conditional_logic` for advanced scenarios.
