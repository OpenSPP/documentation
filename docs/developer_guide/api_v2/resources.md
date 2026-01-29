---
openspp:
  doc_status: draft
  products: [core]
---

# API Resources

This guide is for **developers** working with OpenSPP API V2 resources.

## Available Resources

OpenSPP API V2 provides five core resources:

| Resource          | Description               | Endpoint             |
| ----------------- | ------------------------- | -------------------- |
| Individual        | Person in the registry    | `/Individual`        |
| Group             | Household or other group  | `/Group`             |
| Program           | Social protection program | `/Program`           |
| ProgramMembership | Enrollment in a program   | `/ProgramMembership` |
| Consent           | Data sharing consent      | `/Consent`           |

## Common Patterns

All resources follow consistent REST patterns:

| Operation        | HTTP Method | Endpoint                      | Supported Resources                  |
| ---------------- | ----------- | ----------------------------- | ------------------------------------ |
| Read             | GET         | `/{Resource}/{identifier}`    | All                                  |
| Search           | GET         | `/{Resource}?parameter=value` | All                                  |
| Create           | POST        | `/{Resource}`                 | Individual, Group, ProgramMembership |
| Update (full)    | PUT         | `/{Resource}/{identifier}`    | Individual, Group                    |
| Update (partial) | PATCH       | `/{Resource}/{identifier}`    | Group only                           |

## Individual Resource

Represents a person in the social protection registry.

### Data Model

```json
{
  "resourceType": "Individual",
  "identifier": [
    {
      "system": "urn:gov:ph:psa:national-id",
      "value": "PH-123456789"
    }
  ],
  "active": true,
  "name": {
    "family": "Santos",
    "given": "Maria",
    "middle": "Dela Cruz",
    "text": "SANTOS, Maria Dela Cruz"
  },
  "birthDate": "1985-03-15",
  "birthDateEstimated": false,
  "gender": {
    "coding": [
      {
        "system": "urn:iso:std:iso:5218",
        "code": "2",
        "display": "Female"
      }
    ],
    "text": "Female"
  },
  "telecom": [
    {
      "system": "phone",
      "value": "+639171234567",
      "use": "mobile",
      "rank": 1
    },
    {
      "system": "email",
      "value": "maria.santos@example.com",
      "use": "home"
    }
  ],
  "address": [
    {
      "type": "physical",
      "text": "123 Rizal St, Barangay 1, Manila",
      "line": ["123 Rizal St", "Barangay 1"],
      "city": "Manila",
      "state": "Metro Manila",
      "postalCode": "1000",
      "country": "PH"
    }
  ],
  "photo": "data:image/jpeg;base64,...",
  "groupMembership": [
    {
      "group": {
        "reference": "Group/urn:openspp:group|HH-2024-001",
        "display": "Santos Household"
      },
      "role": {
        "coding": [
          {
            "system": "urn:openspp:vocab:relationship",
            "code": "head",
            "display": "Head of Household"
          }
        ]
      },
      "period": {
        "start": "2024-01-01"
      }
    }
  ],
  "extension": {
    "farmer": {
      "url": "urn:openspp:extension:farmer",
      "farmSize": 2.5,
      "farmSizeUnit": "hectares",
      "primaryCrop": {
        "coding": [
          {
            "system": "urn:fao:agrovoc",
            "code": "rice",
            "display": "Rice"
          }
        ]
      }
    }
  },
  "meta": {
    "versionId": "3",
    "lastUpdated": "2024-11-28T10:30:00Z",
    "source": "urn:openspp:system:field-registration"
  }
}
```

### Field Reference

