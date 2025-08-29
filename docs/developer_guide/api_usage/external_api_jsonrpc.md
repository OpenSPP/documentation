---
review-status: needs-review
review-date: 2025-08-28
reviewer: technical-writer
migration-notes: "Rewritten for JSON-RPC, Python only, with OpenG2P Registry context"
---

# External API using JSON-RPC

This guide explains how to connect to and interact with OpenSPP Registry using the JSON-RPC API, with practical Python examples for adding individuals, groups, and memberships.

## Prerequisites

- OpenSPP server running and accessible.
- User credentials or API key with appropriate permissions.
- Python 3.x and the `requests` library installed (`pip install requests`).

## Process
### Understanding JSON-RPC in OpenSPP

OpenSPP exposes much of its data and functionality via JSON-RPC endpoints. You can use these endpoints to authenticate, read, create, update, and delete records from external applications.

**Endpoint:**  
- `/jsonrpc` — All JSON-RPC calls (authentication and model methods)

### JSON-RPC Payload Structure and Methods

All interactions with the OpenSPP JSON-RPC API use a standard payload structure. Each request is a JSON object with the following keys:

- `jsonrpc`: The JSON-RPC protocol version (always `"2.0"`).
- `method`: The JSON-RPC method (always `"call"` for OpenSPP).
- `params`: The parameters for the call, including:
    - `service`: The Odoo service to use (`"common"` for authentication, `"object"` for model methods).
    - `method`: The method to call on the service (e.g., `"authenticate"`, `"execute_kw"`).
    - `args`: A list of arguments for the method.
- `id`: A unique identifier for the request (integer or string).

**Example Payload:**
```python
payload = {
    "jsonrpc": "2.0",
    "method": "call",
    "params": {
        "service": "object",
        "method": "execute_kw",
        "args": [
            db, uid, password,
            "res.partner", "search_read",
            [[["is_group", "=", False]]],  # Domain filter
            {"fields": ["name", "reg_id"], "limit": 5}  # Options
        ]
    },
    "id": 10,
}
```

**Common JSON-RPC Methods:**
- `authenticate`: Used for logging in and obtaining a user ID.
- `execute_kw`: Used for calling model methods (such as `create`, `write`, `unlink`, `search_read`).

---

### Common Model Methods and Args

When using the `"object"` service with the `"execute_kw"` method, you can call various model methods. Here are the most common:

**`create`**
Creates a new record.

**Args:**
1. Model name (e.g., `"res.partner"`)
2. Method name (`"create"`)
3. List of dictionaries with field values

**Example:**
```python
["res.partner", "create", [{"name": "Jane Doe", "reg_id": "IND654321"}]]
```

**Result:**
Returns the ID of the newly created record.

**`write`**
Updates existing records.

**Args:**
1. Model name
2. Method name (`"write"`)
3. List of record IDs to update
4. Dictionary of fields to update

**Example:**
```python
["res.partner", "write", [[individual_id], {"birthdate": "1991-02-02"}]]
```

**Result:**
Returns a dictionary indicating the result of the update.

**`unlink`**
Deletes records.

**Args:**
1. Model name
2. Method name (`"unlink"`)
3. List of record IDs to delete

**Example:**
```python
["res.partner", "unlink", [individual_id]]
```

**Result:**
Returns a dictionary indicating the result of the deletion.


**`search_read`**
Searches for records and reads their fields.

**Args:**
1. Model name
2. Method name (`"search_read"`)
3. Domain filter (list of conditions)
4. Options dictionary (fields, limit, offset, etc.)

**Example:**
```python
["res.partner", "search_read", [[["is_group", "=", False]]], {"fields": ["name", "reg_id"], "limit": 5}]
```

**Domain Filters:**  
A domain is a list of conditions, each as a list: `[field, operator, value]`.  
Example: `[["name", "=", "John Doe"]]`

**Options:**  
- `fields`: List of fields to return.
- `limit`: Maximum number of records.
- `offset`: Skip the first N records.

**Result**
Returns a dictionary of the search results.

---

### Authentication

You must authenticate before accessing most data. Use your password or an API key (recommended).

```python
import requests

url = "http://localhost:8069/jsonrpc"
db = "my_database"
username = "admin"
password = "your_password_or_api_key"

payload = {
    "jsonrpc": "2.0",
    "method": "call",
    "params": {
        "service": "common",
        "method": "authenticate",
        "args": [db, username, password, {}]
    },
    "id": 1,
}
response = requests.post(url, json=payload).json()
uid = response.get("result")
if not uid:
    raise Exception("Authentication failed")
print("Authenticated UID:", uid)
```

### Working with Individuals

**Gather The Fields**

For this example we are going to use these fields:

- `name` (string, required)
- `given_name` (string, required)
- `family_name` (string, required)
- `gender` (many2one, required)
- `birthdate` (date, required)
- `is_registrant` (boolean, default=True)
- `is_group` (boolean, default=False)

**Example: Create an Individual**

