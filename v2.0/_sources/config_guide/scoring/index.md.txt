---
orphan: true
openspp:
  doc_status: draft
  products: [core]
---

# Scoring & Assessment

This guide is for **implementers** configuring scoring frameworks to assess and rank beneficiaries for program targeting. No code required.

## What You'll Find Here

- **Overview** - Scoring concepts and fundamentals
- **PMT** - Proxy Means Test configuration for poverty targeting
- **Vulnerability** - Crisis response scoring for emergencies
- **SWDI** - Social Welfare Development Index for multi-dimensional assessment
- **Custom** - Build your own scoring models

```{toctree}
:hidden:
:maxdepth: 1

overview
pmt
vulnerability
swdi
custom
```

## Quick Links

- {doc}`overview` - New to scoring? Start here
- {doc}`pmt` - Setting up poverty targeting
- {doc}`vulnerability` - Crisis response scoring
- {doc}`custom` - Creating custom formulas

## What is Scoring?

Scoring transforms household and individual data into numeric assessments that help you:
- **Target** the poorest or most vulnerable households
- **Prioritize** who receives assistance first
- **Classify** beneficiaries into different support levels
- **Track** changes in poverty or vulnerability over time

Scores are calculated from indicators (like housing materials, asset ownership, household size) using weights and formulas you configure.

## Why Use Configurable Scoring?

Traditional social protection systems hardcode scoring formulas, requiring developers to make changes. OpenSPP's configurable approach means:

- **Program managers** can update weights and thresholds without code changes
- **Different programs** can use different scoring models for the same population
- **Governments** can adjust models when policies or research findings change
- **Transparency** is built-in with clear documentation of how scores are calculated

## Common Use Cases

| Use Case | Scoring Type | When to Use |
|----------|--------------|-------------|
| Identify poor households | PMT | National poverty targeting programs |
| Emergency cash transfers | Vulnerability | Disaster response, crisis situations |
| Multi-dimensional welfare | SWDI | Comprehensive social welfare programs |
| Youth employment programs | Custom | Program-specific eligibility criteria |
| Benefit tier determination | Any type | Variable benefit amounts based on need |

---

**Next:** Learn the fundamentals in {doc}`overview`
