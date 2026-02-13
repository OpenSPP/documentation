---
openspp:
  doc_status: draft
  products: [core]
---

# Search and Filtering

This guide is for **developers** implementing search functionality with OpenSPP API V2.

## Search Basics

Search for resources using GET with query parameters:

```http
GET /api/v2/spp/{ResourceType}?parameter=value
Authorization: Bearer TOKEN
```

All searches return a **Bundle** with `type: searchset`:

```json
{
  "resourceType": "Bundle",
  "type": "searchset",
  "total": 1523,
  "link": [
    {
      "relation": "self",
      "url": "/api/v2/spp/Individual?name=Santos&_count=50"
    },
    {
      "relation": "next",
      "url": "/api/v2/spp/Individual?name=Santos&_count=50&_offset=50"
    }
  ],
  "entry": [
    {
      "resource": { /* Individual */ },
      "search": {
        "mode": "match",
        "score": 0.95
      }
    }
  ]
}
```

## Individual Search Parameters

### By Identifier

**Format:** `system|value` or just `value` (searches all systems)

`````{tab-set}

````{tab-item} cURL
```bash
curl "https://api.openspp.org/api/v2/spp/Individual?identifier=urn:gov:ph:psa:national-id|PH-123456789" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```
````

````{tab-item} Python
```python
import requests

params = {"identifier": "urn:gov:ph:psa:national-id|PH-123456789"}
headers = {"Authorization": f"Bearer {token}"}

response = requests.get(
    f"{base_url}/Individual",
    headers=headers,
    params=params
)
response.raise_for_status()
results = response.json()
```
````

````{tab-item} JavaScript
```javascript
const params = new URLSearchParams({
  identifier: "urn:gov:ph:psa:national-id|PH-123456789"
});
const response = await fetch(
  `${baseUrl}/Individual?${params}`,
  { headers: { "Authorization": `Bearer ${token}` } }
);
const results = await response.json();
```
````

`````

### By Name

Name search uses case-insensitive substring matching.

`````{tab-set}

````{tab-item} cURL
```bash
# Contains search (case-insensitive)
curl "https://api.openspp.org/api/v2/spp/Individual?name=Santos" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```
````

````{tab-item} Python
```python
import requests

params = {"name": "Santos"}
headers = {"Authorization": f"Bearer {token}"}

response = requests.get(
    f"{base_url}/Individual",
    headers=headers,
    params=params
)
response.raise_for_status()
results = response.json()
```
````

````{tab-item} JavaScript
```javascript
const response = await fetch(
  `${baseUrl}/Individual?name=Santos`,
  { headers: { "Authorization": `Bearer ${token}` } }
);
const results = await response.json();
```
````

`````

### By Birth Date

**Date Prefixes:**

| Prefix | Meaning | Example |
|--------|---------|---------|
| `eq` | Equal to (default) | `eq1985-03-15` or `1985-03-15` |
| `ne` | Not equal to | `ne1985-03-15` |
| `lt` | Less than | `lt1985-01-01` |
| `le` | Less than or equal | `le1984-12-31` |
| `gt` | Greater than | `gt1990-01-01` |
| `ge` | Greater than or equal | `ge1990-01-01` |

`````{tab-set}

````{tab-item} cURL
```bash
# Exact date
curl "https://api.openspp.org/api/v2/spp/Individual?birthdate=1985-03-15" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"

# Date range
curl "https://api.openspp.org/api/v2/spp/Individual?birthdate=ge1980-01-01&birthdate=le1990-12-31" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```
````

````{tab-item} Python
```python
import requests

# Date range search
params = {
    "birthdate": [
        "ge1980-01-01",
        "le1989-12-31"
    ]
}
headers = {"Authorization": f"Bearer {token}"}

response = requests.get(
    f"{base_url}/Individual",
    headers=headers,
    params=params
)
response.raise_for_status()
results = response.json()
```
````

````{tab-item} JavaScript
```javascript
// Date range search
const params = new URLSearchParams();
params.append("birthdate", "ge1980-01-01");
params.append("birthdate", "le1989-12-31");

const response = await fetch(
  `${baseUrl}/Individual?${params}`,
  { headers: { "Authorization": `Bearer ${token}` } }
);
const results = await response.json();
```
````

`````

### By Gender

**ISO 5218 Gender Codes:**

| Code | Meaning |
|------|---------|
| `0` | Not known |
| `1` | Male |
| `2` | Female |
| `9` | Not applicable |

