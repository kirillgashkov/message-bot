"""
Provides API for running commands.
"""


from typing import Optional
import datetime
from foodbot import bot
from foodbot.commands import (
    base_command,
    tag_eating_command,
    tag_noteating_command,
    untag_command,
    list_command,
    help_command,
)


def run_command(keyword: str, date: datetime.date, student: int, args: list):
    cmd = command(keyword)
    if not cmd:
        context = {
            'keyword': keyword, 'date': date,
            'student': student, 'args': args,
        }
        message = f'InputError: введенной вами команды не существует.'
        bot.error(student, message, context)
        return
    cmd.run(date, student, args)


#
# Command dispatcher
#


def command(keyword: str) -> Optional[base_command.BaseCommand]:
    command_class = _command_classes.get(keyword)
    return command_class() if command_class else None


_command_classes = {
    tag_eating_command.KEYWORD: tag_eating_command.TagEatingCommand,
    tag_noteating_command.KEYWORD: tag_noteating_command.TagNotEatingCommand,
    untag_command.KEYWORD: untag_command.UntagCommand,
    list_command.KEYWORD: list_command.ListCommand,
    help_command.KEYWORD: help_command.HelpCommand,
}
