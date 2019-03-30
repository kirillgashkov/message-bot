
from message_bot.commands.foodbot.set_eating import SetEatingCommand
from message_bot.commands.foodbot.set_not_eating import SetNotEatingCommand
from message_bot.commands.foodbot.unset_eating import UnsetCommand
from message_bot.commands.foodbot.show_list import ShowListCommand
from message_bot.commands.foodbot.show_help import ShowHelpCommand


SUPER_COMMAND = 'food'

commands = {
    SetEatingCommand.keyword: SetEatingCommand,
    SetNotEatingCommand.keyword: SetNotEatingCommand,
    UnsetCommand.keyword: UnsetCommand,
    ShowListCommand.keyword: ShowListCommand,
    ShowHelpCommand.keyword: ShowHelpCommand,
}