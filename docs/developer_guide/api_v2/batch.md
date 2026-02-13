---
openspp:
  doc_status: draft
  products: [core]
---

# Batch Operations

This guide is for **developers** implementing batch and transaction operations with OpenSPP API V2.

## Why Use Batch Operations?

Batch operations allow you to:

- **Create multiple resources** in a single request
- **Ensure atomicity**: All operations succeed or all fail
- **Improve performance**: Reduce network overhead
- **Maintain data consistency**: Create related resources together

## Bundle Types

OpenSPP API V2 supports two bundle types:

| Type | Description | Atomicity | Use Case |
|------|-------------|-----------|----------|
| `transaction` | All-or-nothing | Full rollback on any failure | Creating related records |
| `batch` | Independent operations | Partial success allowed | Bulk imports |

## Transaction Bundles

Transaction bundles process operations atomically. If any operation fails, all changes are rolled back.

### Use Cases

- Register individual + household + program enrollment
- Create group with multiple members
- Update multiple related records
- Import form submissions with dependencies

### Basic Structure

`````{tab-set}

````{tab-item} HTTP
```http
POST /api/v2/spp/$batch
Authorization: Bearer TOKEN
Content-Type: application/json

{
  "resourceType": "Bundle",
  "type": "transaction",
  "entry": [
    {
      "request": {
        "method": "POST",
        "url": "Individual"
      },
      "resource": { /* Individual data */ }
    },
    {
      "request": {
        "method": "POST",
        "url": "Group"
      },
      "resource": { /* Group data */ }
    }
  ]
}
```
````

````{tab-item} cURL
```bash
curl -X POST https://api.openspp.org/api/v2/spp/\$batch \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "resourceType": "Bundle",
    "type": "transaction",
    "entry": [
      {
        "request": {"method": "POST", "url": "Individual"},
        "resource": { ... }
      },
      {
        "request": {"method": "POST", "url": "Group"},
        "resource": { ... }
      }
    ]
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
bundle = {
    "resourceType": "Bundle",
    "type": "transaction",
    "entry": [
        {
            "request": {"method": "POST", "url": "Individual"},
            "resource": { ... }
        },
        {
            "request": {"method": "POST", "url": "Group"},
            "resource": { ... }
        }
    ]
}
response = requests.post(
    f"{base_url}/$batch",
    headers=headers,
    json=bundle
)
response.raise_for_status()
result = response.json()
```
````

````{tab-item} JavaScript
```javascript
const bundle = {
  resourceType: "Bundle",
  type: "transaction",
  entry: [
    {
      request: { method: "POST", url: "Individual" },
      resource: { /* ... */ }
    },
    {
      request: { method: "POST", url: "Group" },
      resource: { /* ... */ }
    }
  ]
};
const response = await fetch(`${baseUrl}/$batch`, {
  method: "POST",
  headers: {
    "Authorization": `Bearer ${token}`,
    "Content-Type": "application/json"
  },
  body: JSON.stringify(bundle)
});
const result = await response.json();
```
````

`````

### Example: Register Household

Create an individual, add them to a household, and enroll in a program:

```http
POST /api/v2/spp/$batch
Authorization: Bearer TOKEN
Content-Type: application/json

{
  "resourceType": "Bundle",
  "type": "transaction",
  "entry": [
    {
      "fullUrl": "urn:uuid:individual-1",
      "request": {
        "method": "POST",
        "url": "Individual"
      },
      "resource": {
        "resourceType": "Individual",
        "identifier": [
          {
            "system": "urn:gov:ph:psa:national-id",
            "value": "PH-NEW-001"
          }
        ],
        "name": {
          "given": "Maria",
          "family": "Santos"
        },
        "birthDate": "1985-03-15",
        "gender": {
          "coding": [
            {
              "system": "urn:iso:std:iso:5218",
              "code": "2"
            }
          ]
        }
      }
    },
    {
      "fullUrl": "urn:uuid:group-1",
      "request": {
        "method": "POST",
        "url": "Group"
      },
      "resource": {
        "resourceType": "Group",
        "identifier": [
          {
            "system": "urn:openspp:group",
            "value": "HH-NEW-001"
          }
        ],
        "type": "household",
        "name": "Santos Household",
        "member": [
          {
            "entity": {
              "reference": "urn:uuid:individual-1"
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
    },
    {
      "request": {
        "method": "POST",
        "url": "ProgramMembership"
      },
      "resource": {
        "resourceType": "ProgramMembership",
        "program": {
          "reference": "Program/urn:openspp:program|4Ps"
        },
        "beneficiary": {
          "reference": "urn:uuid:group-1"
        },
        "status": "enrolled",
        "enrollmentDate": "2024-11-28"
      }
    }
  ]
}
```

