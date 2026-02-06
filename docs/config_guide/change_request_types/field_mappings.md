---
openspp:
  doc_status: draft
  products: [core]
---

# Field mappings

Field mappings define how data from a change request detail model is applied to the target registrant record. This guide covers all mapping options available in OpenSPP.

## Apply strategies

OpenSPP supports three apply strategies:

| Strategy | Description | Use Case |
|----------|-------------|----------|
| Field Mapping | Copies fields from detail to registrant using configured mappings | Most common - simple field updates |
| Custom Method | Executes Python code for complex logic | Adding members, splitting households |
| Manual Application | Requires manual intervention to apply | Complex migrations, bulk corrections |

## Basic mapping

When source and target field names match exactly, use Direct Copy:

| Source Field | Target Field | Transform |
|--------------|--------------|-----------|
| `phone` | `phone` | Direct Copy |
| `email` | `email` | Direct Copy |
| `given_name` | `given_name` | Direct Copy |
| `family_name` | `family_name` | Direct Copy |

```{figure} /_images/en-us/config_guide/change_request_types/11-configured-field-mappings.png
:alt: Field Mappings table showing Direct Copy mappings for the Edit Individual Information type

The **Field Mappings** table with **Source Field**, **Target Field**, and **Transform** columns configured for direct field copying.
```

## Relational field mapping

For Many2one fields, map the ID field:

| Source Field | Target Field | Transform |
|--------------|--------------|-----------|
| `gender_id` | `gender` | Direct Copy |
| `area_id` | `area_id` | Direct Copy |
| `country_id` | `country_id` | Direct Copy |

```{note}
The system automatically handles `.id` extraction for relational fields. You don't need to explicitly reference the ID.
```

## Expression-based mapping

For complex transformations, use expressions. Set the Transform to **Expression** and provide a Python expression.

### Concatenating fields

| Source Field | Target Field | Transform | Expression |
|--------------|--------------|-----------|------------|
| `given_name` | `name` | Expression | `(value or '') + ' ' + (detail.family_name or '')` |

### Calculating values

| Source Field | Target Field | Transform | Expression |
|--------------|--------------|-----------|------------|
| `birthdate` | `age_years` | Expression | `(datetime.now().date() - value).days // 365 if value else 0` |

### Available variables in expressions

| Variable | Description |
|----------|-------------|
| `value` | The source field value |
| `detail` | The entire detail record |
| `registrant` | The target registrant record |
| `datetime` | Python datetime module |
| `date` | Python date module |

```{warning}
Expression-based mappings execute Python code. Only administrators should configure expressions due to arbitrary code execution risk.
```

## Conditional mapping

Only apply a mapping when a condition is met:

| Source Field | Target Field | Transform | Expression |
|--------------|--------------|-----------|------------|
| `is_primary` | `phone` | Expression | `detail.new_phone if value else registrant.phone` |

This example only updates the phone if `is_primary` is true; otherwise, it keeps the existing value.

### More conditional examples

**Update only if not empty:**
```python
value if value else registrant.email
```

**Apply different logic based on type:**
```python
detail.new_phone if detail.phone_type == 'mobile' else registrant.phone
```

**Format before applying:**
```python
value.strip().upper() if value else ''
```

## Custom apply strategies

For complex operations that can't be expressed with field mappings, use a Custom Method:

1. Set **Apply Strategy** to **Custom Method**
2. Set **Apply Model** to the model containing the apply logic
3. Set **Apply Method** to the method name (usually `apply`)

### Available custom strategies

| Model | Purpose |
|-------|---------|
| `spp.cr.apply.add_member` | Add new member to group |
| `spp.cr.apply.remove_member` | Remove member from group |
| `spp.cr.apply.change_hoh` | Change head of household |
| `spp.cr.apply.transfer_member` | Transfer member between groups |
| `spp.cr.apply.exit_registrant` | Deactivate registrant |
| `spp.cr.apply.create_group` | Create new group/household |
| `spp.cr.apply.split_household` | Split household into two |
| `spp.cr.apply.merge_registrants` | Merge duplicate records |

## Manual application

For changes that need human review before application:

1. Set **Apply Strategy** to **Manual**
2. Set **Auto Apply On Approve** to **No**
3. After approval, an administrator manually applies changes

Use cases:
- Complex group restructuring
- Data migrations
- Bulk corrections requiring verification

## Troubleshooting mappings

### Field not updating

**Problem:** Approved change request doesn't update the registrant field.

**Checks:**
- Is the source field name spelled correctly?
- Does the target field exist on `res.partner`?
- Is **Auto Apply On Approve** enabled?
- Check Odoo logs for errors

### Expression errors

**Problem:** Expression mapping throws an error.

**Checks:**
- Test the expression in Odoo shell first
- Ensure all variables are defined
- Handle `None`/`False` values explicitly
- Check for syntax errors

### Relational field issues

**Problem:** Many2one field not being set.

**Checks:**
- Map the field itself, not `.id`
- Ensure the related record exists
- Check access rights to the related model

## See also

- {doc}`creating_types` - Basic configuration steps
- {doc}`patterns` - Common configuration patterns
- {doc}`troubleshooting` - More troubleshooting tips
