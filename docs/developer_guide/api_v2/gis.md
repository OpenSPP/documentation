---
openspp:
  doc_status: draft
  products: [core]
---

# GIS and Geospatial

This guide is for **developers** working with geospatial queries, geofences, and map data through the OpenSPP API V2 GIS extension.

## Overview

The GIS API (`spp_api_v2_gis`) provides spatial analysis capabilities:

- **Spatial queries** — Count and aggregate registrants within polygons
- **Proximity queries** — Find registrants within a radius of points
- **Geofences** — Save and manage areas of interest
- **Statistics discovery** — Browse available GIS indicators
- **OGC API Features** — Standards-compliant feature access for QGIS and other GIS tools
- **Export** — Download layers as GeoPackage for offline use

Spatial computations use PostGIS for efficient processing.

## Prerequisites

- Install `spp_api_v2_gis` module
- PostGIS extension enabled on the database
- API client with appropriate scopes:

| Scope | Permissions |
|-------|------------|
| `gis:read` | Spatial queries, statistics, OGC, export |
| `statistics:read` | Alternative scope for query/statistics endpoints |
| `gis:geofence` | Create and delete geofences |

## Spatial Queries

### Query Statistics Within a Polygon

```http
POST /api/v2/spp/gis/query/statistics
Authorization: Bearer TOKEN
Content-Type: application/json

{
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [120.95, 14.55],
        [121.05, 14.55],
        [121.05, 14.65],
        [120.95, 14.65],
        [120.95, 14.55]
      ]
    ]
  },
  "filters": {
    "program": "4Ps"
  },
  "variables": ["gender", "poverty_score", "age"]
}
```

**Response:**

```json
{
  "total_count": 2500,
  "statistics": {
    "poverty_score": {"mean": 0.65, "min": 0.1, "max": 0.98},
    "age": {"mean": 35.2, "min": 18, "max": 82}
  },
  "by_dimension": {
    "gender": {
      "F": 1350,
      "M": 1150
    }
  }
}
```

### Batch Spatial Query

Query statistics for multiple polygons at once.

```http
POST /api/v2/spp/gis/query/statistics/batch
Authorization: Bearer TOKEN
Content-Type: application/json

{
  "geometries": [
    {"id": "district_1", "geometry": {"type": "Polygon", "coordinates": [[...]]}},
    {"id": "district_2", "geometry": {"type": "Polygon", "coordinates": [[...]]}}
  ],
  "filters": {"program": "4Ps"},
  "variables": ["gender"]
}
```

**Response:**

```json
{
  "per_geometry": [
    {"id": "district_1", "total_count": 1200, "statistics": {}, "by_dimension": {}},
    {"id": "district_2", "total_count": 800, "statistics": {}, "by_dimension": {}}
  ],
  "summary": {
    "total_unique_count": 1950
  }
}
```

The `summary.total_unique_count` is deduplicated — registrants in overlapping zones are counted once.

### Proximity Query

Find registrants within a radius of reference points.

```http
POST /api/v2/spp/gis/query/proximity
Authorization: Bearer TOKEN
Content-Type: application/json

{
  "reference_points": [
    {"latitude": 14.5995, "longitude": 120.9842}
  ],
  "radius_km": 5,
  "relation": "within",
  "filters": {},
  "variables": ["poverty_score"]
}
```

**Relation options:** `"within"` (inside radius) or `"beyond"` (outside radius).

## Geofences

Save areas of interest for reuse.

### Create Geofence

```http
POST /api/v2/spp/gis/geofences
Authorization: Bearer TOKEN
Content-Type: application/json

{
  "name": "Flood Zone A",
  "geofence_type": "hazard_zone",
  "geometry": {
    "type": "Polygon",
    "coordinates": [[...]]
  },
  "description": "Flood-prone area in Metro Manila",
  "incident_code": "FLOOD-2024-001"
}
```

**Geofence types:** `hazard_zone`, `service_area`, `targeting_area`, `custom`

**Response (201 Created):**

```json
{
  "id": 15,
  "name": "Flood Zone A",
  "geofence_type": "hazard_zone",
  "area_sqkm": 12.5,
  "active": true
}
```

### List Geofences

```http
GET /api/v2/spp/gis/geofences?geofence_type=hazard_zone&active=true
Authorization: Bearer TOKEN
```

**Query parameters:** `geofence_type`, `incident_id`, `active`, `_count`, `_offset`

### Get Geofence

```http
GET /api/v2/spp/gis/geofences/{geofence_id}
Authorization: Bearer TOKEN
```

Returns full GeoJSON Feature with geometry and properties.

### Delete Geofence

```http
DELETE /api/v2/spp/gis/geofences/{geofence_id}
Authorization: Bearer TOKEN
```

Returns 204 No Content (soft delete/archive).

## Statistics Discovery

Browse available GIS indicators grouped by category.

```http
GET /api/v2/spp/gis/statistics
Authorization: Bearer TOKEN
```

**Response:**

