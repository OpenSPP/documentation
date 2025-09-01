
**Project Goal:**
[cite_start]Your task is to write a series of documentation pages for the `features/` section of the new OpenSPP documentation structure[cite: 10, 14]. These pages will provide a high-level overview of the platform's core capabilities. [cite_start]The primary audience includes decision-makers evaluating OpenSPP, as well as new administrators and developers seeking to understand the platform's architecture[cite: 2, 129].

**General Tone and Style:**
* **Audience-Aware:** Write clearly and concisely. The content is high-level but must be technically accurate. Avoid marketing language and focus on functionality.
* **Informative & Direct:** The goal is to inform, not to sell. Explain what the feature does and why it's a critical part of a modern social protection platform. Use an active voice.
* **Structure:** Please follow the consistent structure below for each feature page. This ensures a uniform user experience across the documentation.

---

### **Page Structure Template**

Each feature should have its own `.md` file.

**1. Page Title:** (e.g., `<h1>Unified and Hierarchical Beneficiary Registry</h1>`)

**2. Summary:** (1-2 sentences)
   * A crisp definition of the feature and its primary role in the platform.

**3. Why It Matters:** (1-2 paragraphs)
   * Explain the feature's importance in a real-world social protection or registry context. Answer questions like: What problem does it solve? How does it improve data quality, efficiency, or accountability?

**4. Key Capabilities:** (Bulleted list)
   * Detail the specific, concrete functionalities of the feature. Each bullet point should describe a distinct action or capability.

**5. Under the Hood (Related Modules):**
   * List the primary `spp_` and `g2p_` modules that implement this feature. This section grounds the feature in the actual codebase for technical readers.

---

### **Feature Pages to Create**

Below are the 8 feature pages to write. Please create one file for each.

#### **1. Unified and Hierarchical Beneficiary Registry**
* **Core Concept:** Focus on OpenSPP's role as the central, single source of truth for all program participants, supporting both simple individual records and complex, nested group structures.
* **Key Capabilities to cover:**
    * Capturing detailed data for individuals and groups (demographics, IDs, contacts, bank info).
    * Defining and managing relationships between registrants (e.g., Head of Household, Dependent).
    * Supporting nested group structures where groups can be members of other groups.
* **Related Modules:**
    * `g2p_registry_base`, `spp_registry_base`
    * `g2p_registry_individual`, `g2p_registry_group`
    * `g2p_registry_membership`, `spp_registry_group_hierarchy`
    * `g2p_bank`

#### **2. End-to-End Program and Entitlement Management**
* **Core Concept:** Describe the complete lifecycle management for social protection programs, from design and enrollment to calculating and processing different types of benefits.
* **Key Capabilities to cover:**
    * Configuration of diverse programs that target individuals or groups.
    * Management of program cycles for phased or periodic benefit distribution.
    * Support for ongoing "cycleless" programs for continuous benefit delivery.
    * Calculation of cash, in-kind, or voucher-based entitlements based on configurable rules.
* **Related Modules:**
    * `g2p_programs`, `spp_programs`
    * `spp_entitlement_cash`, `spp_entitlement_in_kind`, `spp_entitlement_basket`
    * `g2p_entitlement_voucher`
    * `g2p_program_cycleless`

#### **3. Configurable Eligibility and Targeting**
* **Core Concept:** Explain the powerful and flexible rules engine for determining beneficiary eligibility, which allows programs to precisely target their intended population.
* **Key Capabilities to cover:**
    * Enrollment of beneficiaries through manual selection or automated rules.
    * Targeting based on registrant tags (e.g., "vulnerable household") or specific geographic areas.
    * Defining complex eligibility rules using direct SQL queries for maximum flexibility.
    * Calculating a Proxy Means Test (PMT) score based on custom-weighted indicators to assess socio-economic status.
* **Related Modules:**
    * `spp_manual_eligibility`
    * `spp_eligibility_tags`, `spp_eligibility_sql`
    * `g2p_proxy_means_test`, `spp_pmt`
    * `spp_exclusion_filter`

#### **4. Pluggable Payment and Disbursement**
* **Core Concept:** Detail OpenSPP's flexible architecture for integrating with various financial service providers to deliver benefits to beneficiaries.
* **Key Capabilities to cover:**
    * Support for multiple disbursement methods including direct cash, bank transfers, and digital payments.
    * Integration with payment hubs using standards like G2P Connect.
    * Generation of payment files and secure, printable vouchers with QR codes.
    * Benefit redemption through an integrated Point of Sale (POS) interface.
* **Related Modules:**
    * `g2p_payment_cash`, `g2p_payment_files`
    * `g2p_payment_phee`, `g2p_payment_interop_layer`, `g2p_payment_simple_mpesa`, `g2p_payment_g2p_connect`
    * `spp_pos`, `spp_pos_id_redemption`

#### **5. Data Integration and Interoperability (APIs)**
* **Core Concept:** Present OpenSPP as an interoperable system designed to connect with a larger digital public infrastructure through modern APIs and connectors.
* **Key Capabilities to cover:**
    * A RESTful API for managing registrants, groups, and program enrollments.
    * Secure API authentication using OAuth 2.0.
    * Data import connectors for external sources like ODK Central or other MIS.
    * Support for standardized data exchange (e.g., DCI-compliant).
* **Related Modules:**
    * `spp_api`, `spp_base_api`, `g2p_registry_rest_api`
    * `spp_oauth`
    * `spp_registry_data_source`, `g2p_odk_importer`, `g2p_social_registry_importer`
    * `spp_dci_api_server`

#### **6. Auditable Change Management**
* **Core Concept:** Describe the platform's built-in mechanisms for ensuring data integrity, transparency, and accountability through structured change requests and comprehensive audit trails.
* **Key Capabilities to cover:**
    * A formal change request workflow for submitting, reviewing, and approving data modifications.
    * An immutable audit log that tracks all data changes, recording the before/after values, user, and timestamp.
    * Configurable rules to define precisely which data models and fields require auditing.
* **Related Modules:**
    * `spp_change_request`, `spp_change_request_base`
    * `spp_audit_log`, `spp_audit_config`, `spp_audit_post`
    * `g2p_change_log`

#### **7. Geospatial (GIS) and Land Management**
* **Core Concept:** Explain the integration of GIS to manage, visualize, and analyze location-based data. This is critical for agricultural programs (Farmer Registries) and geographically-targeted social programs.
* **Key Capabilities to cover:**
    * Defining and visualizing hierarchical administrative areas (country, province, district, etc.) on interactive maps.
    * Capturing geospatial boundaries (polygons) and coordinates (points) for entities like land parcels, farms, and service points.
    * Linking digital land records to specific farms and farmers.
* **Related Modules:**
    * `spp_base_gis`, `spp_area`, `spp_area_gis`
    * `spp_land_record`
    * `spp_irrigation`

#### **8. Grievance Redress Mechanism (GRM)**
* **Core Concept:** Describe the integrated system for managing beneficiary feedback and complaints, ensuring a transparent and accountable process for issue resolution.
* **Key Capabilities to cover:**
    * Centralized logging and tracking of all grievances from intake to resolution.
    * Support for multi-channel intake, including a self-service portal for registrants.
    * Customizable stages and workflows to guide the resolution process.
* **Related Modules:**
    * `spp_grm`