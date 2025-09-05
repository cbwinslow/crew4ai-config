# Using CrewAI with uv and Python 3.10

This document explains how to use the CrewAI configuration with uv as the package manager and Python 3.10.

## Prerequisites

- Python 3.10 installed
- uv package manager installed

## Setup

1. Create a virtual environment with Python 3.10:
   ```bash
   uv venv --python 3.10
   ```

2. Activate the virtual environment:
   ```bash
   source .venv/bin/activate
   ```

3. Install the dependencies:
   ```bash
   uv pip install -r requirements.txt
   ```

   Or, if you prefer to use the pyproject.toml file:
   ```bash
   uv pip install .
   ```

## Running Crews

You can run the crews in several ways:

### Method 1: Using the runner script
```bash
./crew4ai.sh <crew-name>
```

### Method 2: Direct execution
```bash
source .venv/bin/activate
python main.py <crew-name>
```

### Method 3: Using Makefile
```bash
make run CREW=<crew-name>
```

## Available Crews

1. `code-review` - Reviews code files for quality, security, and performance
2. `project-analysis` - Reviews projects as a whole for architecture and design
3. `deployment-troubleshooter` - Reviews, configures, and troubleshoots deployment
4. `system-troubleshooter` - Analyzes system logs, processes, CPU usage, I/O issues, network anomalies, etc.
5. `code-recommendation` - Provides detailed recommendations for code improvements and optimizations
6. `project-planning` - Breaks down projects into tasks and creates implementation plans
7. `code-generation` - Writes high-quality code based on specifications
8. `full-project-implementation` - Completes full software projects from planning to implementation

## Example Usage

```bash
# Run the code review crew
./crew4ai.sh code-review

# Run the code recommendation crew
./crew4ai.sh code-recommendation

# Run the project planning crew
./crew4ai.sh project-planning

# Run the code generation crew
./crew4ai.sh code-generation

# Run the full project implementation crew
./crew4ai.sh full-project-implementation
```

## Development

To install development dependencies:
```bash
source .venv/bin/activate
uv pip install -e .[dev]
```

Or using the Makefile:
```bash
make dev
```

## Testing

To run tests:
```bash
source .venv/bin/activate
python -m pytest tests/
```

Or using the Makefile:
```bash
make test
```

## Cleanup

To remove the virtual environment:
```bash
rm -rf .venv/
```

Or using the Makefile:
```bash
make clean
```