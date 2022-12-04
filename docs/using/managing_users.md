# Managing Users

There are two aspects to user management:

- Authentication: Controls who can access the system
- Authorization: Controls what a user can do in the system

## Authentication

OpenSPP can use the Odoo-native authentication mechanism, though the recommendation is to use an external
authentication platform such as Keycloak. This allows for a single sign-on experience for users and ensures
that the authentication mechanism can evolve independently of the systems using it, thus ensuring that the
authentication mechanism can be secured and act as a shield in front of the systems.

## Authorization

Authorization is the process of determining what a user can do in the system, and this is done in each
respective system. In the case of OpenSPP, the concepts from Odoo are used.
