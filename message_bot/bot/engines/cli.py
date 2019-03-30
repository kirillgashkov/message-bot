"""
CLI-based bot engine.
"""

from typing import Tuple, Optional, Callable

from message_bot.bot.engines import BaseEngine


class CLIEngine(BaseEngine):

    def message(self, recipient_id: str, m: str):
        s = f'[MSG] [{recipient_id}] {m}'
        print(s)

    def error(self, recipient_id: str, m: str, e: Optional[Exception]):
        s = f'[ERR]-[{e!r}] [{recipient_id}] {m}'
        print(s)

    def run(self, message_handler: Callable[[str, str], None]):
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
            identifier, message = split_input
            message_handler(identifier, message)


#
# Utilities
#


def split_cli_input(s: str) -> Optional[Tuple[str, str]]:
    parts = s.split(maxsplit=1)
    if not parts:
        return None
    identifier = parts[0]
    if identifier[0:2] != 'id':
        return None
    return (identifier, '') if len(parts) == 1 else (identifier, parts[1])
