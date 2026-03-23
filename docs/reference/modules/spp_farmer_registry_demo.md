---
openspp:
  doc_status: draft
---

# Demo

**Module:** `spp_farmer_registry_demo`

## Overview

Demo generator for Farmer Registry with fixed stories and volume generation

## Purpose

This module is designed to:

- **Generate fixed story farms:** Create eight detailed farmer personas with complete farm data (activities, land parcels, assets) for demonstration and testing.
- **Generate volume data:** Create additional randomized farms using a seeded generator for realistic dashboard populations.
- **Create demo programs:** Set up sample programs with cycles, enrollments, entitlements, and payments using proper Odoo workflow methods.
- **Demonstrate change requests:** Generate sample change requests for farm detail updates to showcase the approval workflow.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `spp_starter_farmer_registry` | Complete Farmer Registry bundle with API, DCI, and Progra... |
| `spp_demo` | Core demo module with data generator and sample data for ... |
| `spp_farmer_registry_cr` | Farmer-specific change request types for farm details and... |
| `spp_studio` | No-code customization interface for OpenSPP |
| `spp_registry_group_hierarchy` | The module introduces hierarchical relationships among Op... |
| `spp_area` | Establishes direct associations between OpenSPP registran... |
| `spp_programs` | Manage cash and in-kind entitlements, integrate with inve... |

## Key Features

### Demo Generator Wizard

A wizard-based generator creates demo data in a controlled sequence:

1. **Areas:** Creates Philippine administrative areas (provinces) with GPS coordinates
2. **Story farms:** Eight fixed farmer personas from blueprints with complete data
3. **Volume farms:** Additional randomized farms using `SeededFarmGenerator` for reproducible output
4. **Programs:** Demo programs created via `demo_programs` module with proper Odoo flows
5. **Enrollments and payments:** Full program lifecycle via state machine transitions

### Farmer Blueprints

Fixed story farms provide realistic, complete test data covering various scenarios:

- Different farm types (crop, livestock, mixed)
- Various land tenure situations
- Multiple activity types with species from FAO vocabularies
- Land parcels with GIS coordinates
- Farm assets and machinery

### Seeded Farm Generator

The `SeededFarmGenerator` class uses deterministic random generation (seeded) to produce reproducible farm data. This ensures consistent demo environments across installations while providing realistic variation in farm sizes, activity types, and geographic distribution.

### Demo Programs

Creates sample social protection programs with:

- Program configuration via XML data
- Cycle creation and enrollment
- Entitlement generation and payment processing
- Logic pack integration for eligibility rules

## Integration

- **spp_starter_farmer_registry:** Uses the complete farmer registry bundle as the foundation.
- **spp_demo:** Extends the core demo infrastructure for data generation.
- **spp_farmer_registry_cr:** Creates sample change requests to demonstrate the approval workflow.
- **spp_programs:** Creates demo programs with full lifecycle (cycles, entitlements, payments).
- **spp_area:** Creates geographic areas for farm location assignment.
- **spp_registry_group_hierarchy:** Supports hierarchical group relationships in demo data.
