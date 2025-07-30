#!/bin/bash
# OpenSPP Development Environment Setup Script
# Supports: Ubuntu 20.04+, Debian 10+, macOS 10.15+
#
# This script automates the setup of a complete OpenSPP development environment
# including all dependencies, database configuration, and development tools.

set -e    # Exit on error if any command fails

# Color codes for output to make messages more readable
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Configuration variables - these can be overridden by command-line arguments
PYTHON_VERSION="3.10"
POSTGRES_VERSION="14"
NODE_VERSION="18"
OPENSPP_BRANCH="main"
ODOO_VERSION="15.0" # Default Odoo version to clone and use

# Function to print colored informational messages
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

# Function to print colored error messages
print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Function to print colored warning messages
print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

# Function to detect the operating system and distribution
detect_os() {
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # Check for Debian-based systems (Ubuntu, Debian)
        if [ -f /etc/debian_version ]; then
            OS="debian"
            DISTRO=$(lsb_release -si 2>/dev/null || echo "Unknown Debian/Ubuntu")
        # Check for RedHat-based systems (CentOS, Fedora, RHEL) - currently not supported by install functions
        elif [ -f /etc/redhat-release ]; then
            OS="redhat" # Mark as redhat, but actual installation will be skipped later
            DISTRO=$(cat /etc/redhat-release)
        else
            OS="unknown"
        fi
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        # Detect macOS
        OS="macos"
        DISTRO="macOS $(sw_vers -productVersion)"
    else
        OS="unknown"
    fi

    print_status "Detected OS: $OS ($DISTRO)"
}

# Function to check if a command exists in the system's PATH
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to install system-level dependencies for Debian/Ubuntu
install_debian_dependencies() {
    print_status "Updating package lists..."
    # Update apt package index
    sudo apt-get update

    print_status "Installing system dependencies for Debian/Ubuntu..."
    # Install common build tools, version control, and Python development headers
    # Also includes libraries for image processing (Pillow), XML (lxml), LDAP, and PostgreSQL client
    sudo apt-get install -y \
        build-essential \
        wget \
        git \
        python3-pip \
        python3-dev \
        python3-venv \
        python3-wheel \
        libxml2-dev \
        libxslt1-dev \
        libldap2-dev \
        libsasl2-dev \
        libtiff5-dev \
        libjpeg8-dev \
        libopenjp2-7-dev \
        zlib1g-dev \
        libfreetype6-dev \
        liblcms2-dev \
        libwebp-dev \
        libharfbuzz-dev \
        libfribidi-dev \
        libxcb1-dev \
        libpq-dev \
        libssl-dev \
        libffi-dev \
        nodejs \
        npm \
        postgresql-$POSTGRES_VERSION \
        postgresql-client-$POSTGRES_VERSION \
        postgresql-server-dev-$POSTGRES_VERSION
}

# Function to install system-level dependencies for macOS using Homebrew
install_macos_dependencies() {
    # Check if Homebrew (macOS package manager) is installed
    if ! command_exists brew; then
        print_status "Installing Homebrew..."
        # Install Homebrew if it's not found
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        # Add Homebrew to PATH for current session
        eval "$(/opt/homebrew/bin/brew shellenv)" || eval "$(/usr/local/bin/brew shellenv)"
    fi

    print_status "Installing system dependencies for macOS..."
    # Install Python, PostgreSQL, Node.js, Git, and various libraries via Homebrew
    brew install \
        python@$PYTHON_VERSION \
        postgresql@$POSTGRES_VERSION \
        node@$NODE_VERSION \
        git \
        wget \
        libxml2 \
        libxslt \
        libjpeg \
        libpng \
        freetype \
        openssl

    # Start PostgreSQL service via Homebrew services
    print_status "Starting PostgreSQL service..."
    brew services start postgresql@$POSTGRES_VERSION || print_warning "PostgreSQL service might already be running or failed to start."
}

# Function to set up the Python virtual environment for OpenSPP
setup_python_env() {
    print_status "Setting up Python virtual environment..."

    # Create the base directory for OpenSPP development if it doesn't exist
    mkdir -p "$HOME/openspp-dev"
    cd "$HOME/openspp-dev"

    # Create the virtual environment using the specified Python version
    python"$PYTHON_VERSION" -m venv venv
    
    # Activate the virtual environment for the current script session
    source venv/bin/activate

    # Upgrade pip, wheel, and setuptools within the virtual environment
    pip install --upgrade pip wheel setuptools

    print_status "Python virtual environment created and activated at $HOME/openspp-dev/venv"
}