`````{tab-set}

````{tab-item} cURL
```bash
curl "https://api.openspp.org/api/v2/spp/Individual?gender=urn:iso:std:iso:5218|2" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```
````

````{tab-item} Python
```python
import requests

params = {"gender": "urn:iso:std:iso:5218|2"}
headers = {"Authorization": f"Bearer {token}"}

response = requests.get(
    f"{base_url}/Individual",
    headers=headers,
    params=params
)
response.raise_for_status()
results = response.json()
```
````

````{tab-item} JavaScript
```javascript
const response = await fetch(
  `${baseUrl}/Individual?gender=urn:iso:std:iso:5218|2`,
  { headers: { "Authorization": `Bearer ${token}` } }
);
const results = await response.json();
```
````

`````

### By Address

Searches across all address fields (city, state, text, etc.)

`````{tab-set}

````{tab-item} cURL
```bash
curl "https://api.openspp.org/api/v2/spp/Individual?address=Manila" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```
````

````{tab-item} Python
```python
import requests

params = {"address": "Manila"}
headers = {"Authorization": f"Bearer {token}"}

response = requests.get(
    f"{base_url}/Individual",
    headers=headers,
    params=params
)
response.raise_for_status()
results = response.json()
```
````

````{tab-item} JavaScript
```javascript
const response = await fetch(
  `${baseUrl}/Individual?address=Manila`,
  { headers: { "Authorization": `Bearer ${token}` } }
);
const results = await response.json();
```
````

`````

### By Last Updated

`````{tab-set}

````{tab-item} cURL
```bash
# Modified since date
curl "https://api.openspp.org/api/v2/spp/Individual?_lastUpdated=ge2024-01-01" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"

# Modified in date range
curl "https://api.openspp.org/api/v2/spp/Individual?_lastUpdated=ge2024-01-01&_lastUpdated=lt2024-02-01" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```
````

````{tab-item} Python
```python
from datetime import datetime, timedelta
import requests

# Find individuals updated in last 7 days
since_date = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
params = {"_lastUpdated": f"ge{since_date}"}
headers = {"Authorization": f"Bearer {token}"}

response = requests.get(
    f"{base_url}/Individual",
    headers=headers,
    params=params
)
response.raise_for_status()
results = response.json()
```
````

````{tab-item} JavaScript
```javascript
// Find individuals updated in last 7 days
const since = new Date();
since.setDate(since.getDate() - 7);
const sinceDate = since.toISOString().split("T")[0];

const response = await fetch(
  `${baseUrl}/Individual?_lastUpdated=ge${sinceDate}`,
  { headers: { "Authorization": `Bearer ${token}` } }
);
const results = await response.json();
```
````

`````

## Group Search Parameters

### By Member

Find all groups containing a specific individual.

`````{tab-set}

````{tab-item} cURL
```bash
curl "https://api.openspp.org/api/v2/spp/Group?member=Individual/urn:gov:ph:psa:national-id|PH-123456789" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```
````

````{tab-item} Python
```python
import requests

params = {"member": "Individual/urn:gov:ph:psa:national-id|PH-123456789"}
headers = {"Authorization": f"Bearer {token}"}

response = requests.get(
    f"{base_url}/Group",
    headers=headers,
    params=params
)
response.raise_for_status()
groups = response.json()

for entry in groups["entry"]:
    group = entry["resource"]
    print(f"Member of: {group['name']}")
```
````

````{tab-item} JavaScript
```javascript
const params = new URLSearchParams({
  member: "Individual/urn:gov:ph:psa:national-id|PH-123456789"
});
const response = await fetch(
  `${baseUrl}/Group?${params}`,
  { headers: { "Authorization": `Bearer ${token}` } }
);
const groups = await response.json();
groups.entry.forEach(entry => {
  console.log(`Member of: ${entry.resource.name}`);
});
```
````

`````

## Pagination

Control result pagination with `_count` and `_offset`:

```http
GET /api/v2/spp/Individual?name=Santos&_count=50&_offset=100
```

| Parameter | Description | Default | Max |
|-----------|-------------|---------|-----|
| `_count` | Results per page | 20 | 100 |
| `_offset` | Skip N results | 0 | - |

### Following Links

Use the `link` array in the response:

