#!/usr/bin/env python3
"""
Example: Using the New CrewAI Crews
===================================

This script demonstrates how to use the new CrewAI crews for coding tasks.
"""

import sys
from pathlib import Path

# Add the crew4ai directory to the Python path
sys.path.insert(0, str(Path(__file__).parent))

def main():
    print("CrewAI Coding Crews Example")
    print("===========================")
    print()
    print("This repository now includes 8 different crews for software development tasks:")
    print()
    print("1. Code Review Crew")
    print("   - Reviews code files for quality, security, and performance")
    print()
    print("2. Project Analysis Crew")
    print("   - Reviews projects as a whole for architecture and design")
    print()
    print("3. Deployment Troubleshooter Crew")
    print("   - Reviews, configures, and troubleshoots deployment processes")
    print()
    print("4. System Troubleshooter Crew")
    print("   - Analyzes system logs, processes, CPU usage, I/O issues, network anomalies, etc.")
    print()
    print("5. Code Recommendation Crew")
    print("   - Provides detailed recommendations for code improvements and optimizations")
    print()
    print("6. Project Planning Crew")
    print("   - Breaks down projects into tasks and creates implementation plans")
    print()
    print("7. Code Generation Crew")
    print("   - Writes high-quality code based on specifications")
    print()
    print("8. Full Project Implementation Crew")
    print("   - Completes full software projects from planning to implementation")
    print()
    print("To run any of these crews, use:")
    print("  ./crew4ai.sh <crew-name>")
    print()
    print("Example:")
    print("  ./crew4ai.sh code-recommendation")

if __name__ == '__main__':
    main()