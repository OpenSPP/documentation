---
openspp:
  doc_status: draft
  products: [core]
---

# Testing CR types

This reference covers test setup patterns, what to test, and common pitfalls when writing tests for custom CR types. For a complete test example, see the test file in the {doc}`tutorial`.

## Test setup pattern

CR tests need a CR type record, test registrants, and group memberships. Create these in `setUpClass` so they are shared across test methods:

```python
from odoo import fields
from odoo.exceptions import UserError, ValidationError
from odoo.tests import TransactionCase


class TestCustomCRType(TransactionCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        Partner = cls.env["res.partner"]
        Membership = cls.env["spp.group.membership"]

        # Create test registrants
        cls.group = Partner.create({
            "name": "Test Household",
            "is_registrant": True,
            "is_group": True,
        })
        cls.individual = Partner.create({
            "name": "Test Person",
            "is_registrant": True,
            "is_group": False,
        })
        cls.membership = Membership.create({
            "group": cls.group.id,
            "individual": cls.individual.id,
            "start_date": fields.Datetime.now(),
        })

        # Look up or create the CR type
        cls.cr_type = cls.env["spp.change.request.type"].search(
            [("code", "=", "your_type_code")], limit=1
        )
        if not cls.cr_type:
            cls.cr_type = cls.env["spp.change.request.type"].create({
                "name": "Your Type",
                "code": "your_type_code",
                "target_type": "group",
                "detail_model": "spp.cr.detail.your_type",
                "apply_strategy": "custom",
                "apply_model": "spp.cr.apply.your_type",
            })
```

**Why look up before creating?** The CR type might already exist from the module's XML data (if the module is installed in the test database). Searching first avoids duplicate code errors.

### Helper method

Add a helper to reduce boilerplate in individual test methods:

```python
    def _create_cr(self, registrant=None, **detail_vals):
        """Create a CR and populate its detail record."""
        cr = self.env["spp.change.request"].create({
            "request_type_id": self.cr_type.id,
            "registrant_id": (registrant or self.group).id,
        })
        if detail_vals:
            cr.get_detail().write(detail_vals)
        return cr
```

## What to test

### Detail model validation

Test that constraints reject invalid data:

```python
def test_constraint_rejects_invalid_input(self):
    cr = self._create_cr()
    detail = cr.get_detail()

    with self.assertRaises(ValidationError):
        detail.write({
            "target_group_id": self.group.id,  # Same as source
        })
```

### Apply strategy: happy path

Test the end state after a successful apply:

```python
def test_successful_apply(self):
    cr = self._create_cr(
        field_a=value_a,
        field_b=value_b,
    )
    cr.approval_state = "approved"
    cr.action_apply()

    # Verify the CR is marked as applied
    self.assertTrue(cr.is_applied)

    # Verify the actual effect on the registrant
    self.assertEqual(self.group.some_field, expected_value)
```

### Apply strategy: error cases

Test each validation in your strategy's `apply()` method:

```python
def test_missing_required_field_raises_error(self):
    cr = self._create_cr()  # Missing a required detail field
    cr.approval_state = "approved"

    with self.assertRaises(UserError):
        cr.action_apply()
```

Create one test per error case. Verify the specific exception type:
- `ValidationError` for constraint violations (detail model)
- `UserError` for strategy validation failures (apply strategy)

### Preview

Test that `preview()` returns the expected structure:

```python
def test_preview_structure(self):
    cr = self._create_cr(
        field_a=value_a,
    )
    preview = cr.action_preview_changes()

    self.assertIn("_action", preview)
    self.assertEqual(preview["_action"], "your_action_name")
```

### Full workflow

Test the complete lifecycle from draft to applied. Note that directly setting `approval_state = "approved"` bypasses the submit/conflict-check path — use this for focused apply tests. For a true end-to-end test, call the submission action:

```python
def test_full_workflow(self):
    cr = self._create_cr(
        field_a=value_a,
        field_b=value_b,
    )

    # Verify initial state
    self.assertEqual(cr.approval_state, "draft")

    # Approve and apply
    cr.approval_state = "approved"
    cr.action_apply()

    # Verify end state
    self.assertTrue(cr.is_applied)
    self.assertTrue(cr.applied_date)
```

## Testing approval hooks

If you override approval hooks, test that your custom logic runs:

```python
def test_on_approve_triggers_custom_logic(self):
    cr = self._create_cr(field_a=value_a)

    # Simulate approval
    cr.approval_state = "approved"

    # Verify your custom side effect occurred
    self.assertTrue(some_side_effect_happened)
```

## Testing conflict detection

Create two CRs that should conflict, then verify the conflict is detected:

```python
def test_conflict_detected_for_same_registrant(self):
    # Create first CR (pending)
    cr1 = self._create_cr(field_a=value_a)
    cr1.approval_state = "pending"

    # Create second CR for the same registrant
    cr2 = self._create_cr(field_a=value_b)

    # Run conflict checks
    result = cr2._run_conflict_checks()

    self.assertTrue(result.get("needs_override") or result.get("has_warning"))
```

This requires conflict rules to be configured for your CR type. Create them in `setUpClass` if they are not part of your module's XML data.

## A note on `sudo()` in tests

Apply strategies run with `sudo()` in production (the CR framework calls them that way). In tests, `action_apply()` also uses `sudo()` internally, so your tests exercise the same code path. You do not need to call `sudo()` explicitly in test code.

If you need to test that non-privileged users cannot bypass the approval workflow, create a test user with limited groups and call actions using `cr.with_user(test_user).action_apply()`.

## Checklist

Use this checklist when writing tests for a custom CR type:

- [ ] Detail model creation succeeds with valid data
- [ ] Each `@api.constrains` raises `ValidationError` for invalid data
- [ ] Apply strategy succeeds with valid, approved CR
- [ ] Apply strategy raises `UserError` for each invalid state (one test per validation)
- [ ] Applied CR has `is_applied = True` and `applied_date` set
- [ ] The registrant is actually modified as expected after apply
- [ ] Preview returns the expected dict structure
- [ ] Each transfer reason / selection value works (if applicable)
- [ ] Conflict detection finds conflicting CRs (if conflict rules are configured)

## Common pitfalls

**Forgetting to set `approval_state = "approved"`** — `action_apply()` only works on approved CRs. If you skip this step, the apply will fail with an unclear error.

**Creating duplicate CR types** — If your module's XML data creates the CR type and your test also creates it, you get a unique constraint error on the `code` field. Always search before creating in `setUpClass`.

**Not creating test data for each test** — Tests that share mutable state (e.g., a membership that gets ended in one test) will interfere with each other. Create fresh records for tests that modify data, or use `TransactionCase` (which rolls back after each test method).

**Testing onchange in unit tests** — `@api.onchange` handlers do not run during `write()` calls in tests. If your test depends on onchange behavior, either call the onchange method directly or test the constraint that backs it up instead.

**Missing vocabulary codes** — Some detail models depend on vocabulary codes (e.g., gender, relationship types) that might not exist in the test database. Use a helper that looks up or creates the vocabulary code:

```python
@classmethod
def _get_or_create_vocab_code(cls, namespace_uri, code, display):
    """Get a vocabulary code, creating it if not found."""
    existing = cls.env["spp.vocabulary.code"].get_code(
        namespace_uri, code
    )
    if existing:
        return existing
    vocab = cls.env["spp.vocabulary"].search(
        [("namespace_uri", "=", namespace_uri)], limit=1
    )
    return cls.env["spp.vocabulary.code"].create({
        "vocabulary_id": vocab.id,
        "code": code,
        "display": display,
        "is_local": True,
    })
```
