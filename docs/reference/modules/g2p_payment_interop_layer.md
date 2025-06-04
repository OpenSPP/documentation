---
review-status: needs-review
review-date: 2025-06-04
reviewer: migration-script
migration-notes: "Added during 2025 documentation reorganization"
---

# OpenG2P Program Payment (Payment Interoperability Layer) Module

```{warning}

**Work in Progress**: This document is actively being developed and updated. Content may be incomplete or subject to change.
```

## Overview

The [g2p_payment_interop_layer](g2p_payment_interop_layer) module extends the OpenG2P platform by providing a generic interoperability layer for integrating with various Digital Financial Service Providers (DFSPs) for disbursement of program payments. It offers a configurable framework to connect with DFSPs through APIs, enabling seamless and automated payment processes.

## Features

- **Centralized Payment Management:** Provides a unified interface within OpenG2P to manage payments across different DFSPs.
- **DFSP Agnostic:** Designed to be adaptable to various DFSPs, reducing the need for DFSP-specific integrations.
- **Automated Payment Processing:** Automates the sending of payment instructions to DFSPs, streamlining the disbursement workflow.
- **Configurable Payment Routing:** Allows administrators to configure payment rules and routing logic based on factors like payment amount, recipient location, and DFSP availability.
- **Payment Tracking and Reconciliation:** Enables real-time tracking of payment statuses and facilitates reconciliation of transactions with DFSPs.
- **Enhanced Security:** Implements security measures to ensure secure communication and protect sensitive payment data during transmission to DFSPs.

## Dependencies

- [g2p_registry_base](g2p_registry_base): Provides core registry functionalities and data structures used for managing beneficiary information.
- [g2p_programs](g2p_programs): Handles program management, including payment cycles and beneficiary entitlements.

## Functionality and Integration

This module builds upon the core OpenG2P modules by adding a dedicated layer specifically for payment interoperability. It interacts with the [g2p_programs](g2p_programs) module to retrieve payment instructions generated for program beneficiaries. It then leverages the defined configuration to translate these instructions into API requests compatible with the target DFSP.

The module also handles the reception of payment statuses and updates the corresponding payment records within OpenG2P, ensuring synchronization between the platform and the DFSP.

## Configuration

The [g2p_payment_interop_layer](g2p_payment_interop_layer) module provides a user-friendly interface for configuring connections with DFSPs. This includes specifying API endpoints, authentication credentials, and any required data mapping or transformation rules.

## Usage

Once configured, the module seamlessly integrates into the existing OpenG2P payment workflow. When a payment cycle is triggered, the module automatically handles the communication with the appropriate DFSP, simplifying the disbursement process for program administrators. 
