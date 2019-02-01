"""
Contains models shared between other models.
"""

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Person:
    id: str
    tags: List[str] = field(default_factory=list)


@dataclass
class Student(Person):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    list_number: Optional[int] = None
    is_eating: Optional[bool] = None
    eating_default: Optional[bool] = None
