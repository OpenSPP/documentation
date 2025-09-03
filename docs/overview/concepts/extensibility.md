---
myst:
  html_meta:
    "title": "OpenSPP Extensibility Concepts"
    "description": "How OpenSPP enables customization through modular Odoo architecture and inheritance for social protection programs"
    "keywords": "OpenSPP, extensibility, customization, Odoo, modular architecture, inheritance, social protection"
---

# Customisable, configurable, and extensible

OpenSPP is a highly adaptable digital social protection information system designed to improve the {term}`efficiency` and {term}`effectiveness` of social protection programs in low and middle-income countries. Thanks to its foundation on the widely used ERP platform, Odoo, OpenSPP offers unparalleled customizability, configurability, and extensibility. This page aims to give technical personnel a thorough understanding of these key features.

## Customisable

OpenSPP's customizability is deeply rooted in its underlying Odoo framework, an open-source ERP platform known for its modular architecture and flexibility. This section will delve into the details of how Odoo empowers the customizability of OpenSPP.

### Modular architecture

Odoo's modular architecture enables developers to create, change, and extend functionalities by working with individual modules. Each module encapsulates specific features, making it easier to develop, support, and upgrade the system without disrupting its core functionality. In OpenSPP, this modular approach allows countries to implement custom solutions that address their unique social protection requirements.

### Inheritance and overrides

Odoo provides a powerful inheritance mechanism, which lets new modules extend, change, or override existing functionalities without altering the original code. This allows OpenSPP to be adapted to specific needs while preserving the ability to receive updates and enhancements in the future.

For example, a developer can create a new module that inherits from an existing module, extending its features or modifying its behavior to meet custom requirements. This can include adding new fields to existing models, changing the way certain methods work, or altering the user interface.

### Python and XML

Odoo is built using Python, a popular programming language with extensive libraries and community support. The platform also relies on XML to define user interface components and initial data. Leveraging these widely used technologies, developers can create custom modules for OpenSPP and change the platform to meet specific needs.

### Odoo Studio

```{note}
This is a paid feature offered by Odoo, not part of the OpenSPP project.
```

Odoo Studio is a user-friendly, visual tool for creating custom modules and changing existing ones. With its drag-and-drop interface, developers can create new applications, modify views, and design workflows without writing code. This lowers the barrier to entry for customizing OpenSPP, allowing even non-technical users to tailor the system to their needs.

## Configurable

OpenSPP's configurability allows implementers to adapt the system's functionality to various scenarios without requiring more customization. The platform offers many options to manage product offerings, rules, and workflows to accommodate diverse use cases.

## Extensible

OpenSPP's extensibility is in part a direct result of its foundation on the Odoo framework, which has been designed with extensibility and adaptability in mind. This section will explore the various aspects of Odoo that make OpenSPP a highly extensible solution.

### Large ecosystem

Odoo boasts a vast ecosystem of pre-built modules and third-party applications developed by its extensive community. This wealth of resources enables OpenSPP users to access a wide range of functionalities and integrations, helping them address specific needs without starting from scratch. With over 15,000 modules available, the possibilities for extending OpenSPP are nearly endless.

### REST API and web services

OpenSPP provides powerful web services and REST APIs, allowing external applications and systems to interact with OpenSPP seamlessly. These APIs enable developers to retrieve, create, update, and delete data in OpenSPP, as well as call methods and execute workflows. By leveraging these web services, countries can integrate OpenSPP with other systems, such as payment gateways, reporting tools, or government databases.

### Custom add-ons path

Odoo enables administrators to specify custom add-ons paths, allowing the installation of third-party modules and extensions without modifying the core platform. This feature ensures that any added extensions or modules can be maintained separately from the core system, preserving the integrity of OpenSPP while allowing for future updates and enhancements.

## Summary

In summary, OpenSPP's customizable, configurable, and extensible nature, made possible by its Odoo foundation, enables implementers to develop tailor-made solutions for their social protection programs. The platform's modular customizations, configurable settings, and extensibility ensure a robust and adaptable system that can evolve alongside the ever-changing needs of low and middle-income countries.
