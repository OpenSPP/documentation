---
openspp:
  doc_status: draft
  products: [core]
---

# Change Requests

**For: developers**

Create, review, and apply change requests via the API — including approval actions (approve, reject, revise).

```{warning}
**Known issue:** The `change_request:approve` and `change_request:apply` scopes are checked by the router but cannot be granted through the standard scope UI — the action selection in `spp_api_v2_change_request` does not include `approve` or `apply` as valid actions. Until this is fixed in the module code, calls to `$approve`, `$reject`, `$request-revision`, and `$apply` will return 403 even with seemingly correct scopes. Track this in the OpenSPP modules repo.
```

## Overview

The Change Request API (`spp_api_v2_change_request`) enables external systems to submit and manage data change requests with approval workflows. This is used for:

- **Field agent submissions** — Mobile apps submitting registrant updates
- **Self-service portals** — Beneficiaries requesting changes to their data
- **Batch corrections** — Automated systems submitting bulk data fixes
- **Integration pipelines** — External systems triggering data updates with audit trails

Change requests go through a defined workflow: draft → pending → approved → applied (or rejected/revision at any stage).

## Prerequisites

- Install `spp_api_v2_change_request` module
- API client with appropriate scopes:

| Scope | Permissions |
|-------|------------|
| `change_request:read` | View CRs and CR type schemas |
| `change_request:create` | Create new CRs |
| `change_request:update` | Edit draft CRs, submit, reset |
| `change_request:approve` | Approve, reject, request revision |
| `change_request:apply` | Apply approved CRs |

## Workflow

```
  ┌───────┐     ┌─────────┐     ┌──────────┐     ┌─────────┐
  │ Draft │────►│ Pending │────►│ Approved │────►│ Applied │
  └───────┘     └─────────┘     └──────────┘     └─────────┘
                    │                                  
                    ├──►  Rejected                     
                    │                                  
                    └──►  Revision ──► Draft           
```

## List CR Types

Discover what types of change requests are available.

```text
GET /api/v2/spp/ChangeRequest/$types
Authorization: Bearer TOKEN
```

**Response:**

```json
[
  {
    "code": "edit_individual",
    "name": "Edit Individual",
    "targetType": "res.partner",
    "applicantRequired": false
  },
  {
    "code": "add_household_member",
    "name": "Add Household Member",
    "targetType": "res.partner",
    "applicantRequired": true
  }
]
```

### Get CR Type Schema

Get the field schema for a specific CR type to know what data to include.

```text
GET /api/v2/spp/ChangeRequest/$types/edit_individual
Authorization: Bearer TOKEN
```

Returns field definitions with types, required flags, and constraints.

## Create Change Request

```text
POST /api/v2/spp/ChangeRequest
Authorization: Bearer TOKEN
Content-Type: application/json

{
  "type": "ChangeRequest",
  "requestType": {
    "code": "edit_individual",
    "name": "Edit Individual"
  },
  "registrant": {
    "system": "urn:gov:ph:psa:national-id",
    "value": "PH-123456789",
    "display": "Maria Santos"
  },
  "detail": {
    "given_name": "Maria",
    "family_name": "Santos-Cruz",
    "phone": "+639179876543"
  },
  "description": "Name change after marriage",
  "notes": "Supporting documents attached via portal"
}
```

**Response (201 Created):**

```json
{
  "reference": "CR/2024/00001",
  "type": "ChangeRequest",
  "requestType": {
    "code": "edit_individual",
    "name": "Edit Individual"
  },
  "registrant": {
    "system": "urn:gov:ph:psa:national-id",
    "value": "PH-123456789",
    "display": "Maria Santos"
  },
  "approvalState": "draft",
  "detail": {
    "given_name": "Maria",
    "family_name": "Santos-Cruz",
    "phone": "+639179876543"
  },
  "meta": {
    "versionId": "1",
    "lastUpdated": "2024-11-28T10:00:00Z"
  }
}
```

**Response headers:** `Location` with the CR reference URL.

**Example: Python**

```python
def create_change_request(cr_type, registrant_id, detail, token, base_url, description=None):
    """Create a new change request."""
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    body = {
        "type": "ChangeRequest",
        "requestType": {"code": cr_type},
        "registrant": registrant_id,
        "detail": detail
    }
    if description:
        body["description"] = description

    response = requests.post(
        f"{base_url}/ChangeRequest",
        headers=headers,
        json=body
    )
    response.raise_for_status()
    return response.json()

# Submit a name change request
cr = create_change_request(
    cr_type="edit_individual",
    registrant_id={
        "system": "urn:gov:ph:psa:national-id",
        "value": "PH-123456789"
    },
    detail={"family_name": "Santos-Cruz", "phone": "+639179876543"},
    description="Name change after marriage",
    token=token,
    base_url=base_url
)
print(f"Created CR: {cr['reference']} (state: {cr['approvalState']})")
```

## Read Change Request

```text
GET /api/v2/spp/ChangeRequest/CR/2024/00001
Authorization: Bearer TOKEN
```

**Response headers:** `ETag` for optimistic locking on updates.

## Search Change Requests

```text
GET /api/v2/spp/ChangeRequest?registrant=urn:gov:ph:psa:national-id|PH-123456789&status=pending
Authorization: Bearer TOKEN
```

