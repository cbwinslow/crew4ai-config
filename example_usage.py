#!/usr/bin/env python3
"""
Simple CrewAI Usage Example
===========================

This script demonstrates how to use the CrewAI configuration.
"""

import sys
from pathlib import Path

# Add the crew4ai directory to the Python path
sys.path.insert(0, str(Path(__file__).parent))

def main():
    print("CrewAI Configuration Example")
    print("============================")
    print()
    print("Available crews:")
    print("1. code-review - Reviews code files for quality, security, and performance")
    print("2. project-analysis - Reviews projects as a whole for architecture and design")
    print("3. deployment-troubleshooter - Reviews, configures, and troubleshoots deployment")
    print("4. system-troubleshooter - Analyzes system logs, processes, CPU usage, I/O issues, network anomalies, etc.")
    print("5. code-recommendation - Provides detailed recommendations for code improvements and optimizations")
    print("6. project-planning - Breaks down projects into tasks and creates implementation plans")
    print("7. code-generation - Writes high-quality code based on specifications")
    print("8. full-project-implementation - Completes full software projects from planning to implementation")
    print()
    print("To run a crew, you can use either:")
    print("  ./crew4ai.sh <crew-name>")
    print("or")
    print("  source .venv/bin/activate && python main.py <crew-name>")
    print()
    print("Examples:")
    print("  ./crew4ai.sh code-review")
    print("  ./crew4ai.sh code-recommendation")
    print("  ./crew4ai.sh project-planning")
    print("  ./crew4ai.sh code-generation")
    print("  ./crew4ai.sh full-project-implementation")

if __name__ == '__main__':
    main()