### Response

```json
{
  "resourceType": "Bundle",
  "type": "transaction-response",
  "entry": [
    {
      "fullUrl": "urn:uuid:individual-1",
      "response": {
        "status": "201 Created",
        "location": "/api/v2/spp/Individual/urn:gov:ph:psa:national-id|PH-NEW-001",
        "etag": "1"
      },
      "resource": { /* Created Individual */ }
    },
    {
      "fullUrl": "urn:uuid:group-1",
      "response": {
        "status": "201 Created",
        "location": "/api/v2/spp/Group/urn:openspp:group|HH-NEW-001",
        "etag": "1"
      },
      "resource": { /* Created Group with resolved reference */ }
    },
    {
      "response": {
        "status": "201 Created",
        "location": "/api/v2/spp/ProgramMembership/urn:openspp:program-membership|..."
      }
    }
  ]
}
```

## Placeholder References

Use `fullUrl` with `urn:uuid:*` to create temporary IDs for cross-references:

```json
{
  "fullUrl": "urn:uuid:temp-individual",
  "resource": {
    "resourceType": "Individual",
    ...
  }
}
```

Reference the placeholder in subsequent entries:

```json
{
  "resource": {
    "resourceType": "Group",
    "member": [
      {
        "entity": {
          "reference": "urn:uuid:temp-individual"
        }
      }
    ]
  }
}
```

The server resolves placeholders to actual identifiers during processing.

## Python Implementation

### Basic Transaction

```python
import requests
from typing import List, Dict

def create_transaction_bundle(entries: List[Dict]) -> Dict:
    """Create a transaction bundle."""
    return {
        "resourceType": "Bundle",
        "type": "transaction",
        "entry": entries
    }

def submit_transaction(bundle: Dict, token: str, base_url: str) -> Dict:
    """Submit a transaction bundle."""
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    response = requests.post(
        f"{base_url}/$batch",
        headers=headers,
        json=bundle
    )
    response.raise_for_status()
    return response.json()

# Usage
entries = [
    {
        "fullUrl": "urn:uuid:ind-1",
        "request": {"method": "POST", "url": "Individual"},
        "resource": {
            "resourceType": "Individual",
            "identifier": [{"system": "urn:gov:ph:psa:national-id", "value": "PH-001"}],
            "name": {"given": "Maria", "family": "Santos"}
        }
    },
    {
        "request": {"method": "POST", "url": "Group"},
        "resource": {
            "resourceType": "Group",
            "identifier": [{"system": "urn:openspp:group", "value": "HH-001"}],
            "type": "household",
            "name": "Santos Household",
            "member": [
                {
                    "entity": {"reference": "urn:uuid:ind-1"},
                    "role": {"coding": [{"system": "urn:openspp:vocab:relationship", "code": "head"}]}
                }
            ]
        }
    }
]

bundle = create_transaction_bundle(entries)
result = submit_transaction(bundle, token, base_url)

print(f"Transaction completed: {len(result['entry'])} resources created")
```

### Helper Class

