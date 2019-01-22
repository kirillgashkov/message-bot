"""
Provides API for reading from and writing to foodbot's database.
"""

from typing import Dict
import datetime


#
# Writing
#


def tag(date: datetime.date, student: int, value: str):
    pass


def untag(date: datetime.date, student: int):
    pass


#
# Reading
#


def student_tags(date: datetime.date) -> Dict[int, str]:
    pass


def student_names() -> Dict[int, str]:
    pass


def student_ids() -> Dict[int, str]:
    pass