```json
{
  "resourceType": "Bundle",
  "total": 1523,
  "link": [
    {
      "relation": "self",
      "url": "/api/v2/spp/Individual?name=Santos&_count=20&_offset=0"
    },
    {
      "relation": "next",
      "url": "/api/v2/spp/Individual?name=Santos&_count=20&_offset=20"
    },
    {
      "relation": "previous",
      "url": "/api/v2/spp/Individual?name=Santos&_count=20&_offset=0"
    }
  ]
}
```

**Example: Python**

```python
def paginate_search(initial_url, token, base_url):
    """Iterate through all pages of search results."""
    headers = {"Authorization": f"Bearer {token}"}
    current_url = initial_url
    all_results = []

    while current_url:
        response = requests.get(
            f"{base_url.rstrip('/')}/{current_url.lstrip('/')}",
            headers=headers
        )
        response.raise_for_status()
        bundle = response.json()

        # Add results
        all_results.extend(bundle.get("entry", []))

        # Find next link
        next_link = next(
            (link for link in bundle.get("link", []) if link["relation"] == "next"),
            None
        )
        current_url = next_link["url"] if next_link else None

    return all_results

# Usage
all_individuals = paginate_search(
    initial_url="/Individual?name=Santos&_count=50",
    token=token,
    base_url=base_url
)
print(f"Found {len(all_individuals)} total results")
```

## Sorting

Sort results with `_sort`:

```http
# Sort by name (ascending)
GET /api/v2/spp/Individual?_sort=name

# Sort by birth date (descending)
GET /api/v2/spp/Individual?_sort=-birthdate

# Multi-field sort
GET /api/v2/spp/Individual?_sort=name,-birthdate
```

**Prefix:**
- No prefix or `+`: Ascending
- `-`: Descending

**Example: Python**

```python
def search_sorted(params, sort_fields, token, base_url):
    """Search with sorting."""
    params["_sort"] = ",".join(sort_fields)
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(
        f"{base_url}/Individual",
        headers=headers,
        params=params
    )
    response.raise_for_status()
    return response.json()

# Sort by name, then birth date descending
results = search_sorted(
    params={"name": "Santos"},
    sort_fields=["name", "-birthdate"],
    token=token,
    base_url=base_url
)
```

## Field Selection

Request only specific fields with `_elements`:

```http
GET /api/v2/spp/Individual?_elements=identifier,name,birthDate
```

Reduces response size and improves performance.

**Example: Python**

```python
def search_with_fields(params, fields, token, base_url):
    """Search and return only specific fields."""
    params["_elements"] = ",".join(fields)
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(
        f"{base_url}/Individual",
        headers=headers,
        params=params
    )
    response.raise_for_status()
    return response.json()

# Get only identifiers and names
results = search_with_fields(
    params={"name": "Santos"},
    fields=["identifier", "name"],
    token=token,
    base_url=base_url
)
```

## Combining Parameters

Combine multiple search parameters (AND logic):

`````{tab-set}

````{tab-item} cURL
```bash
curl "https://api.openspp.org/api/v2/spp/Individual?name=Santos&birthdate=ge1980-01-01&address=Manila&_count=100&_sort=-birthdate" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```
````

````{tab-item} Python
```python
import requests

headers = {"Authorization": f"Bearer {token}"}
params = {
    "name": "Santos",
    "birthdate": ["ge1980-01-01", "le1990-12-31"],
    "address": "Manila",
    "gender": "urn:iso:std:iso:5218|2",
    "_count": 100,
    "_sort": "-birthdate"
}

response = requests.get(
    f"{base_url}/Individual",
    headers=headers,
    params=params
)
response.raise_for_status()
results = response.json()
print(f"Found {results['total']} matching individuals")
```
````

````{tab-item} JavaScript
```javascript
const params = new URLSearchParams({
  name: "Santos",
  address: "Manila",
  gender: "urn:iso:std:iso:5218|2",
  _count: "100",
  _sort: "-birthdate"
});
params.append("birthdate", "ge1980-01-01");
params.append("birthdate", "le1990-12-31");

const response = await fetch(
  `${baseUrl}/Individual?${params}`,
  { headers: { "Authorization": `Bearer ${token}` } }
);
const results = await response.json();
console.log(`Found ${results.total} matching individuals`);
```
````

`````

## Search Score

Results include a relevance score (0.0 to 1.0):

```json
{
  "entry": [
    {
      "resource": { /* Individual */ },
      "search": {
        "mode": "match",
        "score": 0.95
      }
    }
  ]
}
```

