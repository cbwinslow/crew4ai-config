"""
Deployment Checker Tool
=======================

A tool for checking deployment configurations and identifying issues.
"""
import os
import json
import yaml
from typing import Type, Any
from pydantic import BaseModel, Field
from crewai_tools import BaseTool

class DeploymentCheckerToolSchema(BaseModel):
    """Input for DeploymentCheckerTool."""
    deployment_path: str = Field(..., description="Path to the deployment configuration directory")

class DeploymentCheckerTool(BaseTool):
    name: str = "Deployment Checker Tool"
    description: str = "Checks deployment configurations and identifies potential issues."
    args_schema: Type[BaseModel] = DeploymentCheckerToolSchema

    def _run(self, **kwargs: Any) -> Any:
        deployment_path = kwargs.get('deployment_path')
        
        if not deployment_path:
            return "Error: No deployment path provided"
        
        if not os.path.exists(deployment_path):
            return f"Error: Deployment directory not found at {deployment_path}"
        
        try:
            issues = []
            
            # Check for common deployment files
            common_files = [
                'docker-compose.yml',
                'docker-compose.yaml',
                'Dockerfile',
                'k8s/',
                'kubernetes/',
                'deployment.yaml',
                'service.yaml',
                'ingress.yaml',
                '.env',
                'config/',
                'manifests/'
            ]
            
            found_files = []
            missing_files = []
            
            for item in common_files:
                item_path = os.path.join(deployment_path, item)
                if os.path.exists(item_path):
                    found_files.append(item)
                else:
                    missing_files.append(item)
            
            # Check environment files for secrets
            env_issues = self._check_env_files(deployment_path)
            issues.extend(env_issues)
            
            # Check Docker files
            docker_issues = self._check_docker_files(deployment_path)
            issues.extend(docker_issues)
            
            # Check Kubernetes files if they exist
            k8s_issues = self._check_k8s_files(deployment_path)
            issues.extend(k8s_issues)
            
            return {
                "found_files": found_files,
                "missing_files": missing_files,
                "issues_found": len(issues),
                "issues": issues
            }
        except Exception as e:
            return f"Error checking deployment: {str(e)}"
    
    def _check_env_files(self, deployment_path):
        """Check environment files for potential issues."""
        issues = []
        
        # Look for .env files
        for root, dirs, files in os.walk(deployment_path):
            for file in files:
                if file.startswith('.env') or file == '.env':
                    env_path = os.path.join(root, file)
                    try:
                        with open(env_path, 'r') as f:
                            lines = f.readlines()
                        
                        for line_num, line in enumerate(lines, 1):
                            # Check for unquoted values with spaces
                            if '=' in line and not line.strip().startswith('#'):
                                key, value = line.split('=', 1)
                                value = value.strip()
                                if ' ' in value and not (value.startswith('"') and value.endswith('"')) and not (value.startswith("'") and value.endswith("'")):
                                    issues.append({
                                        "type": "Environment Variable Issue",
                                        "file": env_path,
                                        "line": line_num,
                                        "description": f"Unquoted value with spaces: {line.strip()}"
                                    })
                                
                                # Check for potential secrets
                                secret_keywords = ['password', 'secret', 'key', 'token', 'api']
                                if any(keyword in key.lower() for keyword in secret_keywords):
                                    issues.append({
                                        "type": "Potential Secret in File",
                                        "file": env_path,
                                        "line": line_num,
                                        "description": f"Potential secret found: {key}"
                                    })
                    except Exception as e:
                        issues.append({
                            "type": "File Read Error",
                            "file": env_path,
                            "description": f"Could not read file: {str(e)}"
                        })
        
        return issues
    
    def _check_docker_files(self, deployment_path):
        """Check Docker files for potential issues."""
        issues = []
        
        # Look for Dockerfile
        dockerfile_path = os.path.join(deployment_path, 'Dockerfile')
        if os.path.exists(dockerfile_path):
            try:
                with open(dockerfile_path, 'r') as f:
                    lines = f.readlines()
                
                for line_num, line in enumerate(lines, 1):
                    line = line.strip().upper()
                    # Check for latest tag
                    if 'FROM ' in line and ':LATEST' in line:
                        issues.append({
                            "type": "Docker Best Practice",
                            "file": dockerfile_path,
                            "line": line_num,
                            "description": "Using 'latest' tag is not recommended for production"
                        })
                    
                    # Check for root user
                    if 'USER ROOT' in line or (line.startswith('USER') and 'ROOT' in line):
                        issues.append({
                            "type": "Security Issue",
                            "file": dockerfile_path,
                            "line": line_num,
                            "description": "Running container as root user is not recommended"
                        })
            except Exception as e:
                issues.append({
                    "type": "File Read Error",
                    "file": dockerfile_path,
                    "description": f"Could not read Dockerfile: {str(e)}"
                })
        
        return issues
    
    def _check_k8s_files(self, deployment_path):
        """Check Kubernetes files for potential issues."""
        issues = []
        
        # Look for common k8s directories
        k8s_paths = [
            os.path.join(deployment_path, 'k8s'),
            os.path.join(deployment_path, 'kubernetes'),
            os.path.join(deployment_path, 'manifests')
        ]
        
        for k8s_path in k8s_paths:
            if os.path.exists(k8s_path):
                for root, dirs, files in os.walk(k8s_path):
                    for file in files:
                        if file.endswith(('.yaml', '.yml')):
                            file_path = os.path.join(root, file)
                            try:
                                with open(file_path, 'r') as f:
                                    # Try to parse as YAML
                                    content = yaml.safe_load(f)
                                
                                # Check for common k8s issues
                                if isinstance(content, dict):
                                    # Check for hardcoded secrets
                                    issues.extend(self._check_k8s_secrets(file_path, content))
                                    
                                    # Check for resource limits
                                    issues.extend(self._check_k8s_resources(file_path, content))
                            except Exception as e:
                                issues.append({
                                    "type": "File Parse Error",
                                    "file": file_path,
                                    "description": f"Could not parse YAML file: {str(e)}"
                                })
        
        return issues
    
    def _check_k8s_secrets(self, file_path, content):
        """Check Kubernetes files for hardcoded secrets."""
        issues = []
        
        def check_dict(d, path=""):
            if isinstance(d, dict):
                for key, value in d.items():
                    current_path = f"{path}.{key}" if path else key
                    
                    # Check for secret-related keys
                    secret_keywords = ['password', 'secret', 'key', 'token', 'api']
                    if any(keyword in key.lower() for keyword in secret_keywords):
                        if isinstance(value, str) and len(value) > 5:  # Likely a secret value
                            issues.append({
                                "type": "Hardcoded Secret",
                                "file": file_path,
                                "description": f"Possible hardcoded secret in {current_path}"
                            })
                    
                    # Recursively check nested dictionaries
                    if isinstance(value, dict):
                        check_dict(value, current_path)
                    elif isinstance(value, list):
                        for i, item in enumerate(value):
                            if isinstance(item, dict):
                                check_dict(item, f"{current_path}[{i}]")
        
        check_dict(content)
        return issues
    
    def _check_k8s_resources(self, file_path, content):
        """Check Kubernetes files for resource limits."""
        issues = []
        
        def check_resources(obj, obj_type):
            if isinstance(obj, dict) and 'spec' in obj:
                spec = obj['spec']
                if 'containers' in spec:
                    for i, container in enumerate(spec['containers']):
                        if 'resources' not in container:
                            issues.append({
                                "type": "Missing Resource Limits",
                                "file": file_path,
                                "description": f"{obj_type} container[{i}] ({container.get('name', 'unnamed')}) missing resource limits"
                            })
                        elif 'limits' not in container['resources']:
                            issues.append({
                                "type": "Missing Resource Limits",
                                "file": file_path,
                                "description": f"{obj_type} container[{i}] ({container.get('name', 'unnamed')}) missing resource limits"
                            })
        
        # Check different Kubernetes object types
        if isinstance(content, dict):
            if content.get('kind') == 'Deployment':
                check_resources(content, 'Deployment')
            elif content.get('kind') == 'Pod':
                check_resources(content, 'Pod')
            elif content.get('kind') == 'StatefulSet':
                check_resources(content, 'StatefulSet')
            elif content.get('kind') == 'DaemonSet':
                check_resources(content, 'DaemonSet')
        
        return issues