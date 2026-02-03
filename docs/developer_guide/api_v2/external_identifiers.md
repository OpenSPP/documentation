---
openspp:
  doc_status: draft
  products: [core]
---

# External Identifiers

This guide is for **developers** working with OpenSPP's external identifier system.

## Why External Identifiers?

**OpenSPP API V2 never exposes internal database IDs.** Instead, all resources use external identifiers with namespace URIs.

### The Problem with Database IDs

```json
// ❌ WRONG - Database ID exposed
{
  "id": 12345,
  "name": "Maria Santos"
}
```

**Issues:**
- Database IDs leak internal implementation details
- IDs can change during database migrations or merges
- No way to identify the ID system (National ID? Voter ID? Internal?)
- Security risk: sequential IDs are predictable
- Data sovereignty: external systems shouldn't reference internal IDs

### The Solution: Namespaced External IDs

```json
// ✅ CORRECT - External identifier with namespace
{
  "identifier": [
    {
      "system": "urn:gov:ph:psa:national-id",
      "value": "PH-123456789"
    }
  ],
  "name": {
    "given": "Maria",
    "family": "Santos"
  }
}
```

**Benefits:**
- Unambiguous: The namespace tells you what kind of ID this is
- Portable: IDs work across systems and migrations
- Multiple IDs: One person can have many identifiers
- Standards-aligned: Compatible with G2P Connect, FHIR, DCI

## Identifier Structure

Every identifier has two required fields:

```json
{
  "system": "urn:gov:ph:psa:national-id",
  "value": "PH-123456789"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `system` | string (required) | Namespace URI identifying the ID system |
| `value` | string (required) | The actual identifier value |
| `period` | object (optional) | Time period when identifier is/was valid |

### Namespace URI Format

Namespaces use URN (Uniform Resource Name) format:

```
urn:{authority}:{path}
```

**Examples:**

| Type | Namespace URI |
|------|---------------|
| Philippine National ID | `urn:gov:ph:psa:national-id` |
| Philippine PhilHealth | `urn:gov:ph:philhealth` |
| Kenya National ID | `urn:gov:ke:nira:national-id` |
| OpenSPP Internal | `urn:openspp:registry:individual` |
| ISO Gender Code | `urn:iso:std:iso:5218` |
| FAO Crop Vocabulary | `urn:fao:agrovoc` |

### Multiple Identifiers

A person typically has multiple identifiers:

```json
{
  "resourceType": "Individual",
  "identifier": [
    {
      "system": "urn:gov:ph:psa:national-id",
      "value": "PH-123456789"
    },
    {
      "system": "urn:gov:ph:philhealth",
      "value": "12-345678901-2"
    },
    {
      "system": "urn:openspp:registry:individual",
      "value": "5c8f9b4e-3d7a-4f2b-9e1c-8a7b6d5e4f3c"
    },
    {
      "system": "urn:gov:ph:pagibig",
      "value": "1234567890123"
    }
  ]
}
```

**Best Practice:** Always include at least one stable, widely-recognized identifier (like National ID).

### Time-Limited Identifiers

Some identifiers expire or change validity:

```json
{
  "system": "urn:openspp:program:4ps:id",
  "value": "4PS-2024-001234",
  "period": {
    "start": "2024-01-01",
    "end": "2024-12-31"
  }
}
```

## Using Identifiers in API Requests

### Reading a Resource

Use the pipe (`|`) separator in the URL:

```text
GET /api/v2/spp/Individual/{system}|{value}
```

**URL-encode the system** if it contains special characters:

```bash
# Original
urn:gov:ph:psa:national-id|PH-123456789

# URL-encoded
urn%3Agov%3Aph%3Apsa%3Anational-id|PH-123456789
```

### Example: curl

```bash
curl "https://api.openspp.org/api/v2/spp/Individual/urn%3Agov%3Aph%3Apsa%3Anational-id|PH-123456789" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

### Example: Python

