# Computed Fields

Computed fields in Odoo are dynamic fields whose values are calculated in real-time, rather than being directly stored in the database. These fields are essential for scenarios where the field value is a result of a computation involving other field values.

## Creating a Computed Field

To define a computed field, you'll need to establish your field and assign a computation method to its compute attribute. This method calculates the field's value for every record.

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
- Within this method, self represents a recordset and should be iterable.
- Computed fields are executed only when accessed and their values are not stored in the database by default.

In this example, the value of the computed field is based on the value of the “amount” field but it will only execute if the “total” field is called. In this case, the value of the “total” field will not update even after changing the value of the “amount” field. To solve this problem, add dependencies to the method.

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

In this example, the method have a decorator “api.depends” with an argument “amount” which corresponds to the “amount” field, it declares that this method depends on the value of the “amount” field and this method will execute if “amount” field’s value is change thus “total” field will be updated.

## Create a Stored Computed Field

While a regular computed field's value is calculated on-the-fly, a stored computed field allows its computed value to be stored in the database. To create a stored computed field, add the store=True parameter to your field declaration.

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

This approach ensures that the value of total is persisted in the database, reducing computation needs for repeated access.

This overview covers the basics of computed fields in Odoo. For a more in-depth understanding, including advanced techniques and best practices, refer to the official Odoo documentation on computed fields [here](https://www.odoo.com/documentation/17.0/developer/tutorials/getting_started/09_compute_onchange.html#)