```python
import uuid
from typing import Optional

class TransactionBuilder:
    """Build transaction bundles with automatic placeholder management."""

    def __init__(self):
        self.entries = []
        self.placeholders = {}

    def add_individual(
        self,
        identifier: Dict,
        name: Dict,
        birth_date: Optional[str] = None,
        gender: Optional[Dict] = None,
        placeholder: Optional[str] = None
    ) -> str:
        """
        Add an individual to the transaction.

        Args:
            identifier: Identifier dict
            name: Name dict
            birth_date: Birth date (YYYY-MM-DD)
            gender: Gender CodeableConcept
            placeholder: Custom placeholder ID (auto-generated if not provided)

        Returns:
            Placeholder UUID for referencing
        """
        if placeholder is None:
            placeholder = f"urn:uuid:{uuid.uuid4()}"

        resource = {
            "resourceType": "Individual",
            "identifier": [identifier],
            "name": name
        }

        if birth_date:
            resource["birthDate"] = birth_date
        if gender:
            resource["gender"] = gender

        self.entries.append({
            "fullUrl": placeholder,
            "request": {"method": "POST", "url": "Individual"},
            "resource": resource
        })

        self.placeholders[placeholder] = resource
        return placeholder

    def add_group(
        self,
        identifier: Dict,
        name: str,
        members: List[Dict],
        placeholder: Optional[str] = None
    ) -> str:
        """
        Add a group to the transaction.

        Args:
            identifier: Identifier dict
            name: Group name
            members: List of member dicts with 'reference' and 'role'
            placeholder: Custom placeholder ID

        Returns:
            Placeholder UUID
        """
        if placeholder is None:
            placeholder = f"urn:uuid:{uuid.uuid4()}"

        resource = {
            "resourceType": "Group",
            "identifier": [identifier],
            "type": "household",
            "name": name,
            "member": members
        }

        self.entries.append({
            "fullUrl": placeholder,
            "request": {"method": "POST", "url": "Group"},
            "resource": resource
        })

        return placeholder

    def add_program_membership(
        self,
        program_ref: str,
        beneficiary_ref: str,
        status: str = "enrolled",
        enrollment_date: Optional[str] = None
    ):
        """Add a program membership to the transaction."""
        resource = {
            "resourceType": "ProgramMembership",
            "program": {"reference": program_ref},
            "beneficiary": {"reference": beneficiary_ref},
            "status": status
        }

        if enrollment_date:
            resource["enrollmentDate"] = enrollment_date

        self.entries.append({
            "request": {"method": "POST", "url": "ProgramMembership"},
            "resource": resource
        })

    def build(self) -> Dict:
        """Build the transaction bundle."""
        return {
            "resourceType": "Bundle",
            "type": "transaction",
            "entry": self.entries
        }

# Usage
builder = TransactionBuilder()

# Add individual
ind_ref = builder.add_individual(
    identifier={"system": "urn:gov:ph:psa:national-id", "value": "PH-NEW-001"},
    name={"given": "Maria", "family": "Santos"},
    birth_date="1985-03-15",
    gender={"coding": [{"system": "urn:iso:std:iso:5218", "code": "2"}]}
)

# Add household with the individual
group_ref = builder.add_group(
    identifier={"system": "urn:openspp:group", "value": "HH-NEW-001"},
    name="Santos Household",
    members=[
        {
            "entity": {"reference": ind_ref},
            "role": {"coding": [{"system": "urn:openspp:vocab:relationship", "code": "head"}]}
        }
    ]
)

# Enroll in program
builder.add_program_membership(
    program_ref="Program/urn:openspp:program|4Ps",
    beneficiary_ref=group_ref,
    enrollment_date="2024-11-28"
)

# Submit
bundle = builder.build()
result = submit_transaction(bundle, token, base_url)

print(f"Created {len(result['entry'])} resources")
```

## Batch Bundles

Batch bundles process operations independently. Some can succeed while others fail.

### Use Case

- Bulk import from CSV
- Update multiple unrelated records
- Create resources that don't depend on each other

### Structure

```json
{
  "resourceType": "Bundle",
  "type": "batch",
  "entry": [
    {
      "request": {"method": "POST", "url": "Individual"},
      "resource": { /* Individual 1 */ }
    },
    {
      "request": {"method": "POST", "url": "Individual"},
      "resource": { /* Individual 2 */ }
    },
    {
      "request": {"method": "POST", "url": "Individual"},
      "resource": { /* Individual 3 */ }
    }
  ]
}
```

### Response with Partial Failure

```json
{
  "resourceType": "Bundle",
  "type": "batch-response",
  "entry": [
    {
      "response": {
        "status": "201 Created",
        "location": "/api/v2/spp/Individual/..."
      }
    },
    {
      "response": {
        "status": "422 Unprocessable Entity",
        "outcome": {
          "resourceType": "OperationOutcome",
          "issue": [
            {
              "severity": "error",
              "code": "invalid",
              "details": {
                "text": "Duplicate identifier"
              }
            }
          ]
        }
      }
    },
    {
      "response": {
        "status": "201 Created",
        "location": "/api/v2/spp/Individual/..."
      }
    }
  ]
}
```

### Python Implementation