```python
import requests
from urllib.parse import quote

def get_individual_by_identifier(system, value, token, base_url):
    """Fetch individual using a specific identifier."""
    # URL-encode the system
    encoded_system = quote(system, safe='')
    identifier = f"{encoded_system}|{value}"

    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(
        f"{base_url}/Individual/{identifier}",
        headers=headers
    )
    response.raise_for_status()
    return response.json()

# Usage
individual = get_individual_by_identifier(
    system="urn:gov:ph:psa:national-id",
    value="PH-123456789",
    token=token,
    base_url="https://api.openspp.org/api/v2/spp"
)
```

### Example: JavaScript

```javascript
function getIndividualByIdentifier(system, value, token, baseUrl) {
  // URL-encode the system
  const encodedSystem = encodeURIComponent(system);
  const identifier = `${encodedSystem}|${value}`;

  return fetch(`${baseUrl}/Individual/${identifier}`, {
    headers: {
      'Authorization': `Bearer ${token}`
    }
  }).then(response => {
    if (!response.ok) {
      throw new Error(`Request failed: ${response.statusText}`);
    }
    return response.json();
  });
}

// Usage
const individual = await getIndividualByIdentifier(
  'urn:gov:ph:psa:national-id',
  'PH-123456789',
  token,
  'https://api.openspp.org/api/v2/spp'
);
```

## Searching by Identifier

Use the `identifier` search parameter with the same `system|value` format:

```text
GET /api/v2/spp/Individual?identifier=urn:gov:ph:psa:national-id|PH-123456789
```

### Example: Python

```python
def search_by_identifier(system, value, token, base_url):
    """Search for individuals by identifier."""
    headers = {"Authorization": f"Bearer {token}"}
    params = {
        "identifier": f"{system}|{value}"
    }

    response = requests.get(
        f"{base_url}/Individual",
        headers=headers,
        params=params
    )
    response.raise_for_status()
    return response.json()

# Usage
results = search_by_identifier(
    system="urn:gov:ph:philhealth",
    value="12-345678901-2",
    token=token,
    base_url="https://api.openspp.org/api/v2/spp"
)

if results["total"] > 0:
    print(f"Found {results['total']} matching individuals")
```

### Searching Without System

Search across all identifier systems:

```text
GET /api/v2/spp/Individual?identifier=PH-123456789
```

**Note:** This searches the `value` field across all systems. Less efficient than specifying the system.

## Creating Resources with Identifiers

When creating a resource, provide at least one identifier:

```text
POST /api/v2/spp/Individual
Authorization: Bearer YOUR_TOKEN
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
  "birthDate": "1990-05-15"
}
```

### Example: Python

```python
def create_individual(identifier_system, identifier_value, name, birth_date, token, base_url):
    """Create a new individual with an identifier."""
    data = {
        "resourceType": "Individual",
        "identifier": [
            {
                "system": identifier_system,
                "value": identifier_value
            }
        ],
        "name": {
            "given": name["given"],
            "family": name["family"]
        },
        "birthDate": birth_date
    }

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

# Usage
individual = create_individual(
    identifier_system="urn:gov:ph:psa:national-id",
    identifier_value="PH-987654321",
    name={"given": "Juan", "family": "Dela Cruz"},
    birth_date="1990-05-15",
    token=token,
    base_url="https://api.openspp.org/api/v2/spp"
)

print(f"Created individual: {individual['identifier'][0]['value']}")
```

## Updating Identifiers

To add or update identifiers, use PUT with the complete resource:

### Updating Identifiers (PUT)

```text
PUT /api/v2/spp/Individual/urn:gov:ph:psa:national-id|PH-123456789
Authorization: Bearer YOUR_TOKEN
Content-Type: application/json
If-Match: "3"

{
  "resourceType": "Individual",
  "identifier": [
    {
      "system": "urn:gov:ph:psa:national-id",
      "value": "PH-123456789"
    },
    {
      "system": "urn:gov:ph:philhealth",
      "value": "12-345678901-2"
    },
    {
      "system": "urn:gov:ph:pagibig",
      "value": "1234567890123"
    }
  ],
  "name": { ... },
  ...
}
```

