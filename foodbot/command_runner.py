"""
Runs a command by keyword passing kwargs.
"""

from typing import Optional
import datetime
import bot
import base_command
from commands import (
    list_command,
    tag_eating_command,
    tag_noteating_command,
    untag_command,
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
    list_command.KEYWORD: list_command.ListCommand,
    tag_eating_command.KEYWORD: tag_eating_command.TagEatingCommand,
    tag_noteating_command.KEYWORD: tag_noteating_command.TagNotEatingCommand,
    untag_command.KEYWORD: untag_command.UntagCommand,
    help_command.KEYWORD: help_command.HelpCommand,
}
