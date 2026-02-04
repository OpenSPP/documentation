---
openspp:
  doc_status: draft
---

# DCI Server

**Module:** `spp_dci_server`
This module is for **developers** and **sys admins** setting up OpenSPP as a data provider for DCI-compliant external systems.

## Overview

DCI Server provides the infrastructure for receiving and processing incoming DCI API requests from external systems. It enables OpenSPP to act as a data provider, responding to queries from other social protection systems and identity registries.

Use this module when you need to:

- **Receive DCI requests** from authorized external systems
- **Process queries** against OpenSPP registry data
- **Manage subscriptions** for asynchronous notification patterns
- **Track transactions** with a complete audit trail

## Module Dependencies

| Dependency | Purpose |
|------------|---------|
| `base` | Odoo core framework |
| `fastapi` | FastAPI framework for API endpoints |
| `queue_job` | Background job processing |
| `spp_dci` | DCI standards and schemas |
| `spp_dci_client` | Shared DCI infrastructure |
| `spp_api_v2` | API V2 framework |

## Technical Details

| Property | Value |
|----------|-------|
| Technical Name | `spp_dci_server` |
| Category | OpenSPP/Integration |
| Version | 19.0.1.0.0 |
| License | LGPL-3 |
| Application | No |
| Status | Alpha |

## Data Models

| Model | Purpose |
|-------|---------|
| `spp.dci.sender.registry` | Authorized sender configuration |
| `spp.dci.transaction` | Transaction audit records |
| `spp.dci.subscription` | Subscription management |

## API Endpoints

The server exposes DCI-compliant API endpoints:

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/search` | POST | Search for registrants |
| `/verify` | POST | Verify specific data points |
| `/subscribe` | POST | Create subscription for updates |
| `/notify` | POST | Receive notifications |

## Configuration

### 1. Register Authorized Senders

Navigate to **DCI > Server > Sender Registry** and create a sender record:

| Field | Example Value | Description |
|-------|---------------|-------------|
| Sender ID | `ministry-of-health` | Unique identifier for external system |
| Name | Ministry of Health | Display name |
| Public Key | (PEM formatted) | For signature verification |
| Allowed Operations | Search, Verify | Which API operations are permitted |
| Active | Yes | Enable/disable sender |

### 2. Configure Server Keys

Navigate to **DCI > Server > Server Keys**:

1. Generate or import a server signing key
2. Configure the key for signing responses

### 3. Verify FastAPI Endpoint

The module registers a FastAPI endpoint automatically. Verify in:

**Settings > Technical > FastAPI Endpoints**

## Sender Registry

Manage authorized external systems:

| Field | Description |
|-------|-------------|
| Sender ID | Unique identifier for external system |
| Name | Display name |
| Public Key | For signature verification |
| Allowed Operations | Which API operations are permitted |
| Active | Enable/disable sender |

## Transaction Management

Track all API interactions:

| Field | Description |
|-------|-------------|
| Transaction ID | Unique request identifier |
| Sender | Which system made the request |
| Operation | Type of request (search, verify) |
| Request Data | Incoming request payload |
| Response Data | Outgoing response payload |
| Status | Success, error, pending |
| Timestamp | When request was processed |

## Subscription Management

Support asynchronous patterns:

| Field | Description |
|-------|-------------|
| Subscriber | External system identifier |
| Event Type | What events trigger notifications |
| Callback URL | Where to send notifications |
| Filter Criteria | Conditions for notification |
| Active | Enable/disable subscription |

## Security

### Authentication

Incoming requests are authenticated via:

- OAuth2 bearer tokens
- Signature verification using sender's public key
- Sender registry validation

### Authorization

Access control based on:

- Sender's allowed operations
- Data sharing agreements
- Field-level access rules

## Background Processing

Uses `queue_job` for:

- Processing large search requests
- Sending subscription notifications
- Retry handling for failed operations

## API Request Examples

### Search Request

External systems can search for registrants:

```json
{
  "transaction_id": "uuid",
  "sender_id": "ministry-of-health",
  "search_criteria": {
    "national_id": "123456789"
  }
}
```

### Verify Request

Verify specific data without full retrieval:

```json
{
  "transaction_id": "uuid",
  "sender_id": "ministry-of-health",
  "verify": {
    "national_id": "123456789",
    "is_alive": true
  }
}
```

### Subscribe Request

Create subscription for updates:

```json
{
  "transaction_id": "uuid",
  "sender_id": "ministry-of-health",
  "subscription": {
    "event_type": "death",
    "callback_url": "https://moh.gov.example/dci/notify"
  }
}
```
