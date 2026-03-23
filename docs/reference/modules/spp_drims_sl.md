---
openspp:
  doc_status: draft
---

# Sri Lanka Configuration

**Module:** `spp_drims_sl`

## Overview

Sri Lanka-specific configuration for DRIMS disaster response inventory management. Includes geographic hierarchy, government agencies, and approval thresholds per DMC requirements.

## Purpose

This module is designed to:

- **Configure Sri Lanka geography:** Define area types for the Sri Lankan administrative hierarchy (Province, District, DS Division, GN Division) and provide the official admin boundary Excel data file.
- **Set up government agencies:** Pre-configure DMC, NDRRMC, and humanitarian organizations (UNICEF, WFP, Red Cross, CARE, Oxfam) as system partners.
- **Establish warehouse network:** Create DRIMS warehouses for each province and a central national warehouse.
- **Configure approval workflows:** Set up multi-tier approval definitions with DMC-specific thresholds and demo users for each approval tier.
- **Provide product catalog:** Define standard relief product categories and products used in Sri Lanka disaster response.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `spp_drims` | Disaster relief inventory management for donations, reque... |
| `spp_approval` | Standardized approval workflows with multi-tier sequencin... |
| `product_expiry` | Product expiry date tracking |

## Key Features

### Area Types

Defines Sri Lanka-specific area types mapped to administrative levels:

| Level | Area Type |
| --- | --- |
| 0 | Province |
| 1 | District |
| 2 | DS Division |
| 3 | GN Division |

### Master Data

The module installs via XML data files:

- **Company configuration:** Sets the main company to Sri Lanka locale
- **Hazard categories:** Flood, geological (landslide), drought, and other categories relevant to Sri Lanka
- **Vocabulary codes:** Sri Lanka-specific vocabulary entries for DRIMS operations
- **Agencies:** Pre-configured humanitarian organizations as system partners
- **Warehouses:** Central warehouse in Colombo, national reserve in Anuradhapura, and provincial warehouses across all nine provinces
- **Product catalog:** Standard relief items with categories (food, non-food, medical, shelter)
- **Demo users:** Users for each DRIMS role (admin, warehouse manager, approver, officer, viewer)
- **Approval configuration:** Multi-tier approval workflow with national and provincial approval tiers

## Integration

- **spp_drims:** Provides the base DRIMS framework that this module configures with Sri Lanka-specific data.
- **spp_approval:** Configures multi-tier approval definitions with DMC-specific thresholds and tier assignments.
- **product_expiry:** Enables lot-level expiry tracking for perishable relief items.
