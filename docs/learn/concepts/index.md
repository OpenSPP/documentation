# Key Concepts

Understanding the core building blocks of OpenSPP.

**For:** Anyone new to OpenSPP or social protection systems

OpenSPP is built around several key concepts that work together to deliver social protection programs. Understanding these concepts will help you use the platform effectively.

## Core Concepts

The following concepts form the foundation of OpenSPP:

| Concept | Description |
|---------|-------------|
| {doc}`registry` | The central database of individuals, households, and groups |
| {doc}`programs` | Social protection programs that provide benefits to eligible beneficiaries |
| {doc}`cycles` | Time-bound periods during which benefits are distributed |
| {doc}`eligibility` | Rules and criteria that determine who qualifies for a program |
| {doc}`entitlements` | The benefits or amounts that eligible beneficiaries receive |
| {doc}`payments` | The actual disbursement of entitlements to beneficiaries |

## How They Work Together

```
┌─────────────┐
│  REGISTRY   │  ← Individuals & Groups are registered
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  PROGRAMS   │  ← Programs define what benefits are offered
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ ELIGIBILITY │  ← Eligibility rules determine who qualifies
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   CYCLES    │  ← Cycles organize when benefits are distributed
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ENTITLEMENTS │  ← Entitlements calculate what each person gets
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  PAYMENTS   │  ← Payments disburse the actual benefits
└─────────────┘
```

```{toctree}
:maxdepth: 2
:hidden:

registry
programs
cycles
eligibility
entitlements
payments
```
