---
openspp:
  doc_status: draft
  products: [core]
---

# Tutorial: build a Python API client

**For: developers**

This tutorial walks you through building a working Python client that authenticates with OpenSPP API V2, looks up individuals by external identifier, handles consent-filtered responses, and creates new records. By the end, you will have a reusable client module you can extend for your integration.

## Prerequisites

- Python 3.11+ with `requests` installed (`pip install requests`)
- An OpenSPP deployment with `spp_api_v2` installed
- API client credentials — client ID, client secret, and scopes (ask your OpenSPP administrator to register a client if you do not have one; see {doc}`authentication`)
- Basic familiarity with OAuth 2.0 and REST APIs

## What you will build

A minimal but production-ready client that:

| Feature | API V2 concept |
|---------|---------------|
| Acquires an OAuth access token and caches it until expiry | {doc}`authentication` |
| Reads an Individual by national ID | {doc}`external_identifiers` |
| Searches for individuals by name | {doc}`search` |
| Creates a new Individual | {doc}`resources` |
| Handles consent-filtered responses | {doc}`consent` |
| Parses RFC 9457 error responses | {doc}`errors` |

The final module is ~180 lines of Python. Code blocks below are complete and copy-pasteable.

## Project structure

Create a directory for your client:

```text
openspp_client/
├── __init__.py
├── client.py
└── test_client.py
```

## Step 1: scaffold and configuration

### `__init__.py`

```python
from .client import OpenSPPClient, OpenSPPAPIError

__all__ = ["OpenSPPClient", "OpenSPPAPIError"]
```

### `client.py` — imports and exception class

Start the client module with imports and a custom exception that carries RFC 9457 error details:

```python
"""Minimal OpenSPP API V2 client."""

import time
from typing import Any
from urllib.parse import quote

import requests


class OpenSPPAPIError(Exception):
    """Raised when the API returns a 4xx/5xx response."""

    def __init__(self, status: int, detail: str, body: dict | None = None):
        self.status = status
        self.detail = detail
        self.body = body or {}
        super().__init__(f"HTTP {status}: {detail}")
```

**Key patterns to notice:**

- API V2 currently returns errors in FastAPI's default shape: `{"detail": "..."}`. The exception captures the HTTP status and the detail message — that's what every error response gives you today. See {doc}`errors` for the planned richer Problem Detail format.
- `urllib.parse.quote` is imported for URL-encoding namespace URIs. Real OpenSPP identifier systems contain `#` (e.g., `urn:openspp:vocab:id-type#national_id`), and `#` is the URL fragment delimiter — it MUST be encoded as `%23` or the server only sees the part before it.

## Step 2: token acquisition and caching

Add the client class with OAuth 2.0 client credentials flow. The token has an expiration — the client caches it and re-fetches only when needed:

```python
class OpenSPPClient:
    """Thin wrapper around OpenSPP API V2 endpoints."""

    def __init__(self, base_url: str, client_id: str, client_secret: str):
        self.base_url = base_url.rstrip("/")
        self.client_id = client_id
        self.client_secret = client_secret
        self._token: str | None = None
        self._token_expiry: float = 0.0

    def _get_token(self) -> str:
        """Return a cached token, refreshing if expired."""
        if self._token and time.time() < self._token_expiry - 60:
            return self._token

        response = requests.post(
            f"{self.base_url}/oauth/token",
            json={
                "grant_type": "client_credentials",
                "client_id": self.client_id,
                "client_secret": self.client_secret,
            },
            timeout=30,
        )
        response.raise_for_status()
        payload = response.json()

        self._token = payload["access_token"]
        # Refresh 60 seconds before true expiry to avoid races
        self._token_expiry = time.time() + payload["expires_in"]
        return self._token

    def _headers(self) -> dict[str, str]:
        return {
            "Authorization": f"Bearer {self._get_token()}",
            "Content-Type": "application/json",
        }
```

