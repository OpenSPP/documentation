# Prerequisites and System Requirements for Native Installation (Non-Docker)

This section outlines the hardware, software, and library requirements needed to run OpenSPP natively without Docker.

---

## System Requirements

| Requirement        | Recommended Version           |
|--------------------|-------------------------------|
| Operating System   | Ubuntu 20.04 / 22.04 LTS      |
| Python             | 3.10                          |
| PostgreSQL         | 14+                           |
| Node.js            | 16.x                          |
| npm                | Latest                        |
| wkhtmltopdf        | 0.12.6 (with patched Qt)      |
| pip                | Latest                        |
| git                | Latest                        |

---

## Required System Packages

Ensure the following system libraries and tools are installed:

```bash
sudo apt update && sudo apt upgrade
sudo apt install git python3-pip build-essential wget python3-dev python3-venv \
    libxslt-dev libzip-dev libldap2-dev libsasl2-dev python3-setuptools \
    node-less libjpeg-dev libpq-dev libxml2-dev libssl-dev libffi-dev \
    zlib1g-dev libjpeg8-dev liblcms2-dev libblas-dev libatlas-base-dev \
    xz-utils libldap2-dev libsasl2-dev libtiff5-dev libopenjp2-7-dev
