---
openspp:
  doc_status: draft
  products: [core]
---

# Geographic targeting

This guide is for **implementers** configuring area-based eligibility to target registrants in specific administrative areas.

## What is geographic targeting?

Geographic targeting restricts program eligibility to registrants in specific administrative areas (regions, districts, villages, etc.). It's often combined with demographic criteria.

**Example use cases:**

| Scenario | Geographic targeting |
|----------|---------------------|
| Regional pilot program | Target 3 pilot districts |
| Disaster response | Target affected areas only |
| Urban poverty program | Target urban municipalities |
| Phased rollout | Start with accessible areas |

## How it works

The Eligibility Manager has a **Target Areas** section where you select administrative areas:

```{image} /_images/en-us/config_guide/eligibility/06-geographic-targeting-section.png
:alt: Target Areas section in eligibility manager
:class: img-fluid
```

When geographic targeting is configured:

1. Registrants must be in one of the selected areas **AND**
2. Registrants must match the CEL expression (if defined)

```{mermaid}
graph TD
    R[Registrant] --> A{In target area?}
    A --> |Yes| C{Matches CEL?}
    A --> |No| N[Not Eligible]
    C --> |Yes| E[Eligible]
    C --> |No| N
```

## Configuring target areas

### Step 1: Open the eligibility manager

1. Go to **Programs → Programs**
2. Open your program
3. Click the **Configuration** tab
4. Find the **Eligibility Manager** section
5. Click the gear icon to open manager settings

### Step 2: Select target areas

In the **Target Areas** field:

1. Click the field to open the area selector
2. Search or browse for areas
3. Select one or more areas
4. Areas can be at any level (region, district, village)

```{image} /_images/en-us/config_guide/eligibility/07-area-selection-dropdown.png
:alt: Area selection dropdown with search
:class: img-fluid
```

### Step 3: Save configuration

Click **Save** to apply the geographic targeting.

## Area hierarchy

Administrative areas in OpenSPP form a hierarchy:

```
Country
└── Region
    └── District
        └── Sub-district
            └── Village
```

When you select an area:

| Selection | Who is included |
|-----------|-----------------|
| Region only | Registrants in that region (all districts) |
| District only | Registrants in that district only |
| Multiple areas | Registrants in any selected area |

```{note}
Child areas are **not** automatically included. If you select "Region A", only registrants with `area_id` set to "Region A" match—not those in districts within Region A. Select all relevant areas explicitly.
```

## Combining with CEL expressions

Geographic targeting works alongside CEL expressions:

| Configuration | Result |
|--------------|--------|
| Areas only | All registrants in selected areas |
| CEL only | All registrants matching the expression |
| Areas + CEL | Registrants in areas **AND** matching CEL |

### Example: Elderly in pilot districts

To target senior citizens (65+) in three pilot districts:

1. **CEL Expression:** `age_years(r.birthdate) >= 65`
2. **Target Areas:** Select the three pilot districts

Both conditions must be true for eligibility.

### Using area in CEL expressions

You can also reference area in CEL expressions:

```cel
# Registrants in a specific area (by area code)
r.area_id.code == "DISTRICT_01"

# Registrants in urban areas (if area type is tracked)
r.area_id.area_type == "urban"
```

However, using the **Target Areas** field is preferred for:

- Easier configuration (point-and-click)
- Clear audit trail
- Simpler expression maintenance

## Best practices

### Do: Be explicit about area levels

Select areas at the appropriate level. If you want all districts in a region, select each district individually.

### Do: Document your targeting rationale

Record why specific areas were selected (e.g., "Pilot phase 1 districts" or "Flood-affected areas 2024").

### Don't: Mix area methods

Choose one approach:

- Use **Target Areas** field for straightforward area targeting
- Use CEL expressions only if you need dynamic area logic

Mixing both can create confusion.

### Don't: Forget to update areas

When program scope changes (e.g., expansion to new areas), update the target areas configuration.

## Viewing targeted areas

To see which areas are configured:

1. Open the program's **Configuration** tab
2. Find the **Eligibility Manager** section
3. Look for the **Target Areas** field

```{image} /_images/en-us/config_guide/eligibility/08-configured-target-areas.png
:alt: Configured target areas showing selected districts
:class: img-fluid
```

## Are you stuck?

**Registrants in the area aren't matching?**
- Verify the registrant's `area_id` is set correctly
- Check you selected the correct area level (district vs region)
- Ensure the area names match exactly

**Need to target by area type (urban/rural)?**
- Use a CEL expression: `r.area_id.area_type == "urban"`
- Or create separate programs for urban vs rural

**Want to include all sub-areas?**
- Select each sub-area individually in the Target Areas field
- Or use CEL: `r.area_id.parent_id.code == "REGION_01"`

## Next steps

- {doc}`cel_expressions` - Add demographic criteria to area targeting
- {doc}`testing` - Verify your geographic targeting works correctly
- {doc}`advanced` - Use multiple eligibility managers for complex targeting
