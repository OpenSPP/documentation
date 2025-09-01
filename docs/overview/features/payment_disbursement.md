# Pluggable Payment and Disbursement

OpenSPP's payment and disbursement system provides a flexible, pluggable architecture for integrating with diverse financial service providers, enabling programs to deliver {term}`benefits` to {term}`beneficiaries` through multiple channels including banks, mobile money, vouchers, and direct cash distribution.

## Moving Beyond Manual Payments

The "last mile" of {term}`social protection` delivery—getting benefits into the hands of beneficiaries—often presents the greatest operational challenges. Programs must navigate complex financial ecosystems with multiple payment service providers, varying levels of financial inclusion among target populations, and diverse regulatory requirements. A rigid, one-size-fits-all payment system cannot address these varied contexts effectively. Programs operating in urban areas might leverage digital payments through banks and mobile money operators, while those in remote rural areas might rely on cash distribution or voucher systems.

OpenSPP's pluggable architecture recognizes that payment ecosystems vary dramatically across countries and even within regions of the same country. The platform doesn't force programs into predetermined payment channels but instead provides connectors to integrate with existing financial infrastructure. This approach allows programs to use the most appropriate payment methods for their context while maintaining standardized processes for payment preparation, reconciliation, and reporting. The system's support for emerging standards like G2P Connect ensures that programs can leverage modern digital payment infrastructure where available, while still maintaining fallback options for areas with limited financial services. This flexibility is essential for achieving universal coverage and ensuring that no beneficiary is excluded due to payment infrastructure limitations.

## Payment Channels

* **Multi-Channel Payment Support**: Process payments through banks, mobile money operators, payment aggregators, or direct cash distribution based on beneficiary preferences and local infrastructure
* **Standards-Based Integration**: Connect with payment systems using G2P Connect and other international standards for government-to-person payments
* **Batch Payment File Generation**: Create formatted payment files compatible with various banking systems and payment processors for bulk disbursements
* **Voucher Management System**: Generate secure, QR-coded vouchers that can be printed and distributed, with built-in fraud prevention and tracking
* **Point of Sale (POS) Integration**: Enable merchants and service points to accept and redeem vouchers through integrated POS interfaces
* **Real-Time Payment Tracking**: Monitor payment status from initiation through settlement with automated reconciliation capabilities
* **Multi-Currency Support**: Handle programs operating in different currencies with appropriate conversion and accounting
* **Payment Retry and Exception Handling**: Automatically manage failed payments with configurable retry logic and manual intervention workflows

## Payment Infrastructure

The payment system is implemented through specialized payment connectors:

* **[g2p_payment_cash](/reference/modules/g2p_payment_cash.md)**: Direct cash payment management with distribution tracking
* **[g2p_payment_files](/reference/modules/g2p_payment_files.md)**: Payment file generation for bank batch processing
* **[g2p_payment_phee](/reference/modules/g2p_payment_phee.md)**: Integration with Mifos Payment Hub EE
* **[g2p_payment_interop_layer](/reference/modules/g2p_payment_interop_layer.md)**: Interoperability layer for multiple payment providers
* **[g2p_payment_simple_mpesa](/reference/modules/g2p_payment_simple_mpesa.md)**: M-Pesa mobile money integration
* **[g2p_payment_g2p_connect](/reference/modules/g2p_payment_g2p_connect.md)**: G2P Connect standard implementation
* **[spp_pos](/reference/modules/spp_pos.md)**: Point of Sale system for voucher redemption
* **[spp_pos_id_redemption](/reference/modules/spp_pos_id_redemption.md)**: ID-based redemption at service points
* **[g2p_entitlement_voucher](/reference/modules/g2p_entitlement_voucher.md)**: Voucher generation and management