---
openspp:
  doc_status: draft
---

# Event Data Integration

**Module:** `spp_cel_event`

## Overview

Integrate event data with CEL expressions for eligibility and entitlement rules

## Purpose

This module is designed to:

- **Query event data in CEL expressions:** Enable CEL expressions to access, filter, and compare values from event data records for eligibility and entitlement rules.
- **Aggregate event data:** Provide count, sum, average, min, and max aggregation functions over event records within CEL expressions.
- **Support temporal filtering:** Allow CEL expressions to filter events by named periods (year, quarter, month, week), relative ranges (within N days/months), and explicit date boundaries.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `spp_cel_domain` | Write simple CEL-like expressions to filter records (Open... |
| `spp_event_data` | Records and tracks events related to individual and group... |
| `spp_studio` | No-code customization interface for OpenSPP |

## Key Features

### Event Access Functions

CEL expressions can access event data using the following functions:

| Function | Description | Example |
| --- | --- | --- |
| `event(type, field)` | Get a field value from a registrant's event | `event('survey').income > 500` |
| `has_event(type)` | Check if a matching event exists | `has_event('assessment', within_days=365)` |
| `events_count(type)` | Count matching events | `events_count('visit', period=this_year()) >= 3` |
| `events_sum(type, field)` | Sum a field across events | `events_sum('payment', 'amount', period='2024')` |
| `events_avg(type, field)` | Average a field across events | `events_avg('survey', 'score') >= 70` |
| `events_min(type, field)` | Minimum field value across events | `events_min('assessment', 'score')` |
| `events_max(type, field)` | Maximum field value across events | `events_max('assessment', 'score')` |

### Event Selection Modes

When multiple events match, the `select` parameter controls which event is used:

| Mode | Behavior |
| --- | --- |
| `auto` | Uses `active` if event type has one-active-per-registrant, otherwise `latest` |
| `active` | Only active events |
| `latest` | Most recent event regardless of state |
| `latest_active` | Most recent active event |
| `first` | Oldest event |
| `any` | Any matching event |

### Temporal Filters

Events can be filtered by time using parameters on event functions:

| Parameter | Description | Example |
| --- | --- | --- |
| `period` | Named period string | `period='2024-Q1'` |
| `within_days` | Events within last N days | `within_days=90` |
| `within_months` | Events within last N months | `within_months=6` |
| `after` | Events on or after a date | `after='2024-01'` |
| `before` | Events on or before a date | `before='2024-06'` |

### Period Helper Functions

Dynamic period generators for use within CEL expressions:

| Function | Returns | Example Output |
| --- | --- | --- |
| `this_year()` | Current year | `'2026'` |
| `last_year()` | Previous year | `'2025'` |
| `this_quarter()` | Current quarter | `'2026-Q1'` |
| `last_quarter()` | Previous quarter | `'2025-Q4'` |
| `this_month()` | Current month | `'2026-03'` |
| `last_month()` | Previous month | `'2026-02'` |
| `quarters_ago(n)` | N quarters back | `'2025-Q3'` |
| `months_ago(n)` | N months back | `'2025-12'` |

Period strings support these formats: `YYYY`, `YYYY-QN`, `YYYY-HN`, `YYYY-MM`, `YYYY-WNN`.

### CEL Variable Event Aggregation

Extends the CEL variable configuration UI to support event-based aggregations. Users can create variables that aggregate over event data by selecting an event type, aggregation function, time range, and field.

### Optimized Execution

The executor uses SQL fast paths for supported operations (simple comparisons, standard aggregations) and falls back to Python evaluation for complex cases such as default values or where predicates.

## Integration

- **spp_cel_domain:** Extends the CEL translator and executor to handle event-specific query plan nodes (`EventValueCompare`, `EventExists`, `EventsAggregate`).
- **spp_event_data:** Queries `spp.event.data` records and `spp.event.type` configuration for selection mode resolution.
- **spp_studio:** Extends the CEL variable form to include event aggregation configuration fields. Auto-installs when all three dependencies are present.