# Function to clone OpenSPP and Odoo repositories
clone_repositories() {
    print_status "Cloning Odoo and OpenSPP repositories..."

    cd "$HOME/openspp-dev"

    # Clone Odoo repository
    if [ ! -d "odoo" ]; then
        print_status "Cloning Odoo ($ODOO_VERSION branch)..."
        git clone --depth 1 --branch "$ODOO_VERSION" https://github.com/odoo/odoo.git
    else
        print_warning "odoo directory already exists, skipping clone. Please update manually if needed."
    fi

    # Clone OpenSPP modules repository
    if [ ! -d "openspp-modules" ]; then
        print_status "Cloning OpenSPP modules ($OPENSPP_BRANCH branch)..."
        git clone --depth 1 --branch "$OPENSPP_BRANCH" https://github.com/OpenSPP/openspp-modules.git
    else
        print_warning "openspp-modules directory already exists, skipping clone. Please update manually if needed."
    fi

    # Clone OpenSPP documentation repository
    if [ ! -d "openspp-docs" ]; then
        print_status "Cloning OpenSPP documentation..."
        git clone --depth 1 https://github.com/OpenSPP/openspp-docs.git
    else
        print_warning "openspp-docs directory already exists, skipping clone. Please update manually if needed."
    fi
}

# Function to install Python dependencies from requirements files
install_python_dependencies() {
    print_status "Installing Python dependencies..."

    # Ensure virtual environment is active
    source "$HOME/openspp-dev/venv/bin/activate"

    # Install Odoo's Python dependencies
    print_status "Installing Odoo requirements..."
    pip install -r "$HOME/openspp-dev/odoo/requirements.txt"

    # Install additional OpenSPP specific dependencies if a requirements.txt exists
    if [ -f "$HOME/openspp-dev/openspp-modules/requirements.txt" ]; then
        print_status "Installing OpenSPP modules requirements..."
        pip install -r "$HOME/openspp-dev/openspp-modules/requirements.txt"
    else
        print_warning "No requirements.txt found in openspp-modules, skipping specific OpenSPP Python dependencies."
    fi

    # Install common Python development tools
    print_status "Installing Python development tools (pre-commit, black, flake8, etc.)..."
    pip install \
        pre-commit \
        black \
        flake8 \
        pylint \
        pytest \
        coverage
}

# Function to set up PostgreSQL database and users
setup_database() {
    print_status "Setting up PostgreSQL database and user..."

    # Check if the current user exists as a PostgreSQL role
    if ! sudo -u postgres psql -tAc "SELECT 1 FROM pg_roles WHERE rolname='$USER'" | grep -q 1; then
        print_status "Creating PostgreSQL user '$USER'. You will be prompted to set a password."
        # Create a PostgreSQL user with superuser and database creation privileges
        sudo -u postgres createuser --createdb --superuser --replication --pwprompt "$USER"
    else
        print_warning "PostgreSQL user '$USER' already exists."
    fi

    # Create the development database for OpenSPP
    if ! sudo -u postgres psql -tAc "SELECT 1 FROM pg_database WHERE datname='openspp_dev'" | grep -q 1; then
        print_status "Creating development database 'openspp_dev'..."
        sudo -u postgres createdb -O "$USER" openspp_dev
    else
        print_warning "Database 'openspp_dev' already exists."
    fi

    # Create the test database for OpenSPP
    if ! sudo -u postgres psql -tAc "SELECT 1 FROM pg_database WHERE datname='openspp_test'" | grep -q 1; then
        print_status "Creating test database 'openspp_test'..."
        sudo -u postgres createdb -O "$USER" openspp_test
    else
        print_warning "Database 'openspp_test' already exists."
    fi

    print_status "PostgreSQL databases created: openspp_dev, openspp_test"
}

# Function to configure Odoo for OpenSPP development
configure_odoo() {
    print_status "Configuring Odoo for OpenSPP development..."

    # Create the Odoo configuration file (odoo.conf) in the openspp-dev directory
    cat > "$HOME/openspp-dev/odoo.conf" << EOF
[options]
; Database connection settings
db_host = localhost
db_port = 5432
db_user = $USER
db_password = False ; Set to False if using ident authentication or no password for local user

; Addons path - crucial for Odoo to find its own modules and OpenSPP modules
addons_path = $HOME/openspp-dev/openspp-modules,$HOME/openspp-dev/odoo/addons

; Server port settings
http_port = 8069
longpolling_port = 8072

; Development mode settings for faster development
dev_mode = reload,qweb,xml
log_level = info
log_handler = :INFO

; Performance settings for development (single worker, increased timeouts)
workers = 0
limit_time_cpu = 600
limit_time_real = 1200
EOF

    print_status "Odoo configuration created at $HOME/openspp-dev/odoo.conf"
}

# Function to initialize test data by installing base OpenSPP modules
initialize_test_data() {
    print_status "Initializing test data by installing base OpenSPP modules into 'openspp_dev' database..."

    # Ensure virtual environment is active
    source "$HOME/openspp-dev/venv/bin/activate"
    
    # Change to the directory where odoo-bin and odoo.conf are located
    cd "$HOME/openspp-dev"
    
    # Run Odoo to install specified base modules and then stop
    python odoo/odoo-bin \
        --config=odoo.conf \
        -d openspp_dev \
        -i spp_base,spp_programs,spp_beneficiary,spp_eligibility,spp_entitlement \
        --stop-after-init

    print_status "Base OpenSPP modules installed in openspp_dev database."
}

