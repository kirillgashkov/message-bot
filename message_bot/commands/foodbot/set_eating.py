"""
Add a student to the "eating" list.
"""

import datetime
from typing import Set, List

from message_bot import commands, models, bot, database


class SetEatingCommand(commands.BaseCommand):

    @property
    def keyword(self) -> str:
        return '+'

    @property
    def required_tags(self) -> Set[str]:
        return {'STUDENT'}

    def run(self, date: datetime.date, person: models.Person, args: List[str]):
        if not args:
            self._set_eating_direct(date, person)
        elif 'as' == args[0] and len(args) == 2:
            recipient_listnum = args[1]
            self._set_eating_indirect(date, person, recipient_listnum)
        else:
            message = (
                f'InputError: Команда "{self.keyword}" не может принимать '
                f'аргументы отличные от "as STUDENT".'
            )
            bot.error(person, message)

    def _set_eating_direct(self, date, person):
        if not self.has_required_tags(person):
            bot.error(person, 'TagError: вы не являетесь учеником.')
        database.foodbot.set_eating(person, date, True)

        message = 'Вы добавлены в список "Едят".'
        bot.message(person, message)

    @staticmethod
    def _set_eating_indirect(date, sender, recipient_listnum):
        recipient = database.people.get_student_by_listnum(recipient_listnum)
        if not recipient:
            message = (
                f'InputError: при использовании конструкции "as STUDENT" '
                f'STUDENT должен быть целым числом и находиться в промежутке '
                f'[1, 25].'
            )
            bot.error(sender, message)
            return
        database.foodbot.set_eating(recipient, date, True)

        sender_listnum = sender.fields["list_number"]
        sender_message = (
            f'Ученик №{recipient_listnum} добавлен в список "Едят".'
        )
        bot.message(sender, sender_message)
        recipient_message = (
            f'Ученик №{sender_listnum} добавил вас в список "Едят".'
        )
        bot.message(recipient, recipient_message)
