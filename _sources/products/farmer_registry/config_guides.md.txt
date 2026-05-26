---
openspp:
  doc_status: draft
---

# Relevant configuration guides

This page lists the configuration guides relevant to OpenSPP Farmer Registry. These guides are written for implementers and technical staff who configure the system to meet agricultural program requirements.

## Identity and access

- {doc}`Create and assign user roles </config_guide/role_configuration/index>` — Define roles, assign permissions, and control area-based access
- {doc}`Configure consent management </config_guide/consent/index>` — Set up privacy notices, consent flows, and API consent filtering

## Registry and farmer data

- {doc}`Add custom fields </config_guide/custom_fields/index>` — Extend registrant records with programme-specific fields
- {doc}`Configure farmer registry fields </config_guide/farmer_registry/index>` — Set up farm details, land records, and agricultural activity types
- {doc}`Manage vocabularies </config_guide/vocabulary/index>` — Define and maintain standardized code lists including crop and livestock vocabularies
- {doc}`Set up administrative areas </config_guide/area_management/index>` — Import and configure geographic area hierarchies
- {doc}`Configure import matching </config_guide/import_matching/index>` — Set deduplication rules for bulk data imports
- {doc}`Define event types </config_guide/event_data/index>` — Configure event data capture for farm and registrant activities

## GIS configuration

- {doc}`Configure GIS data layers </config_guide/gis/index>` — Set up geographic data layers and map report templates

## Eligibility and targeting

- {doc}`Define eligibility rules </config_guide/eligibility/index>` — Build criteria to identify eligible farmers and households
- {doc}`Write CEL expressions </config_guide/cel/index>` — Use CEL syntax for flexible eligibility and formula logic
- {doc}`Create reusable variables </config_guide/variables/index>` — Define shared variables for use across eligibility rules
- {doc}`Configure vulnerability and PMT scoring </config_guide/scoring/index>` — Set up proxy means testing and scoring frameworks

## Programs and entitlements

- {doc}`Configure entitlement calculation formulas </config_guide/entitlement_formulas/index>` — Define how benefit amounts are calculated per household
- {doc}`Set up approval workflows </config_guide/approval_workflows/index>` — Configure multi-tier approval sequences for program actions
- {doc}`Simulate program scenarios </config_guide/simulation/index>` — Model coverage and cost before running a cycle
- {doc}`Configure graduation criteria </config_guide/graduation/index>` — Define conditions for exiting a program

## Change management

- {doc}`Configure change request types </config_guide/change_request_types/index>` — Define custom change request workflows with field mappings and approval chains
- {doc}`Use OpenSPP Studio </config_guide/studio/index>` — No-code interface for building change request forms and registry fields

## Monitoring and accountability

- {doc}`Configure audit logging </config_guide/audit/index>` — Enable and customize audit trail settings
- {doc}`Set up the grievance redress mechanism </config_guide/grievance_redress/index>` — Configure teams, SLA rules, and complaint categories