**Key patterns to notice:**

- The token is cached in memory and only refreshed when it's within 60 seconds of expiring. Production clients may want a more sophisticated strategy (e.g., refresh on 401, share tokens across workers).
- `timeout=30` is essential — never make requests without a timeout, or a stalled server can hang your client indefinitely.
- Each HTTP call fetches fresh headers via `_headers()`, which transparently refreshes the token if needed.
- The OAuth endpoint accepts JSON body, form-encoded body, or HTTP Basic auth (per RFC 6749, form-encoded is the standard). JSON works for OpenSPP — we use it for simplicity. Default token lifetime is 24 hours (configurable per deployment).

## Step 3: generic request helper with error handling

Add a helper that routes every request through a single code path for error handling and consent-header capture:

```python
    def _request(
        self,
        method: str,
        path: str,
        params: dict | None = None,
        json_body: dict | None = None,
    ) -> tuple[dict, dict]:
        """Issue an authenticated request. Returns (body, headers).

        Raises OpenSPPAPIError for 4xx/5xx responses.
        """
        response = requests.request(
            method,
            f"{self.base_url}{path}",
            headers=self._headers(),
            params=params,
            json=json_body,
            timeout=30,
        )

        if response.status_code >= 400:
            try:
                body = response.json()
                detail = body.get("detail", str(body))
            except ValueError:
                body = None
                detail = response.text or response.reason
            raise OpenSPPAPIError(response.status_code, detail, body)

        return response.json(), dict(response.headers)
```

**Key patterns to notice:**

