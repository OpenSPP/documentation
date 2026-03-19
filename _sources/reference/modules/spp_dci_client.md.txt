---
openspp:
  doc_status: draft
---

# DCI Client

**Module:** `spp_dci_client`

## Overview

This module is for **developers** and **sys admins** who need to connect OpenSPP to external DCI-compliant registries.

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