Higher scores indicate better matches (used for name/text searches).

## ProgramMembership Search

`````{tab-set}

````{tab-item} cURL
```bash
# By beneficiary
curl "https://api.openspp.org/api/v2/spp/ProgramMembership?beneficiary=Individual/urn:gov:ph:psa:national-id|PH-123" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"

# By program
curl "https://api.openspp.org/api/v2/spp/ProgramMembership?program=Program/urn:openspp:program|4Ps" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"

# Combined: active enrollments for a group
curl "https://api.openspp.org/api/v2/spp/ProgramMembership?beneficiary=Group/urn:openspp:group|HH-001&status=active" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```
````

````{tab-item} Python
```python
import requests

# Get active enrollments for a beneficiary
params = {
    "beneficiary": "Individual/urn:gov:ph:psa:national-id|PH-123456789",
    "status": "active"
}
headers = {"Authorization": f"Bearer {token}"}

response = requests.get(
    f"{base_url}/ProgramMembership",
    headers=headers,
    params=params
)
response.raise_for_status()
enrollments = response.json()

for entry in enrollments["entry"]:
    membership = entry["resource"]
    print(f"Enrolled in: {membership['program']['display']}")
    print(f"Since: {membership['enrollmentDate']}")
```
````

````{tab-item} JavaScript
```javascript
// Get active enrollments for a beneficiary
const params = new URLSearchParams({
  beneficiary: "Individual/urn:gov:ph:psa:national-id|PH-123456789",
  status: "active"
});
const response = await fetch(
  `${baseUrl}/ProgramMembership?${params}`,
  { headers: { "Authorization": `Bearer ${token}` } }
);
const enrollments = await response.json();
enrollments.entry.forEach(entry => {
  const m = entry.resource;
  console.log(`Enrolled in: ${m.program.display}`);
  console.log(`Since: ${m.enrollmentDate}`);
});
```
````

`````

## Error Handling

### No Results

Empty results return `total: 0` with empty `entry` array:

```json
{
  "resourceType": "Bundle",
  "type": "searchset",
  "total": 0,
  "entry": []
}
```

### Invalid Parameters

```http
HTTP/1.1 400 Bad Request

{
  "resourceType": "OperationOutcome",
  "issue": [
    {
      "severity": "error",
      "code": "invalid",
      "details": {
        "text": "Invalid search parameter: 'foo' is not a supported parameter"
      }
    }
  ]
}
```

### Too Many Results

If results exceed reasonable limits (e.g., >10,000), the API may return an error:

```json
{
  "resourceType": "OperationOutcome",
  "issue": [
    {
      "severity": "warning",
      "code": "too-many",
      "details": {
        "text": "Search returned >10,000 results. Please refine your search criteria."
      }
    }
  ]
}
```

## Performance Tips

### 1. Use Identifiers When Possible

```python
# ✅ Fast - Direct lookup by identifier
individual = get_by_identifier("urn:gov:ph:psa:national-id|PH-123456789")

# ❌ Slow - Search by name
results = search_by_name("Maria Santos")
```

### 2. Limit Fields with `_elements`

```python
# ✅ Fast - Only request needed fields
params = {"name": "Santos", "_elements": "identifier,name"}

# ❌ Slow - Full resource returned
params = {"name": "Santos"}
```

### 3. Use Pagination Appropriately

```python
# ✅ Good - Reasonable page size
params = {"_count": 50}

# ❌ Bad - Too large
params = {"_count": 1000}
```

### 4. Use Date Filters to Reduce Results

```python
# ✅ Good - Filter to recent changes
params = {"_lastUpdated": "ge2024-11-01"}

# ❌ Bad - No filter (returns everything)
params = {}
```

### 5. Cache Results When Appropriate

```python
import time

class CachedSearch:
    """Simple search result cache."""

    def __init__(self, ttl=300):
        self.cache = {}
        self.ttl = ttl

    def search(self, url, token, base_url):
        """Search with caching."""
        cache_key = f"{url}|{token}"

        # Check cache
        if cache_key in self.cache:
            cached_data, cached_time = self.cache[cache_key]
            if time.time() - cached_time < self.ttl:
                return cached_data

        # Fetch from API
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(
            f"{base_url}/{url.lstrip('/')}",
            headers=headers
        )
        response.raise_for_status()
        data = response.json()

        # Store in cache
        self.cache[cache_key] = (data, time.time())
        return data

# Usage
cache = CachedSearch(ttl=300)  # 5-minute cache
results = cache.search(
    url="/Individual?name=Santos",
    token=token,
    base_url=base_url
)
```

