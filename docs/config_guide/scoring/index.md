---
openspp:
  doc_status: draft
---

# Scoring & Assessment

**For: Implementers**

Configure scoring frameworks to assess and rank beneficiaries for program targeting. OpenSPP V2 provides flexible scoring tools that let you implement Proxy Means Test (PMT), vulnerability assessments, Social Welfare Development Index (SWDI), and custom methodologies—all through configuration, no code required.

## What You'll Learn

This section covers how to set up and manage scoring systems in OpenSPP:

```{toctree}
:maxdepth: 1

overview
pmt
vulnerability
swdi
custom
```

## Quick Start

**New to scoring?** Start with {doc}`overview` to understand how scoring works in OpenSPP.

**Setting up poverty targeting?** Jump to {doc}`pmt` for Proxy Means Test configuration.

**Need vulnerability assessment?** See {doc}`vulnerability` for crisis response scoring.

**Implementing SWDI?** Follow {doc}`swdi` for multi-dimensional welfare assessment.

**Creating custom formulas?** Check {doc}`custom` for building your own scoring models.

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
