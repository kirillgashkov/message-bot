"""
Parses input message.
"""

from typing import Optional, Tuple, List
import bot
from constants import DOMAIN_NAME


def parse_message(student: int, msg: str) -> Optional[Tuple[str, List[str]]]:
    if not msg:
        context = {'msg': msg}
        message = (
            f'InputError: пустое сообщение.'
        )
        bot.error(student, message, context)
        return None
    words = msg.split()
    if words[0] != DOMAIN_NAME:
        context = {'msg': msg}
        message = (
            f'InputError: введенного вами домена команд (первого слова) '
            f'не существует.'
        )
        bot.error(student, message, context)
        return None
    if len(words) < 2:
        context = {'msg': msg}
        message = (
            f'InputError: вы не ввели команду.'
        )
        bot.error(student, message, context)
        return None
    command = words[1]
    args = words[1:]
    return command, args