## Complete Search Example

```python
import requests
from typing import Optional, List, Dict

class OpenSPPSearch:
    """Comprehensive search client."""

    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token
        self.headers = {"Authorization": f"Bearer {token}"}

    def search_individuals(
        self,
        identifier: Optional[str] = None,
        name: Optional[str] = None,
        birth_date_from: Optional[str] = None,
        birth_date_to: Optional[str] = None,
        gender: Optional[str] = None,
        address: Optional[str] = None,
        updated_since: Optional[str] = None,
        count: int = 20,
        offset: int = 0,
        sort: Optional[List[str]] = None,
        fields: Optional[List[str]] = None
    ) -> Dict:
        """
        Search for individuals with flexible criteria.

        Args:
            identifier: System|value identifier
            name: Name to search (case-insensitive substring match)
            birth_date_from: Birth date >= (YYYY-MM-DD)
            birth_date_to: Birth date <= (YYYY-MM-DD)
            gender: Gender code (ISO 5218)
            address: Address search
            updated_since: Last updated >= (YYYY-MM-DD)
            count: Results per page (default 20, max 100)
            offset: Results to skip
            sort: Sort fields (prefix with - for descending)
            fields: Fields to return

        Returns:
            Search results bundle
        """
        params = {}

        if identifier:
            params["identifier"] = identifier
        if name:
            params["name"] = name
        if birth_date_from:
            params.setdefault("birthdate", []).append(f"ge{birth_date_from}")
        if birth_date_to:
            params.setdefault("birthdate", []).append(f"le{birth_date_to}")
        if gender:
            params["gender"] = f"urn:iso:std:iso:5218|{gender}"
        if address:
            params["address"] = address
        if updated_since:
            params["_lastUpdated"] = f"ge{updated_since}"

        params["_count"] = count
        params["_offset"] = offset

        if sort:
            params["_sort"] = ",".join(sort)
        if fields:
            params["_elements"] = ",".join(fields)

        response = requests.get(
            f"{self.base_url}/Individual",
            headers=self.headers,
            params=params
        )
        response.raise_for_status()
        return response.json()

    def get_all_results(self, initial_search_fn, **search_params):
        """Paginate through all search results."""
        all_results = []
        offset = 0
        count = 50

        while True:
            bundle = initial_search_fn(
                **search_params,
                count=count,
                offset=offset
            )

            entries = bundle.get("entry", [])
            all_results.extend(entries)

            # Check if there are more results
            total = bundle.get("total", 0)
            if offset + len(entries) >= total:
                break

            offset += count

        return all_results

# Usage
searcher = OpenSPPSearch(
    base_url="https://api.openspp.org/api/v2/spp",
    token=token
)

# Simple search
results = searcher.search_individuals(
    name="Santos",
    address="Manila",
    count=50
)
print(f"Found {results['total']} individuals")

# Advanced search
results = searcher.search_individuals(
    name="Maria",
    birth_date_from="1980-01-01",
    birth_date_to="1990-12-31",
    gender="2",  # Female
    address="Metro Manila",
    sort=["name", "-birthdate"],
    fields=["identifier", "name", "birthDate", "address"]
)

# Get all results (with pagination)
all_results = searcher.get_all_results(
    searcher.search_individuals,
    name="Santos"
)
print(f"Retrieved {len(all_results)} total results")
```

## Are You Stuck?

**Search returns too many results?**

Add more criteria to narrow the search. Use date ranges or address filters.

**Getting empty results when you expect matches?**

Check if consent is filtering results. Review the `X-Consent-Status` header.

**Name search not finding expected results?**

Name search is case-insensitive and uses substring matching. Try searching with just the family name or given name.

**Pagination links not working?**

Use the full URL from the `link` array. Don't manually construct pagination URLs.

**Search is slow?**

Use `_elements` to request only needed fields. Filter by `_lastUpdated` if you're syncing data.

## Next Steps

- {doc}`batch` - Creating multiple resources efficiently
- {doc}`resources` - Available resources and their fields
- {doc}`consent` - Understanding consent-based filtering
- {doc}`errors` - Error handling

## See Also

- [FHIR Search](https://www.hl7.org/fhir/search.html) - FHIR search patterns
- [REST API Best Practices](https://restfulapi.net/) - REST design principles
