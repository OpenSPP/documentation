---
myst:
  html_meta:
    "description": "This website is the HTML documentation of OpenSPP, an open source social protection platform."
    "property=og:description": "This website is the HTML documentation of OpenSPP, an open source social protection platform."
    "property=og:title": "OpenSPP Documentation"
    "keywords": "OpenSPP, open source, Documentation"
openspp:
  doc_status: unverified
  products: [core]
---

(index-label)=

# Welcome to OpenSPP!

OpenSPP was created to support the improvement and growth of effective social protection and humanitarian programs using open-source technologies. Our goal is to make it easier and more cost effective for governments and humanitarian agencies to digitalize their social protection systems.

OpenSPP is an open-source, modular and highly interoperable platform. The platform offers four main products: SP-MIS - a comprehensive management information system - plus a Social Registry, a Farmer Registry and a Disability Registry.

OpenSPP is a Digital Public Good. It is built on more than 60 open-source modules, and leverages and contributes to other open-source projects including OpenG2P, MOSIP, OpenCRVS, Odoo, Payment Hub EE, ID PASS, CommCare, Metabase and OpenFn

## Get Started

New to OpenSPP? Start here:

- **{doc}`learn/index`** - Understand OpenSPP concepts and architecture
- **{doc}`get_started/index`** - Install and set up your first program
- **{doc}`learn/whats_new_v2`** - What's new in OpenSPP V2

## Documentation by Role

| I am a... | I need to... | Start here |
|-----------|--------------|------------|
| **User** | Register beneficiaries, run programs | {doc}`user_guide/index` |
| **Implementer** | Configure eligibility, scoring, workflows | {doc}`config_guide/index` |
| **Developer** | Extend OpenSPP, build integrations | {doc}`developer_guide/index` |
| **Sys Admin** | Deploy, secure, maintain OpenSPP | {doc}`ops_guide/index` |

## Platform Overview

### SP-MIS

OpenSPP's social protection management information system offers customizable building blocks for effective program implementation. Its modular design allows users to select only the components they need without an overhaul of existing systems.

![](images/openspp_bb.png)

### Social Registry

The Social Registry is a repository for the storage and management of data for planning and administering social protection. It supports intake, dynamic registration and needs assessment, and the efficient and secure sharing of data from the social registry with various social protection programs and services.

### Farmer Registry

The Farmer Registry stores and manages farm holding and farm owner data, supporting coordination between the social and agricultural sectors. It supports mass registrations and regular updates, and integrates data from Geographic Information Systems, national ID and CRVS.

### Disability Registry

The Disability Registry is an organized database for systematically recording and managing information about individuals with disabilities within a specific population or geographic area. It contains important information to facilitate services and assistance for people with disabilities, including access to social protection programs.

## Guiding Principles

Our guiding principles are informed by the Digital Public Goods Standard and the Principles for Digital Development.

- **User-centricity**: Our products are designed to be intuitive and pragmatic, recognizing that social protection operates in complex, resource-constrained and rapidly changing contexts.
- **Modularity**: The platform is composed of independent modules which allow for flexibility, scalability, and the interchangeability of components.
- **Privacy and security**: We rigorously uphold privacy and security standards - essential prerequisites for safeguarding Digital Public Goods.
- **Interoperability**: The platform is designed to support system interoperability - critical for the creation of cohesive and efficient digital ecosystems.
- **Inclusivity**: Our products can be customized to suit linguistic and cultural requirements, accessibility, digital literacy, and deployment in remote and less-developed contexts.

## Get Help

OpenSPP is currently in active development. If you have questions or need support:

- {doc}`community_and_support/index` - Community resources and support channels
- [GitHub Issues](https://github.com/OpenSPP/openspp-modules) - Report bugs or request features
- [OpenSPP Website](https://openspp.org/) - Contact the team

```{toctree}
:maxdepth: 2
:hidden:
:caption: Learn

learn/concepts/index
learn/products/social_registry
learn/products/sp_mis
learn/products/farmer_registry
learn/products/drims
learn/whats_new_v2
```

```{toctree}
:maxdepth: 2
:hidden:
:caption: Get Started

get_started/installation/index
get_started/explore/index
get_started/first_household/index
get_started/first_program/index
get_started/poc_and_pilot
```

```{toctree}
:maxdepth: 2
:hidden:
:caption: User Guide

user_guide/getting_started/index
user_guide/registry/index
user_guide/change_requests/index
user_guide/programs/index
user_guide/payments/index
user_guide/approvals/index
user_guide/drims/index
user_guide/reference/index
```

```{toctree}
:maxdepth: 2
:hidden:
:caption: Configuration Guide

config_guide/studio/index
config_guide/cel/index
config_guide/eligibility/index
config_guide/entitlement_formulas/index
config_guide/scoring/index
config_guide/vocabulary/index
config_guide/variables/index
config_guide/event_data/index
config_guide/change_request_types/index
config_guide/consent/index
config_guide/drims/index
```

```{toctree}
:maxdepth: 2
:hidden:
:caption: Developer Guide

developer_guide/setup/index
developer_guide/architecture/index
developer_guide/extending/index
developer_guide/api_v2/index
developer_guide/dci/index
developer_guide/verifiable_credentials/index
developer_guide/integrations/index
developer_guide/drims/index
developer_guide/migration/index
```

```{toctree}
:maxdepth: 2
:hidden:
:caption: Operations Guide

ops_guide/deployment/index
ops_guide/security/index
ops_guide/storage/index
ops_guide/backup/index
ops_guide/monitoring/index
```

```{toctree}
:maxdepth: 2
:hidden:
:caption: Reference

reference/modules/index
reference/vocabularies/index
reference/api/index
reference/glossary/humanitarian
modules/index
```

```{toctree}
:maxdepth: 2
:hidden:
:caption: Community

community_and_support/index
contributing/index
```

```{toctree}
:maxdepth: 1
:hidden:
:caption: Appendices

glossary
```