# Function to set up pre-commit hooks for code quality
setup_precommit() {
    print_status "Setting up pre-commit hooks in openspp-modules repository..."

    # Change to the openspp-modules directory where hooks will be configured
    cd "$HOME/openspp-dev/openspp-modules"

    # Create the .pre-commit-config.yaml file
    cat > .pre-commit-config.yaml << 'EOF'
# Pre-commit configuration for OpenSPP modules
repos:
  # Black for code formatting
  - repo: https://github.com/psf/black
    rev: 23.3.0 # Specify a fixed version for consistency
    hooks:
      - id: black
        language_version: python3

  # Flake8 for linting
  - repo: https://github.com/pycqa/flake8
    rev: 6.0.0 # Specify a fixed version
    hooks:
      - id: flake8
        args: ['--max-line-length=120', '--extend-ignore=E203,W503'] # Common Odoo linting rules

  # General pre-commit hooks
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0 # Specify a fixed version
    hooks:
      - id: trailing-whitespace # Removes trailing whitespace
      - id: end-of-file-fixer   # Ensures files end with a newline
      - id: check-yaml          # Checks YAML file syntax
      - id: check-added-large-files # Prevents committing large files
EOF

    # Ensure virtual environment is active to use the 'pre-commit' command
    source "$HOME/openspp-dev/venv/bin/activate"
    # Install the configured pre-commit hooks into the Git repository
    pre-commit install

    print_status "Pre-commit hooks configured for openspp-modules."
}

# Function to create helper scripts for starting and updating OpenSPP
create_helper_scripts() {
    print_status "Creating helper scripts (start_openspp.sh, update_openspp.sh)..."

    # Create script to start the OpenSPP development server
    cat > "$HOME/openspp-dev/start_openspp.sh" << 'EOF'
#!/bin/bash
# Start OpenSPP development server

# Activate the Python virtual environment
source "$HOME/openspp-dev/venv/bin/activate"
# Change to the directory containing odoo-bin and odoo.conf
cd "$HOME/openspp-dev"
# Run Odoo with the development configuration
python odoo/odoo-bin -c odoo.conf
EOF
    # Make the start script executable
    chmod +x "$HOME/openspp-dev/start_openspp.sh"

    # Create script to update the OpenSPP development environment
    cat > "$HOME/openspp-dev/update_openspp.sh" << 'EOF'
#!/bin/bash
# Update OpenSPP development environment

# Activate the Python virtual environment
source "$HOME/openspp-dev/venv/bin/activate"

# Update OpenSPP modules repository
echo "Updating openspp-modules repository..."
cd "$HOME/openspp-dev/openspp-modules"
git pull origin main

# Update Odoo repository
echo "Updating Odoo repository..."
cd "$HOME/openspp-dev/odoo"
git pull origin 15.0

# Install any new Python dependencies
echo "Installing/updating Python dependencies..."
cd "$HOME/openspp-dev"
pip install -r odoo/requirements.txt
if [ -f openspp-modules/requirements.txt ]; then
    pip install -r openspp-modules/requirements.txt
fi

# Update all installed modules in the development database
echo "Updating OpenSPP modules in the 'openspp_dev' database..."
python odoo/odoo-bin -c odoo.conf -u all -d openspp_dev --stop-after-init

echo "OpenSPP development environment updated successfully!"
EOF
    # Make the update script executable
    chmod +x "$HOME/openspp-dev/update_openspp.sh"

    print_status "Helper scripts created in $HOME/openspp-dev."
}

# Function to verify the installation by checking key components
verify_installation() {
    print_status "Verifying installation..."

    local errors=0 # Counter for errors found

    # Check Python installation
    if command_exists python3; then
        print_status "✓ Python installed: $(python3 --version)"
    else
        print_error "✗ Python not found"
        ((errors++))
    fi

    # Check PostgreSQL client installation
    if command_exists psql; then
        print_status "✓ PostgreSQL client installed: $(psql --version)"
    else
        print_error "✗ PostgreSQL client not found"
        ((errors++))
    fi

    # Check Git installation
    if command_exists git; then
        print_status "✓ Git installed: $(git --version)"
    else
        print_error "✗ Git not found"
        ((errors++))
    fi

    # Check if the Python virtual environment exists
    if [ -f "$HOME/openspp-dev/venv/bin/activate" ]; then
        print_status "✓ Virtual environment created"
    else
        print_error "✗ Virtual environment not found at $HOME/openspp-dev/venv"
        ((errors++))
    fi

    # Check if OpenSPP modules and Odoo repositories are cloned
    if [ -d "$HOME/openspp-dev/openspp-modules" ] && [ -d "$HOME/openspp-dev/odoo" ]; then
        print_status "✓ OpenSPP modules and Odoo repositories cloned"
    else
        print_error "✗ OpenSPP modules or Odoo repository not found in $HOME/openspp-dev"
        ((errors++))
    fi

    # Check if the main development database exists
    if sudo -u postgres psql -lqt | cut -d \| -f 1 | grep -qw openspp_dev; then
        print_status "✓ Database 'openspp_dev' exists"
    else
        print_error "✗ Database 'openspp_dev' not found"
        ((errors++))
    fi

    # Final summary of verification
    if [ "$errors" -eq 0 ]; then
        print_status "✅ All checks passed! OpenSPP development environment is ready."
        return 0 # Success
    else
        print_error "❌ $errors checks failed. Please review the errors above and troubleshoot."
        return 1 # Failure
    fi
}