```python
def create_batch_bundle(resources: List[Dict]) -> Dict:
    """Create a batch bundle for independent operations."""
    entries = []

    for resource in resources:
        entries.append({
            "request": {"method": "POST", "url": resource["resourceType"]},
            "resource": resource
        })

    return {
        "resourceType": "Bundle",
        "type": "batch",
        "entry": entries
    }

def submit_batch(bundle: Dict, token: str, base_url: str) -> Dict:
    """Submit a batch bundle."""
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    response = requests.post(
        f"{base_url}/$batch",
        headers=headers,
        json=bundle
    )
    response.raise_for_status()
    return response.json()

# Usage: Bulk import individuals
individuals = [
    {
        "resourceType": "Individual",
        "identifier": [{"system": "urn:gov:ph:psa:national-id", "value": f"PH-{i:06d}"}],
        "name": {"given": f"Person{i}", "family": "Test"}
    }
    for i in range(1, 101)
]

bundle = create_batch_bundle(individuals)
result = submit_batch(bundle, token, base_url)

# Check results
success_count = sum(1 for entry in result["entry"] if entry["response"]["status"].startswith("20"))
error_count = len(result["entry"]) - success_count

print(f"Success: {success_count}, Errors: {error_count}")
```

## Mixed Operations

Bundles can include different HTTP methods:

```json
{
  "resourceType": "Bundle",
  "type": "transaction",
  "entry": [
    {
      "request": {"method": "POST", "url": "Individual"},
      "resource": { /* Create individual */ }
    },
    {
      "request": {
        "method": "PUT",
        "url": "Individual/urn:gov:ph:psa:national-id|PH-123",
        "ifMatch": "3"
      },
      "resource": { /* Update individual */ }
    },
    {
      "request": {
        "method": "GET",
        "url": "Program/urn:openspp:program|4Ps"
      }
    }
  ]
}
```

**Supported methods:**
- `POST` - Create
- `PUT` - Update (full)
- `GET` - Read
- `DELETE` - Delete (soft delete)

## Error Handling

### Transaction Failure

If any operation in a transaction fails, the entire bundle fails:

```json
{
  "resourceType": "OperationOutcome",
  "issue": [
    {
      "severity": "error",
      "code": "transaction-failed",
      "details": {
        "coding": [
          {
            "system": "urn:openspp:error",
            "code": "TRANSACTION_FAILED"
          }
        ],
        "text": "Transaction failed at entry[1]: Duplicate identifier"
      },
      "diagnostics": "Entry 1 (Group): Identifier urn:openspp:group|HH-001 already exists"
    }
  ]
}
```

### Handling Errors in Python

```python
def submit_transaction_with_retry(bundle: Dict, token: str, base_url: str, max_retries: int = 3):
    """Submit transaction with retry logic."""
    for attempt in range(max_retries):
        try:
            result = submit_transaction(bundle, token, base_url)
            return result
        except requests.HTTPError as e:
            if e.response.status_code == 409:  # Conflict
                print(f"Conflict detected, attempt {attempt + 1}/{max_retries}")
                if attempt < max_retries - 1:
                    # Optionally update identifiers and retry
                    continue
            elif e.response.status_code == 422:  # Validation error
                print(f"Validation error: {e.response.json()}")
                raise  # Don't retry validation errors
            raise
    raise Exception("Transaction failed after max retries")

# Usage
try:
    result = submit_transaction_with_retry(bundle, token, base_url)
    print("Transaction succeeded")
except Exception as e:
    print(f"Transaction failed: {e}")
```

## Performance Considerations

### Batch Size

Recommended batch sizes:

| Operation | Recommended Size | Maximum |
|-----------|------------------|---------|
| Transaction (related) | 10-20 resources | 50 |
| Batch (independent) | 50-100 resources | 500 |

### Chunking Large Imports

```python
def chunk_list(items: List, chunk_size: int) -> List[List]:
    """Split list into chunks."""
    return [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]

def bulk_import_individuals(individuals: List[Dict], token: str, base_url: str, chunk_size: int = 100):
    """Import individuals in chunks."""
    chunks = chunk_list(individuals, chunk_size)
    results = []

    for i, chunk in enumerate(chunks, 1):
        print(f"Processing chunk {i}/{len(chunks)}...")
        bundle = create_batch_bundle(chunk)
        result = submit_batch(bundle, token, base_url)
        results.append(result)

    # Summarize results
    total_success = sum(
        sum(1 for entry in result["entry"] if entry["response"]["status"].startswith("20"))
        for result in results
    )
    total_errors = sum(len(result["entry"]) for result in results) - total_success

    print(f"Import complete: {total_success} success, {total_errors} errors")
    return results

# Usage: Import 1000 individuals in chunks of 100
individuals = load_individuals_from_csv("data.csv")  # Your data loading function
results = bulk_import_individuals(individuals, token, base_url, chunk_size=100)
```

