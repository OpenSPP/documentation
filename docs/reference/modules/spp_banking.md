---
openspp:
  doc_status: draft
---

# Banking / Bank Details

**Module:** `spp_banking`

## Overview

The OpenSPP Banking module extends Odoo's standard bank account management to support IBAN generation for registrants. It enables social protection programs to capture and validate beneficiary bank details for payment disbursement.

## Purpose

This module is designed to:

- **Capture bank details:** Store bank account information for individuals and groups
- **Generate IBANs:** Automatically compute International Bank Account Numbers
- **Validate accounts:** Ensure bank details are properly formatted
- **Support payments:** Enable payment disbursement to beneficiary accounts

## Module Dependencies

| Dependency       | Description                                |
| ---------------- | ------------------------------------------ |
| **spp_security** | OpenSPP security framework                 |
| **base**         | Core Odoo framework                        |
| **mail**         | Messaging support                          |
| **contacts**     | Contact management                         |
| **spp_registry** | OpenSPP registry for registrant management |

### External Python Dependencies

| Package      | Description                                |
| ------------ | ------------------------------------------ |
| **schwifty** | IBAN/BIC validation and generation library |

## Key Features

### IBAN Generation

The module automatically generates IBANs based on:

| Input           | Description                    |
| --------------- | ------------------------------ |
| Country Code    | From the linked bank's country |
| Bank Code (BIC) | Bank Identifier Code           |
| Account Number  | Local account number           |

The computation uses the `schwifty` library to generate valid IBANs following international standards.

### Bank Account Fields

The module extends `res.partner.bank` with:

| Field          | Description                                |
| -------------- | ------------------------------------------ |
| Account Number | Standard account number                    |
| Bank           | Linked bank record                         |
| IBAN           | Computed International Bank Account Number |

### Automatic Computation

The IBAN is automatically recomputed when:

- Account number changes
- Bank reference changes
- Bank's country or BIC is updated

## Integration

### With spp_registry

Bank accounts can be associated with:

- Individual registrants
- Group/household registrants
- Any partner record in the system

### With Payment Systems

The module provides the foundation for:

- Cash transfer programs
- Direct deposit disbursements
- Payment reconciliation

## Configuration

### Adding Bank Details to a Registrant

Navigate to the registrant's form and add bank account details:

| Field          | Required | Description             |
| -------------- | -------- | ----------------------- |
| Bank           | Yes      | Select or create bank   |
| Account Number | Yes      | Local account number    |
| Account Holder | Auto     | Links to the registrant |

The IBAN is computed automatically if:

1. The bank has a country assigned
2. The bank has a BIC code
3. The account number is provided

### Bank Configuration

Each bank record needs:

| Field     | Description          |
| --------- | -------------------- |
| Name      | Bank name            |
| BIC/SWIFT | Bank Identifier Code |
| Country   | Bank's country       |

## Views

The module adds bank details views for:

- Individual registrants
- Group registrants

These views integrate with the standard registrant forms.

## Technical Details

### IBAN Computation

```
IBAN = Country Code + Check Digits + Bank Code + Account Number
```

The `schwifty` library handles:

- Country-specific formatting rules
- Check digit calculation
- Validation of the generated IBAN

### Error Handling

If IBAN generation fails (invalid data), the field remains empty and a warning is logged. This prevents blocking record saves due to incomplete bank data.

### Migration Support

The module includes pre-migration scripts (`19.0.1.0.0`) to handle upgrades from previous versions.
