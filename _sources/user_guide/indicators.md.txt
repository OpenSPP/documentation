# Indicators

## Introduction

This section will discuss the importance of Indicators in OpenSPP. Indicators are a powerful tool that creates abstraction and simplifies targeting, allowing for the calculation of the number of children under 18 years old, the number of elderly women, or whether a household is headed by a single woman.

The Indicators play a crucial role in determining the eligibility of registrants for social protection programs, as they're computed based on the information available in the social registry. By using Indicators, errors and inaccuracies can be avoided.

## Technical considerations

Indicators are fields added to the group or individual table. In Odoo those are computed fields. To reduce the performance impact of those, those fields are recomputed. in an asynchronous job, only when the data they depend on changes. This means that the value of the field won't be available immediately after the data it depends on is changed. It will be available after the next time the job is run, usually within a second.

The indicator fields are stored as fields in the database, but they're not editable. They're computed based on the data in the registry.

```{note}
Indicators computation, if not properly written can use a lot of resources. 
While Odoo developers often write a for loop in the compute method to fetch some data, this is not a good practice.
It is recommended to fetch the data for all the records in one query and then set the value to each record.

```

## Creating an indicator field

### Through the UI

Go to **Registry → Configuration → Custom Fields** and click **Create**.

```{figure} indicators/indicator-1.png
:align: center
:height: 300
:alt: Indicator creation interface in OpenSPP
```

TODO

### Through the code

Create a model that inherits from `res.partner`. In this example, we will count the number of children in a group.

To learn more about search domain, see the Odoo documentation on [search domains](https://www.odoo.com/documentation/15.0/developer/reference/backend/orm.html#search-domains).
Search domain are like a simplified SQL query. They're used to filter the data that is used to compute the indicator.

To simplify the count of members in a group, we created a helper method `compute_count_and_set_indicator` that takes the name of the indicator field, the domain to filter the members of the group, and the domain to filter the members of the group that are used to compute the indicator.

```{eval-rst}
.. automethod:: odoo.addons.g2p_registry_membership.models.group.G2PMembershipGroup.compute_count_and_set_indicator
    :noindex:
```


```python
import datetime
from odoo import fields, models
from dateutil.relativedelta import relativedelta

CHILDREN_AGE_LIMIT = 18

class G2PGroup(models.Model):
    _inherit = "res.partner"

    z_ind_grp_num_children = fields.Integer(
        "Number of children",
        compute="_compute_ind_grp_num_children",
        help="Number of children",
        store=True,
        allow_filter=True,
    )

    def _compute_ind_grp_num_children(self):
        now = datetime.datetime.now()
        children = now - relativedelta(years=CHILDREN_AGE_LIMIT)
        domain = [("birthdate", ">=", children)]
        self.compute_count_and_set_indicator("z_ind_grp_num_children", None, domain)

```