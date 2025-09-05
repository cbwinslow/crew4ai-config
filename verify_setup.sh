#!/bin/bash
# Verification script for CrewAI setup with uv and Python 3.10

echo "Verifying CrewAI setup with uv and Python 3.10"
echo "============================================="

# Check if uv is installed
if ! command -v uv &> /dev/null
then
    echo "✗ uv is not installed"
    exit 1
else
    echo "✓ uv is installed"
fi

# Check if Python 3.10 is available
if ! python3.10 --version &> /dev/null
then
    echo "✗ Python 3.10 is not available"
    exit 1
else
    echo "✓ Python 3.10 is available"
fi

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    uv venv --python 3.10
fi

# Activate virtual environment
source .venv/bin/activate

# Check Python version in virtual environment
PYTHON_VERSION=$(python --version)
if [[ $PYTHON_VERSION == *"3.10"* ]]; then
    echo "✓ Correct Python version in virtual environment: $PYTHON_VERSION"
else
    echo "✗ Incorrect Python version in virtual environment: $PYTHON_VERSION"
    exit 1
fi

# Check if dependencies are installed
echo "Checking dependencies..."
python -c "import crewai; print('✓ CrewAI imported successfully')"
python -c "import crewai_tools; print('✓ CrewAI Tools imported successfully')"
python -c "import yaml; print('✓ PyYAML imported successfully')"
python -c "import psutil; print('✓ psutil imported successfully')"

# Check if crews can be imported
echo "Checking crews..."
python -c "from crews.code_review import CodeReviewCrew; print('✓ CodeReviewCrew imported successfully')"
python -c "from crews.project_analysis import ProjectAnalysisCrew; print('✓ ProjectAnalysisCrew imported successfully')"
python -c "from crews.deployment_troubleshooter import DeploymentTroubleshooterCrew; print('✓ DeploymentTroubleshooterCrew imported successfully')"
python -c "from crews.system_troubleshooter import SystemTroubleshooterCrew; print('✓ SystemTroubleshooterCrew imported successfully')"
python -c "from crews.code_recommendation import CodeRecommendationCrew; print('✓ CodeRecommendationCrew imported successfully')"
python -c "from crews.project_planning import ProjectPlanningCrew; print('✓ ProjectPlanningCrew imported successfully')"
python -c "from crews.code_generation import CodeGenerationCrew; print('✓ CodeGenerationCrew imported successfully')"
python -c "from crews.full_project_implementation import FullProjectImplementationCrew; print('✓ FullProjectImplementationCrew imported successfully')"

# Check config files
echo "Checking config files..."
if [ -f "config/agents.yaml" ]; then
    echo "✓ agents.yaml exists"
else
    echo "✗ agents.yaml does not exist"
    exit 1
fi

if [ -f "config/tasks.yaml" ]; then
    echo "✓ tasks.yaml exists"
else
    echo "✗ tasks.yaml does not exist"
    exit 1
fi

if [ -f "config/crewai_config.yaml" ]; then
    echo "✓ crewai_config.yaml exists"
else
    echo "✗ crewai_config.yaml does not exist"
    exit 1
fi

echo ""
echo "All checks passed! Your CrewAI setup with uv and Python 3.10 is ready to use."