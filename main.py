#!/usr/bin/env python3
"""
CrewAI Configuration Main Entry Point
=====================================

This script provides a command-line interface to run different crews.
"""

import argparse
import sys
from pathlib import Path

# Add the crew4ai directory to the Python path
sys.path.insert(0, str(Path(__file__).parent))

def main():
    parser = argparse.ArgumentParser(description='CrewAI Configuration Runner')
    parser.add_argument(
        'crew',
        choices=[
            'code-review', 
            'project-analysis', 
            'deployment-troubleshooter', 
            'system-troubleshooter',
            'code-recommendation',
            'project-planning',
            'code-generation',
            'full-project-implementation'
        ],
        help='Which crew to run'
    )
    parser.add_argument(
        '--config',
        default='config/crewai_config.yaml',
        help='Path to the configuration file'
    )
    
    args = parser.parse_args()
    
    if args.crew == 'code-review':
        from crews.code_review import CodeReviewCrew
        crew = CodeReviewCrew()
        result = crew.crew().kickoff()
        print(result)
    elif args.crew == 'project-analysis':
        from crews.project_analysis import ProjectAnalysisCrew
        crew = ProjectAnalysisCrew()
        result = crew.crew().kickoff()
        print(result)
    elif args.crew == 'deployment-troubleshooter':
        from crews.deployment_troubleshooter import DeploymentTroubleshooterCrew
        crew = DeploymentTroubleshooterCrew()
        result = crew.crew().kickoff()
        print(result)
    elif args.crew == 'system-troubleshooter':
        from crews.system_troubleshooter import SystemTroubleshooterCrew
        crew = SystemTroubleshooterCrew()
        result = crew.crew().kickoff()
        print(result)
    elif args.crew == 'code-recommendation':
        from crews.code_recommendation import CodeRecommendationCrew
        crew = CodeRecommendationCrew()
        result = crew.crew().kickoff()
        print(result)
    elif args.crew == 'project-planning':
        from crews.project_planning import ProjectPlanningCrew
        crew = ProjectPlanningCrew()
        result = crew.crew().kickoff()
        print(result)
    elif args.crew == 'code-generation':
        from crews.code_generation import CodeGenerationCrew
        crew = CodeGenerationCrew()
        result = crew.crew().kickoff()
        print(result)
    elif args.crew == 'full-project-implementation':
        from crews.full_project_implementation import FullProjectImplementationCrew
        crew = FullProjectImplementationCrew()
        result = crew.crew().kickoff()
        print(result)
    else:
        print(f"Unknown crew: {args.crew}")
        sys.exit(1)

if __name__ == '__main__':
    main()