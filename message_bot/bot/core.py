"""
Bot module's API.
"""

from typing import Callable, Optional

from message_bot.bot.engines import BaseEngine


#
# Engine
#


engine: BaseEngine


def set_engine(new_engine: BaseEngine):
    global engine
    engine = new_engine


#
# API
#


def message(recipient_id: str, m: str):
    engine.message(recipient_id, m)


def error(recipient_id: str, m: str, e: Optional[Exception] = None):
    engine.error(recipient_id, m, e)


def run(message_handler: Callable[[str, str], None]):
    engine.run(message_handler)
