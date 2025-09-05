"""
CrewAI Configuration Module
==========================

This module provides standard configurations and crews for common development tasks.
"""
import os
from pathlib import Path

# Define the base directory for crew4ai
CREW4AI_BASE_DIR = Path(__file__).parent.absolute()

# Define paths for different components
CREW_DIR = CREW4AI_BASE_DIR / "crews"
TASK_DIR = CREW4AI_BASE_DIR / "tasks"
TOOL_DIR = CREW4AI_BASE_DIR / "tools"
CONFIG_DIR = CREW4AI_BASE_DIR / "config"

# Ensure directories exist
CREW_DIR.mkdir(exist_ok=True)
TASK_DIR.mkdir(exist_ok=True)
TOOL_DIR.mkdir(exist_ok=True)
CONFIG_DIR.mkdir(exist_ok=True)

__version__ = "0.1.0"
__author__ = "Dotfiles Team"