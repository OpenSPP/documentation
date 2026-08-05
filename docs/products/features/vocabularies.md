---
myst:
  html_meta:
    "title": "Standardized Vocabularies"
    "description": "OpenSPP's vocabulary system for standardized, hierarchical, and extensible classification codes"
    "keywords": "OpenSPP, vocabulary, classification, taxonomy, standards, interoperability, social protection"
---

# Standardized vocabularies

OpenSPP's vocabulary system provides standardized, hierarchical, and extensible classification codes — genders, relationship types, disability categories, land use types, document types, and more — used consistently across the registry, eligibility rules, and reporting.

## Consistent classification across programs and countries

Social protection platforms need to classify all kinds of things consistently — genders, relationships, disability categories, land use types, document types — and different programs, countries, and external partners often expect different standards for the same concept. Hard-coding these classifications into application logic makes it difficult to adapt to local contexts, support multiple languages, or align with international reporting requirements without developer involvement for every new code or category.

OpenSPP's vocabulary system addresses this by treating classification codes as configurable, hierarchical, standards-aware data rather than fixed application logic. Vocabularies ship pre-built for common needs — gender, relationship types, disability, marital status, and more — while remaining fully extensible: administrators can add local codes, map them to external standards, and group related codes into reusable concepts that eligibility rules and other features can reference by meaning rather than by a specific code.

## Vocabulary capabilities

* **Standards-aligned code lists**: Vocabularies are identified by globally unique namespace URIs, allowing local codes to align with external standards such as ISO country and currency codes
* **Hierarchical classification**: Organize codes into parent/child trees (for example, broad versus specific disability categories), with built-in protection against circular references
* **Local extensions without code changes**: Administrators can add new codes to a vocabulary through the UI, while system-shipped vocabularies and codes remain protected from accidental modification
* **Cross-vocabulary mapping**: Map codes to other standards or vocabularies with an explicit equivalence relationship (equivalent, wider, narrower, or inexact)
* **Concept groups for portable business logic**: Group codes across vocabularies into reusable concepts (such as "feminine gender," "persons with disability," or "climate hazards") that eligibility rules and other features can reference without hard-coding specific codes
* **Lifecycle management**: Deprecate outdated codes with a pointer to their replacement, without breaking existing records that reference them
* **Multi-language labels**: Code names, definitions, and descriptions are translatable, so the same code displays appropriately in different languages
* **REST API access**: Look up vocabularies and their codes through OpenSPP's REST API for external system integration

OpenSPP ships 19 vocabularies out of the box, including gender, relationship types, group and membership types, marital status, occupation, education level, ethnicity and culture, housing, economic activity, language, country, currency, religion, identification document types, change-request document types, and three disability-related vocabularies (domain, severity, and status).

## Technical implementation

The vocabulary system is delivered through the following modules:

* **[spp_vocabulary](/reference/modules/spp_vocabulary.md)**: Core vocabulary and code classification framework, including hierarchy, mapping, concept groups, and lifecycle management
* **`spp_cel_vocabulary`**: Vocabulary-aware functions for the CEL rules engine, letting eligibility and entitlement rules reference standardized concepts
* **`spp_api_v2_vocabulary`**: REST API for vocabulary and code lookup
* **`spp_farmer_registry_vocabularies`**: Agricultural vocabularies for the farmer registry, covering crop and livestock types, aquaculture, land use and tenure, cultivation methods, irrigation asset types, farm types, and land-holder types
