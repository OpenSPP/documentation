---
openspp:
  doc_status: draft
  products: [core]
---

# Error Handling

**For: developers**

The RFC 9457 Problem Detail format used for all API errors, HTTP status codes, and patterns for building resilient clients.

## Prerequisites

- Familiarity with HTTP status codes
- Understanding of [RFC 9457 Problem Details for HTTP APIs](https://www.rfc-editor.org/rfc/rfc9457.html)

## Error Response Format

Standard API errors use **RFC 9457 Problem Detail** format:

```json
{
  "type": "urn:openspp:error:validation",
  "title": "Validation Error",
  "status": 422,
  "detail": "Identifier value contains invalid characters",
  "instance": "/api/v2/spp/Individual",
  "errors": [
    {
      "field": "identifier[0].value",
      "message": "expected pattern ^[A-Z0-9-]+$"
    }
  ]
}
```

### Field Reference

| Field | Type | Description |
|-------|------|-------------|
| `type` | string | Error category URN (e.g., `urn:openspp:error:validation`) |
| `title` | string | Short human-readable summary |
| `status` | integer | HTTP status code |
| `detail` | string | Explanation specific to this occurrence |
| `instance` | string | URI of the specific problem occurrence |
| `errors` | array | Field-level validation errors (for 422 responses) |

### Error Categories

| Type URN | Meaning |
|----------|---------|
| `urn:openspp:error:not-found` | Resource not found (404) |
| `urn:openspp:error:validation` | Validation failure (422) |
| `urn:openspp:error:authentication` | Authentication failure (401) |
| `urn:openspp:error:authorization` | Insufficient permissions (403) |
| `urn:openspp:error:conflict` | Version conflict (409) |
| `urn:openspp:error:server-error` | Internal server error (500) |

```{note}
Batch and transaction error responses use a different format — see {doc}`batch` for `OperationOutcome` details in bundle responses.
```

## HTTP Status Codes

| Code | Meaning | Description |
|------|---------|-------------|
| 200 | OK | Successful read/update |
| 201 | Created | Successful create |
| 400 | Bad Request | Invalid request format |
| 401 | Unauthorized | Missing/invalid token |
| 403 | Forbidden | Insufficient permissions/consent |
| 404 | Not Found | Resource doesn't exist |
| 409 | Conflict | Version conflict (optimistic locking) |
| 422 | Unprocessable Entity | Validation error |
| 429 | Too Many Requests | Rate limit exceeded |
| 500 | Internal Server Error | Server error |
| 503 | Service Unavailable | Server temporarily unavailable |

## Common Errors

### 400 Bad Request

Invalid request syntax or structure:

```json
{
  "type": "urn:openspp:error:validation",
  "title": "Bad Request",
  "status": 400,
  "detail": "Invalid JSON: Unexpected token at line 5"
}
```

**Causes:**
- Malformed JSON
- Invalid parameter names
- Missing required headers

**Solution:**
```python
# ✅ Good - Validate JSON before sending
import json

try:
    data = json.dumps(resource)
    response = requests.post(url, data=data, headers=headers)
except json.JSONDecodeError as e:
    print(f"Invalid JSON: {e}")
```

### 401 Unauthorized

Missing or invalid access token:

```json
{
  "type": "urn:openspp:error:authentication",
  "title": "Unauthorized",
  "status": 401,
  "detail": "Invalid or expired access token"
}
```

**Causes:**
- Token expired (tokens last 24 hours by default)
- Token not provided
- Invalid token format

**Solution:**
```python
def api_request_with_token_refresh(url, token_manager):
    """Make request with automatic token refresh."""
    token = token_manager.get_token()
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(url, headers=headers)

    if response.status_code == 401:
        # Token expired, refresh and retry
        token_manager.refresh_token()
        token = token_manager.get_token()
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(url, headers=headers)

    response.raise_for_status()
    return response.json()
```

### 403 Forbidden

Insufficient permissions or consent:

```json
{
  "type": "urn:openspp:error:authorization",
  "title": "Forbidden",
  "status": 403,
  "detail": "No active consent for this data access"
}
```

**Common Causes:**

| Cause | Description |
|-------|-------------|
| No consent | Registrant hasn't consented to data sharing |
| Expired consent | Consent has expired |
| Insufficient scope | API client lacks the required scope |

**Solution:**
```python
def handle_forbidden_error(response):
    """Handle 403 Forbidden errors."""
    error = response.json()
    detail = error.get("detail", "")

    if "consent" in detail.lower():
        print("No consent on file. Contact registrant for consent.")
    elif "scope" in detail.lower():
        print("Insufficient scope. Contact administrator.")
    else:
        print(f"Access denied: {detail}")
```

### 404 Not Found

Resource doesn't exist:

```json
{
  "type": "urn:openspp:error:not-found",
  "title": "Not Found",
  "status": 404,
  "detail": "Individual with identifier urn:gov:ph:psa:national-id|PH-999 not found"
}
```

**Causes:**
- Wrong identifier
- Resource was deleted
- Typo in URL

**Solution:**
```python
def get_individual_safe(identifier, token, base_url):
    """Fetch individual with 404 handling."""
    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(
            f"{base_url}/Individual/{identifier}",
            headers=headers
        )
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as e:
        if e.response.status_code == 404:
            print(f"Individual not found: {identifier}")
            return None
        raise
```

### 409 Conflict

Version conflict during update:

```json
{
  "type": "urn:openspp:error:conflict",
  "title": "Conflict",
  "status": 409,
  "detail": "Resource version mismatch. Expected: 3, Current: 5"
}
```

**Cause:** Another client modified the resource between your read and update.

**Solution:**
```python
def update_with_conflict_resolution(identifier, updates, token, base_url, max_retries=3):
    """Update with automatic conflict resolution."""
    for attempt in range(max_retries):
        try:
            # Fetch latest version
            headers = {"Authorization": f"Bearer {token}"}
            response = requests.get(
                f"{base_url}/Individual/{identifier}",
                headers=headers
            )
            response.raise_for_status()
            current = response.json()

            # Merge updates
            current.update(updates)

            # Attempt update with current version
            version = current["meta"]["versionId"]
            headers["If-Match"] = f'"{version}"'
            headers["Content-Type"] = "application/json"

            response = requests.put(
                f"{base_url}/Individual/{identifier}",
                headers=headers,
                json=current
            )
            response.raise_for_status()
            return response.json()

        except requests.HTTPError as e:
            if e.response.status_code == 409:
                if attempt < max_retries - 1:
                    print(f"Conflict detected, retrying ({attempt + 1}/{max_retries})...")
                    continue
            raise

    raise Exception("Update failed after max retries")
```

### 422 Unprocessable Entity

Validation error:

```json
{
  "type": "urn:openspp:error:validation",
  "title": "Unprocessable Entity",
  "status": 422,
  "detail": "Validation failed",
  "errors": [
    {
      "field": "birthDate",
      "message": "date must be in the past"
    },
    {
      "field": "name",
      "message": "field is required"
    }
  ]
}
```

**Common Validation Errors:**

| Error | Description |
|-------|-------------|
| Missing required field | A required field was not provided |
| Invalid identifier format | Identifier doesn't match expected pattern |
| Duplicate identifier | Identifier already exists in the system |
| Invalid reference | Referenced resource doesn't exist |

**Solution:**
```python
def handle_validation_errors(response):
    """Parse and handle validation errors."""
    error = response.json()
    errors = []

    for field_error in error.get("errors", []):
        errors.append({
            "field": field_error.get("field", "unknown"),
            "message": field_error.get("message", "")
        })

    return errors

# Usage
try:
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
except requests.HTTPError as e:
    if e.response.status_code == 422:
        errors = handle_validation_errors(e.response)
        print("Validation errors:")
        for error in errors:
            print(f"  {error['field']}: {error['message']}")
            if error['details']:
                print(f"    {error['details']}")
```

### 429 Too Many Requests

Rate limit exceeded:

```http
HTTP/1.1 429 Too Many Requests
X-RateLimit-Limit: 30
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 45
Retry-After: 45

{
  "type": "urn:openspp:error:server-error",
  "title": "Too Many Requests",
  "status": 429,
  "detail": "Rate limit exceeded. Retry after 45 seconds."
}
```

**Rate Limit Headers:**

| Header | Description |
|--------|-------------|
| `X-RateLimit-Limit` | Requests allowed per minute (default: 30) |
| `X-RateLimit-Remaining` | Requests remaining in current window |
| `X-RateLimit-Reset` | Seconds until the limit resets |
| `Retry-After` | Seconds to wait before retrying |

**Default Rate Limits:**

| Endpoint | Per Minute | Per Day |
|----------|-----------|---------|
| General API | 30 | 5,000 |
| OAuth token (`/oauth/token`) | 5 | 50 |

Rate limits are configurable per API client. Contact your administrator for higher limits.

**Solution:**
```python
import time

def api_request_with_rate_limit_handling(url, headers, max_retries=3):
    """Make request with rate limit handling."""
    for attempt in range(max_retries):
        response = requests.get(url, headers=headers)

        if response.status_code == 429:
            retry_after = int(response.headers.get("Retry-After", 60))
            print(f"Rate limited. Waiting {retry_after} seconds...")
            time.sleep(retry_after)
            continue

        response.raise_for_status()
        return response.json()

    raise Exception("Request failed after max retries")
```

### 500 Internal Server Error

Server-side error:

```json
{
  "type": "urn:openspp:error:server-error",
  "title": "Internal Server Error",
  "status": 500,
  "detail": "Internal server error. Please contact support."
}
```

**Solution:**
```python
def api_request_with_retry(url, headers, max_retries=3):
    """Make request with exponential backoff."""
    import time

    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.HTTPError as e:
            if e.response.status_code == 500:
                if attempt < max_retries - 1:
                    wait_time = 2 ** attempt  # Exponential backoff
                    print(f"Server error, retrying in {wait_time}s...")
                    time.sleep(wait_time)
                    continue
            raise

    raise Exception("Request failed after max retries")
```

## Error Handling Best Practices

### 1. Always Check Status Codes

```python
# ✅ Good - Check status explicitly
response = requests.get(url, headers=headers)
if response.status_code == 200:
    data = response.json()
elif response.status_code == 404:
    print("Resource not found")
elif response.status_code == 403:
    print("Access denied")
else:
    response.raise_for_status()

# ❌ Bad - Assume success
response = requests.get(url, headers=headers)
data = response.json()  # Crashes on error
```

### 2. Parse Error Responses

```python
def parse_error_response(response):
    """Extract error details from ProblemDetail response."""
    if not response.ok:
        try:
            error = response.json()
            error_type = error.get("type", "unknown")
            title = error.get("title", "Error")
            detail = error.get("detail", "Unknown error")
            print(f"[{title}] {detail}")

            # Print field-level errors if present (422 responses)
            for field_error in error.get("errors", []):
                print(f"  {field_error['field']}: {field_error['message']}")
        except Exception:
            print(f"HTTP {response.status_code}: {response.text}")
```

### 3. Implement Retry Logic

```python
from typing import Callable
import time

def retry_with_backoff(
    func: Callable,
    max_retries: int = 3,
    initial_delay: float = 1.0,
    backoff_factor: float = 2.0,
    retryable_statuses: set = {429, 500, 502, 503, 504}
):
    """Retry function with exponential backoff."""
    delay = initial_delay

    for attempt in range(max_retries):
        try:
            return func()
        except requests.HTTPError as e:
            if e.response.status_code not in retryable_statuses:
                raise  # Don't retry non-retryable errors

            if attempt == max_retries - 1:
                raise  # Last attempt, give up

            print(f"Request failed (attempt {attempt + 1}/{max_retries}), retrying in {delay}s...")
            time.sleep(delay)
            delay *= backoff_factor

# Usage
result = retry_with_backoff(
    lambda: requests.get(url, headers=headers).json()
)
```

### 4. Log Errors Properly

```python
import logging

logger = logging.getLogger(__name__)

def api_request_with_logging(url, headers):
    """Make request with comprehensive error logging."""
    try:
        logger.info(f"Requesting: {url}")
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        logger.info(f"Success: {response.status_code}")
        return response.json()
    except requests.HTTPError as e:
        logger.error(f"HTTP Error: {e.response.status_code} {e.response.reason}")
        logger.error(f"URL: {url}")
        logger.error(f"Response: {e.response.text}")
        raise
    except requests.RequestException as e:
        logger.error(f"Request failed: {str(e)}")
        raise
```

### 5. Handle Network Errors

```python
import requests
from requests.exceptions import ConnectionError, Timeout

def api_request_with_error_handling(url, headers, timeout=30):
    """Make request with comprehensive error handling."""
    try:
        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()
        return response.json()
    except ConnectionError:
        print("Connection error. Check network connectivity.")
        raise
    except Timeout:
        print(f"Request timed out after {timeout}s")
        raise
    except requests.HTTPError as e:
        print(f"HTTP error: {e.response.status_code}")
        parse_operation_outcome(e.response)
        raise
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        raise
```

## Complete Error Handler

```python
import requests
import time
import logging
from typing import Optional, Dict, Callable

logger = logging.getLogger(__name__)

class APIErrorHandler:
    """Comprehensive API error handler."""

    def __init__(self, max_retries: int = 3, base_delay: float = 1.0):
        self.max_retries = max_retries
        self.base_delay = base_delay

    def make_request(
        self,
        method: str,
        url: str,
        headers: Dict,
        json_data: Optional[Dict] = None,
        timeout: int = 30
    ) -> Dict:
        """
        Make API request with comprehensive error handling.

        Args:
            method: HTTP method (GET, POST, PUT, etc.)
            url: Request URL
            headers: Request headers
            json_data: JSON body (for POST/PUT)
            timeout: Request timeout in seconds

        Returns:
            Response JSON

        Raises:
            APIError: On unrecoverable errors
        """
        for attempt in range(self.max_retries):
            try:
                logger.info(f"{method} {url} (attempt {attempt + 1}/{self.max_retries})")

                response = requests.request(
                    method,
                    url,
                    headers=headers,
                    json=json_data,
                    timeout=timeout
                )

                # Handle rate limiting
                if response.status_code == 429:
                    retry_after = int(response.headers.get("Retry-After", 60))
                    logger.warning(f"Rate limited. Waiting {retry_after}s...")
                    time.sleep(retry_after)
                    continue

                # Handle server errors with retry
                if response.status_code >= 500:
                    if attempt < self.max_retries - 1:
                        delay = self.base_delay * (2 ** attempt)
                        logger.warning(f"Server error {response.status_code}. Retrying in {delay}s...")
                        time.sleep(delay)
                        continue

                # Handle other errors
                if not response.ok:
                    self._handle_error(response)

                return response.json()

            except requests.Timeout:
                logger.error(f"Request timed out after {timeout}s")
                if attempt < self.max_retries - 1:
                    delay = self.base_delay * (2 ** attempt)
                    time.sleep(delay)
                    continue
                raise

            except requests.ConnectionError as e:
                logger.error(f"Connection error: {str(e)}")
                if attempt < self.max_retries - 1:
                    delay = self.base_delay * (2 ** attempt)
                    time.sleep(delay)
                    continue
                raise

        raise Exception(f"Request failed after {self.max_retries} attempts")

    def _handle_error(self, response):
        """Handle error responses."""
        try:
            error = response.json()
            error_type = error.get("type", "unknown")
            title = error.get("title", "Error")
            detail = error.get("detail", "Unknown error")

            logger.error(f"API error {response.status_code} ({error_type}):")
            logger.error(f"  {title}: {detail}")

            # Log field-level errors if present
            for field_error in error.get("errors", []):
                logger.error(f"  Field '{field_error['field']}': {field_error['message']}")

        except Exception:
            logger.error(f"HTTP {response.status_code}: {response.text}")

        response.raise_for_status()

# Usage
handler = APIErrorHandler(max_retries=3)

try:
    result = handler.make_request(
        method="GET",
        url="https://{your-domain}/api/v2/spp/Individual/...",
        headers={"Authorization": f"Bearer {token}"}
    )
    print("Success:", result)
except requests.HTTPError as e:
    print(f"Request failed: {e}")
```

## Common mistakes

**Getting errors you don't understand?**

Check the `diagnostics` field for technical details. Search the error code in the documentation.

**Retries not working?**

Verify you're only retrying retryable errors (429, 500, 502, 503). Don't retry 400, 401, 403, 404, or 422.

**Error messages not helpful?**

Enable debug logging: `logging.basicConfig(level=logging.DEBUG)`. This shows full request/response details.

**Errors in production but not development?**

Check if production has different rate limits, timeouts, or network conditions. Add retry logic with exponential backoff.

**Transaction failing partway through?**

Transaction bundles should rollback fully. If not, report as a bug. Check that you're using `type: "transaction"`, not `"batch"`.

## What's next

- {doc}`authentication` - OAuth 2.0 setup
- {doc}`resources` - Available resources
- {doc}`batch` - Batch operations
- {doc}`consent` - Consent-based access

## See also

- [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) - HTTP status reference
- [RFC 9457: Problem Details for HTTP APIs](https://www.rfc-editor.org/rfc/rfc9457) - Error response format standard
