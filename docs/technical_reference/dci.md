---
myst:
  html_meta:
    "description": "Digital Convergence Initiative (DCI) integration in OpenSPP"
    "property=og:title": "DCI Integration"
    "keywords": "OpenSPP, DCI, interoperability, Odoo 19"
openspp:
  doc_status: unverified
---

# DCI Integration

OpenSPP includes a DCI (Digital Convergence Initiative) integration layer intended to support interoperability with
social protection and registry ecosystems.

## What is implemented in code

In the OpenSPP codebase (Odoo 19 series), DCI concepts are implemented across multiple Odoo modules, including:

- `spp_dci` (schemas, core models, and services used by DCI features)
- Additional DCI server/client modules (for example `spp_dci_server*`, `spp_dci_client*`) depending on the deployment

## How to approach documentation for DCI

The DCI surface area spans:

- Data models and identifiers used for exchange
- API endpoints (where enabled) and authentication
- Mapping between OpenSPP registry models and DCI payloads

As the documentation is rewritten, this page will be expanded into a full technical reference based on the DCI ADRs
and the current implementation.