# Function to display final instructions and next steps to the user
display_next_steps() {
    cat << EOF

${GREEN}��� OpenSPP Development Environment Setup Complete!${NC}

${YELLOW}Next steps:${NC}
1.  To start working, activate your virtual environment:
    ${GREEN}source ~/openspp-dev/venv/bin/activate${NC}

2.  Start the OpenSPP development server:
    ${GREEN}~/openspp-dev/start_openspp.sh${NC}
    (This will start the Odoo server, which hosts OpenSPP. You can stop it with Ctrl+C.)

3.  Access OpenSPP in your web browser at:
    ${GREEN}http://localhost:8069${NC}
    (The default login is 'admin' with password 'admin' if you created a new database.)

4.  To update your development environment (pull latest code, update dependencies, update database modules):
    ${GREEN}~/openspp-dev/update_openspp.sh${NC}

${YELLOW}Useful paths:${NC}
-   OpenSPP development root: ${GREEN}~/openspp-dev${NC}
-   OpenSPP modules repository: ${GREEN}~/openspp-dev/openspp-modules${NC}
-   Odoo configuration file: ${GREEN}~/openspp-dev/odoo.conf${NC}
-   Python virtual environment: ${GREEN}~/openspp-dev/venv${NC}
-   OpenSPP documentation repository: ${GREEN}~/openspp-dev/openspp-docs${NC}

${YELLOW}Troubleshooting Tips:${NC}
-   If you encounter permission issues, ensure you have `sudo` privileges.
-   If PostgreSQL fails to start, check its logs (`/var/log/postgresql/`) or try `sudo service postgresql start` (Linux) or `brew services start postgresql@${POSTGRES_VERSION}` (macOS).
-   For Python dependency errors, try `pip install -r requirements.txt` again after activating the virtual environment.

Happy coding! ���
EOF
}

# Main installation flow function
main() {
    echo "======================================"
    echo " OpenSPP Development Environment Setup"
    echo "======================================"
    echo

    # Parse command line arguments to allow customization
    while [[ $# -gt 0 ]]; do
        case "$1" in
            --branch)
                OPENSPP_BRANCH="$2"
                shift 2
                ;;
            --python)
                PYTHON_VERSION="$2"
                shift 2
                ;;
            --odoo-version) # Added option to specify Odoo version
                ODOO_VERSION="$2"
                shift 2
                ;;
            --help)
                echo "Usage: $0 [options]"
                echo "Options:"
                echo "  --branch BRANCH      OpenSPP modules branch to checkout (default: main)"
                echo "  --python VERSION     Python version to use (e.g., 3.9, 3.10, default: 3.10)"
                echo "  --odoo-version VERSION Odoo version to clone (e.g., 15.0, 16.0, default: 15.0)"
                echo "  --help               Show this help message"
                exit 0
                ;;
            *)
                print_error "Unknown option: $1"
                exit 1
                ;;
        esac
    done

    # Step 1: Detect operating system
    detect_os

    if [ "$OS" == "unknown" ]; then
        print_error "Unsupported operating system. This script only supports Debian/Ubuntu and macOS."
        exit 1
    fi

    # Step 2: Install system dependencies based on detected OS
    if [ "$OS" == "debian" ]; then
        install_debian_dependencies
    elif [ "$OS" == "macos" ]; then
        install_macos_dependencies
    else
        # This block should ideally not be reached due to the earlier check, but kept for robustness.
        print_error "Unsupported OS. This script only supports Debian/Ubuntu and macOS."
        exit 1
    fi

    # Step 3: Set up Python virtual environment
    setup_python_env

    # Step 4: Clone OpenSPP and Odoo repositories
    clone_repositories

    # Step 5: Install Python dependencies within the virtual environment
    install_python_dependencies

    # Step 6: Set up PostgreSQL database and user
    setup_database

    # Step 7: Configure Odoo
    configure_odoo

    # Step 8: Initialize test data by installing base modules
    initialize_test_data

    # Step 9: Set up pre-commit hooks for code quality
    setup_precommit

    # Step 10: Create helper scripts for starting and updating the environment
    create_helper_scripts

    # Step 11: Verify the entire installation
    if verify_installation; then
        display_next_steps # Show success message and next steps
    else
        print_error "Installation completed with errors. Please check the output above for details."
        exit 1 # Exit with error code if verification failed
    fi
}

