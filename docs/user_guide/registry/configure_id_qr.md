---
openspp:
  doc_status: draft
  products: [registry]
  applies_to:
    - social_registry
    - sp_mis
---

# Generate a QR credential

**Applies to:** Social Registry, SP-MIS

## What you will do

Create a cryptographic signing key, configure a credential issuer, and generate a signed,
offline-verifiable QR credential (MOSIP Claim 169 format) for a registrant.

## Before you start

- Make sure the **OpenSPP QR Credentials** module (`spp_claim_169`) is installed — it
  brings in the **OpenSPP Key Management** module (`spp_key_management`) as a
  dependency, which is what adds the **Key Management** app used in Step 1
- You need **Administrator** access — creating signing keys and issuer configurations are
  administrative tasks
- Have an existing individual in the registry, or register one first — see
  {doc}`register_individual`
- Steps 1 and 2 below are one-time setup. Once a signing key and issuer configuration
  exist, generating QR credentials for registrants only takes the steps in
  [Step 3](#step-3-generate-a-qr-credential-for-a-registrant)

## Steps

### Step 1. Create a signing key

Every QR credential is cryptographically signed, so a signing key must exist before you
can issue one.

Click **Key Management** in the app menu, then click the **Asymmetric Keys** tab.

![Key Management app with Asymmetric Keys tab](/_images/en-us/registry/configureQR/01-open-key-management-asymmetric-keys.png)

Click **New** and give the key a **Name**.

![New Asymmetric Key form](/_images/en-us/registry/configureQR/02-new-asymmetric-key-form.png)

| Field | What to enter |
|-------|----------------|
| **Name** | A label to identify this key (for example, "National ID Signing Key") |
| **Key Type** | **RSA** or **EC (Elliptic Curve)** |
| **Curve** | Shown only for EC keys — **P-256 (secp256r1)** is the standard choice |
| **Purpose** | What the key will be used for, for example **Credentials** |
| **Storage Mode** | Where the private key material is stored, for example **Local (Encrypted)** |

![Key Type set to EC with the P-256 curve selected](/_images/en-us/registry/configureQR/03-key-type-ec-curve-p256.png)

```{note}
**Ed25519** is recommended for local keys and HashiCorp Vault (fast and compact).
**ECDSA P-256** is required if the key will be stored in AWS KMS, Azure Key Vault, or
GCP KMS.
```

```{warning}
**Storage Mode** controls where the private key material is kept. **Local (Encrypted)**
is fine for development and testing, but for production use a KMS- or Vault-backed
storage mode so the private key never leaves a dedicated key management service. Anyone
who can access a locally stored private key can forge signed credentials.
```

Once the key parameters and **Purpose** are set, click **Generate Key Pair**.

![Confirmation dialog before generating the key pair](/_images/en-us/registry/configureQR/04-generate-key-pair-confirmation.png)

Click **Ok** to confirm. A **Key Generated** notification appears with the new key's ID,
and the **Key Details** tab now shows the **Key ID**, creation timestamp, and the
**Public Key (JWK)**.

![Generated key showing Key ID and Public Key](/_images/en-us/registry/configureQR/05-key-generated-details.png)

### Step 2. Configure a credential issuer

Next, define which organization issues the credential and which signing key it uses.

Go to **Registry → Configuration**, then under the **QR Credentials** section click
**Issuer Configurations**.

![Registry Configuration menu showing Issuer Configurations under QR Credentials](/_images/en-us/registry/configureQR/06-registry-configuration-issuer-configurations-menu.png)

This opens the list of existing issuer configurations.

![Issuer Configurations list](/_images/en-us/registry/configureQR/07-issuer-configurations-list.png)

Click **New**. Until a signing key is selected, a **Signing Key Required** warning is
shown, along with a **Setup Guide** explaining the prerequisites and fields.

![New Issuer Configuration form showing the Signing Key Required warning and Setup Guide](/_images/en-us/registry/configureQR/08-new-issuer-configuration-signing-key-required.png)

| Field | Required | What to enter |
|-------|----------|----------------|
| **Issuer Name** | Yes | A human-readable name, for example "National ID Issuer" |
| **Issuer ID** | Yes | A DID or URI identifying your organization, for example `did:web:example.org` |
| **Signing Key** | Yes | The key created in Step 1 |
| **Default Validity (Days)** | No | How many days a generated credential stays valid (default: 365) |
| **Default Issuer** | No | Check to use this configuration by default in the credential generation dialog |

Select the signing key, fill in the remaining fields, and click **Save**.

![Saved issuer configuration with signing key selected](/_images/en-us/registry/configureQR/09-issuer-configuration-saved.png)

```{note}
The **Setup Guide** also points to **Configure Attribute Mappings**
(**Registry → Configuration → QR Credentials → Attribute Mappings**), where you define
which registrant fields are included as claims in the QR credential. Without a mapping
configured, credentials still generate, but with only the registrant's full name as data.
```

### Step 3. Generate a QR credential for a registrant

With a signing key and issuer configured, you can generate credentials for any
registrant.

Open the registrant's record and click the **Identity** tab. If no credential exists
yet, the **QR Credentials** section shows "No active QR credential found for this
registrant."

![Identity tab showing no active QR credential yet](/_images/en-us/registry/configureQR/10-identity-tab-no-qr-credential.png)

Click **Generate QR Credential**.

![Generate QR Credential dialog](/_images/en-us/registry/configureQR/11-generate-qr-credential-modal.png)

| Field | What to enter |
|-------|----------------|
| **Registrants** | Pre-filled with the registrant you opened; add more to generate credentials in bulk |
| **Issuer** | The issuer configuration from Step 2 |
| **Validity (Days)** | How many days this credential stays valid |
| **Generation Mode** | **New Only (Skip if exists)** skips registrants who already have an active credential |

Click **Generate Credentials**.

![Successfully generated credential confirmation](/_images/en-us/registry/configureQR/12-qr-credential-generated-success.png)

Click **View Generated Credentials** to open the list of credentials just created for
this registrant.

![Generated Credentials list](/_images/en-us/registry/configureQR/13-generated-credentials-list.png)

Click the row to open the full credential record. From here you can **Download QR** or
**Download QR Image**, or **Revoke** or **Regenerate** the credential.

![Credential detail page with Download QR, Revoke, and Regenerate actions](/_images/en-us/registry/configureQR/14-credential-detail-download-revoke-regenerate.png)

## Are you stuck?

**"Signing Key Required" warning won't go away?**
Make sure the Asymmetric Key was actually generated (its form shows **Regenerate Key**
instead of **Generate Key Pair** once done), then select it from the Issuer
Configuration's **Signing Key** field.

**Generate QR Credential doesn't produce a credential?**
Confirm an Issuer Configuration exists with a signing key selected and is **Active** —
check **Registry → Configuration → Issuer Configurations**.

**Credential data only shows the registrant's full name?**
Configure **Registry → Configuration → QR Credentials → Attribute Mappings** to include
additional registrant fields as claims.

**Need to invalidate a credential?**
Open the credential's detail page and click **Revoke**. Its status moves from Active to
Revoked and it can no longer be verified as valid.

## Next steps

- {doc}`register_individual` - Register a new individual before generating their QR credential
- {doc}`search_filter` - Find the registrant you want to generate a credential for