| Field                | Type            | Required | Description                              |
| -------------------- | --------------- | -------- | ---------------------------------------- |
| `resourceType`       | string          | Yes      | Always "Individual"                      |
| `identifier`         | array           | Yes      | External identifiers (at least one)      |
| `active`             | boolean         | No       | Whether record is active (default: true) |
| `name`               | object          | Yes      | Human name                               |
| `birthDate`          | date            | No       | Birth date (YYYY-MM-DD)                  |
| `birthDateEstimated` | boolean         | No       | Whether birth date is estimated          |
| `gender`             | CodeableConcept | No       | Gender (ISO 5218)                        |
| `telecom`            | array           | No       | Contact points (phone, email)            |
| `address`            | array           | No       | Physical/postal addresses                |
| `photo`              | string          | No       | Base64-encoded photo                     |
| `groupMembership`    | array           | No       | Group/household memberships              |
| `extension`          | object          | No       | Module-specific fields                   |
| `meta`               | object          | No       | Resource metadata                        |

### Operations

#### Read Individual

```http
GET /api/v2/spp/Individual/urn:gov:ph:psa:national-id|PH-123456789
Authorization: Bearer TOKEN
```

**Query Parameters:**

| Parameter     | Description                                                    |
| ------------- | -------------------------------------------------------------- |
| `_elements`   | Comma-separated fields to include: `identifier,name,birthDate` |
| `_extensions` | Extensions to include: `farmer,disability` or `*` for all      |

**Example: Python**

```python
def get_individual(identifier, token, base_url):
    """Fetch an individual by identifier."""
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(
        f"{base_url}/Individual/{identifier}",
        headers=headers
    )
    response.raise_for_status()
    return response.json()

# Usage
individual = get_individual(
    identifier="urn:gov:ph:psa:national-id|PH-123456789",
    token=token,
    base_url="https://api.openspp.org/api/v2/spp"
)
```

#### Create Individual

```http
POST /api/v2/spp/Individual
Authorization: Bearer TOKEN
Content-Type: application/json

{
  "resourceType": "Individual",
  "identifier": [
    {
      "system": "urn:gov:ph:psa:national-id",
      "value": "PH-987654321"
    }
  ],
  "name": {
    "given": "Juan",
    "family": "Dela Cruz"
  },
  "birthDate": "1990-05-15",
  "gender": {
    "coding": [
      {
        "system": "urn:iso:std:iso:5218",
        "code": "1",
        "display": "Male"
      }
    ]
  }
}
```

**Response:**

```http
HTTP/1.1 201 Created
Location: /api/v2/spp/Individual/urn:gov:ph:psa:national-id|PH-987654321
```

**Example: Python**

```python
def create_individual(data, token, base_url):
    """Create a new individual."""
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    response = requests.post(
        f"{base_url}/Individual",
        headers=headers,
        json=data
    )
    response.raise_for_status()
    return response.json()
```

#### Update Individual

```http
PUT /api/v2/spp/Individual/urn:gov:ph:psa:national-id|PH-123456789
Authorization: Bearer TOKEN
Content-Type: application/json
If-Match: "3"

{
  "resourceType": "Individual",
  "identifier": [...],
  "name": {...},
  ...
}
```

**Note:** Requires `If-Match` header with current version ID for optimistic locking.

## Group Resource

Represents a household or other group of individuals.

### Data Model

```json
{
  "resourceType": "Group",
  "identifier": [
    {
      "system": "urn:openspp:group",
      "value": "HH-2024-001"
    }
  ],
  "active": true,
  "type": "household",
  "name": "Santos Household",
  "quantity": 4,
  "member": [
    {
      "entity": {
        "reference": "Individual/urn:gov:ph:psa:national-id|PH-123456789",
        "display": "Maria Santos"
      },
      "role": {
        "coding": [
          {
            "system": "urn:openspp:vocab:relationship",
            "code": "head",
            "display": "Head"
          }
        ]
      },
      "period": {
        "start": "2024-01-01"
      },
      "inactive": false
    }
  ],
  "address": [
    {
      "type": "physical",
      "text": "123 Rizal St, Barangay 1, Manila",
      "city": "Manila",
      "state": "Metro Manila",
      "country": "PH"
    }
  ],
  "characteristic": [
    {
      "code": {
        "coding": [
          {
            "system": "urn:openspp:vocab:household-char",
            "code": "children_under_5",
            "display": "Children Under 5"
          }
        ]
      },
      "value": 2,
      "exclude": false
    }
  ],
  "meta": {
    "versionId": "5",
    "lastUpdated": "2024-11-28T10:30:00Z"
  }
}
```

