---
openspp:
  doc_status: draft
---

# Audit — Programs

**Module:** `spp_audit_programs`

## Overview

Audit rules for program and cycle models.

## Purpose

This module is designed to:

- **Audit program activity:** provide the audit rules that track changes to programs, cycles and their manager models.
- **Keep core audit program-free:** carry the program/cycle audit configuration so `spp_audit` can be installed without the Programs stack.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `spp_audit` | Comprehensively tracks all data modifications and user ac... |
| `spp_programs` | Manage programs, cycles, beneficiary enrollment, entitlem... |

## Key Features

- **Program and cycle audit rules:** creates rules for `spp.program`, `spp.cycle` and the related program/cycle manager models.
- **Data-only:** ships no models or views; the rules are created from data via `spp.audit.rule`.

## Integration

- Companion to `spp_audit`. Auto-installs when both `spp_audit` and `spp_programs` are present.
