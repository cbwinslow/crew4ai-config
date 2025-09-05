"""
Simplified File Reader Tool
==========================

A tool for reading and analyzing code files.
"""
import os
from typing import Type, Any
from pydantic import BaseModel, Field
from crewai_tools import BaseTool

class FileReaderToolSchema(BaseModel):
    """Input for FileReaderTool."""
    file_path: str = Field(..., description="Path to the file to read")

class FileReaderTool(BaseTool):
    name: str = "File Reader Tool"
    description: str = "Reads and analyzes code files for review purposes."
    args_schema: Type[BaseModel] = FileReaderToolSchema

    def _run(self, **kwargs: Any) -> Any:
        file_path = kwargs.get('file_path')
        if not file_path:
            return "Error: No file path provided"
        
        if not os.path.exists(file_path):
            return f"Error: File not found at {file_path}"
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            return content
        except Exception as e:
            return f"Error reading file: {str(e)}"