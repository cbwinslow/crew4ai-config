#!/usr/bin/env python3
"""
Test Script for CrewAI Configuration
====================================

This script tests that all components of the CrewAI configuration are working correctly.
"""

import sys
from pathlib import Path

# Add the crew4ai directory to the Python path
sys.path.insert(0, str(Path(__file__).parent))

def test_imports():
    """Test that all modules can be imported."""
    try:
        from crews.code_review import CodeReviewCrew
        print("✓ CodeReviewCrew imported successfully")
    except Exception as e:
        print(f"✗ Failed to import CodeReviewCrew: {e}")
    
    try:
        from crews.project_analysis import ProjectAnalysisCrew
        print("✓ ProjectAnalysisCrew imported successfully")
    except Exception as e:
        print(f"✗ Failed to import ProjectAnalysisCrew: {e}")
    
    try:
        from crews.deployment_troubleshooter import DeploymentTroubleshooterCrew
        print("✓ DeploymentTroubleshooterCrew imported successfully")
    except Exception as e:
        print(f"✗ Failed to import DeploymentTroubleshooterCrew: {e}")
    
    try:
        from crews.system_troubleshooter import SystemTroubleshooterCrew
        print("✓ SystemTroubleshooterCrew imported successfully")
    except Exception as e:
        print(f"✗ Failed to import SystemTroubleshooterCrew: {e}")
    
    # Test tools with error handling
    tools = [
        ("FileReaderTool", "tools.file_reader"),
        ("SystemMonitorTool", "tools.system_monitor"),
        ("LogAnalyzerTool", "tools.log_analyzer"),
        ("DocumentationGeneratorTool", "tools.documentation_generator"),
        ("DeploymentCheckerTool", "tools.deployment_checker")
    ]
    
    for tool_name, module_path in tools:
        try:
            module = __import__(module_path, fromlist=[tool_name])
            tool_class = getattr(module, tool_name)
            print(f"✓ {tool_name} imported successfully")
        except Exception as e:
            print(f"✗ Failed to import {tool_name}: {e}")

def test_config_files():
    """Test that configuration files exist and are readable."""
    config_dir = Path(__file__).parent / "config"
    
    config_files = [
        "agents.yaml",
        "tasks.yaml",
        "crewai_config.yaml"
    ]
    
    for config_file in config_files:
        file_path = config_dir / config_file
        if file_path.exists():
            try:
                with open(file_path, 'r') as f:
                    f.read(100)  # Read first 100 characters
                print(f"✓ {config_file} exists and is readable")
            except Exception as e:
                print(f"✗ {config_file} exists but could not be read: {e}")
        else:
            print(f"✗ {config_file} does not exist")

if __name__ == '__main__':
    print("Testing CrewAI Configuration Setup")
    print("==================================")
    
    test_imports()
    print()
    test_config_files()
    
    print("\nTest completed.")
