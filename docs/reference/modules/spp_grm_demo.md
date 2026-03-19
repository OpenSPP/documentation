---
openspp:
  doc_status: draft
---

# Demo Data

**Module:** `spp_grm_demo`

## Overview

Demo data generator for Grievance Redress Mechanism

## Purpose

This module is designed to:

- **Generate realistic GRM demo tickets:** Create story-driven and volume-based grievance tickets linked to demo registrants and programs for testing and demonstration.
- **Simulate ticket workflows:** Progress generated tickets through resolution steps, escalation, and closure with backdated timestamps for realistic timelines.
- **Provide a configuration wizard:** Allow users to control the number, distribution, and characteristics of generated tickets through a form-based wizard.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `spp_demo` | Core demo module with data generator and sample data for ... |
| `spp_grm` | Provides a centralized Grievance Redress Mechanism for re... |
| `spp_grm_registry` | Link GRM tickets to OpenSPP registry (registrants) |
| `spp_grm_programs` | Link GRM tickets to OpenSPP programs, entitlements, and p... |
| `spp_security` | Central security definitions for OpenSPP modules |

### External Dependencies

| Package | Purpose |
| --- | --- |
| `faker` | Generate realistic fake data (names, dates, descriptions) for demo tickets |

## Key Features

### Story-Based Tickets

The module includes predefined story tickets tied to demo personas (Juan Dela Cruz, Fatima Al-Rahman, Ibrahim Hassan, Ahmed Said, David Martinez, Maria Santos, Rosa Garcia, Carlos Morales). Each story includes realistic ticket titles, descriptions, categories, resolution notes, and decisions that align with cross-module demo scenarios.

### Volume Ticket Generation

The wizard generates configurable batches of tickets using scenario-based templates with weighted selection. Scenarios cover common complaint types (information requests, payment issues, registration updates).

| Field | Description |
| --- | --- |
| Number of Tickets | How many volume tickets to generate (1-10,000) |
| Days Back | Time range for backdating ticket creation |
| Resolved % | Percentage of tickets that should be closed with a resolution |
| Escalated % | Percentage of open tickets that should be marked as escalated |
| Severity Distribution | Realistic distribution: 35% low, 45% medium, 15% high, 5% critical |
| Link to Programs | Attach tickets to random programs |
| Link to Beneficiaries | Attach tickets to random registrants |
| Assign Teams | Assign tickets to GRM teams |

### Repeat Ticket Detection

The generator builds a repeat pool (10% of beneficiaries) that receives multiple tickets (30% bias), enabling testing of the repeat ticket detection feature in `spp_grm_registry`.

### Demo Data

The module installs predefined ticket categories (General, Payment, Eligibility, Service, Registration) and demo GRM users via XML data files.

## Integration

- **spp_demo:** Uses the scenario loader from `spp_demo` for ticket scenario templates.
- **spp_grm_registry:** Sets `registrant_id`, `household_id`, and `area_id` on generated tickets when registry integration is installed.
- **spp_grm_programs:** Links generated tickets to programs when program integration is installed.
- **spp_grm:** Creates tickets, progresses them through stages, and applies decisions using the core GRM models.
