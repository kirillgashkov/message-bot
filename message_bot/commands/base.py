"""
Abstract command.
"""

import abc
import datetime
from typing import List, Set

from message_bot import models


class BaseCommand(abc.ABC):

    @property
    @abc.abstractmethod
    def keyword(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def required_tags(self) -> Set[str]:
        pass

    @abc.abstractmethod
    def run(self, date: datetime.date, person: models.Person, args: List[str]):
        pass

    def has_required_tags(self, person: models.Person) -> bool:
        return self.required_tags.issubset(person.tags)
