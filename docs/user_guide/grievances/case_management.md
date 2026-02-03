---
openspp:
  doc_status: draft
  products: [grievances]
---

# Managing and Resolving Grievances

This guide is for **users** who investigate and resolve grievance tickets – GRM Officers and Supervisors.

## What You'll Do

Review assigned tickets, investigate complaints, make decisions, and communicate outcomes to complainants while meeting SLA deadlines.

## Before You Start

- You need **GRM Officer** or **GRM Supervisor** access
- Understand your organization's policies for handling different complaint types
- Know how to access related systems (payment records, program enrollment, registry)

## Your GRM Officer Dashboard

### 1. Access Your Dashboard

Click **GRM** in the sidebar, then select **My Dashboard**.

<!-- TODO: Add screenshot: Sidebar with GRM menu expanded, My Dashboard option highlighted -->
<!-- ![Screenshot should show: Sidebar with GRM menu expanded, My Dashboard option highlighted](case_management/1_open_dashboard.png) -->

### 2. Understand Your Workload

The dashboard shows:

| Section | What It Shows |
|---------|---------------|
| **SLA Status** | Tickets colored by urgency (Red = overdue, Amber = approaching deadline, Green = on track) |
| **My Tickets** | All tickets assigned to you |
| **New Tickets** | Recently assigned, not yet reviewed |
| **Pending Information** | Waiting for response from complainant or others |
| **Escalated** | Flagged for supervisor attention |
| **Ready to Close** | Decision made, ready for final closure |

<!-- TODO: Add screenshot: GRM Dashboard with multiple columns showing tickets in different stages, with color-coded SLA indicators -->
<!-- ![Screenshot should show: GRM Dashboard with multiple columns showing tickets in different stages, with color-coded SLA indicators](case_management/2_dashboard_overview.png) -->

## Investigating a Ticket

### 3. Open a Ticket

Click on any ticket to open it.

The ticket form shows:
- **Top banner**: Ticket number, status, SLA deadline
- **Left panel**: Complainant details and classification
- **Center**: Description and timeline
- **Right panel**: Smart buttons for related records

<!-- TODO: Add screenshot: Ticket form open with all sections labeled: ticket number at top, complainant info on left, description in center, smart buttons on right -->
<!-- ![Screenshot should show: Ticket form open with all sections labeled: ticket number at top, complainant info on left, description in center, smart buttons on right](case_management/3_open_ticket.png) -->

### 4. Review the Complaint

Read the complaint details carefully:

1. **Description tab**: What the complainant reported
2. **Chatter (bottom)**: Timeline of all actions and communications
3. **Attachments**: Any supporting documents
4. **Related records**: Linked program enrollment, payments, etc.

<!-- TODO: Add screenshot: Ticket form with Description tab active showing complaint text, and Chatter section below showing timeline entries -->
<!-- ![Screenshot should show: Ticket form with Description tab active showing complaint text, and Chatter section below showing timeline entries](case_management/4_review_complaint.png) -->

### 5. Check Related Records

Use smart buttons to view related information:

| Smart Button | Shows You |
|--------------|-----------|
| **Beneficiary Profile** | Full registrant record, household info, demographics |
| **Program Enrollment** | Enrollment status, eligibility, enrollment date |
| **Payments** | Payment history, amounts, dates, disbursement status |
| **Previous Tickets** | Past complaints from this person |
| **Case Record** | Related case management record (if any) |

Click a smart button to open the related record in a new tab or popup.

<!-- TODO: Add screenshot: Ticket form with smart buttons visible on right side (Beneficiary, Program, Payments, etc.) with number badges showing counts -->
<!-- ![Screenshot should show: Ticket form with smart buttons visible on right side (Beneficiary, Program, Payments, etc.) with number badges showing counts](case_management/5_smart_buttons.png) -->

### 6. Verify the Facts

**For payment complaints:**
1. Click **Payments** smart button
2. Check payment status: Paid, Failed, Pending
3. Verify amount matches entitlement
4. Check payment date and method
5. Look for errors or rejections in payment logs

**For eligibility complaints:**
1. Click **Program Enrollment** smart button
2. Review eligibility assessment results
3. Check targeting criteria and scores
4. Verify documentation requirements were met

**For service quality complaints:**
1. Check which office or staff member was involved
2. Review service standards and protocols
3. Interview staff if needed (document in ticket notes)

