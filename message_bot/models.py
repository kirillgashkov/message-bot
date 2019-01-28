"""
Contains models shared between other models.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class Person:
    ids: Dict[str, str]
    tags: List[str] = field(default_factory=list)
    first_name: Optional[str] = None
    last_name: Optional[str] = None


@dataclass
class Student(Person):
    list_number: Optional[int] = None
    is_eating: Optional[bool] = None
    eating_default: Optional[bool] = None
