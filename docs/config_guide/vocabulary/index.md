---
openspp:
  doc_status: draft
---

# Vocabulary System

**For: Implementers**

The vocabulary system provides standardized codes and terminologies for consistent data collection and reporting across OpenSPP deployments.

## What You'll Learn

This guide shows you how to configure and use vocabularies in OpenSPP to ensure consistent data entry, enable interoperability, and comply with international standards.

## Quick Start

1. **Understand vocabularies** - Learn what they are and why they matter
2. **Browse standard vocabularies** - Explore built-in international standards (ISO, WHO, ILO, UNESCO)
3. **Configure profiles** - Select which codes are active in your deployment
4. **Create custom vocabularies** - Add organization-specific code lists when needed

## Documentation Structure

```{toctree}
:maxdepth: 2
:hidden:

overview
standard_vocabularies
profiles
custom
```

### [Overview](overview.md)

What vocabularies are, how they work, and why use them instead of hardcoded selections.

**Key topics:**
- Vocabulary system architecture
- Namespace URIs and code uniqueness
- Benefits for multi-country deployments

### [Standard Vocabularies](standard_vocabularies.md)

Built-in international standard vocabularies included with OpenSPP.

**Key topics:**
- ISO standards (gender, countries, languages, currencies)
- WHO ICF (disability classification)
- ILO ISCO-08 (occupations)
- UNESCO ISCED (education levels)
- OpenSPP-specific vocabularies

### [Vocabulary Profiles](profiles.md)

Configure deployment-specific subsets of vocabulary codes.

**Key topics:**
- Deployment profiles
- Selecting active codes
- Code inheritance
- Local code extensions

### [Custom Vocabularies](custom.md)

Create and manage organization-specific vocabularies.

**Key topics:**
- Creating new vocabularies
- Adding codes
- Mapping to international standards
- Managing code hierarchies

## Common Tasks

| Task | Where to Look |
|------|---------------|
| Find which codes are available | [Standard Vocabularies](standard_vocabularies.md) |
| Limit gender codes to Male/Female only | [Profiles](profiles.md) |
| Add local terminology (e.g., "Bagyong" for Typhoon) | [Custom Vocabularies](custom.md) → Local Extensions |
| Map custom codes to international standards | [Custom Vocabularies](custom.md) → Code Mappings |
| Add a new vocabulary for program-specific data | [Custom Vocabularies](custom.md) |

## Are You Stuck?

**Can't find a specific code you need?**
Check [Standard Vocabularies](standard_vocabularies.md) first. If it's not there, you can add it via [Custom Vocabularies](custom.md).

**Users are selecting inappropriate codes?**
Use [Vocabulary Profiles](profiles.md) to limit which codes appear in dropdowns.

**Need to use local terminology?**
See the Local Extensions section in [Custom Vocabularies](custom.md).

**Codes not appearing in forms?**
Check that your deployment profile includes those codes (see [Profiles](profiles.md)).

## Related Documentation

- {doc}`/config_guide/cel/index` - Using vocabulary codes in eligibility expressions
- {doc}`/reference/vocabularies/index` - Complete vocabulary reference listing
- {doc}`/config_guide/event_data/index` - Using vocabularies in event data collection

---

**Next:** Start with [Overview](overview.md) to understand the vocabulary system architecture.
