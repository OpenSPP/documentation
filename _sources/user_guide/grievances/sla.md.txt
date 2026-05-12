---
orphan: true
openspp:
  doc_status: draft
  products: [grievances]
---

# SLA tracking and escalation

This guide is for **users** who need to monitor response times and escalate grievances that risk missing their deadlines.

## What you'll do

Track Service Level Agreement (SLA) deadlines for grievance tickets, identify at-risk tickets, and take action to ensure timely resolution.

## Before you start

- You need **GRM Officer** or **GRM Supervisor** access
- Understand your organization's SLA policies for different complaint types
- Know your escalation procedures and who to contact

## Understanding SLAs

### What is an SLA?

A Service Level Agreement (SLA) is the **maximum time** allowed to resolve a ticket. It's calculated based on:

- **Severity** of the complaint
- **Category** of the complaint
- **Sensitivity** level
- Business days vs calendar days (depending on configuration)

### SLA time targets

Typical SLA targets by severity:

| Severity | SLA target | Example |
|----------|------------|---------|
| **Critical** | 24 hours | GBV report, safety hazard, severe corruption |
| **High** | 3 business days | Payment failures affecting many people, urgent appeals |
| **Medium** | 7 business days | Individual payment issues, eligibility appeals |
| **Low** | 14 business days | Information requests, minor service quality issues |

```{important}
Your organization may have different SLA targets. Check your GRM policies or ask your supervisor for specific targets.
```

### SLA status indicators

The system uses color codes to show SLA status:

| Color | Status | Meaning | Time remaining |
|-------|--------|---------|----------------|
| 🟢 Green | On Track | Resolution time is comfortable | > 25% of SLA remaining |
| 🟡 Amber | At Risk | Deadline approaching, needs attention | 10-25% of SLA remaining |
| 🔴 Red | Breached | Past deadline, urgent action needed | Overdue |


## Monitoring your SLAs

### 1. View your SLA dashboard

Click **GRM** → **My Dashboard**

The dashboard shows tickets organized by SLA status with visual indicators.


### 2. Check SLA deadline

Open any ticket to see SLA details:

| Field | What it shows |
|-------|---------------|
| **SLA Deadline** | Target date and time for resolution |
| **SLA Status** | On Track / At Risk / Breached |
| **Time Remaining** | Days/hours left (e.g., "2 days 5 hours remaining") |
| **Days Open** | How long ticket has been open |

The deadline is shown in the top banner of the ticket form.


### 3. Filter tickets by SLA status

To focus on urgent tickets:

1. Go to **GRM** → **Tickets**
2. Click **Filters** in the left sidebar
3. Select filter options:
   - **SLA Status**: At Risk or Breached
   - **Assigned To**: Me
   - **Stage**: In Review (tickets requiring action)
4. Click **Apply Filter**


### 4. Sort by deadline

To work on most urgent tickets first:

1. In the tickets list, click the **SLA Deadline** column header
2. Tickets sort from earliest to latest deadline
3. Red (breached) tickets appear at the top


## Taking action on at-risk tickets

### 5. Prioritize your workload

**For officers**: Review your dashboard daily

**Priority order:**
1. **Red (Breached)** - Work on these immediately
2. **Amber (At Risk)** - Schedule time today or tomorrow
3. **Green (On Track)** - Normal workflow

**Time management tip:** Block out time each morning for breached tickets before starting other work.


### 6. Fast-track investigation

For at-risk tickets, streamline your investigation:

**Quick checks:**
- Review description and category
- Check most relevant record (payment, enrollment, etc.)
- Contact complainant immediately if information is missing
- Make decision based on available evidence

**Document efficiently:**
- Use bullet points in notes
- Focus on key facts only
- Skip lengthy explanations until ticket is resolved


### 7. Request deadline extension (If Needed)

If you legitimately need more time:

1. Click **Request Extension** button
2. Select reason:
   - Waiting for information from complainant
   - Requires coordination with external agency
   - Complex investigation requiring more time
   - Technical system issues preventing resolution
3. Justify the request (explain why you need more time)
4. Propose new deadline
5. Click **Submit**

Your supervisor receives the request and can approve or deny.

