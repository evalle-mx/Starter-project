#!/bin/bash

# This code check dependences requires to Run the Scripts  (AMER TAP Bot - Development Startup Script)
# ./start-dev.sh

echo "🚀 Starting AMER TAP Bot in Development Mode"
echo "=" * 50

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check for required dependencies
echo "📦 Checking dependencies..."


if command_exists node; then
    echo "✅  Node.js is installed"
else
    echo "❌ Node.js is not installed. Please install Node.js 16+ and try again."
fi

if ! command_exists npm; then
    echo "❌ npm is not installed. Please install npm and try again."
else
    echo "✅  npm is installed"
fi

if ! command_exists python3; then
    echo "❌ Python 3 is not installed. Please install Python 3.11+ and try again."
else
    echo "✅  Python 3 is installed"
fi


# Check Python version matches staging/production (3.11)
PYTHON_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
REQUIRED_VERSION="3.11"

if [[ "$PYTHON_VERSION" != "$REQUIRED_VERSION"* ]]; then
    echo "⚠️  Warning: Python $PYTHON_VERSION detected, but staging uses Python $REQUIRED_VERSION"
    echo "   This may cause subtle behavioral differences (e.g., enum str() representation)"
    echo ""
    echo "   To fix, install Python 3.11 via pyenv:"
    echo "     brew install pyenv"
    echo "     pyenv install 3.11.9"
    echo "     pyenv local 3.11.9"
    echo "     rm -rf backend/myvenv && python3 -m venv backend/myvenv"
    echo ""
    read -p "   Continue anyway? [y/N] " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

echo "✅ All dependencies found (Python $PYTHON_VERSION)"

exit 1