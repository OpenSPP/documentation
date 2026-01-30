---
openspp:
  doc_status: draft
  products: [programs]
  applies_to:
    - sp_mis
---

# Programs

**Applies to:** SP-MIS

This guide is for **users** who manage social protection programs, including enrollment, eligibility, and program cycles.

## Overview

Programs in OpenSPP represent your social protection interventions. Each program defines who is eligible, what benefits they receive, and how those benefits are distributed over time through cycles.

A typical program workflow follows these steps:

1. **Create a program** with eligibility rules
2. **Import registrants** who may qualify
3. **Verify eligibility** and enroll beneficiaries
4. **Create cycles** for each distribution period
5. **Generate entitlements** for enrolled beneficiaries
6. **Approve and distribute** benefits

## Key concepts

| Term | What it means |
|------|---------------|
| **Program** | A social protection intervention (e.g., cash transfer, food assistance) |
| **Cycle** | A time period during which benefits are calculated and distributed |
| **Enrollment** | Adding a beneficiary to a program |
| **Eligibility** | Rules that determine who qualifies for a program |
| **Entitlement** | The specific benefit amount a beneficiary receives per cycle |
| **Beneficiary** | A registrant who is enrolled and receiving benefits |

## Before you start

You need one of these access levels:

| Role | What You Can Do |
|------|-----------------|
| **Program Viewer** | View programs and beneficiary lists |
| **Program Officer** | Manage enrollments and cycles |
| **Program Manager** | Full access including configuration |
| **Program Validator** | Approve cycles and entitlements |

If you cannot see the **Programs** menu, contact your administrator.

## In this section

```{toctree}
:maxdepth: 1

understanding_programs
program_cycles
enroll_beneficiaries
manage_entitlements
```

## Are you stuck?

**Cannot find the Programs menu?**
You may not have the required access. Contact your administrator to request Program Viewer or Program Officer access.

**Cannot find a specific program?**
Use the search bar or filters. You may only see programs assigned to your company or region.

**Program shows as "Ended"?**
Ended programs are read-only. Contact a Program Manager if the program needs to be reactivated.

## Next steps

- {doc}`understanding_programs` - Learn how programs, cycles, and entitlements work together
- {doc}`enroll_beneficiaries` - Add registrants to a program
