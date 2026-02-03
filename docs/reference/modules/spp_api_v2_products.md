---
openspp:
  doc_status: draft
---

# OpenSPP API V2 - Products


## Overview

OpenSPP API V2 - Products extends the core API V2 module with RESTful endpoints for querying products, product categories, and units of measure. This module enables external systems to access the product catalog for in-kind entitlement processing and inventory coordination.

## Purpose

This module is designed to:

- **Expose product catalog:** Provide read access to products used in social protection programs
- **Support in-kind programs:** Enable external systems to reference products for distributions
- **Share category structure:** Allow systems to understand product organization
- **Provide unit standardization:** Expose units of measure for quantity coordination

## Module Dependencies

| Dependency     | Description                                                   |
| -------------- | ------------------------------------------------------------- |
| **spp_api_v2** | Core API V2 module providing authentication and base patterns |
| **product**    | Odoo product management module                                |
| **uom**        | Odoo unit of measure module                                   |

## Key Features

### Product Search

Query products with filtering by category, type, and other criteria. Results include product details needed for external system integration.

### Product Lookup

Retrieve detailed information for a specific product using its code or name as the external identifier.

### Product Categories

List the hierarchical product category structure used to organize the catalog.

### Units of Measure

Access the standard units of measure for quantity coordination across systems.

## API Endpoints

| Endpoint                | Method | Description                             |
| ----------------------- | ------ | --------------------------------------- |
| `/Product`              | GET    | Search products with optional filters   |
| `/Product/{identifier}` | GET    | Read a specific product by code or name |
| `/ProductCategory`      | GET    | List product categories                 |
| `/UnitOfMeasure`        | GET    | List units of measure                   |

### Product Search Parameters

| Parameter | Type    | Description                |
| --------- | ------- | -------------------------- |
| category  | string  | Filter by product category |
| type      | string  | Filter by product type     |
| active    | boolean | Filter by active status    |

### Product Response Fields

| Field       | Type    | Description                 |
| ----------- | ------- | --------------------------- |
| code        | string  | Product code (default_code) |
| name        | string  | Product name                |
| category    | string  | Product category name       |
| type        | string  | Product type                |
| uom         | string  | Default unit of measure     |
| description | string  | Product description         |
| active      | boolean | Whether product is active   |

### Category Response Fields

| Field     | Type   | Description                   |
| --------- | ------ | ----------------------------- |
| name      | string | Category name                 |
| parent    | string | Parent category name (if any) |
| full_path | string | Complete category path        |

### Unit of Measure Response Fields

| Field    | Type    | Description                                  |
| -------- | ------- | -------------------------------------------- |
| name     | string  | Unit name                                    |
| category | string  | Unit category (e.g., Weight, Volume)         |
| uom_type | string  | Reference, bigger, or smaller than reference |
| factor   | decimal | Conversion factor                            |

## Integration

### With Core API V2

This module extends `spp_api_v2` and inherits:

- OAuth 2.0 authentication
- External identifier patterns (uses code or name, not database IDs)
- Standard response formats
- Consistent error handling

### With Odoo Product Module

Product data comes from Odoo's standard `product` module:

- Product templates and variants
- Product categories
- Product attributes

### With Odoo UoM Module

Unit of measure data comes from Odoo's standard `uom` module:

- Unit definitions
- Unit categories
- Conversion factors

### With Entitlements

Products exposed through this API are referenced in:

- In-kind entitlement records
- Distribution planning
- Inventory management

### Auto-Installation

This module auto-installs when both `spp_api_v2` and `product` are present, ensuring product endpoints are available whenever the prerequisites exist.

## Are you stuck?

### Product not found error

**Symptom:** 404 error when requesting a product
**Cause:** Invalid product code/name or product does not exist
**Solution:** Use the product's exact `default_code` or `name` as the identifier

### Empty product search

**Symptom:** Search returns no products
**Cause:** No products match filters or no products defined
**Solution:** Verify products exist in the catalog, adjust filter parameters

### Missing unit of measure

**Symptom:** Product UoM field is empty
**Cause:** Product has no default unit of measure configured
**Solution:** Configure the product's default unit of measure in Odoo

### Category not showing full hierarchy

**Symptom:** Category appears without parent information
**Cause:** Top-level category has no parent
**Solution:** This is expected behavior for root categories
