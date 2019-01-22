"""
Add the student to the "not eating" list.
"""

from typing import List
import datetime
import base_command
import bot
import database
from constants import STUDENT_REGEX


KEYWORD = '-'


class TagNotEatingCommand(base_command.BaseCommand):

    def run(self, date: datetime.date, student: int, args: List[str]):
        if not args:
            database.tag(date, student, '-')
            message = f'Вы добавлены в список "Не едят".'
            bot.message(student, message)
        elif 'as' == args[0] and len(args) == 2:
            recipient = args[1]
            if not STUDENT_REGEX.match(recipient):
                context = {'date': date, 'student': student, 'args': args}
                message = (
                    f'InputError: при использовании конструкции "as STUDENT" '
                    f'STUDENT должен быть числом и находиться в промежутке '
                    f'[1, 25].'
                )
                bot.error(student, message, context)
                return
            recipient = int(recipient)
            database.tag(date, recipient, '-')
            sender_message = (
                f'Ученик №{recipient} добавлен в список "Не едят".'
            )
            bot.message(student, sender_message)
            recipient_message = (
                f'Ученик №{student} добавил вас в список "Не едят".'
            )
            bot.message(recipient, recipient_message)
        else:
            context = {'date': date, 'student': student, 'args': args}
            message = (
                f'InputError: Команда "{KEYWORD}" не может принимать аргументы '
                f'отличные от "as STUDENT".'
            )
            bot.error(student, message, context)
