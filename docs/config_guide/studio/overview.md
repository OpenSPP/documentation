---
openspp:
  doc_status: draft
  products: [core]
---

# Studio Overview

This guide is for **implementers** configuring OpenSPP Studio. You should be familiar with form builders like KoBoToolbox or ODK, but you don't need programming knowledge.

## What is OpenSPP Studio?

OpenSPP Studio is a no-code configuration interface that lets you customize OpenSPP without developer involvement. It handles 80% of common customization needs through visual tools.

### Mental Model

Think of Studio like KoBoToolbox's form builder, but for configuring your entire registry system:

| In KoBoToolbox | In OpenSPP Studio |
|----------------|-------------------|
| Build a form | Design an event type |
| Add questions | Add registry fields |
| Set question types | Choose field types |
| Make fields required | Configure validation |
| Deploy form | Activate configuration |
| View submissions | View collected data |

## Accessing Studio

### Prerequisites

- You need **Studio Editor** or **Studio Manager** permissions
- Access is controlled through user roles by your system administrator

### Opening Studio

1. Log in to OpenSPP
2. Click **Studio** in the main menu
3. You'll see the Studio Dashboard with quick access to Studio tools

![Studio highlighted in the apps menu](/_images/en-us/config_guide/studio/overview/01-apps-menu-studio-highlighted.png)

![Studio Dashboard showing the main tool cards](/_images/en-us/config_guide/studio/overview/02-studio-dashboard.png)

## Studio Components

### 1. Registry Field Builder

**Use when**: You need to track additional information about registrants or groups.

**Examples**:
- Add "Disability Type" field to Individual registry
- Add "Pantawid ID" for Philippines beneficiaries
- Track "Vulnerability Score" for targeting

**What you can do**:
- Add fields to existing registry tabs
- Choose field types (text, number, date, dropdown, etc.)
- Set field as required or optional
- Control where the field appears in the form

**What requires a developer**:
- Creating entirely new tabs or pages
- Complex calculated fields with business logic

→ See {doc}`registry_field_builder` for detailed instructions.

### 2. Event Type Designer

**Use when**: You collect time-based observations or survey data about registrants.

**Examples**:
- Import vulnerability assessment from KoBoToolbox
- Create monthly follow-up visit form
- Design household verification survey

**What you can do**:
- Create event types with custom fields
- Import field definitions from Kobo/ODK forms
- Connect to external data collection servers
- Configure event lifecycle (expiration, approval, replacement)

**What requires a developer**:
- Complex data transformations during import
- Custom integrations beyond Kobo/ODK
- Performance optimization for large datasets

→ See {doc}`event_type_designer` for detailed instructions.

### 3. Change Request Builder

**Use when**: You need a formal workflow to update registry information with approval.

**Examples**:
- Phone number update with supervisor approval
- Address change request with documentation
- ID document update workflow

**What you can do**:
- Create simple change request types
- Define what information to collect
- Map fields to registry for automatic updates
- Configure approval requirements

**What requires a developer**:
- Complex change requests (add member, split household, merge records)
- Custom approval logic beyond standard workflows
- Multi-record operations

→ See {doc}`change_request_builder` for detailed instructions.

### 4. Eligibility Rules (CEL Expressions)

**Use when**: You need to define who qualifies for a program based on specific criteria.

**Examples**:
- Households with income below threshold and children under 5
- Elderly individuals over 65 living alone
- Families with vulnerability score above 70

**What you can do**:
- Build eligibility rules using CEL (Common Expression Language) expressions
- Use the Expression Editor under the **Rules** menu
- Access variables for registry fields, event data, and computed values
- Test expressions with test personas
- Browse pre-built Logic Packs for common eligibility patterns

**What requires a developer**:
- Very complex logic with nested conditions across multiple data sources
- Custom CEL functions not in the standard library
- Performance-optimized batch eligibility checks for millions of records

→ See {doc}`/config_guide/cel/index` for detailed instructions on building eligibility expressions.

### 5. External Connections

**Use when**: You want to connect OpenSPP to KoBoToolbox or ODK Central for data collection.

Access external connections through the **Connections** menu in Studio.

**What you can do**:
- Connect to Kobo servers with API tokens
- Connect to ODK Central servers
- Browse and import form definitions
- Manually fetch submissions (Phase 1)

**Future capabilities** (Phase 2):
- Automatic submission sync via webhooks
- Real-time event creation from submissions

→ See {doc}`event_type_designer` for instructions on importing Kobo/ODK forms.

## Configuration Lifecycle

All Studio configurations follow the same lifecycle:

```
Draft → Active → Inactive
  ↑__________________|
     (can reactivate)
```

### States Explained

| State | Meaning | Who Can Edit |
|-------|---------|--------------|
| **Draft** | Configuration is being prepared | Studio Editor or Manager |
| **Active** | Configuration is live and in use | Studio Manager only |
| **Inactive** | Configuration was active but is now disabled | Studio Manager only |

### Important Rules

- You can freely edit **Draft** configurations
- You cannot delete **Active** configurations (deactivate first)
- Deactivating shows impact warning (e.g., "This field is used by 1,247 records")
- All changes are logged with user and timestamp

## Permissions

Studio has three permission levels:

| Role | Can Do |
|------|--------|
| **Viewer** | View all configurations, but cannot create or edit |
| **Editor** | Create and edit draft configurations |
| **Manager** | Activate, deactivate, and delete configurations |

