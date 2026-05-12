---
openspp:
  doc_status: draft
  products: [core]
---

# Products and Service Points

**For: developers**

Work with the product catalog (entitlement items) and service points (distribution locations) through the API.

## Overview

These extension modules expose reference data used in program distribution:

- **Products** (`spp_api_v2_products`) — Product catalog for in-kind distributions, with categories and units of measure
- **Service Points** (`spp_api_v2_service_points`) — Physical locations where beneficiaries collect benefits

Both provide read-only search access. Products and service points are managed through the OpenSPP admin interface.

## Prerequisites

- Install `spp_api_v2_products` and/or `spp_api_v2_service_points` modules
- API client with `product:read` and/or `service_point:read` scope

## Product Endpoints

### Read Product

```text
GET /api/v2/spp/Product/{identifier}
Authorization: Bearer TOKEN
```

The identifier is the product SKU (`default_code`) or name (URL-encoded).

### Search Products

```text
GET /api/v2/spp/Product?name=rice&category=food
Authorization: Bearer TOKEN
```

**Query parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `name` | string | Product name (substring search) |
| `code` | string | Product SKU/code |
| `category` | string | Category name |
| `_lastUpdated` | date | Modified since (with prefix) |
| `_count` | integer | Results per page (1-100, default 20) |
| `_offset` | integer | Skip N results (default 0) |

**Example: Python**

```python
def search_products(token, base_url, name=None, category=None):
    """Search the product catalog."""
    headers = {"Authorization": f"Bearer {token}"}
    params = {}
    if name:
        params["name"] = name
    if category:
        params["category"] = category

    response = requests.get(
        f"{base_url}/Product",
        headers=headers,
        params=params
    )
    response.raise_for_status()
    return response.json()

# Find food products
result = search_products(token=token, base_url=base_url, category="food")
```

### Product Categories

```text
GET /api/v2/spp/ProductCategory
GET /api/v2/spp/ProductCategory/{identifier}
Authorization: Bearer TOKEN
```

**Search parameters:** `name` (substring), `_count`, `_offset`

### Units of Measure

```text
GET /api/v2/spp/UnitOfMeasure
GET /api/v2/spp/UnitOfMeasure/{identifier}
Authorization: Bearer TOKEN
```

**Search parameters:** `name`, `category`, `_count`, `_offset`

## Service Point Endpoints

### Read Service Point

```text
GET /api/v2/spp/ServicePoint/{identifier}
Authorization: Bearer TOKEN
```

The identifier is the service point name (URL-encoded).

**Response:**

```json
{
  "name": "Manila Distribution Center",
  "description": "Main distribution point for Metro Manila",
  "area": "Metro Manila",
  "country": "PH",
  "coordinates": {
    "latitude": 14.5995,
    "longitude": 120.9842
  },
  "contractActive": true,
  "meta": {
    "versionId": "3",
    "lastUpdated": "2024-06-15T08:00:00Z"
  }
}
```

### Search Service Points

```text
GET /api/v2/spp/ServicePoint?area=Metro+Manila&contractActive=true
Authorization: Bearer TOKEN
```

**Query parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `name` | string | Name (substring search) |
| `area` | string | Geographic area |
| `country` | string | Country code (e.g., `PH`) |
| `contractActive` | boolean | Only active service points |
| `_lastUpdated` | date | Modified since (with prefix) |
| `_count` | integer | Results per page (1-100, default 20) |
| `_offset` | integer | Skip N results (default 0) |

**Example: Python**

```python
def find_active_service_points(area, token, base_url):
    """Find active service points in an area."""
    headers = {"Authorization": f"Bearer {token}"}
    params = {"area": area, "contractActive": True}

    response = requests.get(
        f"{base_url}/ServicePoint",
        headers=headers,
        params=params
    )
    response.raise_for_status()
    return response.json()

# Find active service points in Metro Manila
result = find_active_service_points("Metro Manila", token=token, base_url=base_url)
```

## Common mistakes

**Getting 404 on product/service point endpoints?**

The extension module may not be installed. Check `GET /metadata` to see available resources.

**Product search returns no results?**

Product search uses substring matching on the name. Try a shorter search term. Use `code` for exact SKU lookup.

**Service point coordinates missing?**

Not all service points have GPS coordinates. Coordinates are optional and depend on data entry.

## What's next

- {doc}`entitlements_cycles` - Entitlements reference products for in-kind distributions
- {doc}`resources` - Core API resources
- {doc}`search` - Search and filtering patterns

## See also

- {doc}`overview` - API V2 design principles
- {doc}`authentication` - OAuth 2.0 setup and scopes