<!-- TODO: Add screenshot: Split view with ticket on left and related payment record open on right showing payment details and status -->
<!-- ![Screenshot should show: Split view with ticket on left and related payment record open on right showing payment details and status](case_management/6_verify_facts.png) -->

### 7. Document Your Investigation

Add notes to the ticket as you investigate:

1. Scroll to the **Chatter** section at the bottom
2. Click **Log note** (for internal notes) or **Send message** (to notify others)
3. Type your findings
4. **Format**: Use bullet points for clarity
5. Click **Log** or **Send**

**What to document:**
- Records you checked (e.g., "Reviewed payment batch 2025-03-15")
- People you contacted (e.g., "Spoke with field officer Maria Lopez")
- Findings (e.g., "Payment was sent but beneficiary didn't receive SMS")
- Next steps (e.g., "Requesting payment re-issue from finance team")

```{important}
**Confidentiality**: Never include sensitive personal information (health status, abuse details, specific GBV information) in chatter messages. Use coded language or mark notes as "Log note" (internal only).
```

<!-- TODO: Add screenshot: Chatter section with "Log note" button highlighted, text entry box with sample investigation notes, and previous logged notes visible below -->
<!-- ![Screenshot should show: Chatter section with "Log note" button highlighted, text entry box with sample investigation notes, and previous logged notes visible below](case_management/7_log_notes.png) -->

## Requesting Additional Information

### 8. Request Information from Complainant

If you need more details from the complainant:

1. Move ticket to **Pending Information** stage (drag ticket in kanban view, or change Stage field)
2. Click **Send message** in Chatter
3. Select **Send to complainant** option
4. Type your request clearly (e.g., "Please provide your bank account number for payment re-issue")
5. Click **Send**

The system sends an email or SMS to the complainant (if contact info was provided).

<!-- TODO: Add screenshot: Ticket form with Stage dropdown showing "Pending Information" selected, and Chatter compose box showing email being composed to complainant -->
<!-- ![Screenshot should show: Ticket form with Stage dropdown showing "Pending Information" selected, and Chatter compose box showing email being composed to complainant](case_management/8_request_information.png) -->

### 9. Set a Follow-up Reminder

To remind yourself to check back:

1. Click **Activities** button in the toolbar
2. Click **Schedule activity**
3. Choose **To-Do** or **Call**
4. Set due date
5. Add note about what you're waiting for
6. Click **Schedule**

You'll receive a reminder notification when the due date arrives.

<!-- TODO: Add screenshot: Schedule Activity dialog with activity type dropdown, due date picker, and summary field visible -->
<!-- ![Screenshot should show: Schedule Activity dialog with activity type dropdown, due date picker, and summary field visible](case_management/9_schedule_activity.png) -->

## Making a Decision

### 10. Choose the Resolution

Once investigation is complete, record your decision:

1. Go to **Resolution** tab
2. Select **Decision** from dropdown:

| Decision | When to Use |
|----------|-------------|
| **Upheld** | Complaint is valid; complainant is right |
| **Partially Upheld** | Part of the complaint is valid |
| **Rejected** | Complaint is not valid; no error found |
| **Withdrawn** | Complainant withdrew the complaint |
| **Redirected** | Not a GRM matter; directed to correct channel |
| **Referred to Case** | Complex issue escalated to case management system |

3. In **Resolution Summary**, explain your decision:
   - What you found
   - Why you made this decision
   - What actions will be taken (if upheld)
   - Reference relevant policies or regulations

<!-- TODO: Add screenshot: Ticket form with Resolution tab active, Decision dropdown expanded showing options, and Resolution Summary text editor below -->
<!-- ![Screenshot should show: Ticket form with Resolution tab active, Decision dropdown expanded showing options, and Resolution Summary text editor below](case_management/10_record_decision.png) -->

### 11. Record Actions Taken

If the decision requires action (payment re-issue, eligibility review, etc.):

1. In **Resolution Summary**, specify:
   - What will be done
   - Who will do it
   - When it will be completed
2. If action is in another system (payments, enrollment), create the necessary records there
3. Link back to this ticket in those records (reference ticket number)

**Example resolution summary:**

> **Decision**: Upheld
>
> **Findings**: Payment was sent to beneficiary's old phone number on file. Beneficiary updated their phone number in registry on March 1, but payment batch was processed using data from February 28.
>
> **Actions**:
> - Payment will be re-issued to new phone number (0912-345-6789)
> - Payment request submitted to Finance (Ref: PAY-2025-1234)
> - Expected completion: March 25, 2025
> - Beneficiary will receive SMS notification when payment is sent

