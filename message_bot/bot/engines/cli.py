"""
CLI-based bot engine.
"""

from typing import Tuple, Optional, Callable

from message_bot import bot, models, container
from message_bot.constants import HELP_OFFER_ON_ERROR


class CLIEngine(bot.engines.BaseEngine):

    def message(self, person: models.Person, m: str):
        s = f'[MSG] [{person.id}] {m}'
        print(s)

    def error(self, person: models.Person, m: str, e: Optional[Exception]):
        s = f'[ERR]-[{e!r}] [{person.id}] {m} {HELP_OFFER_ON_ERROR}'
        print(s)

    def run(self, message_handler: Callable[[models.Person, str], None]):
        while True:
            s = input('> ')
            split_input = split_cli_input(s)
            if not split_input:
                print(
                    'MessageBotError: received cli message either is empty '
                    'or specifies sender incorrectly (prefix your message '
                    'with `id` and any sequence of characters as one word).'
                )
                continue
            person, message = split_input
            message_handler(person, message)


#
# Utilities
#


def split_cli_input(s: str) -> Optional[Tuple[models.Person, str]]:
    parts = s.split(maxsplit=1)
    if not parts:
        return None
    identifier = parts[0]
    if identifier[0:2] != 'id':
        return None
    person = container.person_for_id(parts[0])
    return (person, '') if len(parts) == 1 else (person, parts[1])
