"""
Bot's engine that interacts with the user via command line.
"""

from typing import Tuple, Optional, Callable
from message_bot import models
from message_bot.bot.engines.base import BaseEngine
from message_bot.constants import HELP_OFFER_ON_ERROR


class CLIEngine(BaseEngine):

    def message(self, person: models.Person, m: str):
        id_ = person.ids.get('cli')
        if not id_:
            print(
                'MessageBotError: person targeted to receive message does '
                'not have CLI id.'
            )
            return
        print(f'[{id_}] {m}')

    def error(self, person: models.Person, m: str, e: Exception):
        formatted_m = m + ' ' + HELP_OFFER_ON_ERROR
        id_ = person.ids.get('cli')
        if not id_:
            print(
                'MessageBotError: person targeted to receive message does '
                'not have CLI id.'
            )
            return
        print(f'[{id_}] [!] {formatted_m} {e!r}')

    def run(self, message_handler: Callable[[models.Person, str], None]):
        for m in cli_listen():
            extracted = extract_person_from_message(m)
            if not extracted:
                continue
            sender, new_m = extracted
            message_handler(sender, new_m)


#
# Utilities
#


def extract_person_from_message(m: str) -> Optional[Tuple[models.Person, str]]:
    parts = m.split(maxsplit=1)
    if not parts:
        print(
            'MessageBotError: input string does not contain sender\'s id.'
        )
        return None
    person = models.Person.for_id('cli', parts[0])
    return (person, '') if len(parts) == 1 else (person, parts[1])


def cli_listen():
    while True:
        s = input()
        yield s
