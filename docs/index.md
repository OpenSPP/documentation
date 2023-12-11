---
myst:
  html_meta:
    "description": "This website is the HTML documentation of OpenSPP, an open source social protection platform."
    "property=og:description": "This website is the HTML documentation of OpenSPP, an open source social protection platform."
    "property=og:title": "OpenSPP Documentation"
    "keywords": "OpenSPP, open source, Documentation"
---

(index-label)=

# OpenSPP - Social Protection Platform

OpenSPP is an open-source, modular and highly interoperable platform for social protection offering a comprehensive management information system and registries which can be easily adapted to a country’s needs, goals and existing systems.

## How the documentation is organized

A high-level overview of how OpenSPP’s documentation is organized will help you know where to look for certain things:

- [Tutorials](tutorials/index) are lessons that guide you through a topic and help you to achieve basic competence and familiarity with the platform. Tutorials will help you to make sense of the rest of the documentation. Start here if you are new to OpenSPP.
- [User guides](user_guide/index) discuss key topics and concepts at a fairly high level and provide useful background information and explanation.
- [Reference guides](technical_reference/index) are technical descriptions of the software, and describe how OpenSPP works and how to use it. They are technical documents and assume that you have a basic understanding of key software concepts.
- [How-to guides](howto/index) provide detailed instructions on how to use the specific features and modules of OpenSPP. They provide step by step guidance on how to perform a specific task or achieve a particular goal. They are more advanced than tutorials and assume some knowledge of how OpenSPP works.
- [Explanations](explanation/index) help to clarify, deepen and broaden understanding of a subject. They help to explain the background and context of why certain things are done e.g. design decisions, historical reasons, technical constraints. Explanations help to give a bigger picture and join things together.
- [Glossary](glossary/index) provides definitions and explanations of terms or specialized language used in social protection. Translations are provided in French, Spanish and Arabic.

## Guiding principles

Our guiding principles are informed by the Digital Public Goods Standard and the Principles for Digital Development.

- **User-centricity**: Our products are designed to be intuitive and pragmatic, recognizing that social protection operates in complex, resource-constrained and rapidly changing contexts.
- **Modularity**: The platform is composed of independent modules which allow for flexibility, scalability, and the interchangeability of components.
- **Privacy and security**: We rigorously uphold privacy and security standards - essential prerequisites for safeguarding Digital Public Goods.
- **Interoperability**: The platform is designed to support system interoperability - critical for the creation of cohesive and efficient digital ecosystems.
- **Inclusivity**: Our products can be customized to suit linguistic and cultural requirements, accessibility, digital literacy, and deployment in remote and less-developed contexts.

## Technical information

`OpenSPP` is built on top of [Odoo 15.0](https://odoo.com/documentation/15.0/), a popular open-source [ERP](https://en.wikipedia.org/wiki/Enterprise_resource_planning). It is designed to be easy to install and maintain, and can be run on any Linux distribution.

The OpenSPP platform is evolving rapidly. If you have any questions or needs, please do not hesitate to contact us through Github issues or our [Website](https://openspp.org/).

To learn more, take a look at the [Architecture](technical_reference/architecture) page.

```{toctree}
:maxdepth: 3
:hidden: true

tutorials/index
user_guide/index
howto/index
technical_reference/index
explanation/index
community_and_support/index
contributing/index
```

```{toctree}
:caption: Appendices
:maxdepth: 1
:hidden: true

glossary
```

{ref}`genindex`
