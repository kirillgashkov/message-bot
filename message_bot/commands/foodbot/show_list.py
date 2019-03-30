"""
Show "eating" and "not eating" lists.
"""

import datetime
from typing import List

from message_bot import commands, models, bot, database
from message_bot.constants import DATE_FORMAT


class ShowListCommand(commands.BaseCommand):
    keyword = 'list'
    required_tags = set()

    def run(self, date: datetime.date, person: models.Person, args: List[str]):
        if args:
            message = (
                f'InputError: Команда "{self.keyword}" не может принимать '
                f'никакие аргументы.'
            )
            bot.error(person.id, message)
            return

        eatings = database.foodbot.get_eatings(date)

        eating_list = list()
        not_eating_list = list()
        unset_list = list()

        for student, eating in eatings.items():
            if eating is None:
                unset_list.append(_repr_student(student))
            elif eating:
                eating_list.append(_repr_student(student))
            else:
                not_eating_list.append(_repr_student(student))

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
            f'{_repr_list(unset_list)}\n'
            f'\n'
            f'===-===-===-===-===\n'
            f'# Едят: {len(eating_list)}\n'
            f'# Не едят: {len(not_eating_list)}\n'
            f'# Не отметились: {len(unset_list)}\n'
        )
        bot.message(person.id, message)


#
# Utilities
#


def _repr_student(student: models.Person) -> str:
    student_listnum = student.fields['list_number']
    student_name = student.fields['name']
    return f'- {student_listnum}: {student_name}'


def _repr_date(date: datetime.date) -> str:
    return date.strftime(DATE_FORMAT)


def _repr_list(strings: List[str]) -> str:
    return '\n'.join(strings)
