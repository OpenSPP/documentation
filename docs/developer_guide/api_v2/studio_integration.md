---
openspp:
  doc_status: draft
  products: [core]
---

# Studio API Integration

This guide is for **developers** integrating with OpenSPP's Studio custom fields via API V2.

## Overview

The `spp_studio_api_v2` module bridges OpenSPP Studio (custom fields and CEL variables) with API V2. It enables:

- **Automatic field exposure** - Studio fields are automatically available via API when marked for exposure
- **Variable discovery** - List available CEL variables and their metadata
- **Variable value retrieval** - Get computed or cached variable values for subjects
- **Data mapping** - Seamless conversion between API camelCase and Odoo snake_case

This module auto-installs when both `spp_api_v2` and `spp_studio` are present.

## Prerequisites

- `spp_api_v2` - Core API V2 module
- `spp_studio` - Studio custom fields module
- `spp_cel_domain` - CEL expression domain module
- API client with `studio:read` scope

For API setup, see {doc}`authentication`.

## Extension URIs

Studio fields are exposed through two API extensions, organized by target registry type:

| Extension | URI | Applies To |
|-----------|-----|------------|
| Studio Individual Fields | `urn:openspp:extension:studio-individual` | Individual registrants |
| Studio Group Fields | `urn:openspp:extension:studio-group` | Group/Household registrants |

When requesting Individual or Group resources, include these extensions via the `_extensions` parameter:

```text
GET /api/v2/spp/Individual/{identifier}?_extensions=studio-individual
```

## Exposing Studio Fields to API

### Automatic Registration

When a Studio field is created and activated with the **Expose via API** option enabled, it automatically registers with the appropriate extension (individual or group).

| Studio Setting | Default | Description |
|----------------|---------|-------------|
| Expose via API | `True` | Include field in API responses and allow updates |

### Manual Registration

For existing fields or migration scenarios, use the registration helper:

```python
# Register all existing active fields with api_exposed=True
env["spp.studio.field"]._register_existing_fields()
```

### Field Lifecycle

| Event | API Behavior |
|-------|--------------|
| Field activated with `api_exposed=True` | Registered in extension |
| Field deactivated | Unregistered from extension |
| `api_exposed` changed to `False` | Unregistered from extension |
| `api_exposed` changed to `True` | Registered in extension |

## Studio API Endpoints

### List Studio Fields

Retrieve metadata about all active Studio custom fields.

```text
GET /api/v2/spp/Studio/fields
Authorization: Bearer {token}
```

**Query Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `target_type` | string | Filter by registry type: `individual` or `group` |
| `api_exposed_only` | boolean | Only return API-exposed fields (default: `true`) |
| `_count` | integer | Page size, 1-500 (default: 100) |
| `_lastId` | integer | Cursor for pagination |

**Response:**

```json
{
  "total": 5,
  "items": [
    {
      "technicalName": "x_farm_size",
      "label": "Farm Size",
      "fieldType": "decimal",
      "targetType": "individual",
      "helpText": "Total farm area in hectares",
      "isRequired": false,
      "placementZone": "basic_info",
      "apiExposed": true,
      "isReadonly": false,
      "isSearchable": true,
      "sequence": 10,
      "selectionOptions": null,
      "visibilityField": null,
      "visibilityOperator": null,
      "visibilityValue": null,
      "linkModel": null,
      "linkDomain": null
    },
    {
      "technicalName": "x_primary_crop",
      "label": "Primary Crop",
      "fieldType": "selection",
      "targetType": "individual",
      "selectionOptions": [
        {"value": "rice", "label": "Rice"},
        {"value": "corn", "label": "Corn"},
        {"value": "vegetables", "label": "Vegetables"}
      ]
    }
  ],
  "nextPageId": 42
}
```

### Get Field Schema

Retrieve JSON Schema validation rules for a specific field.

```text
GET /api/v2/spp/Studio/fields/{technical_name}/schema
Authorization: Bearer {token}
```

**Response:**

```json
{
  "technicalName": "x_farm_size",
  "type": "number",
  "description": "Total farm area in hectares",
  "required": false,
  "minimum": 0
}
```

**Schema Type Mapping:**

| Studio Field Type | JSON Schema Type | Additional Properties |
|-------------------|------------------|----------------------|
| `text` | `string` | `maxLength: 255` |
| `long_text` | `string` | `maxLength: 65535` |
| `integer` | `number` | `minimum: 0` |
| `decimal` | `number` | - |
| `date` | `string` | `format: date` |
| `datetime` | `string` | `format: date-time` |
| `boolean` | `boolean` | - |
| `selection` | `string` | `enum`, `enumDisplay` |
| `multi_select` | `array` | `enum`, `enumDisplay` |
| `link` | `object` | `format: reference`, `linkModel`, `linkDomain` |

