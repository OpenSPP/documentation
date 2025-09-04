---
myst:
  html_meta:
    "title": "DCI API Usage Guide"
    "description": "Learn how to use OpenSPP's DCI-compliant RESTful API for secure registry data synchronization and search with OAuth 2.0 authentication."
    "keywords": "OpenSPP, DCI API, REST API, OAuth 2.0, registry search, data synchronization, digital public infrastructure"
---

# DCI API

OpenSPP provides a RESTful API that adheres to the Digital Convergence Initiative (DCI) specification.
This API enables authorized external systems to securely search and synchronize with OpenSPP's registry data, promoting interoperability with other digital public infrastructure components like a Civil Registration and Vital Statistics (:term:`CRVS`) system.

## Prerequisites

- OpenSPP server running with the {doc}`spp_dci_api_server </reference/modules/spp_dci_api_server>` module installed.
- Client credentials (Client ID and Client Secret) obtained from the OpenSPP instance.
- Python 3.x and the `requests` library installed (`pip install requests`).

## Process

### Authentication: Obtaining an access token

The DCI API is secured using OAuth 2.0 with the Client Credentials grant type.
Before making any data requests, your application must obtain a bearer token.

- **Endpoint**: `/oauth2/client/token`
- **Method**: `POST`
- **Body**: `x-www-form-urlencoded` with `grant_type`, `client_id`, `client_secret`, `db_name`.

**Example: Get access token**

```python
import requests

url = "http://localhost:8069"
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"

token_payload = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
    'db_name': 'your_db'
}

token_url = f"{url}/oauth2/client/token"
response = requests.post(token_url, json=token_payload)

if response.status_code != 200:
    raise Exception(f"Failed to get token: {response.text}")

token_data = response.json()
access_token = token_data.get("access_token")
print("Access Token obtained successfully.")
```

### Searching the registry

Once authenticated, you can use the access token to perform a synchronous search on the registry.

- **Endpoint**: `/registry/sync/search`
- **Method**: `POST`
- **Headers**:
    - `Authorization`: `Bearer <your_access_token>`
    - `Content-Type`: `application/json`
- **Body**: A JSON object conforming to the DCI `sync/search` request specification.

**Example: Search for an individual**

```python
search_url = f"{url}/registry/sync/search"

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
}

# Example search payload based on DCI specification
# This searches for an individual with a specific birthdate.
search_payload = {
    "header": {
        "message_id": "123456789020211216223812",
        "message_ts": "2022-12-04T18:01:07+00:00",
        "action": "search",
        "sender_id": "https://integrating-server.com",
        "total_count": 10
    },
    
    "message": {
        "transaction_id": "123456789020211216223812",
        "search_request": [
            {
                "reference_id": "123456789020211216223812",
                "timestamp": "2022-12-04T17:20:07-04:00",
                "search_criteria": {
                    "reg_type": "SPP:RegistryType:Individual",
                    "query_type": "predicate",
                    "query": [
                        {
                            "expression1": {
                                "attribute_name": "birthdate",
                                "operator": "ge",
                                "attribute_value": "2000-11-02"
                            }
                        },
                        {
                            "expression1": {
                                "attribute_name": "birthdate",
                                "operator": "eq",
                                "attribute_value": "2020-11-02"
                            }
                        }
                    ]
                }
            }
        ]
    }
}

response = requests.post(search_url, headers=headers, json=search_payload)

if response.status_code == 200:
    search_results = response.json()
    print("Search successful:")
    print(search_results)
else:
    print(f"Search failed with status {response.status_code}:")
    print(response.text)
```


### Setup and configuration

To use the DCI API, you must first configure a client in OpenSPP.

1.  **Install the Module**: Log in to OpenSPP, navigate to **Apps**, search for `OpenSPP API: DCI Server`, and install it.
2.  **Navigate to Client Credentials**: Go to **Settings > DCI API Client Credentials**.
3.  **Create a New Client**: Click **Create** and enter a descriptive **Client Name**. Save the record.
4.  **Reveal Credentials**: A **Show** button will appear. Click it to reveal the `Client ID` and `Client Secret`.
5.  **Important**: Copy these credentials immediately. For security, the **Show** button will disappear after you close the dialog, and you will not be able to retrieve the secret again.

## Best practices

-  **Secure Credential Storage**: Never hard-code your `Client ID` or `Client Secret` in your application. Use environment variables or a secure secret management system.
-  **Token Management**: Access tokens are short-lived. Your application should handle token expiration and automatically request a new one when needed.
-  **Error Handling**: Implement robust error handling to manage different HTTP status codes and error responses from the API.
-  **Secure Connections**: Always use HTTPS for all API traffic to protect data in transit.
-  **Logging**: Log request `transaction_id`s and correlation IDs to help with troubleshooting and auditing.

## References

- [DCI Interface Standards v1.0](https://standards.spdci.org/standards/standards-for-interoperability-interfaces/structure-and-versioning-of-the-standards)