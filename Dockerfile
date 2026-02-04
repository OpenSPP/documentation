FROM debian:12-slim

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3.11 python3.11-venv python3.11-dev \
    build-essential pkg-config git curl unzip \
    libldap2-dev libsasl2-dev libssl-dev libffi-dev \
    libxml2-dev libxslt1-dev \
    libjpeg-dev zlib1g-dev \
    libpq-dev \
    graphviz \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /docs

COPY . /docs/

EXPOSE 8050