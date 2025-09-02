---
review-status: reviewed
review-date: 2025-09-01
reviewer: Mark Penalosa
migration-notes: "Added during 2025 documentation reorganization"
---

# Concepts

This section is dedicated to exploring the core concepts and theoretical foundations of OpenSPP platform. Unlike reference materials that focus on specific functionalities, this documentation provides a higher-level understanding of the principles and philosophies guiding OpenSPP's design and implementation.

- {doc}`data_collection_validation`: This document outlines OpenSPP's approach to data, emphasizing data minimization, user consent, and versatile input methods. It also covers the platform's validation processes, including input validation, data integrity checks, and a mix of automated and manual validation.

- {doc}`data_protection`: This document details the principles of data protection within the context of Digital Public Infrastructure. It covers key concepts like lawfulness, data minimization, and accountability, and provides measures for implementing strong data protection.

- {doc}`digital_public_infrastructure`: This document introduces the concept of Digital Public Infrastructure (DPI) and its essential components. It explains the role of DPI in social protection and how OpenSPP aligns with DPI principles through its modular and interoperable architecture.

- {doc}`extensibility`: This document explains how OpenSPP's foundation on the Odoo framework makes it a highly customizable, configurable, and extensible platform. It covers concepts like modular architecture, inheritance, and the use of a large ecosystem of pre-built modules.

- {doc}`integrated_beneficiary_registry`: This document defines the Integrated Beneficiary Registry (IBR) and explains its role in social protection. It details the key components of an IBR, its advantages, and its relationship with a social registry.

- {doc}`registrant_concepts`: This document introduces the key terminology related to registrants in OpenSPP. It defines what a registrant is and explains the core concepts of individuals, groups, group memberships, and their relationships within the system.

- {doc}`registry_key_concepts`: This document outlines the best practices for organizing data within the OpenSPP registry, emphasizing a minimalistic approach. It provides guidance on where to store different types of data and introduces the four main components of the registry's structure.

- {doc}`user_management`: This document describes the user management framework in OpenSPP, which is designed to safeguard user data and control access to system features. It covers the two main approaches to user management and outlines best practices for ensuring security and efficiency.

By delving into these concepts, you will gain a deeper appreciation for how OpenSPP works, enabling you to make more informed decisions when configuring and utilizing the platform for your specific needs.

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
```
