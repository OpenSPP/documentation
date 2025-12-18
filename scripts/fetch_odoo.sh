#!/bin/bash
# Fetch Odoo sources for documentation build
# Downloads a zip instead of using git submodule to save space

set -e

ODOO_VERSION="${ODOO_VERSION:-19.0}"
ODOO_DIR="submodules/odoo"
ODOO_ZIP_URL="https://github.com/odoo/odoo/archive/refs/heads/${ODOO_VERSION}.zip"

# Skip if already exists
if [ -d "$ODOO_DIR" ] && [ -f "$ODOO_DIR/odoo-bin" ]; then
    echo "Odoo sources already present in $ODOO_DIR"
    exit 0
fi

echo "Fetching Odoo ${ODOO_VERSION} sources..."

# Create directory
mkdir -p submodules

# Download and extract
echo "Downloading from $ODOO_ZIP_URL"
curl -L -o /tmp/odoo.zip "$ODOO_ZIP_URL"

echo "Extracting..."
unzip -q /tmp/odoo.zip -d submodules/
mv "submodules/odoo-${ODOO_VERSION}" "$ODOO_DIR"

# Cleanup
rm -f /tmp/odoo.zip

echo "Odoo sources ready in $ODOO_DIR"
