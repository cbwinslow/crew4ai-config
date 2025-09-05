# CrewAI Configuration

This repository contains a collection of pre-configured CrewAI crews for common software development and system administration tasks.

## Overview

CrewAI is a framework for orchestrating role-playing AI agents. This configuration provides ready-to-use crews for code review, project analysis, deployment troubleshooting, and system diagnostics.

## Prerequisites

- Python 3.10
- [uv](https://github.com/astral-sh/uv) package manager (recommended) or pip

## Installation

### Using uv (recommended)

1. Clone this repository:
   ```bash
   git clone <repository-url>
   ```

2. Create a virtual environment and install dependencies using uv:
   ```bash
   cd crew4ai
   uv venv --python 3.10
   source .venv/bin/activate
   uv pip install -r requirements.txt
   ```

   Or, if you prefer to use the pyproject.toml file:
   ```bash
   cd crew4ai
   uv venv --python 3.10
   source .venv/bin/activate
   uv pip install .
   ```

### Using pip

1. Clone this repository:
   ```bash
   git clone <repository-url>
   ```

2. Create a virtual environment and install dependencies using pip:
   ```bash
   cd crew4ai
   python3.10 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. Set up your environment variables for LLM access (OpenAI, Anthropic, etc.)

## Available Crews

### 1. Code Review Crew
Reviews code files for quality, best practices, and potential issues.

Usage:
```bash
python main.py code-review
```

### 2. Project Analysis Crew
Reviews projects as a whole for architecture, design, and big picture issues.

Usage:
```bash
python main.py project-analysis
```

### 3. Deployment Troubleshooter Crew
Reviews, configures, and troubleshoots deployment processes.

Usage:
```bash
python main.py deployment-troubleshooter
```

### 4. System Troubleshooter Crew
Analyzes system logs, processes, CPU usage, I/O issues, network anomalies, etc.

Usage:
```bash
python main.py system-troubleshooter
```

### 5. Code Recommendation Crew
Provides detailed recommendations for code improvements and optimizations.

Usage:
```bash
python main.py code-recommendation
```

### 6. Project Planning Crew
Breaks down projects into tasks and creates implementation plans.

Usage:
```bash
python main.py project-planning
```

### 7. Code Generation Crew
Writes high-quality code based on specifications.

Usage:
```bash
python main.py code-generation
```

### 8. Full Project Implementation Crew
Completes full software projects from planning to implementation.

Usage:
```bash
python main.py full-project-implementation
```

## Configuration

The configuration files are located in the `config/` directory:
- `agents.yaml` - Defines the roles, goals, and backstories of agents
- `tasks.yaml` - Defines the tasks assigned to agents
- `crewai_config.yaml` - General CrewAI configuration settings

## Directory Structure

```
crew4ai/
├── config/          # Configuration files
├── crews/           # Crew implementations
├── tools/           # Custom tools (may have dependency conflicts)
├── examples/        # Usage examples
├── docs/            # Documentation
├── requirements.txt # Python dependencies
├── pyproject.toml   # Project configuration for uv
├── main.py         # Main entry point
├── crew4ai.sh      # Runner script
├── Makefile        # Makefile for common tasks
├── README.md       # This file
└── LICENSE         # License file
```

## Usage Examples

Run any of the available crews using the main entry point:

```bash
# Activate the virtual environment first
source .venv/bin/activate

# Run the code review crew
python main.py code-review

# Run the code recommendation crew
python main.py code-recommendation

# Run the project planning crew
python main.py project-planning

# Run the code generation crew
python main.py code-generation

# Run the full project implementation crew
python main.py full-project-implementation
```

Or use the provided runner script:
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

Or use the Makefile:
```bash
# Run the code review crew
make run CREW=code-review

# Run the code recommendation crew
make run CREW=code-recommendation

# Run the project planning crew
make run CREW=project-planning

# Run the code generation crew
make run CREW=code-generation

# Run the full project implementation crew
make run CREW=full-project-implementation
```

## Customization

To customize the crews for your specific needs:

1. Modify the agent configurations in `config/agents.yaml`
2. Adjust the task definitions in `config/tasks.yaml`
3. Update the general settings in `config/crewai_config.yaml`

## Documentation

For more detailed information about using CrewAI with uv, see [docs/uv_usage.md](docs/uv_usage.md).

## Troubleshooting

If you encounter dependency conflicts with the tools in the `tools/` directory, you can still use the crews without those tools by running the main entry point directly.

## Contributing

Contributions are welcome! Please submit a pull request with your improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.