---
openspp:
  doc_status: draft
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
3. You'll see the Studio Dashboard with five main sections

**Screenshot should show**: OpenSPP main menu with Studio option highlighted, then Studio Dashboard with the five main cards (Registry Fields, Event Types, Change Requests, Eligibility Rules, External Sources).

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

### 4. Eligibility Rule Builder

**Use when**: You need to define who qualifies for a program based on specific criteria.

**Examples**:
- Households with income below threshold and children under 5
- Elderly individuals over 65 living alone
- Families with vulnerability score above 70

**What you can do**:
- Build rules visually by combining conditions
- Check registry fields, event data, group membership, and location
- Test rules to see how many registrants match
- Create rules without writing CEL expressions

**What requires a developer**:
- Very complex logic with nested OR/AND groups
- Custom functions not available in visual builder
- Performance-optimized rules for millions of records

→ See {doc}`eligibility_rule_builder` for detailed instructions.

### 5. External Sources

**Use when**: You want to connect OpenSPP to KoBoToolbox or ODK Central for data collection.

**What you can do**:
- Connect to Kobo servers with API tokens
- Connect to ODK Central servers
- Browse and import form definitions
- Manually fetch submissions (Phase 1)

**Future capabilities** (Phase 2):
- Automatic submission sync via webhooks
- Real-time event creation from submissions

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
| **Studio Viewer** | View all configurations, but cannot create or edit |
| **Studio Editor** | Create and edit draft configurations |
| **Studio Manager** | Activate, deactivate, and delete configurations |

**Screenshot should show**: Settings > Users & Companies > Groups, with Studio security groups highlighted.

## The 80/20 Rule

Studio is designed to handle 80% of common customization needs. Here's what's included and what requires developer help:

### What Studio Handles (80%)

| Task | Studio Tool |
|------|-------------|
| Add fields to registries | ✓ Registry Field Builder |
| Create event types | ✓ Event Type Designer |
| Import Kobo forms | ✓ Event Type Designer |
| Simple change requests | ✓ Change Request Builder |
| Visual eligibility rules | ✓ Eligibility Rule Builder |
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

The Studio Dashboard is your starting point:

**Screenshot should show**: Complete Studio Dashboard view showing all five cards with statistics.

### Dashboard Cards

Each card shows:
- Number of configurations (total and draft)
- Quick actions to create new configurations
- Link to manage existing configurations

### Recent Activity

The bottom section shows recent changes:
- Who made changes
- What was changed
- When changes occurred

This helps teams coordinate when multiple people use Studio.

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

For eligibility rules:
- Use the "Test Rule" button to see match counts
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
4. **To define eligibility**: Continue to {doc}`eligibility_rule_builder`
