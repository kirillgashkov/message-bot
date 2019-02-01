"""
Contains models shared between other models.
"""

from dataclasses import dataclass
from typing import List, Dict


@dataclass
class Person:
    id: str
    tags: List[str]
    fields: Dict[str, str]
