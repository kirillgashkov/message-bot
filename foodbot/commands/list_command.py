"""
Add the student to the "eating" list.
"""

from typing import List, Dict
import datetime
import base_command
import bot
import database
from constants import DATE_FORMAT


KEYWORD = 'list'


class ListCommand(base_command.BaseCommand):

    def run(self, date: datetime.date, student: int, args: List[str]):
        if args:
            context = {'date': date, 'student': student, 'args': args}
            message = (
                f'InputError: Команда "{KEYWORD}" не может принимать никакие '
                f'аргументы.'
            )
            bot.error(student, message, context)
            return

        student_tags = database.student_tags(date)
        student_names = database.student_names()

        eating_list = list()
        not_eating_list = list()
        undefined_list = list()
        for student, tag in student_tags.items():
            if tag == '+':
                eating_list.append(_repr_student(student, student_names))
            elif tag == '-':
                not_eating_list.append(_repr_student(student, student_names))
            else:
                undefined_list.append(_repr_student(student, student_names))

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


def _repr_student(student: int, student_names: Dict[int, str]) -> str:
    return f'- {student}: {student_names[student]}'


def _repr_date(date: datetime.date) -> str:
    return date.strftime(DATE_FORMAT)


def _repr_list(strings: List[str]) -> str:
    return '\n'.join(strings)
