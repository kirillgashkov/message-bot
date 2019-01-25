"""
Add the student to the "eating" list.
"""

from typing import List
import datetime
from foodbot import bot, database
from foodbot.commands import base_command
from foodbot.constants import STUDENT_REGEX


KEYWORD = '+'


class TagEatingCommand(base_command.BaseCommand):

    def run(self, date: datetime.date, student: int, args: List[str]):
        if not args:
            database.tag(date, student, '+')
            message = f'Вы добавлены в список "Едят".'
            bot.message(student, message)
        elif 'as' == args[0] and len(args) == 2:
            recipient = args[1]
            if not STUDENT_REGEX.match(recipient):
                message = (
                    f'InputError: при использовании конструкции "as STUDENT" '
                    f'STUDENT должен быть числом и находиться в промежутке '
                    f'[1, 25].'
                )
                bot.error(student, message)
                return
            recipient = int(recipient)
            database.tag(date, recipient, '+')
            sender_message = (
                f'Ученик №{recipient} добавлен в список "Едят".'
            )
            bot.message(student, sender_message)
            recipient_message = (
                f'Ученик №{student} добавил вас в список "Едят".'
            )
            bot.message(recipient, recipient_message)
        else:
            message = (
                f'InputError: Команда "{KEYWORD}" не может принимать аргументы '
                f'отличные от "as STUDENT".'
            )
            bot.error(student, message)