# Run the main function with all command-line arguments
main "$@"#!/bin/bash
# OpenSPP Development Environment Setup Script
# Supports: Ubuntu 20.04+, Debian 10+, macOS 10.15+
#
# This script automates the setup of a complete OpenSPP development environment
# including all dependencies, database configuration, and development tools.

set -e    # Exit on error if any command fails

# Color codes for output to make messages more readable
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Configuration variables - these can be overridden by command-line arguments
PYTHON_VERSION="3.10"
POSTGRES_VERSION="14"
NODE_VERSION="18"
OPENSPP_BRANCH="main"
ODOO_VERSION="15.0" # Default Odoo version to clone and use

# Function to print colored informational messages
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

# Function to print colored error messages
print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Function to print colored warning messages
print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

# Function to detect the operating system and distribution
detect_os() {
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # Check for Debian-based systems (Ubuntu, Debian)
        if [ -f /etc/debian_version ]; then
            OS="debian"
            DISTRO=$(lsb_release -si 2>/dev/null || echo "Unknown Debian/Ubuntu")
        # Check for RedHat-based systems (CentOS, Fedora, RHEL) - currently not supported by install functions
        elif [ -f /etc/redhat-release ]; then
            OS="redhat" # Mark as redhat, but actual installation will be skipped later
            DISTRO=$(cat /etc/redhat-release)
        else
            OS="unknown"
        fi
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        # Detect macOS
        OS="macos"
        DISTRO="macOS $(sw_vers -productVersion)"
    else
        OS="unknown"
    fi

    print_status "Detected OS: $OS ($DISTRO)"
}

# Function to check if a command exists in the system's PATH
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to install system-level dependencies for Debian/Ubuntu
install_debian_dependencies() {
    print_status "Updating package lists..."
    # Update apt package index
    sudo apt-get update

    print_status "Installing system dependencies for Debian/Ubuntu..."
    # Install common build tools, version control, and Python development headers
    # Also includes libraries for image processing (Pillow), XML (lxml), LDAP, and PostgreSQL client
    sudo apt-get install -y \
        build-essential \
        wget \
        git \
        python3-pip \
        python3-dev \
        python3-venv \
        python3-wheel \
        libxml2-dev \
        libxslt1-dev \
        libldap2-dev \
        libsasl2-dev \
        libtiff5-dev \
        libjpeg8-dev \
        libopenjp2-7-dev \
        zlib1g-dev \
        libfreetype6-dev \
        liblcms2-dev \
        libwebp-dev \
        libharfbuzz-dev \
        libfribidi-dev \
        libxcb1-dev \
        libpq-dev \
        libssl-dev \
        libffi-dev \
        nodejs \
        npm \
        postgresql-$POSTGRES_VERSION \
        postgresql-client-$POSTGRES_VERSION \
        postgresql-server-dev-$POSTGRES_VERSION
}

# Function to install system-level dependencies for macOS using Homebrew
install_macos_dependencies() {
    # Check if Homebrew (macOS package manager) is installed
    if ! command_exists brew; then
        print_status "Installing Homebrew..."
        # Install Homebrew if it's not found
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        # Add Homebrew to PATH for current session
        eval "$(/opt/homebrew/bin/brew shellenv)" || eval "$(/usr/local/bin/brew shellenv)"
    fi

    print_status "Installing system dependencies for macOS..."
    # Install Python, PostgreSQL, Node.js, Git, and various libraries via Homebrew
    brew install \
        python@$PYTHON_VERSION \
        postgresql@$POSTGRES_VERSION \
        node@$NODE_VERSION \
        git \
        wget \
        libxml2 \
        libxslt \
        libjpeg \
        libpng \
        freetype \
        openssl

    # Start PostgreSQL service via Homebrew services
    print_status "Starting PostgreSQL service..."
    brew services start postgresql@$POSTGRES_VERSION || print_warning "PostgreSQL service might already be running or failed to start."
}

# Function to set up the Python virtual environment for OpenSPP
setup_python_env() {
    print_status "Setting up Python virtual environment..."

    # Create the base directory for OpenSPP development if it doesn't exist
    mkdir -p "$HOME/openspp-dev"
    cd "$HOME/openspp-dev"

    # Create the virtual environment using the specified Python version
    python"$PYTHON_VERSION" -m venv venv
    
    # Activate the virtual environment for the current script session
    source venv/bin/activate

    # Upgrade pip, wheel, and setuptools within the virtual environment
    pip install --upgrade pip wheel setuptools

    print_status "Python virtual environment created and activated at $HOME/openspp-dev/venv"
}

