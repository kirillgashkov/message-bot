"""
Outputs help message.
"""

from typing import List
import datetime
from foodbot import bot
from foodbot.commands import (
    base_command,
    list_command,
    tag_eating_command,
    tag_noteating_command,
    untag_command,
)
from foodbot.constants import DOMAIN_NAME


KEYWORD = 'help'


class HelpCommand(base_command.BaseCommand):

    def run(self, date: datetime.date, student: int, args: List[str]):
        if args:
            message = (
                f'InputError: Команда "{KEYWORD}" не может принимать никакие '
                f'аргументы.'
            )
            bot.error(student, message)
            return
        message = (
            f'Введите\n'
            f'- "{DOMAIN_NAME} {tag_eating_command.KEYWORD}", '
            f'чтобы попасть в список "Едят";\n'
            f'- "{DOMAIN_NAME} {tag_noteating_command.KEYWORD}", '
            f'чтобы попасть в список "Не едят";\n'
            f'- "{DOMAIN_NAME} {untag_command.KEYWORD}", '
            f'чтобы удалить себя из обоих списков;\n'
            f'- "{DOMAIN_NAME} {list_command.KEYWORD}", '
            f'чтобы получить списки "Едят" и "Не едят".'
            f'- "{DOMAIN_NAME} {KEYWORD}", '
            f'чтобы вывести это сообщение."\n'
            f'\n'
            f'Добавьте "as STUDENT" к концу команды, чтобы выполнить ее от лица '
            f'другого ученика. STUDENT - это число в диапазоне [1, 25].'
        )
        bot.message(student, message)
