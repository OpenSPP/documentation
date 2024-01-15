# Installation Guide

## Installing using Docker for development

### Quick start

#### Step 1: Install Python.

On Debian-based systems (Ubuntu, Debian, etc.),

```bash
$ sudo apt-get update -y
$ sudo apt-get install -y python3 python3-pip
```
On RHEL-based systems (Fedora, RedHat, CentOS, etc.),

```bash
$ sudo dnf update -y
$ sudo dnf install -y python3 python3-pip
```

Instructions for other systems, including source code installations, can be found here: [More Installation Instructions](https://wiki.python.org/moin/BeginnersGuide/Download).

#### Step 2: Install Python packages.

```bash
$ sudo python3 -m pip install invoke pre-commit
```

If your organization requires the use of a proxy instructions for how to use proxies in the installation of the packages can be found here: [Proxied Installation Instructions](https://pip.pypa.io/en/stable/user_guide/#using-a-proxy-server)

#### Step 3: Install Docker.

On Debian-based systems (Ubuntu, Debian, etc.),

```bash
$ sudo apt-get update -y
$ sudo apt-get install -y apt-transport-https ca-certificates curl gnupg lsb-release
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
$ echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
$ sudo apt-get update  -y
$ sudo apt-get install -y docker-ce docker-ce-cli containerd.io
```
On RHEL-based systems (Fedora, RedHat, excluding CentOS, etc.),

```bash
$ sudo dnf -y update
$ sudo dnf -y install dnf-plugins-core
$ sudo dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo
$ sudo dnf -y update
$ sudo dnf -y install docker-ce docker-ce-cli containerd.io
$ sudo systemctl enable docker.service
$ sudo systemctl enable containerd.service
$ sudo systemctl start docker.service
$ sudo systemctl start containerd.service
```

On CentOS

```bash
$ sudo yum -y install yum-utils
$ sudo yum-config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo
$ sudo yum install docker-ce docker-ce-cli containerd.io
```

#### Step 4: Install Docker-Compose

Docker-Compose requires installing and downloading software from the docker GitHub repository. As such, you will need to find the latest version of the software from their website and follow the installation instructions that follow.

The Docker Compose Documentation Website: [Docker Compose Linux Installation Instructions](https://docs.docker.com/compose/install/standalone/#on-linux)

#### Step 5: Install git

On Debian-based systems (Ubuntu, Debian, etc.),

```bash
$ sudo apt-get update -y
$ sudo apt-get install -y git
```
On RHEL-based systems (Fedora, RedHat, CentOS, etc.),

```bash
$ sudo dnf update -y
$ sudo dnf install -y git
```

#### Step 6: Install OpenSPP

```bash
$ git clone https://github.com/OpenSPP/openspp-docker.git
$ cd ./openspp-docker/
$ sudo invoke develop img-pull img-build git-aggregate resetdb start
```

#### Step 7: Use OpenSPP!

Then open `http://localhost:15069/` in your browser.

For more details, see [OpenSPP Docker](https://github.com/OpenSPP/openspp-docker) Readme file.

## Installing for production

### Using OpenSPP Cloud (Coming soon)

The easiest way to get a OpenSPP server is by using OpenSPP's Cloud.

OpenSPP Cloud provides fast OpenSPP servers with regular feature updates, automatic security patches, daily
backups, uptime management, enterprise security, and guaranteed support on any issues.

By choosing OpenSPP Cloud, you are also directly supporting future development on OpenSPP and helping make it
better for everyone.

[Contact us](https://openspp.org/contact/) if you want to get early access.