```{note}
Extension requests should be exceptional. Overuse of extensions may indicate workload issues or training needs.
```


## Escalation procedures

### 8. When to escalate

Escalate a ticket when:

| Situation | Action |
|-----------|--------|
| **Can't meet deadline** | Need supervisor to prioritize or reassign |
| **Lack authority** | Decision requires higher approval level |
| **Policy unclear** | Need guidance on how to handle the case |
| **Complex investigation** | Need specialist expertise or resources |
| **Complainant dispute** | Conflict you can't resolve at your level |
| **Serious issues** | Corruption, abuse, safety concerns |

### 9. Escalate to supervisor

To escalate within GRM:

1. Open the ticket
2. Click **Escalate** button in toolbar
3. Select **Escalate to**: Choose supervisor or specific person
4. Provide clear reason:
   - What you've done so far
   - What's blocking you
   - What you need from them
   - Deadline context (e.g., "Due in 6 hours")
5. Click **Escalate**

Ticket moves to "Escalated" stage. Supervisor receives urgent notification.


### 10. Escalate to specialized team

Some issues need specialist handling:

| Team | Handles |
|------|---------|
| **Protection Team** | GBV, child abuse, exploitation |
| **Finance Team** | Payment system errors, bulk payment issues |
| **Eligibility Team** | Complex targeting disputes, appeals |
| **IT Support** | Portal access, system errors |

To route to specialist team:

1. Open ticket
2. Change **Team** field to specialist team
3. Add note in Chatter explaining why you're routing it
4. Click **Save**


## Automatic escalations

### 11. Understanding auto-escalation rules

Your system may have automatic escalation rules configured:

**Common auto-escalation triggers:**
- SLA breached by more than 24 hours
- Critical severity tickets not reviewed within 2 hours
- Highly sensitive tickets (GBV, child abuse) - immediate escalation
- Third complaint from same beneficiary within 6 months
- Staff misconduct complaints

When auto-escalation happens:
- System changes ticket stage to "Escalated"
- Supervisor or designated person is automatically notified
- SLA deadline may be extended per policy
- Escalation is logged in ticket chatter


### 12. Responding to auto-escalated tickets

If you receive an auto-escalated ticket:

1. Check the escalation reason in Chatter
2. Review what the original officer did (if applicable)
3. Take immediate action:
   - Make the decision if you have authority
   - Re-assign to correct person/team
   - Investigate urgently
4. Respond within your supervisor SLA (usually 24 hours)


## Supervisor SLA monitoring

### 13. Team SLA dashboard (supervisors)

**For supervisors**: Click **GRM** → **Team dashboard**

Monitor team-wide SLA performance:

| Metric | What it shows | Target |
|--------|---------------|--------|
| **SLA compliance rate** | % of tickets resolved within SLA | > 90% |
| **Average resolution time** | Mean time to resolve tickets | Varies by severity |
| **Breached tickets** | Count of overdue tickets | Minimize |
| **At risk tickets** | Count of tickets approaching deadline | Monitor daily |
| **Tickets per officer** | Workload distribution | Balanced across team |


### 14. Identify performance issues

**Warning signs to watch for:**

| Issue | Indicator | Action |
|-------|-----------|--------|
| **Officer overloaded** | One officer has many at-risk tickets | Reassign some tickets |
| **Category bottleneck** | One category has high breach rate | Review if special skills needed |
| **Repeat extensions** | Same officer requests many extensions | Training or workload review |
| **Low compliance rate** | Team SLA compliance below 85% | Process review, resources check |


### 15. Reassign to balance workload

To address overload:

1. Go to **Team Dashboard**
2. Check **Tickets per Officer** chart
3. Select tickets from overloaded officer (use checkboxes)
4. Click **Action** → **Reassign**
5. Choose officer with lighter workload and appropriate skills
6. Click **Reassign**

Officers receive notifications of new assignments.


### 16. Approve extension requests

When an officer requests deadline extension:

1. Go to **GRM** → **Extension requests**
2. Click on request to review
3. Check:
   - Is reason valid?
   - Have they made reasonable progress?
   - Is new deadline realistic?
4. Options:
   - **Approve** - Extends deadline as requested
   - **Approve with Changes** - Set different deadline
   - **Deny** - Explain what officer should do instead


