#!/bin/bash
# crew4ai runner script

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Activate the virtual environment
source "${SCRIPT_DIR}/.venv/bin/activate"

# Run the main script with all passed arguments
python "${SCRIPT_DIR}/main.py" "$@"