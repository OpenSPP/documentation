---
openspp:
  doc_status: draft
---

# API V2 - Vocabulary


## Overview

OpenSPP API V2 - Vocabulary extends the core API V2 module with RESTful endpoints for vocabulary and lookup value retrieval. This module enables external systems to access standardized terminology definitions for consistent data coding across integrations.

## Purpose

This module is designed to:

- **Expose vocabulary definitions:** Provide read access to standardized code lists and terminology
- **Enable data consistency:** Allow external systems to use the same codes as OpenSPP
- **Support namespace URIs:** Expose vocabularies by their globally unique namespace identifiers
- **Facilitate integration:** Help external systems understand valid values for coded fields

## Module Dependencies

| Dependency         | Description                                                   |
| ------------------ | ------------------------------------------------------------- |
| **spp_api_v2**     | Core API V2 module providing authentication and base patterns |
| **spp_vocabulary** | Centralized vocabulary and lookup value management            |

## Key Features

### Vocabulary Listing

Retrieve all vocabularies defined in the system, including their namespace URIs and descriptions. This enables external systems to discover available code lists.

### Code Retrieval

Get all codes for a specific vocabulary using its namespace URI. This allows external systems to synchronize lookup values.

### Public Access

Vocabulary data is reference information that does not require consent-based filtering. All authenticated clients can access vocabulary endpoints.

### Namespace URI Identifiers

Vocabularies are identified by namespace URIs rather than database IDs, ensuring globally unique and portable references.

## API Endpoints

| Endpoint                            | Method | Description                         |
| ----------------------------------- | ------ | ----------------------------------- |
| `/Vocabulary`                       | GET    | List all vocabularies               |
| `/Vocabulary/{namespace_uri}/codes` | GET    | Get codes for a specific vocabulary |

### Vocabulary List Response Fields

| Field         | Type    | Description                           |
| ------------- | ------- | ------------------------------------- |
| namespace_uri | string  | Globally unique vocabulary identifier |
| name          | string  | Human-readable vocabulary name        |
| description   | string  | Vocabulary description                |
| code_count    | integer | Number of codes in the vocabulary     |

### Vocabulary Codes Response Fields

| Field       | Type    | Description              |
| ----------- | ------- | ------------------------ |
| code        | string  | The code value           |
| name        | string  | Human-readable code name |
| description | string  | Code description         |
| sequence    | integer | Display order            |
| active      | boolean | Whether code is active   |

## Common Vocabularies

OpenSPP typically includes vocabularies for:

| Vocabulary   | Namespace URI Example                 | Purpose                   |
| ------------ | ------------------------------------- | ------------------------- |
| Gender       | `urn:openspp:vocabulary:gender`       | Gender identity codes     |
| Relationship | `urn:openspp:vocabulary:relationship` | Family relationship types |
| ID Type      | `urn:openspp:vocabulary:id-type`      | Identifier type codes     |
| Disability   | `urn:openspp:vocabulary:disability`   | Disability category codes |
| Education    | `urn:openspp:vocabulary:education`    | Education level codes     |

## Integration

### With Core API V2

This module extends `spp_api_v2` and inherits:

- OAuth 2.0 authentication
- Namespace URI identifier patterns
- Standard response formats
- Consistent error handling

### With Vocabulary Module

Vocabulary data comes from `spp_vocabulary`, including:

- Vocabulary definitions
- Code lists
- Namespace URI mappings

### With Other API V2 Modules

Vocabularies exposed here are referenced by:

- Individual and Group endpoints (gender, relationship codes)
- Program endpoints (eligibility criteria codes)
- All endpoints using coded values

### With External Systems

Common integration patterns include:

- **Data collection tools:** Synchronize dropdown values with survey forms
- **Partner registries:** Align terminology across systems
- **Reporting systems:** Map codes to display labels
- **Migration tools:** Translate codes between systems

### Auto-Installation

This module auto-installs when both `spp_api_v2` and `spp_vocabulary` are present, ensuring vocabulary endpoints are available whenever the prerequisites exist.

## Are you stuck?

### Vocabulary not found error

**Symptom:** 404 error when requesting vocabulary codes
**Cause:** Invalid namespace URI or vocabulary does not exist
**Solution:** Use the exact namespace URI from the vocabulary list endpoint

### Empty code list

**Symptom:** Vocabulary exists but codes endpoint returns empty
**Cause:** No codes defined for the vocabulary
**Solution:** Configure codes for the vocabulary in OpenSPP

### Namespace URI encoding issues

**Symptom:** 400 error with namespace URI in path
**Cause:** Special characters in URI not properly encoded
**Solution:** URL-encode the namespace URI (colons, slashes)

### Inactive codes not returned

**Symptom:** Known codes missing from results
**Cause:** Codes marked as inactive are filtered out by default
**Solution:** Include parameter to retrieve inactive codes if needed