To assign Studio permissions to a user:
1. Go to **Settings** > **Users & Companies** > **Users**
2. Edit the user
3. Under **Privileges**, enable **Studio**
4. Choose the appropriate level: Viewer, Editor, or Manager

```{note}
Studio uses OpenSPP's privilege-based security system. Groups appear as "Studio / Viewer", "Studio / Editor", and "Studio / Manager" in the Groups list.
```

![User settings showing Studio privilege options](/_images/en-us/config_guide/studio/overview/08-user-studio-privileges.png)

## The 80/20 Rule

Studio is designed to handle 80% of common customization needs. Here's what's included and what requires developer help:

### What Studio Handles (80%)

| Task | Studio Tool |
|------|-------------|
| Add fields to registries | ✓ Registry Field Builder |
| Create event types | ✓ Event Type Designer |
| Import Kobo forms | ✓ Event Type Designer |
| Simple change requests | ✓ Change Request Builder |
| CEL eligibility expressions | ✓ Expression Editor (Rules menu) |
| Field validation | ✓ Configuration options |
| Conditional visibility | ✓ Visibility settings |

### What Requires Developers (20%)

| Task | Why Developer Needed |
|------|---------------------|
| New registry tabs/pages | View architecture changes |
| Complex change requests (add member, split household) | Multi-record operations |
| Custom computed fields | Python code required |
| New integrations | API development needed |
| Custom reports | Report builder not in scope |
| Performance-critical batch operations | Queue job configuration |

**When you need developer help**, Studio will show clear messages like:

```
ℹ️ This feature requires developer assistance

Creating a change request that adds new group members
requires custom code. This cannot be done through Studio.

What you can do:
• Use the built-in "Add Member" CR type
• Contact your IT administrator for custom requirements
```

## Studio Dashboard

The Studio Dashboard is your starting point for configuring OpenSPP without code.

![Studio Dashboard with main tool cards](/_images/en-us/config_guide/studio/overview/02-studio-dashboard.png)

### Dashboard Cards

The dashboard provides quick access to the main Studio tools:

| Card | Description |
|------|-------------|
| **Expressions** | Build eligibility rules, benefit calculations, and compliance checks |
| **Variables** | Define reusable variables for expressions (fields, computed values, aggregates) |
| **Custom Fields** | Add custom fields to individual and group registries |
| **Event Types** | Define data collection forms for surveys, assessments, and field visits |
| **Change Requests** | Configure change request types for updating registrant information |

Each card includes a brief description and a button to open that tool.

### Studio Menu

Besides the dashboard, you can access Studio features through the main Studio menu:

![Studio menu sections in the sidebar](/_images/en-us/config_guide/studio/overview/03-studio-sidebar-menu.png)

- **Home** - Return to the dashboard
- **Rules** - Work with expressions, variables, logic packs, and test personas
- **Forms & Fields** - Manage custom fields, event types, and change request types
- **Settings** - Advanced configuration options (Studio Manager only)
- **History** - View audit logs of all Studio changes

```{note}
Additional menu items may appear depending on installed modules:
- **Privacy** - Configure consent and data classification (requires `spp_studio_consent`)
- **Connections** - Set up external data sources like Kobo/ODK (requires `spp_studio_dci`)
```

## Best Practices

### 1. Start with Draft

Always create configurations as **Draft** first:
- Test thoroughly before activating
- Have colleagues review configurations
- Check that field names and labels are clear

### 2. Use Clear Names

Choose descriptive names that other staff will understand:

| Bad | Good |
|-----|------|
| "Field 1" | "Pantawid ID Number" |
| "Survey" | "Monthly Household Visit" |
| "Update" | "Phone Number Change Request" |

### 3. Document Your Intent

Use help text and descriptions:
- Explain what fields are for
- Note where data comes from
- Describe when to use change request types

### 4. Test Before Activating

For CEL expressions:
- Use the test personas feature to validate your expressions
- Verify expected registrants are included/excluded
- Check with program staff that logic is correct

### 5. Coordinate with Team

Before activating configurations that affect others:
- Notify relevant staff
- Explain what will change
- Provide training if needed

## Studio vs Developer Work

Understanding when to use Studio vs when to request developer help:

### Use Studio When

- Adding standard field types to registries
- Creating new survey/event types
- Building simple update workflows
- Defining eligibility based on existing data

### Request Developer Help When

- Needing calculations or formulas in fields
- Creating complex multi-step workflows
- Building custom integrations
- Optimizing performance for large-scale operations
- Adding new core functionality

## Are You Stuck?

**Can't see certain options in Studio?**
Check your permissions. You may need Studio Manager access for activation/deactivation.

**Configuration doesn't appear after activating?**
Try refreshing your browser. Some changes require a page reload.

**Want to undo an activation?**
Studio Managers can deactivate configurations. The system will warn you about impacts before deactivating.

**Need to change an active configuration?**
You cannot edit active configurations directly. Options:
1. Deactivate, edit, reactivate (may cause data issues)
2. Create a new version as draft, activate new one, deactivate old one
3. Contact developer for structural changes

**Getting "field already exists" error?**
Field names must be unique. Choose a different name or check if the field was created previously.

## Next Steps

Now that you understand Studio's capabilities:

1. **To add custom fields**: Continue to {doc}`registry_field_builder`
2. **To create event types**: Continue to {doc}`event_type_designer`
3. **To build change workflows**: Continue to {doc}`change_request_builder`
4. **To define eligibility rules**: Continue to {doc}`/config_guide/cel/index`
