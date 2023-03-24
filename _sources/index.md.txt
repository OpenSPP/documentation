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

OpenSPP is an open-source project that aims to streamline the management of social protection programs. It can be used on its own or in conjunction with other services.

## How the documentation is organized
A high-level overview of how OpenSPP’s documentation is organized will help you know where to look for certain things:

- [Tutorials](tutorials/index) take you by the hand through a series of steps to create a web application. Start here if you’re new to Django or web application development. Also look at the “First steps”.
- [User guides](user_guide/index) discuss key topics and concepts at a fairly high level and provide useful background information and explanation.
- [Technical guides](technical_reference/index) contain technical reference for APIs and other aspects of OpenSPP's machinery. They describe how it works and how to use it but assume that you have a basic understanding of key concepts.
- [How-to guides](howto/index) are recipes. They guide you through the steps involved in addressing key problems and use-cases. They are more advanced than tutorials and assume some knowledge of how OpenSPP works.
- [Glossary](glossary/index) contain background information and reference material.

## Principles

OpenSPP is based on the following principles:

- **Design for the user**: the project is designed to be easy to use and to meet the needs of the users in the field.
- **Focused on the needs of low to middle income countries**: the project is designed to meet the needs of low to middle income countries.
- **Open source**: the project is open source and free to use for any purpose, including commercial use.
- **Modular**: the project is modular and can be used on its own or in conjunction with other services.

## Technical information

`OpenSPP` is built on top of [Odoo 15.0](https://odoo.com/documentation/15.0/), a popular open-source [ERP](https://en.wikipedia.org/wiki/Enterprise_resource_planning). It is designed to be easy to install and maintain, and can be run on any Linux distribution.

The project is currently under development, and everything is evolving rapidly as a result of our users' comments. If you have any questions or needs, please do not hesitate to contact the team through Github issues or our [Website](https://openspp.org/).

To learn more, take a look at the [Architecture](technical_reference/architecture) page.


```{toctree}
:maxdepth: 2
:hidden: true

tutorials/index
user_guide/index
howto/index
technical_reference/index
community_and_support/index
contributing/index
```

```{toctree}
:caption: Appendices
:maxdepth: 1
:hidden: true

glossary/index
```

{ref}`genindex`
