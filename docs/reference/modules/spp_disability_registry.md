---
openspp:
  doc_status: draft
---

# Disability Registry

**Module:** `spp_disability_registry`

## Overview

Disability assessment and registry management for social protection

## Purpose

This module is designed to:

- **Assess disability status:** Record structured disability assessments using the Washington Group Short Set (WG-SS) for adults and the Child Functioning Module (CFM) for children, with automatic age-based assessment type selection.
- **Track assistive devices:** Manage assistive device needs, requests, and provisions for registrants with disabilities.
- **Compute disability indicators:** Automatically determine disability status based on WG standard thresholds (any domain with "a lot of difficulty" or "cannot do at all").
- **Schedule reassessments:** Set review categories (improvement expected, possible, or not expected) that compute next review dates automatically.
- **Provide CEL functions:** Register disability-related functions for use in program eligibility and entitlement calculations.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `spp_registry` | Consolidated registry management for individuals, groups,... |
| `spp_vocabulary` | OpenSPP: Vocabulary |
| `spp_approval` | Standardized approval workflows with multi-tier sequencin... |
| `spp_cel_domain` | Write simple CEL-like expressions to filter records (Open... |

## Key Features

### Disability Assessments

The assessment model (`spp.disability.assessment`) captures structured disability data with approval workflows.

| Field | Description |
| --- | --- |
| Assessment Type | Automatically computed from age: WG-SS (18+), CFM 5-17, CFM 2-4 |
| WG-SS Domains | Six domains: seeing, hearing, walking, remembering, self-care, communicating |
| Difficulty Levels | None, Some difficulty, A lot of difficulty, Cannot do at all |
| Impairment Classification | Type, cause, and severity using DCI-aligned vocabulary codes |
| Review Category | Improvement Expected (12 mo), Possible (3 yr), Not Expected (6 yr) |
| Proxy Response | Tracks whether responses were provided by a proxy and the relationship |

### Computed Disability Status

- `has_disability` is set to `True` when any WG domain has "a lot of difficulty" or "cannot do at all"
- `wg_domain_count` counts the number of domains with severe difficulty
- The latest approved assessment automatically becomes the registrant's current assessment

### Assistive Devices

Tracks assistive devices (`spp.assistive.device`) linked to registrants with vocabulary-based device types and a status workflow: Needed, Requested, Provided. An `has_unmet_device_need` flag on the registrant indicates outstanding needs.

### CEL Functions for Eligibility

The module registers six CEL functions for use in program eligibility rules:

| Function | Description |
| --- | --- |
| `has_disability(r)` | Check if registrant has approved disability status |
| `disability_severity(r)` | Get the disability severity vocabulary code |
| `is_severe_disability(r)` | Check for severe or profound disability (uses concept groups) |
| `household_has_pwd(r)` | Check if any active household member has a disability |
| `household_pwd_count(r)` | Count household members with disability |
| `needs_reassessment(r)` | Check if next review date is past or today |

## Integration

- **spp_registry:** Extends `res.partner` with disability assessment history, current status fields, and assistive device tracking on individual registrants.
- **spp_approval:** Assessments use the approval mixin for multi-tier review before becoming the registrant's current assessment.
- **spp_vocabulary:** Impairment types, causes, severity levels, and device types are defined as vocabulary codes with DCI-aligned namespace URIs.
- **spp_cel_domain:** Registers disability CEL functions for building eligibility expressions in programs.
