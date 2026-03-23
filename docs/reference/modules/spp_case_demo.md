---
openspp:
  doc_status: draft
---

# Demo Data

**Module:** `spp_case_demo`

## Overview

Demo data generator for Case Management

## Purpose

This module is designed to:

- **Generate realistic demo data:** Populate the case management system with configurable volumes of cases, intervention plans, visits, notes, and referrals for testing and demonstration.
- **Provide fixed demo stories:** Create predictable named case scenarios with scripted journeys through the case lifecycle for consistent demonstrations.
- **Supply base configuration:** Install case types (Child Protection, Livelihood Support, etc.) and workflow stages (Intake through Closure) as XML data.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `spp_demo` | Core demo module with data generator and sample data for ... |
| `spp_case_base` | Core case management functionality for OpenSPP |
| `spp_security` | Central security definitions for OpenSPP modules |

### External Dependencies

| Package | Purpose |
| --- | --- |
| `faker` | Generate realistic names, paragraphs, and sentences for demo content |

## Key Features

### Demo Data Wizard

A transient model wizard (`spp.case.demo.generator`) provides configurable generation of case management demo data:

| Setting | Default | Description |
| --- | --- | --- |
| Number of Cases | 25 | Total cases to generate (1 to 5,000) |
| Include Demo Stories | Yes | Generate fixed demo stories with predictable names |
| Days Back | 120 | Distribute case creation dates within this time window |
| % with Plans | 70% | Percentage of cases with intervention plans |
| % with Visits | 60% | Percentage of cases with visit records |
| % with Notes | 80% | Percentage of cases with progress notes |
| % Closed | 40% | Percentage of cases in closed state |
| Link to Beneficiaries | Yes | Link cases to existing registrants |
| Locale | Company country | Faker locale for generating realistic content |

### Demo Stories

Fixed demo stories define specific case scenarios with scripted journeys. Each story specifies a client profile, case configuration, and a sequence of journey actions:

| Action | Description |
| --- | --- |
| intake | Initial case opening |
| create_plan | Create an intervention plan with goals |
| add_intervention | Add an intervention task to the current plan |
| complete_intervention | Mark an intervention as completed |
| home_visit / office_visit | Record a visit |
| progress_note | Add a progress note |
| assessment | Record an assessment |
| add_referral | Create a service referral |
| close_case | Close the case and mark plans as completed |

### Random Case Generation

Beyond fixed stories, the wizard generates random cases with:

- Random case types and stages (weighted toward middle stages)
- Random beneficiary assignments from existing registrants
- Realistic presenting issues (financial hardship, housing assistance, health support, etc.)
- Random intake sources, priorities, and intensity levels
- Backdated creation dates distributed across the configured time window

## Integration

- **spp_case_base:** Creates `spp.case`, `spp.case.intervention.plan`, `spp.case.intervention`, `spp.case.visit`, `spp.case.note`, and `spp.case.referral` records using the base case management models.
- **spp_demo:** Depends on the core demo module infrastructure. Uses `res.partner` registrants as case clients when "Link to Beneficiaries" is enabled.
