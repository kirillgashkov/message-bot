"""
Outputs help message.
"""

from typing import List
import datetime
import base_command
import bot
from commands import (
    list_command,
    tag_eating_command,
    tag_noteating_command,
    untag_command,
)
from constants import DOMAIN_NAME


KEYWORD = 'help'


class HelpCommand(base_command.BaseCommand):

    def run(self, date: datetime.date, student: int, args: List[str]):
        if args:
            context = {'date': date, 'student': student, 'args': args}
            message = (
                f'InputError: Команда "{KEYWORD}" не может принимать никакие '
                f'аргументы.'
            )
            bot.error(student, message, context)
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
