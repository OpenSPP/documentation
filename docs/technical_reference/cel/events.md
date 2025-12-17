---
openspp:
  doc_status: unverified
---

# Event functions and event aggregations

When the event/CEL integration is installed, CEL expressions can query event data collected for registrants (surveys, visits, assessments, etc.).

This integration adds:

- an `events` relation symbol on registry profiles
- event helper functions (`event`, `has_event`, `events_count`, `events_sum`, `events_avg`, `events_min`, `events_max`)
- Studio support for event aggregation variables

For the user/admin workflow of creating event types and entering events, see {doc}`../../tutorial/event_data`.

## Event relation

In the registry profiles, `events` represents event data records (`spp.event.data`) linked to the current registrant.

Event queries typically only consider active events by default.

## Which event type and field names to use

Event helper functions take an **event type code** (a string), and some functions take a **field name** (a key in the event’s JSON payload).

- For event types created via **Studio → Event Types**, the generated event type code usually looks like `x_evt_<slug>`. You can confirm the exact code by clicking **View Event Type** on the Studio event type and looking at the underlying Event Type record.
- For fields created in Studio event types, the **Technical Name** of the Studio field is the JSON key stored in `spp.event.data.data_json`. That is the name you pass to `event(<type>, <field>)` and related helpers.

## Common patterns

### Check existence

```text
has_event("household_survey", within_days=365)
```

### Count events

```text
events_count("visit", within_days=90) >= 1
```

### Sum/avg/min/max over a field

```text
events_sum("payment", "amount", period=this_year()) > 0
```

### Read a value from an event

```text
event("survey", "income", select="latest", within_months=12, default=0) < 500
```

## Parameters you can use

Event helper functions support named parameters such as:

- `select` (for `event(...)`): which matching event to read (for example latest/first/active)
- temporal filters: `after`, `before`, `within_days`, `within_months`, `period`
- `states`: filter by event state
- `default` (for `event(...)`): fallback value when no event matches
- `where` (for aggregates): additional predicate filtering (may fall back to Python execution depending on configuration)

## Studio: event aggregation variables

In Studio → Variables, you can define an **Aggregate** variable targeting **Events**.

This builds expressions like:

```text
events_count("visit", within_days=90)
events_sum("payment", "amount", period=this_year())
```

```{note}
Developer reference (source code):
- Event profile extensions: `openspp-modules-v2/spp_cel_event/data/cel_profiles.yaml`
- Event translator: `openspp-modules-v2/spp_cel_event/models/cel_event_translator.py`
- Studio event aggregation variable support: `openspp-modules-v2/spp_cel_event/models/cel_variable_event_agg.py`
- Studio event type designer: `openspp-modules-v2/spp_studio_events/models/studio_event_type.py`
```
