"""
This module defines the data models for the Todo application.
"""

from dataclasses import dataclass

@dataclass
class Task:
    """Represents a single task in the aplication."""
    id: int
    title: str
    description: str
    status: str = "incomplete"