### List Variables

Retrieve metadata about available CEL variables.

```text
GET /api/v2/spp/Studio/variables
Authorization: Bearer {token}
```

**Query Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `applies_to` | string | Filter: `individual`, `group`, or `both` |
| `source_type` | string | Filter by source type (e.g., `field`, `computed`, `aggregate`) |
| `category` | string | Filter by category name (case-insensitive) |
| `_count` | integer | Page size, 1-500 (default: 100) |
| `_lastId` | integer | Cursor for pagination |

**Response:**

```json
{
  "total": 12,
  "items": [
    {
      "name": "household_income",
      "label": "Household Income",
      "description": "Total monthly household income",
      "valueType": "number",
      "sourceType": "computed",
      "appliesTo": "group",
      "periodGranularity": "monthly",
      "supportsHistorical": true,
      "unit": "PHP",
      "category": "Economic"
    }
  ],
  "nextPageId": 15
}
```

### Get Subject Variables

Retrieve cached variable values for a specific Individual or Group.

```text
GET /api/v2/spp/Studio/variables/{resource_type}/{identifier}
Authorization: Bearer {token}
```

**Path Parameters:**

| Parameter | Description |
|-----------|-------------|
| `resource_type` | `Individual` or `Group` |
| `identifier` | External identifier in format `{system}\|{value}` |

**Query Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `variables` | string | Comma-separated variable names, or `*` for all (default: `*`) |
| `period_key` | string | Period key: `current`, `2024-12`, etc. (default: `current`) |

**Example:**

```text
GET /api/v2/spp/Studio/variables/Individual/urn:gov:ph:psa:national-id|PH-123456789?variables=household_income,children_count&period_key=current
```

**Response:**

```json
{
  "subjectId": "urn:gov:ph:psa:national-id|PH-123456789",
  "periodKey": "current",
  "variables": {
    "household_income": {
      "value": 15000.00,
      "periodKey": "current",
      "recordedAt": "2024-11-28T10:30:00",
      "isStale": false,
      "sourceType": "computed"
    },
    "children_count": {
      "value": 3,
      "periodKey": "current",
      "recordedAt": "2024-11-28T10:30:00",
      "isStale": false,
      "sourceType": "aggregate"
    }
  }
}
```

## Data Mapping

### API to Odoo Field Name Conversion

The API uses camelCase names while Odoo uses snake_case with an `x_` prefix for custom fields.

| API Name | Odoo Field Name |
|----------|-----------------|
| `farmSize` | `x_farm_size` |
| `primaryCrop` | `x_primary_crop_id` |
| `householdIncome` | `x_household_income` |
| `landOwnership` | `x_land_ownership` |

**Conversion rules:**

1. Remove `x_` prefix
2. Remove `_id` suffix (for Many2one fields)
3. Convert snake_case to camelCase

### CodeableConcept Mapping

Many2one fields pointing to vocabulary codes use the CodeableConcept format:

**API Format (Request/Response):**

```json
{
  "primaryCrop": {
    "coding": [
      {
        "system": "urn:openspp:vocab:crops",
        "code": "rice",
        "display": "Rice"
      }
    ]
  }
}
```

**Odoo Field:**

```python
x_primary_crop_id = Many2one("spp.vocabulary.code")
```

### Writing Extension Data

When creating or updating records via API, include extension data in the `extension` object:

```text
{
  "resourceType": "Individual",
  "identifier": [...],
  "name": {...},
  "extension": {
    "studio-individual": {
      "farmSize": 2.5,
      "primaryCrop": {
        "coding": [
          {
            "system": "urn:openspp:vocab:crops",
            "code": "rice"
          }
        ]
      },
      "landOwnership": "owned"
    }
  }
}
```

## Code Examples

### Python: List Studio Fields

```python
import requests

BASE_URL = "https://api.openspp.org/api/v2/spp"
TOKEN = "your_access_token"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

# List all individual fields
response = requests.get(
    f"{BASE_URL}/Studio/fields",
    headers=headers,
    params={"target_type": "individual"}
)

fields = response.json()
for field in fields["items"]:
    print(f"{field['technicalName']}: {field['label']} ({field['fieldType']})")
```

### Python: Get Variable Values

