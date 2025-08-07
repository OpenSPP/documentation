---
review-status: needs-review
review-date: 2025-06-04
reviewer: migration-script
migration-notes: "Added during 2025 documentation reorganization"
---

# Getting Started

## How the documentation is organized

This overview of how OpenSPP's documentation is organized will help you know where to look for certain things:

- {doc}`../overview/index` provides high-level information about OpenSPP's features, concepts, and use cases for decision makers and new users.
- {doc}`../user_guide/index` provides practical, task-oriented instructions for using OpenSPP's features in day-to-day operations for administrators and end-users.
- {doc}`../developer_guide/index` provides technical information and instructions for developers who need to customize, extend, integrate with, or contribute to OpenSPP.
- {doc}`../reference/index` provides detailed reference material about OpenSPP components, including module documentation and technical specifications.
- {doc}`../community/index` contains information about the OpenSPP project, community interaction, contribution processes, and legal information.
- {doc}`../reference/glossary` provides definitions and explanations of terms or specialized language used in social protection. Translations are provided in French, Spanish and Arabic.

## Technical information

OpenSPP is built on top of [Odoo 15.0](https://www.odoo.com/documentation/15.0/), a popular open-source [ERP](https://en.wikipedia.org/wiki/Enterprise_resource_planning). It is designed to be easy to install and maintain, and can be run on any Linux distribution.

To learn more, visit the {doc}`../developer_guide/architecture` section.

To begin working with OpenSPP, refer to the installation guides below.

```{toctree}
---
caption: Getting Started
maxdepth: 2
hidden: true
---

installation_docker
installation_pypi
poc_and_pilot
```