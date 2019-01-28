"""
Abstract bot engine.
"""

from abc import ABC, abstractmethod
from typing import Callable, Optional

from message_bot import models


class BaseEngine(ABC):

    @abstractmethod
    def message(self, person: models.Person, m: str):
        pass

    @abstractmethod
    def error(self, person: models.Person, m: str, e: Optional[Exception]):
        pass

    @abstractmethod
    def run(self, message_handler: Callable[[models.Person, str], None]):
        pass
