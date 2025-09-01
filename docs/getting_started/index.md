---
review-status: needs-review
review-date: 2025-06-04
reviewer: migration-script
migration-notes: "Added during 2025 documentation reorganization"
---

# Getting Started

## How the documentation is organized

This overview of how OpenSPP's documentation is organized will help you know where to look for certain things:


- {doc}`installation_deb` offers a detailed, step-by-step guide for installing OpenSPP using Debian-based packages. It covers system requirements, installation procedures, initial configuration, and troubleshooting tips to ensure a smooth setup process.
- {doc}`module_installation` offers a comprehensive, step-by-step guide for configuring OpenSPP after the initial installation. It explains how to install additional modules, customize features, and optimize your setup for specific needs.
- {doc}`../overview/index` provides high-level information about OpenSPP's features, concepts, and use cases for decision makers and new users.
- {doc}`../user_guide/index` provides practical, task-oriented instructions for using OpenSPP's features in day-to-day operations for administrators and end-users.
- {doc}`../developer_guide/index` provides technical information and instructions for developers who need to customize, extend, integrate with, or contribute to OpenSPP.
- {doc}`../reference/index` provides detailed reference material about OpenSPP components, including module documentation and technical specifications.
- {doc}`../community/index` contains information about the OpenSPP project, community interaction, contribution processes, and legal information.
- {doc}`../reference/glossary` provides definitions and explanations of terms or specialized language used in social protection. Translations are provided in French, Spanish and Arabic.

## Technical information

OpenSPP is built on top of [Odoo 17.0](https://www.odoo.com/documentation/17.0/), a popular open-source [ERP](https://en.wikipedia.org/wiki/Enterprise_resource_planning). It is designed to be easy to install and maintain, and can be run on any Linux distribution.

To learn more, visit the {doc}`../developer_guide/architecture` section.

```{toctree}
---
caption: Getting Started
maxdepth: 2
hidden: true
---

installation_deb
module_installation
```