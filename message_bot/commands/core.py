"""
Provides API for running commands.
"""

import datetime
from typing import Optional

from message_bot import bot, commands, models


def run_command(
        super_command: str, command: str,
        date: datetime.date, person: models.Person, args: list
        ):
    cmd = get_command(super_command, command)
    if not cmd:
        message = f'InputError: введенной вами команды не существует.'
        bot.error(person.id, message)
        return
    cmd.run(date, person, args)


#
# Command dispatcher
#


_all_command_classes = {
    commands.foodbot.SUPER_COMMAND: commands.foodbot.commands
}


def get_command(
        super_command: str,
        command: str
        ) -> Optional[commands.BaseCommand]:
    command_classes = _all_command_classes.get(super_command)
    command_class = command_classes.get(command) if command_classes else None
    return command_class() if command_class else None
