---
openspp:
  doc_status: draft
---

# Vocabulary


## Overview

The Vocabulary module provides a standardized code list management system for OpenSPP. It enables organizations to maintain consistent terminology across the platform by managing vocabularies such as gender, relationship types, marital status, occupations, and other classification systems used throughout social protection programs.

## Purpose

This module is designed to:

- **Standardize terminology:** Maintain consistent code lists across all OpenSPP modules using international standards (ISO, WHO, ILO) or custom definitions
- **Support interoperability:** Enable data exchange with external systems by using globally unique namespace URIs
- **Manage hierarchical codes:** Support parent/child relationships within vocabularies for complex classification systems
- **Control data quality:** Provide system vocabularies that cannot be modified by end users

## Module Dependencies

| Dependency       | Description                            |
| ---------------- | -------------------------------------- |
| **base**         | Odoo core functionality                |
| **mail**         | Messaging and activity tracking        |
| **spp_security** | OpenSPP security groups and privileges |

## Key Features

### Vocabulary Management

Vocabularies are collections of codes with unique namespace URIs. Each vocabulary can be categorized by domain:

| Domain            | Description                        |
| ----------------- | ---------------------------------- |
| Core              | General-purpose vocabularies       |
| Social Assistance | Social assistance programs         |
| Social Insurance  | Insurance-related codes            |
| Labor             | Employment and labor codes         |
| Disability        | WHO ICF disability classifications |
| Agriculture       | Agricultural sector codes          |
| Health            | Health-related classifications     |
| Education         | Educational level codes            |

### Pre-loaded Vocabularies

The module includes standard vocabularies:

| Vocabulary         | Namespace Example                     |
| ------------------ | ------------------------------------- |
| Gender             | `urn:iso:std:iso:5218`                |
| Relationship Types | `urn:openspp:vocab:relationship`      |
| Marital Status     | `urn:openspp:vocab:marital_status`    |
| Occupation         | `urn:openspp:vocab:occupation`        |
| Education Level    | `urn:openspp:vocab:education_level`   |
| Disability         | `urn:who:icf`                         |
| Housing            | `urn:openspp:vocab:housing`           |
| Economic Activity  | `urn:openspp:vocab:economic_activity` |
| Language           | `urn:openspp:vocab:language`          |
| Country            | `urn:iso:std:iso:3166`                |
| Currency           | `urn:iso:std:iso:4217`                |
| Religion           | `urn:openspp:vocab:religion`          |
| ID Types           | `urn:openspp:vocab:id_type`           |

### Vocabulary Codes

Each vocabulary contains codes with:

- **Code:** Unique identifier within the vocabulary
- **Name:** Human-readable label (translatable)
- **Parent:** Optional parent code for hierarchical vocabularies
- **Active:** Enable/disable codes without deletion

### Vocabulary Mapping

Map codes between different vocabularies or external systems to support data transformation and interoperability.

### Deployment Profiles

Configure which vocabularies and codes are active for specific deployment contexts, allowing customization per country or program.

### Concept Groups

Group related codes across vocabularies for logical organization and easier management.

## Integration

The Vocabulary module integrates with:

- **spp_registry:** Provides code lists for registrant attributes (gender, marital status, education)
- **spp_programs:** Supplies eligibility criteria options and program classifications
- **spp_api_v2:** Exposes vocabularies via REST API for external system integration
- **spp_dci_client:** Maps local codes to DCI-compliant standards for registry interoperability

## Are you stuck?

### Vocabulary namespace already exists

**Symptom:** Error message "Namespace URI is already used by another vocabulary"

**Cause:** Each vocabulary must have a globally unique namespace URI

**Solution:** Use a different namespace URI or find and modify the existing vocabulary with that namespace

### Cannot edit system vocabulary

**Symptom:** Unable to modify codes in a vocabulary marked as "System Vocabulary"

**Cause:** System vocabularies are protected from user modifications to ensure data consistency

**Solution:** Create a custom vocabulary with your own namespace if you need different codes. Contact your administrator if the system vocabulary needs updates.

### Missing vocabulary codes in forms

**Symptom:** Expected options not appearing in dropdown fields

**Cause:** The vocabulary code may be inactive or the vocabulary is not assigned to the deployment profile

**Solution:** Check that both the vocabulary and the specific codes are marked as active. Verify the deployment profile configuration includes the required vocabulary.
