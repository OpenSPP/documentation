---
openspp:
  doc_status: draft
  products: [core]
---

# Authentication

This guide is for **developers** implementing OAuth 2.0 authentication for OpenSPP API V2.

## Authentication Flow

OpenSPP API V2 uses **OAuth 2.0 Client Credentials** flow for machine-to-machine authentication.

```
┌────────┐                              ┌────────────┐
│ Client │──(1) POST /oauth/token──────►│  OpenSPP   │
│        │     client_id, client_secret │   OAuth    │
│        │◄─(2) access_token────────────│   Server   │
│        │                              └────────────┘
│        │──(3) GET /api/v2/spp/...────►┌────────────┐
│        │     Authorization: Bearer    │  OpenSPP   │
│        │◄─(4) Response────────────────│    API     │
└────────┘                              └────────────┘
```

## Prerequisites

Before you can authenticate:

1. Your application must be registered in OpenSPP
2. You must have a **Client ID** and **Client Secret**
3. Your client must have authorized **scopes**

Contact your OpenSPP administrator to register your application.

## Obtaining an Access Token

### Request

```text
POST /api/v2/spp/oauth/token
Content-Type: application/json

{
  "grant_type": "client_credentials",
  "client_id": "ministry-of-agriculture",
  "client_secret": "your-secret-key-here"
}
```

### Response

```json
{
  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "Bearer",
  "expires_in": 3600,
  "scope": "individual:read individual:search group:read"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `access_token` | string | JWT token for API requests |
| `token_type` | string | Always "Bearer" |
| `expires_in` | integer | Token lifetime in seconds (3600 = 1 hour) |
| `scope` | string | Space-separated list of granted scopes |

### Example: curl

```bash
curl -X POST https://api.openspp.org/api/v2/spp/oauth/token \
  -H "Content-Type: application/json" \
  -d '{
    "grant_type": "client_credentials",
    "client_id": "ministry-of-agriculture",
    "client_secret": "your-secret-key-here"
  }'
```

### Example: Python (requests)

```python
import requests

def get_access_token(client_id, client_secret, base_url):
    """Obtain an OAuth 2.0 access token."""
    response = requests.post(
        f"{base_url}/oauth/token",
        json={
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret
        }
    )
    response.raise_for_status()
    return response.json()["access_token"]

# Usage
token = get_access_token(
    client_id="ministry-of-agriculture",
    client_secret="your-secret-key-here",
    base_url="https://api.openspp.org/api/v2/spp"
)
print(f"Token: {token}")
```

### Example: JavaScript (fetch)

```javascript
async function getAccessToken(clientId, clientSecret, baseUrl) {
  const response = await fetch(`${baseUrl}/oauth/token`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      grant_type: 'client_credentials',
      client_id: clientId,
      client_secret: clientSecret
    })
  });

  if (!response.ok) {
    throw new Error(`Token request failed: ${response.statusText}`);
  }

  const data = await response.json();
  return data.access_token;
}

// Usage
const token = await getAccessToken(
  'ministry-of-agriculture',
  'your-secret-key-here',
  'https://api.openspp.org/api/v2/spp'
);
console.log('Token:', token);
```

## Using the Access Token

Include the token in the `Authorization` header of all API requests:

```text
GET /api/v2/spp/Individual/urn:gov:ph:psa:national-id|PH-123456789
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...
```

### Example: curl

```bash
curl https://api.openspp.org/api/v2/spp/Individual/urn:gov:ph:psa:national-id|PH-123456789 \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Example: Python

```python
import requests

def get_individual(identifier, token, base_url):
    """Fetch an individual using an access token."""
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
print(individual)
```

### Example: JavaScript

```javascript
async function getIndividual(identifier, token, baseUrl) {
  const response = await fetch(`${baseUrl}/Individual/${identifier}`, {
    headers: {
      'Authorization': `Bearer ${token}`
    }
  });

  if (!response.ok) {
    throw new Error(`API request failed: ${response.statusText}`);
  }

  return await response.json();
}

// Usage
const individual = await getIndividual(
  'urn:gov:ph:psa:national-id|PH-123456789',
  token,
  'https://api.openspp.org/api/v2/spp'
);
console.log(individual);
```

## Token Management

### Token Expiration

Access tokens expire after **1 hour** (3600 seconds). You must request a new token when the current one expires.

### Token Refresh Strategy

Since client credentials don't support refresh tokens, implement a proactive refresh strategy:

