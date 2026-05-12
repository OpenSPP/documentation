---
openspp:
  doc_status: draft
  products: [core]
---

# In-kind entitlements

This guide is for **implementers** configuring in-kind (physical goods) entitlements for social protection programs.

## Understanding in-kind entitlements

In-kind entitlements distribute physical goods instead of cash. Common examples:

| Program type | In-kind items |
|--------------|---------------|
| Food assistance | Rice, cooking oil, beans |
| Agricultural support | Seeds, fertilizer, tools |
| School supplies | Books, uniforms, materials |
| Emergency relief | Blankets, tarps, hygiene kits |

## Configuring in-kind entitlements

### Creating an in-kind entitlement manager

1. Open your program's **Configuration** tab
2. In **Entitlement Manager**, click **Add a line**
3. Select **In-Kind** as the manager type
4. Configure the in-kind items

```{figure} /_images/en-us/config_guide/entitlement_formulas/07-inkind-entitlement-manager.png
:alt: In-kind entitlement manager form

The In-Kind entitlement manager form with **Manage Inventory**, **Evaluate Single Item**, and the **Items** list.
```

### In-kind manager settings

| Field | Description |
|-------|-------------|
| **Name** | Display name for this manager |
| **Warehouse** | Source warehouse for inventory |
| **Entitlement Items** | List of products to distribute |

### Adding in-kind items

Each item specifies a product and quantity:

| Field | Description | Example |
|-------|-------------|---------|
| **Product** | Item from product catalog | Rice (25kg bag) |
| **Quantity** | Amount per beneficiary | `1` |
| **Unit of Measure** | How quantity is measured | Bags, kg, pieces |
| **Condition** | Who receives this item | (optional CEL) |

```{figure} /_images/en-us/config_guide/entitlement_formulas/08-inkind-item-configuration.png
:alt: In-kind item configuration with product, quantity, and condition

Configure each item with a **Product**, **Quantity**, **Condition**, and optional **Multiplier** field.
```

## Product configuration

### Setting up products

Products must be configured in the system before use:

1. Go to **Inventory → Products**
2. Create or select a product
3. Configure product details

| Field | Description |
|-------|-------------|
| **Name** | Product display name |
| **Type** | Storable Product (for inventory tracking) |
| **Unit of Measure** | Default measurement unit |
| **Category** | Product categorization |

### Product categories for social protection

Organize products by category:

| Category | Products |
|----------|----------|
| Food Staples | Rice, beans, flour, oil |
| Agricultural Inputs | Seeds, fertilizer, pesticides |
| Household Items | Blankets, cookware, containers |
| Hygiene | Soap, sanitizer, menstrual products |

## Warehouse integration

In-kind entitlements integrate with inventory management:

### Warehouse configuration

| Field | Description |
|-------|-------------|
| **Source Warehouse** | Where products are stored |
| **Service Points** | Distribution locations |

### Inventory tracking

When entitlements are prepared:

1. System checks available stock
2. Reserves inventory for entitlements
3. Reduces stock on distribution
4. Tracks redemption status

```{note}
Ensure sufficient stock exists before preparing entitlements. Low stock warnings appear if inventory is insufficient.
```

## Quantity multipliers

Scale quantities based on beneficiary attributes:

### Per-household-member distribution

| Field | Value |
|-------|-------|
| Product | Rice (1kg) |
| Base Quantity | `1` |
| Multiplier Field | `household_size` |

**Result:** 1kg rice per household member

### Maximum quantities

Set limits on multiplied quantities:

| Field | Value |
|-------|-------|
| Quantity | `1` |
| Multiplier Field | `household_size` |
| Max Multiplier | `10` |

**Result:** Maximum 10kg regardless of household size

## Conditional in-kind items

Different items for different beneficiaries:

### Example: Age-based items

**Item 1: Rice for all**

| Field | Value |
|-------|-------|
| Product | Rice |
| Quantity | 5 |
| Condition | (empty) |

**Item 2: Baby food for households with infants**

| Field | Value |
|-------|-------|
| Product | Baby formula |
| Quantity | 2 |
| Condition | `members.exists(m, age_years(m.birthdate) < 2)` |

### Example: Geographic items

| Field | Value |
|-------|-------|
| Product | Winter blanket |
| Quantity | 2 |
| Condition | `r.area_id.climate_zone == 'cold'` |

## Distribution workflow

### Preparing in-kind entitlements

1. Open the cycle
2. Click **Prepare Entitlements**
3. System calculates items for each beneficiary
4. Draft entitlements are created

### Approving in-kind entitlements

1. Review entitlement list
2. Verify quantities and products
3. Approve entitlements
4. Inventory is reserved

### Distribution/redemption

| Method | Description |
|--------|-------------|
| **Direct distribution** | Items delivered to beneficiaries |
| **Service point redemption** | Beneficiaries collect at designated locations |
| **Voucher exchange** | Vouchers redeemed for products |

## Service points

Configure where beneficiaries collect in-kind items:

| Field | Description |
|-------|-------------|
| **Name** | Service point name |
| **Location** | Physical address |
| **Warehouse** | Associated warehouse |
| **Operating Hours** | When open for distribution |

## Tracking redemption

| State | Description |
|-------|-------------|
| **Draft** | Entitlement created |
| **Approved** | Ready for distribution |
| **Partially Redeemed** | Some items collected |
| **Fully Redeemed** | All items collected |

## Best practices

### Product management

| Practice | Benefit |
|----------|---------|
| Use consistent product names | Clear reporting |
| Set up proper units of measure | Accurate quantities |
| Maintain product categories | Easy organization |

### Inventory planning

| Practice | Benefit |
|----------|---------|
| Check stock before preparing | Avoid shortfalls |
| Plan procurement cycles | Ensure availability |
| Track expiration dates | Prevent waste |

### Distribution efficiency

| Practice | Benefit |
|----------|---------|
| Pre-pack items where possible | Reduce wait times |
| Track redemption rates | Identify issues |

## Are you stuck?

**Products not appearing in selection?**
- Verify products are created in Inventory → Products
- Check product type is "Storable Product"
- Ensure you have access to the product category

**Inventory insufficient warning?**
- Check warehouse stock levels
- Verify correct warehouse is selected
- Plan procurement before preparing entitlements

**Quantities seem wrong?**
- Review multiplier field configuration
- Check max multiplier setting
- Verify beneficiary data has values

## Next steps

- {doc}`conditional_logic` - Complex conditions for items
- {doc}`dynamic_entitlements` - Household-based quantities
- {doc}`/user_guide/programs/manage_entitlements` - Distribution workflow
