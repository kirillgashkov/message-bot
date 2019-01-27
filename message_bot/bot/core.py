"""
'bot' module's core.
"""

from typing import Callable
from message_bot import models
from message_bot.bot.engines import BaseEngine


engine: BaseEngine = None


def set_engine(new_engine: BaseEngine):
    global engine
    engine = new_engine


#
# API
#


def message(person: models.Person , m: str):
    engine.message(person, m)


def error(person: models.Person, m: str, e: Exception):
    engine.error(person, m, e)


def run(message_handler: Callable[[models.Person, str], None]):
    engine.run(message_handler)