```python
import requests
from datetime import datetime, timedelta

class TokenManager:
    """Manage OAuth 2.0 access tokens with automatic refresh."""

    def __init__(self, client_id, client_secret, base_url):
        self.client_id = client_id
        self.client_secret = client_secret
        self.base_url = base_url
        self.token = None
        self.expires_at = None

    def get_token(self):
        """Get a valid access token, refreshing if necessary."""
        if self.token is None or self._is_expired():
            self._refresh_token()
        return self.token

    def _is_expired(self):
        """Check if token is expired or about to expire (5 min buffer)."""
        if self.expires_at is None:
            return True
        return datetime.now() >= self.expires_at - timedelta(minutes=5)

    def _refresh_token(self):
        """Request a new access token."""
        response = requests.post(
            f"{self.base_url}/oauth/token",
            json={
                "grant_type": "client_credentials",
                "client_id": self.client_id,
                "client_secret": self.client_secret
            }
        )
        response.raise_for_status()

        data = response.json()
        self.token = data["access_token"]
        expires_in = data["expires_in"]
        self.expires_at = datetime.now() + timedelta(seconds=expires_in)

# Usage
token_manager = TokenManager(
    client_id="ministry-of-agriculture",
    client_secret="your-secret-key-here",
    base_url="https://api.openspp.org/api/v2/spp"
)

# Always get fresh token
token = token_manager.get_token()
```

### Handling 401 Unauthorized

If you receive a 401 response, your token has expired or is invalid:

```python
def api_request_with_retry(url, token_manager):
    """Make API request with automatic token refresh on 401."""
    token = token_manager.get_token()
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(url, headers=headers)

    if response.status_code == 401:
        # Token expired, force refresh
        token_manager._refresh_token()
        token = token_manager.get_token()
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(url, headers=headers)

    response.raise_for_status()
    return response.json()
```

## Scopes

Scopes define what your API client can access. Common scopes:

| Scope | Description |
|-------|-------------|
| `individual:read` | Read individual registrants |
| `individual:search` | Search individuals |
| `individual:create` | Create new individuals |
| `individual:update` | Update existing individuals |
| `group:read` | Read groups/households |
| `group:search` | Search groups |
| `program:read` | Read program definitions |
| `program_membership:read` | Read program enrollments |
| `program_membership:create` | Enroll beneficiaries |

Your administrator configures which scopes your client receives.

### Checking Your Scopes

The token response includes granted scopes:

```json
{
  "access_token": "...",
  "scope": "individual:read individual:search group:read"
}
```

### Scope Errors

If you attempt an operation without the required scope:

```text
HTTP/1.1 403 Forbidden
Content-Type: application/json

{
  "resourceType": "OperationOutcome",
  "issue": [
    {
      "severity": "error",
      "code": "forbidden",
      "details": {
        "coding": [
          {
            "system": "urn:openspp:error",
            "code": "SCOPE_INSUFFICIENT",
            "display": "Insufficient scope"
          }
        ],
        "text": "Required scope: individual:create. Granted: individual:read, individual:search"
      }
    }
  ]
}
```

## Security Best Practices

### Protect Your Client Secret

**Never expose your client secret in:**
- Public repositories (GitHub, GitLab, etc.)
- Client-side code (JavaScript in browsers)
- Log files or error messages
- Environment variables in CI/CD without encryption

**Store secrets securely:**

```python
# ✅ Good: Read from environment variable
import os
client_secret = os.environ["OPENSPP_CLIENT_SECRET"]

# ✅ Good: Use secrets management service
from aws_secretsmanager import get_secret
client_secret = get_secret("openspp/client_secret")

# ❌ Bad: Hardcoded
client_secret = "abc123secret"  # Never do this!
```

### Rotate Credentials Regularly

Contact your administrator to rotate your client secret periodically (e.g., every 90 days).

### Use HTTPS Only

**Always** use HTTPS endpoints in production. Never send credentials or tokens over HTTP.

```python
# ✅ Good
base_url = "https://api.openspp.org/api/v2/spp"

# ❌ Bad (development only)
base_url = "http://localhost:8069/api/v2/spp"
```

### Limit Token Lifetime

Tokens expire after 1 hour. This limits the exposure window if a token is compromised.

### Monitor for Unauthorized Usage

Check API logs regularly for:
- Failed authentication attempts
- Access from unexpected IP addresses
- Unusual request patterns