```python
# Get specific variable values for an individual
response = requests.get(
    f"{BASE_URL}/Studio/variables/Individual/urn:gov:ph:psa:national-id|PH-123456789",
    headers=headers,
    params={
        "variables": "household_income,children_count",
        "period_key": "current"
    }
)

data = response.json()
for var_name, var_info in data["variables"].items():
    print(f"{var_name}: {var_info['value']}")
    if var_info["isStale"]:
        print("  (Warning: Value may be outdated)")
```

### curl: List Variables by Category

```bash
curl -X GET \
  "https://api.openspp.org/api/v2/spp/Studio/variables?category=Economic&applies_to=group" \
  -H "Authorization: Bearer ${TOKEN}" \
  -H "Content-Type: application/json"
```

### curl: Create Individual with Studio Fields

```bash
curl -X POST \
  "https://api.openspp.org/api/v2/spp/Individual" \
  -H "Authorization: Bearer ${TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{
    "resourceType": "Individual",
    "identifier": [
      {
        "system": "urn:gov:ph:psa:national-id",
        "value": "PH-NEW-001"
      }
    ],
    "name": {
      "given": "Maria",
      "family": "Santos"
    },
    "extension": {
      "studio-individual": {
        "farmSize": 2.5,
        "primaryCrop": {
          "coding": [{"system": "urn:openspp:vocab:crops", "code": "rice"}]
        }
      }
    }
  }'
```

## Security Considerations

### Required Scope

All Studio endpoints require the `studio:read` scope. Without it, requests return `403 Forbidden`:

```json
{
  "detail": "Missing required scope 'studio:read'. Request access from your administrator."
}
```

### Blocked Models

For security, certain models are blocked from lookup operations:

| Blocked Model | Reason |
|---------------|--------|
| `res.users` | User credentials |
| `ir.config_parameter` | System configuration |
| `spp.api.client` | API client secrets |
| `ir.cron` | Scheduled actions |
| `ir.mail_server` | Mail server credentials |

### Safe Lookup Models

Display name lookups are only permitted on safe reference models:

| Safe Model | Use Case |
|------------|----------|
| `spp.vocabulary.code` | Vocabulary code references |
| `spp.vocabulary` | Vocabulary lookups |
| `res.country` | Country references |
| `res.country.state` | State/Province references |
| `res.partner.category` | Partner category references |

### Variable Computation Restrictions

On-demand variable computation is restricted to safe source models:

- `res.partner`
- `spp.program.membership`
- `spp.entitlement`

## Are you stuck?

### Field not appearing in API response

**Symptom:** A Studio field exists but is not returned by `/Studio/fields`.

**Cause:** The field may not be active or not marked for API exposure.

**Solution:**

1. Verify the field is in `active` state (not `draft` or `inactive`)
2. Check that **Expose via API** is enabled on the field
3. Verify the target type matches your query (individual vs group)

### 403 Forbidden on Studio endpoints

**Symptom:** All Studio endpoint requests return 403.

**Cause:** Your API client lacks the `studio:read` scope.

**Solution:** Contact your administrator to add the `studio:read` scope to your API client configuration.

### Variable value shows as stale

**Symptom:** `isStale: true` in variable response.

**Cause:** The cached value has expired but has not been recomputed.

**Solution:** Variable values are recomputed on a schedule. Either:

1. Wait for the next computation cycle
2. Request an on-demand recomputation (if your client has appropriate permissions)
3. Use the raw field data instead of cached variables for time-sensitive operations

### Extension data not being saved

**Symptom:** PUT/POST requests with extension data succeed but fields are not updated.

**Cause:** The extension key or field name may be incorrect.

**Solution:**

1. Use the correct extension key: `studio-individual` or `studio-group`
2. Verify field names use camelCase (e.g., `farmSize` not `farm_size` or `x_farm_size`)
3. For CodeableConcept fields, ensure the `coding` array includes valid `system` and `code` values

### Pagination not working correctly

**Symptom:** Same results returned regardless of `_lastId` parameter.

**Cause:** Using ID value from wrong response field.

**Solution:** Use the `nextPageId` value from the response, not individual item IDs:

```python
# First page
response = requests.get(f"{BASE_URL}/Studio/fields", headers=headers)
data = response.json()

# Next page - use nextPageId
if data["nextPageId"]:
    response = requests.get(
        f"{BASE_URL}/Studio/fields",
        headers=headers,
        params={"_lastId": data["nextPageId"]}
    )
```

## See Also

- {doc}`overview` - API V2 design principles
- {doc}`authentication` - OAuth 2.0 setup and scopes
- {doc}`resources` - Individual and Group resource operations
- {doc}`external_identifiers` - Identifier format and usage
