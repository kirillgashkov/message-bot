"""
A command that is intended to be inherited.
"""

from typing import List
import datetime


class BaseCommand:

    def run(self, date: datetime.date, student: int, args: List[str]):
        raise NotImplementedError
