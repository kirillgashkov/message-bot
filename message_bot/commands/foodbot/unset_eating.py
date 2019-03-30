"""
Remove a student from "eating" and "not eating" lists.
"""

import datetime
from typing import Set, List

from message_bot import commands, models, bot, database


class UnsetCommand(commands.BaseCommand):
    keyword = '?'
    required_tags = {'STUDENT'}

    def run(self, date: datetime.date, person: models.Person, args: List[str]):
        if not args:
            self._unset_direct(date, person)
        elif 'as' == args[0] and len(args) == 2:
            recipient_listnum = int(args[1])
            if recipient_listnum is None:
                message = (
                    f'InputError: Команда "{self.keyword}" не может принимать '
                    f'аргументы отличные от "as STUDENT", где STUDENT является '
                    f'целым числом.'
                )
                bot.error(person.id, message)
            else:
                self._unset_indirect(date, person, recipient_listnum)
        else:
            message = (
                f'InputError: Команда "{self.keyword}" не может принимать '
                f'аргументы отличные от "as STUDENT".'
            )
            bot.error(person.id, message)

    def _unset_direct(self, date: datetime.date, person: models.Person):
        if not self.has_required_tags(person):
            bot.error(person.id, 'TagError: вы не являетесь учеником.')
            return
        database.foodbot.set_eating(person, date, None)

        message = 'Вы удалены из списков "Едят" и "Не едят".'
        bot.message(person.id, message)

    @staticmethod
    def _unset_indirect(
            date: datetime.date,
            sender: models.Person,
            recipient_listnum: int
            ):
        recipient = database.people.get_student_by_listnum(recipient_listnum)
        if not recipient:
            message = (
                f'InputError: при использовании конструкции "as STUDENT" '
                f'STUDENT должен быть целым числом и находиться в промежутке '
                f'[1, 25].'
            )
            bot.error(sender.id, message)
            return
        database.foodbot.set_eating(recipient, date, None)

        sender_listnum = sender.fields["list_number"]
        sender_message = (
            f'Ученик №{recipient_listnum} удален из списоков "Едят" и '
            f'"Не едят".'
        )
        bot.message(sender.id, sender_message)
        recipient_message = (
            f'Ученик №{sender_listnum} удалил вас из списоков "Едят" и '
            f'"Не едят".'
        )
        bot.message(recipient.id, recipient_message)