## Error Responses

### 401 Unauthorized

Token is missing, invalid, or expired:

```json
{
  "resourceType": "OperationOutcome",
  "issue": [
    {
      "severity": "error",
      "code": "unauthorized",
      "details": {
        "text": "Invalid or expired access token"
      }
    }
  ]
}
```

**Solution:** Request a new access token.

### 400 Bad Request

Invalid token request:

```json
{
  "error": "invalid_client",
  "error_description": "Invalid client credentials"
}
```

**Solution:** Verify your client ID and secret are correct.

### 403 Forbidden

Valid token, but insufficient permissions:

```json
{
  "resourceType": "OperationOutcome",
  "issue": [
    {
      "severity": "error",
      "code": "forbidden",
      "details": {
        "coding": [
          {
            "system": "urn:openspp:error",
            "code": "SCOPE_INSUFFICIENT"
          }
        ]
      }
    }
  ]
}
```

**Solution:** Request additional scopes from your administrator.

## Are You Stuck?

**Getting "invalid_client" error?**

Double-check your client ID and secret. Ensure there are no extra spaces or line breaks when copying credentials.

**Token request hangs or times out?**

Check your network connection and firewall rules. Ensure you can reach the OAuth server endpoint.

**Getting 401 on all requests despite valid token?**

Your API client may be disabled. Contact your administrator to verify your client is active.

**Scopes in token don't match what you expected?**

Scopes are configured server-side. Contact your administrator to update your client's scope configuration.

## Complete Example

```python
import requests
from datetime import datetime, timedelta

class OpenSPPClient:
    """Complete OpenSPP API client with authentication."""

    def __init__(self, client_id, client_secret, base_url):
        self.client_id = client_id
        self.client_secret = client_secret
        self.base_url = base_url
        self.token = None
        self.expires_at = None

    def _get_token(self):
        """Get a valid access token."""
        if self.token is None or self._is_expired():
            self._refresh_token()
        return self.token

    def _is_expired(self):
        """Check if token needs refresh."""
        if self.expires_at is None:
            return True
        return datetime.now() >= self.expires_at - timedelta(minutes=5)

    def _refresh_token(self):
        """Request new access token."""
        response = requests.post(
            f"{self.base_url}/oauth/token",
            json={
                "grant_type": "client_credentials",
                "client_id": self.client_id,
                "client_secret": self.client_secret
            }
        )
        response.raise_for_status()

        data = response.json()
        self.token = data["access_token"]
        self.expires_at = datetime.now() + timedelta(seconds=data["expires_in"])

    def _request(self, method, path, **kwargs):
        """Make authenticated API request."""
        token = self._get_token()
        headers = kwargs.pop("headers", {})
        headers["Authorization"] = f"Bearer {token}"

        response = requests.request(
            method,
            f"{self.base_url}/{path}",
            headers=headers,
            **kwargs
        )

        # Retry once on 401
        if response.status_code == 401:
            self._refresh_token()
            token = self._get_token()
            headers["Authorization"] = f"Bearer {token}"
            response = requests.request(
                method,
                f"{self.base_url}/{path}",
                headers=headers,
                **kwargs
            )

        response.raise_for_status()
        return response.json()

    def get_individual(self, identifier):
        """Fetch an individual by identifier."""
        return self._request("GET", f"Individual/{identifier}")

    def search_individuals(self, **params):
        """Search for individuals."""
        return self._request("GET", "Individual", params=params)

    def create_individual(self, data):
        """Create a new individual."""
        return self._request("POST", "Individual", json=data)

# Usage
client = OpenSPPClient(
    client_id="ministry-of-agriculture",
    client_secret="your-secret-key-here",
    base_url="https://api.openspp.org/api/v2/spp"
)

# Fetch individual
individual = client.get_individual("urn:gov:ph:psa:national-id|PH-123456789")
print(individual)

# Search
results = client.search_individuals(name="Santos")
print(f"Found {results['total']} individuals")
```

## Next Steps

- {doc}`resources` - Learn about available API resources
- {doc}`search` - Advanced search and filtering
- {doc}`consent` - Understanding consent-based access control
- {doc}`errors` - Complete error handling guide

## See Also

- [OAuth 2.0 RFC 6749](https://datatracker.ietf.org/doc/html/rfc6749) - OAuth standard
- [JWT RFC 7519](https://datatracker.ietf.org/doc/html/rfc7519) - JSON Web Tokens