# Function to clone OpenSPP and Odoo repositories
clone_repositories() {
    print_status "Cloning Odoo and OpenSPP repositories..."

    cd "$HOME/openspp-dev"

    # Clone Odoo repository
    if [ ! -d "odoo" ]; then
        print_status "Cloning Odoo ($ODOO_VERSION branch)..."
        git clone --depth 1 --branch "$ODOO_VERSION" https://github.com/odoo/odoo.git
    else
        print_warning "odoo directory already exists, skipping clone. Please update manually if needed."
    fi

    # Clone OpenSPP modules repository
    if [ ! -d "openspp-modules" ]; then
        print_status "Cloning OpenSPP modules ($OPENSPP_BRANCH branch)..."
        git clone --depth 1 --branch "$OPENSPP_BRANCH" https://github.com/OpenSPP/openspp-modules.git
    else
        print_warning "openspp-modules directory already exists, skipping clone. Please update manually if needed."
    fi

    # Clone OpenSPP documentation repository
    if [ ! -d "openspp-docs" ]; then
        print_status "Cloning OpenSPP documentation..."
        git clone --depth 1 https://github.com/OpenSPP/openspp-docs.git
    else
        print_warning "openspp-docs directory already exists, skipping clone. Please update manually if needed."
    fi
}

# Function to install Python dependencies from requirements files
install_python_dependencies() {
    print_status "Installing Python dependencies..."

    # Ensure virtual environment is active
    source "$HOME/openspp-dev/venv/bin/activate"

    # Install Odoo's Python dependencies
    print_status "Installing Odoo requirements..."
    pip install -r "$HOME/openspp-dev/odoo/requirements.txt"

    # Install additional OpenSPP specific dependencies if a requirements.txt exists
    if [ -f "$HOME/openspp-dev/openspp-modules/requirements.txt" ]; then
        print_status "Installing OpenSPP modules requirements..."
        pip install -r "$HOME/openspp-dev/openspp-modules/requirements.txt"
    else
        print_warning "No requirements.txt found in openspp-modules, skipping specific OpenSPP Python dependencies."
    fi

    # Install common Python development tools
    print_status "Installing Python development tools (pre-commit, black, flake8, etc.)..."
    pip install \
        pre-commit \
        black \
        flake8 \
        pylint \
        pytest \
        coverage
}

# Function to set up PostgreSQL database and users
setup_database() {
    print_status "Setting up PostgreSQL database and user..."

    # Check if the current user exists as a PostgreSQL role
    if ! sudo -u postgres psql -tAc "SELECT 1 FROM pg_roles WHERE rolname='$USER'" | grep -q 1; then
        print_status "Creating PostgreSQL user '$USER'. You will be prompted to set a password."
        # Create a PostgreSQL user with superuser and database creation privileges
        sudo -u postgres createuser --createdb --superuser --replication --pwprompt "$USER"
    else
        print_warning "PostgreSQL user '$USER' already exists."
    fi

    # Create the development database for OpenSPP
    if ! sudo -u postgres psql -tAc "SELECT 1 FROM pg_database WHERE datname='openspp_dev'" | grep -q 1; then
        print_status "Creating development database 'openspp_dev'..."
        sudo -u postgres createdb -O "$USER" openspp_dev
    else
        print_warning "Database 'openspp_dev' already exists."
    fi

    # Create the test database for OpenSPP
    if ! sudo -u postgres psql -tAc "SELECT 1 FROM pg_database WHERE datname='openspp_test'" | grep -q 1; then
        print_status "Creating test database 'openspp_test'..."
        sudo -u postgres createdb -O "$USER" openspp_test
    else
        print_warning "Database 'openspp_test' already exists."
    fi

    print_status "PostgreSQL databases created: openspp_dev, openspp_test"
}

# Function to configure Odoo for OpenSPP development
configure_odoo() {
    print_status "Configuring Odoo for OpenSPP development..."

    # Create the Odoo configuration file (odoo.conf) in the openspp-dev directory
    cat > "$HOME/openspp-dev/odoo.conf" << EOF
[options]
; Database connection settings
db_host = localhost
db_port = 5432
db_user = $USER
db_password = False ; Set to False if using ident authentication or no password for local user

; Addons path - crucial for Odoo to find its own modules and OpenSPP modules
addons_path = $HOME/openspp-dev/openspp-modules,$HOME/openspp-dev/odoo/addons

; Server port settings
http_port = 8069
longpolling_port = 8072

; Development mode settings for faster development
dev_mode = reload,qweb,xml
log_level = info
log_handler = :INFO

; Performance settings for development (single worker, increased timeouts)
workers = 0
limit_time_cpu = 600
limit_time_real = 1200
EOF

    print_status "Odoo configuration created at $HOME/openspp-dev/odoo.conf"
}

# Function to initialize test data by installing base OpenSPP modules
initialize_test_data() {
    print_status "Initializing test data by installing base OpenSPP modules into 'openspp_dev' database..."

    # Ensure virtual environment is active
    source "$HOME/openspp-dev/venv/bin/activate"
    
    # Change to the directory where odoo-bin and odoo.conf are located
    cd "$HOME/openspp-dev"
    
    # Run Odoo to install specified base modules and then stop
    python odoo/odoo-bin \
        --config=odoo.conf \
        -d openspp_dev \
        -i spp_base,spp_programs,spp_beneficiary,spp_eligibility,spp_entitlement \
        --stop-after-init

    print_status "Base OpenSPP modules installed in openspp_dev database."
}

