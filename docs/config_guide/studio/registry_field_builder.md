---
openspp:
  doc_status: draft
  products: [core]
---

# Registry Field Builder

This guide is for **implementers** adding custom fields to the registry. You should be comfortable with form builders like KoBoToolbox, but you don't need programming knowledge.

## What is Registry Field Builder?

Registry Field Builder lets you add custom fields to Individual and Group registries without developer help. Place fields in pre-defined sections of the registry forms.

## When to Use Registry Field Builder

Use this tool when you need to track information that isn't in the standard OpenSPP registry:

| Use Case | Example Field |
|----------|---------------|
| Country-specific IDs | "Pantawid ID" for Philippines |
| Disability information | "Disability Type" dropdown |
| Program-specific data | "Vulnerability Score" number |
| Custom contact info | "WhatsApp Number" text field |
| Housing conditions | "Housing Material" selection |

## Mental Model

Think of the registry as a form with pre-defined tabs and sections:

| Tab | Sections | What Goes Here |
|-----|----------|----------------|
| **Profile** | Demographics, Contact, Financial | Personal info, age, gender, phone, income |
| **Identity** | IDs, Relationships | National ID, program IDs, family connections |
| **Participation** | Programs, Events | Program enrollments, survey data |
| **Custom** | Additional Details | Your custom fields (default location) |

You can add fields to any section. Most custom fields go in "Additional Details" unless they clearly fit elsewhere.

## Before You Start

### Prerequisites

- **Studio Editor** or **Studio Manager** permissions
- Understanding of what data you need to collect
- Clear field names and labels planned

### Planning Your Field

Before creating a field, decide:

1. **Label**: What users will see (e.g., "Disability Type")
2. **Field type**: Text, number, date, dropdown, etc.
3. **Location**: Which tab and section
4. **Validation**: Required? Read-only? Searchable?
5. **Help text**: Tooltip to help users understand the field

## Creating a Custom Field

### Step 1: Open Field Builder

1. Click **Studio** in the main menu
2. Click **Registry Fields**
3. Click **+ New Field** button

**Screenshot should show**: Studio menu item in main menu, then Studio Dashboard with Registry Fields card highlighted, then Registry Field Builder list view with "+ New Field" button.

### Step 2: Choose Registry Type

Select where this field will appear:

| Option | Use When |
|--------|----------|
| **Individual** | Field applies to people (e.g., "Disability Type") |
| **Group** | Field applies to households/groups (e.g., "Housing Material") |

**Screenshot should show**: Registry type selection screen with Individual and Group radio buttons.

### Step 3: Enter Basic Information

| Field | What to Enter | Example |
|-------|---------------|---------|
| **Label** | What users see | "Disability Type" |
| **Technical Name** | Auto-generated from label | `x_cst_disability_type` |
| **Help Text** | Optional tooltip for users | "Select the primary type of disability, if any" |

**Tips**:
- Use clear, descriptive labels
- Help text explains when/how to fill the field
- Technical name is automatic - you don't need to change it

**Screenshot should show**: Step 1 of field creation wizard with Label, Technical Name (grayed out), and Help Text fields filled in with the example above.

Click **Next →** when ready.

### Step 4: Choose Field Type

Select the type of data this field will hold:

| Type | Use For | Example |
|------|---------|---------|
| **Text** | Short text up to 256 characters | "Pantawid ID", "WhatsApp Number" |
| **Long Text** | Multi-line notes or descriptions | "Special Needs Notes" |
| **Number (whole)** | Counting numbers | "Number of Dependents" |
| **Number (decimal)** | Amounts with decimals | "Vulnerability Score" |
| **Date** | Calendar dates | "Last Assessment Date" |
| **Yes/No** | Checkbox for true/false | "Has Disability" |
| **Selection** | Dropdown with choices | "Disability Type", "Housing Material" |
| **Multi-Select** | Choose multiple options | "Languages Spoken" |
| **Link** | Link to another record (advanced) | "Link to Area", "Link to Language" |

**Screenshot should show**: Step 2 of wizard with the nine field type cards displayed as shown in the spec (icons and descriptions).

#### If You Choose "Selection" or "Multi-Select"

You'll see an additional screen to define choices:

| Column | What to Enter |
|--------|---------------|
| **Value** | What's stored in database | `physical`, `visual`, `hearing` |
| **Label** | What users see | "Physical Disability", "Visual Impairment" |

