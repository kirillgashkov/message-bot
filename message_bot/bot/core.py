"""
Bot module's API.
"""

from typing import Callable, Optional

from message_bot import bot, models


#
# Engine
#


engine: bot.engines.BaseEngine


def set_engine(new_engine: bot.engines.BaseEngine):
    global engine
    engine = new_engine


#
# API
#


def message(person: models.Person, m: str):
    engine.message(person, m)


def error(person: models.Person, m: str, e: Optional[Exception] = None):
    engine.error(person, m, e)


def run(message_handler: Callable[[models.Person, str], None]):
    engine.run(message_handler)
