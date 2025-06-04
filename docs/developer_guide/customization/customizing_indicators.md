# Indicators

The indicators in OpenSPP are built using computed fields. The computed fields in Odoo are dynamic fields whose values are calculated in real time rather than being directly stored in the database. These fields are essential for scenarios where the field value results from a computation involving other field values.

## 1. Creating a Computed Field

To define a computed field, you must establish your field and assign a computation method to its compute attribute. This method calculates the field's value for every record.

```python
class SampleModel(models.Model):
   _name = "sample.model"

   total = fields.Float(compute="_compute_total")
   amount = fields.Float()

   def _compute_total(self):
       for record in self:
           record.total = 2.0 * record.amount
```

Key Points

- The computation method, conventionally named with a `_compute` prefix, is responsible for setting the field's value.
- Within this method, the `self` represents a record set and should be iterable.
- Computed fields are executed only when accessed, and their values are not stored in the database by default.

In this example, the value of the computed field is based on the value of the `amount` field, but it will only execute if the `total` field is called. In this case, the value of the `total` field will not update even after changing the value of the `amount` field. To solve this problem, add dependencies to the method.

```python
class SampleModel(models.Model):
   _name = "sample.model"

   total = fields.Float(compute="_compute_total")
   amount = fields.Float()

   @api.depends("amount")
   def _compute_total(self):
       for record in self:
           record.total = 2.0 * record.amount
```

The method has a decorator `api.depends` with an argument `amount`, which corresponds to the `amount` field; it declares that this method depends on the value of the `amount` field and this method will execute if `amount` field's value is change thus `total` field will be updated.

## 2. Create a Stored Computed Field

While a regular computed field's value is calculated on the fly, a stored computed field allows its computed value to be stored in the database. Add the `store=True` parameter to your field declaration to create a stored computed field field.

```python
class SampleModel(models.Model):
   _name = "sample.model"

   total = fields.Float(compute="_compute_total", store=True)
   amount = fields.Float()

   @api.depends("amount")
   def _compute_total(self):
       for record in self:
           record.total = 2.0 * record.amount
```

This approach ensures that the value of the total is persisted in the database, reducing computation needs for repeated access.

This overview covers the basics of computed fields in Odoo. For a more in-depth understanding, including advanced techniques and best practices, refer to the official Odoo [documentation](https://www.odoo.com/documentation/17.0/developer/tutorials/server_framework_101/08_compute_onchange.html) on computed fields.

## 3. Sample Use-case 1

In a real-life scenario, most form applications have a birth date field and no age field since the age of a person can be determined by using the birth date. To apply this scenario in Odoo, we need to use a computed field.

```python
from datetime import date

class ResPartner(models.Model):
   _inherit = "res.partner"

   birthdate = fields.Date("Date of Birth")
   age = fields.Int(compute="_compute_age")

   @api.depends("birthdate")
   def _compute_age(self):
       today = date.today()
       for rec in self:
           rec.age = today.year - rec.birthdate.year - ((today.month, today.day) < (rec.birthdate.month, rec.birthdate.day))
```

In this example, a birthdate field and a computed age field that depends on the `birthdate` field using the function `_compute_age` are created, `age` is computed by getting and using the current date and the date in the `birthdate` field. `age` field will be automatically updated every time the `birthdate` field is updated since the compute method have a dependencies to the `birthdate` field.

## 4. Sample Use-case 2

In a hypothetical scenario, If a group/family should know the number of individuals that are under five years old, we can to use a computed field.

```python
from odoo import api, fields, models

class G2PGroup(models.Model):
   _inherit = "res.partner"

   z_ind_grp_num_children_below_5 = fields.Integer(
       "Number of children below 5 years old",
       compute="_compute_ind_ind_grp_num_children_below_5",
       help="Number of children below 5 years old",
       store=True,
       allow_filter=True,
   )

   @api.depends("group_membership_ids", "group_membership_ids.birthdate")
   def _compute_ind_ind_grp_num_children_below_5(self):
       for rec in self:
           total = 0
           for membership in rec.group_membership_ids:
               try:
                   age = int(membership.individual.age)
               except Exception:
                   age = None

               if age and age < 5:
                   total += 1
           rec.z_ind_grp_num_children_below_5 = total
```

In this example, a computed field with a computed function that is based on the member's birth date is created. A parameter `store=True` is added in the computed field to save this field in the database where it can be queried in the model.

Further, using the `z_ind_grp` will allow you to add the indicator at the group level as shown in the above example.

```python
self.env["res.partner"].search(["z_ind_grp_num_children_below_5", "=", 1])
```

The above query will only retrieve records with one child under five years old.