### Operations

#### Search Groups

```http
GET /api/v2/spp/Group?type=household&name=Santos
Authorization: Bearer TOKEN
```

**Search Parameters:**

| Parameter      | Type      | Description                                       |
| -------------- | --------- | ------------------------------------------------- |
| `identifier`   | token     | System\|value                                     |
| `type`         | token     | Group type: `household`, `family`, `organization` |
| `name`         | string    | Group name (contains)                             |
| `member`       | reference | Has member: `Individual/{identifier}`             |
| `_lastUpdated` | date      | Modified since: `ge2024-01-01`                    |

**Example: Python**

```python
def search_groups(params, token, base_url):
    """Search for groups."""
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(
        f"{base_url}/Group",
        headers=headers,
        params=params
    )
    response.raise_for_status()
    return response.json()

# Usage
results = search_groups(
    params={"type": "household", "name": "Santos"},
    token=token,
    base_url="https://api.openspp.org/api/v2/spp"
)
```

#### Create Group

```http
POST /api/v2/spp/Group
Authorization: Bearer TOKEN
Content-Type: application/json

{
  "resourceType": "Group",
  "identifier": [
    {
      "system": "urn:openspp:group",
      "value": "HH-2024-NEW"
    }
  ],
  "type": "household",
  "name": "Dela Cruz Household",
  "member": [
    {
      "entity": {
        "reference": "Individual/urn:gov:ph:psa:national-id|PH-987654321"
      },
      "role": {
        "coding": [
          {
            "system": "urn:openspp:vocab:relationship",
            "code": "head"
          }
        ]
      }
    }
  ]
}
```

## Program Resource

Represents a social protection program.

### Data Model

```json
{
  "resourceType": "Program",
  "identifier": [
    {
      "system": "urn:openspp:program",
      "value": "4Ps"
    }
  ],
  "active": true,
  "name": "Pantawid Pamilyang Pilipino Program",
  "description": "Conditional cash transfer program for poor families",
  "type": {
    "coding": [
      {
        "system": "urn:openspp:vocab:program-type",
        "code": "cash_transfer",
        "display": "Cash Transfer"
      }
    ]
  },
  "targetType": "group",
  "eligibilityCriteria": "Households with children under 18 and income below poverty line",
  "period": {
    "start": "2008-02-01"
  },
  "meta": {
    "versionId": "1",
    "lastUpdated": "2024-01-01T00:00:00Z"
  }
}
```

### Operations

#### List Programs

```http
GET /api/v2/spp/Program?status=active
Authorization: Bearer TOKEN
```

**Example: Python**

```python
def list_programs(token, base_url):
    """List active programs."""
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(
        f"{base_url}/Program",
        headers=headers,
        params={"status": "active"}
    )
    response.raise_for_status()
    return response.json()
```

## ProgramMembership Resource

Represents enrollment of a beneficiary in a program.

### Data Model

```json
{
  "resourceType": "ProgramMembership",
  "identifier": [
    {
      "system": "urn:openspp:program-membership",
      "value": "4PS-2024-001234"
    }
  ],
  "program": {
    "reference": "Program/urn:openspp:program|4Ps",
    "display": "Pantawid Pamilyang Pilipino Program"
  },
  "beneficiary": {
    "reference": "Group/urn:openspp:group|HH-2024-001",
    "display": "Santos Household"
  },
  "status": "active",
  "enrollmentDate": "2024-01-15",
  "exitDate": null,
  "exitReason": null,
  "meta": {
    "versionId": "2",
    "lastUpdated": "2024-01-15T10:00:00Z"
  }
}
```

### Status Values

| Status      | Description                    |
| ----------- | ------------------------------ |
| `enrolled`  | Enrolled but not yet active    |
| `active`    | Actively receiving benefits    |
| `suspended` | Temporarily suspended          |
| `graduated` | Successfully completed program |
| `exited`    | Left program (see exitReason)  |

