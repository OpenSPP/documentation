# Configuring Keycloak for OAuth

## configuration

If you are using the [docker-compose setup](https://github.com/openspp/openspp-docker), you already have the
`auth_oidc` from [OCA](https://github.com/OCA/server-auth) installed, otherwise you will need to install it.

### Configure Keycloak

1. Go to the admin console of your keycloak instance
2. Create a new realm (if needed), in our example we use `odoo`.
3. Create a new client, in our example we use `odoo`.
4. Enable `standard flow` and save.
5. Set the `Valid redirect URIs` to be "<url of your server>/auth_oauth/signin".
6. Enable `Client authentication`.
7. Go to the "Credentials" tab and copy the `Client secret` to be used later.

### Configure Odoo

1. Install `Authentication OpenID Connect` from the Apps menu.
2. Go to `Settings > General Settings > Integrations > oAuth Authentication > oAuth Providers` and configure
   it as following:

   - **Provider name**: Keycloak (or any name you like that identify your keycloak provider)
   - **Auth Flow**: OpenID Connect (authorization code flow)
   - **Client ID**: the same Client ID you entered when configuring the client in Keycloak
   - **Client Secret**: found in keycloak on the client Credentials tab
   - **Allowed**: yes
   - **Body**: the link text to appear on the login page, such as Login with Keycloak
   - **Scope**: openid email
   - **Authentication URL**: The "authorization_endpoint" URL found in the OpenID Endpoint Configuration of
     your Keycloak realm
   - **Token URL**: The "token_endpoint" URL found in the OpenID Endpoint Configuration of your Keycloak realm
   - **JWKS URL**: The "jwks_uri" URL found in the OpenID Endpoint Configuration of your Keycloak realm

**For example:**

![](images/openspp_oidc_configuration.png)

### Customizing the login page (Optional)

- **Enable Developer Settings**: "Settings" > "Activate The Developer Mode"

- **Edit The Login Template**: "Settings" > "Technical" > "User Interface > Views" > Search for "Login"

## Using

### Existing users

For users that already exist before the configuration, they need to go through the reset password process to
configure their account to use OpenID Connect.

### New users

For new users, create their user account in odoo with the same email address used in `Keycloak` and they will
be able to login.
