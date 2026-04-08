---
myst:
  html_meta:
    "title": "OpenSPP Core Concepts"
    "description": "Core concepts and theoretical foundations of OpenSPP social protection platform"
    "keywords": "OpenSPP, concepts, digital public infrastructure, data protection, registry"
---

# Concepts

These concepts explain the theoretical foundations and design principles behind OpenSPP. Understanding them helps you make better decisions about implementation and customization.

## Architecture and design


**{doc}`Digital public infrastructure <digital_public_infrastructure>`**: Essential components of DPI and how OpenSPP aligns with DPI principles through modular, interoperable architecture.

**{doc}`Integrated beneficiary registry <integrated_beneficiary_registry>`**: Key components of an IBR, its advantages, and its relationship with social registries.

**{doc}`Extensibility <extensibility>`**: How OpenSPP's Odoo foundation enables customization through modular architecture and inheritance.

**{doc}`Modularity <modularity>`**: Understanding modularity in OpenSPP and how modular architecture enables faster deployment, easier feature addition, and reduced risk.

**{doc}`Odoo Framework Value <odoo_framework_value>`**: Understanding the value of Odoo framework for OpenSPP clients: built-in ERP features, technical ecosystem, and modular design benefits.

**{doc}`Configuration vs Customization <configuration_vs_customization>`**: Comparing configuration and customization approaches: functional, technical, cost, time, and maintenance implications for PM, BA, and Sales decision-making.

## Data management

**{doc}`Registry key concepts <registry_key_concepts>`**: Best practices for organizing data with a minimalistic approach and the four main registry structure components.

**{doc}`Registrant concepts <registrant_concepts>`**: Core terminology for individuals, groups, group memberships, and their relationships.

**{doc}`Data collection and validation <data_collection_validation>`**: Data minimization, user consent, versatile input methods, and validation processes.

## Security and governance

**{doc}`Data protection <data_protection>`**: Principles of lawfulness, data minimization, and accountability within DPI context.

**{doc}`User management <user_management>`**: Framework for controlling system access and safeguarding user data with two management approaches.

**{doc}`Role-Based Access Control <role_based_access_control>`**: Why RBAC is critical for security, auditing, and workflow integrity in OpenSPP social protection programs.

## Social protection foundations

**{doc}`Social Protection Management Information System <sp_mis_concepts>`**: Introduction to Social Protection Management Information Systems (SPMIS) and their role in the social protection ecosystem.

**{doc}`Social Registry <social_registry_concepts>`**: Introduction to Social Registries and their role in the social protection ecosystem.

**{doc}`Farmer Registry <farmer_registry_concepts>`**: Introduction to Farmer Registries and their role in the social protection ecosystem.

```{toctree}
---
caption: Learn
maxdepth: 2
hidden: true
---

digital_public_infrastructure
integrated_beneficiary_registry
user_management
data_collection_validation
registrant_concepts
registry_key_concepts
data_protection
extensibility
modularity
odoo_framework_value
configuration_vs_customization
role_based_access_control
sp_mis_concepts
social_registry_concepts
farmer_registry_concepts
```
