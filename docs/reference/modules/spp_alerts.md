---
openspp:
  doc_status: draft
---

# Alerts

**Module:** `spp_alerts`

## Overview

Generic alert engine for threshold monitoring, expiry tracking, and deadline management across OpenSPP modules.

## Purpose

This module is designed to:

- **Monitor thresholds and deadlines:** Automatically detect when numeric fields exceed thresholds or date fields approach deadlines across any Odoo model.
- **Manage alert lifecycle:** Track alerts through active, acknowledged, and resolved states with full audit trail.
- **Configure monitoring rules:** Define reusable rules that specify what to monitor, how to compare values, and what priority to assign.
- **Schedule automated evaluation:** Run alert rules on a cron schedule to continuously monitor system conditions without manual intervention.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `base` | Odoo core framework |
| `mail` | Communication and activity tracking |
| `spp_security` | Central security definitions for OpenSPP modules |
| `spp_vocabulary` | OpenSPP: Vocabulary |

## Key Features

### Alert Management

Alerts are the core records that represent detected conditions requiring attention.

| Field | Description |
| --- | --- |
| Reference | Auto-generated unique identifier (e.g., ALT/0001) |
| Alert Type | Classification from the alerts vocabulary |
| Priority | Low, Medium, High, or Critical |
| State | Active, Acknowledged, or Resolved |
| Source Record | Link to the record that triggered the alert |
| Current Value / Threshold | Numeric values for threshold-based alerts |
| Days Until | Days remaining for deadline-based alerts |

Alerts support a three-step workflow: **Active** (newly raised) -> **Acknowledged** (seen and being investigated) -> **Resolved** (addressed with resolution notes).

### Alert Rules

Rules define the monitoring criteria for automatically creating alerts. Two rule types are supported:

| Rule Type | Description |
| --- | --- |
| Threshold | Compares a numeric field against a configured value using operators: <, <=, >, >=, = |
| Date / Deadline | Checks if a date field is within N days of today |

Each rule specifies a model to monitor, an optional domain filter, and a default priority. The rule engine checks for existing active/acknowledged alerts before creating duplicates.

### Scheduled Evaluation

A cron job (`_cron_evaluate_rules`) periodically evaluates all active rules. Each rule searches its monitored model, applies the domain filter, and creates alerts for records that match the threshold or deadline condition.

## Integration

- **spp_vocabulary:** Alert types are managed as vocabulary codes under the `urn:openspp:vocab:alerts` namespace, allowing flexible classification without code changes.
- **mail:** Alerts inherit `mail.thread` for change tracking and message history on each alert record.
- **Consumer modules:** Other modules (e.g., spp_drims) can extend `spp.alert` and `spp.alert.rule` to add domain-specific fields and behaviors.
