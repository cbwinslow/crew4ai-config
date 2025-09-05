"""
Documentation Generator Tool
============================

A tool for generating project documentation.
"""
import os
from typing import Type, Any
from pydantic import BaseModel, Field
from crewai_tools import BaseTool

class DocumentationGeneratorToolSchema(BaseModel):
    """Input for DocumentationGeneratorTool."""
    project_path: str = Field(..., description="Path to the project directory")
    doc_type: str = Field(..., description="Type of documentation to generate (README, API, technical, user)")

class DocumentationGeneratorTool(BaseTool):
    name: str = "Documentation Generator Tool"
    description: str = "Generates project documentation of various types."
    args_schema: Type[BaseModel] = DocumentationGeneratorToolSchema

    def _run(self, **kwargs: Any) -> Any:
        project_path = kwargs.get('project_path')
        doc_type = kwargs.get('doc_type', 'README')
        
        if not project_path:
            return "Error: No project path provided"
        
        if not os.path.exists(project_path):
            return f"Error: Project directory not found at {project_path}"
        
        try:
            # Gather project information
            project_info = self._gather_project_info(project_path)
            
            # Generate documentation based on type
            if doc_type.upper() == 'README':
                return self._generate_readme(project_info)
            elif doc_type.upper() == 'API':
                return self._generate_api_docs(project_info)
            elif doc_type.upper() == 'TECHNICAL':
                return self._generate_technical_docs(project_info)
            elif doc_type.upper() == 'USER':
                return self._generate_user_docs(project_info)
            else:
                return f"Unknown documentation type: {doc_type}"
        except Exception as e:
            return f"Error generating documentation: {str(e)}"
    
    def _gather_project_info(self, project_path):
        """Gather basic information about the project."""
        info = {
            "name": os.path.basename(project_path),
            "path": project_path,
            "files": [],
            "directories": [],
            "main_files": []
        }
        
        for item in os.listdir(project_path):
            item_path = os.path.join(project_path, item)
            if os.path.isfile(item_path):
                info["files"].append(item)
                # Identify main files
                if item.lower() in ['main.py', 'app.py', 'index.js', 'package.json', 'requirements.txt']:
                    info["main_files"].append(item)
            elif os.path.isdir(item_path):
                info["directories"].append(item)
        
        return info
    
    def _generate_readme(self, project_info):
        """Generate a README.md file."""
        readme_content = f"""# {project_info['name']}

## Project Overview

Brief description of what this project does and what problem it solves.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

Instructions on how to install and set up the project:

```bash
# Clone the repository
git clone <repository-url>

# Navigate to the project directory
cd {project_info['name']}

# Install dependencies
# Add specific installation commands here
```

## Usage

Instructions on how to use the project:

```bash
# Example usage commands
```

## Features

- Feature 1
- Feature 2
- Feature 3

## Contributing

Guidelines for contributing to the project:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

Information about the project's license.

---
*This README was automatically generated.*
"""
        return readme_content
    
    def _generate_api_docs(self, project_info):
        """Generate API documentation."""
        return f"""# API Documentation for {project_info['name']}

## Overview

Documentation for the APIs provided by this project.

## Endpoints

Detailed information about each API endpoint would go here.

## Authentication

Information about API authentication methods.

## Rate Limiting

Details about API rate limits if applicable.

## Error Codes

List of possible error codes and their meanings.

## Examples

Example requests and responses for each endpoint.
"""
    
    def _generate_technical_docs(self, project_info):
        """Generate technical documentation."""
        return f"""# Technical Documentation for {project_info['name']}

## System Architecture

Description of the system architecture.

## Components

Detailed information about each component in the system.

## Data Flow

Description of how data flows through the system.

## Database Schema

Information about the database structure if applicable.

## Configuration

Details about system configuration options.

## Deployment

Instructions for deploying the system.
"""
    
    def _generate_user_docs(self, project_info):
        """Generate user documentation."""
        return f"""# User Guide for {project_info['name']}

## Getting Started

Instructions for new users to get started with the project.

## User Interface

Description of the user interface and how to navigate it.

## Features

Detailed information about each feature from a user perspective.

## Troubleshooting

Common issues users might encounter and how to resolve them.

## FAQ

Frequently asked questions and their answers.
"""