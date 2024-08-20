# g2p_program_documents Module

```{warning}

**Work in Progress**: This document is actively being developed and updated. Content may be incomplete or subject to change.
```

## Overview

The [g2p_program_documents](g2p_program_documents) module extends the OpenG2P framework to incorporate document management capabilities within social protection programs. This module builds upon the functionalities provided by the [g2p_documents](g2p_documents) and [g2p_programs](g2p_programs) modules.

## Purpose

This module aims to streamline the handling of supporting documents throughout the lifecycle of a social protection program. It enables the association of documents with various program elements, including:

* **Programs:** Defining a designated document storage backend for each program.
* **Program Memberships:** Uploading and managing supporting documents for individual beneficiary program memberships.
* **Entitlements:** Linking relevant documents to specific entitlements within a program.

## Functionality

* **Program-Level Document Storage:**
    * Administrators can configure a specific storage backend for each program to centrally manage supporting documents.
* **Document Attachment to Program Memberships:**
    * Beneficiaries or program staff can upload supporting documents during the program enrollment process or at any point during their membership.
    * Documents associated with a program membership are accessible from the beneficiary's profile.
* **Document Linking to Entitlements:**
    * Relevant documents can be linked to individual entitlements, providing evidence or context for approval processes.
    * When new entitlements are created, the module attempts to automatically copy relevant documents from the beneficiary's program membership or previous entitlements.
* **Document Preview:**
    * The module provides a built-in document preview mechanism for supported file types, allowing users to view documents directly within the OpenG2P interface.

## Integration

* **[g2p_documents](g2p_documents):**  Leverages the core document management functionalities provided by this module for document storage, retrieval, and preview.
* **[g2p_programs](g2p_programs):** Extends the existing program management features by integrating document handling capabilities into program definitions, beneficiary memberships, and entitlements.

## Security

The module inherits security groups from the [g2p_documents](g2p_documents) module, ensuring that only authorized users can access, upload, or manage documents. This includes roles such as program validators, cycle approvers, program managers, and finance validators.
