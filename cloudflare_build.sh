#!/usr/bin/env bash
set -euo pipefail

sudo apt-get update && sudo apt-get install -y graphviz libsasl2-dev libldap2-dev libssl-dev

python -m pip install --upgrade pip
pip install -r requirements_for_docs.txt

git submodule update --init --recursive

DEFAULT_BRANCH="stable"
CURRENT_BRANCH="${CF_PAGES_BRANCH:-$DEFAULT_BRANCH}"
SAFE_BRANCH=$(echo "${CURRENT_BRANCH}" | sed 's/[^a-zA-Z0-9._-]/-/g' | cut -c1-50)

if [ "${CURRENT_BRANCH}" = "${DEFAULT_BRANCH}" ]; then
  export DOCS_VERSION=stable
  export DOCS_BASEURL=https://docs.openspp.org/
  export IS_PREVIEW=0
else
  export DOCS_VERSION="${SAFE_BRANCH}"
  if [ -n "${CF_PAGES_URL:-}" ]; then
    export DOCS_BASEURL="${CF_PAGES_URL%/}/"
  else
    export DOCS_BASEURL="https://docs.openspp.org/previews/${SAFE_BRANCH}/"
  fi
  export IS_PREVIEW=1
fi

sphinx-build -b html docs docs/_build/html
cp docs/_static/_redirects docs/_build/html/_redirects || true
