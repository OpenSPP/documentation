---
openspp:
  doc_status: draft
---

# Grievance Redress Mechanism


## Overview

The Grievance Redress Mechanism module (`spp_grm`) provides a centralized system for receiving, tracking, and resolving beneficiary complaints and feedback. It supports multi-channel submission, manages resolution workflows through customizable stages, and links grievances directly to individual or group registrants.

## Purpose

This module is designed to:

- **Centralize complaint management:** Single system for all grievance channels
- **Track resolution progress:** Stage-based workflow with SLA monitoring
- **Link to registrants:** Connect complaints to existing beneficiary records
- **Support accountability:** Full audit trail of ticket handling
- **Enable escalation:** Automatic and manual escalation for overdue tickets

## Module Dependencies

| Dependency       | Description                             |
| ---------------- | --------------------------------------- |
| `base`           | Odoo core framework                     |
| `mail`           | Email integration and chatter           |
| `portal`         | Beneficiary self-service portal         |
| `spp_registry`   | Registrant records for linking          |
| `spp_area`       | Administrative areas for ticket routing |
| `spp_user_roles` | Role-based access for GRM teams         |
| `spp_security`   | Security groups and access control      |

## Key Features

### Ticket Management

Core ticket fields:

| Field       | Description                             |
| ----------- | --------------------------------------- |
| Number      | Auto-generated unique identifier        |
| Title       | Brief description of the complaint      |
| Description | Detailed complaint text                 |
| Contact     | Linked registrant (individual or group) |
| Category    | Primary classification                  |
| Subcategory | Secondary classification                |
| Priority    | Low, Medium, High, Very High            |
| Severity    | Low, Medium, High, Critical             |

### Multi-Channel Intake

| Channel   | Description                                   |
| --------- | --------------------------------------------- |
| Email     | Automatic ticket creation from incoming email |
| Portal    | Beneficiary self-service submission           |
| Phone     | Manual entry by call center staff             |
| In-person | Manual entry at service points                |
| SMS       | Integration with SMS gateway (optional)       |

### Stage-Based Workflow

Configure customizable stages:

| Stage Type       | Description                        |
| ---------------- | ---------------------------------- |
| Open             | Initial state, awaiting assignment |
| In Progress      | Under investigation                |
| Pending Response | Awaiting complainant input         |
| Resolved         | Solution implemented               |
| Closed           | Ticket completed                   |

Stage features:

- Allowed groups (who can move to this stage)
- Requires approval flag
- Requires decision flag (must record outcome)
- Is closed flag (marks ticket as done)

### SLA Tracking

| Feature         | Description                                   |
| --------------- | --------------------------------------------- |
| SLA Deadline    | Calculated from category/subcategory settings |
| SLA Status      | On Track, At Risk (< 25% time left), Breached |
| Auto-escalation | Trigger rules when SLA is breached            |

### Classification

**Categories and Subcategories:**

| Configuration       | Description                 |
| ------------------- | --------------------------- |
| Default SLA Hours   | Time allowed for resolution |
| Default Severity    | Initial severity assignment |
| Default Sensitivity | Data handling requirements  |
| Default Team        | Initial team assignment     |

**Sensitivity Levels:**

| Level            | Description                         |
| ---------------- | ----------------------------------- |
| Standard         | Normal handling procedures          |
| Sensitive        | Restricted access, careful handling |
| Highly Sensitive | Maximum privacy protection          |

### Decision and Resolution

| Decision         | Description                    |
| ---------------- | ------------------------------ |
| Upheld           | Complaint valid, action taken  |
| Partially Upheld | Some aspects valid             |
| Rejected         | Complaint not valid            |
| Withdrawn        | Complainant withdrew complaint |
| Redirected       | Sent to appropriate authority  |
| Referred to Case | Escalated for case management  |

### Team Assignment

- Configure GRM teams with managers and members
- Auto-assign based on category/team mapping
- Manual reassignment by supervisors

### Appeals

Tickets can be linked as appeals:

| Field           | Description                   |
| --------------- | ----------------------------- |
| Is Appeal       | Flag indicating appeal status |
| Original Ticket | Link to the appealed ticket   |
| Appeal Tickets  | List of appeals for a ticket  |

### Anonymous Complaints

For complaints without registered contact:

| Field            | Description                                           |
| ---------------- | ----------------------------------------------------- |
| Complainant Type | Beneficiary, Non-beneficiary, Staff, Anonymous, Other |
| Contact Name     | Alternative contact name                              |
| Contact Phone    | Alternative phone                                     |
| Contact Email    | Alternative email                                     |

## Integration

### Email Integration

Incoming emails automatically create tickets:

```
# Configuration via mail alias
Alias: complaints@yourdomain.org
Model: spp.grm.ticket
```

Replies to ticket notifications update the ticket.

### Portal Access

Beneficiaries can:

1. Submit new complaints
2. View their ticket status
3. Add comments to existing tickets
4. Receive status notifications

### With Programs

Link complaints to program participation:

- Complaints about entitlement amounts
- Service delivery issues
- Enrollment problems

### CEL-Based Escalation

When `spp_grm_cel` module is installed:

- Define escalation rules with CEL expressions
- Automatic routing based on ticket attributes
- Complex escalation workflows

## Are you stuck?

### Emails not creating tickets

**Symptom:** Emails sent to the GRM alias don't create tickets.

**Cause:** Mail alias may not be configured, or sender not recognized.

**Solution:**

1. Verify mail alias is configured in **Settings > Technical > Email > Aliases**
2. Check that incoming mail server is configured
3. Review mail logs for delivery issues
4. Note: By default, emails from unknown addresses notify sender that no ticket was created

### SLA showing wrong deadline

**Symptom:** SLA deadline doesn't match expected category settings.

**Cause:** Subcategory SLA overrides category SLA, or settings changed after ticket creation.

**Solution:**

1. Check subcategory SLA hours setting (takes precedence over category)
2. Verify category default SLA hours
3. Note: SLA is calculated at creation time; changes don't affect existing tickets

### Cannot close ticket

**Symptom:** Error when trying to move ticket to closed stage.

**Cause:** Stage may require decision or approval.

**Solution:**

1. If "Requires Decision" is set, select a decision value first
2. If "Requires Approval" is set, ensure you have supervisor permissions
3. Check that your user is in the stage's allowed groups

### Team assignment not working

**Symptom:** Tickets not automatically assigned to expected team.

**Cause:** Category-team mapping may be missing.

**Solution:**

1. Edit the ticket category
2. Set the "Default Team" field
3. New tickets will be assigned to this team
4. Existing tickets need manual reassignment
