---
myst:
  html_meta:
    "description": "OpenSPP APIs technical reference"
    "property=og:title": "OpenSPP APIs"
    "keywords": "OpenSPP, API, REST, OAuth2, XML-RPC, Odoo 19"
openspp:
  doc_status: unverified
  products: [core]
---

# APIs

OpenSPP exposes an **official REST API (API v2)**, and also supports **XML-RPC** for advanced/legacy integrations.

## API v2 (REST)

API v2 is implemented by the Odoo module `spp_api_v2`.

Start here:

- {doc}`API v2 reference <api_v2/index>`

## XML-RPC (advanced / legacy)

If you need direct access to Odoo models over XML-RPC (for example, for administrative scripting), see:

- {doc}`External API (XML-RPC) <external_api>`
