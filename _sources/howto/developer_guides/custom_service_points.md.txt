# Customize Service Points

The following article guides the reader in understanding how the service point module will work in OpenSPP and how it can be customized by providing a sample scenario and a working example.

## Prerequisites

- Knowledge of Python, Odoo, XML, Xpaths.
- To set up OpenSPP for development, please refer to the [Developer Guide](https://docs.openspp.org/howto/developer_guides/development_setup.html)

# If the Service Points module is not installed

- Log into OpenSPP with administrative rights.
- Access the “Apps” menu from the dashboard to manage OpenSPP modules.
- Choose “Update Apps List” to refresh the module list.
- Search for the following modules that are required to be installed such as G2P Registry: Groups, G2P Registry: Individual and G2P Registry: Membership.

![](custom_service_points/1.png)

## Utilising the Service Points Module

For more detailed guidance on utilizing the Service Point module in OpenSPP, please refer to the information available at the provided link, which will be published soon.

## Customize Service Points

In this hypothetical scenario, we will add the dropdown service point type and service point operating hours, which can be shown to the beneficiaries so they can redeem their entitlements by knowing the operation hours and service point type.

A working sample module for the described scenario can be accessed at the provided [link](https://github.com/OpenSPP/documentation_code/tree/main/howto/developer_guides/customizations/spp_service_point_custom).

The key steps in module development are as follows:

1. To customize service point, a new module can be developed.
2. To initiate the development of a custom module for service point customization, begin by creating a manifest file. This file should include fields like name, category, and version. Additionally, it's crucial to define the dependencies of the new module as outlined below.

```python
   "depends": [
       "spp_service_points",
   ],

```

3. To add the new field in the new module, develop a Python file named `service_point.py` that extends `spp.service.point` and incorporate this file into `models/init.py`. The definition of the fields should be implemented as demonstrated below.

```python
from odoo import fields, models

class OpenSPPServicePoint(models.Model):
   _inherit = "spp.service.point"

   weekday_time_start = fields.Float(string='Start Time')
   weekday_time_end = fields.Float(string='End Time')


   weekend_time_start = fields.Float(string='Start Time')
   weekend_time_end = fields.Float(string='End Time')

```

The code mentioned above will introduce the new fields to the `spp_service_point` table for storing the operating hours for weekdays and weekends. To understand further, refer to the following documentation given [1](https://www.odoo.com/documentation/15.0/developer/tutorials/getting_started/04_basicmodel.html),[2](https://www.odoo.com/documentation/15.0/developer/tutorials/getting_started/14_other_module.html),[3](https://www.odoo.com/documentation/15.0/developer/tutorials/getting_started/13_inheritance.html)

4. To integrate new fields into the UI, the following steps should be followed. Create a new file called `views/service_point_views.xml` in the module. Add the below code to the manifest file.

```python
   "data": [
       "views/service_point_views.xml",
   ],
```

The following code can be added to the `service_point_views.xml` file to show the fields in the UI.

```xml
<?xml version="1.0" encoding="utf-8" ?>
<odoo>
   <record id="view_service_points_custom" model="ir.ui.view">
       <field name="name">view_service_points_custom</field>
       <field name="model">spp.service.point</field>
       <field name="inherit_id" ref="spp_service_points.view_service_points_form" />
       <field name="arch" type="xml">
           <xpath expr="//field[@name='disabled_reason']" position="after">
               <div >
                   <h2>Weekdays</h2>
               </div>
               <field name="weekday_time_start" widget="float_time" colspan="4" />
               <field name="weekday_time_end" widget="float_time" colspan="4" />
               <div>
                   <h2>Weekends</h2>
               </div>
               <field name="weekend_time_start" widget="float_time" colspan="4" />
               <field name="weekend_time_end" widget="float_time" colspan="4" />
           </xpath>
       </field>
   </record>
</odoo>
```

5. To add the service types in the service type dropdown field, the following steps should be followed. Create a new file called `data/service_type_data.xml` in the module and ddd the below code to the manifest file.

```python
   "data": [
       "data/service_type_data.xml",
       "views/service_point_views.xml",
   ],
```

The following code can be added to the `service_type_data.xml` file to add the service types.

```xml
<?xml version="1.0" encoding="utf-8" ?>
<odoo>
   <record id="voucher_redemption_center" model="spp.service.type">
       <field name="name">Voucher Redemption Center</field>
   </record>


   <record id="in_kind_goods_distribution" model="spp.service.type">
       <field name="name">In-Kind Goods Distribution</field>
   </record>


   <record id="information_desk" model="spp.service.type">
       <field name="name">Information Desk</field>
   </record>
</odoo>
```

6. Install the module to include the new changes.

The following screenshot shows the added newly fields in the above developed module.

![](custom_service_points/2.png)
