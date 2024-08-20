# g2p_openid_vci_programs Module 

```{warning}

**Work in Progress**: This document is actively being developed and updated. Content may be incomplete or subject to change.
```

## Overview

The `g2p_openid_vci_programs` module extends the OpenG2P platform's OpenID Connect Verifiable Credentials Issuer functionality to generate and issue verifiable credentials specifically designed for program beneficiaries. This module builds upon the core functionalities provided by the [g2p_openid_vci](g2p_openid_vci) and [g2p_programs](g2p_programs) modules.

## Purpose and Functionality

This module focuses on providing a streamlined way to issue verifiable credentials that attest to a beneficiary's enrollment and status within a specific social protection program.  This allows beneficiaries to possess digitally verifiable proof of their program participation, which can be beneficial for various purposes like accessing program benefits or proving eligibility.

Here's a breakdown of the key features:

* **Program-Specific Verifiable Credentials:**  The module defines a new type of verifiable credential, "OpenG2PBeneficiaryVerifiableCredential", specifically structured to include relevant program-related information.
* **Issuance based on Program Enrollment:** It leverages the existing program enrollment data from the [g2p_programs](g2p_programs) module. Only enrolled beneficiaries can receive these verifiable credentials.
* **Integration with OpenID Connect Issuer:** This module seamlessly integrates with the OpenID Connect issuer framework established in the [g2p_openid_vci](g2p_openid_vci) module. This ensures that the issuance process adheres to OpenID Connect standards for security and interoperability.
* **Data Rich Credentials:** The issued verifiable credentials can include comprehensive information about the beneficiary, their program membership details, and other relevant data, making them valuable for various verification purposes.

## Integration and Dependencies

* **[g2p_openid_vci](g2p_openid_vci):** This module depends on the core OpenID Connect Verifiable Credentials Issuer functionality to manage the technical aspects of credential issuance and signing.
* **[g2p_programs](g2p_programs):**  This module relies on the program enrollment data and beneficiary information managed by the [g2p_programs](g2p_programs) module.

## Benefits

* **Enhanced Trust and Transparency:**  Verifiable credentials provide a tamper-proof and verifiable way to prove program participation, fostering trust between beneficiaries and service providers.
* **Improved Efficiency:** Digital credentials streamline verification processes, potentially reducing administrative burden and improving the efficiency of benefit delivery.
* **Empowerment of Beneficiaries:**  Providing beneficiaries with verifiable credentials gives them control over their data and empowers them to prove their eligibility securely and conveniently. 
