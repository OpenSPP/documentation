---
openspp:
  doc_status: draft
---

# Registry Search

**Module:** `spp_cel_registry_search`

## Overview

Search the registry using CEL expressions

## Purpose

This module is designed to:

- **Search the registry using CEL expressions:** Provide an advanced search interface that lets users write CEL expressions to find individuals and groups in the registry.
- **Control access to advanced search:** Restrict the search portal to authorized users through a dedicated security group.
- **Display search results with pagination:** Show matching registrants in a paginated list with navigation to registrant profiles.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `spp_registry` | Consolidated registry management for individuals, groups,... |
| `spp_cel_domain` | Write simple CEL-like expressions to filter records (Open... |
| `spp_cel_widget` | Reusable CEL expression editor with syntax highlighting a... |

## Key Features

### Advanced Search Portal

An OWL client action that provides a full-page search interface accessible from the Registry menu. Users can:

- Write CEL expressions using the shared CEL editor with syntax highlighting
- Select a search profile (Individuals or Groups)
- View real-time validation of the expression before executing
- Browse paginated results (50 records per page)
- Click on any result to open the registrant form

### Security Groups

| Group | Description |
| --- | --- |
| `group_cel_search_user` | Grants access to the Advanced Search menu; implies `group_registry_viewer` |

Registry Officers automatically receive CEL Search access through group implication.

### Menu Entry

The module adds an "Advanced Search" menu item under the Registry root menu, visible only to users with the `group_cel_search_user` security group.

## Integration

- **spp_registry:** The search portal is accessible from the Registry menu and opens registrant forms using registry view references.
- **spp_cel_domain:** Uses `spp.cel.service.compile_expression()` to translate CEL expressions into Odoo domains and retrieve matching records.
- **spp_cel_widget:** Embeds the shared `CelEditor` component for expression editing with syntax highlighting and validation.