## References Between Resources

Use identifiers to reference other resources:

```json
{
  "resourceType": "ProgramMembership",
  "program": {
    "reference": "Program/urn:openspp:program|4Ps",
    "display": "Pantawid Pamilyang Pilipino Program"
  },
  "beneficiary": {
    "reference": "Individual/urn:gov:ph:psa:national-id|PH-123456789",
    "display": "Maria Santos"
  },
  "status": "enrolled"
}
```

**Reference format:**

```
{ResourceType}/{system}|{value}
```

## Common Identifier Systems

### Philippines

| System | Namespace URI | Example |
|--------|---------------|---------|
| PhilSys (National ID) | `urn:gov:ph:psa:national-id` | `PH-1234-5678-9012` |
| PhilHealth | `urn:gov:ph:philhealth` | `12-345678901-2` |
| SSS | `urn:gov:ph:sss` | `34-1234567-8` |
| Pag-IBIG | `urn:gov:ph:pagibig` | `1234567890123` |
| TIN | `urn:gov:ph:bir:tin` | `123-456-789-000` |

### Kenya

| System | Namespace URI | Example |
|--------|---------------|---------|
| National ID | `urn:gov:ke:nira:national-id` | `12345678` |
| Huduma Number | `urn:gov:ke:huduma` | `HN-12345678` |
| NHIF | `urn:gov:ke:nhif` | `1234567890` |

### OpenSPP Internal

| System | Namespace URI | Format |
|--------|---------------|--------|
| Individual Registry | `urn:openspp:registry:individual` | UUID v4 |
| Group Registry | `urn:openspp:registry:group` | UUID v4 |
| Program | `urn:openspp:program` | Program code |

## Identifier Validation

The API validates identifiers on create/update:

### Duplicate Detection

Creating a resource with an existing identifier fails:

```text
HTTP/1.1 422 Unprocessable Entity

{
  "resourceType": "OperationOutcome",
  "issue": [
    {
      "severity": "error",
      "code": "invalid",
      "details": {
        "coding": [
          {
            "system": "urn:openspp:error",
            "code": "DUPLICATE_IDENTIFIER"
          }
        ],
        "text": "Identifier urn:gov:ph:psa:national-id|PH-123456789 already exists"
      },
      "location": ["Individual.identifier[0]"]
    }
  ]
}
```

### Format Validation

Some identifier systems have format requirements:

```python
# Philippine PhilSys format: XX-NNNN-NNNN-NNNN
PHILSYS_PATTERN = r'^PH-\d{4}-\d{4}-\d{4}$'

# Philippine PhilHealth format: NN-NNNNNNNNN-N
PHILHEALTH_PATTERN = r'^\d{2}-\d{9}-\d$'
```

Invalid formats trigger validation errors:

```json
{
  "resourceType": "OperationOutcome",
  "issue": [
    {
      "severity": "error",
      "code": "invalid",
      "details": {
        "coding": [
          {
            "system": "urn:openspp:error",
            "code": "INVALID_IDENTIFIER"
          }
        ],
        "text": "Invalid PhilSys ID format. Expected: PH-NNNN-NNNN-NNNN"
      },
      "diagnostics": "identifier[0].value: expected pattern ^PH-\\d{4}-\\d{4}-\\d{4}$",
      "location": ["Individual.identifier[0].value"]
    }
  ]
}
```

## Best Practices

### 1. Always Specify the System

```python
# ✅ Good - Explicit system
identifier = {
    "system": "urn:gov:ph:psa:national-id",
    "value": "PH-123456789"
}

# ❌ Bad - No system
identifier = {
    "value": "PH-123456789"
}
```

### 2. Use Stable Identifiers for Lookups

Prefer government-issued IDs over program-specific IDs:

