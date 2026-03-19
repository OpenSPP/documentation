---
myst:
  html_meta:
    "title": "DRIMS - Disaster Response Inventory Management"
    "description": "OpenSPP SP-MIS product configuration for comprehensive social protection program management from enrollment to payment"
    "keywords": "OpenSPP, SP-MIS, social protection, management information system, beneficiary management, payments"
---
# OpenSPP DRIMS
*A digital system to manage the full lifecycle of social protection programs*

The **OpenSPP Disaster Response Inventory Management (DRIMS)** manages the complete lifecycle of emergency supplies, supporting donation tracking, request approvals, dispatch management, real-time inventory visibility, stock monitoring, and inter-agency coordination during disaster response.

## Key features

**Donation and supply management** – Track pledged and received supplies from UN agencies, NGOs, governments, and private donors. Manage inspection, lot tracking, and expiry monitoring to ensure safe and accountable stock handling.

**Multi-tier request and dispatch workflows** – Support structured approval workflows for relief requests from field teams. Manage picking, packing, waybill generation, and proof of delivery to ensure supplies reach affected populations efficiently.

**Real-time inventory visibility** – Monitor stock levels across central, regional, and mobile warehouses. Use dashboards and automated alerts to detect low stock levels, expiring items, and fulfillment delays.

**Cluster-based humanitarian coordination** – Tag requests, supplies, and personnel by OCHA/IASC humanitarian clusters (e.g., Food Security, Health, WASH, Shelter). Enable sector-specific reporting, gap analysis, and 4W (Who does What, Where, When) reporting for coordination meetings.

**Monitoring, audit, and accountability** – Maintain full audit trails of all operations. Track service-level agreements (SLAs), generate incident-based reporting, and ensure transparency across all disaster response workflows.

**Personnel and role management** – Manage deployed disaster response staff by role, cluster assignment, organization, and location. Enforce role-based access control to protect sensitive data and operational integrity.

## Who is it for?

**Government agencies** coordinating national emergency operations

**Humanitarian organizations** managing relief coordination

**NGOs and implementing partners** delivering emergency supplies

**Warehouse and logistics teams** managing disaster inventory

## Next step

The OpenSPP DRIMS is an open-source product, built and supported by the OpenSPP community. Read more about installing OpenSPP DRIMS.

## OpenSPP modules included in the OpenSPP DRIMS

The preconfigured OpenSPP DRIMS product is intended to provide the basic use cases of disaster response inventory and coordination management.

The following modules are included in the OpenSPP DRIMS product:

- **{doc}`OpenSPP Alerts <../../reference/modules/spp_alerts>`**: Manages and dispatches emergency alerts and notifications.
- **{doc}`OpenSPP Hazard <../../reference/modules/spp_hazard>`**: Records and tracks hazard events and affected areas.
- **{doc}`OpenSPP GIS <../../reference/modules/spp_gis>`**: Geospatial mapping and geographic analysis for response operations.
- **{doc}`OpenSPP GIS Reports <../../reference/modules/spp_gis_report>`**: GIS-based spatial reports for disaster response analysis.
- **{doc}`OpenSPP Security <../../reference/modules/spp_security>`**: Central security definitions for OpenSPP modules.
- **{doc}`OpenSPP Vocabulary <../../reference/modules/spp_vocabulary>`**: Standardized code list management system for OpenSPP.
- **{doc}`OpenSPP Area Management <../../reference/modules/spp_area>`**: Establishes direct associations between OpenSPP registrants, beneficiary groups, and their corresponding geographical administrative areas.
- **{doc}`OpenSPP User Roles <../../reference/modules/spp_user_roles>`**: Defines and manages distinct user roles for area-based access control.
- **{doc}`OpenSPP Service Points Management <../../reference/modules/spp_service_points>`**: Manages physical or virtual locations for social protection service delivery.
- **{doc}`OpenSPP Approval <../../reference/modules/spp_approval>`**: Standardized approval workflows with multi-tier sequencing and CEL rules.
- **{doc}`OpenSPP CEL Domain Query Builder <../../reference/modules/spp_cel_domain>`**: Write simple CEL-like expressions to filter records.
- **{doc}`OpenSPP Audit <../../reference/modules/spp_audit>`**: Audit logging of user actions and data changes.

## Expanding DRIMS

The OpenSPP-based DRIMS contains everything necessary to set up a foundational disaster response inventory and coordination system. It can, however, be expanded with additional functionalities to perfectly suit specific operational needs. Read more about module installation.
