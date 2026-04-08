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

All searches return a **SearchResult** response:

```json
{
  "data": [
    { /* Individual */ }
  ],
  "meta": {
    "total": 1523,
    "count": 50,
    "offset": 0
  },
  "links": {
    "self": "/api/v2/spp/Individual?name=Santos&_count=50",
    "next": "/api/v2/spp/Individual?name=Santos&_count=50&_offset=50",
    "prev": null
  }
}
```

## Individual Search Parameters

### By Identifier

```http
GET /api/v2/spp/Individual?identifier=urn:gov:ph:psa:national-id|PH-123456789
```

**Format:** `system|value` or just `value` (searches all systems)

**Example: Python**

```python
def search_by_identifier(system, value, token, base_url):
    """Search for individuals by identifier."""
    params = {"identifier": f"{system}|{value}"}
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(
        f"{base_url}/Individual",
        headers=headers,
        params=params
    )
    response.raise_for_status()
    return response.json()

# Usage
results = search_by_identifier(
    system="urn:gov:ph:psa:national-id",
    value="PH-123456789",
    token=token,
    base_url="https://{your-domain}/api/v2/spp"
)
```

### By Name

```http
# Contains search (case-insensitive)
GET /api/v2/spp/Individual?name=Santos
```

Name search uses case-insensitive substring matching.

**Example: Python**

```python
def search_by_name(name, token, base_url):
    """Search for individuals by name."""
    params = {"name": name}
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(
        f"{base_url}/Individual",
        headers=headers,
        params=params
    )
    response.raise_for_status()
    return response.json()

# Search by family name
results = search_by_name("Santos", token=token, base_url=base_url)
```

### By Birth Date

```http
# Exact date
GET /api/v2/spp/Individual?birthdate=1985-03-15

# Date range
GET /api/v2/spp/Individual?birthdate=ge1980-01-01&birthdate=le1990-12-31
```

**Date Prefixes:**

| Prefix | Meaning | Example |
|--------|---------|---------|
| `eq` | Equal to (default) | `eq1985-03-15` or `1985-03-15` |
| `ne` | Not equal to | `ne1985-03-15` |
| `lt` | Less than | `lt1985-01-01` |
| `le` | Less than or equal | `le1984-12-31` |
| `gt` | Greater than | `gt1990-01-01` |
| `ge` | Greater than or equal | `ge1990-01-01` |

**Example: Python**

```python
def search_by_birth_date_range(start_date, end_date, token, base_url):
    """Search for individuals by birth date range."""
    params = {
        "birthdate": [
            f"ge{start_date}",
            f"le{end_date}"
        ]
    }
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(
        f"{base_url}/Individual",
        headers=headers,
        params=params
    )
    response.raise_for_status()
    return response.json()

# Find individuals born in the 1980s
results = search_by_birth_date_range(
    start_date="1980-01-01",
    end_date="1989-12-31",
    token=token,
    base_url=base_url
)
```

### By Gender

```http
GET /api/v2/spp/Individual?gender=urn:iso:std:iso:5218|2
```

**ISO 5218 Gender Codes:**

| Code | Meaning |
|------|---------|
| `0` | Not known |
| `1` | Male |
| `2` | Female |
| `9` | Not applicable |

**Example: Python**

```python
def search_by_gender(gender_code, token, base_url):
    """Search for individuals by gender."""
    params = {"gender": f"urn:iso:std:iso:5218|{gender_code}"}
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(
        f"{base_url}/Individual",
        headers=headers,
        params=params
    )
    response.raise_for_status()
    return response.json()

# Find all females
results = search_by_gender("2", token=token, base_url=base_url)
```

### By Address

```http
GET /api/v2/spp/Individual?address=Manila
```

Searches across all address fields (city, state, text, etc.)

**Example: Python**

```python
def search_by_address(location, token, base_url):
    """Search for individuals by address."""
    params = {"address": location}
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(
        f"{base_url}/Individual",
        headers=headers,
        params=params
    )
    response.raise_for_status()
    return response.json()

# Find all individuals in Manila
results = search_by_address("Manila", token=token, base_url=base_url)
```

### By Last Updated

```http
# Modified since date
GET /api/v2/spp/Individual?_lastUpdated=ge2024-01-01

# Modified in date range
GET /api/v2/spp/Individual?_lastUpdated=ge2024-01-01&_lastUpdated=lt2024-02-01
```

**Example: Python**

```python
from datetime import datetime, timedelta

def search_recently_updated(days, token, base_url):
    """Search for individuals updated in the last N days."""
    since_date = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
    params = {"_lastUpdated": f"ge{since_date}"}
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(
        f"{base_url}/Individual",
        headers=headers,
        params=params
    )
    response.raise_for_status()
    return response.json()

# Find individuals updated in last 7 days
results = search_recently_updated(7, token=token, base_url=base_url)
```

## Group Search Parameters

### By Member

```http
GET /api/v2/spp/Group?member=Individual/urn:gov:ph:psa:national-id|PH-123456789
```

Find all groups containing a specific individual.

**Example: Python**

```python
def find_groups_for_individual(individual_ref, token, base_url):
    """Find all groups an individual belongs to."""
    params = {"member": individual_ref}
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(
        f"{base_url}/Group",
        headers=headers,
        params=params
    )
    response.raise_for_status()
    return response.json()

# Usage
groups = find_groups_for_individual(
    individual_ref="Individual/urn:gov:ph:psa:national-id|PH-123456789",
    token=token,
    base_url=base_url
)

for group in groups["data"]:
    print(f"Member of: {group['name']}")
```

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

Use the `links` object in the response:

