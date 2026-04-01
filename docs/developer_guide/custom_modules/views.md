---
openspp:
  doc_status: draft
  products: [core]
---

# Views and menus

**For: developers**

This page covers the XML ID naming conventions and common view patterns for OpenSPP modules. View and menu XML follows standard Odoo conventions, but OpenSPP enforces specific naming rules via the `openspp-check-xml-ids` pre-commit hook.

## XML ID naming conventions

| Type        | Pattern                                         | Example                                   |
| ----------- | ----------------------------------------------- | ----------------------------------------- |
| List view   | `{module}_view_list` or `view_{model}_list`     | `spp_alert_view_list`                     |
| Form view   | `{module}_view_form` or `view_{model}_form`     | `spp_alert_view_form`                     |
| Search view | `{module}_view_search` or `view_{model}_search` | `spp_alert_view_search`                   |
| Action      | `action_{model}`                                | `action_spp_alert`                        |
| Menu (root) | `menu_{domain}_root`                            | `menu_spp_alerts_root`                    |
| Menu (item) | `menu_{domain}` or `menu_{domain}_{purpose}`    | `menu_spp_alerts`, `menu_spp_alert_rules` |

## List view

```xml
<record id="spp_my_feature_view_list" model="ir.ui.view">
    <field name="name">spp.my.feature.list</field>
    <field name="model">spp.my.feature</field>
    <field name="arch" type="xml">
        <list string="My Features" sample="1">
            <field name="reference" />
            <field name="name" />
            <field name="feature_type_id" />
            <field
                name="state"
                widget="badge"
                decoration-info="state == 'draft'"
                decoration-success="state == 'active'"
                decoration-muted="state == 'closed'"
            />
        </list>
    </field>
</record>
```

## Form view

```xml
<record id="spp_my_feature_view_form" model="ir.ui.view">
    <field name="name">spp.my.feature.form</field>
    <field name="model">spp.my.feature</field>
    <field name="arch" type="xml">
        <form string="My Feature">
            <header>
                <button
                    name="action_activate"
                    string="Activate"
                    type="object"
                    class="btn-primary"
                    invisible="state != 'draft'"
                />
                <field
                    name="state"
                    widget="statusbar"
                    statusbar_visible="draft,active,closed"
                />
            </header>
            <sheet>
                <div class="oe_title">
                    <h1>
                        <field name="reference" readonly="1" />
                    </h1>
                </div>
                <group>
                    <group>
                        <field name="name" />
                        <field name="feature_type_id" />
                    </group>
                    <group>
                        <field name="partner_id" />
                        <field name="company_id" groups="base.group_multi_company" />
                    </group>
                </group>
                <notebook>
                    <page string="Items" name="items">
                        <field name="item_ids" />
                    </page>
                </notebook>
            </sheet>
            <chatter />
        </form>
    </field>
</record>
```

### Key patterns

- Use `<header>` for status bar and action buttons
- Use `invisible` attribute (not `attrs`) for conditional visibility (Odoo 19 change)
- Include `<chatter />` if your model inherits `mail.thread`
- Use `groups="base.group_multi_company"` on `company_id` to only show it in multi-company setups

## Search view

```xml
<record id="spp_my_feature_view_search" model="ir.ui.view">
    <field name="name">spp.my.feature.search</field>
    <field name="model">spp.my.feature</field>
    <field name="arch" type="xml">
        <search string="Search My Features">
            <field name="name" />
            <field name="reference" />
            <field name="partner_id" />
            <filter
                name="filter_active"
                string="Active"
                domain="[('state', '=', 'active')]"
            />
            <filter
                name="filter_draft"
                string="Draft"
                domain="[('state', '=', 'draft')]"
            />
            <separator />
            <group expand="0" string="Group By">
                <filter
                    name="group_state"
                    string="State"
                    context="{'group_by': 'state'}"
                />
                <filter
                    name="group_type"
                    string="Type"
                    context="{'group_by': 'feature_type_id'}"
                />
            </group>
        </search>
    </field>
</record>
```

## Action

```xml
<record id="action_spp_my_feature" model="ir.actions.act_window">
    <field name="name">My Features</field>
    <field name="res_model">spp.my.feature</field>
    <field name="view_mode">list,form</field>
    <field name="search_view_id" ref="spp_my_feature_view_search" />
    <field name="context">{'search_default_filter_active': 1}</field>
    <field name="help" type="html">
        <p class="o_view_nocontent_smiling_face">
            Create your first feature
        </p>
    </field>
</record>
```

## Menus

```xml
<!-- Root menu -->
<menuitem
    id="menu_spp_my_feature_root"
    name="My Feature"
    parent="base.menu_custom"
    sequence="100"
    groups="spp_my_module.group_myfeature_viewer"
/>

<!-- List menu -->
<menuitem
    id="menu_spp_my_feature"
    name="Features"
    parent="menu_spp_my_feature_root"
    action="action_spp_my_feature"
    sequence="10"
    groups="spp_my_module.group_myfeature_viewer"
/>
```

### Menu visibility

Always set the `groups` attribute on menus:

- Use the **viewer** group for read-only menus (visible to all roles)
- Use the **manager** group for configuration/admin menus (visible only to managers)

## Extending existing views

To add fields to an existing view, use XPath inheritance:

```xml
<record id="spp_my_feature_partner_form" model="ir.ui.view">
    <field name="name">spp.my.feature.partner.form</field>
    <field name="model">res.partner</field>
    <field name="inherit_id" ref="spp_registry.view_individuals_form" />
    <field name="arch" type="xml">
        <xpath expr="//page[@name='ids']" position="after">
            <page string="My Feature" name="my_feature">
                <field name="my_custom_field" />
            </page>
        </xpath>
    </field>
</record>
```
