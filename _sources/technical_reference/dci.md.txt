# Implementation of DCI Specification

In the rapidly evolving landscape of digital public infrastructure (DPI), the principle of interoperability stands as an important for building efficient, inclusive, and sustainable systems in a country. This article delves into how OpenSPP implemented APIs outlined in the [DCI Interface Standards v1.0](https://spdci.github.io/standards/release/html/registry_core_api_v1.0.0.html) under Registry to enable interoperability with other systems such as CRVS.

The implementation can be categorized into two sections where OpenSPP operates as the client and OpenSPP operates as the server. Note that currently OpenSPP has only completed the sync implementation.

## 1. Server Implementation

This section focuses on utilizing OpenSPP as the source of truth for beneficiary information where OpenSPP acts as the server. Such integration allows OpenSPP to seamlessly interact with other critical systems by providing data, thereby enhancing data exchange and operational efficiency. The following steps elaborate how the module can be configured.

### 1.1 Deployment and Installation

- Deploy [this branch](https://github.com/OpenSPP/openspp-api/tree/spp_dci_api_server) on a server
- Generate RSA Private and Public key.
- Save the RSA private key to spp_dci_api_server/tools/private_key.pem.
- Save the RSA public key to spp_dci_api_server/tools/public_key.pub
- Login to OpenSPP, Go to Apps, Search “OpenSPP API: DCI Server” and Install.

### 1.2 How to use

- Login to OpenSPP
- Navigate to Settings -> DCI API Client Credentials
- Click Create button and fill-up the Client Name field then click Save.
- “Show” button will appear.
- Click the “Show” button to reveal the Client ID and Client Secret.
- Make sure to copy the Client ID and Client Secret.
- Upon closing the modal, “Show” button will not appear anymore and will not be able to reveal the Client ID and Client Secret.
- Client ID and Client Secret will be used to retrieve Access Token.
- Access Token will be used to authenticate in the search Registry API.
- To retrieve Access Token, Send a POST request to the url <domain>/oauth2/client/token with a body client_id, client_secret, and grant_type=’client_credentials’
- Copy the access_token in the response.
- To retrieve registry data, Send a POST request to the url <domain>/registry/sync/search.
- Header should have a key “Authorization” with a value “Bearer <access_token>”
- Refer the DCI API spec for the request and response structure

## 2. Client Implementation

This section focuses on utilizing another registry as the source for truth to get beneficiary information. The following steps elaborate how the module can be configured to fetch data where OpenSPP acts as the client.

### 2.1 Deployment and Installation

- Deploy these two branches([1](https://github.com/OpenSPP/openspp-api/tree/spp_crvs_import),[2](https://github.com/OpenSPP/openspp-base/tree/spp_data_source)) on a server
- Get client_id and client_secret from CRVS(or from server).
- Login to OpenSPP
- Navigate to the Apps page, Search “OpenSPP Import: DCI API” and Install it.
- Upon installing “OpenSPP Import: DCI API”, a data source is automatically created.
- Navigate to Settings -> Data Source to view the created data source.
- Input the credentials in the client_id, client_secret, and grant_type field inside the Data Source record.
- The only supported grant_type for now is “client_credentials”.
- Be careful on updating the Data Source since it may affect the process of importing.

### 2.2 How to use

- Navigate to Programs -> Import From Registry
- Create Search Criteria, Enter Search Criteria Name, Location, and Birthdate Range
- Click Fetch Button.
- Individual records will be imported from OpenCRVS Lab to OpenSPP.
- Fetch Button is now disabled but it can be enabled by clicking the “Enable Fetching”.
- Once an individual record is already fetched, They are now created and visible to the Registry page.
- Navigate to Registry -> Individual to check the individuals.
- Navigate to Registry -> Group to check the groups.
- Refer the DCI API spec for the request and response structure

_NOTE: This documentation/implementation should be considered as an alpha release of the implementation of the DCI Interface Standards v1.0._