```json
{
  "meta": {
    "total": 1523,
    "count": 20,
    "offset": 0
  },
  "links": {
    "self": "/api/v2/spp/Individual?name=Santos&_count=20&_offset=0",
    "next": "/api/v2/spp/Individual?name=Santos&_count=20&_offset=20",
    "prev": null
  }
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
        result = response.json()

        # Add results
        all_results.extend(result.get("data", []))

        # Follow next link
        current_url = result.get("links", {}).get("next")

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

```http
GET /api/v2/spp/Individual?name=Santos&birthdate=ge1980-01-01&address=Manila
```

**Example: Python**

```python
def advanced_search(token, base_url, **criteria):
    """Perform advanced search with multiple criteria."""
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(
        f"{base_url}/Individual",
        headers=headers,
        params=criteria
    )
    response.raise_for_status()
    return response.json()

# Complex search
results = advanced_search(
    token=token,
    base_url=base_url,
    name="Santos",
    birthdate=["ge1980-01-01", "le1990-12-31"],
    address="Manila",
    gender="urn:iso:std:iso:5218|2",
    _count=100,
    _sort="-birthdate"
)

print(f"Found {results['meta']['total']} matching individuals")
```

## Advanced Search

For complex queries with AND/OR logic, use the advanced search endpoint:

### Discover Available Filters

```http
GET /api/v2/spp/Individual/_filters
Authorization: Bearer TOKEN
```

Returns filterable fields, supported operators, and saved filter presets for the resource type.

### Complex Filter Queries

```http
POST /api/v2/spp/Individual/_search
Authorization: Bearer TOKEN
Content-Type: application/json

{
  "filters": [
    {"field": "age", "operator": ">=", "value": 18},
    {"field": "gender", "operator": "==", "value": "F"}
  ],
  "filter_logic": "AND",
  "sort": [
    {"field": "name", "direction": "ASC"}
  ],
  "pagination": {
    "count": 50,
    "last_id": null
  }
}
```

**Supported filter logic:** `"AND"` (default) or `"OR"`

**Pagination:** Uses cursor-based pagination with `last_id` (the internal ID from the last entry of the previous page). Use `null` for the first page, then pass the `last_id` from the response for subsequent pages.

**Example: Python**

```python
def advanced_filter_search(filters, token, base_url, filter_logic="AND", count=50):
    """Search with complex filter conditions."""
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    body = {
        "filters": filters,
        "filter_logic": filter_logic,
        "pagination": {"count": count, "last_id": None}
    }

    response = requests.post(
        f"{base_url}/Individual/_search",
        headers=headers,
        json=body
    )
    response.raise_for_status()
    return response.json()

# Find females aged 18+ OR males aged 65+
results = advanced_filter_search(
    filters=[
        {"field": "age", "operator": ">=", "value": 18},
        {"field": "address", "operator": "contains", "value": "Manila"}
    ],
    filter_logic="AND",
    token=token,
    base_url=base_url
)
```

```{note}
Advanced search is available for Individual, Group, Program, and ProgramMembership resources.
```

## Search Score

For name and text searches, results are sorted by relevance. The API returns the best matches first based on how closely the result matches the search terms.

## ProgramMembership Search

```http
# By beneficiary
GET /api/v2/spp/ProgramMembership?beneficiary=Individual/urn:gov:ph:psa:national-id|PH-123

# By program
GET /api/v2/spp/ProgramMembership?program=Program/urn:openspp:program|4Ps

# By status
GET /api/v2/spp/ProgramMembership?status=active

# Combined
GET /api/v2/spp/ProgramMembership?beneficiary=Group/urn:openspp:group|HH-001&status=active
```

**Example: Python**

```python
def get_active_enrollments(beneficiary_ref, token, base_url):
    """Get active program enrollments for a beneficiary."""
    params = {
        "beneficiary": beneficiary_ref,
        "status": "active"
    }
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(
        f"{base_url}/ProgramMembership",
        headers=headers,
        params=params
    )
    response.raise_for_status()
    return response.json()

# Usage
enrollments = get_active_enrollments(
    beneficiary_ref="Individual/urn:gov:ph:psa:national-id|PH-123456789",
    token=token,
    base_url=base_url
)

for membership in enrollments["data"]:
    print(f"Enrolled in: {membership['program']['display']}")
    print(f"Since: {membership['enrollmentDate']}")
```

## Error Handling

### No Results

Empty results return `total: 0` with empty `data` array:

```json
{
  "data": [],
  "meta": {
    "total": 0,
    "count": 0,
    "offset": 0
  },
  "links": {
    "self": "/api/v2/spp/Individual?name=NonexistentName",
    "next": null,
    "prev": null
  }
}
```

### Invalid Parameters

```http
HTTP/1.1 400 Bad Request

{
  "type": "urn:openspp:error:validation",
  "title": "Bad Request",
  "status": 400,
  "detail": "Invalid search parameter: 'foo' is not a supported parameter"
}
```

### Too Many Results

If results exceed reasonable limits, use pagination. Add filters or use `_count` and `_offset` to page through results:

```http
GET /api/v2/spp/Individual?name=Santos&_count=100&_offset=0
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
            result = initial_search_fn(
                **search_params,
                count=count,
                offset=offset
            )

            items = result.get("data", [])
            all_results.extend(items)

            # Check if there are more results
            total = result.get("meta", {}).get("total", 0)
            if offset + len(items) >= total:
                break

            offset += count

        return all_results

# Usage
searcher = OpenSPPSearch(
    base_url="https://{your-domain}/api/v2/spp",
    token=token
)

# Simple search
results = searcher.search_individuals(
    name="Santos",
    address="Manila",
    count=50
)
print(f"Found {results['meta']['total']} individuals")

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

- [REST API Best Practices](https://restfulapi.net/) - REST design principles
