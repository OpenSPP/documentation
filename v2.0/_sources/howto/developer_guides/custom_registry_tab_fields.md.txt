---
openspp:
  doc_status: unverified
  products: [core]
---

# Customize Registry's Tabs/Fields

The following article guides the reader in understanding how the registry’s tabs and fields can be customized. In this article, we will look at how to add and remove the tabs and fields in the registry module.

## Prerequisites

- Knowledge of Python, Odoo, XML, Xpaths.
- To set up OpenSPP for development, please refer to the [Developer Guide](https://docs.openspp.org/howto/developer_guides/development_setup.html)
- Refer [Customize Registry](https://docs.openspp.org/howto/developer_guides/custom_registry.html) for basic customizations of Registry module

## Adding a new tab and a field

To add a new tab and a new field in Group or/and in Individual Page, use xpath and view inheritance. Check the code samples below.

1. Example 1

The file name is `group_views.xml`.

```xml
<record id="view_custom_groups_form" model="ir.ui.view">
    <field name="name">view_custom_groups_form</field>
    <field name="model">res.partner</field>
    <field name="inherit_id" ref="spp_registry.view_groups_form" />
    <field name="arch" type="xml">
        <xpath expr="//page[@name='basic_info']" position="after">
            <page string="Disability information" name="disability_info">
                <group col="4" colspan="4">
                    <field name="grp_with_disability_individual" />
                </group>
            </page>
        </xpath>
    </field>
</record>
```

This code snippet adds a new tab titled "Disability Information" to the Group form in OpenSPP, featuring a field for disability-related data.

2. Example 2

The file name is `individual_views.xml`.

```xml
<record id="view_individuals_salary_detail" model="ir.ui.view">
    <field name="name">view_individuals_salary_detail</field>
    <field name="model">res.partner</field>
    <field name="inherit_id" ref="spp_registry.view_individuals_form" />
    <field name="arch" type="xml">
        <!-- Adding a new tab and adding a new field in a tab -->
        <xpath expr="//page[@name='basic_info']" position="after">
            <page string="Disability information" name="disability_info">
                <group col="4" colspan="4">
                    <field name="ind_disability_type" />
                    <field name="ind_special_notes" />
                </group>
            </page>
        </xpath>
    </field>
</record>
```

This code introduces a new tab called "Disability Information" to the Individual form in OpenSPP, containing fields for the type of disability and special notes.

## Removing an existing tab and a field

In removing an existing tab or existing field, use xpath with a position `attributes` and add `invisible` attribute to the tab or field you want to remove. Check the code samples below.

1. Example 1

The file name is `group_views.xml`.

```xml
<record id="view_custom_groups_form" model="ir.ui.view">
    <field name="name">view_custom_groups_form</field>
    <field name="model">res.partner</field>
    <field name="inherit_id" ref="spp_registry.view_groups_form" />
    <field name="arch" type="xml">
        <!-- removing a tab -->
        <xpath expr="//page[@name='other']" position="attributes">
            <attribute name="invisible">1</attribute>
        </xpath>

        <!-- removing a field -->
        <xpath expr="//field[@name='phone_number_ids']" position="attributes">
            <attribute name="invisible">1</attribute>
        </xpath>
    </field>
</record>
```

This code hides an existing tab named `other` and a field `phone_number_ids` in the Group form, making them invisible in the user interface.

2. Example 2

The file name is `individual_views.xml`.

```xml
<record id="view_individuals_salary_detail" model="ir.ui.view">
    <field name="name">view_individuals_salary_detail</field>
    <field name="model">res.partner</field>
    <field name="inherit_id" ref="spp_registry.view_individuals_form" />
    <field name="arch" type="xml">
        <!-- removing a tab -->
        <xpath expr="//page[@name='other']" position="attributes">
            <attribute name="invisible">1</attribute>
        </xpath>

        <!-- removing a field -->
        <xpath expr="//field[@name='birth_place']" position="attributes">
            <attribute name="invisible">1</attribute>
        </xpath>
    </field>
</record>
```

This snippet is used to make an existing tab named `other` and a field `birth_place` invisible in the Individual form interface.