### Operations

#### Search Enrollments

```http
GET /api/v2/spp/ProgramMembership?beneficiary=Individual/urn:gov:ph:psa:national-id|PH-123456789&status=active
Authorization: Bearer TOKEN
```

**Search Parameters:**

| Parameter     | Type      | Description                   |
| ------------- | --------- | ----------------------------- |
| `beneficiary` | reference | Individual or Group reference |
| `program`     | reference | Program reference             |
| `status`      | token     | Enrollment status             |

**Example: Python**

```python
def get_program_memberships(beneficiary_ref, token, base_url):
    """Get program enrollments for a beneficiary."""
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(
        f"{base_url}/ProgramMembership",
        headers=headers,
        params={"beneficiary": beneficiary_ref, "status": "active"}
    )
    response.raise_for_status()
    return response.json()

# Usage
memberships = get_program_memberships(
    beneficiary_ref="Individual/urn:gov:ph:psa:national-id|PH-123456789",
    token=token,
    base_url="https://api.openspp.org/api/v2/spp"
)

for entry in memberships["entry"]:
    membership = entry["resource"]
    print(f"Enrolled in: {membership['program']['display']}")
    print(f"Status: {membership['status']}")
```

#### Enroll Beneficiary

```http
POST /api/v2/spp/ProgramMembership
Authorization: Bearer TOKEN
Content-Type: application/json

{
  "resourceType": "ProgramMembership",
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

## Extension Fields

Modules can add custom fields via extensions. Request extensions using the `_extensions` parameter:

```http
GET /api/v2/spp/Individual/...?_extensions=farmer,disability
```

### Available Extensions

Check the capability statement for available extensions:

```http
GET /api/v2/spp/metadata
```

Response includes:

```json
{
  "extension": [
    {
      "url": "urn:openspp:extension:farmer",
      "module": "spp_farmer_registry",
      "appliesTo": ["Individual"],
      "fields": ["farmSize", "farmSizeUnit", "primaryCrop", "livestockCount"]
    },
    {
      "url": "urn:openspp:extension:disability",
      "module": "spp_disability_registry",
      "appliesTo": ["Individual"],
      "fields": ["disabilityType", "severity", "assistanceNeeded"]
    }
  ]
}
```

### Using Extensions

```python
def get_individual_with_extensions(identifier, extensions, token, base_url):
    """Fetch individual with specific extensions."""
    headers = {"Authorization": f"Bearer {token}"}
    params = {"_extensions": ",".join(extensions)}

    response = requests.get(
        f"{base_url}/Individual/{identifier}",
        headers=headers,
        params=params
    )
    response.raise_for_status()
    return response.json()

# Usage
individual = get_individual_with_extensions(
    identifier="urn:gov:ph:psa:national-id|PH-123456789",
    extensions=["farmer"],
    token=token,
    base_url="https://api.openspp.org/api/v2/spp"
)

if "extension" in individual and "farmer" in individual["extension"]:
    farmer_data = individual["extension"]["farmer"]
    print(f"Farm size: {farmer_data['farmSize']} {farmer_data['farmSizeUnit']}")
