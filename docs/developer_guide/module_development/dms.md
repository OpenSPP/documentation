---
review-status: needs-review
review-date: 2025-08-22
reviewer: migration-script
migration-notes: "Added during 2025 documentation reorganization"
---

# Document Management System

The OpenSPP Document Management System (DMS), provided by the `spp_dms` module, is a robust system for organizing and managing files. It allows for a structured repository of documents related to social protection programs, using a hierarchy of directories, files, and categories.

**Document Categories** are a key feature of the DMS, allowing users to classify files for streamlined searching, filtering, and reporting. This guide will walk you through the simple process of extending the DMS by adding new, custom document categories. We will create a small module that adds a "Proof of School Enrollment" category, which can then be used to classify documents across the platform.

By the end of this guide, you will be able to:

- Understand how to add new DMS categories.
- Create a simple data module to extend DMS functionality.
- Register the new categories so they are available system-wide.

## Prerequisites

- Solid understanding of Odoo 17 module development, including Python, XML, and XPath.
- Familiarity with the `OpenSPP Document Management System` (`spp_dms`) core module.
- To set up OpenSPP for development, please refer to the {doc}`Development Setup Guide <../setup>`.

## Module Structure

A module for adding new DMS categories is very simple and typically only contains data files. Here's the complete structure of the module we will build, `spp_dms_school_documents`:

```
spp_dms_school_documents/
├── __init__.py
├── __manifest__.py
└── data/
    └── dms_category_data.xml
```

---

## Step-by-Step Guide

### Step 1: Create the Module Scaffold

Begin by creating a new directory for your module (e.g., `spp_dms_school_documents`) and add the basic Odoo module files: `__init__.py` and `__manifest__.py`. Then, create the `data` subdirectory.

### Step 2: Define the Manifest (`__manifest__.py`)

The manifest file declares your module's metadata and its dependencies. Our module only needs to depend on `spp_dms` to get access to the `spp.dms.category` model.

```python
# From: spp_dms_school_documents/__manifest__.py
{
    "name": "OpenSPP DMS School Documents",
    "summary": "Adds custom DMS categories for school-related documents.",
    "category": "OpenSPP",
    "version": "17.0.1.0.0",
    "author": "OpenSPP.org",
    "website": "https://github.com/OpenSPP/openspp-modules",
    "license": "LGPL-3",
    "depends": [
        "spp_dms",
    ],
    "data": [
        "data/dms_category_data.xml",
    ],
    "installable": True,
    "auto_install": False,
}
```

### Step 3: Create the Data File

This is where you define the new document categories. In the `data/` directory, create an XML file named `dms_category_data.xml`.

This file will contain one or more `<record>` tags that create new entries in the `spp.dms.category` model. Each record needs a unique ID and the name of the new category.

```xml
<!-- From: spp_dms_school_documents/data/dms_category_data.xml -->
<?xml version="1.0" encoding="utf-8" ?>
<odoo>
    <data noupdate="1">

        <record id="spp_dms_school_enrollment" model="spp.dms.category">
            <field name="name">Proof of School Enrollment</field>
        </record>

        <record id="spp_dms_report_card" model="spp.dms.category">
            <field name="name">School Report Card</field>
        </record>

    </data>
</odoo>
```
The `noupdate="1"` attribute prevents the data from being overwritten if the module is updated, which is standard practice for configuration data that users might modify.

### Step 4: Install and Use Your New Categories

1.  Install or upgrade the module through the Apps menu.
2.  Install your new module (`spp_dms_school_documents`).
3.  To verify that the new categories have been added, navigate to **DMS -> Configuration -> Categories**. You should see "Proof of School Enrollment" and "School Report Card" in the list.
4.  Now, when you upload a new file anywhere in the DMS, these new categories will be available in the **Category** dropdown menu, allowing you to classify your documents appropriately.

## References

For more information on extending OpenSPP modules, refer to:
- [Odoo 17 Developer Documentation](https://www.odoo.com/documentation/17.0/developer/)
- [OpenSPP Documentation](https://docs.openspp.org/)
- [OpenSPP DMS Module Source](https://github.com/OpenSPP/openspp-modules/tree/17.0/spp_dms)