# Function to set up pre-commit hooks for code quality
setup_precommit() {
    print_status "Setting up pre-commit hooks in openspp-modules repository..."

    # Change to the openspp-modules directory where hooks will be configured
    cd "$HOME/openspp-dev/openspp-modules"

    # Create the .pre-commit-config.yaml file
    cat > .pre-commit-config.yaml << 'EOF'
# Pre-commit configuration for OpenSPP modules
repos:
  # Black for code formatting
  - repo: https://github.com/psf/black
    rev: 23.3.0 # Specify a fixed version for consistency
    hooks:
      - id: black
        language_version: python3

  # Flake8 for linting
  - repo: https://github.com/pycqa/flake8
    rev: 6.0.0 # Specify a fixed version
    hooks:
      - id: flake8
        args: ['--max-line-length=120', '--extend-ignore=E203,W503'] # Common Odoo linting rules

  # General pre-commit hooks
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0 # Specify a fixed version
    hooks:
      - id: trailing-whitespace # Removes trailing whitespace
      - id: end-of-file-fixer   # Ensures files end with a newline
      - id: check-yaml          # Checks YAML file syntax
      - id: check-added-large-files # Prevents committing large files
EOF

    # Ensure virtual environment is active to use the 'pre-commit' command
    source "$HOME/openspp-dev/venv/bin/activate"
    # Install the configured pre-commit hooks into the Git repository
    pre-commit install

    print_status "Pre-commit hooks configured for openspp-modules."
}

# Function to create helper scripts for starting and updating OpenSPP
create_helper_scripts() {
    print_status "Creating helper scripts (start_openspp.sh, update_openspp.sh)..."

    # Create script to start the OpenSPP development server
    cat > "$HOME/openspp-dev/start_openspp.sh" << 'EOF'
#!/bin/bash
# Start OpenSPP development server

# Activate the Python virtual environment
source "$HOME/openspp-dev/venv/bin/activate"
# Change to the directory containing odoo-bin and odoo.conf
cd "$HOME/openspp-dev"
# Run Odoo with the development configuration
python odoo/odoo-bin -c odoo.conf
EOF
    # Make the start script executable
    chmod +x "$HOME/openspp-dev/start_openspp.sh"

    # Create script to update the OpenSPP development environment
    cat > "$HOME/openspp-dev/update_openspp.sh" << 'EOF'
#!/bin/bash
# Update OpenSPP development environment

# Activate the Python virtual environment
source "$HOME/openspp-dev/venv/bin/activate"

# Update OpenSPP modules repository
echo "Updating openspp-modules repository..."
cd "$HOME/openspp-dev/openspp-modules"
git pull origin main

# Update Odoo repository
echo "Updating Odoo repository..."
cd "$HOME/openspp-dev/odoo"
git pull origin 15.0

# Install any new Python dependencies
echo "Installing/updating Python dependencies..."
cd "$HOME/openspp-dev"
pip install -r odoo/requirements.txt
if [ -f openspp-modules/requirements.txt ]; then
    pip install -r openspp-modules/requirements.txt
fi

# Update all installed modules in the development database
echo "Updating OpenSPP modules in the 'openspp_dev' database..."
python odoo/odoo-bin -c odoo.conf -u all -d openspp_dev --stop-after-init

echo "OpenSPP development environment updated successfully!"
EOF
    # Make the update script executable
    chmod +x "$HOME/openspp-dev/update_openspp.sh"

    print_status "Helper scripts created in $HOME/openspp-dev."
}

# Function to verify the installation by checking key components
verify_installation() {
    print_status "Verifying installation..."

    local errors=0 # Counter for errors found

    # Check Python installation
    if command_exists python3; then
        print_status "✓ Python installed: $(python3 --version)"
    else
        print_error "✗ Python not found"
        ((errors++))
    fi

    # Check PostgreSQL client installation
    if command_exists psql; then
        print_status "✓ PostgreSQL client installed: $(psql --version)"
    else
        print_error "✗ PostgreSQL client not found"
        ((errors++))
    fi

    # Check Git installation
    if command_exists git; then
        print_status "✓ Git installed: $(git --version)"
    else
        print_error "✗ Git not found"
        ((errors++))
    fi

    # Check if the Python virtual environment exists
    if [ -f "$HOME/openspp-dev/venv/bin/activate" ]; then
        print_status "✓ Virtual environment created"
    else
        print_error "✗ Virtual environment not found at $HOME/openspp-dev/venv"
        ((errors++))
    fi

    # Check if OpenSPP modules and Odoo repositories are cloned
    if [ -d "$HOME/openspp-dev/openspp-modules" ] && [ -d "$HOME/openspp-dev/odoo" ]; then
        print_status "✓ OpenSPP modules and Odoo repositories cloned"
    else
        print_error "✗ OpenSPP modules or Odoo repository not found in $HOME/openspp-dev"
        ((errors++))
    fi

    # Check if the main development database exists
    if sudo -u postgres psql -lqt | cut -d \| -f 1 | grep -qw openspp_dev; then
        print_status "✓ Database 'openspp_dev' exists"
    else
        print_error "✗ Database 'openspp_dev' not found"
        ((errors++))
    fi

    # Final summary of verification
    if [ "$errors" -eq 0 ]; then
        print_status "✅ All checks passed! OpenSPP development environment is ready."
        return 0 # Success
    else
        print_error "❌ $errors checks failed. Please review the errors above and troubleshoot."
        return 1 # Failure
    fi
}

