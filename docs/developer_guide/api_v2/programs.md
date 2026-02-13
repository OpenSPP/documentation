---
openspp:
  doc_status: draft
  products: [core]
---

# Programs and Enrollments

This guide covers querying social protection programs and managing beneficiary enrollments through program memberships.

## Overview

Programs are managed through the OpenSPP admin interface. The API provides **read-only** access to programs and **full CRUD** for program memberships (enrollments).

### Program Endpoints

| Operation | Method | Endpoint | Scope Required |
|-----------|--------|----------|----------------|
| Search programs | GET | `/Program` | `program:read` |
| Read program | GET | `/Program/{identifier}` | `program:read` |

### ProgramMembership Endpoints

| Operation | Method | Endpoint | Scope Required |
|-----------|--------|----------|----------------|
| Search enrollments | GET | `/ProgramMembership` | `program_membership:read` |
| Read enrollment | GET | `/ProgramMembership/{identifier}` | `program_membership:read` |
| Create enrollment | POST | `/ProgramMembership` | `program_membership:create` |
| Update enrollment | PUT | `/ProgramMembership/{identifier}` | `program_membership:update` |

### Enrollment Status Values

| Status | Description |
|--------|-------------|
| `draft` | Enrollment request created but not yet processed |
| `enrolled` | Actively enrolled in the program |
| `paused` | Enrollment temporarily suspended |
| `exited` | Left the program |
| `not_eligible` | Determined not eligible for the program |
| `duplicated` | Duplicate enrollment detected |

```{note}
Program search uses cursor-based pagination with `_lastId` instead of `_offset`.
```

## Create an Enrollment

`````{tab-set}

````{tab-item} HTTP
```http
POST /api/v2/spp/ProgramMembership
Authorization: Bearer {token}
Content-Type: application/json

{
  "type": "ProgramMembership",
  "program": {
    "reference": "Program/urn:openspp:program|4Ps"
  },
  "beneficiary": {
    "reference": "Group/urn:openspp:group|HH-2024-001"
  },
  "status": "enrolled",
  "enrollmentDate": "2024-11-28"
}
```
````

````{tab-item} cURL
```bash
curl -X POST https://api.openspp.org/api/v2/spp/ProgramMembership \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "type": "ProgramMembership",
    "program": {
      "reference": "Program/urn:openspp:program|4Ps"
    },
    "beneficiary": {
      "reference": "Group/urn:openspp:group|HH-2024-001"
    },
    "status": "enrolled",
    "enrollmentDate": "2024-11-28"
  }'
```
````

````{tab-item} Python
```python
import requests

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}
data = {
    "type": "ProgramMembership",
    "program": {"reference": "Program/urn:openspp:program|4Ps"},
    "beneficiary": {"reference": "Group/urn:openspp:group|HH-2024-001"},
    "status": "enrolled",
    "enrollmentDate": "2024-11-28"
}
response = requests.post(
    f"{base_url}/ProgramMembership",
    headers=headers,
    json=data
)
response.raise_for_status()
enrollment = response.json()
print(f"Enrollment created: {enrollment['status']}")
```
````

````{tab-item} JavaScript
```javascript
const data = {
  type: "ProgramMembership",
  program: { reference: "Program/urn:openspp:program|4Ps" },
  beneficiary: { reference: "Group/urn:openspp:group|HH-2024-001" },
  status: "enrolled",
  enrollmentDate: "2024-11-28"
};
const response = await fetch(`${baseUrl}/ProgramMembership`, {
  method: "POST",
  headers: {
    "Authorization": `Bearer ${token}`,
    "Content-Type": "application/json"
  },
  body: JSON.stringify(data)
});
const enrollment = await response.json();
console.log(`Enrollment created: ${enrollment.status}`);
```
````

`````

## Next Steps

- {doc}`individuals` -- Manage individual registrants
- {doc}`groups` -- Manage households and group membership
- {doc}`batch` -- Create enrollments alongside individuals and groups
