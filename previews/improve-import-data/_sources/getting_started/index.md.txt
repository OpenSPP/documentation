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

:::::{grid} 2
:gutter: 3

::::{grid-item-card} New installation
Start here if you're setting up OpenSPP for the first time:

1. **{doc}`Installation guide <installation_deb>`**  
   Install OpenSPP on Debian/Ubuntu (30 minutes)

2. **{doc}`Module installation <module_installation>`**  
   Choose {doc}`SP-MIS <../overview/products/sp_mis>`, {doc}`Social Registry <../overview/products/social_registry>`, or {doc}`Farmer Registry <../overview/products/farmer_registry>`

3. **Initial setup**  
   Configure your first program and import data
::::

::::{grid-item-card} Learn the system
Explore OpenSPP's capabilities:

- **{doc}`Features <../overview/features/index>`** - Understand key features
- **{doc}`Products <../overview/products/index>`** - Choose the right product configuration  
- **{doc}`User guide <../user_guide/index>`** - Learn day-to-day operations
::::
:::::

## Choose your configuration

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

## Steps

### 1. System installation
**Time required:** 30-45 minutes

Install OpenSPP using our Debian packages:
- {doc}`Installation Guide <installation_deb>` - Production deployment on Ubuntu/Debian

### 2. Module configuration  
**Time required:** 15-30 minutes

After installation, configure your system:
- {doc}`Module Installation <module_installation>` - Install base modules and extensions

### 3. Initial setup
**Time required:** 1-2 hours

Get your system ready for use:
- Create your first program - {doc}`Creating a Program <../user_guide/program_management/create_program>`
- Import beneficiary data - {doc}`Registry Management <../user_guide/registry_management/index>`
- Configure user access - {doc}`Administration <../user_guide/administration/index>`

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

```{toctree}
---
caption: Getting Started
maxdepth: 2
hidden: true
---

installation_deb
module_installation
```