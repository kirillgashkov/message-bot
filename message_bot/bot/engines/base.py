"""
Bot's base engine that is indented to be inherited.
"""

from typing import Callable
from message_bot import models


class BaseEngine:

    def message(self, person: models.Person, m: str):
        raise NotImplementedError

    def error(self, person: models.Person, m: str, e: Exception):
        raise NotImplementedError

    def run(self, message_handler: Callable[[models.Person, str], None]):
        raise NotImplementedError
