---
openspp:
  doc_status: draft
  products: [core]
---

# Creating change request types

This guide walks through creating a new change request type using the OpenSPP configuration interface.

## Prerequisites

- Access to OpenSPP with administrator or Change Request Administrator permissions
- An existing detail model (see {doc}`overview` for available models)
- An approval workflow configured (optional, but recommended)

## Step 1: Create the request type

Navigate to **Change Requests → Configuration → Change Request Types** and click **New**.

```{figure} /_images/en-us/config_guide/change_request_types/01-cr-types-list.png
:alt: Change Request Types list showing all configured types

The **Change Request Types** list — click **New** to create a type.
```

### Header

Enter the type name in the header field (placeholder shows "Type Name").

```{figure} /_images/en-us/config_guide/change_request_types/02-cr-type-form-new.png
:alt: New Change Request Type form with Name field highlighted

Enter the type name in the **Name** field at the top of the form.
```

### Basic info section

| Field | Value | Notes |
|-------|-------|-------|
| Code | `edit_individual` | Unique identifier (lowercase, underscores only) |
| Sequence | 10 | Lower numbers appear first in menus |
| Icon | `fa-edit` | Font Awesome icon class |
| Color | (select) | Color picker for visual identification |

### Target section

| Field | Value | Notes |
|-------|-------|-------|
| Target Type | Individual | Individual, Group/Household, or Both |
| Is Requires Applicant? | No | If yes, forces separate "submitted by" field |

### Description

Enter a description at the bottom of the form to help users understand when to use this type.

```{figure} /_images/en-us/config_guide/change_request_types/03-basic-info-filled.png
:alt: Basic info section with Code, Sequence, Icon, and Target Type fields highlighted

Configure the **Code**, **Sequence**, **Icon**, and **Target Type** fields.
```

## Step 2: Link to detail model

Navigate to the **Detail Model** tab.

| Field | Value | Notes |
|-------|-------|-------|
| Detail Model | `spp.cr.detail.edit_individual` | Technical model name (pre-created, required) |
| Detail Form View | (leave blank) | Auto-selects default view |

```{figure} /_images/en-us/config_guide/change_request_types/04-detail-model-tab.png
:alt: Detail Model tab with Detail Model and Detail Form View fields highlighted

Set the **Detail Model** and optionally the **Detail Form View** on the **Detail Model** tab.
```

```{note}
For basic configurations, use existing detail models. See {doc}`overview` for the complete list of available models.
```

## Step 3: Configure approval workflow

Navigate to the **Approval** tab.

| Field | Value | Notes |
|-------|-------|-------|
| Approval Workflow | Select from dropdown | Choose existing approval definition |
| Auto Approve From Event | No | If yes, requests from event data are auto-approved |

```{figure} /_images/en-us/config_guide/change_request_types/07-approval-tab.png
:alt: Approval tab with Approval Workflow and Auto Approve From Event fields highlighted

Select an **Approval Workflow** and configure **Auto Approve From Event** on the **Approval** tab.
```

```{note}
The **Auto Apply On Approve** field is located in the **Apply Configuration** tab (see Step 4).
```

### Creating approval workflows

If you need a new workflow, go to **Studio → Approvals → Definitions** first.

Example: Two-level approval for sensitive changes

| Field | Value |
|-------|-------|
| Name | Change Request - Sensitive |
| Levels | 2 |
| Level 1 Approvers | Supervisor Group |
| Level 2 Approvers | Program Manager Group |
| Require All | No |

## Step 4: Configure apply strategy

Navigate to the **Apply Configuration** tab.

```{figure} /_images/en-us/config_guide/change_request_types/05-apply-config-tab.png
:alt: Apply Configuration tab with Apply Strategy and Auto Apply On Approve fields highlighted

Choose the **Apply Strategy** and enable **Auto Apply On Approve** on the **Apply Configuration** tab.
```

### For simple field mapping

| Field | Value | Notes |
|-------|-------|-------|
| Apply Strategy | Field Mapping | Copies fields from detail to registrant |
| Auto Apply On Approve | Yes | If yes, changes apply immediately when approved |

### Field mappings

In the **Field Mappings** section below, add your mappings:

| Source Field | Target Field | Transform |
|--------------|--------------|-----------|
| `given_name` | `given_name` | Direct Copy |
| `family_name` | `family_name` | Direct Copy |
| `phone` | `phone` | Direct Copy |
| `email` | `email` | Direct Copy |
| `birthdate` | `birthdate` | Direct Copy |
| `gender_id` | `gender` | Direct Copy |

```{figure} /_images/en-us/config_guide/change_request_types/06-field-mapping-added.png
:alt: Field Mappings section with a phone field mapping added

Add **Field Mappings** to define how change request fields map to registrant fields.
```

### For custom logic

| Field | Value | Notes |
|-------|-------|-------|
| Apply Strategy | Custom Method | Uses Python code |
| Apply Model | `spp.cr.apply.add_member` | Pre-created custom strategy |
| Apply Method | `apply` | Method name (usually "apply") |

See {doc}`field_mappings` for detailed mapping configuration options.

## Step 5: Configure document requirements

Navigate to the **Documents** tab.

| Field | Value | Notes |
|-------|-------|-------|
| Document Validation Mode | No Validation | No Validation / Warning if Missing / Block if Missing |
| Available Documents | (select document types) | Document types that can be attached |
| Required Documents | (select document types) | Use Ctrl/Cmd+Click for multiple |

```{figure} /_images/en-us/config_guide/change_request_types/08-documents-tab.png
:alt: Documents tab with Document Validation Mode field highlighted

Set the **Document Validation Mode** and select **Available Documents** and **Required Documents**.
```

### Document validation modes

| Mode | Behavior |
|------|----------|
| No Validation | Documents are optional |
| Warning if Missing | Shows warning if missing, but allows submission |
| Block if Missing | Blocks submission until all required documents are uploaded |

## Save and activate

After completing all configuration:

1. Click **Save** to save the change request type
2. Click **Activate** to make it available for use

```{important}
Change request types must be activated before users can create requests of that type.
```

## Next steps

- {doc}`field_mappings` - Learn about advanced field mapping options
- {doc}`patterns` - See common configuration patterns
- {doc}`troubleshooting` - Troubleshoot common issues