<!-- TODO: Add screenshot: Resolution Summary field with formatted text example showing findings and actions clearly structured -->
<!-- ![Screenshot should show: Resolution Summary field with formatted text example showing findings and actions clearly structured](case_management/11_resolution_example.png) -->

### 12. Notify the Complainant

To send the decision to the complainant:

1. Click **Send Resolution** button in the toolbar
2. Review the auto-generated message (you can edit if needed)
3. Click **Send**

The system sends the decision via email or SMS to the complainant's contact information.

```{note}
If the complaint was anonymous or no contact info provided, you can't send notifications. Mark ticket as resolved anyway for record-keeping.
```

<!-- TODO: Add screenshot: Email compose dialog with resolution notification template populated, showing decision and summary ready to send to complainant -->
<!-- ![Screenshot should show: Email compose dialog with resolution notification template populated, showing decision and summary ready to send to complainant](case_management/12_send_notification.png) -->

### 13. Close the Ticket

After decision is communicated and actions completed:

1. Change **Stage** to **Resolved**
2. Click **Save**

If approval is required (based on category or decision type):
1. Click **Submit for Approval** button
2. System routes to your supervisor
3. Supervisor will approve or send back with comments

<!-- TODO: Add screenshot: Ticket form with Stage field showing "Resolved" selected, and Submit for Approval button visible if approval workflow is enabled -->
<!-- ![Screenshot should show: Ticket form with Stage field showing "Resolved" selected, and Submit for Approval button visible if approval workflow is enabled](case_management/13_close_ticket.png) -->

## Handling Special Situations

### Escalating to Supervisor

If you need supervisor help:

1. Click **Escalate** button in toolbar
2. Select **Escalate to** (choose supervisor or specific user)
3. Add reason for escalation in the dialog
4. Click **Escalate**

The ticket moves to "Escalated" stage and supervisor receives notification.

**When to escalate:**
- Decision requires higher authority
- Complaint involves serious misconduct
- You need policy guidance
- SLA deadline will be missed despite best efforts

<!-- TODO: Add screenshot: Escalate dialog with "Escalate to" user selection field and Reason text area -->
<!-- ![Screenshot should show: Escalate dialog with "Escalate to" user selection field and Reason text area](case_management/14_escalate.png) -->

### Converting to Case Management

For complex issues requiring ongoing support:

1. Click **Convert to Case** button
2. Dialog opens with case details pre-filled from ticket
3. Select **Case Type** (Protection, Livelihood Support, etc.)
4. Set **Intensity Level** (1=Information, 2=Intermediation, 3=Case Work)
5. Assign **Case Worker** (can be you or someone else)
6. Click **Create Case**

The system:
- Creates a new case record
- Links case to this ticket
- Moves ticket to "Referred to Case" status
- Notifies the case worker

```{note}
Some ticket categories automatically trigger case creation (e.g., GBV, child abuse). Your system administrator configures these rules.
```

<!-- TODO: Add screenshot: Convert to Case dialog with case type dropdown, intensity level selection, and case worker assignment field -->
<!-- ![Screenshot should show: Convert to Case dialog with case type dropdown, intensity level selection, and case worker assignment field](case_management/15_convert_to_case.png) -->

### Handling Appeals

If a complainant appeals your decision:

1. They can click **Submit Appeal** in the portal, or contact you directly
2. System creates a new ticket of type "Appeal"
3. Appeal ticket links to original ticket
4. Appeals usually route to supervisor or appeals committee
5. Original ticket remains closed; appeal is a new ticket

To find appeals of your decisions:
- Go to **GRM** → **Tickets**
- Filter by **Ticket Type**: Appeal
- Filter by **Related to**: your username

<!-- TODO: Add screenshot: Tickets list filtered to show appeals, with "Ticket Type: Appeal" filter active and Related Ticket column showing linked original tickets -->
<!-- ![Screenshot should show: Tickets list filtered to show appeals, with "Ticket Type: Appeal" filter active and Related Ticket column showing linked original tickets](case_management/16_appeals.png) -->

### Reassigning Tickets

If ticket was assigned to you by mistake:

1. Open the ticket
2. Change **Assigned To** field to correct officer
3. Add a note in Chatter explaining why you're reassigning
4. Click **Save**

The other officer receives a notification.

**Supervisors** can reassign any tickets in their team:
- Go to dashboard
- Select tickets (checkbox)
- Click **Action** → **Reassign**
- Choose new officer

