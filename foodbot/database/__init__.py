"""
Provides API for interacting with database.
"""

from typing import Dict
import datetime


#
# Reading
#


def student_tags(date: datetime.date) -> Dict[int, str]:
    pass


def student_name(student: int) -> str:
    pass


def student_id(student: int) -> str:
    pass


#
# Writing
#


def tag(date: datetime.date, student: int, value: str):
    pass


def untag(date: datetime.date, student: int):
    pass