```python
# ✅ Good - National ID is stable
system = "urn:gov:ph:psa:national-id"

# ⚠️ Caution - Program ID may change
system = "urn:openspp:program:4ps:id"
```

### 3. Store the Full Identifier Object

Don't just store the value; store the system too:

```python
# ✅ Good - Full identifier preserved
stored_identifiers = [
    {"system": "urn:gov:ph:psa:national-id", "value": "PH-123456789"},
    {"system": "urn:gov:ph:philhealth", "value": "12-345678901-2"}
]

# ❌ Bad - Lost system context
stored_ids = ["PH-123456789", "12-345678901-2"]  # Which is which?
```

### 4. Handle Multiple Matches Gracefully

When searching by identifier, check if multiple records match:

```python
results = search_by_identifier(system, value, token, base_url)

if results["total"] == 0:
    print("No match found")
elif results["total"] == 1:
    individual = results["entry"][0]["resource"]
    print(f"Found: {individual['name']['text']}")
else:
    print(f"Warning: Multiple matches ({results['total']})")
    # Decide how to handle duplicates
```

## Are You Stuck?

**Getting 404 Not Found?**

Check that you're URL-encoding the system correctly:

```python
# Correct
encoded = quote("urn:gov:ph:psa:national-id", safe='')
# Result: urn%3Agov%3Aph%3Apsa%3Anational-id
```

**Which identifier system should I use?**

Use the most widely-recognized, stable identifier available. For Philippines: PhilSys (National ID). For Kenya: National ID (NIRA).

**Can I search by partial identifier value?**

No. Identifier searches are exact-match only. Use name search for fuzzy matching.

**What if someone doesn't have a government ID?**

OpenSPP can generate a UUID-based identifier:

```json
{
  "system": "urn:openspp:registry:individual",
  "value": "5c8f9b4e-3d7a-4f2b-9e1c-8a7b6d5e4f3c"
}
```

**How do I know what identifier systems are supported?**

Check the capability statement:

```bash
curl https://api.openspp.org/api/v2/spp/metadata
```

Look for `identifierSystems` in the response.

## Complete Example

```python
import requests
from urllib.parse import quote

class IdentifierHelper:
    """Helper class for working with OpenSPP identifiers."""

    @staticmethod
    def format_identifier_path(system, value):
        """Format system|value for URL path."""
        encoded_system = quote(system, safe='')
        return f"{encoded_system}|{value}"

    @staticmethod
    def format_identifier_param(system, value):
        """Format system|value for query parameter."""
        return f"{system}|{value}"

    @staticmethod
    def find_identifier(identifiers, system):
        """Find an identifier by system in a list."""
        for identifier in identifiers:
            if identifier["system"] == system:
                return identifier
        return None

# Usage
helper = IdentifierHelper()

# Fetch by identifier
path = helper.format_identifier_path(
    "urn:gov:ph:psa:national-id",
    "PH-123456789"
)
individual = requests.get(
    f"https://api.openspp.org/api/v2/spp/Individual/{path}",
    headers={"Authorization": f"Bearer {token}"}
).json()

# Find specific identifier in response
philhealth_id = helper.find_identifier(
    individual["identifier"],
    "urn:gov:ph:philhealth"
)

if philhealth_id:
    print(f"PhilHealth: {philhealth_id['value']}")
else:
    print("No PhilHealth ID on file")
```

## Next Steps

- {doc}`resources` - Learn about available API resources
- {doc}`search` - Advanced search capabilities
- {doc}`consent` - Consent-based access control
- {doc}`batch` - Creating multiple resources with identifiers

## See Also

- [ADR-007: Namespace URIs for Identifiers](https://github.com/OpenSPP/openspp-docs/blob/main/docs/architecture/decisions/ADR-007-namespace-uris.md)
- [G2P Connect: Identifier Systems](https://g2pconnect.cdpi.dev/protocol/resources/identifier)
- [FHIR: Identifier Type](https://www.hl7.org/fhir/datatypes.html#Identifier)
