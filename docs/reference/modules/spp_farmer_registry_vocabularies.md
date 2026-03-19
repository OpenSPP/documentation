---
openspp:
  doc_status: draft
---

# Vocabularies

**Module:** `spp_farmer_registry_vocabularies`

## Overview

FAO-aligned vocabularies for farmer registry (crops, livestock, aquaculture)

## Purpose

This module is designed to:

- **Provide FAO-aligned vocabularies:** Install pre-configured vocabulary codes for farm type, land tenure, land use, cultivation method, activity purpose, holder type, data source, and irrigation asset types.
- **Supply species vocabularies:** Provide default crop, livestock, and aquaculture species codes aligned with FAO classification systems (ICC, FAO Livestock, ASFIS).
- **Import AGROVOC data:** Enable bulk import of AGROVOC RDF vocabulary data with filtering, hierarchy preservation, and multilingual label extraction.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `spp_vocabulary` | OpenSPP: Vocabulary |
| `job_worker` | Background job worker |

## Key Features

### Pre-installed Vocabularies

The module installs vocabulary codes via XML data files:

| Vocabulary | Namespace URI | Description |
| --- | --- | --- |
| Farm Type | `urn:openspp:vocab:farm-type` | Crop, livestock, aquaculture, mixed |
| Land Tenure | `urn:openspp:vocab:land-tenure` | Ownership and use rights |
| Land Use | `urn:openspp:vocab:land-use` | Land use classification |
| Cultivation Method | `urn:openspp:vocab:cultivation-method` | Irrigated, rainfed |
| Activity Purpose | `urn:openspp:vocab:activity-purpose` | Subsistence, commercial, both |
| Holder Type | `urn:openspp:vocab:holder-type` | Individual, joint, institutional (FAO WCA 2020) |
| Data Source | `urn:openspp:vocab:data-source` | Census, self-registration, field visit |
| Irrigation Asset Type | `urn:openspp:vocab:irrigation-asset-type` | Types of irrigation infrastructure |

### Species Vocabularies

Default species codes for the three activity types:

| Vocabulary | Namespace URI | Source Standard |
| --- | --- | --- |
| Crops | `urn:fao:icc:1.1` | FAO Indicative Crop Classification |
| Livestock | `urn:fao:livestock:2020` | FAO Livestock Classification |
| Aquaculture | `urn:fao:asfis:2024` | FAO ASFIS Species List |

### AGROVOC Import

The AGROVOC import system (`spp.agrovoc.import`) supports batch import from RDF N-Triples files:

- **Filtering modes:** Import all concepts, filter by root concept hierarchy (e.g., only cereals), or import a specific list of concept codes
- **Hierarchy support:** Extracts parent-child relationships from SKOS broader/narrower relations with configurable maximum depth
- **Multilingual labels:** Extracts labels in a primary language plus configurable additional languages
- **Background processing:** Uses `job_worker` for scalable processing of large datasets
- **Preview mode:** Preview what would be imported before executing

A wizard (`spp.agrovoc.import.wizard`) provides a user-friendly interface for uploading files, selecting the target vocabulary type, and previewing results before import.

## Integration

- **spp_vocabulary:** All vocabulary codes are stored in `spp.vocabulary.code` records and referenced by `spp_farmer_registry` for farm classification and species selection.
- **job_worker:** AGROVOC import processing runs as background jobs for handling large RDF datasets without blocking the UI.
