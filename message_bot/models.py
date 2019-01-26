"""
Contains models shared between other models.
"""

from typing import Dict, List


class Person:

    def __init__(self, **ids: str):
        self.ids: Dict[str, str] = ids
        self.tags: List[str] = list()
        self.first_name: str = ''
        self.last_name: str = ''


class Student:

    def __init__(self, **ids: str):
        super().__init__(**ids)
        self.list_number = None
        self.should_order = None
        self.should_order_default = None
