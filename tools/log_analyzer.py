"""
Log Analyzer Tool
=================

A tool for analyzing log files and identifying errors or anomalies.
"""
import os
import re
from typing import Type, Any
from pydantic import BaseModel, Field
from crewai_tools import BaseTool

class LogAnalyzerToolSchema(BaseModel):
    """Input for LogAnalyzerTool."""
    log_file_path: str = Field(..., description="Path to the log file to analyze")
    error_patterns: list = Field(default=[], description="List of error patterns to search for")

class LogAnalyzerTool(BaseTool):
    name: str = "Log Analyzer Tool"
    description: str = "Analyzes log files and identifies errors or anomalies."
    args_schema: Type[BaseModel] = LogAnalyzerToolSchema

    def _run(self, **kwargs: Any) -> Any:
        log_file_path = kwargs.get('log_file_path')
        error_patterns = kwargs.get('error_patterns', [])
        
        if not log_file_path:
            return "Error: No log file path provided"
        
        if not os.path.exists(log_file_path):
            return f"Error: Log file not found at {log_file_path}"
        
        # Default error patterns if none provided
        if not error_patterns:
            error_patterns = [
                r"ERROR",
                r"CRITICAL",
                r"FAIL",
                r"EXCEPTION",
                r"Traceback",
                r"Timeout",
                r"Connection refused",
                r"Out of memory"
            ]
        
        try:
            error_lines = []
            warning_lines = []
            with open(log_file_path, 'r', encoding='utf-8', errors='ignore') as file:
                for line_num, line in enumerate(file, 1):
                    # Check for error patterns
                    for pattern in error_patterns:
                        if re.search(pattern, line, re.IGNORECASE):
                            error_lines.append({
                                "line_number": line_num,
                                "content": line.strip(),
                                "pattern_matched": pattern
                            })
                    
                    # Also collect warnings
                    if re.search(r"WARNING", line, re.IGNORECASE):
                        warning_lines.append({
                            "line_number": line_num,
                            "content": line.strip()
                        })
            
            return {
                "total_lines": line_num,
                "errors_found": len(error_lines),
                "warnings_found": len(warning_lines),
                "error_details": error_lines[:50],  # Limit to first 50 errors
                "warning_details": warning_lines[:50]  # Limit to first 50 warnings
            }
        except Exception as e:
            return f"Error analyzing log file: {str(e)}"