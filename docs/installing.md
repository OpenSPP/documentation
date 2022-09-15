# Installation

## Installing using Docker for development

### Quick start

You need to have Docker and docker-compose installed on your system.
You also need to have Python installed and pip packages `invoke` and `pre-commit`.

```bash
$ git clone git@github.com:openspp-project/openspp-docker.git
$ invoke develop img-pull img-build git-aggregate resetdb start
```

Then open `http://localhost15069/` in your browser.

## Installing for production

### Using OpenSPP Cloud (recommended)

The easiest way to get a OpenSPP server is by using OpenSPP's Cloud.

OpenSPP Cloud provides fast OpenSPP servers with regular feature updates, automatic security patches, daily
backups, uptime management, enterprise security, and guaranteed support on any issues.

By choosing OpenSPP Cloud, you are also directly supporting future development on OpenSPP and helping make it
better for everyone.

### Using Docker

TODO

### Installing on Amazon EC2

Amazon Web Services (AWS) is one of the many other options for installing OpenSPP. It's a good idea to read
through the Docker instructions, as many of the steps remain the same or similar.

To obtain a server you will need to first `create an AWS account <https://aws.amazon.com/>`. When launching
your instance, select the Ubuntu Server 20.04 LTS AMI in step 1. The `t2.micro` instance type has the 1GB of
memory recommended for if you don't expect many registrants and you don't expect many large activities.

When adjusting the security settings open up the ports for SSH, HTTP, and HTTPS. Once you have launched your
instance, go to the Elastic IPs menu option under Network & Security, then allocate a new address and
associate it with your server in order to keep the IP address for your server consistent.

Before installing OpenSPP on your server, you need to install Docker and Docker Compose. Follow the
instructions below.

1. Install Docker Engine on [Ubuntu](https://docs.docker.com/engine/install/ubuntu/).

2. Install [Docker Compose](https://docs.docker.com/compose/install/).

After installing Docker and Docker Compose you can follow our DigitalOcean instructions from running:

`git clone https://github.com/openspp-project/openspp-docker.git`

Continue with the Docker instructions.

Finally, configure an e-mail service such as
[Amazon SES](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-email-smtp.html) because Amazon
restricts emails sent from EC2.