**Example for Disability Type**:

| Value | Label |
|-------|-------|
| `physical` | Physical Disability |
| `visual` | Visual Impairment |
| `hearing` | Hearing Impairment |
| `cognitive` | Cognitive Disability |

**Screenshot should show**: Selection options configuration screen with the disability type example filled in, showing the table with Value/Label columns and [↑][↓][×] buttons for each row.

**Tips**:
- Use simple, lowercase values without spaces
- Use clear, user-friendly labels
- Order choices logically (most common first, or alphabetically)
- Use [↑][↓] buttons to reorder choices

Click **Next →** when field type is configured.

### Step 5: Configure Placement and Options

#### Placement

Choose where the field appears:

| Setting | Options |
|---------|---------|
| **Tab** | Profile, Identity, Participation, or Custom |
| **Section** | Depends on tab selected |
| **After** | Which existing field to appear after (or "At the end") |

**Common placements**:

| Field Type | Suggested Tab | Suggested Section |
|------------|---------------|-------------------|
| ID numbers | Identity | IDs |
| Contact info | Profile | Contact |
| Demographics | Profile | Demographics |
| Income/financial | Profile | Financial |
| Custom/unique data | Custom | Additional Details |

**Screenshot should show**: Step 3 of wizard showing Tab dropdown (Profile selected), Section dropdown (Demographics selected), and After dropdown (Gender selected).

#### Options

| Option | When to Use |
|--------|-------------|
| **Required** | Users must fill this field before saving |
| **Read-only** | Users can see but cannot edit (for calculated fields) |
| **Searchable** | Can filter registry by this field |

**Screenshot should show**: Options checkboxes with "Required" checked, others unchecked.

#### Visibility

Control when the field shows:

| Setting | Use When |
|---------|----------|
| **Always visible** | Field always appears |
| **Only when...** | Show field conditionally based on another field |

**Example**: Only show "Disability Type" when "Has Disability" is checked.

**Screenshot should show**: Visibility section with "Only when another field has a specific value" selected, showing dropdowns for "Has Disability" [is checked].

Click **Save as Draft** to create the field.

## After Creating a Field

### Review Your Field

1. Go to **Registry → Individuals** (or Groups)
2. Open any record or create a new one
3. Find your custom field in the tab/section you specified
4. Test entering data

**Screenshot should show**: Individual registry form with custom "Disability Type" field visible in the Demographics section.

### Activate the Field

Once you've tested:

1. Return to **Studio → Registry Fields**
2. Find your field in the list
3. Click to open it
4. Click **Activate** (requires Studio Manager permission)

**Screenshot should show**: Field detail view with "Activate" button highlighted.

**Warning**: Activating makes the field live for all users. Make sure you've tested thoroughly.

## Managing Existing Fields

### View All Custom Fields

**Studio → Registry Fields** shows all fields you've created:

| Column | Shows |
|--------|-------|
| **Field Name** | Label of the field |
| **Type** | Field type (Text, Selection, etc.) |
| **Location** | Tab and section |
| **Status** | Draft or Active |

**Screenshot should show**: Registry Field list view with several custom fields listed, showing columns as described.

### Edit a Field

**For Draft fields**:
1. Click the field name
2. Make your changes
3. Click **Save**

**For Active fields**:
- You cannot edit active fields directly
- Options:
  1. Deactivate → Edit → Reactivate (may cause data issues)
  2. Create new field → Migrate data → Delete old field (requires developer)

### Deactivate a Field

**Warning**: Deactivating removes the field from forms, but existing data is preserved.

1. Open the field
2. Click **Deactivate**
3. System shows impact warning: "This field is used by 1,247 records"
4. Confirm deactivation

**Screenshot should show**: Deactivation confirmation dialog with warning message.

### Delete a Field

You can only delete **inactive** fields:

1. Deactivate the field first
2. Open the field
3. Click **Delete**
4. Confirm deletion

**Warning**: This removes the field configuration. Data may still exist in the database but won't be accessible through the UI.

## Field Type Reference

### Text Field

**Use for**: Short single-line text (up to 256 characters)

**Examples**:
- ID numbers: "Pantawid ID"
- Phone numbers: "WhatsApp Number"
- Short names: "Nickname"

**Options**:
- Can be marked as required
- Can be made searchable
- Supports basic text validation

### Long Text Field

**Use for**: Multi-line text notes