```json
[
  {
    "code": "health",
    "name": "Health Indicators",
    "icon": "health.png",
    "statistics": [
      {
        "name": "malnutrition_rate",
        "label": "Malnutrition Rate (%)",
        "unit": "%",
        "format": "0.0"
      }
    ]
  }
]
```

Use these statistic names in the `variables` field of spatial queries.

## OGC API Features

Standards-compliant feature access for GIS tools like QGIS.

### Landing Page

```http
GET /api/v2/spp/gis/ogc
Authorization: Bearer TOKEN
```

### Collections

```http
GET /api/v2/spp/gis/ogc/collections
Authorization: Bearer TOKEN
```

Lists all available feature collections (derived from GIS reports and data layers).

### Get Features

```http
GET /api/v2/spp/gis/ogc/collections/{collection_id}/items?limit=1000&bbox=120.9,14.5,121.1,14.7
Authorization: Bearer TOKEN
```

**Query parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `limit` | integer | Max features (1-10000, default 1000) |
| `offset` | integer | Skip N features (default 0) |
| `bbox` | string | Bounding box filter: `west,south,east,north` |

**Response:** GeoJSON FeatureCollection with `Content-Type: application/geo+json`.

### Get Single Feature

```http
GET /api/v2/spp/gis/ogc/collections/{collection_id}/items/{feature_id}
Authorization: Bearer TOKEN
```

### QGIS Styling

Get a QGIS style file (QML) for a collection.

```http
GET /api/v2/spp/gis/ogc/collections/{collection_id}/qml?field_name=poverty_score&opacity=0.7
Authorization: Bearer TOKEN
```

Returns XML style file. Available for report-based collections only.

## Export

Download layers as GeoPackage or ZIP of GeoJSON for offline use.

```http
GET /api/v2/spp/gis/export/geopackage?layer_ids=health,poverty&include_geofences=true&admin_level=2
Authorization: Bearer TOKEN
```

**Query parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `layer_ids` | string | Comma-separated report codes (all if omitted) |
| `include_geofences` | boolean | Include user's geofences (default: true) |
| `admin_level` | integer | Filter by admin level (e.g., 2 for districts) |

**Response:** Binary file download (GeoPackage `.gpkg` or ZIP of GeoJSON files).

## Example: Python

```python
import requests

class GISClient:
    """Client for GIS spatial queries."""

    def __init__(self, base_url, token):
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def query_polygon(self, polygon_coords, filters=None, variables=None):
        """Query registrant statistics within a polygon."""
        body = {
            "geometry": {
                "type": "Polygon",
                "coordinates": [polygon_coords]
            },
            "filters": filters or {},
            "variables": variables or []
        }
        resp = requests.post(
            f"{self.base_url}/gis/query/statistics",
            headers=self.headers,
            json=body
        )
        resp.raise_for_status()
        return resp.json()

    def create_geofence(self, name, geofence_type, polygon_coords, description=None):
        """Save a polygon as a geofence."""
        body = {
            "name": name,
            "geofence_type": geofence_type,
            "geometry": {
                "type": "Polygon",
                "coordinates": [polygon_coords]
            }
        }
        if description:
            body["description"] = description
        resp = requests.post(
            f"{self.base_url}/gis/geofences",
            headers=self.headers,
            json=body
        )
        resp.raise_for_status()
        return resp.json()

# Usage
gis = GISClient(base_url=base_url, token=token)

# Query a rectangular area
manila_bbox = [
    [120.95, 14.55], [121.05, 14.55],
    [121.05, 14.65], [120.95, 14.65],
    [120.95, 14.55]  # Close the polygon
]
result = gis.query_polygon(
    polygon_coords=manila_bbox,
    filters={"program": "4Ps"},
    variables=["gender", "age"]
)
print(f"Found {result['total_count']} beneficiaries in area")

# Save as geofence for reuse
geofence = gis.create_geofence(
    name="Manila Target Area",
    geofence_type="targeting_area",
    polygon_coords=manila_bbox,
    description="CCT targeting zone for Metro Manila"
)
print(f"Created geofence: {geofence['name']} ({geofence['area_sqkm']} sq km)")
```

## Are You Stuck?

**Spatial query returns zero results?**

Check that registrants have GPS coordinates (`latitude`/`longitude` fields). Not all registrants have location data.

**Getting "PostGIS extension not found"?**

The database needs PostGIS enabled. Contact your system administrator.

**OGC collections list is empty?**

Collections are derived from GIS reports. Verify that GIS reports are configured in the OpenSPP admin.

**GeoPackage export fails?**

GeoPackage format requires the `fiona` Python library. If unavailable, the API falls back to ZIP of GeoJSON files.

**How do I use this with QGIS?**

Use the OGC API endpoints as a WFS data source in QGIS. The QML endpoint provides automatic layer styling.

## Next Steps

- {doc}`simulation` - Simulation scenarios use spatial data
- {doc}`resources` - Core API resources
- {doc}`data_api` - Variable data used in spatial queries

## See Also

- {doc}`overview` - API V2 design principles
- {doc}`authentication` - OAuth 2.0 setup and scopes