- The helper returns `(body, headers)` as a tuple — consent information is only in headers (`X-Consent-Status`, `X-Consent-Scope`), so callers need access to both.
- On failure, we extract `detail` from the JSON body (FastAPI's standard error key) and raise `OpenSPPAPIError`. If the body isn't JSON (e.g., a 502 from a proxy), we fall back to the response text.

## Step 4: read by external identifier

Now the first real endpoint. External identifiers use `system|value` format, with `system` URL-encoded:

```python
    def get_individual(self, system: str, value: str) -> dict:
        """Fetch an Individual by external identifier.

        Args:
            system: Namespace URI, e.g., "urn:openspp:vocab:id-type#national_id"
            value: Identifier value, e.g., "IND-001"

        Returns:
            The Individual resource. Check ``_consent`` key for consent status.
        """
        encoded_system = quote(system, safe="")
        identifier = f"{encoded_system}|{value}"
        body, headers = self._request("GET", f"/Individual/{identifier}")

        # Surface consent status to the caller
        consent_status = headers.get("X-Consent-Status")
        if consent_status and consent_status != "active":
            body.setdefault("_consent", {})["status"] = consent_status

        return body
```

**Key patterns to notice:**

- `quote(system, safe="")` URL-encodes the namespace URI — without `safe=""`, the colons in `urn:gov:ph:...` would pass through and break some servers.
- When consent is not `active`, the response body may contain only the identifier. The client annotates `body["_consent"]["status"]` so the caller can detect this without inspecting headers separately.

## Step 5: search individuals

Searches use query parameters and return a `SearchResult` envelope:

```python
    def search_individuals(
        self,
        name: str | None = None,
        birthdate: str | None = None,
        count: int = 20,
        offset: int = 0,
    ) -> dict:
        """Search Individuals. Returns a SearchResult envelope.

        The envelope contains ``data`` (array of Individual resources),
        ``meta`` (total/count/offset), and ``links`` (self/next/prev).
        """
        params: dict[str, Any] = {"_count": count, "_offset": offset}
        if name:
            params["name"] = name
        if birthdate:
            params["birthdate"] = birthdate

        body, _ = self._request("GET", "/Individual", params=params)
        return body

    def iter_search_individuals(self, **kwargs) -> "list[dict]":
        """Iterate all pages of a search by following ``links.next``."""
        results = []
        page = self.search_individuals(**kwargs)

        while True:
            results.extend(page["data"])

            next_url = page.get("links", {}).get("next")
            if not next_url:
                break

            # Follow the absolute path the server returned (it includes
            # the correct _offset, which may differ from a naive +count
            # when consent filtering is applied).
            path = next_url.split(self.base_url, 1)[-1]
            page, _ = self._request("GET", path)

        return results
```

**Key patterns to notice:**

- The `_count` and `_offset` parameters are prefixed with underscore per FHIR convention; resource-specific filters like `name` and `birthdate` are not.
- The Individual search endpoint requires the `individual:read` scope (not a separate `individual:search`). See {doc}`authentication` for the full scope matrix.
- `iter_search_individuals` follows `links.next` rather than incrementing offset locally. This matters when consent filtering is active: the server may skip records the client cannot see, and only the returned `next` URL has the correct offset.

## Step 6: create an individual

Creates use `POST` with the resource body. On success, the response is the created resource with any server-assigned fields:

```python
    def create_individual(
        self,
        identifier_system: str,
        identifier_value: str,
        given_name: str,
        family_name: str,
        birth_date: str | None = None,
    ) -> dict:
        """Create a new Individual record."""
        body = {
            "type": "Individual",
            "identifier": [
                {"system": identifier_system, "value": identifier_value}
            ],
            "name": {"given": given_name, "family": family_name},
        }
        if birth_date:
            body["birthDate"] = birth_date

        response_body, _ = self._request("POST", "/Individual", json_body=body)
        return response_body
```

**Key patterns to notice:**

- The request body uses `"type": "Individual"` (not `"resourceType"`) — API V2 uses the simpler modernized format (see {doc}`overview`).
- The server responds with `201 Created` and a `Location` header pointing to the new resource (e.g., `/api/v2/spp/Individual/urn:openspp:vocab:id-type%23national_id|IND-001`). For a richer client, capture the `Location` header from the response — it gives you the canonical URL of the resource you just created.
- At least one identifier is required, and its `system` URI must already exist as a vocabulary code in the deployment. Otherwise you'll get a 422 with a message like `Invalid identifier type: system='...'`.

## Step 7: test the client

Create `test_client.py` with tests that cover both happy paths and error cases:

```python
"""Integration tests for OpenSPPClient.

These tests hit a real OpenSPP deployment and require the OPENSPP_* environment
variables to be set. Skip when not configured.
"""

import os
import unittest
import uuid

from openspp_client import OpenSPPClient, OpenSPPAPIError


@unittest.skipUnless(
    all(os.getenv(k) for k in ("OPENSPP_BASE_URL", "OPENSPP_CLIENT_ID", "OPENSPP_CLIENT_SECRET")),
    "Set OPENSPP_BASE_URL, OPENSPP_CLIENT_ID, OPENSPP_CLIENT_SECRET to run",
)
class OpenSPPClientTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = OpenSPPClient(
            base_url=os.environ["OPENSPP_BASE_URL"],
            client_id=os.environ["OPENSPP_CLIENT_ID"],
            client_secret=os.environ["OPENSPP_CLIENT_SECRET"],
        )

    def test_token_acquisition(self):
        """Token fetch returns a non-empty bearer token."""
        token = self.client._get_token()
        self.assertIsInstance(token, str)
        self.assertGreater(len(token), 20)

    def test_token_is_cached(self):
        """Second _get_token call returns the cached token (no new HTTP)."""
        first = self.client._get_token()
        second = self.client._get_token()
        self.assertEqual(first, second)

    # Use a vocabulary code that exists in your deployment.
    # The default seeds include "national_id" — adjust if your deployment uses a different code.
    ID_SYSTEM = "urn:openspp:vocab:id-type#national_id"

    def test_get_individual_missing_raises(self):
        """A missing identifier raises OpenSPPAPIError.

        The status will be 404 if the API client has require_consent=False,
        or 403 if require_consent=True (the default — masks 404 to prevent
        enumeration attacks). Both indicate "no accessible record."
        """
        with self.assertRaises(OpenSPPAPIError) as ctx:
            self.client.get_individual(
                self.ID_SYSTEM, f"nonexistent-{uuid.uuid4()}"
            )
        self.assertIn(ctx.exception.status, (403, 404))

    def test_search_returns_envelope(self):
        """Search returns a SearchResult envelope with data/meta/links."""
        result = self.client.search_individuals(count=5)
        self.assertIn("data", result)
        self.assertIn("meta", result)
        self.assertIn("links", result)
        self.assertIn("total", result["meta"])

    def test_create_and_read_round_trip(self):
        """Created resource can be read back by identifier.

        Requires the vocabulary code in ID_SYSTEM to exist in the deployment
        AND the API client to have ``individual:create`` and ``individual:read``
        scopes. See {doc}`authentication` for scope setup.
        """
        value = f"tutorial-{uuid.uuid4().hex[:12]}"

        created = self.client.create_individual(
            identifier_system=self.ID_SYSTEM,
            identifier_value=value,
            given_name="Tutorial",
            family_name="Example",
            birth_date="1990-01-01",
        )
        self.assertEqual(created["type"], "Individual")

        fetched = self.client.get_individual(self.ID_SYSTEM, value)
        self.assertEqual(fetched["name"]["given"], "Tutorial")


if __name__ == "__main__":
    unittest.main()
```

**Key patterns to notice:**

- Tests are **integration tests** that hit a real deployment. They skip cleanly when credentials aren't configured, so they won't fail in CI environments without API access.
- `test_token_is_cached` verifies the caching logic — an important behavior because token acquisition adds latency to every call if not cached.
- The round-trip test uses a unique UUID-suffixed identifier so repeated runs don't collide.

## Verify it works

Set your credentials and run the tests:

```bash
export OPENSPP_BASE_URL="https://your-openspp.example.org/api/v2/spp"
export OPENSPP_CLIENT_ID="your-client-id"
export OPENSPP_CLIENT_SECRET="your-client-secret"

python -m unittest test_client.py
```

Or try the client interactively:

```python
from openspp_client import OpenSPPClient

client = OpenSPPClient(
    base_url="https://your-openspp.example.org/api/v2/spp",
    client_id="your-client-id",
    client_secret="your-client-secret",
)

# Search
results = client.search_individuals(name="Santos", count=10)
print(f"Found {results['meta']['total']} matches")

# Read by external identifier — the system URI must match a vocabulary code
# registered in your deployment. The default seeds include "national_id".
individual = client.get_individual(
    "urn:openspp:vocab:id-type#national_id", "IND-001"
)
print(individual["name"])
```

```{tip}
Identifier system URIs in OpenSPP follow the format `urn:openspp:vocab:id-type#<code>`, where `<code>` matches a registered vocabulary code (see `spp.vocabulary.code` in your deployment). Ask your administrator which codes are available, or query the vocabulary endpoint if `spp_api_v2_vocabulary` is installed.
```

## What's next

You now have a working client. To extend it for real integrations:

- {doc}`authentication` — token refresh on 401, scope management, JWT introspection
- {doc}`search` — advanced filters, sorting, sparse fieldsets, complex queries via POST
- {doc}`batch` — transaction bundles for atomic multi-resource operations
- {doc}`consent` — consent-aware client patterns, handling filtered responses
- {doc}`errors` — retry logic with exponential backoff, handling 429 rate limits
- {doc}`studio_integration` — request Studio-extended fields via `_extensions`

## See also

- {doc}`overview` — API V2 design philosophy and base URL
- {doc}`resources` — complete Individual, Group, Program, ProgramMembership, Consent reference
- {doc}`external_identifiers` — namespace URI format and common identifier systems
