---
openspp:
  doc_status: draft
---

# Vocabulary Integration

**Module:** `spp_cel_vocabulary`

## Overview

Vocabulary-aware CEL functions for robust eligibility rules

## Purpose

This module is designed to:

- **Enable vocabulary-aware CEL expressions:** Provide CEL functions that compare and group vocabulary codes by URI, supporting local code mappings and concept groups.
- **Offer semantic helper shortcuts:** Supply human-readable CEL functions like `is_female()` and `is_head()` that map to concept group membership checks.
- **Cache vocabulary lookups for performance:** Use session-scoped and ORM-level caching to avoid N+1 queries during CEL evaluation.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `spp_cel_domain` | Write simple CEL-like expressions to filter records (Open... |
| `spp_vocabulary` | OpenSPP: Vocabulary |

## Key Features

### Vocabulary Functions

The module registers the following functions for use in CEL expressions:

| Function | Description | Example |
| --- | --- | --- |
| `code(identifier)` | Resolve a vocabulary code by URI or alias | `r.gender_id == code("female")` |
| `code_eq(field, identifier)` | Compare a code field handling local code mappings | `code_eq(r.gender_id, "female")` |
| `in_group(field, group_name)` | Check if a code belongs to a concept group | `in_group(r.gender_id, "feminine_gender")` |

### Semantic Helpers

Shortcut functions that delegate to `in_group()` with predefined concept group names:

| Function | Concept Group | Example |
| --- | --- | --- |
| `is_female(field)` | `feminine_gender` | `is_female(r.gender_id)` |
| `is_male(field)` | `masculine_gender` | `is_male(r.gender_id)` |
| `is_head(field)` | `head_of_household` | `is_head(r.relationship_type_id)` |
| `is_pregnant(field)` | `pregnant_eligible` | `is_pregnant(r.pregnancy_status_id)` |
| `head(member)` | N/A (checks membership type) | `members.exists(m, head(m))` |

The `head()` function checks whether a member holds the "head" membership type in their group, rather than checking a vocabulary code field.

### Domain Translation

The CEL translator is extended to convert vocabulary functions into Odoo domains:

- `in_group()` and semantic helpers produce `OR` domains checking both `uri` and `reference_uri` fields against the group's code URIs.
- `code_eq()` and `code()` comparisons resolve identifiers via alias lookup and build URI-based equality domains.
- Only `==` and `!=` operators are supported for code comparisons.

### Vocabulary Cache

A two-layer caching system optimizes vocabulary lookups:

- **Layer 1 (ORM cache):** Registry-scoped cache in `VocabularyConceptGroup` for group URI sets.
- **Layer 2 (Session cache):** Per-evaluation `VocabularyCache` instance that provides O(1) frozenset membership checks and avoids redundant lookups within a single CEL evaluation session.

## Integration

- **spp_cel_domain:** Extends the CEL translator to handle vocabulary function calls and the CEL function registry for runtime function resolution. Auto-installs when both dependencies are present.
- **spp_vocabulary:** Reads from `spp.vocabulary.code` for code resolution and `spp.vocabulary.concept.group` for group membership checks. Ships predefined concept groups via XML data.