```

## Resource Metadata

All resources include metadata:

```json
{
  "meta": {
    "versionId": "3",
    "lastUpdated": "2024-11-28T10:30:00Z",
    "source": "urn:openspp:system:field-registration"
  }
}
```

| Field         | Description                               |
| ------------- | ----------------------------------------- |
| `versionId`   | Version number for optimistic locking     |
| `lastUpdated` | Last modification timestamp (ISO 8601)    |
| `source`      | System that created/modified the resource |

### Version Control

Use the `versionId` for optimistic locking:

```http
PUT /api/v2/spp/Individual/...
If-Match: "3"
```

If another client modified the resource, you'll get a 409 Conflict:

```json
{
  "resourceType": "OperationOutcome",
  "issue": [
    {
      "severity": "error",
      "code": "conflict",
      "details": {
        "coding": [
          {
            "system": "urn:openspp:error",
            "code": "VERSION_CONFLICT"
          }
        ],
        "text": "Resource version mismatch. Expected: 3, Current: 5"
      }
    }
  ]
}
```

## Are You Stuck?

**Which resource should I use for households?**

Use the `Group` resource with `type: "household"`.

**Can I create a ProgramMembership without creating the Individual first?**

No. The beneficiary (Individual or Group) must exist before enrollment.

**How do I know which extensions are available?**

Check the capability statement: `GET /api/v2/spp/metadata`

**Getting 409 Conflict on updates?**

Another client modified the resource. Fetch the latest version, merge your changes, and retry with the new `versionId`.

**What's the difference between PUT and PATCH?**

PUT replaces the entire resource. PATCH applies partial updates using JSON Patch format.

## Complete Example: Full Workflow

```python
import requests

class OpenSPPAPI:
    """Complete API client example."""

    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token
        self.headers = {"Authorization": f"Bearer {token}"}

    def create_individual(self, identifier, name, birth_date):
        """Create a new individual."""
        data = {
            "resourceType": "Individual",
            "identifier": [identifier],
            "name": name,
            "birthDate": birth_date
        }
        response = requests.post(
            f"{self.base_url}/Individual",
            headers={**self.headers, "Content-Type": "application/json"},
            json=data
        )
        response.raise_for_status()
        return response.json()

    def create_group(self, identifier, name, members):
        """Create a new group."""
        data = {
            "resourceType": "Group",
            "identifier": [identifier],
            "type": "household",
            "name": name,
            "member": members
        }
        response = requests.post(
            f"{self.base_url}/Group",
            headers={**self.headers, "Content-Type": "application/json"},
            json=data
        )
        response.raise_for_status()
        return response.json()

    def enroll_in_program(self, program_ref, beneficiary_ref):
        """Enroll a beneficiary in a program."""
        data = {
            "resourceType": "ProgramMembership",
            "program": {"reference": program_ref},
            "beneficiary": {"reference": beneficiary_ref},
            "status": "enrolled",
            "enrollmentDate": "2024-11-28"
        }
        response = requests.post(
            f"{self.base_url}/ProgramMembership",
            headers={**self.headers, "Content-Type": "application/json"},
            json=data
        )
        response.raise_for_status()
        return response.json()

# Usage
api = OpenSPPAPI(
    base_url="https://api.openspp.org/api/v2/spp",
    token="YOUR_TOKEN"
)

# Create individual
individual = api.create_individual(
    identifier={"system": "urn:gov:ph:psa:national-id", "value": "PH-NEW-001"},
    name={"given": "Juan", "family": "Dela Cruz"},
    birth_date="1990-05-15"
)
print(f"Created individual: {individual['identifier'][0]['value']}")

# Create household
group = api.create_group(
    identifier={"system": "urn:openspp:group", "value": "HH-NEW-001"},
    name="Dela Cruz Household",
    members=[
        {
            "entity": {
                "reference": f"Individual/urn:gov:ph:psa:national-id|PH-NEW-001"
            },
            "role": {
                "coding": [
                    {"system": "urn:openspp:vocab:relationship", "code": "head"}
                ]
            }
        }
    ]
)
print(f"Created group: {group['identifier'][0]['value']}")

# Enroll in program
membership = api.enroll_in_program(
    program_ref="Program/urn:openspp:program|4Ps",
    beneficiary_ref=f"Group/urn:openspp:group|HH-NEW-001"
)
print(f"Enrolled in program: {membership['program']['display']}")
```

## Next Steps

- {doc}`search` - Advanced search and filtering
- {doc}`batch` - Create multiple resources atomically
- {doc}`consent` - Understanding consent-based access
- {doc}`errors` - Error handling

## See Also

- [FHIR Resource Types](https://www.hl7.org/fhir/resourcelist.html) - FHIR resource patterns
- [G2P Connect Resources](https://g2pconnect.cdpi.dev/protocol/resources) - G2P resource definitions
