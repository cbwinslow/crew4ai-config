#!/usr/bin/env python3
"""
Example: Code Review Crew Usage
===============================

This script demonstrates how to use the Code Review Crew to review a code file.
"""

import sys
from pathlib import Path

# Add the crew4ai directory to the Python path
sys.path.insert(0, str(Path(__file__).parent))

from crews.code_review import CodeReviewCrew

def main():
    # Create and run the code review crew
    crew = CodeReviewCrew()
    result = crew.crew().kickoff()
    
    print("Code Review Results:")
    print("====================")
    print(result)

if __name__ == '__main__':
    main()