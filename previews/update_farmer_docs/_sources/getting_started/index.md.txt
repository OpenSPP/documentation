---
myst:
  html_meta:
    "title": "Getting Started with OpenSPP"
    "description": "Quick start guide for installing and configuring OpenSPP social protection platform"
    "keywords": "OpenSPP, installation, setup, SP-MIS, Social Registry, Farmer Registry"
---

# Getting started

Welcome to OpenSPP! This guide will help you get your social protection platform up and running quickly.

## Quick start path
Start here if you're setting up OpenSPP for the first time:

:::::{grid} 2
:gutter: 3

::::{grid-item-card} I want to use the OpenSPP products

1. {doc}`Install OpenSPP on Debian/Ubuntu (30 minutes) <installation_deb>`

<br>

2. Install {doc}`SP-MIS <spmis_installation>`, {doc}`Social Registry <social_installation>`, or {doc}`Farmer Registry <farmer_installation>` from the available modules.

<br>

3. Get your system ready for use:
    - Create your first program - {doc}`Creating a Program <../user_guide/program_management/create_program>`
    - Import beneficiary data - {doc}`Registry Management <../user_guide/registry_management/index>`
    - Configure user access - {doc}`Administration <../user_guide/administration/index>` 
   
::::

::::{grid-item-card} I want to select my modules freely

1. {doc}`Install OpenSPP on Debian/Ubuntu (30 minutes) <installation_deb>`

<br>

2. Choose modules to install. Read more about {doc}`module installation <module_installation>` and {doc}`available modules <../reference/modules/index>`

<br>

3. Get your system ready for use:
    - Create your first program - {doc}`Creating a Program <../user_guide/program_management/create_program>`
    - Import beneficiary data - {doc}`Registry Management <../user_guide/registry_management/index>`
    - Configure user access - {doc}`Administration <../user_guide/administration/index>`
::::
:::::

## OpenSPP configurations

OpenSPP offers three primary configurations based on your needs:

```{list-table}
:header-rows: 1
:widths: 20 30 50

* - Configuration
  - Best For
  - Key Features
* - **{doc}`SP-MIS <../overview/products/sp_mis>`**
  - Social protection programs, cash transfers, humanitarian aid
  - • Registry management<br>• Program cycles<br>• Eligibility targeting<br>• Payment processing
* - **{doc}`Social Registry <../overview/products/social_registry>`**
  - Centralized beneficiary database, inter-program coordination
  - • Unified beneficiary data<br>• Deduplication<br>• Data sharing across programs<br>• Needs assessment
* - **{doc}`Farmer Registry <../overview/products/farmer_registry>`**
  - Agricultural support, farmer subsidies, rural development
  - • Farm mapping<br>• Crop tracking<br>• Input distribution<br>• Seasonal cycles
```

## Where to go next

Based on your role:

:::::{grid} 3
:gutter: 3

::::{grid-item-card} Program Managers & Administrators

- **{doc}`User Guide <../user_guide/index>`**<br>
  Day-to-day operations guide

- **{doc}`Concepts <../overview/concepts/index>`**<br>
  Understand core concepts
::::

::::{grid-item-card} Developers & System Integrators

- **{doc}`Development Setup <../developer_guide/setup>`** <br>
  Development environment setup
- **{doc}`API Usage <../developer_guide/api_usage/index>`**<br>
  API integration guide  
- **{doc}`Customization <../developer_guide/module_development/index>`**<br>
  Customization guides
::::

::::{grid-item-card} Decision Makers

- **{doc}`Overview <../overview/index>`**<br>
  Product overview and capabilities
- **{doc}`Case Studies <../overview/case_studies/index>`** <br>
  Implementation examples
::::
:::::

## Need help?

- **[GitHub Discussions](https://github.com/orgs/OpenSPP/discussions)** - Ask questions and get help from the community
- **[Report Issues](https://github.com/OpenSPP/openspp-modules/issues)** - Report bugs or request features
- **{doc}`OpenSPP Glossary <../reference/glossary>`** - Look up terms (available in multiple languages)
- **[OpenSPP Discord server](https://discord.gg/bgrwxhEQty)** - Join the OpenSPP Discord server and meet the rest of the community

```{toctree}
---
caption: Getting Started
maxdepth: 2
hidden: true
---

installation_deb
module_installation
```