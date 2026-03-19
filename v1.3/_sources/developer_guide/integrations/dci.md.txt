---
myst:
  html_meta:
    "title": "Digital Convergence Initiative Integration"
    "description": "Learn how to implement DCI Interface Standards v1.0 in OpenSPP for interoperability with CRVS and other digital public infrastructure."
    "keywords": "OpenSPP, DCI, Digital Convergence Initiative, interoperability, CRVS, API integration, data exchange"
---

# Digital Convergence Initiative

In the rapidly evolving landscape of digital public infrastructure (DPI), the principle of interoperability stands as an important foundation for building efficient, inclusive, and sustainable systems in a country.
This article delves into how OpenSPP implemented APIs outlined in the [DCI Interface Standards v1.0](https://standards.spdci.org/standards/standards-for-interoperability-interfaces/structure-and-versioning-of-the-standards) under Registry to enable interoperability with other systems such as {term}`CRVS`.

The implementation can be categorized into two sections where OpenSPP operates as the client and OpenSPP operates as the server.
Note that currently OpenSPP has only completed the sync implementation.

## Server implementation

This section focuses on utilizing OpenSPP as the source of truth for {term}`beneficiary` information where OpenSPP acts as the server.
Such integration allows OpenSPP to seamlessly interact with other critical systems by providing data, thereby enhancing data exchange and operational {term}`efficiency`.
The following steps elaborate how the module can be configured.

### Deployment and installation

1. Deploy [this branch](https://github.com/OpenSPP/openspp-api/tree/spp_dci_api_server) on a server.

2. Generate RSA Private and Public key.

3. Save the RSA private key to spp_dci_api_server/tools/private_key.pem

4. Save the RSA public key to spp_dci_api_server/tools/public_key.pub

5. Login to OpenSPP and go to Apps. Search for “OpenSPP API: DCI Server” and install.

### How to use

1. Login to OpenSPP.

2. Navigate to Settings and click on DCI API Client Credentials.

3. Click Create button. Fill in the Client Name field and then click Save.

4. Click the “Show” button to reveal the Client ID and Client Secret.

5. Make sure to copy the Client ID and Client Secret.

6. Upon closing the modal, “Show” button will not appear anymore and will not be able to reveal the Client ID and Client Secret.

7. Client ID and Client Secret will be used to retrieve Access Token.

8. Access Token will be used to authenticate in the search Registry API.

9. To retrieve Access Token, Send a POST request to the url `<domain>/oauth2/client/token` with a body client_id, client_secret, and grant_type=’client_credentials’

10. Copy the access_token in the response.

11. To retrieve registry data, Send a POST request to the url `<domain>/registry/sync/search`.

12. Header should have a key “Authorization” with a value “Bearer <access_token>”

13. Refer to the DCI API spec for the request and response structure.

## Client implementation

This section focuses on utilizing another registry as the source for truth to get beneficiary information that can then be utilized in OpenSPP.

This section focuses on utilizing another registry as the source for truth to get {term}`beneficiary` information.
The following steps elaborate how the module can be configured to fetch data where OpenSPP acts as the client.

### 2.1 Deployment and Installation

1. Deploy these two branches([1](https://github.com/OpenSPP/openspp-api/tree/spp_crvs_import),[2](https://github.com/OpenSPP/openspp-base/tree/spp_data_source)) on a server

2. Get client_id and client_secret from CRVS (or from server).

3. Login to OpenSPP.

4. Navigate to the Apps page. Search for “OpenSPP Import: DCI API” and Install it.

5. Upon installing “OpenSPP Import: DCI API”, a data source is automatically created.

6. Navigate to Settings and select Data Source to view the created data source.

7. Input the credentials in the client_id, client_secret, and grant_type field inside the Data Source record.

NOTE: The only supported grant_type for now is “client_credentials”.

### How to use

1. Navigate to Programs and select Import From Registry.

2. Create Search Criteria, Enter Search Criteria Name, Location, and Birthdate Range.

3. Click Fetch Button.

4. Individual records will be imported from OpenCRVS Lab to OpenSPP.

5. Fetch Button is now {term}`disabled` but can be enabled by clicking the “Enable Fetching”.

6. Once an individual record is fetched, it is created and visible on the Registry page.

7. Navigate to Registry and select Individual to check the individuals. Select Group to check the groups.

8. Refer the DCI API spec for the request and response structure.

_NOTE: This documentation/implementation should be considered as an alpha release of the implementation of the DCI Interface Standards v1.0._
