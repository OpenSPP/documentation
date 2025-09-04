---
myst:
  html_meta:
    "title": "OpenSPP Integrations Overview"
    "description": "Comprehensive guides for integrating OpenSPP with external systems, identity providers, and digital public infrastructure components."
    "keywords": "OpenSPP, integrations, external systems, identity providers, DCI, eSignet, OIDC, interoperability"
---

# Integrations

This section provides guides for connecting OpenSPP with external systems, identity providers, and other digital public infrastructure components. These integrations are key to building a robust and interoperable social protection ecosystem.

In addition to the ones listed below, we also have integration with OpenCRVS and OpenFN.

Here, you will find detailed instructions and best practices for:

- {doc}`dci`: Learn how to implement the DCI specification to enable seamless data exchange between OpenSPP and other registries, such as a Civil Registration and Vital Statistics (CRVS) system.

- {doc}`esignet`: Discover how to integrate eSignet as an identity provider, allowing users to authenticate into OpenSPP using their MOSIP-based digital identity.

- {doc}`oidc`: Follow our guide to configure Keycloak as an :term:`OIDC` provider for OpenSPP, enabling single sign-on (SSO) for a secure and streamlined user authentication experience.

```{toctree}
:maxdepth: 2
:caption: Contents
:hidden:

dci
esignet
oidc
```
