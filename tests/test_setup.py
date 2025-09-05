"""
Test script to verify the CrewAI setup with uv and Python 3.10
"""

import sys
import os
from pathlib import Path

# Add the crew4ai directory to the Python path
crew4ai_path = Path(__file__).parent.parent
sys.path.insert(0, str(crew4ai_path))

def test_virtual_environment():
    """Test that we're in the correct virtual environment"""
    # Check that we're using the expected Python version
    python_version = sys.version_info
    assert python_version.major == 3 and python_version.minor == 10, f"Expected Python 3.10, got {python_version.major}.{python_version.minor}"
    print("✓ Correct Python version (3.10)")

def test_dependencies():
    """Test that required dependencies are installed"""
    # Test crewai
    try:
        import crewai
        print("✓ CrewAI imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import CrewAI: {e}")
        return False
    
    # Test crewai-tools
    try:
        import crewai_tools
        print("✓ CrewAI Tools imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import CrewAI Tools: {e}")
        return False
    
    # Test pyyaml
    try:
        import yaml
        print("✓ PyYAML imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import PyYAML: {e}")
        return False
    
    # Test psutil
    try:
        import psutil
        print("✓ psutil imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import psutil: {e}")
        return False
    
    return True

def test_crews():
    """Test that crews can be imported"""
    try:
        from crews.code_review import CodeReviewCrew
        print("✓ CodeReviewCrew imported successfully")
    except Exception as e:
        print(f"✗ Failed to import CodeReviewCrew: {e}")
        return False
    
    try:
        from crews.project_analysis import ProjectAnalysisCrew
        print("✓ ProjectAnalysisCrew imported successfully")
    except Exception as e:
        print(f"✗ Failed to import ProjectAnalysisCrew: {e}")
        return False
    
    try:
        from crews.deployment_troubleshooter import DeploymentTroubleshooterCrew
        print("✓ DeploymentTroubleshooterCrew imported successfully")
    except Exception as e:
        print(f"✗ Failed to import DeploymentTroubleshooterCrew: {e}")
        return False
    
    try:
        from crews.system_troubleshooter import SystemTroubleshooterCrew
        print("✓ SystemTroubleshooterCrew imported successfully")
    except Exception as e:
        print(f"✗ Failed to import SystemTroubleshooterCrew: {e}")
        return False
    
    try:
        from crews.code_recommendation import CodeRecommendationCrew
        print("✓ CodeRecommendationCrew imported successfully")
    except Exception as e:
        print(f"✗ Failed to import CodeRecommendationCrew: {e}")
        return False
    
    try:
        from crews.project_planning import ProjectPlanningCrew
        print("✓ ProjectPlanningCrew imported successfully")
    except Exception as e:
        print(f"✗ Failed to import ProjectPlanningCrew: {e}")
        return False
    
    try:
        from crews.code_generation import CodeGenerationCrew
        print("✓ CodeGenerationCrew imported successfully")
    except Exception as e:
        print(f"✗ Failed to import CodeGenerationCrew: {e}")
        return False
    
    try:
        from crews.full_project_implementation import FullProjectImplementationCrew
        print("✓ FullProjectImplementationCrew imported successfully")
    except Exception as e:
        print(f"✗ Failed to import FullProjectImplementationCrew: {e}")
        return False
    
    return True

def test_config_files():
    """Test that configuration files exist and are readable"""
    config_dir = crew4ai_path / "config"
    
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
                return False
        else:
            print(f"✗ {config_file} does not exist at {file_path}")
            return False
    
    return True

def main():
    print("Testing CrewAI Configuration Setup")
    print("==================================")
    
    # Test virtual environment
    try:
        test_virtual_environment()
    except AssertionError as e:
        print(f"✗ {e}")
        return False
    
    print()
    
    # Test dependencies
    if not test_dependencies():
        return False
    
    print()
    
    # Test crews
    if not test_crews():
        return False
    
    print()
    
    # Test config files
    if not test_config_files():
        return False
    
    print("\nAll tests passed! 🎉")
    return True

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)