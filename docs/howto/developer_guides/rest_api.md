# Extend API v2 (REST)

This guide explains how to extend API v2 by exposing module-specific fields through the **API Extensions** mechanism in `spp_api_v2`.

## Prerequisites

- Knowledge of Python, Odoo, XML, Xpaths.
- To set up OpenSPP for development, see {doc}`development_setup`.

## Install API v2

1. Log into OpenSPP with administrative rights.

2. Access the “Apps” menu from the dashboard to manage OpenSPP modules.

3. Choose “Update Apps List” to refresh the module list.

4. Search for “OpenSPP API V2” (`spp_api_v2`) and install it.

Once installed:

- API base URL is `/api/v2/spp`
- Capability statement is `/api/v2/spp/metadata`
- OpenAPI schema is `/api/v2/spp/openapi.json`

## Extend API v2 with an API Extension

API Extensions allow modules to expose extra fields on `Individual` and/or `Group` resources without changing the core schemas.

At runtime, clients request extensions using the `_extensions` query parameter (for example `_extensions=farmer`).

### Step 1: Create (or reuse) fields

Extensions expose existing Odoo fields. If your module needs new data, add fields to the underlying model (typically `res.partner` for registry data).

For custom fields created by Studio, the field names typically start with `x_...`.

### Step 2: Register the extension (XML data)

In your custom module:

- Add dependency on `spp_api_v2`
- Create a `spp.api.extension` record referencing the fields you want to expose

Example `__manifest__.py` dependency:

```python
"depends": [
    "spp_api_v2",
],
```

Example XML data to register an extension:

```xml
<record id="api_extension_farmer" model="spp.api.extension">
    <field name="name">Farmer</field>
    <field name="url">urn:openspp:extension:farmer</field>
    <field name="module_id" ref="base.module_your_module"/>
    <field name="applies_to">individual</field>
    <field name="field_ids" eval="[(6, 0, [
        ref('your_module.field_res_partner__x_farm_size'),
        ref('your_module.field_res_partner__x_primary_crop_id')
    ])]"/>
</record>
```

### Step 3: Request the extension in API calls

Example:

```bash
curl "http://localhost:8069/api/v2/spp/Individual/<system>%7C<value>?_extensions=farmer" \
  -H "Authorization: Bearer <access_token>"
```

The server includes an `extension` object in the response when data exists for the requested fields.

## Next steps

- For the full API reference, see {doc}`API v2 <../../technical_reference/api_v2/index>`.
- To manage extension registrations in the UI, use **Registry → Configuration → API V2 → API Extensions**.

## About older REST API modules

Older deployments may include REST API modules unrelated to API v2 (for example path-driven APIs which require `request_id` parameters). Those are not covered by this guide.
