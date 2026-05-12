---
openspp:
  doc_status: draft
  products: [core]
---

# Testing

**For: developers**

This page covers how to write tests for OpenSPP modules. Tests follow Odoo's testing framework with OpenSPP-specific patterns for role-based access testing and vocabulary data.

## Test file structure

```
spp_my_module/
└── tests/
    ├── __init__.py      # Imports all test modules
    ├── common.py        # Shared setup and helper methods
    ├── test_my_model.py # Tests for spp.my.feature
    └── test_security.py # Access control tests
```

The `__init__.py` imports each test module:

```python
# Part of OpenSPP. See LICENSE file for full copyright and licensing details.
from . import common
from . import test_my_model
from . import test_security
```

## Common test base

Create a `common.py` with shared setup for your module's tests. This avoids duplicating user creation and data setup across test files.

```python
# Part of OpenSPP. See LICENSE file for full copyright and licensing details.
from odoo import Command
from odoo.tests.common import TransactionCase


class MyFeatureTestCommon(TransactionCase):
    """Common test setup for spp_my_module tests."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        # Load vocabulary codes created by module's data files
        cls.feature_type_basic = cls.env.ref(
            "spp_my_module.code_feature_basic"
        )

        # Create test users with different access levels
        base_user_group = cls.env.ref("base.group_user")

        cls.user_viewer = cls.env["res.users"].create({
            "name": "Feature Viewer",
            "login": "feature_viewer",
            "email": "viewer@test.com",
            "group_ids": [
                Command.link(base_user_group.id),
                Command.link(
                    cls.env.ref("spp_my_module.group_myfeature_viewer").id
                ),
            ],
        })

        cls.user_officer = cls.env["res.users"].create({
            "name": "Feature Officer",
            "login": "feature_officer",
            "email": "officer@test.com",
            "group_ids": [
                Command.link(base_user_group.id),
                Command.link(
                    cls.env.ref("spp_my_module.group_myfeature_officer").id
                ),
            ],
        })

        cls.user_manager = cls.env["res.users"].create({
            "name": "Feature Manager",
            "login": "feature_manager",
            "email": "manager@test.com",
            "group_ids": [
                Command.link(base_user_group.id),
                Command.link(
                    cls.env.ref("spp_my_module.group_myfeature_manager").id
                ),
            ],
        })

    def _create_test_feature(self, **kwargs):
        """Create a test feature record with defaults.

        Args:
            **kwargs: Override default field values.

        Returns:
            spp.my.feature: Created record.
        """
        default_vals = {
            "name": "Test Feature",
            "feature_type_id": self.feature_type_basic.id,
        }
        default_vals.update(kwargs)
        return self.env["spp.my.feature"].create(default_vals)
```

### Key patterns

- Use `@classmethod` and `setUpClass` for setup that runs once per test class (faster than `setUp`)
- Always include `base.group_user` when creating test users — many Odoo mixins (like `mail.thread`) require it
- Use `env.ref()` to load data created by your module's XML/CSV data files
- Create helper methods that return records with sensible defaults

## Writing test cases

```python
# Part of OpenSPP. See LICENSE file for full copyright and licensing details.
from odoo.exceptions import AccessError
from odoo.tests import tagged

from .common import MyFeatureTestCommon


@tagged("post_install", "-at_install")
class TestMyFeature(MyFeatureTestCommon):
    """Tests for spp.my.feature model."""

    def test_create_feature_with_defaults(self):
        """Test that creating a feature sets default values."""
        feature = self._create_test_feature()

        self.assertEqual(feature.state, "draft")
        self.assertTrue(feature.reference)
        self.assertNotEqual(feature.reference, "New")

    def test_state_transition_draft_to_active(self):
        """Test activating a draft feature."""
        feature = self._create_test_feature()
        feature.action_activate()

        self.assertEqual(feature.state, "active")

    def test_viewer_cannot_create(self):
        """Test that viewers cannot create records."""
        with self.assertRaises(AccessError):
            self.env["spp.my.feature"].with_user(
                self.user_viewer
            ).create({
                "name": "Unauthorized Feature",
                "feature_type_id": self.feature_type_basic.id,
            })

    def test_officer_can_create(self):
        """Test that officers can create records."""
        feature = self.env["spp.my.feature"].with_user(
            self.user_officer
        ).create({
            "name": "Officer Feature",
            "feature_type_id": self.feature_type_basic.id,
        })

        self.assertTrue(feature.id)

    def test_multi_company_isolation(self):
        """Test that records are isolated by company."""
        feature = self._create_test_feature(
            company_id=self.env.company.id,
        )

        # User in a different company should not see this record
        other_company_user = self.user_viewer.copy({
            "login": "other_company_viewer",
            "company_ids": [
                Command.set([self.env.ref("base.main_company").id])
            ],
        })
        visible = self.env["spp.my.feature"].with_user(
            other_company_user
        ).search([("id", "=", feature.id)])

        self.assertFalse(visible)
```

### Test decorators

```python
@tagged("post_install", "-at_install")
```

This is the standard decorator for OpenSPP tests:

- `post_install` — Run after the module is fully installed (data files loaded, groups created)
- `-at_install` — Do not run during installation

### Testing with different users

Use `with_user()` to execute operations as a specific user:

```python
# This runs as the viewer user
record = self.env["spp.my.feature"].with_user(self.user_viewer).search([])

# This should raise AccessError
with self.assertRaises(AccessError):
    self.env["spp.my.feature"].with_user(self.user_viewer).create({...})
```

### What to test

At minimum, test these for every module:

| Category          | What to verify                                                                       |
| ----------------- | ------------------------------------------------------------------------------------ |
| CRUD              | Create with required fields, read, update, delete                                    |
| State transitions | Each valid transition, and that invalid transitions raise errors                     |
| Access control    | Each role (viewer, officer, manager) can/cannot perform expected actions             |
| Multi-company     | Records are isolated between companies                                               |
| Computed fields   | Computed values are correct and update when dependencies change                      |
| Constraints       | Required fields, unique constraints, and domain validations raise appropriate errors |

## Running tests

```bash
spp test spp_my_module
spp test spp_my_module --tags=post_install
```

See the {doc}`../setup/index` page for more details on the test runner.