## SLA reporting

### 17. Generate SLA reports

To track SLA performance over time:

1. Go to **GRM** → **Reports** → **SLA Performance**
2. Select time period (e.g., Last Month, Last Quarter)
3. Optional filters:
   - Team
   - Category
   - Severity
4. Click **Generate Report**

Report shows:
- Compliance rate trend
- Average resolution time by category
- Top reasons for breaches
- Officer-level performance


### 18. Export SLA data

To export for analysis:

1. In any ticket list or dashboard, click **Export** button
2. Choose format:
   - **Excel** - For data analysis
   - **CSV** - For importing to other tools
   - **PDF** - For sharing/printing
3. Select fields to include (SLA Deadline, Days Open, Resolution Time, etc.)
4. Click **Export**


## Best practices

### Daily routine for officers

**Morning (15 minutes):**
1. Check dashboard for breached tickets (red) - prioritize these
2. Review at-risk tickets (amber) - plan to work on today
3. Respond to any complainant messages from overnight

**Throughout day:**
1. Work on oldest tickets first within each SLA status
2. Log progress notes as you go (don't wait until end of day)
3. Flag issues early - don't wait until deadline to escalate

**Before leaving (10 minutes):**
1. Update ticket statuses
2. Set follow-up activities for next day
3. Check if any tickets moved from green to amber

### Weekly routine for supervisors

**Monday:**
- Review weekend accumulation (if any)
- Check team workload distribution
- Approve pending extension requests

**Mid-week:**
- Review SLA compliance metrics
- Follow up on escalated tickets
- Coach officers struggling with deadlines

**Friday:**
- Review week's performance
- Plan for next week's workload
- Address any recurring issues

### SLA improvement tips

**For Officers:**
- **Front-load the investigation**: Gather all information early, don't procrastinate
- **Set internal mini-deadlines**: Aim to finish 2 days before SLA deadline
- **Ask for help early**: Don't wait until the last minute to escalate
- **Use templates**: Speed up communication with standard messages
- **Batch similar tasks**: Handle all payment issues together, all eligibility issues together

**For Supervisors:**
- **Review SLA rules regularly**: Are they realistic? Do they need adjustment?
- **Identify training needs**: If same issue causes delays repeatedly, train team
- **Remove bottlenecks**: If approvals slow things down, streamline approval process
- **Recognize good performance**: Thank officers who consistently meet SLAs
- **Analyze breach patterns**: Learn from misses to prevent future ones

## Are you stuck?

**SLA deadline seems wrong or unfair?**
SLA is calculated automatically based on category and severity. If it's consistently too short or too long for certain types, talk to your supervisor about adjusting the SLA rules. Individual tickets can be extended if there's good reason.

**Can't meet SLA because waiting for external agency response?**
Document your attempts to contact them in Chatter (dates, methods, who you contacted). Request extension with this documentation. Consider escalating to supervisor who may have higher-level contacts.

**SLA keeps getting extended and ticket is very old?**
This may indicate the case is too complex for GRM and should be converted to Case Management. Case Management is designed for long-term, ongoing issues. Discuss with your supervisor.

**Officer's SLA performance is poor - what to do?**
Have a conversation to understand why:
- Too many tickets? → Reassign some
- Lack of skills? → Provide training
- Not prioritizing correctly? → Coach on time management
- System issues? → Escalate to IT
Don't assume poor performance = bad worker. Often there's a fixable root cause.

**System shows ticket as breached but you resolved it on time?**
Check if there's a time zone issue. Contact your system administrator. Also check if the system is counting business days vs calendar days correctly.

**Complainant keeps adding new issues and deadline pressure builds?**
If they raise a different issue, create a new ticket. Keep the original ticket focused on the original complaint only. This keeps investigation clear and prevents scope creep.

**Critical ticket assigned to someone on leave?**
Supervisors can see all tickets. If you're covering for someone, check their dashboard and reassign any critical/urgent tickets to available officers. Don't let tickets breach because someone is out.

**Getting auto-escalation notifications for tickets that don't need escalation?**
The auto-escalation rules may need adjustment. Document which tickets are being incorrectly escalated and discuss with your supervisor or system administrator. Rules are configurable.
