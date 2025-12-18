---
openspp:
  doc_status: draft
---

# Submitting a Grievance

This guide is for **users** who need to log complaints from beneficiaries through various channels (phone calls, in-person visits, field visits, or portal submissions).

## What You'll Do

Record a complaint or appeal in the system, ensuring all necessary details are captured so it can be routed to the right person and resolved on time.

## Before You Start

- You need **GRM Officer**, **Call Centre Operator**, or **Field Officer** access
- Have the beneficiary's information ready (name, ID number, or phone number)
- Know which program or service the complaint relates to (if applicable)

## Ways to Submit Grievances

OpenSPP supports multiple channels for receiving complaints:

| Channel | Who Uses It | When to Use |
|---------|-------------|-------------|
| **Call Centre** | Phone operators | Beneficiary calls the hotline |
| **Field Entry** | Field officers | During home visits or community outreach |
| **Portal** | Beneficiaries | Self-service online submission |
| **Walk-in** | Front desk staff | Beneficiary visits office in person |
| **Paper Forms** | Data entry staff | Transcribing paper complaint forms |

This guide focuses on **staff-assisted submission** (call centre, field, walk-in). For beneficiary portal submissions, see the Beneficiary Portal guide.

## Steps to Submit a Grievance

### 1. Open the GRM Module

Click **GRM** in the sidebar, then select **Tickets**.

![Screenshot should show: OpenSPP sidebar with GRM menu highlighted, and Tickets submenu visible](submit/1_open_grm_menu.png)

### 2. Create New Ticket

Click the **New** button in the top left corner.

![Screenshot should show: GRM Tickets list view with New button highlighted in top toolbar](submit/2_click_new_button.png)

### 3. Identify the Complainant

Fill in the complainant details:

**Complainant Type**: Select the appropriate type from the dropdown

| Type | When to Use |
|------|-------------|
| Beneficiary | Person is registered in the system |
| Non-beneficiary | Person not in registry but affected by program |
| Staff | Internal complaint from staff member |
| Anonymous | Complainant wants to remain anonymous |
| Other | Other cases (specify in notes) |

**Link to Beneficiary** (if applicable):
- Click the **Beneficiary** field
- Start typing the person's name or ID number
- Select the correct person from the dropdown

If the person is not in the system, leave this blank and fill in:
- **Contact Name**
- **Contact Phone**
- **Contact Email** (optional)

![Screenshot should show: Ticket form with Complainant Type dropdown expanded, and Beneficiary lookup field visible below it](submit/3_complainant_details.png)

### 4. Record Intake Details

Fill in how the complaint was received:

