---
openspp:
  doc_status: draft
  products: [core]
---

# Common configuration patterns

This guide presents common patterns for configuring change request types based on real-world use cases.

## Pattern 1: Auto-approved simple changes

For low-risk changes that don't need manual review.

### Configuration

| Field | Value |
|-------|-------|
| Approval Workflow | (select "Auto-Approve" or leave empty) |
| Auto Approve From Event | No |
| Auto Apply On Approve | Yes |
| Document Validation Mode | No Validation |

### Use cases

- Phone number updates
- Email address changes
- Address corrections
- Tag updates

### Example: Phone update

| Setting | Value |
|---------|-------|
| Name | Update Phone Number |
| Code | `update_phone` |
| Target Type | Individual |
| Detail Model | `spp.cr.detail.edit_individual` |
| Apply Strategy | Field Mapping |
| Auto Apply On Approve | Yes |

**Field Mappings:**

| Source | Target | Transform |
|--------|--------|-----------|
| `phone` | `phone` | Direct Copy |

## Pattern 2: Two-level sensitive changes

For changes requiring supervisor and manager approval.

### Configuration

| Field | Value |
|-------|-------|
| Approval Workflow | (select "Two-Level Approval") |
| Auto Apply On Approve | Yes |
| Document Validation Mode | Block if Missing |
| Required Documents | National ID, Supporting Document |

### Use cases

- Name changes
- Birth date corrections
- Gender updates
- ID document changes

### Example: Name change

| Setting | Value |
|---------|-------|
| Name | Change Name |
| Code | `change_name` |
| Target Type | Individual |
| Detail Model | `spp.cr.detail.edit_individual` |
| Apply Strategy | Field Mapping |

**Approval Workflow:**

| Level | Approvers | Action |
|-------|-----------|--------|
| 1 | Supervisor Group | Verify documents |
| 2 | Program Manager Group | Final approval |

**Required Documents:**

- National ID (front and back)
- Supporting document (marriage certificate, court order, etc.)

**Field Mappings:**

| Source | Target | Transform |
|--------|--------|-----------|
| `given_name` | `given_name` | Direct Copy |
| `family_name` | `family_name` | Direct Copy |

## Pattern 3: Manual application

For changes needing technical review before applying.

### Configuration

| Field | Value |
|-------|-------|
| Approval Workflow | (select "Single Approver") |
| Auto Apply On Approve | **No** |
| Apply Strategy | Manual |

### Use cases

- Complex group restructuring
- Data migrations
- Bulk corrections
- Merging duplicate records

### Example: Merge registrants

| Setting | Value |
|---------|-------|
| Name | Merge Duplicate Records |
| Code | `merge_registrants` |
| Target Type | Individual |
| Detail Model | `spp.cr.detail.merge_registrants` |
| Apply Strategy | Custom Method |
| Apply Model | `spp.cr.apply.merge_registrants` |
| Auto Apply On Approve | No |

**Workflow:**

1. Officer identifies duplicates and creates merge request
2. Manager approves the merge
3. Administrator reviews and manually applies the merge
4. Records are consolidated

## Pattern 4: Event-sourced auto-creation

For change requests created automatically from external data.

### Configuration

| Field | Value |
|-------|-------|
| Auto Approve From Event | Yes |
| Auto Apply On Approve | Yes |
| Apply Strategy | Field Mapping |
| Document Validation Mode | No Validation |

### Use cases

- Field survey updates
- Mobile app submissions
- API integrations
- Bulk data imports

### Example: Field survey update

| Setting | Value |
|---------|-------|
| Name | Survey Data Update |
| Code | `survey_update` |
| Target Type | Both |
| Detail Model | `spp.cr.detail.edit_individual` |
| Auto Approve From Event | Yes |

**Integration:**

```python
# Event data automatically creates and approves CR
event_data.create_change_request(
    type_code='survey_update',
    registrant_id=registrant.id,
    values={'phone': '+1234567890', 'email': 'new@email.com'}
)
```

## Pattern 5: Household member changes

For adding, removing, or transferring household members.

### Configuration

| Field | Value |
|-------|-------|
| Target Type | Group/Household |
| Apply Strategy | Custom Method |
| Auto Apply On Approve | Yes |

### Example: Add member

| Setting | Value |
|---------|-------|
| Name | Add Household Member |
| Code | `add_member` |
| Target Type | Group/Household |
| Detail Model | `spp.cr.detail.add_member` |
| Apply Strategy | Custom Method |
| Apply Model | `spp.cr.apply.add_member` |

**Custom Apply Logic:**

The `spp.cr.apply.add_member` strategy:
1. Creates a new individual if needed
2. Creates group membership relationship
3. Sets membership type (member, head, etc.)
4. Updates household composition

### Example: Change head of household

| Setting | Value |
|---------|-------|
| Name | Change Head of Household |
| Code | `change_hoh` |
| Target Type | Group/Household |
| Detail Model | `spp.cr.detail.change_hoh` |
| Apply Strategy | Custom Method |
| Apply Model | `spp.cr.apply.change_hoh` |

**Custom Apply Logic:**

The `spp.cr.apply.change_hoh` strategy:
1. Demotes current head to regular member
2. Promotes selected member to head
3. Updates household relationships

## Pattern 6: Conditional approval

For changes where approval requirements depend on the data.

### Configuration

Use multiple CR types with different approval workflows:

| CR Type | Condition | Approval |
|---------|-----------|----------|
| Minor Address Update | Same city | Auto-approve |
| Major Address Update | Different city | Single approval |
| Cross-Region Move | Different region | Two-level approval |

### Implementation approach

1. Create separate CR types for each scenario
2. Use domain filters to show appropriate types
3. Or use a computed field to select approval workflow

## Pattern 7: Document-heavy requests

For requests requiring extensive documentation.

### Configuration

| Field | Value |
|-------|-------|
| Document Validation Mode | Block if Missing |
| Available Documents | (multiple types) |
| Required Documents | (specific required types) |

### Example: Birth certificate update

| Setting | Value |
|---------|-------|
| Name | Update Birth Certificate |
| Code | `update_birth_cert` |
| Document Validation Mode | Block if Missing |

**Available Documents:**

- Birth Certificate (Original)
- Birth Certificate (Copy)
- Supporting Letter
- ID Document

**Required Documents:**

- Birth Certificate (Original) OR Birth Certificate (Copy)

## Choosing the right pattern

| Scenario | Recommended Pattern |
|----------|---------------------|
| Simple data corrections | Auto-approved simple changes |
| Legal document changes | Two-level sensitive changes |
| Complex data transformations | Manual application |
| External system integrations | Event-sourced auto-creation |
| Family structure changes | Household member changes |
| Risk-based approval | Conditional approval |
| Compliance-heavy processes | Document-heavy requests |

## See also

- {doc}`creating_types` - Step-by-step configuration guide
- {doc}`field_mappings` - Field mapping options
- {doc}`conflict_detection` - Preventing conflicting changes
- {doc}`troubleshooting` - Common issues and solutions