## Complete Example: CSV Import

```python
import csv
import requests
from typing import List, Dict

class BulkImporter:
    """Import data from CSV using batch operations."""

    def __init__(self, base_url: str, token: str):
        self.base_url = base_url
        self.token = token
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def load_csv(self, filepath: str) -> List[Dict]:
        """Load individuals from CSV."""
        individuals = []

        with open(filepath, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                individuals.append({
                    "resourceType": "Individual",
                    "identifier": [
                        {
                            "system": "urn:gov:ph:psa:national-id",
                            "value": row["national_id"]
                        }
                    ],
                    "name": {
                        "given": row["given_name"],
                        "family": row["family_name"]
                    },
                    "birthDate": row["birth_date"],
                    "gender": {
                        "coding": [
                            {
                                "system": "urn:iso:std:iso:5218",
                                "code": row["gender_code"]
                            }
                        ]
                    }
                })

        return individuals

    def import_batch(self, resources: List[Dict], chunk_size: int = 100):
        """Import resources in batches."""
        chunks = [resources[i:i + chunk_size] for i in range(0, len(resources), chunk_size)]

        total_success = 0
        total_errors = 0
        errors = []

        for i, chunk in enumerate(chunks, 1):
            print(f"Processing batch {i}/{len(chunks)}...")

            bundle = {
                "resourceType": "Bundle",
                "type": "batch",
                "entry": [
                    {
                        "request": {"method": "POST", "url": "Individual"},
                        "resource": resource
                    }
                    for resource in chunk
                ]
            }

            try:
                response = requests.post(
                    f"{self.base_url}/$batch",
                    headers=self.headers,
                    json=bundle
                )
                response.raise_for_status()
                result = response.json()

                # Count successes and errors
                for j, entry in enumerate(result["entry"]):
                    if entry["response"]["status"].startswith("20"):
                        total_success += 1
                    else:
                        total_errors += 1
                        errors.append({
                            "batch": i,
                            "index": j,
                            "resource": chunk[j],
                            "error": entry["response"].get("outcome", {})
                        })

            except requests.HTTPError as e:
                print(f"Batch {i} failed: {e}")
                total_errors += len(chunk)
                errors.append({
                    "batch": i,
                    "error": str(e)
                })

        print(f"\nImport complete:")
        print(f"  Success: {total_success}")
        print(f"  Errors: {total_errors}")

        return {
            "success": total_success,
            "errors": total_errors,
            "error_details": errors
        }

# Usage
importer = BulkImporter(
    base_url="https://api.openspp.org/api/v2/spp",
    token=token
)

# Load from CSV
individuals = importer.load_csv("individuals.csv")
print(f"Loaded {len(individuals)} individuals from CSV")

# Import in batches
result = importer.import_batch(individuals, chunk_size=100)

# Report errors
if result["errors"] > 0:
    print("\nErrors occurred:")
    for error in result["error_details"][:10]:  # Show first 10
        print(f"  Batch {error.get('batch')}, Index {error.get('index')}: {error['error']}")
```

## Are You Stuck?

**Transaction failing with "reference not found"?**

Ensure placeholders (`urn:uuid:*`) are defined before they're referenced. The order of entries matters.

**Getting timeout errors?**

Reduce batch size. Very large transactions can timeout. Split into smaller batches.

**Some resources created despite transaction failure?**

This shouldn't happen with transactions. If it does, report it as a bug. Transactions should rollback completely.

**How do I update multiple resources atomically?**

Use a transaction bundle with `PUT` requests. Include `If-Match` headers with version IDs.

**Can I mix creates and updates in one transaction?**

Yes. Use `POST` for creates, `PUT` for updates in the same transaction.

## Next Steps

- {doc}`resources` - Learn about available resources
- {doc}`errors` - Complete error handling guide
- {doc}`search` - Finding existing resources
- {doc}`authentication` - OAuth 2.0 setup

## See Also

- [FHIR Bundle](https://www.hl7.org/fhir/bundle.html) - FHIR bundle specification
- [HTTP Batch Processing](https://datatracker.ietf.org/doc/html/rfc7233) - HTTP batch patterns
