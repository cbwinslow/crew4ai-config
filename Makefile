# Makefile for CrewAI Configuration

# Variables
PYTHON = python3.10
UV = uv

# Default target
.PHONY: help
help:
	@echo "CrewAI Configuration Makefile"
	@echo "============================="
	@echo "Available targets:"
	@echo "  setup     - Set up the virtual environment and install dependencies"
	@echo "  run       - Run a crew (specify with CREW=crew-name)"
	@echo "  test      - Run tests"
	@echo "  clean     - Remove the virtual environment"
	@echo "  help      - Show this help message"

# Set up the virtual environment and install dependencies
.PHONY: setup
setup:
	$(UV) venv --python $(PYTHON)
	source .venv/bin/activate && $(UV) pip install -r requirements.txt

# Run a crew
.PHONY: run
run:
	@if [ -z "$(CREW)" ]; then \
		echo "Please specify a crew to run with CREW=crew-name"; \
		echo "Available crews: code-review, project-analysis, deployment-troubleshooter, system-troubleshooter, code-recommendation, project-planning, code-generation, full-project-implementation"; \
		exit 1; \
	fi
	source .venv/bin/activate && python main.py $(CREW)

# Run tests
.PHONY: test
test:
	source .venv/bin/activate && python -m pytest tests/

# Remove the virtual environment
.PHONY: clean
clean:
	rm -rf .venv/

# Install development dependencies
.PHONY: dev
dev:
	source .venv/bin/activate && $(UV) pip install -e .[dev]