# Function to display final instructions and next steps to the user
display_next_steps() {
    cat << EOF

${GREEN}��� OpenSPP Development Environment Setup Complete!${NC}

${YELLOW}Next steps:${NC}
1.  To start working, activate your virtual environment:
    ${GREEN}source ~/openspp-dev/venv/bin/activate${NC}

2.  Start the OpenSPP development server:
    ${GREEN}~/openspp-dev/start_openspp.sh${NC}
    (This will start the Odoo server, which hosts OpenSPP. You can stop it with Ctrl+C.)

3.  Access OpenSPP in your web browser at:
    ${GREEN}http://localhost:8069${NC}
    (The default login is 'admin' with password 'admin' if you created a new database.)

4.  To update your development environment (pull latest code, update dependencies, update database modules):
    ${GREEN}~/openspp-dev/update_openspp.sh${NC}

${YELLOW}Useful paths:${NC}
-   OpenSPP development root: ${GREEN}~/openspp-dev${NC}
-   OpenSPP modules repository: ${GREEN}~/openspp-dev/openspp-modules${NC}
-   Odoo configuration file: ${GREEN}~/openspp-dev/odoo.conf${NC}
-   Python virtual environment: ${GREEN}~/openspp-dev/venv${NC}
-   OpenSPP documentation repository: ${GREEN}~/openspp-dev/openspp-docs${NC}

${YELLOW}Troubleshooting Tips:${NC}
-   If you encounter permission issues, ensure you have `sudo` privileges.
-   If PostgreSQL fails to start, check its logs (`/var/log/postgresql/`) or try `sudo service postgresql start` (Linux) or `brew services start postgresql@${POSTGRES_VERSION}` (macOS).
-   For Python dependency errors, try `pip install -r requirements.txt` again after activating the virtual environment.

Happy coding! ���
EOF
}

# Main installation flow function
main() {
    echo "======================================"
    echo " OpenSPP Development Environment Setup"
    echo "======================================"
    echo

    # Parse command line arguments to allow customization
    while [[ $# -gt 0 ]]; do
        case "$1" in
            --branch)
                OPENSPP_BRANCH="$2"
                shift 2
                ;;
            --python)
                PYTHON_VERSION="$2"
                shift 2
                ;;
            --odoo-version) # Added option to specify Odoo version
                ODOO_VERSION="$2"
                shift 2
                ;;
            --help)
                echo "Usage: $0 [options]"
                echo "Options:"
                echo "  --branch BRANCH      OpenSPP modules branch to checkout (default: main)"
                echo "  --python VERSION     Python version to use (e.g., 3.9, 3.10, default: 3.10)"
                echo "  --odoo-version VERSION Odoo version to clone (e.g., 15.0, 16.0, default: 15.0)"
                echo "  --help               Show this help message"
                exit 0
                ;;
            *)
                print_error "Unknown option: $1"
                exit 1
                ;;
        esac
    done

    # Step 1: Detect operating system
    detect_os

    if [ "$OS" == "unknown" ]; then
        print_error "Unsupported operating system. This script only supports Debian/Ubuntu and macOS."
        exit 1
    fi

    # Step 2: Install system dependencies based on detected OS
    if [ "$OS" == "debian" ]; then
        install_debian_dependencies
    elif [ "$OS" == "macos" ]; then
        install_macos_dependencies
    else
        # This block should ideally not be reached due to the earlier check, but kept for robustness.
        print_error "Unsupported OS. This script only supports Debian/Ubuntu and macOS."
        exit 1
    fi

    # Step 3: Set up Python virtual environment
    setup_python_env

    # Step 4: Clone OpenSPP and Odoo repositories
    clone_repositories

    # Step 5: Install Python dependencies within the virtual environment
    install_python_dependencies

    # Step 6: Set up PostgreSQL database and user
    setup_database

    # Step 7: Configure Odoo
    configure_odoo

    # Step 8: Initialize test data by installing base modules
    initialize_test_data

    # Step 9: Set up pre-commit hooks for code quality
    setup_precommit

    # Step 10: Create helper scripts for starting and updating the environment
    create_helper_scripts

    # Step 11: Verify the entire installation
    if verify_installation; then
        display_next_steps # Show success message and next steps
    else
        print_error "Installation completed with errors. Please check the output above for details."
        exit 1 # Exit with error code if verification failed
    fi
}

# Run the main function with all command-line arguments
main "$@"
