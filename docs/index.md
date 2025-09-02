---
myst:
  html_meta:
    "description": "This website is the HTML documentation of OpenSPP, an open source social protection platform."
    "property=og:description": "This website is the HTML documentation of OpenSPP, an open source social protection platform."
    "property=og:title": "OpenSPP Documentation"
    "keywords": "OpenSPP, open source, Documentation"
---

(index-label)=

# Welcome to OpenSPP!

OpenSPP empowers governments and humanitarian organizations to deliver effective social protection and agricultural support programs through open-source digital infrastructure. By bridging social welfare with agricultural development, OpenSPP enables coordinated assistance to vulnerable populations, from urban cash transfers to rural farming subsidies.

The platform's modular architecture offers three integrated products: **SP-MIS** for comprehensive program management, **Social Registry** for beneficiary data coordination, and **Farmer Registry** for agricultural-social protection convergence. Organizations can deploy specific modules that match their needs while maintaining interoperability with existing systems.


## Key Features

- **🎯 [Program Management](overview/features/program_management.md)** - Design and operate multiple social protection programs with configurable cycles and eligibility rules
- **📊 [Unified Registry](overview/features/unified_registry.md)** - Maintain consolidated beneficiary data across programs with advanced deduplication
- **🌾 [GIS & Land Management](overview/features/gis_land_management.md)** - Integrate agricultural data, land holdings, and geospatial analysis for farmer support programs
- **💳 [Payment & Disbursement](overview/features/payment_disbursement.md)** - Connect with multiple payment providers and track benefit distribution
- **🎯 [Eligibility & Targeting](overview/features/eligibility_targeting.md)** - Apply sophisticated criteria for beneficiary selection and prioritization
- **📦 [In-Kind Benefits](overview/features/in_kind_benefits.md)** - Manage distribution of goods, vouchers, and non-cash assistance
- **💬 [Grievance Redress](overview/features/grievance_redress.md)** - Handle complaints and feedback with configurable workflows
- **🔌 [APIs & Integration](overview/features/data_integration_apis.md)** - RESTful APIs and data exchange protocols for system interoperability

## Who Uses OpenSPP

OpenSPP serves diverse organizations implementing social protection and agricultural support programs:

- **Government Ministries** - Social welfare, agriculture, and disaster management agencies
- **Humanitarian Organizations** - UN agencies and NGOs delivering emergency assistance
- **Agricultural Development Programs** - Supporting smallholder farmers with subsidies and climate adaptation
- **Cash Transfer Programs** - Conditional and unconditional cash assistance initiatives
- **Food Security Programs** - Coordinating nutrition support with agricultural production

## Quick Start

:::::{grid} 2
:gutter: 2

::::{grid-item-card} 🚀 Get Started
:link: getting_started/index.md
:link-type: doc

New to OpenSPP? Start with our installation guide and quickstart tutorial.
::::

::::{grid-item-card} 📚 User Guide  
:link: user_guide/index.md
:link-type: doc

Learn how to use OpenSPP for registry and program management.
::::

::::{grid-item-card} 🔧 Developer Guide
:link: developer_guide/index.md
:link-type: doc

Customize and extend OpenSPP with our technical documentation.
::::

::::{grid-item-card} 🏗️ Architecture
:link: developer_guide/architecture.md
:link-type: doc

Understand OpenSPP's technical architecture and design principles.
::::
:::::

## Products

Explore our complete product documentation to understand how each component addresses specific use cases.

![](images/openspp_bb.png)

### SP-MIS

OpenSPP's social protection management information system offers customizable building blocks for effective program implementation. Its modular design allows users to select only the components they need without an overhaul of existing systems. 

[Learn more →](overview/products/sp_mis.md)



### Social Registry

The Social Registry is a repository for the storage and management of data for planning and administering social protection. It supports intake, dynamic registration and needs assessment, and the efficient and secure sharing of data from the social registry with various social protection programs and services.

