---
openspp:
  doc_status: draft
---

# Demo

**Module:** `spp_demo`

## Overview

The Demo module provides core demonstration functionality for OpenSPP, including a data generator with locale-specific providers, sample user data, and demo stories for realistic test scenarios. It serves as the foundation for domain-specific demo modules.

## Purpose

This module is designed to:

- **Generate realistic test data:** Create sample registrants with locale-appropriate names and attributes
- **Provide demo users:** Pre-configure users with appropriate roles for testing
- **Support multiple locales:** Generate culturally appropriate data for different countries
- **Enable rapid prototyping:** Quickly populate a system for demonstrations and training

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `base` | Odoo core framework |
| `spp_base_common` | The OpenSPP base module that provides the main menu, gene... |
| `spp_registry` | Consolidated registry management for individuals, groups,... |
| `spp_vocabulary` | OpenSPP: Vocabulary |
| `job_worker` | Background job worker |
| `spp_security` | Central security definitions for OpenSPP modules |
| `spp_area` | Establishes direct associations between OpenSPP registran... |

### External Dependencies

| Package | Purpose |
| --- | --- |
| `faker` | |

## Key Features

### Data Generator

Generate sample registrant data with configurable options:

| Setting           | Description                          |
| ----------------- | ------------------------------------ |
| Number of Records | How many registrants to create       |
| Locale            | Language/country for name generation |
| Include Groups    | Generate households with members     |
| Group Size Range  | Min/max members per household        |

### Locale Providers

Generate culturally appropriate names for:

| Locale Code | Region              |
| ----------- | ------------------- |
| en_KE       | Kenya (English)     |
| sw_KE       | Kenya (Swahili)     |
| lo_LA       | Laos                |
| si_LK       | Sri Lanka (Sinhala) |
| ta_LK       | Sri Lanka (Tamil)   |

### Demo Users

Pre-configured users for testing different roles:

| User Type     | Description                     |
| ------------- | ------------------------------- |
| Administrator | Full system access              |
| Manager       | Program and registry management |
| Officer       | Data entry and processing       |
| Viewer        | Read-only access                |

### Demo Stories

Realistic scenarios for testing:

- Typical household compositions
- Common registrant attributes
- Representative geographic distributions

### Configuration Settings

Access demo generation settings through Odoo's configuration:

| Setting                 | Description                     |
| ----------------------- | ------------------------------- |
| Demo Generation Enabled | Allow demo data creation        |
| Default Locale          | Default language for generation |
| Batch Size              | Records per background job      |

## Integration

The Demo module provides the foundation for:

- **spp_mis_demo_v2:** SP-MIS specific demo with programs and indicators
- **spp_base_farmer_registry_demo:** Farmer registry demo data
- **spp_case_demo:** Case management demo data
- **spp_grm_demo:** Grievance management demo data
- **spp_event_demo:** Event tracking demo data
