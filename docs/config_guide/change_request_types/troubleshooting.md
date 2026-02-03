---
openspp:
  doc_status: draft
  products: [core]
---

# Troubleshooting

This guide covers testing your configuration, security settings, and solutions to common issues.

## Testing your configuration

Before deploying a new change request type, test the complete workflow.

### Step 1: Create test request

1. Log in as a **Change Request Officer**
2. Navigate to **Registry → Change Requests → New**
3. Select your new request type
4. Fill in all fields
5. Click **Submit for Approval**

### Step 2: Test approval

1. Log in as a **Change Request Approver**
2. Open the pending request
3. Review the information
4. Click **Approve**

### Step 3: Verify application

1. Open the registrant record
2. Check that the fields were updated correctly
3. Check the **Event Data** tab for audit trail

### Step 4: Test rejection flow

1. Create another test request
2. As approver, click **Reject**
3. Verify the registrant record was **not** updated

## Security configuration

### Access groups

Change request types respect standard Odoo security:

**Group: Change Request Officer**
- Create change requests
- Submit for approval
- Edit draft requests

**Group: Change Request Approver**
- View pending requests
- Approve/reject/request revision
- View approval history

**Group: Change Request Administrator**
- Configure request types
- View all requests
- Manually apply requests
- Override approval workflows

### Record rules

Configure record rules to restrict which requests users can see:

**Rule: Own Requests Only**
```python
[('create_uid', '=', user.id)]
```

**Rule: Requests for My Area**
```python
[('registrant_id.area_id', 'in', user.allowed_area_ids.ids)]
```

**Rule: Requests for My Program**
```python
[('registrant_id.program_ids', 'in', user.program_ids.ids)]
```

## Common issues

### Request type not appearing

**Problem:** Users don't see the new request type in the dropdown.

**Checks:**
- Has the request type been activated? (Click **Activate** button to change from Draft status)
- Does the user have the **Change Request Officer** group?
- Is **Target Type** compatible with the selected registrant (Individual vs Group/Household)?
- Is there a domain filter on the request type field?

### Apply fails after approval

**Problem:** Request is approved but changes don't apply to the registrant.

**Checks:**
- Is **Auto Apply On Approve** enabled in the Apply Configuration tab?
- Are the field mappings correct? Check source/target field names.
- Check Odoo logs for errors: `/var/log/odoo/odoo.log`
- Do the fields exist on the target model (`res.partner`)?
- Does the apply strategy model exist?

### Approval workflow not triggering

**Problem:** Request stays in "Draft" after submission.

**Checks:**
- Is an **Approval Workflow** selected on the request type?
- Is the approval definition active?
- Are there approvers assigned to the approval groups?
- Check the **Approval Reviews** tab on the change request

### Missing fields in form

**Problem:** Detail form doesn't show expected fields.

**Checks:**
- Is the **Detail Form View** specified correctly?
- Were the fields added to the detail model?
- Is the form view's `model` attribute correct?
- Try clearing browser cache
- Check Studio's form view editor

### Document validation not working

**Problem:** Users can submit without required documents.

**Checks:**
- Is **Document Validation Mode** set to "Block if Missing"?
- Are the **Required Documents** selected?
- Do the document types exist in the system?
- Is the document field visible in the form?

### Field mapping not updating value

**Problem:** Approved CR doesn't update the target field.

**Checks:**
- Is the source field name spelled correctly (case-sensitive)?
- Does the target field exist on `res.partner`?
- For relational fields, are you mapping the field itself (not `.id`)?
- Is the field value actually different from the current value?

### Expression mapping error

**Problem:** Expression throws an error during apply.

**Checks:**
- Test the expression in Odoo shell first
- Handle `None`/`False` values with `or` operators
- Check for syntax errors (missing quotes, parentheses)
- Verify all referenced fields exist

### Custom apply strategy fails

**Problem:** Custom method throws an error.

**Checks:**
- Does the apply model exist? (`spp.cr.apply.<name>`)
- Does the apply method exist on the model?
- Check Odoo logs for the specific error
- Verify the method signature matches expected parameters

## Are you stuck?

**Want to add a field that doesn't exist in the detail model?**

Use Configurator V2 to add the field to the detail model, or ask a developer to add it via code. Then add a new apply mapping for the field.

**Need to map to a custom field on res.partner?**

Ensure the custom field exists first (via Configurator or custom module). Then add the mapping as normal.

**Apply strategy is too simple for your needs?**

You'll need a **custom apply strategy**. This requires Python code - see the developer guide or ask a developer to create one.

**Need to validate data before approval?**

Add validation logic to the detail model using `@api.constrains` decorators, or create a custom approval workflow with validation steps.

**Want different approval workflows based on field values?**

Use **conditional approval definitions** - configure multiple approval workflows and use a computed field on the change request to select the right one based on the detail values.

**Need to create requests programmatically?**

Use the API V2 endpoints (`/ChangeRequest`) or create records directly:

```python
detail = env['spp.cr.detail.edit_individual'].create({
    'given_name': 'John',
    'family_name': 'Doe',
    'phone': '+1234567890',
})

cr = env['spp.change.request'].create({
    'request_type_id': env.ref('spp_change_request_v2.cr_type_edit_individual').id,
    'registrant_id': registrant.id,
    'detail_res_id': detail.id,
    'source_type': 'api',
})

cr.action_submit()  # Submit for approval
```

**Conflict detection blocking legitimate requests?**

Review your conflict rules:
- Reduce the time window
- Change action from "Block" to "Warning"
- Use "Same Type Only" to narrow scope
- Add specific conflict types instead of checking all

**Duplicate detection not catching duplicates?**

Adjust the configuration:
- Lower the similarity threshold (try 85% instead of 95%)
- Specify which fields to compare
- Increase the time window

## See also

- {doc}`creating_types` - Step-by-step configuration guide
- {doc}`field_mappings` - Field mapping options
- {doc}`conflict_detection` - Conflict and duplicate detection
- {doc}`patterns` - Common configuration patterns
- {doc}`../event_data/index` - Integrate with event data collection
- {doc}`../../developer_guide/api_v2/index` - Create change requests via REST API
