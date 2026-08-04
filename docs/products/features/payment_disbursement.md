---
myst:
  html_meta:
    "title": "Payment Processing and Disbursement"
    "description": "OpenSPP payment processing system for bank and cash-based benefit disbursement"
    "keywords": "OpenSPP, payment disbursement, banking integration, batch processing, social protection"
---

# Payment processing and disbursement

OpenSPP's payment and disbursement system manages the payment lifecycle for social protection benefits, enabling programs to deliver {term}`benefits` to {term}`beneficiaries` through bank or cash disbursement channels.

## Moving beyond manual payments

The "last mile" of {term}`social protection` delivery — getting benefits into the hands of beneficiaries — often presents the greatest operational challenges. Programs must navigate complex financial ecosystems, varying levels of financial inclusion among target populations, and diverse regulatory requirements. A rigid, one-size-fits-all payment system cannot address these varied contexts effectively. Programs operating in urban areas might rely on bank transfers, while those without access to banking infrastructure may need cash-based distribution.

OpenSPP allows each program to configure its own disbursement channel — bank transfer or cash — and currency, based on what's appropriate for its beneficiary population and local context. Payments are grouped into configurable batches and processed asynchronously, allowing large-scale disbursements to run without blocking other system operations. Payment status is tracked throughout the disbursement lifecycle, and failed batches can be reprocessed through the payment preparation workflow.

## Payment channels

* **Multi-channel payment support**: Process payments through bank or cash disbursement channels, configured per program
* **Payment batching**: Group payments into configurable batches for bulk processing, with asynchronous job-queue handling for large batches
* **Payment status tracking**: Track payment status throughout the disbursement lifecycle
* **Per-program currency configuration**: Configure each program's disbursement currency independently
* **Failed payment reprocessing**: Reprocess failed payment batches through the payment preparation workflow

## Payment infrastructure

The payment system is implemented through the following modules:

* **[spp_programs](/reference/modules/spp_programs.md)**: Payment record lifecycle, batching, and asynchronous processing for bulk disbursements
* **[spp_banking](/reference/modules/spp_banking.md)**: Bank account and IBAN capture for payment processing
