"""
Add the student to the "eating" list.
"""

from typing import List
import datetime
from foodbot import bot, database
from foodbot.commands import base_command
from foodbot.constants import DATE_FORMAT


KEYWORD = 'list'


class ListCommand(base_command.BaseCommand):

    def run(self, date: datetime.date, student: int, args: List[str]):
        if args:
            message = (
                f'InputError: Команда "{KEYWORD}" не может принимать никакие '
                f'аргументы.'
            )
            bot.error(student, message)
            return

        student_tags = database.student_tags(date)

        eating_list = list()
        not_eating_list = list()
        undefined_list = list()
        for student, tag in student_tags.items():
            if tag == '+':
                eating_list.append(_repr_student(student))
            elif tag == '-':
                not_eating_list.append(_repr_student(student))
            else:
                undefined_list.append(_repr_student(student))

        message = (
            f'Дата: {_repr_date(date)}\n'
            f'===-===-===-===-===\n'
            f'\n'
            f'Едят:\n'
            f'{_repr_list(eating_list)}\n'
            f'\n'
            f'Не едят:\n'
            f'{_repr_list(not_eating_list)}\n'
            f'\n'
            f'Не отметились:\n'
            f'{_repr_list(undefined_list)}\n'
            f'\n'
            f'===-===-===-===-===\n'
            f'# Едят: {len(eating_list)}\n'
            f'# Не едят: {len(not_eating_list)}\n'
            f'# Не отметились: {len(undefined_list)}\n'
        )
        bot.message(student, message)


#
# Utilities
#


def _repr_student(student: int) -> str:
    return f'- {student}: {database.student_name(student)}'


def _repr_date(date: datetime.date) -> str:
    return date.strftime(DATE_FORMAT)


def _repr_list(strings: List[str]) -> str:
    return '\n'.join(strings)
