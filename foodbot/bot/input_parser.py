"""
Parses input message.
"""

from typing import Optional, Tuple, List
from foodbot import bot
from foodbot.constants import DOMAIN_NAME


def parse_message(student: int, msg: str) -> Optional[Tuple[str, List[str]]]:
    if not msg:
        message = f'InputError: пустое сообщение.'
        bot.error(student, message)
        return None
    words = msg.split()
    if words[0] != DOMAIN_NAME:
        message = (
            f'InputError: введенного вами домена команд (первого слова) '
            f'не существует.'
        )
        bot.error(student, message)
        return None
    if len(words) < 2:
        message = f'InputError: вы не ввели команду.'
        bot.error(student, message)
        return None
    command = words[1]
    args = words[1:]
    return command, args
