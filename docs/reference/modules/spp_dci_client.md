---
openspp:
  doc_status: draft
---

# DCI Client

This module is for **developers** and **sys admins** who need to connect OpenSPP to external DCI-compliant registries.

## Overview

DCI Client provides the base infrastructure for connecting to external registries and data sources using Digital Convergence Initiative (DCI) API standards. It handles OAuth2 authentication and data source management, enabling interoperability with civil registration systems, disability registries, and identity bureaus.

This is a foundation module. Install specialized client modules for specific registry types:

| Module | Connects To |
|--------|-------------|
| `spp_dci_client_crvs` | Civil Registration and Vital Statistics |
| `spp_dci_client_dr` | Disability Registry |
| `spp_dci_client_ibr` | Identity Bureau Registry |

## Module Information

| Property | Value |
|----------|-------|
| Technical Name | `spp_dci_client` |
| Version | 19.0.1.0.0 |
| Category | OpenSPP/Integration |
| License | LGPL-3 |
| Application | No |
| Status | Alpha |

### Dependencies

| Module | Purpose |
|--------|---------|
| `base` | Odoo core framework |
| `spp_dci` | DCI standards and schemas |

### External Python Dependencies

| Package | Purpose |
|---------|---------|
| `httpx` | Async HTTP client for API calls |

## Data Models

| Model | Purpose |
|-------|---------|
| `spp.dci.data.source` | Data source connection configuration |

## Configuration

### Create a Data Source

Navigate to **DCI > Configuration > Data Sources** and create a new record:

| Field | Description | Example |
|-------|-------------|---------|
| Name | Descriptive name for the data source | National CRVS Registry |
| Base URL | API endpoint base URL | `https://api.crvs.gov.example/v1` |
| Auth URL | OAuth2 token endpoint | `https://auth.crvs.gov.example/token` |
| Client ID | OAuth2 client identifier | `openspp-client` |
| Client Secret | OAuth2 client secret (stored encrypted) | (secure value) |
| Scope | OAuth2 scopes for API access | `read:registry` |
| Active | Enable/disable the connection | Checked |

### Test the Connection

After saving, click **Test Connection** to verify:

- OAuth2 authentication works
- API endpoint is reachable
- Credentials have appropriate permissions

## Service Methods

For developers extending this module:

| Method | Description |
|--------|-------------|
| `get_access_token()` | Obtain or refresh OAuth2 token |
| `make_request()` | Execute authenticated API request |
| `test_connection()` | Verify data source connectivity |

### OAuth2 Flow

The module implements the OAuth2 client credentials flow:

1. Client sends credentials to auth endpoint
2. Receives access token with expiration
3. Uses token for subsequent API calls
4. Automatically refreshes expired tokens

## Are you stuck?

### Authentication failing

**Symptom:** "Invalid credentials" or "Unauthorized" error when testing connection.

**Cause:** Incorrect OAuth2 credentials or expired client secret.

**Solution:**

1. Verify client ID and secret with the external system administrator
2. Check if credentials have expired and need renewal
3. Confirm the auth URL is correct (including any path like `/token` or `/oauth/token`)

### Connection timeout

**Symptom:** Request times out when testing connection.

**Cause:** Network issues or firewall blocking outbound connections.

**Solution:**

1. Verify the server can reach the external API endpoint:
   ```bash
   curl -I https://api.crvs.gov.example/v1
   ```
2. Check firewall rules for outbound HTTPS (port 443)
3. Verify DNS resolution is working

### Scope errors

**Symptom:** "Insufficient scope" or "access_denied" error on API calls after successful authentication.

**Cause:** OAuth2 token missing required scopes for the requested operation.

**Solution:**

1. Review required scopes in the external system's API documentation
2. Update data source configuration with correct scopes (space-separated)
3. Request scope authorization from external system administrator if needed

### SSL certificate errors

**Symptom:** "SSL certificate verify failed" or similar error.

**Cause:** External system uses self-signed certificate or certificate chain is incomplete.

**Solution:**

1. Verify the external system's SSL certificate is valid
2. For test environments with self-signed certificates, consult with your sys admin about certificate trust configuration

## See Also

- {doc}`spp_dci_server` - DCI server for receiving requests from external systems
- {doc}`spp_registry` - Registry for storing retrieved data
