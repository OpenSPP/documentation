---
openspp:
  doc_status: draft
---

# Event Data

**For: Implementers**

Event data captures time-based observations about registrants from surveys, field visits, assessments, and external data collection tools. Unlike static profile fields, event data is repeatable, versioned, and maintains source information.

## What You'll Learn

This guide shows you how to configure event types, define custom fields, integrate with ODK/KoboToolbox, and use event data in eligibility rules and program logic.

```{toctree}
:maxdepth: 1

overview
event_types
odk_kobo
field_definitions
```

## Quick Links

| Topic | When to Use |
|-------|-------------|
| {doc}`overview` | Understand event data concepts and use cases |
| {doc}`event_types` | Create and configure event type schemas |
| {doc}`odk_kobo` | Connect mobile data collection tools |
| {doc}`field_definitions` | Define custom fields with validation |

## Prerequisites

Before configuring event data, you should:

- Have **Studio** access in OpenSPP
- Understand your program's data collection requirements
- Know what information you need to capture and how often
- Have familiarity with form builders (like KoboToolbox or CommCare) if integrating external tools

## What's New in V2

OpenSPP V2 enhances event data with:

- **Studio Integration** - Visual event type builder with field library
- **Field Validation** - Range checks, pattern matching, and conditional visibility
- **ODK/Kobo Sync** - Two-way integration with mobile data collection
- **Event Aggregation** - Use event data in CEL expressions for eligibility
- **Field Templates** - Reusable field sets for common assessment types
- **Entry Forms** - Auto-generated data entry wizards

---

*This documentation covers OpenSPP V2 event data configuration for implementers.*
