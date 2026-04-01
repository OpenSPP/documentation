---
openspp:
  doc_status: draft
  products: [core]
---

# Models

**For: developers**

This page covers the rules and patterns for defining Odoo models in OpenSPP modules. These conventions are enforced by pre-commit hooks — violations will block your commits.

## Model namespace

All OpenSPP models must use the `spp.*` namespace:

```python
class MyModel(models.Model):
    _name = "spp.my.feature"              # Single domain
    _description = "My Feature"

class MySubModel(models.Model):
    _name = "spp.my.feature.item"         # Domain + entity
    _description = "My Feature Item"
```

The deprecated `g2p.*` namespace is rejected by linting.

Standard Odoo models (`res.partner`, `res.users`, `ir.model`, etc.) are exempt from this rule when using `_inherit` to extend them.

## Field naming rules

OpenSPP enforces specific naming conventions for fields. These are checked by the `openspp-check-naming` pre-commit hook.

### Boolean fields

Must start with a recognized prefix:

```python
# Correct
is_active = fields.Boolean()
has_children = fields.Boolean()
can_approve = fields.Boolean()
enable_notifications = fields.Boolean()
show_details = fields.Boolean()

# Will fail linting
active_flag = fields.Boolean()    # No recognized prefix
approved = fields.Boolean()       # No recognized prefix
```

Recognized prefixes: `is_`, `has_`, `can_`, `enable_`, `show_`, `notify_on_`, `allow_`, `require_`, `auto_`.

### Many2one fields

Must end with `_id`:

```python
# Correct
program_id = fields.Many2one("spp.program")
alert_type_id = fields.Many2one("spp.vocabulary.code")

# Will fail linting
program = fields.Many2one("spp.program")
```

Common exceptions (these don't need `_id`): `parent`, `company`, `partner`, `user`, `currency`, `country`, `state`.

### One2many and Many2many fields

Must end with `_ids`:

```python
# Correct
membership_ids = fields.One2many("spp.group.membership", "group")
tag_ids = fields.Many2many("spp.vocabulary.code")

# Will fail linting
memberships = fields.One2many("spp.group.membership", "group")
```

## Model structure pattern

Here is a typical model following OpenSPP conventions:

```python
# Part of OpenSPP. See LICENSE file for full copyright and licensing details.
import logging

from odoo import _, api, fields, models
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)


class MyFeature(models.Model):
    """Brief description of what this model represents.

    Longer description explaining the purpose and key behaviors.
    """

    _name = "spp.my.feature"
    _description = "My Feature"
    _inherit = ["mail.thread"]
    _order = "create_date desc"
    _check_company_auto = True

    # === IDENTIFICATION ===
    name = fields.Char(required=True, tracking=True)
    reference = fields.Char(
        required=True,
        copy=False,
        readonly=True,
        default=lambda self: _("New"),
    )

    # === CLASSIFICATION ===
    feature_type_id = fields.Many2one(
        "spp.vocabulary.code",
        string="Type",
        domain="[('vocabulary_id.name', '=', 'Feature Types')]",
    )

    # === STATE ===
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("active", "Active"),
            ("closed", "Closed"),
        ],
        default="draft",
        tracking=True,
    )

    # === RELATIONSHIPS ===
    partner_id = fields.Many2one("res.partner", string="Registrant")
    item_ids = fields.One2many("spp.my.feature.item", "feature_id")

    # === FLAGS ===
    is_archived = fields.Boolean(default=False)

    # === COMPANY ===
    company_id = fields.Many2one(
        "res.company",
        required=True,
        default=lambda self: self.env.company,
    )
```

### Key patterns

- **Use `mail.thread`** for models that need change tracking (adds the chatter widget)
- **Use `_check_company_auto = True`** for multi-company safety
- **Add `company_id`** to every model that needs multi-company isolation
- **Use `spp.vocabulary.code`** for type/category fields instead of hardcoded selections (this allows configuration through the vocabulary system)
- **Use `tracking=True`** on important fields to log changes in the chatter

## Extending existing models

To add fields to an existing OpenSPP or Odoo model, use `_inherit` without `_name`:

```python
class ResPartnerExtension(models.Model):
    _inherit = "res.partner"

    my_custom_field = fields.Char(string="My Custom Field")
    is_my_feature_enabled = fields.Boolean(default=False)
```

This adds your fields to the existing model's database table. No new table is created.

## Auto-generated sequences

For models that need auto-incrementing reference numbers, define a sequence in `data/ir_sequence.xml`:

```xml
<?xml version="1.0" encoding="utf-8" ?>
<odoo noupdate="1">
    <record id="seq_spp_my_feature" model="ir.sequence">
        <field name="name">My Feature Sequence</field>
        <field name="code">spp.my.feature</field>
        <field name="prefix">MF/%(year)s/</field>
        <field name="padding">5</field>
    </record>
</odoo>
```

Then use it in your model's `create` method:

```python
@api.model_create_multi
def create(self, vals_list):
    for vals in vals_list:
        if vals.get("reference", _("New")) == _("New"):
            vals["reference"] = self.env["ir.sequence"].next_by_code(
                "spp.my.feature"
            ) or _("New")
    return super().create(vals_list)
```