**Query parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `registrant` | string | Registrant identifier (`system\|value`) |
| `requestType` | string | CR type code |
| `status` | string | `draft`, `pending`, `revision`, `approved`, `rejected`, `applied` |
| `createdAfter` | date | Created after date |
| `createdBefore` | date | Created before date |
| `_count` | integer | Results per page (1-100, default 20) |
| `_offset` | integer | Skip N results (default 0) |

## Update Change Request

Update the detail fields of a draft CR.

```text
PUT /api/v2/spp/ChangeRequest/CR/2024/00001
Authorization: Bearer TOKEN
Content-Type: application/json
If-Match: "1"

{
  "detail": {
    "given_name": "Maria",
    "family_name": "Santos-Cruz",
    "phone": "+639179876543"
  }
}
```

Only draft CRs can be updated. Returns 409 Conflict if the CR is not in draft state or the version doesn't match.

## Workflow Actions

### Submit for Approval

Move a draft CR to pending review.

```text
POST /api/v2/spp/ChangeRequest/CR/2024/00001/$submit
Authorization: Bearer TOKEN
```

### Approve

Approve a pending CR.

```text
POST /api/v2/spp/ChangeRequest/CR/2024/00001/$approve
Authorization: Bearer TOKEN
Content-Type: application/json

{
  "comment": "Verified supporting documents"
}
```

### Reject

Reject a pending CR with a reason.

```text
POST /api/v2/spp/ChangeRequest/CR/2024/00001/$reject
Authorization: Bearer TOKEN
Content-Type: application/json

{
  "reason": "Missing required identification documents"
}
```

### Request Revision

Send a pending CR back for revision.

```text
POST /api/v2/spp/ChangeRequest/CR/2024/00001/$request-revision
Authorization: Bearer TOKEN
Content-Type: application/json

{
  "notes": "Please provide updated phone number and verify address"
}
```

### Apply

Execute an approved CR — applies the changes to the registrant record.

```text
POST /api/v2/spp/ChangeRequest/CR/2024/00001/$apply
Authorization: Bearer TOKEN
```

### Reset

Reset a rejected or revision CR back to draft.

```text
POST /api/v2/spp/ChangeRequest/CR/2024/00001/$reset
Authorization: Bearer TOKEN
```

## Complete Workflow Example

```python
import requests

class ChangeRequestClient:
    """Client for the change request workflow."""

    def __init__(self, base_url, token):
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def create(self, cr_type, registrant_id, detail, description=None):
        """Create a draft CR."""
        body = {
            "type": "ChangeRequest",
            "requestType": {"code": cr_type},
            "registrant": registrant_id,
            "detail": detail
        }
        if description:
            body["description"] = description
        resp = requests.post(f"{self.base_url}/ChangeRequest", headers=self.headers, json=body)
        resp.raise_for_status()
        return resp.json()

    def submit(self, reference):
        """Submit a draft CR for approval."""
        resp = requests.post(f"{self.base_url}/ChangeRequest/{reference}/$submit", headers=self.headers)
        resp.raise_for_status()
        return resp.json()

    def approve(self, reference, comment=None):
        """Approve a pending CR."""
        body = {"comment": comment} if comment else {}
        resp = requests.post(f"{self.base_url}/ChangeRequest/{reference}/$approve", headers=self.headers, json=body)
        resp.raise_for_status()
        return resp.json()

    def apply(self, reference):
        """Apply an approved CR."""
        resp = requests.post(f"{self.base_url}/ChangeRequest/{reference}/$apply", headers=self.headers)
        resp.raise_for_status()
        return resp.json()

# Full workflow
client = ChangeRequestClient(base_url=base_url, token=token)

# 1. Create
cr = client.create(
    cr_type="edit_individual",
    registrant_id={"system": "urn:gov:ph:psa:national-id", "value": "PH-123456789"},
    detail={"family_name": "Santos-Cruz"},
    description="Name change after marriage"
)
ref = cr["reference"]
print(f"Created: {ref}")

# 2. Submit for approval
cr = client.submit(ref)
print(f"Submitted: {cr['approvalState']}")

# 3. Approve (typically done by a different user/system)
cr = client.approve(ref, comment="Documents verified")
print(f"Approved: {cr['approvalState']}")

# 4. Apply changes to registrant
cr = client.apply(ref)
print(f"Applied: {cr['approvalState']}")
```

## Common mistakes

**Getting 409 Conflict on submit?**

The CR may not be in draft state. Check the current `approvalState` before attempting workflow actions.

**How do I know what fields to include in `detail`?**

Use `GET /ChangeRequest/$types/{code}` to get the field schema for a CR type.

**Can I approve and apply in one step?**

No. Approve and apply are separate actions to support multi-step approval workflows.

**CR reference format?**

References use the format `CR/YYYY/NNNNN` (e.g., `CR/2024/00001`). Include all three path segments in the URL.

**Who can approve/reject?**

Only API clients with the `change_request:approve` scope. Typically a different client than the one that created the CR.

## What's next

- {doc}`resources` - Core API resources
- {doc}`batch` - Batch operations for bulk CR creation
- {doc}`errors` - Error handling

## See also

- {doc}`overview` - API V2 design principles
- {doc}`authentication` - OAuth 2.0 setup and scopes
- {doc}`external_identifiers` - Identifier format for registrant references