[Explore features →](overview/products/social_registry.md)

### Farmer Registry

The Farmer Registry bridges social protection with agricultural development, storing and managing comprehensive farm and farmer data. Key capabilities include:
- **Farm holding mapping** with GIS integration for land parcels and crop data
- **Agricultural subsidy management** for input distribution and support programs  
- **Climate resilience programs** targeting vulnerable farming communities
- **Integration with agricultural extension services** and market information systems
- **Seasonal support cycles** aligned with planting and harvest periods

This enables coordinated delivery of both social protection and agricultural support to rural communities. 

[View documentation →](overview/products/farmer_registry.md)

## Guiding principles

Our guiding principles are informed by the Digital Public Goods Standard and the Principles for Digital Development.

- **User-centricity**: Our products are designed to be intuitive and pragmatic, recognizing that social protection operates in complex, resource-constrained and rapidly changing contexts.
- **Modularity**: The platform is composed of independent modules which allow for flexibility, scalability, and the interchangeability of components.
- **Privacy and security**: We rigorously uphold privacy and security standards - essential prerequisites for safeguarding Digital Public Goods.
- **Interoperability**: The platform is designed to support system interoperability - critical for the creation of cohesive and efficient digital ecosystems.
- **Inclusivity**: Our products can be customized to suit linguistic and cultural requirements, accessibility, digital literacy, and deployment in remote and less-developed contexts.

## Common Tasks

- **[Install OpenSPP](getting_started/installation_deb.md)** - Set up your development or production environment
- **[Create a Program](user_guide/program_management/create_program.md)** - Design and launch social protection programs  
- **[Manage Registrants](user_guide/registry_management/index.md)** - Add and manage beneficiary data
- **[Configure Integrations](developer_guide/integrations/index.md)** - Connect with external systems

## Digital Public Good & Open Source Foundation

OpenSPP is recognized as a [Digital Public Good](https://digitalpublicgoods.net/), meeting the highest standards for open-source software that addresses the Sustainable Development Goals. Built on a foundation of **60+ modular components**, OpenSPP integrates with and contributes to a robust ecosystem of digital public infrastructure:

- **[OpenCRVS](https://www.opencrvs.org/)** for civil registration and vital statistics
- **[MOSIP](https://mosip.io/)** for digital ID integration  
- **[OpenFn](https://www.openfn.org/)** for workflow automation and integration
- **[DHIS2](https://dhis2.org/)** for health information management  
- **[Payment Hub EE](https://mifos.org/payment-hub/)** for financial services integration
- **[OpenG2P](https://openg2p.org/)** for government-to-person delivery systems
- **[Odoo](https://www.odoo.com/)** as the enterprise platform foundation





## Resources & Community

:::::{grid} 3
:gutter: 2

::::{grid-item}
**Get Help**
- 📖 [Documentation](https:/docs.openspp.org/)
- 💬 [GitHub Discussions](https://github.com/OpenSPP/OpenSPP/discussions)
- 🐛 [Report Issues](https://github.com/OpenSPP/openspp-modules/issues)
::::

::::{grid-item}
**Stay Connected**
- 🌐 [OpenSPP Website](https://openspp.org/)
- 📰 [Release Notes](https://github.com/OpenSPP/openspp-modules/releases)
- 🤝 [Contributing Guide](community/contributing.md)
::::

::::{grid-item}
**Learn More**
- 🔍 [API Reference](developer_guide/api_usage/index.md)
- 📋 [Glossary](reference/glossary.md)
::::
:::::

OpenSPP is currently in development, and everything is evolving rapidly thanks to the input provided by our users. If you have any questions or needs, please do not hesitate to contact the team.

```{toctree}
:maxdepth: 3
:hidden: true

getting_started/index
overview/index
user_guide/index
developer_guide/index
reference/index
community/index
```

```{toctree}
:caption: Appendices
:maxdepth: 1
:hidden: true

reference/glossary
```
