---
review-status: needs-review
review-date: 2025-08-28
reviewer: "Edwin Gonzales"
migration-notes: "Added during 2025 documentation reorganization"
---

# Module Development

OpenSPP is built on the powerful and flexible Odoo framework. One of the core principles of Odoo is its modular architecture. Instead of modifying the core source code of the platform, customizations and new features are added through self-contained packages called **modules**.

This guide will walk you through the fundamental process of creating a custom OpenSPP module. We will build a simple but practical module that adds a "National ID" field to the Individual record in the registry.

By the end of this guide, you will understand:
- Why creating a custom module is the best practice.
- The basic structure of an OpenSPP/Odoo module.
- How to extend existing models to add new data fields.
- How to modify user interface forms to display these new fields.
- The complete process for installing and activating your custom module.

### Why Create a Custom Module?

For developers new to Odoo, it might seem easier to directly edit the existing OpenSPP files. However, this approach, often called forking, leads to significant long-term problems. The recommended approach is to encapsulate all your customizations within a custom module.

**Key Advantages of Using Modules:**

- **Maintainability & Upgradability:** When a new version or security patch for OpenSPP is released, you can update the core platform code without losing your custom features. Your module remains separate and can be easily installed on the new version, often with minimal changes.
- **Cleanliness & Organization:** Your custom code is neatly organized in its own directory, making it easy to find, understand, and manage.
- **Portability:** You can easily share your module with other projects or deploy it on different OpenSPP instances.
- **Collaboration:** It allows multiple teams to work on different custom features without creating conflicts in the core codebase.

In short, creating modules is the professional standard for Odoo and OpenSPP development that ensures your solution is robust and future-proof.

This modular approach is the foundation for all advanced customizations. From here, you can explore:
- Adding more complex field types (Selection, Many2one, etc.).
- Creating entirely new models and menus.
- Adding business logic with Python methods.

By mastering this pattern, you can tailor OpenSPP to meet any specific program requirement while ensuring your implementation remains clean, stable, and easy to maintain.

## Best Practices in OpenSPP Development

For more detailed guidelines, refer to the {doc}`Best Practices Guide <../best_practices>`.

## References

For more information on developing OpenSPP modules, refer to:
- [Odoo 17 Developer Documentation](https://www.odoo.com/documentation/17.0/developer/)
- [OpenSPP Documentation](https://docs.openspp.org/)
- [OpenSPP Source](https://github.com/OpenSPP/openspp-modules/tree/17.0/)

```{toctree}
:maxdepth: 2
:hidden: true
:caption: Contents

areas
audit
change_requests
cycles
dashboard
dms
entitlements
fields
indicators
programs
registry
rest_api
service_points
```