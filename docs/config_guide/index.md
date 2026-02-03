---
openspp:
  doc_status: draft
  products: [core]
---

# Configuration guide

**For: implementers** (M&E teams, technical staff comfortable with Kobo/CommCare level configuration)

This guide covers configuring OpenSPP without code - setting up eligibility rules, formulas, workflows, and system behavior through the OpenSPP Studio interface and configuration files.

## Overview

The Configuration Guide is designed for implementers who need to customize OpenSPP for their specific program requirements. No programming knowledge is required - configuration uses visual tools and simple expression languages.

## Topics covered

- **[OpenSPP Studio](studio/index.md)** - No-code configuration tool (NEW V2)
- **[CEL Expressions](cel/index.md)** - Common Expression Language for rules and formulas
- **[Eligibility rules](eligibility/index.md)** - Configuring who qualifies for programs
- **[Entitlement formulas](entitlement_formulas/index.md)** - Calculating benefit amounts
- **[Vocabulary system](vocabulary/index.md)** - Standardized codes and terminologies (NEW V2)
- **[Variables and indicators](variables/index.md)** - Unified variable system (NEW V2)
- **[Event data](event_data/index.md)** - Capturing external data from surveys and forms (V2 enhanced)
- **[Change request types](change_request_types/index.md)** - Configuring change request workflows (NEW V2)
- **[Consent configuration](consent/index.md)** - Managing data sharing consent (NEW V2)
- **[Role configuration](role_configuration.md)** - Configuring users, roles, and role-based access (and optionally local/area-scoped roles)

```{toctree}
:maxdepth: 2
:hidden:

studio/index
cel/index
eligibility/index
entitlement_formulas/index
vocabulary/index
variables/index
event_data/index
change_request_types/index
consent/index
role_configuration
```

<!-- Hidden until ready: drims/index -->