**Examples**:
- "Special Needs Description"
- "Home Visit Notes"
- "Program Comments"

**Displays as**: Multi-line text area

### Number Fields

**Integer (whole numbers)**:
- Examples: "Number of Dependents", "Age in Years"
- No decimal places

**Float (decimal numbers)**:
- Examples: "Vulnerability Score", "Monthly Income"
- Allows decimals

**Options**:
- Can set minimum/maximum values
- Can mark as required

### Date Field

**Use for**: Calendar dates

**Examples**:
- "Last Assessment Date"
- "ID Expiry Date"
- "Enrollment Date"

**Shows**: Calendar picker in UI

**Screenshot should show**: Date field with calendar picker open.

### Yes/No Field

**Use for**: True/false, checkbox data

**Examples**:
- "Has Disability"
- "Owns Land"
- "Receives Other Benefits"

**Displays as**: Checkbox

### Selection Field

**Use for**: Choose one option from a list

**Examples**:
- "Disability Type" (Physical, Visual, Hearing, Cognitive)
- "Housing Material" (Concrete, Wood, Bamboo, Mixed)
- "Education Level" (None, Primary, Secondary, Tertiary)

**Displays as**: Dropdown list

**Configuration**:
- Define value/label pairs
- Order matters (shows in defined order)
- Can add/remove choices before activating

### Multi-Select Field

**Use for**: Choose multiple options from a list

**Examples**:
- "Languages Spoken" (English, Tagalog, Cebuano, Ilocano)
- "Disabilities" (Multiple types)
- "Income Sources" (Employment, Farming, Remittances, Pension)

**Displays as**: Tag selector

**Screenshot should show**: Multi-select field showing tags for selected items.

### Link Field (Advanced)

**Use for**: Linking to other records

**Examples**:
- Link to Area (geographic region)
- Link to Language
- Link to custom lookup table

**Note**: This is advanced and may require developer help for complex relationships.

## Common Patterns

### Country-Specific ID

```
Label: Pantawid ID Number
Type: Text
Location: Identity > IDs
Required: No (only for Philippines beneficiaries)
Searchable: Yes
```

### Disability Tracking

```
Field 1:
  Label: Has Disability
  Type: Yes/No
  Location: Profile > Demographics
  Required: No

Field 2:
  Label: Disability Type
  Type: Selection
  Options: Physical, Visual, Hearing, Cognitive, Other
  Location: Profile > Demographics
  Visible: Only when "Has Disability" is checked
  Required: No
```

### Housing Conditions

```
Label: Housing Material
Type: Selection
Options:
  - concrete: Concrete/Brick
  - wood: Wood
  - bamboo: Bamboo/Nipa
  - mixed: Mixed Materials
  - other: Other
Location: Custom > Additional Details
Required: No
```

### Vulnerability Score

```
Label: Vulnerability Score
Type: Number (decimal)
Location: Custom > Additional Details
Required: No
Help Text: Score from 0-100 based on PMT assessment
```

## Are You Stuck?

**Field doesn't appear in the registry form?**
- Make sure the field is **Active**, not Draft
- Try refreshing your browser (Ctrl+F5 or Cmd+Shift+R)
- Check that you're viewing the correct registry (Individual vs Group)

**Can't change the technical name?**
Technical names are auto-generated and cannot be edited. They must be unique and follow Odoo field naming rules (`x_cst_` prefix).

**Field appears in wrong location?**
- Edit the field (if still Draft)
- Change the Tab, Section, or After settings
- Save and check again

**Getting "field already exists" error?**
- Field names must be unique within a registry
- Choose a different label
- Check if someone already created this field

**Want to rename a field?**
- For Draft fields: Edit and change the label
- For Active fields: You can only change the label, not the technical name

**Need calculated fields (like Age from Birthdate)?**
This requires developer help. Calculated fields need Python code.

**Want to make field visible only for specific programs?**
Studio supports basic conditional visibility. For program-specific fields, contact a developer.

**Field shows but can't enter data?**
- Check if field is marked as Read-only
- Check user permissions for the registry
- Verify field isn't hidden by conditional visibility

**How do I migrate data from one field to another?**
This requires developer help using database migration scripts.

## Next Steps

- **Create event types from surveys**: {doc}`event_type_designer`
- **Build change request workflows**: {doc}`change_request_builder`
- **Define eligibility rules**: {doc}`/config_guide/cel/index`
- **Return to Studio overview**: {doc}`overview`
