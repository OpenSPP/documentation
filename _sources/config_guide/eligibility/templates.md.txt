---
openspp:
  doc_status: draft
  products: [core]
---

# Expression templates

This guide is for **implementers** using and creating CEL expression templates for common eligibility criteria.

## What are templates?

Templates are pre-built CEL expressions for common eligibility scenarios. They provide:

- **Quick start** - Select a template instead of writing from scratch
- **Consistency** - Standard expressions across programs
- **Governance** - Locked templates for compliance requirements

## Available templates

OpenSPP includes templates for common social protection criteria:

### Individual-based templates

| Template | Expression | Use case |
|----------|------------|----------|
| Senior Citizens (65+) | `age_years(r.birthdate) >= 65` | Old age pension |
| Adults (18+) | `age_years(r.birthdate) >= 18` | Adult programs |
| Adult Women (18+) | `is_female(r.gender_id) and age_years(r.birthdate) >= 18` | Women's programs |
| Women of Reproductive Age (15-49) | `is_female(r.gender_id) and age_years(r.birthdate) >= 15 and age_years(r.birthdate) <= 49` | Maternal health |

### Household-based templates

| Template | Expression | Use case |
|----------|------------|----------|
| Large Households (4+) | `hh_size >= 4` | Family support |
| Children Under 5 | `members.count(m, age_years(m.birthdate) < 5) >= 1` | Child nutrition |
| School-Age Children (6-18) | `members.count(m, age_years(m.birthdate) >= 6 and age_years(m.birthdate) <= 18) >= 1` | Education support |
| Female-Headed Households | `members.exists(m, head(m) and is_female(m.gender_id))` | Vulnerability targeting |
| Elderly-Headed Households (60+) | `members.exists(m, head(m) and age_years(m.birthdate) >= 60)` | Elderly support |
| High Dependency Ratio (3+) | `members.count(m, age_years(m.birthdate) < 18 or age_years(m.birthdate) >= 60) >= 3` | Vulnerability scoring |

## Using a template

### Step 1: Open the eligibility manager

1. Go to **Programs → Programs** and open your program
2. Click the **Configuration** tab
3. Find the **Eligibility Manager** section
4. Click the gear icon to open manager settings

### Step 2: Select a template

In the eligibility manager form:

1. Look for the **Based On** or template selector field
2. Click to open the template list
3. Select the appropriate template

```{figure} ../../_images/en-us/config_guide/eligibility/09-template-selection-dropdown.png
:alt: Template selection dropdown showing available templates

The **Examples** tab in the Advanced Builder showing available expression templates.
```

### Step 3: Review and customize

After selecting a template:

1. The CEL expression is populated automatically
2. Review the expression to ensure it matches your requirements
3. Modify if needed (unless the template is locked)
4. Check the match count
5. Save the configuration

```{figure} ../../_images/en-us/config_guide/eligibility/10-template-applied-with-expression.png
:alt: Template applied showing expression and match count

A template expression applied to the eligibility manager with validation and match count.
```

## Template lineage tracking

When you use a template, OpenSPP tracks:

| Field | Description |
|-------|-------------|
| **Based On** | The source template |
| **Modified** | Whether you've changed the expression |
| **Locked** | Whether modifications are prevented |

```{figure} ../../_images/en-us/config_guide/eligibility/11-template-lineage-indicators.png
:alt: CEL Expression Examples list showing available templates with categories and expressions

The **CEL Expression Examples** list where templates are managed. Each template has a category, name, expression, and target type.
```

### Modified indicator

If you change a template's expression:

- A "Modified" indicator appears
- The original template reference is preserved
- You can compare your version to the original

### Locked templates

Some templates are locked for governance:

- The expression cannot be modified
- Ensures compliance with standardized criteria
- Contact an administrator to unlock if needed

```{warning}
Locked templates show a warning: "This eligibility criteria is locked and cannot be modified."
```

## Customizing templates

Unless locked, you can modify a template's expression:

### Adding conditions

```cel
# Original: Senior Citizens (65+)
age_years(r.birthdate) >= 65

# Customized: Senior Women (65+)
age_years(r.birthdate) >= 65 and is_female(r.gender_id)
```

### Adjusting thresholds

```cel
# Original: Large Households (4+)
hh_size >= 4

# Customized: Very Large Households (6+)
hh_size >= 6
```

### Combining templates

You can combine criteria from multiple templates:

```cel
# Combine: Female-headed AND children under 5
members.exists(m, head(m) and is_female(m.gender_id)) and members.count(m, age_years(m.birthdate) < 5) >= 1
```

## Creating custom templates

Administrators can create new templates for organization-specific criteria.

### Step 1: Access template management

Go to **Programs → Configuration → CEL Expression Examples**

```{note}
This menu is only visible to administrators with the appropriate permissions.
```

### Step 2: Create new template

1. Click **Create**
2. Fill in template details:

| Field | Description |
|-------|-------------|
| **Name** | Display name (e.g., "Subsistence Farmers") |
| **Code** | Unique identifier (e.g., `eligibility_farmers`) |
| **Expression Type** | Select "Filter" for eligibility |
| **Context Type** | Individual or Group |
| **CEL Expression** | The eligibility rule |
| **Is Template** | Check this box |
| **Is Locked** | Check to prevent modifications |

### Step 3: Test and activate

1. Verify the expression is valid
2. Test with sample data
3. Set state to **Active**
4. The template now appears in the template selector

## Template best practices

### Naming conventions

Use clear, descriptive names:

| Good | Bad |
|------|-----|
| Senior Citizens (65+) | Elderly |
| Households with Children Under 5 | HH Children |
| Female-Headed Households | FHH |

Include the threshold in the name where applicable (65+, 4+, etc.).

### When to lock templates

Lock templates when:

- Standardized criteria are required for compliance
- Multiple programs must use identical criteria
- Central policy defines the eligibility rules

### When to allow modifications

Allow modifications when:

- Programs need flexibility for local adaptation
- Templates are starting points, not strict requirements
- Implementers need to add additional conditions

## Are you stuck?

**Template not showing in the list?**
- Check the template's state is "Active"
- Verify the context type matches your program (Individual vs Group)
- Ask an administrator to verify template configuration

**Can't modify a locked template?**
- Contact an administrator to unlock if changes are required
- Or create a new program with an unlocked template

**Expression from template doesn't match expected count?**
- Verify your registry data contains the expected values
- Check the context type (Individual vs Group)
- Review the expression logic carefully

## Next steps

- {doc}`cel_expressions` - Understand CEL syntax for customization
- {doc}`testing` - Validate template-based eligibility
- {doc}`advanced` - Use multiple managers with different templates
