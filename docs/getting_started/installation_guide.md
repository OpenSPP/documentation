# Installation Guide

## Installing using Docker for development

### Quick start

You need to have Docker and docker-compose installed on your system. You also need to have Python installed
and pip packages `invoke` and `pre-commit`.

```bash
$ git clone git@github.com:openspp/openspp-docker.git
$ invoke develop img-pull img-build git-aggregate resetdb start
```

Then open `http://localhost:15069/` in your browser.

## Installing for production

### Using OpenSPP Cloud (Coming soon)

The easiest way to get a OpenSPP server is by using OpenSPP's Cloud.

OpenSPP Cloud provides fast OpenSPP servers with regular feature updates, automatic security patches, daily
backups, uptime management, enterprise security, and guaranteed support on any issues.

By choosing OpenSPP Cloud, you are also directly supporting future development on OpenSPP and helping make it
better for everyone.

[Contact us](https://openspp.org/contact/) if you want to get early access.