| Field | What to Enter |
|-------|---------------|
| **Channel** | How they contacted you (Hotline, Walk-in, Field Visit, Portal, Paper Form) |
| **Intake Date** | When you received the complaint (auto-filled with today's date) |
| **Subject** | Brief summary (e.g., "Missing payment for March 2025") |

![Screenshot should show: Ticket form with Channel dropdown, Intake Date field, and Subject field highlighted](submit/4_intake_details.png)

### 5. Classify the Complaint

Choose the appropriate category and severity:

**Category**: Select the main type of complaint

| Category | Examples |
|----------|----------|
| Payments | Missing payment, incorrect amount, payment delay |
| Eligibility | Rejected enrollment, wrongful exclusion, appeals |
| Service Quality | Rude staff, long wait times, office accessibility |
| Staff Conduct | Misconduct, corruption, favoritism |
| System Access | Can't log in to portal, lost credentials |
| Other | Complaints that don't fit other categories |

**Subcategory**: Select a more specific type (options depend on category)

**Severity**: Choose the urgency level

| Severity | When to Use | SLA (typical) |
|----------|-------------|---------------|
| Low | Minor issue, no immediate impact | 14 days |
| Medium | Moderate impact, needs attention | 7 days |
| High | Significant impact, urgent | 3 days |
| Critical | Emergency, safety risk, severe harm | 24 hours |

```{important}
**Sensitive Cases**: If the complaint involves Gender-Based Violence (GBV), child abuse, or serious corruption, mark **Sensitivity** as "Highly Sensitive". These automatically route to specialized teams and have restricted access.
```

![Screenshot should show: Ticket form with Category dropdown expanded showing options like Payments, Eligibility, etc., and Severity field visible](submit/5_classify_complaint.png)

### 6. Describe the Complaint

In the **Description** tab, record what the complainant told you:

- **What happened?** State the facts as reported
- **When did it happen?** Include dates if known
- **What does the complainant want?** Document their desired outcome

**Tips for good descriptions:**
- Use the complainant's own words when possible
- Include specific details (dates, amounts, names of staff involved)
- Be factual - don't add your own opinions
- Note if there are language or communication barriers

In the **Desired Resolution** field, write what the complainant is asking for (e.g., "Receive missing payment", "Review eligibility decision", "Apology from staff").

![Screenshot should show: Ticket form with Description tab active, showing rich text editor with sample complaint text, and Desired Resolution field below](submit/6_describe_complaint.png)

### 7. Link to Related Records (Optional)

If the complaint relates to specific records in the system, link them:

| Field | When to Use |
|-------|-------------|
| **Program** | Complaint about a specific program enrollment |
| **Payment** | Complaint about a specific payment transaction |
| **Household** | Complaint affects the entire household |
| **Case** | Related to an open case management record |

To link a record, click the field and search for the relevant item.

![Screenshot should show: Ticket form with Related Records section showing Program, Payment, Household, and Case lookup fields](submit/7_link_related_records.png)

### 8. Attach Supporting Documents (Optional)

If the complainant provided evidence (photos, documents, forms), attach them:

1. Click the **Attachments** button (paperclip icon) in the top toolbar
2. Click **Upload** and select files from your computer
3. Add a description for each file

**Accepted file types**: PDF, images (JPG, PNG), Word documents, Excel files

![Screenshot should show: Attachments dialog open with Upload button and list of uploaded files visible](submit/8_attach_documents.png)

### 9. Save the Ticket

Click **Save** to create the ticket.

The system will automatically:
- Generate a unique ticket number (e.g., GRM-2025-00123)
- Calculate the SLA deadline based on severity
- Route the ticket to the appropriate team and officer
- Send an acknowledgment notification to the complainant (if contact info provided)

![Screenshot should show: Saved ticket with ticket number visible at top, and status showing "Registered" with auto-assigned team visible](submit/9_save_ticket.png)

### 10. Provide the Ticket Number

**Important:** Give the complainant their ticket number so they can track their complaint.

You can:
- Read it out loud (for phone calls)
- Write it on a receipt (for walk-in)
- Send via SMS (if configured)
- Email it (if email provided)

![Screenshot should show: Ticket form with ticket number prominently displayed, and a "Send Acknowledgment" button visible in the toolbar](submit/10_provide_ticket_number.png)

## After Submission

Once saved, the ticket moves through these stages:

1. **Registered** - Waiting for officer assignment
2. **In Review** - Officer is investigating
3. **Pending Information** - More details needed
4. **Resolved** - Decision made and communicated
5. **Closed** - Case complete

The assigned GRM Officer will receive a notification and can begin investigating.

## Special Cases

### Anonymous Complaints

For anonymous complaints:
1. Select **Complainant Type**: Anonymous
2. Leave **Beneficiary** field blank
3. Do NOT record identifying information in description
4. You won't be able to send acknowledgments

```{warning}
Anonymous complaints have limited follow-up options. Encourage complainants to provide at least a phone number for updates.
```

### Urgent/Critical Complaints

For critical complaints (safety risks, GBV, child abuse):
1. Set **Severity**: Critical
2. Set **Sensitivity**: Highly Sensitive (if appropriate)
3. Contact your supervisor immediately - don't just submit and wait
4. Follow your organization's safeguarding protocols

### Complaints About Multiple Issues

If a complainant has several unrelated issues:
- Create **separate tickets** for each distinct issue
- This ensures proper routing and tracking
- Link tickets together in the "Related Tickets" field if needed

### Appeals of Previous Decisions

If the complaint is an appeal of an earlier decision:
1. Find the original ticket
2. Click **Create Appeal** button on the original ticket
3. System will automatically link the appeal to the original

## Are You Stuck?

**Can't find the beneficiary in the system?**
They might not be registered yet. Use the "Non-beneficiary" complainant type and enter their contact details manually. The GRM Officer can link them to their record later if needed.

**Don't know which category to choose?**
Choose the closest match. GRM Officers can reclassify tickets during investigation. If truly unsure, use "Other" and explain in the description.

**System won't let you save?**
Check for required fields marked with a red asterisk (*). Common missing fields:
- Subject (must not be empty)
- Category (must be selected)
- Description (must have content)

**Complainant is upset or emotional?**
Record the facts of what they're reporting, not the emotional tone. Note in the description if the person is distressed - this can help the investigating officer respond appropriately.

**Need to edit a ticket after saving?**
You can edit tickets in "Draft" or "Registered" status. Once an officer starts investigation, only they can edit. If you made a mistake, contact the assigned officer or your supervisor.

**Complainant doesn't have a ticket number handy when calling back?**
Search for tickets by:
- Beneficiary name (if linked)
- Contact phone number
- Date range and keyword in description

Click **Search** in the Tickets list and use the filters on the left sidebar.