```python
# First, get a gender_id (e.g., for "Male")
payload = {
    "jsonrpc": "2.0",
    "method": "call",
    "params": {
        "service": "object",
        "method": "execute_kw",
        "args": [
            db, uid, password,
            "gender.type", "search_read",
            [[["code", "=", "Male"]]],
            {"fields": ["id"], "limit": 1}
        ]
    },
    "id": 2,
}
response = requests.post(url, json=payload).json()
gender_id = response["result"][0]["id"]

# Now, create the individual
payload = {
    "jsonrpc": "2.0",
    "method": "call",
    "params": {
        "service": "object",
        "method": "execute_kw",
        "args": [
            db, uid, password,
            "res.partner", "create",
            [{
                "name": "John Doe",
                "given_name": "John",
                "family_name": "Doe",
                "gender": gender_id,
                "birthdate": "1990-01-01",
                "is_registrant": True,
                "is_group": False,
            }]
        ]
    },
    "id": 3,
}
response = requests.post(url, json=payload).json()
individual_id = response["result"]
print("Created Individual ID:", individual_id)

# Update the individual's birthdate
payload = {
    "jsonrpc": "2.0",
    "method": "call",
    "params": {
        "service": "object",
        "method": "execute_kw",
        "args": [
            db, uid, password,
            "res.partner", "write",
            [[individual_id],  # List of IDs to update
            {"birthdate": "1991-02-02"}]  # Fields to update
        ]
    },
    "id": 8,
}
response = requests.post(url, json=payload).json()
updated = response["result"]
print("Result:", updated)
```

### Working with Groups

**Gather The Fields**

For this example we are going to use these fields:

- `name` (string, required)
- `kind` (many2one, required)
- `is_registrant` (boolean, default=True)
- `is_group` (boolean, default=True)


**Example: Create a Group**

```python
# Get a group kind (e.g., "Household")
payload = {
    "jsonrpc": "2.0",
    "method": "call",
    "params": {
        "service": "object",
        "method": "execute_kw",
        "args": [
            db, uid, password,
            "g2p.group.kind", "search_read",
            [[["name", "=", "Household"]]],
            {"fields": ["id"], "limit": 1}
        ]
    },
    "id": 4,
}
response = requests.post(url, json=payload).json()
kind_id = response["result"][0]["id"]

# Create the group
payload = {
    "jsonrpc": "2.0",
    "method": "call",
    "params": {
        "service": "object",
        "method": "execute_kw",
        "args": [
            db, uid, password,
            "res.partner", "create",
            [{
                "name": "Doe Family",
                "kind": kind_id
                "is_registrant": True,
                "is_group": True,
            }]
        ]
    },
    "id": 5,
}
response = requests.post(url, json=payload).json()
group_id = response["result"]
print("Created Group ID:", group_id)

# Update the group's name
payload = {
    "jsonrpc": "2.0",
    "method": "call",
    "params": {
        "service": "object",
        "method": "execute_kw",
        "args": [
            db, uid, password,
            "res.partner", "write",
            [[group_id],  # List of IDs to update
            {"name": "Doe Family Updated"}]  # Fields to update
        ]
    },
    "id": 10,
}
response = requests.post(url, json=payload).json()
updated = response["result"]
print("Result:", updated)
```

### Working with Memberships

**Gather The Fields**

From your `g2p_registry_membership` module, the main model is likely `g2p_registry_membership.group_membership`. Required fields typically include:
- `individuak` (many2one, required)
- `group` (many2one, required)
- `kind` (many2many, required; e.g., "Head", "Member")
- `start_date` (date, required)
- Any other required fields as defined in your model

**Example: Add an Individual to a Group**

```python
# Get a membership kind (e.g., "Head")
payload = {
    "jsonrpc": "2.0",
    "method": "call",
    "params": {
        "service": "object",
        "method": "execute_kw",
        "args": [
            db, uid, password,
            "g2p.group.membership.kind", "search_read",
            [[["name", "=", "Head"]]],
            {"fields": ["id"], "limit": 1}
        ]
    },
    "id": 6,
}
response = requests.post(url, json=payload).json()
kind_id = response["result"][0]["id"]

# Create the membership
payload = {
    "jsonrpc": "2.0",
    "method": "call",
    "params": {
        "service": "object",
        "method": "execute_kw",
        "args": [
            db, uid, password,
            "g2p.group.membership", "create",
            [{
                "individual": individual_id,
                "group": group_id,
                "kind": [[4, kind_id]],
                "start_date": "2025-01-01"
            }]
        ]
    },
    "id": 7,
}
response = requests.post(url, json=payload).json()
membership_id = response["result"]
print("Created Membership ID:", membership_id)
```

### Security: Using API Keys

- **API keys** are recommended over passwords for scripts and integrations.
- Generate API keys in your OpenSPP user preferences under **Account Security**.
- Use the API key in place of your password in all JSON-RPC calls.

## Best Practices

1. **Use API Keys**: Safer than passwords; revoke if compromised.
2. **Limit Permissions**: Create dedicated users for API access with only necessary rights.
3. **Validate Responses**: Always check for errors or unexpected results.
4. **Secure Connections**: Use HTTPS for all API traffic.
5. **Log and Monitor**: Track API usage for auditing and troubleshooting.

## References

- [Odoo 17 Developer Documentation](https://www.odoo.com/documentation/17.0/developer/)
- [JSON-RPC Specification](https://www.jsonrpc.org/specification)