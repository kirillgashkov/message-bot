"""
Show help message.
"""

import datetime
from typing import Set, List

from message_bot import commands, models, bot
from message_bot.commands import foodbot


class ShowHelpCommand(commands.BaseCommand):
    keyword = 'help'
    required_tags = set()

    def run(self, date: datetime.date, person: models.Person, args: List[str]):
        if args:
            message = (
                f'InputError: Команда "{self.keyword}" не может принимать '
                f'никакие аргументы.'
            )
            bot.error(person.id, message)
            return

        message = (
            f'Введите\n'
            f'- "{foodbot.SUPER_COMMAND} {foodbot.SetEatingCommand.keyword}", '
            f'чтобы попасть в список "Едят";\n'
            f'- "{foodbot.SUPER_COMMAND} {foodbot.SetNotEatingCommand.keyword}", '
            f'чтобы попасть в список "Не едят";\n'
            f'- "{foodbot.SUPER_COMMAND} {foodbot.UnsetCommand.keyword}", '
            f'чтобы удалить себя из обоих списков;\n'
            f'- "{foodbot.SUPER_COMMAND} {foodbot.ShowListCommand.keyword}", '
            f'чтобы получить списки "Едят" и "Не едят".\n'
            f'- "{foodbot.SUPER_COMMAND} {foodbot.ShowHelpCommand.keyword}", '
            f'чтобы вывести это сообщение."\n'
            f'\n'
            f'Добавьте "as STUDENT" к концу команды, чтобы выполнить ее от лица '
            f'другого ученика. STUDENT - это целое число в диапазоне [1, 25].'
        )
        bot.message(person.id, message)