<!-- TODO: Add screenshot: Ticket form with Assigned To field dropdown open showing list of team members, and bulk reassign action visible in list view -->
<!-- ![Screenshot should show: Ticket form with Assigned To field dropdown open showing list of team members, and bulk reassign action visible in list view](case_management/17_reassign.png) -->

## Supervisor Functions

### Monitoring Team Performance

**For Supervisors**: Click **GRM** → **Team Dashboard**

The dashboard shows:
- Tickets by officer and status
- SLA compliance metrics (% resolved on time)
- Average resolution time
- Overdue tickets (red)
- Categories receiving most complaints

<!-- TODO: Add screenshot: Team Dashboard with charts showing ticket volume by officer, SLA performance gauge, and list of overdue tickets -->
<!-- ![Screenshot should show: Team Dashboard with charts showing ticket volume by officer, SLA performance gauge, and list of overdue tickets](case_management/18_supervisor_dashboard.png) -->

### Approving Decisions

If officers need approval before closing tickets:

1. Go to **GRM** → **Pending Approvals**
2. Click on ticket requiring approval
3. Review investigation and decision
4. Options:
   - **Approve**: Ticket proceeds to resolved
   - **Reject**: Ticket returns to officer with feedback
   - **Request Changes**: Officer must revise before resubmitting

Add your comments in Chatter before approving/rejecting.

<!-- TODO: Add screenshot: Ticket in approval view with Approve and Reject buttons prominent, and Comments field for supervisor feedback -->
<!-- ![Screenshot should show: Ticket in approval view with Approve and Reject buttons prominent, and Comments field for supervisor feedback](case_management/19_approve_decision.png) -->

### Managing Workload

To rebalance workload among officers:

1. Go to **GRM** → **Team Dashboard**
2. Check **Tickets per Officer** chart
3. If someone is overloaded, select their tickets
4. Click **Action** → **Reassign**
5. Choose officer with lighter workload

<!-- TODO: Add screenshot: Team Dashboard with tickets per officer bar chart visible, showing uneven distribution, and selection checkboxes active on ticket list -->
<!-- ![Screenshot should show: Team Dashboard with tickets per officer bar chart visible, showing uneven distribution, and selection checkboxes active on ticket list](case_management/20_rebalance_workload.png) -->

## Are You Stuck?

**Can't find related payment record?**
The payment might not be linked to the ticket. Use the **Payments** smart button to search, or go to **Payments** module and search by beneficiary name and date range. If you find the relevant payment, you can link it by editing the ticket's "Related Payment" field.

**Need to change ticket category after starting investigation?**
You can reclassify the ticket. Change the **Category** field and click **Save**. The system may recalculate the SLA deadline based on the new category. If SLA changes, a note is automatically added to the chatter.

**Complainant provided new information after you closed ticket?**
Reopen the ticket: Change **Stage** back to "In Review" and add a note explaining why you reopened it. Continue investigation with the new information.

**Don't know if you should escalate?**
Ask yourself:
- Do you have authority to make this decision per your organization's policies?
- Do you have all needed information and evidence?
- Is the deadline approaching and you need help?
- Does this involve serious issues (corruption, abuse, safety)?

When in doubt, it's better to escalate than make a wrong decision.

**System won't let you close ticket?**
Check:
- **Decision** field must be filled
- **Resolution Summary** must have content
- Some categories require supervisor approval - click "Submit for Approval" instead of changing stage directly
- Check if there are validation rules specific to your organization

**Need to document sensitive information?**
Use **Log note** (not "Send message") to keep it internal. For highly sensitive cases (GBV, child abuse), these tickets should be marked with "Highly Sensitive" sensitivity level, which restricts who can view them. If you're handling such a case, follow your organization's safeguarding protocols in addition to documenting in the system.

**Beneficiary is dissatisfied with your decision and argues?**
Explain that they have the right to appeal. Appeals go to a supervisor or appeals committee for independent review. Provide them with:
- Instructions for submitting an appeal (usually via portal or written request)
- Deadline for appeals (typically 14-30 days from decision notification)
- What additional evidence they should provide to support their appeal

**Can't reach complainant to notify them?**
Try all contact methods on file (phone, SMS, email). Document your attempts in Chatter (e.g., "Called 3 times on March 15-17, no answer"). If you can't reach them after reasonable attempts, you can still close the ticket. Some organizations have a policy like "3 contact attempts over 1 week" - check your local procedures.
